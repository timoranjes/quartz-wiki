---
title: Coding Agent Comparison
description: Head-to-head comparison of autonomous and semi-autonomous coding agents
tags: [comparison, overview, coding]
draft: false
---

# Coding Agent Comparison

Which autonomous coding tool fits your workflow — from full repo access to inline edits.

## Agent Matrix

| Agent | Developer | Languages | Repo Access | Test Execution | PR Creation | Autonomous | Pricing |
|-------|-----------|:---------:|:-----------:|:--------------:|:-----------:|:----------:|---------|
| [[openai-codex\|Codex CLI]] | OpenAI | Multi | Full | Yes | Yes | Semi | Subscription |
| [[claude-code\|Claude Code]] | Anthropic | Multi | Full | Yes | Yes | Semi | API pay-per-use |
| [[cursor\|Cursor]] | Anysphere | Multi | Full | Yes | Manual | No | $20/mo |
| [[aider\|Aider]] | Paul Gauthier | Multi | Full | Yes | Yes | Semi | Free / Open |
| [[opencode\|OpenCode]] | OpenCode | Multi | Full | Yes | Yes | Semi | Free / Open |
| [[github-copilot\|Copilot]] | GitHub | Multi | Partial | No | No | No | $19/mo |
| [[gemini-cli\|Gemini CLI]] | Google | Multi | Full | Yes | Yes | Semi | API pay-per-use |
| [[amazon-nova-act\|Nova Act]] | Amazon AWS | Multi | Full | Yes | Yes | Yes | AWS pricing |

## Capability Breakdown

### Full Autonomous Agents
Agents that can plan, implement, test, and open PRs with minimal human guidance.

- [[openai-codex\|Codex CLI]] — OpenAI's terminal agent, full repo access, iterative test-fix loop
- [[claude-code\|Claude Code]] — Anthropic's agent, safety-guarded, strong at refactoring
- [[opencode\|OpenCode]] — Open-source, configurable, supports multiple model backends

### IDE-Integrated Tools
Agents that work inside your editor with human-in-the-loop.

- [[cursor\|Cursor]] — Fork of VS Code with built-in AI agent, strongest UX for pair programming
- [[aider\|Aider]] — Terminal-based, Git-aware, works with any model via LiteLLM
- [[github-copilot\|Copilot]] — Inline completions, chat, agent mode (limited autonomy)

### Emerging Players
- [[gemini-cli\|Gemini CLI]] — Google's CLI agent, tight integration with Gemini models
- [[amazon-nova-act\|Nova Act]] — AWS agent fleet management service for production UI workflows (GA Dec 2025)

## Quick Picks

- **Best for production workflows:** [[claude-code\|Claude Code]] (safety + quality)
- **Best open-source:** [[aider\|Aider]], [[opencode\|OpenCode]]
- **Best IDE experience:** [[cursor\|Cursor]]
- **Best for multi-model flexibility:** [[opencode\|OpenCode]] (plug in any provider)
- **Best value:** [[aider|Aider]] (free, works with cheap models)

## Labor Market Impact (June 2026)

Despite rapid capability gains, coding agents have **not** caused mass software engineering layoffs:

- **NY WARN Act disclosure** (March 2025): 160+ companies filed layoff notices in the first year — **not a single one** checked the "AI-related" box
- **Narayanan & Kapoor analysis** (June 2026): Even in software engineering (uniquely suited to AI disruption), mass layoffs have not materialized. The real bottlenecks are not coding speed but:
  1. **Deciding and specifying** what to build
  2. **Verifying and being accountable** for what is delivered
  3. **Deep human understanding** — of the codebase, the business, and the environment

AI accelerates the "typing code into a computer" phase, but software engineering is fundamentally about specification, verification, and judgment — not typing. Other professions with more regulatory barriers are likely even more cushioned from displacement.

Source: [Normal Tech (Narayanan & Kapoor)](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers) via Simon Willison ^[raw/sources/2026-06-14-why-ai-hasnt-replaced-software-engineers-and-wont.md]

---

*Last updated: 2026-06-17*