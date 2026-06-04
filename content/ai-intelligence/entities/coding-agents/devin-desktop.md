---
title: "Devin Desktop"
type: entity
tags: [coding-agent, ide, acp, multi-agent]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

# Devin Desktop

Agent-first IDE developed by Cognition, rebranded from Windsurf on June 2, 2026. Features the Agent Command Center as its default surface, supporting multiple coding agents via the open Agent Client Protocol (ACP).

## Overview

- **Developer**: Cognition
- **Previous Name**: Windsurf (rebranded June 2, 2026)
- **Backend Models**: Devin (native), Codex, Claude Agent, OpenCode, any ACP-compatible agent
- **Interface**: Desktop IDE (VS Code compatible, macOS, Windows, Linux)
- **Pricing**: Pro ($20/mo), Teams ($40/user/mo), Max ($200/mo)
- **Open Source**: Core editor based on VS Code; ACP protocol is open source

## Key Capabilities

- **Agent Command Center**: Kanban view for managing all local and cloud agents in one place
- **Spaces**: Shared context layer grouping agent sessions, PRs, files, and context objects
- **ACP Support**: Run Codex, Claude Agent, OpenCode, and custom agents inside the IDE
- **Devin Local**: Rust-rewritten local agent, 30% more token-efficient than legacy Cascade, supports subagents
- **Devin Cloud**: Autonomous long-running agent on remote VMs
- **Multi-agent orchestration**: Dispatch and monitor multiple agents from a single interface

## Devin Local vs Cascade

| Feature | Cascade (legacy) | Devin Local |
|---------|-----------------|-------------|
| Language | Python | Rust |
| Token Efficiency | Baseline | ~30% more efficient |
| Subagents | No | Yes (parallel, specialized) |
| Status | Deprecated, EOL July 1, 2026 | Default local agent |

## Agent Client Protocol (ACP)

Devin Desktop is the largest single ACP adoption event to date. ACP (created by Zed Industries, Aug 2025) is an open standard for connecting AI coding agents to editors — the "LSP for AI agents."

**Supported agents at launch**: Codex, Claude Agent, OpenCode, any custom ACP-compatible agent.

## Devin Ecosystem

- **Devin Desktop**: Agent manager with full IDE
- **Devin Cloud**: Autonomous cloud-based agent
- **Devin CLI**: Terminal intelligence
- **Devin Review**: Code review on every diff

## Competitive Positioning

- Positioned as the "Switzerland" of AI coding — agent-neutral via ACP
- Agent Command Center differentiates from editor-first competitors
- Strong multi-agent orchestration, early leader in agent management UX
- Adopted by Ramp, Harvey, NVIDIA, Modal, Intact Financial as design partners
- Direct competitor to Cursor (IDE), Claude Code (agent depth), Codex (ecosystem)

## Notable Adopters

- **Ramp**: Uses Devin Desktop to dispatch and monitor agent array from single command center
- **Harvey**: Runs internal background agent (Spectre) via Devin Desktop's custom agent support
- **NVIDIA**: Multi-agent support research preview partner
- **Modal**: Design partner for multi-agent workflows

## Related

- [[acp-protocol]] — Agent Client Protocol
- [[openai-codex]] — Supported agent via ACP
- [[claude-code]] — Supported agent via ACP
- [[opencode]] — Supported agent via ACP
- [[cursor]] — Direct IDE competitor
- [[model-commoditization]] — Agent-neutral positioning
