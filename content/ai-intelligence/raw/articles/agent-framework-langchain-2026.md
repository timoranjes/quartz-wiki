---
title: LangChain
researched: 2026-06-05
sources:
  - https://www.langchain.com/
  - https://python.langchain.com/docs/introduction/
  - https://github.com/langchain-ai/langchain
---

# LangChain

LangChain is the most widely adopted framework for building applications powered by large language models. Created by Harrison Chase in 2022, it provides a standardized interface for chaining LLM calls, managing conversation history, and integrating with external tools and data sources.

## Architecture

- **langchain-core**: Base abstractions (BaseLanguageModel, BaseChatModel, Tool, PromptTemplate)
- **langchain-community**: Third-party integrations (vector stores, APIs, databases)
- **langgraph**: Stateful, multi-actor application framework built on top of LangChain
- **langserve**: Deploy LangChain chains as REST APIs

## Key Features

- **Chains**: Composable sequences of LLM calls and operations
- **Agents**: LLMs that can decide the order of tool calls dynamically
- **Retrieval (RAG)**: Document loading, splitting, embedding, and retrieval pipelines
- **Memory**: Conversation history management (buffer, summary, vector store-backed)

## LangGraph

LangGraph extends LangChain with stateful, cyclic graph-based workflows for multi-agent systems:
- **StateGraph**: Define schema and nodes of multi-agent workflow
- **Conditional edges**: Route execution based on agent decisions
- **Persistence**: Checkpoint state for human-in-the-loop workflows
- **Streaming**: Real-time output from each node

## Pricing

- Open-source (MIT license)
- LangSmith: Free tier (5,000 traces/mo), Plus ($39/user/mo), Enterprise
- LangGraph Platform: Free tier available

## Latest Updates (2025-2026)

- LangGraph is the preferred abstraction for multi-agent workflows
- Integration with all major LLM providers
- Growing enterprise adoption for RAG pipelines and agent orchestration
