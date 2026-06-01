---
domain: llm-providers
type: concept
tags: [concept/optimization, concept/kv-cache, concept/inference]
aliases: [KV Cache, Key-Value Cache, Paged Attention, vLLM]
created: 2026-06-01
---
# KV Cache Optimization

## Overview
The KV cache stores key and value tensors from previous tokens during autoregressive generation. It's the dominant memory consumer during inference for long sequences and is the target of multiple optimization techniques.

## The Problem
- For a 70B model with 128K context, KV cache can exceed **50GB**
- Limits batch size and throughput
- Wastes memory on tokens that aren't attended to

## Key Optimization Techniques

### Paged Attention (vLLM)
- **Concept**: Treat KV cache like virtual memory — pages allocated on demand
- **Benefit**: Eliminates memory fragmentation, 2-4× throughput improvement
- **Adoption**: Industry standard for open-source serving

### Prefix Caching
- **Concept**: Reuse KV cache for shared prefixes across requests
- **Benefit**: Dramatic cost savings for repeated system prompts
- **See**: [[prompt-caching]]

### KV Cache Compression
- **Quantization**: INT8/INT4 KV cache with minimal quality loss
- **Eviction**: Remove less-important tokens from cache
- **Sliding Window**: Only keep recent tokens in cache (Mistral, Llama)

### Flash Attention
- **Concept**: IO-aware attention computation that minimizes memory reads
- **Benefit**: 2-3× faster attention, lower memory usage
- **Versions**: FlashAttention-1, -2, -3 (each ~2× faster than previous)
- **Adoption**: Universal across modern inference frameworks

### Sparse Attention
- **Concept**: Only compute attention over a subset of tokens
- **Benefit**: Linear rather than quadratic complexity
- **Trade-off**: Some quality degradation

## Provider Implementations

| Provider | KV Cache Technique | Notes |
|----------|-------------------|-------|
| **OpenAI** | Internal paged attention + prefix caching | Production serving stack |
| **Anthropic** | Prefix caching (90% savings) | Industry-leading cache efficiency |
| **Google** | Paged attention + semantic caching | Vertex AI optimized |
| **DeepSeek** | Engram memory (conditional KV cache) | 97% NIAH at 1M tokens |
| **Meta** | Standard paged attention | Open-source serving stack |
| **Mistral** | Sliding window attention | 256K context, efficient |

## Memory Footprint Comparison (70B model, 128K context)

| Technique | KV Cache Size | Throughput |
|-----------|--------------|------------|
| Naive FP16 | ~50 GB | 1× |
| Paged Attention FP16 | ~50 GB | 2-4× |
| Paged Attention INT8 | ~25 GB | 4-6× |
| Paged Attention INT4 | ~12.5 GB | 6-8× |

## Related
- [[prompt-caching]] — Prefix caching is a KV cache optimization
- [[context-windows]] — KV cache limits practical context window size
- [[quantization]] — KV cache can be quantized independently of model weights
