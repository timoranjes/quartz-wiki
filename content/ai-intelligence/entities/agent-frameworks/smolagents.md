---
title: "smolagents"
type: entity
tags: [agent-framework, framework, python, code-agent, huggingface]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/openai]]
  - [[../llm-providers/anthropic]]
---

# smolagents

## Overview

**smolagents** is Hugging Face's lightweight Python library for building AI agents with minimal code (~1,000 lines). It empowers LLMs with agency — enabling them to observe, reason, and act in real-world environments using a code-first approach.

- **GitHub Stars**: ~27,687
- **License**: Apache-2.0
- **Parent Company**: Hugging Face
- **Website**: [huggingface.co/docs/smolagents](https://huggingface.co/docs/smolagents/index)
- **GitHub**: [github.com/huggingface/smolagents](https://github.com/huggingface/smolagents)

## Architecture

### Code-First Design
- **Core Philosophy**: Minimal abstractions — the entire library is ~1,000 lines of code
- **CodeAgent** (default): Agent writes tool calls as **executable Python code**, enabling natural composition (loops, conditionals, nesting)
- **ToolCallingAgent**: Standard JSON-based tool calling for compatibility with other frameworks
- No JSON parsing overhead — output can be executed directly

### Execution Model
- Agent loop: generate thought → write Python code → execute → observe result → repeat
- Code execution is isolated and supports sandboxed environments

## Key Features

| Feature | Description |
|---------|-------------|
| **CodeAgent** | Agent writes Python code for tool calls — no JSON parsing needed |
| **ToolCallingAgent** | JSON-based tool calling (alternative to CodeAgent) |
| **Sandboxed Execution** | Supports Modal, Blaxel, E2B, or Docker sandboxes for secure execution |
| **HF Hub Integration** | Share/load agents & tools as Gradio Spaces on Hugging Face Hub |
| **Model-Agnostic** | Works with any LLM: HF Inference API, OpenAI/Anthropic (LiteLLM), local (Transformers/Ollama) |
| **Tool-Agnostic** | Import tools from MCP servers, LangChain, or HF Spaces |
| **CLI Tools** | `smolagent` and `webagent` CLI commands for quick agent runs |
| **Multimodal** | Supports text, vision, video, and audio inputs |

## 2026 Updates
- **ToolKit**: Default tools including DuckDuckGoSearch, Vision QA
- **MCP Server Support**: Native `from_mcp()` tool import
- **LangChain Tool Import**: `Tool.from_langchain()` for cross-framework compatibility
- **Web Browser Agent**: Vision-based web browsing agent example
- **Integration into Hugging Face Agents Course**: Official teaching framework

## Model Integration

| Model Class | Use Case |
|-------------|----------|
| `TransformersModel` | Local inference using `transformers` |
| `InferenceClientModel` | HF Inference API / third-party providers |
| `LiteLLMModel` | Multi-provider access via LiteLLM |
| `OpenAIServerModel` | OpenAI-compatible APIs |
| `AzureOpenAIServerModel` | Azure OpenAI deployments |

## Code Example

```python
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

model = InferenceClientModel()
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
)

result = agent.run("What is the current weather in Paris?")
print(result)
```

## Ecosystem

| Component | Purpose |
|-----------|---------|
| **CodeAgent** | Primary agent — writes Python code |
| **ToolCallingAgent** | JSON-based tool calling |
| **MultiStepAgent** | Base class for thought → action → execution loop |
| **Tools** | `@tool` decorator, `Tool` class, MCP/LangChain/HF Space imports |
| **Models** | Transformers, InferenceClient, LiteLLM, OpenAI-compatible |
| **CLI** | `smolagent`, `webagent` commands |

## When to Use

- Rapid prototyping with minimal setup
- Code-first agent development where Python composition is natural
- Lightweight experimentation without complex configurations
- Straightforward application logic
- Leveraging HF ecosystem (models, spaces, tools)

## When NOT to Use

- Highly complex orchestration scenarios
- Enterprise-grade agent systems requiring strict schema enforcement
- Multi-agent coordination at scale (consider [[langchain]] or [[crewai]])
- Non-Python environments

## Related

- [[langchain]] — Full-featured orchestration framework
- [[crewai]] — Role-based multi-agent framework
- [[llamaindex]] — Retrieval-centric framework
- [[../../concepts/llm-architecture/mcp-protocol]] — Tool integration protocol (smolagents supports MCP tool import)

## Sources

- [Hugging Face smolagents Documentation](https://huggingface.co/docs/smolagents/index)
- [Hugging Face Blog: Introducing smolagents](https://huggingface.co/blog/smolagents)
- [Hugging Face Agents Course: Why use smolagents](https://huggingface.co/learn/agents-course/en/unit2/smolagents/why_use_smolagents)
