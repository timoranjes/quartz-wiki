---
title: MCP (Model Context Protocol)
created: 2026-06-01
updated: 2026-06-02
type: concept
tags:
  - integration
  - tool-use
  - agent
sources:
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-anthropic-2026.md
  - raw/articles/llm-provider-google-gemini-2026.md
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-meta-llama-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
  - raw/articles/llm-provider-mistral-2026.md
  - raw/articles/llm-provider-cohere-2026.md
  - raw/articles/llm-provider-zhipu-ai-2026.md
  - raw/articles/llm-provider-minimax-2026.md
  - raw/articles/llm-provider-alibaba-qwen-2026.md
  - raw/articles/llm-provider-nvidia-2026.md
  - raw/articles/llm-provider-microsoft-phi-2026.md
  - raw/articles/llm-provider-stepfun-2026.md
  - raw/articles/llm-provider-perplexity-2026.md
  - raw/articles/llm-provider-moonshot-ai-2026.md
confidence: high
---

# MCP (Model Context Protocol)

## Overview

MCP is an open standard for connecting LLMs to external tools, data sources, and services. It defines a universal protocol for tool discovery, invocation, and result formatting — enabling any MCP-compatible model to use any MCP server.

## Architecture

- **MCP Host**: The LLM or application (Claude Desktop, VS Code, agent frameworks)
- **MCP Client**: Protocol handler within the host
- **MCP Server**: Tool provider (file system, database, web search, API wrapper)
- **Transport**: stdio (local), HTTP/SSE (remote), or WebSocket

## Tool Use vs MCP

| Feature | Tool Calling (Native) | MCP |
|---------|----------------------|-----|
| Definition | Provider-specific JSON schema | Universal protocol |
| Discovery | Model must be pre-trained on tools | Servers provide tool definitions at runtime |
| Portability | Locked to provider's API | Works across providers |
| Setup | Requires API key + SDK | Install MCP server + configure host |

## Provider MCP Support (2026)

| Provider | MCP Support | Notes |
|----------|-------------|-------|
| Anthropic | Native MCP in Claude Desktop | Pioneer of the protocol |
| OpenAI | MCP-compatible function calling | Function calling maps to MCP semantics |
| Google | Gemini MCP integration | Vertex AI MCP connectors |
| DeepSeek | Tool calling with MCP-compatible schemas | OpenAI-compatible endpoints support function calling |
| Meta | Llama 4 function calling | MCP server integration via llama-stack |
| xAI | Grok tool calling | MCP-compatible function schemas |
| Mistral | Function calling in Large 3, Codestral | MCP server support via Mistral platform |
| Cohere | Tool calling in Command A+ | Enterprise MCP integration |
| Alibaba Qwen | Function calling | OpenAI-compatible endpoints |
| Zhipu AI | GLM-5 function calling | Chinese tool ecosystem |
| MiniMax | Multi-modal tool calling | Image analysis tools |
| NVIDIA | Nemotron tool use | Enterprise MCP servers |
| Microsoft | Phi function calling | On-device tool integration |
| StepFun | Advisor tool use | Enterprise workflow tools |
| Perplexity | Native web search tools | Built-in MCP-like tool pipeline |
| Moonshot AI | Kimi tool use | Chinese tool ecosystem |

## Common MCP Servers

- **File system**: Read, write, search files
- **GitHub**: Repository operations, PR management
- **Web search**: Google, Bing, DuckDuckGo, Brave
- **Database**: PostgreSQL, MySQL, SQLite
- **Browser**: Playwright, Puppeteer automation
- **Custom**: Any REST API wrapped as MCP server

## Agent Integration

- **Hermes Agent**: Uses MCP for tool discovery and execution
- **Claude Code**: MCP-powered code editing, terminal access
- **OpenHands**: MCP integration for autonomous coding agents
- **Codex**: MCP-compatible tool pipeline

## Related

- [[context-windows]] — Tool definitions consume context budget
- [[prompt-caching]] — Cached tool definitions reduce repeated cost
