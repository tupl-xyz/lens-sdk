# Lens Reasoning SDK

A Python SDK for the Lens Reasoning System focused on query processing and reasoning capabilities. For steering directives and advanced reasoning management, use the integrated Lens UI overlay.

## Installation

### Option 1: Install from Source (Recommended)

```bash
# Clone or navigate to the SDK directory
cd /path/to/lens-sdk

# Install in editable mode
pip install -e .
```

### Option 2: Install from PyPI (if published)

```bash
pip install lens-reasoning-sdk
```

### Prerequisites

- Python 3.8+
- A running Lens Reasoning System backend server (default: `http://localhost:8001`)

## Testing Your Installation

Run the included test script to verify everything works:

```bash
# Navigate to the SDK directory
cd /path/to/lens-sdk

# Run the test script
python test_sdk.py
```

Expected output:
```
Testing LensQueryProcessor...
✅ Query processed successfully
Contract ID: [contract-id]
Answer: [reasoning result...]

🎯 Steering Directives Management:
Contract ID: [contract-id]

To add steering directives and modify reasoning:
1. Press Ctrl/Cmd + Shift + L to open the Lens UI overlay
2. Navigate to your contract using ID: [contract-id]
3. Add steering directives through the visual interface
4. Re-run reasoning with your custom directives

✅ SDK test completed - Use the UI for advanced steering features!
```

## SDK Overview

This SDK provides:

1. **LensQueryProcessor** - For query processing and reasoning
2. **Lens UI Integration** - For steering directives management through visual overlay (Ctrl/Cmd + Shift + L)

## Quick Start

### Query Processing

Use `LensQueryProcessor` for reasoning tasks:

```python
import sys
import os

# Add SDK directory to path (if not installed via pip)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from query_processor import LensQueryProcessor
from exceptions import ProcessingError

try:
    # Initialize the query processor
    processor = LensQueryProcessor("http://localhost:8001")

    # Process a query
    result = processor.process_query("What are the implications of AI in healthcare?")

    print(f"Answer: {result['final_answer']}")
    print(f"Confidence: {result['confidence_overall']}")
    print(f"Contract ID: {result['contract_id']}")

    # For steering directives, use the UI overlay
    print(f"\nTo modify reasoning with steering directives:")
    print(f"Press Ctrl/Cmd + Shift + L and navigate to contract: {result['contract_id']}")

except ProcessingError as e:
    print(f"Processing failed: {e}")
finally:
    processor.close()
```

### Steering Directives Management

Instead of programmatic steering directives, use the **Lens UI Overlay** for a visual, interactive experience:

1. **Run your query** using the SDK above
2. **Note the Contract ID** from the result
3. **Press `Ctrl/Cmd + Shift + L`** to open the Lens UI overlay
4. **Navigate to your contract** using the Contract ID
5. **Add steering directives** through the visual interface
6. **Re-run reasoning** with your custom directives applied

#### Benefits of UI-Based Steering:
- 🎯 **Visual Interface** - See reasoning steps and add directives intuitively
- 🔄 **Real-time Feedback** - Immediate preview of directive impact
- 📊 **Advanced Analytics** - Detailed reasoning trace visualization
- ⚡ **Quick Iteration** - Easily modify and test different steering approaches

## API Reference

### LensQueryProcessor

#### Constructor
```python
LensQueryProcessor(base_url="http://localhost:8001", timeout=300)
```

#### Methods

##### `process_query(query, **kwargs)`
Process a query through the reasoning system.

**Parameters:**
- `query` (str): The question or problem to reason about
- `initial_docs` (List[str], optional): Initial documents to include
- `reasoning_mode` (str): "comprehensive", "focused", or "policy_guided"
- `workflow_id` (str, optional): Workflow identifier
- `workflow_name` (str, optional): Workflow name

**Returns:** Dictionary with reasoning results

##### `get_contract(contract_id)`
Get complete contract details.

##### `get_reasoning_trace(contract_id)`
Get detailed step-by-step reasoning trace.

##### `list_contracts(workflow_id=None, limit=20)`
List existing contracts with optional filtering.

### Lens UI Overlay Integration

The SDK integrates with the Lens UI overlay for advanced steering directives management:

#### Opening the UI Overlay
```python
# After getting a contract_id from your query
print(f"Contract ID: {contract_id}")
print("Press Ctrl/Cmd + Shift + L to open Lens UI overlay")
```

