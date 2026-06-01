---
domain: llm-providers
type: concept
tags: [concept/optimization, concept/caching]
aliases: [KV Cache, Context Caching]
created: 2026-06-01
---
# Prompt Caching

## Overview
Prompt caching allows providers to reuse previously computed key-value (KV) pairs for repeated prompt prefixes, dramatically reducing cost and latency for repeated context.

## Provider Implementations

### Anthropic (Industry Leader)
- **Savings**: Up to **90%** on repeated prefixes
- **Cache Read**: $0.50/M (vs $5.00/M input) for Opus 4.8
- **Cache Write**: $6.25/M (one-time cost to cache)
- **Mechanism**: Automatic prefix matching across requests

### OpenAI
- **Cache Read**: $0.50/M (10× discount) for GPT-5.5
- **Cache Write**: Implicit in pricing
- **Mechanism**: Automatic for repeated prefixes

### Google
- **Semantic Caching**: $0.15/1M tokens for 3.5 Flash
- **Mechanism**: Content-aware caching (not just prefix matching)

### DeepSeek
- **Auto-caching**: No opt-in needed
- **Cache Hit**: $0.0028/M (1/50th of cache-miss for Flash)
- **Threshold**: ≥1,024 token prefix match
- **Savings**: 98%+ discount on cache hits

### xAI
- **Cached Input**: $0.20/M (vs $1.25/M) for Grok 4.3
- **Mechanism**: Automatic for repeated prefixes

### Alibaba Qwen
- **KV Cache**: ~80-90% discount on cache reads via DashScope

## Cost Impact Example
For a workflow with 80% cache hit rate on 1M token inputs:
- Anthropic Opus 4.8: ~$1.25/M effective (vs $5.00)
- DeepSeek V4-Flash: ~$0.028/M effective (vs $0.14)
- **Caching makes long-context workflows economically viable**

## When Caching Works Best
- System prompts + long context documents
- Repeated codebase analysis
- Multi-turn conversations with stable context
- Batch processing with shared prefixes

## Related
- [[moE-architecture]] — Complementary cost optimization
- [[context-windows]] — Caching becomes more valuable with larger contexts
