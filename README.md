# Lens Reasoning SDK

A Python SDK for the Lens Reasoning System that provides query processing and reasoning capabilities.

## Installation

```bash
pip install lens-reasoning-sdk
```

## Prerequisites

- Python 3.8+
- Internet access to the Lens Reasoning System production API

## Quick Start

```python
from lens_reasoning_sdk import LensQueryProcessor
from lens_reasoning_sdk.exceptions import ProcessingError

try:
    # Initialize the query processor
    processor = LensQueryProcessor()

    # Process a query
    result = processor.process_query("What are the implications of AI in healthcare?")

    print(f"Answer: {result['final_answer']}")
    print(f"Confidence: {result['confidence_overall']}")
    print(f"Contract ID: {result['contract_id']}")

except ProcessingError as e:
    print(f"Processing failed: {e}")
finally:
    processor.close()
```

## Available Methods

- `process_query(query, **kwargs)` - Process a query through the reasoning system
- `get_contract(contract_id)` - Get complete contract details
- `get_reasoning_trace(contract_id)` - Get detailed reasoning trace
- `list_contracts(workflow_id=None, limit=20)` - List existing contracts

## API Documentation

The Lens Reasoning SDK interfaces with a comprehensive REST API that provides advanced AI reasoning capabilities. All endpoints are available at `https://api.tupl.xyz/lens/`.

### Query Processing

#### Process Query
Process a query through the Lens Reasoning system and receive detailed analysis.

**Endpoint:** `POST /lens/reasoning/process`

**Parameters:**
- `query` (str, required): The question or problem to reason about
- `initial_docs` (List[str], optional): Initial documents to include in context
- `reasoning_mode` (str, optional): Reasoning mode - "comprehensive", "focused", or "policy_guided" (default: "comprehensive")
- `workflow_id` (str, optional): Optional workflow identifier
- `workflow_name` (str, optional): Optional workflow name

**Returns:**
- `success` (bool): Processing success status
- `contract_id` (str): Unique identifier for the reasoning session
- `final_answer` (str): The AI-generated answer to your query
- `confidence_overall` (float): Overall confidence score (0.0-1.0)
- `execution_time_ms` (int): Processing time in milliseconds
- `total_steps` (int): Number of reasoning steps performed
- `knowledge_gaps` (List[str]): Identified gaps in available knowledge

### Contract Management

#### List Contracts
Retrieve a list of previously processed reasoning contracts.

**Endpoint:** `GET /lens/contracts`

**Parameters:**
- `workflow_id` (str, optional): Filter contracts by workflow ID
- `limit` (int, optional): Maximum number of contracts to return (default: 20)

**Returns:** List of contract summaries including contract ID, original query, final answer, confidence score, and creation timestamp.

#### Get Contract Details
Retrieve comprehensive details for a specific reasoning contract.

**Endpoint:** `GET /lens/contracts/{contract_id}`

**Parameters:**
- `contract_id` (str, required): The contract identifier

**Returns:** Complete contract information including reasoning trace, confidence assessments, knowledge gaps, directive change records, and execution metadata.

### Reasoning Analysis

#### Get Reasoning Trace
Access detailed step-by-step reasoning analysis with evidence and decision breakdowns.

**Endpoint:** `GET /lens/reasoning/trace/{contract_id}`

**Parameters:**
- `contract_id` (str, required): The contract identifier

**Returns:** Comprehensive reasoning trace including:
- Individual reasoning steps with decisions and confidence levels
- Evidence sources and relevance scores
- Applied steering directives and their impact
- Context summaries from knowledge base, tools, and external sources

### Advanced Steering Features

The API supports advanced steering directives for controlling and customizing the reasoning process:

#### Configure Step Directives
Add custom guidance to specific reasoning steps.

**Endpoint:** `POST /lens/reasoning/{contract_id}/configure-step-directives`

**Parameters:**
- `contract_id` (str, required): The contract identifier
- Request body:
```json
{
  "contract_id": "string",
  "step_directives": [
    {
      "step_id": "string",
      "directives": [
        {
          "target_step_types": ["problem_decomposition", "evidence_gathering"],
          "priority": 8,
          "guidance": "Focus specifically on peer-reviewed scientific studies",
          "constraints": {},
          "enforce_order": false
        }
      ]
    }
  ]
}
```

