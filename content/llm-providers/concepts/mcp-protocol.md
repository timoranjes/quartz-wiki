---
domain: llm-providers
type: concept
tags: [concept/protocol, concept/tool-calling, concept/mcp]
aliases: [Model Context Protocol, MCP]
created: 2026-06-01
---
# Model Context Protocol (MCP)

## Overview
MCP is an open standard for connecting AI models to external data sources and tools. Created by [[anthropic]] in 2024, it has become the **industry standard** for tool/data connections.

## Purpose
- Standardize how LLMs access external resources (files, databases, APIs, tools)
- Eliminate custom integrations per provider
- Enable composable tool ecosystems

## Architecture
- **MCP Host**: The AI application (Claude, GPT, etc.)
- **MCP Client**: Protocol implementation within the host
- **MCP Server**: External resource exposing capabilities via MCP

## MCP Atlas Benchmark
Measures model performance on tool orchestration via MCP:

| Model | MCP Atlas Score |
|-------|----------------|
| Gemini 3.5 Flash | **83.6%** |
| Claude Opus 4.7 | **77.3%** |
| Claude Sonnet 4.6 | 69.5% |
| GPT-5.5 | 75.3% |

## Provider Support
| Provider | MCP Status |
|----------|-----------|
| Anthropic | **Creator** — native MCP support in Claude API and claude.ai |
| OpenAI | Supported via tool calling (not native MCP) |
| Google | Supported in Gemini API |
| DeepSeek | V4.1 expected to include MCP support (June 2026) |

## Adoption
- Growing across developer tools
- Claude's MCP Atlas benchmark tracks progress
- Open standard — any provider can implement

## Related
- [[anthropic]] — MCP protocol creator
- [[tool-calling]] — Related but distinct concept
