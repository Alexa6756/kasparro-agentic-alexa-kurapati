# Multi-Agent Content Generation System

This project implements a **lightweight, agentic content generation pipeline** that converts structured product data into multiple machine-readable content pages.

The system is designed using **LangChain agents**, **LangGraph-based orchestration**, reusable logic blocks, and deterministic JSON outputs.

---

## Overview

Given a single product dataset, the system generates **exactly three structured content pages**:

- FAQ Page
- Product Description Page
- Product Comparison Page (against a fictional competitor)

The pipeline is built using **specialized agents**, each responsible for a single task, coordinated through a shared state and an explicit workflow graph.

---

## Input & Output

### Input
- A structured product object provided at runtime

### Output
The system always generates the following JSON files:

- `faq.json`
- `product_page.json`
- `comparison_page.json`

All outputs are fully structured, deterministic, and derived strictly from the input data.

---

## System Design (High Level)

The system is composed of three core agents:

- **Parser Agent** – structures and validates raw product data
- **Question Agent** – generates categorized user questions
- **Writer Agent** – assembles final pages using templates

Agents communicate via shared state and are executed conditionally using a graph-based workflow.

---

## Execution Flow (Conceptual)

```

Raw Product Input
│
▼
Parser Agent
│
▼
Question Agent
│
▼
Writer Agent
│
▼
Structured JSON Outputs

````

---

## Key Characteristics

- Clear agent responsibilities
- Explicit orchestration (no scripted flow)
- Tool-driven reasoning
- Reusable templates and logic blocks
- Fully JSON-structured output
- Clean, minimal architecture

---

## Running the Project

```bash
pip install -r requirements.txt
python main.py
````

---

## Conclusion

This project demonstrates a **real agentic pipeline** using LangChain and LangGraph, with a focus on modularity, determinism, and clean system design suitable for production-style AI automation workflows.
