---
title: "LangChain / LangGraph"
type: entity
tags: [agent-framework, framework, orchestrator, tool-use]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/openai]]
  - [[../llm-providers/anthropic]]
  - [[../coding-agents/openai-codex]]
  - [[../coding-agents/claude-code]]
used_by:
  - [[../coding-agents/openai-codex]]
  - [[../coding-agents/github-copilot]]
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge free">Free</span>
    <span class="open-weight-yes">● Open weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Agent Framework<span class="entity-meta-key">HQ</span>Open Source<span class="entity-meta-key">Key Models</span>Any LLM
  </div>
</div>
# LangChain / LangGraph

## Overview

**LangChain** is the largest LLM application framework (launched 2022), providing chain-based orchestration for rapid prototyping. **LangGraph** is LangChain's production-grade agent runtime, modeling workflows as state machines using directed graphs.

- **GitHub Stars**: ~85K (LangChain ecosystem)
- **License**: MIT (open-source)
- **Parent Company**: LangChain, Inc.
- **Website**: [langchain.com](https://www.langchain.com/)

## Architecture

### LangChain (Chain-based)
- Core design: Sequential chains of LLM calls, prompts, and tools
- Philosophy: Developer velocity & flexibility
- Strengths: Huge ecosystem, easy tool integration, rapid prototyping
- Limitations: Less control than graph-based systems, complex abstractions for non-trivial flows

### LangGraph (Graph-based)
- Core design: State machines with nodes (functions) and edges (transitions)
- State Schema: Typed data flowing through the graph
- Supports: Cycles, conditional branching, parallel execution
- Philosophy: Production-grade reliability with maximum control

## Key Features

| Feature | Description |
|---------|-------------|
| **Human-in-the-loop** | Workflow pause/resume hooks, approval gates |
| **Customizable Workflows** | Single-agent, multi-agent, hierarchical, cyclic architectures |
| **Built-in Memory** | Persist conversation history across sessions |
| **Native Streaming** | Token-by-token streaming for real-time UX |
| **Model Agnostic** | Works with any LLM provider |
| **Checkpointing** | State persistence via SQLite, Postgres, or memory |
| **LangSmith Integration** | Native tracing, debugging, and evaluation |

## 2026 Updates
- **v0.4 (April 2026)**: Improved state persistence, HITL checkpoints, native LangSmith tracing
- **v0.3.x (Feb 2026)**: PostgresSaver, streaming for tool outputs

## Production Usage

LangGraph powers production agents at: Klarna, Vanta, Clay, Rippling, Lyft, Gong, Harvey, Abridge, Cloudflare, The Home Depot, Workday, Cisco, Mercor, monday.com, NVIDIA, Bridgewater, LinkedIn, Coinbase, Elastic, ServiceNow, Uber, Exa, and more.

## Code Example

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    sources: List[str]
    summary: str
    enough_info: bool

graph = StateGraph(ResearchState)
graph.add_node("search", search_node)
graph.add_node("evaluate", evaluate_node)
graph.add_node("summarize", summarize_node)

graph.set_entry_point("search")
graph.add_edge("search", "evaluate")
graph.add_conditional_edges(
    "evaluate",
    lambda s: "summarize" if s["enough_info"] else "search"
)
graph.add_edge("summarize", END)

agent = graph.compile()
```

## Ecosystem

| Component | Purpose |
|-----------|---------|
| **LangChain** | Core framework for LLM applications |
| **LangGraph** | Agent orchestration runtime |
| **LangSmith** | Debugging, tracing, evaluation platform |
| **LangGraph Platform** | Hosting and deployment |
| **LangGraph Studio** | Visual IDE for building and debugging graphs |

## When to Use

- Building production-grade agents requiring explicit control over execution flow
- Workflows with cycles, branching logic, or human approval gates
- Teams of engineers building complex, multi-step agent systems
- Need for observability, tracing, and debugging

## When NOT to Use

- Simple linear workflows (single API call → result)
- Rapid prototyping where speed matters more than control (consider [[crewai]])
- Non-engineers designing agent systems

## Related

- [[crewai]] — Role-based multi-agent framework
- [[autogen]] — Microsoft's conversational multi-agent framework
- [[llamaindex]] — Retrieval-centric agent framework
- [[multi-agent-orchestration]] — Orchestration patterns
- [[mcp-protocol]] — Tool integration protocol

## Sources

- [[../../raw/sources/2026-06-02-top-agentic-frameworks-2026-jetbrains]]
- [[../../raw/sources/datacamp-crewai-vs-langgraph-vs-autogen]]
- [[../../raw/sources/pecollective-agent-frameworks-compared-2026]]
