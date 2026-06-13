title: Prompt Caching
tags: inference, cost-optimization, latency
# Prompt Caching

## Overview

Prompt caching reuses previously computed KV states when the input prefix matches a prior request. Since most tokens in an API call are in the input (not output), caching repeated prefixes can reduce costs by 80-95% for the cached portion.

## Provider Implementations

### Anthropic Context Caching
- Prefix-based KV cache reuse
- **Cache hit pricing**: ~80-90% discount on cached prefix tokens
- **TTL**: Cached prefixes available for minutes to hours depending on system load
- **Use case**: System prompts, few-shot examples, repeated instructions
- **Integration**: Automatic in Claude API — no special parameters needed

### OpenAI Prompt Caching
- **Automatic**: Caches repeated prefixes automatically
- **Pricing**: Cache hits at $0.00125/M tokens (GPT-5.4) vs $2.50/M for cache miss
- **Granularity**: Works at prefix boundaries
- **Best practice**: Put reusable content (system prompts, examples) at the start

### Google Gemini Context Caching
- **Context caching**: Pin and reuse KV states for static prefixes
- **Pricing**: Significant discount for cached tokens
- **Use case**: RAG pipelines with static system prompts + document corpus

### DeepSeek Cache Hit Reduction
- **April 26, 2026**: Input cache hit prices reduced to 1/10 of launch price
- **V4 Flash cache hit**: $0.0028/M tokens (extremely low)
- **V4 Pro cache hit**: $0.003625/M tokens (with 75% promo)

## Cost Impact Example

For a request with 49K input + 1K output tokens:
- **GPT-5.4 without cache**: 49K × $2.50 + 1K × $15.00 = $0.1375 + $0.015 = **$0.15**
- **GPT-5.4 with cache hit**: 49K × $0.00125 + 1K × $15.00 = $0.00006 + $0.015 = **$0.015**
- **Savings**: ~90% reduction on input portion

## Best Practices

- Place reusable content at the **beginning** of the prompt (prefix matching)
- Use for RAG systems with static retrieval templates
- Use for few-shot prompting with fixed examples
- Not useful for one-off queries with unique inputs

## Trade-offs

- **TTL uncertainty**: Cache eviction depends on system load
- **Cold start**: First request always full price
- **Prefix requirement**: Only exact prefix matches benefit
- **Latency**: Cache lookup adds minimal latency; hit reduces overall latency

## Related

- [[kv-cache-optimization]] — Caching reuses KV states; optimization improves cache efficiency
- [[context-windows]] — Caching most beneficial for long-context prompts
- [[mcp-protocol]] — Repeated tool definitions benefit from caching