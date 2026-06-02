---
confidence: high
created: '2026-05-29T00:00:00.000Z'
sources: []
tags:
  - mcp
  - protocol
  - tool-use
  - anthropic
  - openai
  - google
title: MCP (Model Context Protocol)
type: concept
updated: '2026-06-02T00:00:00.000Z'
---
# MCP (Model Context Protocol)

The Model Context Protocol (MCP) is an open standard protocol for connecting AI models to external tools, data sources, and services. Created by Anthropic in November 2024 and subsequently open-sourced, MCP has become the dominant standard for tool integration across the AI agent ecosystem, adopted by Anthropic, Google, OpenAI, and dozens of third-party tool providers.

---

## Definition

MCP standardizes how AI models discover, invoke, and receive results from external tools. Before MCP, every agent framework implemented its own tool integration pattern — LangChain had its tool abstraction, AutoGen had its own, and each provider had proprietary function calling formats. With MCP, tools are pluggable: any MCP-compatible agent can use any MCP server without custom integration code.

## Architecture

```
Agent (Claude, GPT, Gemini, etc.)
    -> MCP Client (in agent runtime)
    -> MCP Protocol (JSON-RPC over stdio/HTTP/WebSocket)
MCP Server -> Tool (filesystem, browser, database, API, etc.)
```

### Protocol Layers

1. **Transport Layer**: stdio (local subprocess), HTTP with Server-Sent Events (remote), or Streamable HTTP (bidirectional)
2. **Protocol Layer**: JSON-RPC 2.0 with standardized methods for tool discovery, invocation, and resource access
3. **Capability Layer**: Tools declare their schemas, resources, and prompts using JSON Schema

### Transport Modes

- **stdio** — subprocess communication, most common for local tools; zero network overhead
- **HTTP/SSE** — remote servers with streaming responses; suitable for cloud-hosted tools
- **Streamable HTTP** — newer bidirectional mode enabling server-initiated messages and subscriptions

## Anthropic MCP Support

Anthropic created MCP and provides first-class support across its ecosystem:

- **Claude Desktop**: Native MCP server configuration via `claude_desktop_config.json`; users can add arbitrary MCP servers
- **Claude API**: MCP tool definitions can be passed as native tools; Anthropic's API translates MCP schemas to its tool format
- **MCP SDK**: Official Python and TypeScript SDKs for building MCP servers and clients
- **Claude Code**: Anthropic's coding agent uses MCP internally for filesystem, git, and shell tool access
- **Ecosystem**: 1000+ community MCP servers catalogued at github.com/modelcontextprotocol/servers

**Key Anthropic tools via MCP**: filesystem access, PostgreSQL queries, browser automation, Slack integration, GitHub operations, and custom API connectors.

## Google Gemini Tool Use

Google has integrated MCP support into its Gemini ecosystem alongside its native function calling:

- **Google ADK (Agent Development Kit)**: Native MCP server support for connecting Gemini agents to external tools
- **Gemini API**: Supports MCP-compatible tool definitions; Google's function calling format is largely compatible with MCP schemas
- **Vertex AI**: MCP servers can be deployed as managed services within Google Cloud, enabling enterprise tool integration
- **Gemini Extensions**: Chrome extension architecture uses MCP-like patterns for browser tool integration
- **Tool orchestration**: Gemini 2.5 Pro supports multi-tool chains where output from one MCP tool feeds into another

**Google's approach**: Parallel to MCP, Google also promotes its Agent-to-Agent (A2A) protocol for inter-agent communication, complementing MCP's agent-to-tool focus.

## OpenAI Function Calling

OpenAI pioneered function calling in its API (June 2023) and has evolved it significantly:

- **Function calling API**: Structured tool definitions with JSON Schema parameters; models output tool calls in a standardized format
- **Structured Outputs** (August 2024): Guarantees function call parameters conform exactly to the provided JSON Schema
- **Responses API** (2025-2026): Newer API with built-in tool orchestration, supporting parallel tool calls and tool result processing
- **Codex integration**: OpenAI's Codex agent uses internal tool calling patterns similar to MCP for filesystem, terminal, and browser access
- **MCP compatibility**: OpenAI's function calling schemas are compatible with MCP tool definitions; third-party MCP adapters exist

