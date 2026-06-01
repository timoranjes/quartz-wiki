---
domain: llm-providers
type: comparison
tags: [comparison/pricing, comparison/2026Q2]
aliases: [Pricing Matrix, Cost Comparison]
created: 2026-06-01
---
# Pricing Comparison — 2026 Q2

## Flagship Models (per 1M tokens, USD)

| Provider | Model | Input | Output | Cache Read | Cache Write |
|----------|-------|-------|--------|-----------|------------|
| OpenAI | GPT-5.5 | $5.00 | $30.00 | $0.50 | — |
| Anthropic | Opus 4.8 | $5.00 | $25.00 | $0.50 | $6.25 |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | $0.15 | — |
| Meta | Llama 4 Maverick | ~$0.10 | ~$0.60 | — | — |
| xAI | Grok 4.3 | $1.25 | $2.50 | $0.20 | — |
| Mistral | Medium 3.5 | $1.50 | $7.50 | — | — |
| Alibaba | Qwen3.7 Max | $1.25–$2.50 | $3.75–$7.50 | ~80-90% off | — |
| DeepSeek | V4-Pro | $1.74 | $3.48 | $0.0145 | — |

## Mid-Tier Models

| Provider | Model | Input | Output |
|----------|-------|-------|--------|
| OpenAI | GPT-5.4 | $2.50 | $15.00 |
| Anthropic | Sonnet 4.6 | $3.00 | $15.00 |
| Google | Gemini 3.1 Pro | $2.00 (≤200K) | $12.00 (≤200K) |
| xAI | Grok Build 0.1 | $1.00 | $2.00 |
| Alibaba | Qwen3.5-Plus | $0.26 | $1.56 |
| DeepSeek | V4-Flash | $0.14 | $0.28 |

## Economy Models (cheapest per provider)

| Provider | Model | Input | Output |
|----------|-------|-------|--------|
| OpenAI | GPT-5.4 mini | $0.75 | $4.50 |
| Anthropic | Haiku 4.5 | $1.00 | $5.00 |
| Google | 3.1 Flash-Lite | $0.25 | $1.50 |
| Meta | 3rd-party API | ~$0.10 | ~$0.60 |
| xAI | Grok 4.1 Fast | $0.20 | $0.50 |
| Mistral | NeMo | $0.02 | $0.03 |
| Alibaba | Qwen3.5-0.8B | $0.01 | $0.05 |
| DeepSeek | V4-Flash (cache hit) | $0.0028 | $0.28 |

## Absolute Cheapest by Category

| Category | Winner | Model | Cost ($/1M) |
|----------|--------|-------|------------|
| **Flagship input** | DeepSeek | V4-Pro (cache hit) | $0.0145 |
| **Flagship output** | DeepSeek | V4-Pro | $3.48 |
| **Mid-tier input** | Alibaba | Qwen3.5-Plus | $0.26 |
| **Mid-tier output** | DeepSeek | V4-Flash | $0.28 |
| **Economy input** | Mistral | NeMo | $0.02 |
| **Economy output** | Mistral | NeMo | $0.03 |

## Cost Multipliers vs Cheapest Option

Using Mistral NeMo ($0.02/$0.03) as baseline:

| Provider | Flagship Input Multiplier | Flagship Output Multiplier |
|----------|-------------------------|--------------------------|
| Mistral NeMo | 1× | 1× |
| DeepSeek V4-Flash | 7× | 9× |
| Alibaba Qwen3.5-0.8B | 0.5× | 1.7× |
| xAI Grok 4.1 Fast | 10× | 17× |
| Google 3.1 Flash-Lite | 12.5× | 50× |
| OpenAI GPT-5.4 mini | 37.5× | 150× |
| Anthropic Haiku 4.5 | 50× | 167× |
| OpenAI GPT-5.5 | 250× | 1000× |
| Anthropic Opus 4.8 | 250× | 833× |

## Batch Processing Discounts

| Provider | Discount | Processing Time |
|----------|----------|----------------|
| OpenAI | 50% off | 24h async |
| Anthropic | 50% off | Async |
| Google | 50% off | Async |

## Related
- [[prompt-caching]] — Caching can reduce effective cost by 80-98%
- [[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
