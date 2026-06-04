---
title: "Anthropic Claude Code"
type: entity
tags: [coding-agent, anthropic, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

# Anthropic Claude Code

Anthropic's autonomous coding agent, available as a CLI tool and integrated into the Claude web interface.

## Overview

- **Developer**: Anthropic
- **Backend Model**: Claude Sonnet 4, Claude Opus 4
- **Interface**: CLI (`claude`), claude.ai web interface
- **Pricing**: API usage-based + Claude Pro/Team/Enterprise tiers
- **Open Source**: SDK and core are open source

## Key Capabilities

- Autonomous code editing with natural language instructions
- Full codebase context awareness
- Built-in terminal, file editing, and web search
- 200K+ context window for large codebase understanding
- Permission model for tool use control

## Workflow

1. User provides task description in natural language
2. Agent reads codebase, plans approach
3. Executes edits, runs tests, iterates
4. Provides summary and asks for feedback

## Notable Features

- **Permission modes**: Always allow, default (ask), read-only
- **CLAUDE.md**: Project-level instructions file for custom behavior
- **Slash commands**: `/help`, `/clear`, `/compact`, `/cost`
- **Multi-file editing**: Can modify many files in a single turn

## Competitive Positioning

- Strong in code quality and safety consciousness
- Claude Sonnet 4 offers competitive pricing for coding tasks
- Direct competitor to OpenAI Codex
- Known for more cautious, thorough approach vs. faster but riskier agents

## Related

- [[anthropic]] — Provider
- [[openai-codex]] — Competitor
- [[cursor]] — Uses Claude as one of its model backends
- [[model-selection-for-agents]] — Model selection for agent workloads
