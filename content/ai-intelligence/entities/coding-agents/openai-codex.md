---
title: "OpenAI Codex"
type: entity
tags: [coding-agent, openai, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

# OpenAI Codex

OpenAI's autonomous coding agent, launched as a CLI tool. Built on the `o3` / `o4-mini` reasoning models with deep code comprehension.

## Overview

- **Developer**: OpenAI
- **Backend Model**: o3, o4-mini, gpt-4.1
- **Interface**: CLI (`codex`), VS Code extension, GitHub integration
- **Pricing**: Consumption-based API pricing + ChatGPT Pro tier
- **Open Source**: Core CLI is open source (codex-rs)

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
- **Model routing**: Automatically selects cheapest capable model per subtask
- **Compact mode**: Conversation compression to manage context

## Integration

- GitHub pull request creation and review
- CI/CD pipeline integration
- MCP tool server connections

## Competitive Positioning

- Strongest in code comprehension and reasoning depth
- Direct competitor to Anthropic's Claude Code
- Model backing advantage: o3/o4-mini reasoning models

## Related

- [[openai]] — Provider
- [[claude-code]] — Competitor
- [[github-copilot]] — Related product
- [[model-selection-for-agents]] — Model selection for agent workloads
