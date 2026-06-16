---
title: MCP (Model Context Protocol)
created: 2026-06-01
updated: "2026-06-17"
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

## MCP in Scientific Workflows: AgentBuild (June 2026)

**AgentBuild** (arXiv:2606.12834) demonstrates MCP + [[acp-protocol|A2A]] (Agent-to-Agent) protocol for scientific workflow automation.

### Approach
- Treats agent construction as a **workflow stage** rather than fine-tuning or prompt-and-go
- Scientist authors a **contract**: version-controlled rubric + difficulty-graded curriculum + curated external knowledge base
- Rubric-driven judge gates a meta-optimizer coding agent that edits the agent within a declared boundary
- The build **compiles the agent, not the scientist's judgment**

### Implementation
- Rietveld refinement of X-ray diffraction data through GSAS-II behind **MCP and A2A**
- Blank-harness construction run progresses through a lithium lanthanum zirconium oxide (LLZO) signal-to-noise ladder
- As base models evolve, re-running AgentBuild is a **re-tune, not a rebuild** — the scientist's authored contract remains the durable asset

### Key Insight
MCP provides the tool interface; A2A enables agent-to-agent coordination. Together they allow scientific agents to be constructed from contracts that preserve scientist judgment while automating implementation.

Sources: [arXiv:2606.12834](https://arxiv.org/abs/2606.12834) ^[raw/papers/unknown-fantastic-scientific-agents-and-how-to-build-them-agentbuild-for-rietveld-refine.md]

## MCP Evaluation Challenges (June 2026)

### MCP-Bench (via Evoflux)
- 250 tools across live MCP servers
- Small planners achieve ~3% execution feasibility at zero-shot
- Evolutionary search ([[tool-use-pattern|Evoflux]]) raises to 17-24%
- Demonstrates that MCP tool catalogs at scale expose critical weaknesses in small model planning

### ToolSense Findings
- Parametric tool retrieval over ToolBench (~47K tools): **knowledge-retrieval dissociation**
- Models with strong retrieval scores score near-random on factual probes about their tools
- Under realistic queries: performance collapses 50-64 percentage points
- Implication: MCP servers with large tool catalogs may exceed what small models can effectively navigate

## MCP Practical Limitations (June 2026)

Real-world usage reveals that MCP servers may not expose all capabilities of the underlying service:

- **Cloudflare MCP + [[claude-code]]**: Simon Willison used the Cloudflare MCP to configure WAF rules but found it **could not edit managed challenge rules** — had to switch to the Cloudflare API directly for write operations. Read-only or partial-write MCP servers are common; the protocol doesn't guarantee full API parity.
- **Implication**: MCP is best understood as a *discovery and invocation* layer, not a complete replacement for direct API access. Agent harnesses should plan for API fallback when MCP servers lack write capabilities.

Source: [Simon Willison](https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/) ^[raw/sources/2026-06-16-cloudflare-captcha-on-at-least-one-ampersand.md]

## Related

- [[context-windows]] — Tool definitions consume context budget
- [[prompt-caching]] — Cached tool definitions reduce repeated cost
- [[tool-use-pattern]] — Evoflux, ToolSense, tool workflow patterns
- [[acp-protocol]] — A2A protocol for agent-to-agent coordination
- [[evaluation-benchmarks]] — MCP-Bench, ToolSense benchmarks
- [[agent-safety]] — Containment Gap in MCP-based frameworks
