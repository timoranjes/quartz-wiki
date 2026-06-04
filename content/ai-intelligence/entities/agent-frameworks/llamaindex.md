---
title: "LlamaIndex"
type: entity
tags: [agent-framework, framework, retrieval, memory]
sources: [raw/articles/agent-framework-llamaindex-2026.md]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/openai]]
  - [[../llm-providers/anthropic]]
  - [[../llm-providers/meta-llama]]
  - [[../llm-providers/cohere]]
used_by: []
---

# LlamaIndex

## Overview

**LlamaIndex** (formerly GPT Index) is a retrieval-centric data framework for building LLM applications. It specializes in connecting LLMs to private data sources through indexing, retrieval, and context augmentation.

- **Core Philosophy**: Data-first agent building
- **Key Strength**: Strong indexing & memory, optimized for RAG
- **License**: MIT (open-source)
- **Website**: [llamaindex.ai](https://www.llamaindex.ai/)

## Architecture

LlamaIndex uses a **retrieval-centric orchestration** model:
- **Data Connectors**: 25+ integrations (APIs, PDFs, SQL, Notion, Google Drive, etc.)
- **Indexes**: Structured representations of data for efficient retrieval
- **Query Engines**: Interfaces for asking questions over indexed data
- **Chat Engines**: Stateful conversation interfaces with retrieval context
- **Agents**: Basic agent capabilities built on top of retrieval

## Key Features

| Feature | Description |
|---------|-------------|
| **25+ Data Connectors** | APIs, PDFs, SQL, Notion, Google Drive, Confluence, Slack, and more |
| **Vector Store Integration** | Works with all major vector databases |
| **Structured Retrieval** | Keyword, semantic, and hybrid search |
| **Strong Memory** | Persistent memory across sessions |
| **Query Transformation** | Multi-step query decomposition and refinement |
| **Router** | Intelligent selection of the best retrieval strategy |
| **Sub-Question Querying** | Breaks complex questions into sub-queries |
| **LLM Agnostic** | Works with any LLM provider |

## Agent Capabilities

While primarily a retrieval framework, LlamaIndex supports basic agent patterns:
- **ReAct Agent**: Reasoning + acting loop with tool use
- **Query Pipeline**: Chain retrieval → reasoning → response
- **OpenAI Agent**: Uses OpenAI function calling for tool selection
- **RAG Pipeline**: Retrieval-augmented generation as a composable pipeline

## Comparison with Other Frameworks

| Dimension | LlamaIndex | LangGraph | CrewAI |
|-----------|------------|-----------|--------|
| Architecture | Retrieval-centric | Graph-based state machines | Role-based team metaphor |
| Multi-Agent | Limited | Strong — explicit graphs | Strong — role-defined teams |
| Memory | Strong — persistent, indexed | Strong — state-based | Light — session-based |
| Action Orchestration | Weak | Strong — explicit control | Moderate — task-based |
| Best For | Knowledge-heavy agents | Production agent workflows | Task-oriented agent teams |
| RAG Quality | Best-in-class | Good (via LangChain) | Moderate |

## Strengths

- **Best-in-class RAG**: Optimized for retrieval-augmented generation
- **Data connectors**: Largest ecosystem of data source integrations
- **Strong indexing**: Multiple indexing strategies (vector, keyword, tree, keyword-table)
- **Query pipelines**: Composable, debuggable retrieval flows

## Weaknesses

- **Weak action orchestration**: Not designed for complex agent workflows
- **Limited multi-agent support**: Primarily single-agent retrieval
- **Not ideal for tool-heavy agents**: Action patterns are basic compared to [[langchain]] or [[crewai]]

## When to Use

- Building knowledge-heavy agents that need to query large document collections
- RAG applications (document Q&A, search over private data)
- Applications requiring strong data ingestion and indexing pipelines
- When retrieval quality is the primary bottleneck

## When NOT to Use

- Complex multi-agent orchestration (use [[langchain]] or [[crewai]])
- Production agents requiring fine-grained control flow
- Tool-heavy applications with many external API integrations

## Related

- [[langchain]] — Chain/graph-based orchestration
- [[crewai]] — Role-based multi-agent framework
- [[autogen]] — Microsoft's conversational multi-agent framework
- [[multi-agent-orchestration]] — Orchestration patterns
- [[mcp-protocol]] — Tool integration protocol

## Sources

- [[../../raw/sources/2026-06-02-top-agentic-frameworks-2026-jetbrains]]
- [[../../raw/sources/datacamp-crewai-vs-langgraph-vs-autogen]]
- [[../../raw/sources/pecollective-agent-frameworks-compared-2026]]