**OpenAI's position**: While OpenAI hasn't officially adopted MCP as a first-class protocol, its function calling format serves the same purpose. The ecosystem has converged on similar patterns.

## Agent Tool Orchestration

Modern agents coordinate multiple MCP tools in sophisticated workflows:

### Tool Selection Strategies

- **Single tool per turn**: Agent selects one tool, executes, then decides next action (simple, predictable)
- **Parallel tool calls**: Agent dispatches multiple independent tool calls simultaneously (faster, requires careful dependency management)
- **Tool chains**: Output from Tool A becomes input to Tool B (common in data processing pipelines)
- **Conditional branching**: Tool results determine which subsequent tools to invoke (decision trees, error recovery)

### Orchestration Frameworks

| Framework | MCP Support | Tool Orchestration | Notes |
|-----------|------------|-------------------|-------|
| **LangGraph** | Yes (via MCP adapters) | State-machine-based tool flows | Most popular for complex agent workflows |
| **Google ADK** | Native | Hierarchical agent-tool trees | Deep Gemini integration |
| **CrewAI** | Yes | Role-based tool assignment | Multi-agent tool sharing |
| **AutoGen** | Yes (via extensions) | Conversational tool negotiation | Microsoft-backed |
| **Hermes Agent** | Native | Dynamic tool selection with MCP servers | Nous Research's agent framework |

### Tool Lifecycle Management

1. **Discovery**: Agent queries MCP servers for available tools via `tools/list`
2. **Selection**: Agent chooses appropriate tool(s) based on task context
3. **Invocation**: Agent sends `tools/call` with tool name and arguments
4. **Execution**: MCP server executes tool, returns result (success, error, or partial)
5. **Processing**: Agent interprets results, decides next action
6. **Cleanup**: Long-running tools may require explicit cancellation or timeout handling

## MCP Servers in My Setup

| Server | Tools Provided | Transport |
|--------|---------------|-----------|
| mcp-obsidian | Read/write/search Obsidian notes | stdio |
| mcp-swarmvault | Knowledge graph queries | stdio |
| mcp-github | GitHub API (issues, PRs, files) | stdio |
| mcp-codex | Codex CLI session management | stdio |

## Key Operations

### Listing Tools
```yaml
# In Hermes config.yaml
mcp_servers:
  mcp-obsidian:
    command: node
    args: [path/to/obsidian-mcp/dist/index.js]
```

### Tool Call Flow
1. Agent sends `tools/list` request -> server returns available tools
2. Agent sends `tools/call` with tool name + arguments
3. Server executes tool, returns result
4. Agent processes result and decides next action

## Common Pitfalls

### 1. Server Startup Failures
- Missing dependencies (Node.js, Python packages)
- Wrong path to server binary
- Permission issues

### 2. Tool Timeout
- Long-running tools need timeout configuration
- Browser tools especially prone to hanging

### 3. Context Overflow
- MCP tool outputs count toward context window
- Large file reads can blow the budget
- **Fix:** Use pagination, filtering, or pre-processing

### 4. Credential Leaks
- MCP servers may have API keys in their config
- Never inline secrets — use environment variables
- Hermes filters secrets per server automatically

## When to Use MCP vs Native Tools

| Scenario | Use | Why |
|----------|-----|-----|
| Standard tools (search, file, terminal) | Native | Built into agent, no overhead |
| Specialized domain (Obsidian, GitHub) | MCP | Purpose-built, rich toolset |
| Custom internal APIs | MCP | Standardized interface, reusable |
| Simple HTTP calls | Native | No need for server infrastructure |

## Recent Developments (2025–2026)

- **MCP 1.0 specification** finalized with transport, protocol, and capability layers
- **Stateless MCP servers** emerged as a pattern for cloud deployment (May 2026)
- **Private MCP** support for enterprise environments with credential isolation
- **MCP + A2A combination**: Agents use MCP for tools and A2A for inter-agent coordination
- **Tool marketplace**: Growing ecosystem of reusable MCP servers for databases, APIs, and SaaS products

## Related Concepts
- [[a2a-protocol]] — Agent-to-Agent protocol (complementary to MCP's agent-to-tool focus)
- [[tool-use-pattern]] — How agents use tools effectively
- [[agent-architectures]] — Where MCP fits in the agent stack
- [[function-calling]] — OpenAI's parallel approach to tool integration
