---
title: MCP (Model Context Protocol)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [mcp, protocol, tool-use]
sources: []
confidence: high
---

# MCP (Model Context Protocol)

## Definition

Standardized protocol for connecting AI models to external tools and data sources. Created by Anthropic, now an open standard adopted by multiple vendors.

## Why It Matters

Before MCP: every agent framework had its own tool integration pattern. With MCP: tools are pluggable, and any MCP-compatible agent can use any MCP server.

## Architecture

```
Agent (Claude, GPT, etc.)
    -> MCP Client
    -> MCP Protocol (JSON-RPC over stdio/HTTP)
MCP Server -> Tool (filesystem, browser, database, etc.)
```

### Transport Modes
- **stdio** — subprocess communication, most common for local tools
- **HTTP/SSE** — remote servers, streaming responses
- **Streamable HTTP** — newer bidirectional mode

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

## Related Concepts
- [[a2a-protocol]] — Agent-to-Agent protocol (complementary to MCP)
- [[tool-use-pattern]] — How agents use tools effectively
- agent-architecture — Where MCP fits in the stack
