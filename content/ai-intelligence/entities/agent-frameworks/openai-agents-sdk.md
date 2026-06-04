---
title: "OpenAI Agents SDK"
type: entity
tags: [agent-framework, framework, openai, orchestration, sdk, python, typescript]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/openai]]
  - [[../coding-agents/openai-codex]]
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge free">Free</span>
    <span class="open-weight-no">● Closed weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Agent Framework<span class="entity-meta-key">HQ</span>San Francisco, US<span class="entity-meta-key">Valuation</span>OpenAI<span class="entity-meta-key">Key Models</span>OpenAI models only
  </div>
</div>
# OpenAI Agents SDK

## Overview

**OpenAI Agents SDK** is OpenAI's official code-first framework for building multi-agent applications. It gives developers typed application code (TypeScript/Python) with full control over orchestration, tool execution, state management, approvals, and agent handoffs.

- **GitHub Repos**: [openai-agents-python](https://github.com/openai/openai-agents-python), [openai-agents-js](https://github.com/openai/openai-agents-js)
- **License**: MIT
- **Parent Company**: OpenAI
- **Website**: [platform.openai.com/docs/guides/agents](https://platform.openai.com/docs/guides/agents)

## Architecture

### Agent Model
- **Agents** are applications that plan, call tools, collaborate across specialists, and maintain state to complete multi-step work
- **Agent Definition**: Typed contract for a single specialist — model, tools, instructions, handoffs
- **Orchestration & Handoffs**: Multi-agent ownership model with clear boundaries between specialists
- **State Management**: Resumable state, continuation strategies, server-managed conversation

### API Positioning
| Use Case | Recommended API |
|----------|-----------------|
| One model call + tools + app-owned logic | Responses API |
| Full orchestration, tool execution, approvals, state | **Agents SDK** |

## Key Features

| Feature | Description |
|---------|-------------|
| **Typed SDK** | Native TypeScript and Python support |
| **Agent Handoffs** | Clean orchestration between specialist agents |
| **Tool Integration** | Hosted tools, MCP servers, custom function tools |
| **Guardrails** | Block/pause before risky actions with human review |
| **Sandbox Agents** | Container-based execution with files, commands, packages, snapshots, mounts |
| **Streaming** | Real-time token and event streaming |
| **Voice Agents** | SDK's voice pipeline + real-time agent patterns |
| **Observability** | Native tracing, debugging, and evaluation loops |
| **OpenAI-Native** | Deep integration with Responses API, Assistants, GPT models |

## 2026 Updates
- **Agents SDK Launch**: Official multi-agent orchestration framework
- **Sandbox Mode**: Container-based agent execution for isolated environments
- **Voice Agents Pipeline**: Real-time voice-first agent workflows
- **MCP Integration**: Native MCP server tool import
- **Evaluation Framework**: Built-in agent workflow evaluation loops

## Ecosystem

| Component | Purpose |
|-----------|---------|
| **Agents SDK (Python)** | Python SDK for building agents |
| **Agents SDK (TypeScript)** | TypeScript/JS SDK for building agents |
| **Responses API** | Underlying API for model calls with tools |
| **Assistants API** | Managed agent hosting on OpenAI infrastructure |
| **Agent Evals** | Evaluation loops for agent workflows |
| **Sandbox** | Container execution for agent environments |

## Code Example

```python
from openai.agents import Agent, Runner

researcher = Agent(
    name="Researcher",
    model="gpt-5.5",
    instructions="You are a research assistant.",
    tools=[web_search_tool],
)

reviewer = Agent(
    name="Reviewer",
    model="gpt-5.5",
    instructions="Review and validate research findings.",
)

result = Runner.run(researcher, "Research the latest LLM benchmarks")
```

## When to Use

- Building production applications with server-owned orchestration
- Multi-agent systems with clear specialist boundaries and handoffs
- Need for guardrails, approvals, and human-in-the-loop
- TypeScript or Python codebases
- Tight integration with OpenAI model ecosystem

## When NOT to Use

- Cross-provider model usage (SDK is OpenAI-first)
- Open-source/self-hosted model requirements
- Complex graph-based workflows (consider [[langchain]]/LangGraph)
- Role-based multi-agent scenarios (consider [[crewai]])

## Related

- [[../llm-providers/openai]] — OpenAI LLM provider (GPT-5.5, GPT-4o, etc.)
- [[../coding-agents/openai-codex]] — OpenAI's coding agent
- [[langchain]] — Cross-provider orchestration framework
- [[autogen]] — Microsoft's conversational multi-agent framework
- [[../../concepts/llm-architecture/mcp-protocol]] — Tool integration protocol

## Sources

- [OpenAI Agents SDK Documentation](https://platform.openai.com/docs/guides/agents)
- [OpenAI Agents SDK Quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart)
- [OpenAI Agents SDK GitHub (Python)](https://github.com/openai/openai-agents-python)
