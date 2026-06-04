---
title: "GitHub Copilot"
type: entity
tags: [coding-agent, github, openai, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

# GitHub Copilot

GitHub's AI coding assistant, evolved from autocomplete to full agent capabilities with Copilot Workspace. Moved to usage-based billing on June 1, 2026.

## Overview

- **Developer**: GitHub (Microsoft)
- **Backend Model**: GPT-4o, GPT-5.5, Claude (via model marketplace)
- **Interface**: IDE extensions (VS Code, JetBrains), GitHub.com, CLI (`github-copilot-cli`)
- **Pricing**: Copilot Pro ($10/mo, 1,500 AI Credits), Pro+ (with $39/mo AI Credits), Business ($19/user/mo), Enterprise (custom, up to 20,000 credits), Max (new tier)
- **Open Source**: CLI tools open source, core model proprietary

## Key Capabilities

- Code completion and generation in IDE
- Copilot Chat for conversational code assistance
- Copilot Workspace for task-level autonomous work
- PR summarization and code review
- GitHub ecosystem integration (issues, PRs, Actions)

## Recent Updates (May–June 2026)

- **Usage-based billing (June 1, 2026)**: Migrated from request-based to usage-based billing. All plans now consume GitHub AI Credits based on token usage (input, output, cached context). Code completions and next edit suggestions remain unbilled.
- **Copilot Code Review**: PR reviews now count against included Actions minutes at per-minute rates
- **New Max plan**: Higher-tier plan with increased credit allotment
- **User-level budget controls**: New spending limits and upgrade paths to Max
- **Model catalog refresh**: GPT-5.5 added, legacy model retirements (o3, GPT-4.5 sunset June 27, 2026)

## Notable Features

- **Model marketplace**: Can switch between OpenAI, Anthropic, and custom models
- **GitHub native**: Deepest integration with GitHub workflow
- **Enterprise compliance**: SOC 2, data residency controls
- **Custom instructions**: Repository-level `.github/copilot-instructions.md`
- **Usage-based pricing transparency**: AI Credits model with per-model token pricing

## Pricing Impact

The June 1, 2026 migration to usage-based billing has caused significant user concern:
- A quick chat question and multi-hour autonomous session now cost differently (token-based)
- Some heavy users report projected bills of $500–$847/month under new pricing
- Code completions remain free (not billed in AI Credits)
- Base credits consumed first, then flex allotment at same rates

## Competitive Positioning

- Dominant in IDE autocomplete market
- Agent capabilities still maturing vs. standalone CLI agents
- Unmatched GitHub integration advantage
- Model flexibility is a key differentiator
- Usage-based billing shift creates cost unpredictability concern

## Related

- [[openai]] — Primary model provider
- [[anthropic]] — Available via model marketplace
- [[openai-codex]] — Competitor
- [[claude-code]] — Competitor
- [[enterprise-ai-costs]] — Enterprise AI cost management
