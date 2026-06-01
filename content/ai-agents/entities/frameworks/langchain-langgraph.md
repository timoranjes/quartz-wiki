---
title: LangChain & LangGraph
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [framework, sdk, open-source]
sources: []
confidence: high
---

# LangChain & LangGraph

## Overview

LangChain is a Python/JS framework for building LLM applications. LangGraph adds stateful, multi-actor workflows on top — enabling complex agent flows with cycles, branching, and persistence.

## LangChain Components

### Core Abstractions
- **Chains:** Sequences of LLM calls + tool invocations
- **Agents:** LLM + tools + memory in a loop
- **Tools:** Callable functions the agent can invoke
- **Memory:** Conversation history, vector stores, key-value stores
- **Retrievers:** Document retrieval from vector databases

### Key Use Cases
- RAG pipelines (document retrieval + synthesis)
- Simple agent loops (tool use + reasoning)
- Data extraction from unstructured text

## LangGraph Components

### Core Abstractions
- **StateGraph:** Define nodes (functions) and edges (transitions)
- **State:** Typed dictionary shared across all nodes
- **Nodes:** Functions that read/write state
- **Edges:** Conditional or unconditional transitions between nodes
- **Checkpoints:** Persist state for resumption

### Key Use Cases
- Multi-agent workflows with complex routing
- Human-in-the-loop approval flows
- Long-running processes with resumption
- Agent swarms with shared state

## When to Use LangChain/LangGraph

### Use LangChain When
- Building RAG pipelines
- Simple tool-using agents
- Rapid prototyping of LLM apps
- You need out-of-the-box integrations (100+ providers)

### Use LangGraph When
- Agent workflows have cycles or conditional branching
- Multiple agents need to coordinate
- You need checkpointing/resumption
- The control flow is too complex for LangChain chains

### When NOT to Use
- Simple Q&A (overkill — use direct API)
- Single-turn tool calls (native tool calling is simpler)
- When you need maximum control over the agent loop

## Comparison with Other Frameworks

| Framework | Strength | Weakness | Best For |
|-----------|----------|----------|----------|
| LangChain | Integrations, RAG | Verbose, heavy | Quick LLM apps |
| LangGraph | Complex flows | Learning curve | Multi-agent workflows |
| CrewAI | Role-based teams | Limited flexibility | Team simulation |
| AutoGen | Multi-agent convos | Complexity | Research agents |
| Hermes delegate_task | Simple delegation | No shared state | Parallel tasks |

## Pitfalls

1. **Chain complexity** — Long chains become unmaintainable. Fix: break into sub-chains.
2. **State drift** — LangGraph state can get out of sync. Fix: use typed state with validation.
3. **Token bloat** — LangChain passes full context at each step. Fix: truncate/summarize.
4. **Debugging difficulty** — Hard to trace which step failed. Fix: use LangSmith tracing.

## Related
- [[langchain-langgraph]] — Primary framework for building these architectures
- [[crewai]] — role-based multi-agent framework
- [[autogen]] — Microsoft multi-agent framework
- [[orchestrator-workers]] — how Hermes does delegation differently
