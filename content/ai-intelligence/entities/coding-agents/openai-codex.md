---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge competitive">Subscription</span>
    <span class="provider-badge us">🇺🇸 OpenAI</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge autonomous"><span class="cap-icon">🤖</span> Autonomous</span>
    <span class="capability-badge multi-file"><span class="cap-icon">📁</span> Multi-File</span>
    <span class="capability-badge code-review"><span class="cap-icon">🔍</span> Code Review</span>
    <span class="capability-badge testing"><span class="cap-icon">🧪</span> Testing</span>
  </div>
</div>

title: OpenAI Codex
type: entity
tags:
  - coding-agent
  - openai
  - llm-provider
created: '2026-06-04'
updated: '2026-06-04'
status: published
confidence: high
sources: [raw/articles/coding-agent-openai-codex-2026.md]
---

# OpenAI Codex

OpenAI's autonomous coding agent, launched as a CLI tool. Now powered primarily by `gpt-5.5` (released April 2026), with support for multiple model tiers.

## Overview

- **Developer**: OpenAI
- **Backend Model**: gpt-5.5 (recommended/default), gpt-5.4, gpt-5.4-mini, gpt-5.3-codex, gpt-5.3-codex-spark (Pro only, research preview)
- **Interface**: CLI (`codex`), VS Code extension, GitHub integration, ChatGPT app
- **Pricing**: Standard: $5/$30 per 1M tokens (input/output); Pro: $30/$180; Batch: $2.50/$15
- **Open Source**: Core CLI is open source (codex-rs)
- **Context Window**: 1M tokens (API), 400K tokens (Codex CLI — auto-compaction)

## Key Capabilities

- Autonomous code editing across entire codebases
- Plan-mode for structured task decomposition before execution
- Built-in terminal execution with safety approvals
- Git-aware: understands branches, diffs, commit history
- MCP server support for tool integrations

## Workflow

1. **Plan**: Analyzes codebase, writes implementation plan
2. **Execute**: Makes edits, runs tests, iterates
3. **Review**: Summarizes changes, suggests next steps

## Notable Features

- **Sandbox mode**: Read-only, workspace-write, danger-full-access
- **Approval policy**: untrusted, on-failure, on-request, never
- **Goal Mode** (v0.133.0+, May 2026): Default-on autonomous agent runtime — define outcome + success criteria, Codex works for hours or days, persists state across sessions
- **Model routing**: Supports any Chat Completions or Responses API model (Chat Completions deprecated)
- **Compact mode**: Conversation compression to manage context
- **Conversation search** (v0.134.0): Search within conversation history
- **Modal Vim editing** (v0.129.0): `/vim` command for Vim-style editing
- **Sites Plugin** (June 2, 2026): Create, save, deploy, and inspect websites, dashboards, and web apps hosted by OpenAI. Included by default in ChatGPT Business workspaces.
- **Six new role-specific plugins** (June 2, 2026): Sales, Marketing, Finance, HR, Product, Ops
- **Codex Annotations** (June 2, 2026): Visual targeted-edit feedback system
- **Amazon Bedrock integration** (June 1, 2026): OpenAI models via AWS-managed auth and billing
- **Multi-Agent v2** (v0.137.0): Runtime choice per thread, cleaner follow-up and metadata defaults
- **Enterprise features** (v0.137.0): Monthly credit limits, cloud-managed config bundles, EDU workspaces

## Recent Updates (May–June 2026)

- **v0.137.0 (June 4, 2026)**: TUI enhancements (F13–F24 keybindings, searchable paste menus), enterprise/admin flows, remote control, Multi-Agent v2, plugin workflows
- **v0.136.0 (June 1, 2026)**: Session archiving, app-server integrations, Windows sandbox provisioning
- **Sites Plugin launch (June 2, 2026)**: Web app deployment directly from Codex
- **Role-specific plugins (June 2, 2026)**: Six new plugins for non-engineering roles
- **Amazon Bedrock (June 1, 2026)**: Codex runs on AWS infrastructure with managed auth
- **iOS v1.2026.146 (June 2, 2026)**: Face ID lock, SSH to Windows, `/side` command
- **5M+ weekly developers** using Codex (late May 2026)
- **"Intelligence at Work" event (June 2, 2026)**: OpenAI's business-focused Codex showcase

## Integration

- GitHub pull request creation and review
- CI/CD pipeline integration
- MCP tool server connections

## Competitive Positioning

- Industry-leading code comprehension with GPT-5.5 (88.7% SWE-bench, 92.4% MMLU)
- Direct competitor to Anthropic's Claude Code
- Goal Mode enables autonomous multi-hour coding sessions — unique differentiator
- 4M+ weekly active developers
- 4 major CLI releases in May 2026 alone (v0.129–v0.134)

## Related

- [[openai]] — Provider
- [[claude-code]] — Competitor
- [[github-copilot]] — Related product
- [[model-selection-for-agents]] — Model selection for agent workloads
