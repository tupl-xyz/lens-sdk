# Lens Reasoning SDK

A Python SDK for the Lens Reasoning System that provides two focused SDKs for AI-powered reasoning capabilities.

## Installation

```bash
pip install lens-reasoning-sdk
```

## Two Focused SDKs

This SDK provides two specialized interfaces:

1. **LensQueryProcessor** - For query processing and reasoning
2. **LensSteeringManager** - For steering directive management and guided reasoning

## Quick Start

### 1. Query Processing SDK

Use `LensQueryProcessor` for basic reasoning tasks:

```python
from lens_reasoning import LensQueryProcessor

# Initialize the query processor
processor = LensQueryProcessor("http://localhost:8001")

# Process a query
result = processor.process_query("What are the implications of AI in healthcare?")

print(f"Answer: {result['final_answer']}")
print(f"Confidence: {result['confidence_overall']}")
print(f"Contract ID: {result['contract_id']}")

processor.close()
```

### 2. Steering Directives SDK

Use `LensSteeringManager` for guided reasoning with custom directives:

```python
from lens_reasoning import LensQueryProcessor, LensSteeringManager
from models import ReasoningStepType

# Step 1: Process initial query
processor = LensQueryProcessor("http://localhost:8001")
result = processor.process_query("Analyze the environmental impact of electric vehicles")
contract_id = result['contract_id']

# Step 2: Add steering directives
manager = LensSteeringManager("http://localhost:8001")
trace = processor.get_reasoning_trace(contract_id)
first_step_id = trace['steps'][0]['id']

manager.add_steering_directive(
    contract_id=contract_id,
    step_id=first_step_id,
    target_step_types=[ReasoningStepType.EVIDENCE_GATHERING],
    guidance="Focus specifically on battery manufacturing and disposal impacts",
    priority=8
)

# Step 3: Re-run with steering applied
updated_result = manager.apply_steering_and_rerun(contract_id)
print(f"Updated answer: {updated_result['final_answer']}")

processor.close()
manager.close()
```

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

### LensSteeringManager

#### Constructor
```python
LensSteeringManager(base_url="http://localhost:8001", timeout=300)
```

#### Methods

##### `add_steering_directive(contract_id, step_id, target_step_types, guidance, **kwargs)`
Add a steering directive to a specific reasoning step.

**Parameters:**
- `contract_id` (str): Contract to modify
- `step_id` (str): Specific step to target
- `target_step_types` (List[ReasoningStepType]): Step types to apply to
- `guidance` (str): Guidance text
- `priority` (int): Priority level (1-10, default: 5)
- `constraints` (Dict, optional): Additional constraints
- `enforce_order` (bool): Whether to enforce step order

##### `add_multiple_steering_directives(contract_id, directives)`
Add multiple steering directives to different steps.

##### `apply_steering_and_rerun(contract_id, preserve_original_trace=True)`
Apply steering directives and re-run reasoning.

##### `get_directive_status(contract_id)`
Get status of all configured steering directives.

##### `clear_directives(contract_id)`
Clear all configured steering directives.

##### `get_reasoning_trace_with_steering(contract_id)`
Get detailed reasoning trace showing steering impact.

## Complete Example

```python
from lens_reasoning import LensQueryProcessor, LensSteeringManager
from models import ReasoningStepType

# Initialize both SDKs
processor = LensQueryProcessor("http://localhost:8001")
manager = LensSteeringManager("http://localhost:8001")

try:
    # Step 1: Initial reasoning
    result = processor.process_query(
        query="How can we reduce carbon emissions in urban transportation?",
        reasoning_mode="comprehensive"
    )

    contract_id = result['contract_id']
    print(f"Initial answer: {result['final_answer']}")

    # Step 2: Get detailed trace to understand the reasoning steps
    trace = processor.get_reasoning_trace(contract_id)

    # Step 3: Add steering to focus on electric vehicles
    manager.add_steering_directive(
        contract_id=contract_id,
        step_id=trace['steps'][0]['id'],  # Target first step
        target_step_types=[ReasoningStepType.HYPOTHESIS_FORMATION],
        guidance="Prioritize electric vehicle solutions and charging infrastructure",
        priority=9
    )

    # Step 4: Re-run with steering
    steered_result = manager.apply_steering_and_rerun(contract_id)
    print(f"Steered answer: {steered_result['final_answer']}")

    # Step 5: Check what changed
    if steered_result.get('directive_impact_summary'):
        print("Directive Impact:", steered_result['directive_impact_summary'])

finally:
    processor.close()
    manager.close()
```

## Error Handling

```python
from lens_reasoning import LensQueryProcessor, LensSteeringManager
from lens_reasoning import ProcessingError, SteeringError

try:
    processor = LensQueryProcessor("http://localhost:8001")
    result = processor.process_query("Your query here")

    manager = LensSteeringManager("http://localhost:8001")
    # ... steering operations

except ProcessingError as e:
    print(f"Failed to process query: {e}")
except SteeringError as e:
    print(f"Steering operation failed: {e}")
finally:
    processor.close()
    manager.close()
```

## Requirements

- Python 3.8+
- httpx
- Access to a running Lens Reasoning System server

## License

MIT License