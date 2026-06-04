---
title: "Semantic Kernel"
type: entity
tags: [agent-framework, framework, microsoft, enterprise, csharp, python, java]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/microsoft-phi]]
  - [[../llm-providers/openai]]
  - [[../coding-agents/github-copilot]]
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge free">Free</span>
    <span class="open-weight-yes">● Open weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Agent Framework<span class="entity-meta-key">HQ</span>Redmond, US<span class="entity-meta-key">Valuation</span>Microsoft<span class="entity-meta-key">Key Models</span>Any LLM
  </div>
</div>
# Semantic Kernel

## Overview

**Semantic Kernel** is Microsoft's open-source AI orchestration framework, enabling developers to integrate large language models into applications with enterprise-grade patterns. With 27,900+ GitHub stars, it has become a cornerstone tool for enterprise AI development since its initial release in 2023.

- **GitHub Stars**: ~27,900
- **License**: MIT
- **Parent Company**: Microsoft
- **Website**: [learn.microsoft.com/semantic-kernel](https://learn.microsoft.com/en-us/semantic-kernel/)
- **GitHub**: [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)

## Architecture

### Multi-Language Support
- **C# (.NET)**: Primary language, full feature parity
- **Python**: Production-ready with agent framework
- **Java**: Growing support for enterprise Java stacks

### Agent Model
- **AI Agent**: Software entity that performs tasks autonomously by receiving input, processing information, and taking actions
- **Modular Components**: Specialized agents (data scraper, NLP processor) that can be reused or swapped
- **Collaboration**: Multiple agents working together — one collects data, another analyzes, a third decides
- **Human-Agent Collaboration**: Humans can review, refine, or override agent outputs (human-in-the-loop)
- **Process Orchestration**: Automate end-to-end workflows across systems, APIs, and tools

### Agent Types

| Agent Type | Description |
|------------|-------------|
| `ChatCompletionAgent` | Core chat-based agent with LLM + tools |
| `OpenAIAssistantAgent` | Leverages OpenAI Assistant API |
| `AzureAIAgent` | Azure AI service integration |
| `OpenAIResponsesAgent` | OpenAI Responses API integration |

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Language** | C#, Python, Java — enterprise language coverage |
| **Plugin Architecture** | Reusable plugins for skills, tools, and data sources |
| **Agent Orchestration** | Multi-agent coordination framework |
| **Human-in-the-Loop** | Review, refine, and override agent outputs |
| **Azure Integration** | Native Azure OpenAI, Azure AI Search, Azure Functions |
| **Memory & Context** | Conversation history, semantic memory, vector stores |
| **Prompt Templates** | Handlebars, Jinja, semantic function templates |
| **OpenAI Compatible** | Works with any OpenAI-compatible API |

## 2026 Updates
- **Agent Framework SDK**: Dedicated agent orchestration package
- **Orchestration Package**: Multi-agent coordination with typed workflows
- **Enterprise Adoption**: Customer service chatbots, intelligent document processing, AI-powered automation
- **Multi-Step Workflows**: Agents handling document analysis, information extraction, calculations, report generation

## Packages

### .NET (NuGet)
| Package | Purpose |
|---------|---------|
| `Microsoft.SemanticKernel` | Core libraries |
| `Microsoft.SemanticKernel.Agents.Core` | ChatCompletionAgent |
| `Microsoft.SemanticKernel.Agents.OpenAI` | OpenAIAssistantAgent |
| `Microsoft.SemanticKernel.Agents.Orchestration` | Multi-agent coordination |

### Python (PyPI)
| Module | Description |
|--------|-------------|
| `semantic-kernel.agents` | Agent framework with ChatCompletionAgent, OpenAIAssistantAgent, AzureAIAgent |

### Java (Maven)
| Package | Description |
|---------|-------------|
| `semantickernel-agents-core` | ChatCompletionAgent |
| `semantickernel-aiservices-openai` | OpenAI service integration |

## When to Use

- Enterprise .NET/Java applications requiring AI integration
- Multi-agent systems with human-in-the-loop requirements
- Document processing, customer service, and workflow automation
- Azure ecosystem applications
- Teams with existing Microsoft/Azure infrastructure

## When NOT to Use

- Python-first startups or rapid prototyping (consider [[smolagents]] or [[crewai]])
- Open-source model-heavy workflows (consider [[langchain]])
- Simple single-agent chatbots without orchestration needs
- Non-Microsoft cloud environments without Azure integration

## Related

- [[../llm-providers/microsoft-phi]] — Microsoft's open-weight model family
- [[../llm-providers/openai]] — OpenAI integration (GPT models)
- [[../coding-agents/github-copilot]] — Microsoft's coding assistant (uses Semantic Kernel patterns)
- [[autogen]] — Microsoft's conversational multi-agent framework
- [[langchain]] — Cross-provider orchestration

## Sources

- [Microsoft Learn: Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/)
- [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
- [is4.ai: Semantic Kernel 2026 Overview](https://is4.ai/blog/our-blog-1/semantic-kernel-microsoft-ai-framework-2026-426)
