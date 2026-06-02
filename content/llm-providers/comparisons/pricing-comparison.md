---
title: Pricing Comparison
created: 2026-06-01
updated: 2026-06-02
type: comparison
tags:
  - pricing
  - cost-comparison
sources:
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-anthropic-2026.md
  - raw/articles/llm-provider-google-gemini-2026.md
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-meta-llama-2026.md
  - raw/articles/llm-provider-alibaba-qwen-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
  - raw/articles/llm-provider-mistral-2026.md
  - raw/articles/llm-provider-cohere-2026.md
  - raw/articles/llm-provider-minimax-2026.md
  - raw/articles/llm-provider-microsoft-phi-2026.md
  - raw/articles/llm-provider-moonshot-ai-2026.md
  - raw/articles/llm-provider-stepfun-2026.md
  - raw/articles/llm-provider-perplexity-2026.md
  - raw/articles/llm-provider-together-ai-2026.md
  - raw/articles/llm-provider-zhipu-ai-2026.md
confidence: high
---

# Pricing Comparison

## API Pricing (Mid-2026)

All prices in USD per million tokens. Cache hit prices shown where available.

### Flagship Models

| Provider | Model | Input (Cache Hit) | Input (Cache Miss) | Output | Context |
|----------|-------|------------------|-------------------|--------|---------|
| DeepSeek | V4 Pro | **$0.004** | **$0.44** | **$0.87** | 1M |
| DeepSeek | V4 Flash | **$0.003** | **$0.14** | **$0.28** | 1M |
| OpenAI | GPT-5.5 | — | $5.00 | $30.00 | 1M |
| OpenAI | GPT-5.4 | — | $2.50 | $15.00 | 1M |
| Anthropic | Claude Opus 4.6 | — | $5.00 | $25.00 | 1M |
| Anthropic | Claude Opus 4.1 | — | $15.00 | $75.00 | 1M |
| Google | Gemini 3.5 Pro | — | $2.50 | $10.00 | 10M+ |
| Google | Gemini 3.1 Pro | — | $2.00 | $12.00 | 1M |
| Alibaba | Qwen3.7 Max | — | $0.50 | $2.00 | 256K |
| xAI | Grok 4.3 | — | $3.00 | $15.00 | 256K |
| Mistral | Large 3 | — | $0.70 | $0.70 | 128K |
| Cohere | Command A+ | — | $2.00 | $6.00 | 128K |
| Moonshot | Kimi K2 | — | $1.00 | $4.00 | 256K |
| MiniMax | M2.5 | — | $0.35 | $1.40 | 204K |
| StepFun | Step-3.7-Flash | — | $0.50 | $2.00 | 128K |
| Zhipu AI | GLM-5 | — | $0.80 | $3.20 | 128K |

### Cost Leader Analysis

**DeepSeek dominates on price:**
- V4 Flash output at $0.28/M vs GPT-5.4 at $15.00/M — **54× cheaper**
- V4 Pro at $0.87/M output vs Claude Opus 4.6 at $25.00/M — **29× cheaper**
- With cache hit pricing at $0.003/M input, DeepSeek is **800× cheaper** than GPT-5.4 for repeated prefixes

**Budget-friendly tier:**
- DeepSeek V4 Flash: $0.14 input / $0.28 output
- MiniMax M2.5: $0.35 input / $1.40 output
- Mistral Large 3: $0.70 input / $0.70 output

**Premium tier:**
- Claude Opus 4.1: $15.00 input / $75.00 output (highest)
- GPT-5.5: $5.00 input / $30.00 output
- Claude Opus 4.6: $5.00 input / $25.00 output

## Hosting Platform Pricing

| Platform | Base Markup | GPU Type | Notes |
|----------|------------|----------|-------|
| Together AI | +20-40% over API | H100/B200 | Batch processing discounts |
| NVIDIA NIM | Enterprise pricing | DGX Cloud | Full stack optimization |
| Perplexity API | — | — | Search-focused, included in Pro plan |

## Cost per Session Example

50K input + 10K output × 20 requests/day:

| Model | Daily | Monthly |
|-------|-------|---------|
| DeepSeek V4 Flash | $0.20 | $6 |
| DeepSeek V4 Pro | $2.43 | $73 |
| MiniMax M2.5 | $5.60 | $168 |
| Mistral Large 3 | $8.40 | $252 |
| GPT-5.4 | $17.50 | $525 |
| Claude Opus 4.6 | $30.00 | $900 |
| Claude Opus 4.1 | $90.00 | $2,700 |

## Related

- [[context-windows]] — Longer context increases per-request cost
- [[prompt-caching]] — Caching reduces input costs by 80-95%
- [[quantization]] — Quantized models cheaper to serve
