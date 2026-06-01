---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/us, provider/closed-source]
aliases: [GPT, OpenAI]
created: 2026-06-01
---
# OpenAI

## Overview
- **Founded:** 2015 (non-profit) → 2019 (capped-profit)
- **CEO:** Sam Altman
- **HQ:** San Francisco, CA
- **Key Products:** ChatGPT, GPT API, Codex, Sora, DALL-E, Whisper, o-series
- **Platform:** platform.openai.com
- **Backing:** Microsoft (deep Azure integration)
- **Revenue:** Estimated $10B+ ARR (2025)

## Strategy
Dual-track: consumer ChatGPT + API-first developer platform. 2026 transitioned from incremental updates to full retraining cycles (GPT-5.5 = first fully retrained since GPT-4.5).

## Model Lineup (2026)

| Model | Context | Input $/1M | Output $/1M | Notes |
|-------|---------|-----------|------------|-------|
| **GPT-5.5** | 1M | $5.00 | $30.00 | Flagship, natively omnimodal, Apr 2026 |
| **GPT-5.4** | 1.05M | $2.50 | $15.00 | Unified Codex+GPT line, Mar 2026 |
| **GPT-5.4 mini** | ~272K | $0.75 | $4.50 | Economy tier |
| **o3** | 200K | $10.00 | $40.00 | Reasoning model |
| **o4-mini** | 200K | $1.10 | $4.40 | Budget reasoning |

## Key Benchmarks (GPT-5.5)
- Terminal-Bench 2.0: **82.7%** (agentic CLI leader)
- GPQA Diamond: 93.6%
- ARC-AGI-2: **85.0%**
- SWE-bench Pro: 58.6%
- MRCR v2 1M: **74.0%** (long-context)
- OSWorld-Verified: 78.7%

## API & Ecosystem
- OpenAI-compatible format (industry standard)
- Native tool calling, parallel tool calling, deferred tool loading
- Structured output (JSON schema)
- Web search ($10/1K calls), containers API
- SDKs: Python, Node.js, community (Go, Java, Rust)
- Hosting: OpenAI API, Azure, OpenRouter

## Strengths
- Industry-standard API format
- Strongest agentic CLI coding (Terminal-Bench leader)
- Best long-context retrieval (+37pt vs GPT-5.4)
- Natively omnimodal (text+image+audio+video)
- Self-improving infrastructure (Codex rewrote serving stack, +20% speed)
- Broadest tool ecosystem (web search, containers, image gen)

## Recent Developments
- May 2026: GPT-5.5 default in ChatGPT
- Apr 2026: GPT-5.5 launched (fully retrained base model)
- Mar 2026: GPT-5.4 + mini launched
- Dec 2025: o3, o4-mini reasoning models

[[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
