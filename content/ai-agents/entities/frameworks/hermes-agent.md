---
title: Hermes Agent
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [framework, platform, open-source]
sources: []
confidence: high
---

# Hermes Agent

## Overview

An open-source AI agent framework running locally on macOS. Provides multi-profile routing, tool orchestration, subagent delegation, cron scheduling, and cross-platform messaging.

## Key Features

### Tool Orchestration
- 50+ built-in tools (web search, browser, terminal, file ops, image generation, etc.)
- MCP server integration (Obsidian, GitHub, SwarmVault, Codex)
- Tool filtering per subagent profile

### Multi-Profile System
- Named profiles with isolated skills, plugins, cron jobs, and memories
- Model routing per profile (coder, reviewer, researcher, analyst, writer)
- Disabled toolsets per profile for security

### Subagent Delegation
- `delegate_task()` for spawning isolated workers
- Up to 3 concurrent workers (configurable)
- Orchestrator mode for nested delegation (up to 2 levels)
- ACP support for external coding agents (OpenCode, Codex, Claude Code)

### Automation
- Cron jobs with configurable schedules, delivery channels, and scripts
- Two-stage pipeline support (no_agent fetch + agent-driven synthesis)
- Watch mode for git repo monitoring

### Cross-Platform Messaging
- Discord, Telegram, WhatsApp (wacli), iMessage, Signal
- Native media delivery (images, audio, files)
- Channel-specific routing

## My Configuration

### Profiles
| Profile | Model | Purpose |
|---------|-------|---------|
| coder | MiniMax-M2.5 | Code fixes, PRs |
| reviewer | glm-5 | Code review |
| researcher | qwen3.6-plus | Web research |
| analyst | glm-5 | Data analysis |
| writer | qwen3.6-plus | Content generation |

### Key Skills
- `llm-wiki` — Karpathy-style knowledge base management
- `subagent-driven-development` — Algorithmic task decomposition
- `portfolio-alert-system` — Stock monitoring and alerts
- `kanban-orchestrator` — Complex project management

### Cron Jobs
- AI Supply Chain Wiki daily ingestion (08:00 HKT)
- Portfolio alerts (market hours)
- Market briefs (morning)

## When to Use Hermes
- Complex multi-step tasks requiring multiple tools
- Automated monitoring and ingestion pipelines
- Cross-platform communication needs
- When you need persistent memory across sessions

## When NOT to Use
- Simple one-off queries (use direct model API)
- Tasks requiring specialized frameworks (LangChain chains, CrewAI crews)
- When you need fine-grained control over agent loop internals

## Related
- [[mcp-protocol]] — how Hermes connects to MCP servers
- [[orchestrator-workers]] — delegate_task implementation
- [[cost-optimization]] — Hermes model routing
