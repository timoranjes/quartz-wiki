title: Agent Client Protocol (ACP)
tags: protocol, acp, coding-agent, agent-editor
# Agent Client Protocol (ACP)

Open standard for connecting any AI coding agent to any compatible code editor. Created by Zed Industries in August 2025, ACP is often described as the "LSP for AI coding agents."

## Overview

- **Creator**: Zed Industries (August 2025)
- **Purpose**: Standardize communication between code editors and AI coding agents
- **Transport**: JSON-RPC 2.0 over stdin/stdout
- **Adoption**: JetBrains, Google, GitHub, Devin Desktop, and 25+ agents by June 2026
- **Open Source**: Yes — [github.com/agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol)

## How It Works

1. **Bootstrapping**: `session/new` handshake between editor and agent
2. **MCP Integration**: Agents can declare MCP servers to connect during handshake
3. **Agent Discovery**: ACP Agent Registry (JetBrains) lets users find and connect agents
4. **Context Sharing**: Editors provide codebase context; agents return edits, diffs, and status

## ACP vs MCP

| | ACP | MCP |
|---|---------|---------|
| **Purpose** | Agents ↔ Editors | Agents ↔ Tools & Data |
| **Creator** | Zed Industries (Aug 2025) | Anthropic (late 2024) |
| **Transport** | JSON-RPC 2.0 over stdio | JSON-RPC 2.0 over stdio or HTTP |
| **Analogy** | LSP for AI agents | API gateway for agent tools |
| **Adopters** | Zed, JetBrains, Google, GitHub, Devin Desktop | Most AI providers & tool vendors |

ACP and MCP are complementary: ACP connects agents to editors; MCP connects agents to external tools and data sources.

## Key Adopters

- **Editors/IDEs**: Zed, JetBrains (IntelliJ, PyCharm, etc.), Google (Antigravity), GitHub, Devin Desktop
- **Agents**: Codex (OpenAI), Claude Agent (Anthropic), OpenCode, Kimi CLI, and 25+ others
- **Largest single adoption event**: Devin Desktop rebrand (June 2, 2026) — made ACP the default protocol for its Agent Command Center

## Significance

ACP enables agent-neutral IDEs. Before ACP, each coding agent was locked to its own editor interface. With ACP:
- Any ACP-compatible agent can run inside any ACP-compatible editor
- Devin Desktop can run Codex, Claude Agent, and custom agents side-by-side
- JetBrains IDEs can host any ACP agent via the ACP Agent Registry
- Developers can switch agents without switching editors

This mirrors how LSP standardized language support across editors — ACP standardizes agent support.

## Technical Details

- **Protocol**: JSON-RPC 2.0
- **Transport**: stdin/stdout (same as LSP)
- **Session model**: `session/new` → `session/initialize` → request/response loop → `session/exit`
- **MCP declaration**: Agents can declare which MCP servers they need during handshake
- **Registry**: JetBrains maintains an ACP Agent Registry for discoverability

## Related

- [[mcp-protocol]] — Model Context Protocol (complementary tool standard)
- [[devin-desktop]] — Major ACP adopter (June 2026)
- [[opencode]] — Open-source ACP-compatible agent
- [[coding-agent]] — Agent category