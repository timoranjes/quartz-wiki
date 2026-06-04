---
title: "OpenAI Agents SDK - Official Agent Framework"
researched: 2026-06-05
sources:
  - url: "https://platform.openai.com/docs/guides/agents"
    title: "OpenAI Agents SDK Official Documentation"
  - url: "https://github.com/openai/openai-agents-python"
    title: "OpenAI Agents SDK Python GitHub Repository"
  - url: "https://github.com/openai/openai-agents-js"
    title: "OpenAI Agents SDK TypeScript GitHub Repository"
  - url: "https://developers.openai.com/api/docs/guides/agents/quickstart"
    title: "Agents SDK Quickstart"
  - url: "https://developers.openai.com/api/docs/guides/agents/orchestration"
    title: "Agents SDK Orchestration & Handoffs"
  - url: "https://openai.com/index/the-next-evolution-of-the-agents-sdk/"
    title: "The Next Evolution of the Agents SDK - OpenAI Blog"
tags:
  - agent-framework
  - multi-agent-orchestration
  - openai
  - open-source
---

# OpenAI Agents SDK - Official Agent Framework

## Overview

The **OpenAI Agents SDK** is a **lightweight, provider-agnostic framework** for building **multi-agent workflows** in Python and TypeScript/JavaScript. Launched in March 2025, it provides a code-first approach where your application controls the agent loop, state management, tool execution, and approval workflows. The SDK supports OpenAI's Responses API and Chat Completions API, as well as 100+ other LLMs through integrations (LiteLLM, any-llm), making it provider-agnostic despite being built by OpenAI.

**GitHub**: [openai/openai-agents-python](https://github.com/openai/openai-agents-python) · **26.9k+ stars** · **MIT License** · **Python & TypeScript** · **Latest Release: v0.17.4 (May 2026)**

## Key Features

- **Agent Definitions**: Define specialist agents with instructions, tools, guardrails, and handoffs. Clean separation of agent contracts.
- **Orchestration & Handoffs**: Multi-agent workflows where agents delegate tasks to other specialists. Deciding who owns the reply in multi-agent systems.
- **Sandbox Agents**: Introduced in v0.14.0 — agents with persistent, isolated workspaces including filesystem access, command execution, Git repositories, and state snapshots.
- **Guardrails & Human Review**: Input/output validation and safety checks with built-in mechanisms for human intervention at critical decision points.
- **Sessions**: Automatic conversation history management across runs with configurable persistence strategies.
- **Tracing & Observability**: Built-in observability for debugging and optimization, with integration support for external tracing platforms.
- **MCP Integration**: Support for Model-Context Protocol tools alongside function tools and hosted tools.
- **Realtime Agents**: Voice agents using `gpt-realtime-2` for voice-first workflows.
- **Provider-Agnostic**: While optimized for OpenAI models, supports 100+ other LLMs via LiteLLM and other integrations.
- **Memory System**: Agents extract and reuse lessons across runs with read-only/generate-only modes, multi-turn grouping, and S3-backed persistence.

## Architecture

The Agents SDK follows a modular, code-first architecture:

1. **Agent Layer**: Core agent abstraction configured with:
   - **Instructions**: System prompts defining agent behavior.
   - **Tools**: Functions, MCP tools, or hosted tools.
   - **Guardrails**: Input/output validation rules.
   - **Handoffs**: Delegation to other specialized agents.

2. **Runner Layer**: Executes agents with configurable:
   - Agent loop control and iteration management.
   - Streaming support for real-time output.
   - Continuation strategies for multi-turn interactions.

3. **Sandbox Layer** (v0.14.0+):
   - **SandboxAgent**: Agent with sandbox defaults (manifest, instructions, capabilities, run_as).
   - **Manifest**: Workspace contract defining files, directories, Git repos, environment variables, users, and mounts.
   - **SandboxRunConfig**: Per-run configuration with client selection, session management, snapshots, and concurrency limits.
   - **Supported Clients**: Local (`UnixLocalSandboxClient`), Docker (`DockerSandboxClient`), and hosted providers (Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel).

4. **Tool Layer**:
   - Function tools (Python/TypeScript functions).
   - MCP server integration.
   - Hosted tools (OpenAI platform tools).
   - Agents-as-tools (using other agents as callable tools).

5. **State & Memory Layer**:
   - **Sessions**: Conversation history with configurable storage (including Redis).
   - **Memory**: Cross-run lesson extraction and reuse with S3-backed persistence.
   - **Snapshots**: Portable sandbox state with path normalization and symlink preservation.

6. **Observability Layer**: Built-in tracing with external platform integrations for debugging and evaluation loops.

## Use Cases

- **Multi-Agent Workflows**: Complex, multi-step processes where different specialist agents handle different parts of a task.
- **Sandboxed Code Execution**: Agents that interact with real filesystems, run commands, and persist state in isolated environments.
- **Voice-First Applications**: Realtime voice agents for customer service, personal assistants, and interactive applications.
- **Enterprise Automation**: Business processes with human-in-the-loop approval stages and guardrail enforcement.
- **Repository Analysis**: Agents that clone Git repos, inspect code, and provide analysis or review.
- **Data Room QA**: Agents extracting metrics and answering questions from structured document collections.
- **Typed Application Integration**: Server-side agent logic in TypeScript or Python with direct control over tools, MCP servers, and runtime behavior.

## Pricing & Open-Source Status

- **Agents SDK**: **Free and open-source** under the MIT License (both Python and TypeScript versions).
- **Model Costs**: You pay only for model API calls using standard OpenAI API pricing, based on tokens and tool usage. The SDK itself has no additional cost.
- **Sandbox Providers**: Hosted sandbox clients (E2B, Modal, etc.) have their own pricing for compute resources.
- **Provider-Agnostic**: Can be used with non-OpenAI models via integrations, with pricing dependent on the chosen model provider.

## Latest Updates (2025-2026)

- **Launched March 2025**: Initial release of the Agents SDK in Python, followed by TypeScript/JavaScript version.
- **v0.14.0**: Introduced **Sandbox Agents** — a major capability enabling agents to interact with real filesystems, run commands, and persist state in isolated workspaces.
- **v0.17.4** (May 2026): Latest release with ongoing improvements to the SDK.
- **GA Status**: New Agents SDK capabilities are generally available to all customers via the API.
- **Memory System**: Recent addition enabling agents to extract and reuse lessons across runs with configurable persistence modes.
- **Voice Agents**: Support for `gpt-realtime-2` model enabling voice-first workflows through the SDK.
- The SDK has grown to **26.9k+ GitHub stars** (Python) with active community adoption.
- OpenAI positions the SDK for use cases where the **application owns orchestration, tool execution, approvals, and state** (vs. the Responses API for simpler one-call + tools scenarios).
- TypeScript version ([openai-agents-js](https://github.com/openai/openai-agents-js)) provides equivalent capabilities for JavaScript/TypeScript developers.
