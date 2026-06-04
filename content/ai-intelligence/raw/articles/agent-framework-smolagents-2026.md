---
title: "SmolAgents - HuggingFace Lightweight Agent Framework"
researched: 2026-06-05
sources:
  - url: "https://huggingface.co/docs/smolagents/index"
    title: "SmolAgents Official Documentation"
  - url: "https://github.com/huggingface/smolagents"
    title: "SmolAgents GitHub Repository"
  - url: "https://smolagents.org/"
    title: "SmolAgents Website"
  - url: "https://huggingface.co/docs/smolagents/tutorials/secure_code_execution"
    title: "SmolAgents Secure Code Execution Tutorial"
tags:
  - agent-framework
  - lightweight-agents
  - huggingface
  - code-agents
  - open-source
---

# SmolAgents - HuggingFace Lightweight Agent Framework

## Overview

`smolagents` is a **minimalist, open-source Python library** from HuggingFace for building and running AI agents with **extreme simplicity**. The core agent logic fits in approximately **1,000 lines of code**, keeping abstractions to their minimal shape above raw code. It offers powerful agents in just a few lines of code, with a distinctive focus on **CodeAgents** — agents that write their own actions as Python code rather than just generating code.

**GitHub**: [huggingface/smolagents](https://github.com/huggingface/smolagents) · **27.7k+ stars** · **Apache-2.0 License** · **Python** · **Latest Release: v1.26.0 (May 2026)**

## Key Features

- **Simplicity**: Core logic under ~1,000 lines of code. Minimal abstractions above raw code, making the framework easy to understand and modify.
- **CodeAgent**: Agents write their own actions as **Python code** (not just using code as a tool), enabling natural use of loops, conditionals, and function nesting. This approach uses **30% fewer LLM calls** compared to traditional tool-calling agents and achieves higher performance on hard benchmarks.
- **ToolCallingAgent**: Standard JSON/text-based tool calling via `ToolCallingAgent` for compatibility with standard LLM tool-calling APIs.
- **Secure Code Execution**: Sandboxed execution via Modal, Blaxel, E2B, or Docker for safe code agent operation.
- **HuggingFace Hub Integration**: Seamlessly share and load agents & tools as Gradio Spaces on the HuggingFace Hub with `push_to_hub()` and `from_hub()`.
- **Model-Agnostic**: Works with any LLM — HuggingFace Inference API, OpenAI/Anthropic (via LiteLLM), local models (Transformers/Ollama), Azure OpenAI, Amazon Bedrock, OpenRouter, Together AI, and more.
- **Modality-Agnostic**: Supports text, vision, video, and audio inputs.
- **Tool-Agnostic**: Integrate tools from MCP servers, LangChain, HuggingFace Spaces, or custom sources.
- **CLI Tools**: `smolagent` and `webagent` commands for quick agent runs without boilerplate. Interactive mode with setup wizard.

## Architecture

Smolagents uses a minimal, flat architecture:

1. **Agent Types**:
   - **`CodeAgent`**: The flagship agent type. Agents write Python code to invoke tools and compute results. Uses a ReAct loop where code is the action format.
   - **`ToolCallingAgent`**: Traditional tool-calling with JSON/text-based tool invocation for standard LLM APIs.

2. **Model Layer**: Unified model interface with provider-specific implementations:
   - `InferenceClientModel`: HuggingFace Inference API (default, no API key needed for many models).
   - `LiteLLMModel`: 100+ model providers via LiteLLM.
   - `TransformersModel`: Local model execution.
   - `OpenAIModel`: OpenAI-compatible APIs.
   - `AzureOpenAIModel`, `AmazonBedrockModel`: Cloud provider integrations.

3. **Tool System**: First-class tool abstraction:
   - Built-in tools: `DuckDuckGoSearchTool`, `PythonInterpreterTool`, `WebSearchTool`, etc.
   - `ToolCollection.from_mcp()`: Import tools from MCP servers.
   - `Tool.from_langchain()`: Import LangChain tools.
   - `Tool.from_space()`: Import tools from HuggingFace Spaces.
   - Custom tools via subclassing `Tool` and implementing `__call__()`.

4. **Code Execution**: Sandboxed environments for safe code execution:
   - Modal, Blaxel, E2B (cloud-based).
   - Docker (local).

5. **ReAct Loop (Code-Style)**: Task → Memory → Generate → Execute Code → Store Results → Repeat until `final_answer` is called.

6. **CLI Interface**: `smolagent` for general-purpose CodeAgent runs, `webagent` for vision-based browser automation using Helium.

## Use Cases

- **Quick Prototyping**: Rapid agent development with minimal boilerplate — ideal for experimentation and proof-of-concepts.
- **Code-Based Reasoning**: Tasks requiring complex logic, loops, and conditional execution where CodeAgent's code-as-action approach excels.
- **Web Research**: Agents with web search tools for information gathering and summarization.
- **Data Analysis**: CodeAgents that write Python to analyze datasets, generate visualizations, and compute results.
- **Browser Automation**: `webagent` CLI for vision-based web browsing and interaction.
- **Hub-Based Agent Sharing**: Publishing agents to HuggingFace Hub for community use and reuse.
- **Local Model Agents**: Running agents with local/open models via Transformers or Ollama for privacy-sensitive applications.
- **Multi-Modal Applications**: Agents processing text, images, video, and audio inputs.

## Pricing & Open-Source Status

- **SmolAgents**: **Free and open-source** under the Apache-2.0 License.
- **No Commercial Tier**: The framework is entirely free with no paid version.
- **Sandbox Providers**: Secure code execution backends (Modal, Blaxel, E2B) may have their own pricing for compute resources.
- **HuggingFace Hub**: Free agent and tool sharing; Inference API has free tier with rate limits.

## Latest Updates (2025-2026)

- **Latest Release**: `v1.26.0` (May 2026) with ongoing improvements to the framework.
- The framework has grown to **27.7k+ GitHub stars** and **2.6k+ forks**.
- `[toolkit]` extra package now includes default tools like `DuckDuckGoSearchTool` and `PythonInterpreterTool` out of the box.
- **CLI Tools** (`smolagent`, `webagent`) provide zero-boilerplate agent execution with interactive setup wizard.
- The framework is frequently compared to LangGraph for its simplicity — described as a "barebones" alternative that favors minimalism over complex abstractions.
- Ongoing improvements to secure code execution, model integrations, and Hub sharing capabilities.
- The project emphasizes transparency: the entire agent logic is visible in ~1,000 lines, making it ideal for learning and customization.
