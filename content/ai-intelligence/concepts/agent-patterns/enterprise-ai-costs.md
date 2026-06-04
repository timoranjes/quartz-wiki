---
title: "Enterprise AI Cost Management"
type: concept
tags: [cost-optimization, code-generation]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
sources:
  - "raw/sources/2026-06-03-uber-caps-usage-of-ai-tools-like-claude-code-to-manage-costs.md"
---

# Enterprise AI Cost Management

## Overview

As AI coding agents (Claude Code, Cursor, etc.) see rapid enterprise adoption, companies are facing unexpected token costs and implementing spending controls.

## Case Study: Uber (June 2026)

- **Policy:** $1,500/month per AI coding tool per employee
- **Scope:** Applies to agentic coding software (Claude Code, Cursor)
- **Design:** Per-tool limits — spending on one tool doesn't affect budget for another
- **Context:** Uber reportedly burned through its entire 2026 AI budget in 4 months

## Cost Benchmarks

| Metric | Value |
|--------|-------|
| Monthly cap per tool | $1,500 |
| Estimated annual cap (2 tools) | $36,000/engineer |
| Uber median SWE compensation | ~$330,000/year |
| AI spend as % of comp | ~11% |
| Individual subscriber cost (Anthropic/OpenAI) | ~$100/month per provider |
| Typical individual usage | ~$1,000/month per provider |

## Key Observations

- Enterprise pricing differs significantly from individual subsidized plans — individuals pay ~$100/month for usage that would cost ~$1,000/month at enterprise rates
- A $1,500/month per-tool cap suggests companies are getting meaningful value but need guardrails against runaway spending
- Per-tool limits (rather than aggregate caps) incentivize tool diversity but may increase total spend
- This is an early signal of the "token-burning" pattern becoming a real cost center at scale

## Related

- [[model-selection-for-agents]]
- [[evaluation-benchmarks]]
- [[single-vs-multi-agent]]
