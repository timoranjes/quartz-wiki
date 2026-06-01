---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/china, provider/open-weight]
aliases: [Qwen, Tongyi Qianwen, 通义千问, Alibaba Cloud, Tongyi Lab]
created: 2026-06-01
---
# Alibaba (Qwen / Tongyi Qianwen)

## Overview
- **Parent:** Alibaba Cloud (Alibaba Group, ~$400B market cap)
- **Lab:** Tongyi Lab (formerly DAMO Academy)
- **Founded:** April 2023 (beta), Sep 2023 (public)
- **Open-source:** 100+ open-weight models, >40M downloads, >200K HF derivatives
- **Chip Strategy:** Zhenwu M890 AI accelerator (Pingtouge division, May 2026)
- **Gartner:** Named "Emerging Leader" in Generative AI Model Providers (2026)

## Model Lineup (2026)

| Model | Architecture | Context | Input $/1M | Output $/1M | Notes |
|-------|-------------|---------|-----------|------------|-------|
| **Qwen3.7 Max** | Sparse MoE (~1T) | 1M | $1.25–$2.50 | $3.75–$7.50 | Flagship (API-only) |
| **Qwen3.7 Plus** | 35B-A3B MoE | 1M | ~$0.26 | ~$1.56 | Apache 2.0 variant |
| **Qwen3.5-Plus** | MoE | 1M | $0.26 | $1.56 | Balanced cost |
| **Qwen3.5 397B-A17B** | MoE | 262K | $0.39 | $0.90 | |
| **Qwen3.5-9B** | 9B dense | 262K | $0.04 | $0.15 | |
| **Qwen3.5-0.8B** | 0.8B dense | — | $0.01 | $0.05 | |

## Specialty Models
- Qwen3 Coder Flash (coding, 1M context, $0.195/$0.975)
- Qwen3 VL 235B-A22B (vision-language, $0.20/$0.88)
- Qwen3-Omni (multimodal text/audio/vision)

## Key Benchmarks (Qwen3.7 Max)
- GPQA Diamond: **92.4**
- SWE-bench Pro: **60.6** (#1 in China, top 3 globally)
- Terminal-Bench 2.0: 69.7
- Hallucination rate: **22.9%** (lowest among frontier)
- AA Intelligence Index: 56.6

## Qwen3.5 Benchmarks
| Benchmark | Qwen3.5 | GPT-5.2 | Claude Opus 4.6 |
|-----------|---------|---------|-----------------|
| AIME 2026 | 91.3 | 96.7 | 93.3 |
| SWE-bench Verified | 76.4 | 80.0 | 80.9 |
| Tau2-Bench | 86.7 | — | 91.6 |
| BFCL-V4 (tool use) | **72.2** | — | 55.5 |

## API & Ecosystem
- DashScope (百炼): OpenAI-compatible endpoints
- Regions: Singapore, US Virginia, mainland China
- SDKs: Python, Java, curl, OpenAI-compatible
- Free tier: 1M input + 1M output (90-day)
- Integrations: ModelScope, Bailian, Spring AI Alibaba, liteLLM, OpenRouter

## Strengths
- Best-in-class Chinese NLP
- 100+ open-weight models (Apache 2.0)
- 201 languages and dialects
- Agentic coding leadership (autonomous 35-hour runs, 1000+ tool calls)
- Full-stack: Zhenwu chip + Qwen model + Cloud platform
- Small model efficiency (9B outperforms 13× larger models)
- 1/25th cost of GPT-5.5
- Lowest hallucination rate (22.9%)

## Weaknesses
- Data residency (China-hosted, though international endpoints exist)
- Proprietary flagship models (Qwen3.7 Max API-only)
- Less third-party tooling outside China
- Organizational turbulence (Qwen architect departure, early 2026)

## Recent Developments
- May 2026: Qwen 3.7 series + Zhenwu M890 chip
- Apr 2026: Qwen3.6-35B-A3B + Qwen3.6-27B (Apache 2.0)
- Feb 2026: Qwen3.5 flagship (397B-A17B MoE)
- Early 2026: Qwen team restructured (Lin Junyang stepped down)

[[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[deepseek]]
