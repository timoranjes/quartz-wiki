---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/china, provider/open-weight]
aliases: [DeepSeek, 深度求索, Hangzhou DeepSeek]
created: 2026-06-01
---
# DeepSeek

## Overview
- **Full Name:** Hangzhou DeepSeek Artificial Intelligence Co., Ltd. (杭州深度求索人工智能)
- **Founded:** May 2023 (independent lab), spun out from High-Flyer July 2023
- **Founder:** Liang Wenfeng (梁文峰), net worth $16.7B
- **Parent:** Zhejiang High-Flyer Asset Management (幻方量化) — quant hedge fund, 56.6% return 2025
- **Valuation:** $20B+ (April 2026 funding); seeking $10B at >$50B valuation (May 2026)
- **Investors:** Tencent, Alibaba, state-backed funds (Big Fund III), CATL, JD.com, NetEase
- **HQ:** Hangzhou, China; Data center in Ulanqab, Inner Mongolia

## Strategy
Unconventional AI lab from quant hedge fund. Short-term monetization not priority — focus on R&D. DAU hit 200M+ (May 2026).

## Model Lineup (2026)

| Model | Total | Active | Context | License | Release |
|-------|-------|--------|---------|---------|---------|
| **V4-Pro** | 1.6T | 49B | 1M | MIT (planned) | Apr 2026 |
| **V4-Flash** | 284B | 13B | 1M | MIT (planned) | Apr 2026 |
| **V3.2** | 685B | 37B | 128K | — | Legacy |
| **R1** | 671B | 37B | 128K | — | Legacy |
| **R1 v0528** | 671B | 37B | 128K | — | May 2026 update |

## Pricing (USD per 1M tokens)

| Model | Input (hit) | Input (miss) | Output |
|-------|------------|-------------|--------|
| **V4-Flash** | $0.0028 | $0.14 | $0.28 |
| **V4-Pro** (list) | $0.0145 | $1.74 | $3.48 |
| V3.2 | — | $0.28 | $0.42 |
| R1 | — | $0.55 | $2.19 |

## Key Benchmarks (V4-Pro)
| Benchmark | V4-Pro | GPT-5.5 | Claude Opus 4.7 |
|-----------|--------|---------|-----------------|
| GPQA Diamond | 88.8–90.1% | 93.6% | ~93% |
| SWE-bench Pro | 55.4% | 58.6% | 64.3% |
| Terminal-Bench 2.0 | 67.9% | 82.7% | ~70% |
| MRCR 1M (long context) | **83.5%** | 74.0% | — |
| τ²-Bench Telecom | **96.2%** | — | — |
| AA Intelligence Index | 51.5 | 60.2 | 61.4 |

## R1 v0528 Update (May 2026)
- AIME 2025: 70% → **87.5%**
- Hallucination rate: ↓45-50%
- Trade-off: 30-60 min per task

## API & Ecosystem
- Base URL: api.deepseek.com/v1/chat/completions (OpenAI-compatible)
- Also: api.deepseek.com/anthropic/v1/messages (Anthropic-compatible)
- SDK: OpenAI Python SDK (drop-in)
- Thinking modes: Non-thinking / Think High / Think Max
- Third-party: OpenRouter, Alibaba Cloud, DeepInfra, Fireworks, NVIDIA NIM
- Coding agents: Claude Code, OpenClaw, OpenCode, CodeBuddy

## Strengths
- Extreme cost efficiency (10-107× cheaper than Western frontier)
- MoE architecture mastery (1.6T total, 49B active)
- 1M context with 97% NIAH accuracy (Engram memory)
- MIT-licensed open weights
- Consumer-grade inference (fits on single RTX 5090 at INT4)
- China chip independence (Huawei Ascend, Cambricon)
- Dual API compatibility (OpenAI + Anthropic format)

## Weaknesses
- Agentic coding gap (Terminal-Bench 67.9% vs 82.7% GPT-5.5)
- Scientific reasoning behind (GPQA 90.1% vs 93.6% GPT-5.5)
- Internal benchmarks await third-party validation
- Unprofitable, long-term sustainability unclear
- Talent retention issues (5 core R&D left for 2-3× compensation)
- Geopolitical risk
- No multimodal yet (V4.1 expected June 2026)

## Recent Developments
- May 2026: R1 v0528 update, V4 Pro permanent price cut
- May 2026: Service outage (200M+ DAU)
- Apr 2026: V4 launched (V4-Pro + V4-Flash)
- Apr 2026: First external funding ($300M+ at >$20B valuation)

[[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]]