#### UI Features Available:
- **Contract Browser** - View all your reasoning contracts
- **Reasoning Trace Viewer** - Detailed step-by-step analysis
- **Steering Directive Editor** - Visual interface for adding directives
- **Re-run Controls** - Apply steering and re-execute reasoning
- **Impact Analysis** - See how directives changed the reasoning

#### Keyboard Shortcuts:
- `Ctrl/Cmd + Shift + L` - Open/close Lens UI overlay
- Navigate to your contract using the Contract ID from SDK results

## Complete Working Example

Copy this exact code to test the SDK with UI integration:

```python
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from query_processor import LensQueryProcessor
from exceptions import ProcessingError

def test_sdk_with_ui():
    processor = None

    try:
        # Initialize the SDK
        processor = LensQueryProcessor("http://localhost:8001")

        # Step 1: Process a reasoning query
        result = processor.process_query(
            query="How can we reduce carbon emissions in urban transportation?",
            reasoning_mode="comprehensive"
        )

        contract_id = result['contract_id']
        print(f"✅ Query processed successfully!")
        print(f"Contract ID: {contract_id}")
        print(f"Initial answer: {result['final_answer'][:100]}...")

        # Step 2: Get reasoning trace for reference
        trace = processor.get_reasoning_trace(contract_id)
        print(f"Reasoning steps: {len(trace['steps'])}")

        # Step 3: Provide UI instructions for steering
        print(f"\n🎯 Next Steps - Use Lens UI for Steering:")
        print(f"1. Press Ctrl/Cmd + Shift + L to open the Lens UI overlay")
        print(f"2. Navigate to contract: {contract_id}")
        print(f"3. Review the {len(trace['steps'])} reasoning steps")
        print(f"4. Add steering directives through the visual interface")
        print(f"5. Re-run reasoning with your custom directives")

        print(f"\n✅ SDK test completed - Use the UI overlay for advanced features!")

    except ProcessingError as e:
        print(f"❌ Processing failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        if processor:
            processor.close()

if __name__ == "__main__":
    test_sdk_with_ui()
```

Save this as `sdk_ui_test.py` and run with: `python sdk_ui_test.py`

## Running from Any Directory

To use this SDK from anywhere on your system:

### Method 1: Install Globally
```bash
# Navigate to SDK directory
cd /Users/aashishbharadwaj/lens/sdk/lens-sdk

# Install globally
pip install -e .

# Now you can use from anywhere
python -c "
from query_processor import LensQueryProcessor
processor = LensQueryProcessor('http://localhost:8001')
print('✅ Global installation works!')
processor.close()
"
```

### Method 2: Add to Python Path
```python
import sys
import os

# Add the SDK directory to your path
sdk_path = '/Users/aashishbharadwaj/lens/sdk/lens-sdk'
if sdk_path not in sys.path:
    sys.path.insert(0, sdk_path)

# Now import and use
from query_processor import LensQueryProcessor
from exceptions import ProcessingError

# Get contract ID, then use Ctrl/Cmd + Shift + L for steering
```

### Method 3: Copy Test Files
Copy `test_sdk.py` to any directory and it will work without modification.

## Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**: Make sure your backend server is running on `http://localhost:8001`
2. **Import Errors**: Use the exact import patterns shown above
3. **Connection Refused**: Verify backend server is accessible

### Verify Installation:
```bash
# Test basic functionality
cd /Users/aashishbharadwaj/lens/sdk/lens-sdk
python test_sdk.py
```

## Requirements

- Python 3.8+
- httpx>=0.25.0
- pydantic>=2.0.0
- Access to a running Lens Reasoning System backend server
- Lens UI overlay installed for steering directives (Ctrl/Cmd + Shift + L)

## Server Configuration

Ensure your Lens Reasoning System backend is:
- Running on `http://localhost:8001` (or modify base_url in code)
- Accepting HTTP requests
- Properly configured for reasoning operations

## UI Overlay Setup

The Lens UI overlay provides the visual interface for steering directives:
- **Keyboard Shortcut**: `Ctrl/Cmd + Shift + L`
- **Features**: Contract browser, reasoning trace viewer, steering directive editor
- **Integration**: Seamlessly works with Contract IDs from the SDK

## License

MIT License