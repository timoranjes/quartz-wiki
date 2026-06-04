---
title: "Anthropic Claude Code"
type: entity
tags: [coding-agent, anthropic, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
sources:
  - raw/articles/coding-agent-claude-code-2026.md
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge premium">Premium</span>
    <span class="provider-badge us">🇺🇸 San Francisco (Anthropic)</span>
  </div>
  <div class="entity-meta">
    <div><span class="entity-meta-key">Model</span><span class="entity-meta-value">Opus 4.5 / Sonnet 4.5</span></div>
    <div><span class="entity-meta-key">Capability</span><span class="entity-meta-value">Dynamic Workflows</span></div>
    <div><span class="entity-meta-key">SWE-bench</span><span class="entity-meta-value">Verified 87.6%</span></div>
  </div>
</div>


# Anthropic Claude Code

Anthropic's autonomous coding agent, available as a CLI tool and integrated into the Claude web interface. Powered by Claude Opus 4.8 (May 2026) for deepest reasoning.

## Overview

- **Developer**: Anthropic
- **Backend Model**: Claude Opus 4.8 (default), Claude Sonnet 4.6 (cheaper turns)
- **Interface**: CLI (`claude`), claude.ai web interface
- **Pricing**: Base (~$20/mo, Claude Pro), Max ($200/mo, 20× limits), Teams (custom)
- **Open Source**: SDK and core are open source

## Key Capabilities

- Autonomous code editing with natural language instructions
- Full codebase context awareness
- Built-in terminal, file editing, and web search
- 200K+ context window for large codebase understanding
- Permission model for tool use control
- **Dynamic Workflows**: Adaptive task decomposition and execution
- **Subagents**: Parallel task execution for independent work items
- **LSP Support**: Language Server Protocol integration for real-time code analysis
- **Async Sub Agents**: Background task execution for parallel processing
- **Ultrathink**: Enhanced deep reasoning mode for complex tasks
- **Slack Handover**: Ability to hand off tasks via Slack integration
- **AutoCloud**: Cloud-based execution support

## Recent Updates (May–June 2026)

- **Claude Opus 4.8 (May 28, 2026)**: New default model — SOTA reasoning (GPQA 92%), coding (SWE-bench Verified 87.6%), 1M context
- **Dynamic Workflows**: Adaptive task decomposition for complex multi-step work
- **Limits doubled (May 6, 2026)**: Increased usage limits for Pro and Max tiers
- **Anthropic S-1 filing (June 1, 2026)**: Confidentially submitted draft S-1 to SEC — IPO preparation
- **$65B Series H (May 28, 2026)**: Raised at $965B post-money valuation
- **Project Glasswing expanded (June 2, 2026)**: AI security initiative with AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks
- **Claude Partner Network (June 3, 2026)**: New Services Track and Partner Hub launched

## Notable Features

- **Permission modes**: Always allow, default (ask), read-only
- **CLAUDE.md**: Project-level instructions file for custom behavior
- **Slash commands**: `/help`, `/clear`, `/compact`, `/cost`
- **Multi-file editing**: Can modify many files in a single turn
- **MCP support**: Model Context Protocol for third-party tool integrations

## Competitive Positioning

- Strong in code quality and safety consciousness
- Claude Opus 4.8 is current #1 by AA Intelligence Index (61.4)
- Best for architectural refactors and multi-file reasoning
- Direct competitor to OpenAI Codex
- Known for more cautious, thorough approach vs. faster but riskier agents
- Supports ACP protocol — can run inside ACP-compatible editors (Devin Desktop, JetBrains)

## Related

- [[anthropic]] — Provider
- [[openai-codex]] — Competitor
- [[cursor]] — Uses Claude as one of its model backends
- [[model-selection-for-agents]] — Model selection for agent workloads
- [[acp-protocol]] — Supported protocol for editor integration
