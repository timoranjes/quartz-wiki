title: Enterprise AI Cost Management
tags: cost-optimization, code-generation
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


## LLM API Pricing War (2026)

LLM API prices dropped approximately **80%** between early 2025 and early 2026, driven by three structural forces:

### Cost Drivers
1. **Hardware Efficiency**: NVIDIA Blackwell, AMD MI350, and Google TPU v6 deliver ~2x YoY inference throughput per watt improvements
2. **Model Competition**: Open-weight models (Qwen, DeepSeek, Llama) force proprietary providers to cut prices
3. **Scale Economics**: Larger context windows and batch processing reduce per-token costs

### Price Examples
| Model | Early 2025 Input | Early 2026 Input | Reduction |
|-------|-----------------|-----------------|-----------|
| GPT-4o | $5.00/MTok | $2.50/MTok | 50% |
| o4 Mini | N/A | $0.55/MTok | New |
| Gemini 3.1 Flash-Lite | N/A | $0.25/MTok | New ultra-low |

**Implication for enterprise:** The cost-per-agent-hour continues to decline, making AI agent deployments increasingly economical even with heavy usage.

## Cost Observability Tools

**AgentsView** (by Wes McKinney) — local token usage analytics tool for coding agents. Provides treemap visualization of cost attribution across projects, models, and agents. Tracks cache efficiency (reads/writes/uncached), session-level costs, and supports custom model pricing for newly released models not yet in standard pricing databases. Observed usage: single Claude Fable 5 session consuming 55.9M tokens at $74.06 cost. ^[raw/sources/2026-06-09-setting-a-custom-price-for-a-model-in-agentsview.md]

## Related

- [[model-selection-for-agents]]
- [[evaluation-benchmarks]]
- [[single-vs-multi-agent]]