**Returns:**
```json
{
  "success": true,
  "message": "Step directives configured successfully",
  "steps_configured": 2,
  "ready_to_apply": true
}
```

#### Apply Directives
Execute configured steering directives and re-run the reasoning process.

**Endpoint:** `POST /lens/reasoning/{contract_id}/apply-directives`

**Parameters:**
- `contract_id` (str, required): The contract identifier
- Request body:
```json
{
  "contract_id": "string",
  "preserve_original_trace": true
}
```

**Returns:**
```json
{
  "success": true,
  "message": "Directives applied and reasoning re-executed successfully",
  "contract_id": "string",
  "total_steps": 15,
  "confidence_overall": 0.85,
  "execution_time_ms": 2340,
  "steps_with_directives": 3,
  "final_answer": "Updated reasoning result with applied directives",
  "directive_impact_summary": {
    "total_directives_applied": 3,
    "steps_modified": 2,
    "confidence_change": 0.12,
    "reasoning_path_changes": ["evidence_gathering", "synthesis"]
  },
  "directive_change_records": [
    {
      "step_id": "step_1",
      "directive_applied": "Focus on peer-reviewed studies",
      "original_decision": "Original reasoning",
      "modified_decision": "Enhanced reasoning with directive guidance",
      "impact_score": 0.8
    }
  ]
}
```

#### Directive Status
Check the status of configured steering directives.

**Endpoint:** `GET /lens/reasoning/{contract_id}/directive-status`

**Parameters:**
- `contract_id` (str, required): The contract identifier

**Returns:**
```json
{
  "contract_id": "string",
  "total_steps": 15,
  "steps_with_directives": 3,
  "step_statuses": [
    {
      "step_id": "step_1",
      "step_type": "evidence_gathering",
      "directives_count": 1,
      "directives": [
        {
          "target_step_types": ["evidence_gathering"],
          "priority": 8,
          "guidance": "Focus on peer-reviewed studies",
          "constraints": {},
          "enforce_order": false
        }
      ]
    }
  ],
  "has_pending_directives": true
}
```

#### Clear Directives
Remove all configured steering directives from a contract.

**Endpoint:** `DELETE /lens/reasoning/{contract_id}/clear-directives`

**Parameters:**
- `contract_id` (str, required): The contract identifier

**Returns:**
```json
{
  "success": true,
  "message": "All step directives cleared"
}
```

#### Add Custom Steering Directive
Create a custom steering directive template for reuse.

**Endpoint:** `POST /lens/reasoning/add-steering-directive`

**Parameters:**
- Request body:
```json
{
  "target_step_types": ["evidence_gathering", "synthesis"],
  "priority": 7,
  "guidance": "Prioritize recent research from the last 5 years",
  "constraints": {
    "time_limit": "5_years",
    "source_types": ["academic", "peer_reviewed"]
  },
  "enforce_order": false
}
```

**Returns:**
```json
{
  "success": true,
  "template_name": "custom_0"
}
```

### Supported Reasoning Step Types

The system performs analysis across 29 specialized reasoning step types:

**Core Analysis:** Problem decomposition, fact extraction, evidence gathering, pattern recognition, hypothesis formation

**Logical Operations:** Deductive reasoning, inductive reasoning, abductive reasoning, causal analysis, contradiction checking

**Evaluation:** Evidence validation, confidence assessment, risk assessment, comparative analysis, quality verification

**Synthesis:** Information synthesis, conclusion formation, recommendation generation, decision making

**External Integration:** Tool invocation, knowledge retrieval, document analysis, web search

**Meta-Reasoning:** Strategy planning, approach selection, step validation, error detection, course correction

### Error Handling

The API returns standard HTTP status codes:
- `200 OK`: Successful operation
- `404 Not Found`: Contract or resource not found
- `500 Internal Server Error`: Processing failure

Error responses include detailed error messages in the format: `{"detail": "error description"}`

### Rate Limits and Usage

The production API is designed for research and development use. For high-volume production deployments, please contact the development team for appropriate scaling and rate limit configurations.

## License

MIT License