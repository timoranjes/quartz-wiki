---
title: "Semantic Kernel - Microsoft AI Application Framework"
researched: 2026-06-05
sources:
  - url: "https://learn.microsoft.com/en-us/semantic-kernel/overview/"
    title: "Semantic Kernel Official Documentation"
  - url: "https://github.com/microsoft/semantic-kernel"
    title: "Semantic Kernel GitHub Repository"
  - url: "https://github.com/microsoft/semantic-kernel-java"
    title: "Semantic Kernel for Java GitHub Repository"
  - url: "https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel"
    title: "Semantic Kernel to MAF Migration Guide"
  - url: "https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/"
    title: "Semantic Kernel and Microsoft Agent Framework - Microsoft DevBlog"
tags:
  - agent-framework
  - microsoft
  - multi-language
  - enterprise
  - open-source
  - maintenance-mode
---

# Semantic Kernel - Microsoft AI Application Framework

## Overview

Semantic Kernel (SK) is a **lightweight, open-source development kit** from Microsoft that enables developers to build AI agents and integrate the latest AI models into **C#, Python, or Java** codebases. It serves as an efficient middleware for rapid delivery of enterprise-grade AI solutions, combining prompts with existing APIs to perform actions through model function calling. As of April 2026, Semantic Kernel has been **succeeded by Microsoft Agent Framework (MAF)** and will receive only minimal security and bug fixes.

**GitHub**: [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) · **28.1k+ stars** · **MIT License** · **Python/C#/Java** · **Latest Release: python-1.43.0 (Jun 2026)** · **Status: Succeeded by MAF**

## Key Features

- **Multi-Language Support**: Native SDKs for **C# (.NET 10.0+)**, **Python (3.10+)**, and **Java (JDK 17+)** with version 1.0+ support across all three languages.
- **Model Flexibility**: Supports OpenAI, Azure OpenAI, HuggingFace, NVIDIA NIM, and local models (Ollama, LMStudio, ONNX). Future-proof design allows swapping models without rewriting the entire codebase.
- **Plugin Ecosystem**: Native functions, prompt templates, OpenAPI specifications (compatible with Microsoft 365 Copilot), and Model Context Protocol (MCP) support.
- **Agent Framework**: Modular agents with tools/plugins, memory, and planning capabilities.
- **Multi-Agent Systems**: Orchestrate collaborating specialist agents (e.g., triage → billing → refund workflows).
- **Process Framework**: Structured workflow modeling for business processes with deterministic execution patterns.
- **Vector Database Support**: Azure AI Search, Elasticsearch, Chroma, SQL Server (with `VECTOR_SEARCH()`), and other vector stores.
- **Multimodal**: Text, vision, and audio input support.
- **Enterprise Ready**: Telemetry support, hooks and filters, observability, security features, and stable APIs committed to non-breaking changes.
- **Local Deployment**: Ollama, LMStudio, and ONNX support for on-premise and edge deployments.

## Architecture

Semantic Kernel uses a modular, middleware-oriented architecture:

1. **Kernel**: The central orchestrator that manages AI services, plugins, and function execution. Acts as the middleware between AI models and application code.

2. **Connectors**: Model-agnostic interfaces for AI services:
   - **Chat Completion**: LLM text generation (OpenAI, Azure OpenAI, HuggingFace, Ollama, etc.).
   - **Text Embedding**: Embedding generation for vector operations.
   - **Text-to-Image**: Image generation services.
   - **Audio-to-Text**: Speech recognition services.

3. **Plugins (Functions)**: The core extensibility mechanism:
   - **Native Functions**: Traditional code functions annotated with `@kernel_function` (Python) or equivalent attributes in C#/Java.
   - **Prompt Functions**: Templates combining instructions with model parameters.
   - **OpenAPI Plugins**: Import OpenAPI specifications as callable plugins.
   - **MCP Plugins**: Model Context Protocol server integration.

4. **Agent Layer**:
   - **ChatCompletionAgent**: Agent backed by chat completion models.
   - **Agent Group Chat**: Multi-agent collaboration with orchestrated conversation flow.
   - **Agents as Plugins**: Agents can be wrapped as callable plugins within the kernel.

5. **Process Framework**: Structured workflow modeling for business processes with step definitions, state management, and conditional execution.

6. **Memory & Vector Search**: Integration with vector databases for semantic search and RAG patterns.

7. **Telemetry & Observability**: Built-in support for OpenTelemetry, logging, and custom hooks/filters for enterprise monitoring.

## Use Cases

- **Business Process Automation**: Combining prompts with existing APIs to automate workflows (e.g., customer service triage, order processing).
- **Enterprise AI Integration**: Integrating AI capabilities into existing C#, Python, or Java enterprise applications.
- **Multi-Agent Collaboration**: Specialist agent teams for complex tasks requiring multiple domains of expertise.
- **Microsoft 365 Copilot Extensions**: Building extensions compatible with Microsoft 365 Copilot using OpenAPI specifications.
- **RAG Applications**: Retrieval-augmented generation with vector database integration.
- **Local AI Deployments**: On-premise AI applications using Ollama, LMStudio, or ONNX models.
- **Legacy System Modernization**: Adding AI capabilities to existing enterprise codebases without major rewrites.

## Pricing & Open-Source Status

- **Semantic Kernel**: **Free and open-source** under the MIT License.
- **Status**: **Succeeded by Microsoft Agent Framework (MAF)** as of April 2026. SK will continue receiving only minimal security and bug fixes.
- **MAF**: The successor framework provides enterprise-grade, multi-language (.NET & Python) support with stable APIs, long-term support, and cross-runtime interoperability (A2A, MCP).
- **No Commercial Tier**: The SDK itself is entirely free; model API costs depend on the chosen AI service provider.

## Latest Updates (2025-2026)

- **Succession to MAF**: In April 2026, Microsoft announced that Semantic Kernel has been succeeded by the **Microsoft Agent Framework (MAF)** v1.0. This represents a strategic consolidation of Microsoft's AI agent frameworks, merging learnings from both Semantic Kernel and AutoGen.
- **Latest Release**: `python-1.43.0` (Jun 3, 2026) — likely a final security/bug-fix release.
- **Migration Guide**: Comprehensive migration path available at [learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel).
- The framework has **28.1k+ GitHub stars** and **438+ contributors** across Python, C#, and Java repositories.
- Semantic Kernel reached **Version 1.0+** support across C#, Python, and Java, with committed non-breaking change guarantees.
- Java and Python versions reached General Availability in 2024, completing the multi-language support strategy.
- Key strategic insight: Microsoft's agent framework evolution (AutoGen → maintenance, SK → succeeded, MAF → future) reflects a move toward a unified, enterprise-grade agent platform with stable APIs and long-term support commitments.
