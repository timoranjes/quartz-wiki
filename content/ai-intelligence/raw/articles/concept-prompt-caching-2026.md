---
title: Prompt Caching
researched: 2026-06-05
sources:
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/
  - https://hakkoda.io/resources/prompt-caching/
---

# Prompt Caching

## Overview

Prompt caching is an API-level optimization technique that caches the intermediate computational states (key/value tensors) for frequently used prompt prefixes, enabling dramatic reductions in both latency and cost for repeated API calls. When the same or similar prompts are sent multiple times, the cached prefix can be reused instead of being fully recomputed, reducing latency by up to 80% and input token costs by up to 90%.

Unlike KV cache (which operates within a single inference session), prompt caching works across separate API requests. It caches the intermediate attention representations — not the raw prompt text — and is automatically enabled on modern LLM APIs with no code changes required. This is particularly valuable for applications with repeated system prompts, tool definitions, or structured output schemas that remain constant across many user requests.

## Key Details

### How It Works
1. **Cache Routing**: Requests are routed based on a hash of the initial prompt prefix (~first 256 tokens)
2. **Cache Lookup**: System checks if prefix exists in cache on selected machine
3. **Cache Hit**: Reuses cached prefix → faster processing and lower cost
4. **Cache Miss**: Full prompt processed; prefix cached for future use

### Requirements
- **Minimum prompt length**: ≥ 1024 tokens for caching to apply
- **Supported models**: gpt-4o and newer (including gpt-5.5, gpt-5, gpt-4.1, etc.)
- **No extra fees**: Automatic and included at no additional cost
- **No code changes**: Enabled by default on supported models

### Cache Retention Policies
- **In-memory cache**: Up to 1 hour, typically 5-10 minutes of inactivity (GPU memory only)
- **Extended cache**: Up to 24 hours for newer models (gpt-5.5, gpt-5, gpt-4.1) using GPU-local storage
- Extended cache stores only key/value tensors, not raw prompt content

### What Can Be Cached
- Messages (system, user, assistant)
- Images (links or base64; detail param must match)
- Tools (messages + tools list)
- Structured outputs (schema prefixed to system message)

### Best Practices
- **Structure prompts**: Place static content (instructions, examples, tools, schema) at the beginning; place dynamic content (user input, IDs, timestamps) at the end
- **Use prompt_cache_key**: Helps route similar requests to the same cache node; keep unique prefix + key combinations under 15 requests/minute
- **Monitor performance**: Track `cached_tokens` in `usage.prompt_tokens_details` and hit rate via usage dashboard
- **Maintain request frequency**: Regular requests with identical prefixes reduce cache evictions

### Privacy and Security
- Caches are organization-isolated; only same-org members can access identical prompts
- Extended cache retains key/value tensors for ≤24 hours but not raw content
- Works with Zero Data Retention (ZDR): in-memory caches no data; extended caches only key/value tensors
- Works with Data Residency when using Regional Inference

### Impact on Rate Limits
- Cached tokens still count toward tokens-per-minute (TPM) rate limits
- Rate limits apply to total tokens processed, not just uncached tokens

## Sources
- https://developers.openai.com/api/docs/guides/prompt-caching
- https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/
- https://hakkoda.io/resources/prompt-caching/
