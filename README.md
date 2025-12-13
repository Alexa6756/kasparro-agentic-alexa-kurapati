# Multi-Agent Content Generation System

A production-ready, agentic system that transforms structured product data into multiple machine-readable content pages using specialized agents.

This project demonstrates how to build a **lightweight, modular, and extensible agent-based pipeline** focused on clarity, determinism, and clean system design.

---

## Overview

The system processes a single product dataset and generates **three structured content pages**:

- FAQ Page
- Product Description Page
- Product Comparison Page (vs a fictional competitor)

The pipeline is implemented using **multiple specialized agents**, explicit orchestration, reusable logic blocks, and strict validation.

---

## Key Features

- Multi-agent architecture with clear responsibilities  
- Explicit pipeline orchestration  
- Reusable logic blocks and templates  
- Fully structured JSON outputs  
- Multiple validation layers  
- Registry-based extensibility  
- Deterministic and repeatable results  
- Error handling and logging  

---

## Generated Content

- **FAQ Page (`faq.json`)**  
  Categorized user questions and answers

- **Product Page (`product_page.json`)**  
  Structured product description and usage details

- **Comparison Page (`comparison_page.json`)**  
  Product comparison against a fictional competitor

---

## System Architecture

### High-Level Architecture

```

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Configuration   │───▶│ Pipeline         │───▶│ Agents           │
│ (YAML / Input)  │    │ Orchestrator     │    │ (Specialized)    │
└─────────────────┘    └─────────────────┘    └─────────┬─────────┘
│
┌─────────────────┐    ┌─────────────────┐    ┌─────────▼─────────┐
│ Input Validation│◀───│ Logic Blocks     │◀───│ Templates         │
│                 │    │ (Reusable)       │    │ (Content Layout)  │
└─────────────────┘    └─────────────────┘    └─────────┬─────────┘
│
┌─────────────────┐    ┌─────────────────┐    ┌─────────▼─────────┐
│ Output Validation│◀──│ Schema Validation│◀──│ JSON Generation   │
└─────────────────┘    └─────────────────┘    └───────────────────┘

```

---

## Agent Responsibilities

| Agent | Responsibility | Input | Output |
|-----|---------------|-------|--------|
| ProductParserAgent | Parse and normalize product data | Raw product data | Validated product model |
| QuestionGenerationAgent | Generate categorized user questions | Product model | Question list |
| FAQPageAgent | Build FAQ content | Questions | FAQ JSON |
| ProductPageAgent | Build product description | Product model | Product JSON |
| ComparisonPageAgent | Generate comparison page | Product model | Comparison JSON |

Each agent follows the **single-responsibility principle** and communicates only through shared state.

---

## Orchestration

The pipeline is executed through an explicit orchestration layer that:

- Runs agents in the correct order
- Avoids unnecessary execution
- Ensures required inputs are present before each step
- Produces deterministic outputs

No hard-coded sequencing or hidden control flow is used.

---

## Project Structure

```

kasparro-ai-agentic-content-generation-system/
├── docs/
│   └── projectdocumentation.md
├── src/
│   ├── agents/            # Agent implementations
│   ├── logic_blocks/      # Reusable transformation logic
│   ├── templates/         # Output templates
│   ├── models/            # Data models
│   ├── validators/        # Validation layers
│   ├── registry/          # Agent registry
│   ├── orchestrator/      # Pipeline orchestration
│   └── utils/             # Logging & helpers
├── tests/                 # Test suite
├── outputs/               # Generated JSON files
├── pipeline_config.yaml   # Configuration
├── run.py                 # Entry point
├── requirements.txt
└── README.md

````

---

## Quick Start

### Installation

```bash
git clone https://github.com/your-username/kasparro-ai-agentic-content-generation-system.git
cd kasparro-ai-agentic-content-generation-system
pip install -r requirements.txt
````

### Run the Pipeline

```bash
# Default execution
python run.py

# Verbose mode
python run.py --verbose

# Custom configuration
python run.py --config custom_config.yaml
```

---

## Configuration

The system is configured via `pipeline_config.yaml`.

Example:

```yaml
product_data:
  product_name: "Sample Product"
  concentration: "10%"
  skin_type: ["Oily"]
  key_ingredients: ["Ingredient"]
  benefits: ["Benefit"]
  how_to_use: "Usage instructions"
  side_effects: "Safety information"
  price: 999

agents:
  - ProductParserAgent
  - QuestionGenerationAgent
  - FAQPageAgent
  - ProductPageAgent
  - ComparisonPageAgent

output:
  directory: "outputs"
```

---

## Output

After execution, the `outputs/` directory contains:

```
faq.json
product_page.json
comparison_page.json
```

All outputs are:

* Fully JSON-structured
* Validated
* Deterministic
* Derived strictly from input data

---

## Testing

```bash
pytest tests/
pytest tests/test_agents.py
pytest tests/test_pipeline.py
```

---

## Design Principles

* **Single Responsibility** – One purpose per agent
* **Modularity** – Independent, reusable components
* **Validation-First** – Multiple validation layers
* **Configurability** – Externalized configuration
* **Extensibility** – Easy to add new agents
* **Determinism** – Consistent outputs for the same input

---

## Extending the System

### Add a New Agent

```python
from src.registry.agent_registry import register_agent

@register_agent("NewAgent")
class NewAgent(BaseAgent):
    def run(self, context):
        return {"output": value}
```

### Add a Logic Block

```python
def custom_logic(product):
    return processed_data
```

---

## Conclusion

This project demonstrates a **production-ready agentic architecture** for structured content generation.

It emphasizes:

* Clear agent boundaries
* Explicit orchestration
* Reusable logic and templates
* Fully structured outputs

The system is minimal, extensible, and suitable for real-world AI content automation workflows.

```
