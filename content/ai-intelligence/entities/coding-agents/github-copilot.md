---
title: "GitHub Copilot"
type: entity
tags: [coding-agent, github, openai, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

# GitHub Copilot

GitHub's AI coding assistant, evolved from autocomplete to full agent capabilities with Copilot Workspace.

## Overview

- **Developer**: GitHub (Microsoft)
- **Backend Model**: GPT-4o, Claude (via model marketplace)
- **Interface**: IDE extensions (VS Code, JetBrains), GitHub.com, CLI (`github-copilot-cli`)
- **Pricing**: Copilot Individual ($10/mo), Business ($19/mo), Enterprise (custom)
- **Open Source**: CLI tools open source, core model proprietary

## Key Capabilities

- Code completion and generation in IDE
- Copilot Chat for conversational code assistance
- Copilot Workspace for task-level autonomous work
- PR summarization and code review
- GitHub ecosystem integration (issues, PRs, Actions)

## Workflow

- **IDE mode**: Inline completion + chat for interactive coding
- **Agent mode**: Task-level autonomous editing via Copilot Workspace
- **Review mode**: Automated PR reviews and summaries

## Notable Features

- **Model marketplace**: Can switch between OpenAI, Anthropic, and custom models
- **GitHub native**: Deepest integration with GitHub workflow
- **Enterprise compliance**: SOC 2, data residency controls
- **Custom instructions**: Repository-level `.github/copilot-instructions.md`

## Competitive Positioning

- Dominant in IDE autocomplete market
- Agent capabilities still maturing vs. standalone CLI agents
- Unmatched GitHub integration advantage
- Model flexibility is a key differentiator

## Related

- [[openai]] — Primary model provider
- [[anthropic]] — Available via model marketplace
- [[github]] — Parent company
- [[openai-codex]] — Competitor
- [[claude-code]] — Competitor
