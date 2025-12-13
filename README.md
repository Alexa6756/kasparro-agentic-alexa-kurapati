# Project Documentation  
Multi-Agent Content Generation System

---

## 1. Problem Statement

The objective of this project is to design and implement a **true agentic system** that transforms a single product dataset into multiple structured, machine-readable content pages.

The system must:
- Use multiple agents with clear responsibilities
- Avoid monolithic or scripted pipelines
- Be orchestrated using a framework-based workflow
- Rely on model + tool interactions
- Produce deterministic JSON outputs
- Use only the provided input data

---

## 2. Solution Overview

The solution is implemented as a **LangChain + LangGraph multi-agent system**.

Each agent performs one well-defined task and communicates through a shared state object.  
Execution order is controlled by an explicit workflow graph rather than hard-coded sequencing.

---

## 3. Scope & Assumptions

### Input Scope
- A structured product object provided at runtime
- No external data sources are used

### Output Scope
- Exactly three JSON files:
  - `faq.json`
  - `product_page.json`
  - `comparison_page.json`

### Constraints
- Outputs are deterministic
- Architecture correctness is independent of API availability

---

## 4. System Design (Mandatory)

### 4.1 Architectural Principles

- Single responsibility per agent
- Explicit orchestration via workflow graph
- Tool-driven reasoning
- Reusable templates and logic blocks
- No hidden control flow

---

### 4.2 Agent Responsibilities

**Parser Agent**
- Validates and structures raw product input
- Produces a normalized product representation

**Question Agent**
- Generates categorized user questions
- Uses model-driven logic rather than static lists

**Writer Agent**
- Uses reusable templates
- Assembles final JSON outputs deterministically
- Does not perform autonomous reasoning

---

### 4.3 Orchestration

The system uses a **graph-based workflow** to control execution:

- If product data is missing → Parser Agent
- If questions are missing → Question Agent
- Otherwise → Writer Agent → END

This ensures correct sequencing without custom orchestration logic.

---

### 4.4 Tool & Template Usage

- Business logic is encapsulated in tools and logic blocks
- Output structure is defined using reusable templates
- No predefined output strings are embedded in prompts

---

## 5. Output Guarantees

The system always produces:

````

outputs/
├── faq.json
├── product_page.json
└── comparison_page.json

```

All outputs are:
- Fully JSON-structured
- Machine-readable
- Deterministic
- Derived strictly from input data

---

## 6. Conclusion

This project demonstrates a **clean, minimal, agentic architecture** built using LangChain and LangGraph.

It satisfies all core requirements for real-world agent-based automation systems, including clear agent boundaries, framework-based orchestration, and structured outputs.
```
---
