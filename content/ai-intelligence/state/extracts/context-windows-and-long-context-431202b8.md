title: Context Windows and Long Context
tags: inference, architecture, benchmark
# Context Windows and Long Context

## Overview

The context window defines the maximum number of tokens a model can process in a single forward pass, including both input (prompt) and output (generation). Long context capability is critical for document analysis, codebase understanding, and multi-turn agent workflows.

## Context Window Sizes (Mid-2026)

| Provider | Model | Context Window | Positional Encoding | Notes |
|----------|-------|---------------|-------------------|-------|
| Google | Gemini 3.5 Pro | 10M+ tokens | RoPE extensions | Longest publicly available |
| Meta | Llama 4 Maverick | 10M tokens | iRoPE (interleaved) | Memory + personalization at scale |
| OpenAI | GPT-5.5 | 1M tokens | RoPE | Full context retrieval |
| DeepSeek | V4 Pro / Flash | 1M tokens | CSA+HCA hybrid | 27% of V3.2 FLOPs at 1M |
| Anthropic | Claude Opus 4.8 | 1M tokens | — | Context caching synergy |
| Alibaba | Qwen3.7 Max | 256K tokens | — | Enterprise document processing |
| xAI | Grok 4.3 | 256K tokens | — | Long-form analysis |
| Moonshot | Kimi K2 | 256K tokens | — | Strong retention at full context |
| Cohere | Command A+ | 128K tokens | — | Enterprise RAG |
| Mistral | Large 3 | 128K tokens | — | Code and document analysis |
| Together AI | Hosted models | 128K-1M | vLLM optimization | Platform supports varied contexts |
| Zhipu AI | GLM-5 | 128K tokens | — | Chinese document processing |
| MiniMax | M2.5 | 204K tokens | — | Multi-modal long context |
| StepFun | Step-3.7-Flash | 128K tokens | — | Enterprise workflows |

## Long Context Benchmarks

### NIAH (Needle in a Haystack)

Tests whether a model can find a specific fact embedded in a large context:

| Model | Context Length | Retrieval Accuracy | Needle Position Robustness |
|-------|---------------|-------------------|---------------------------|
| Gemini 3.5 Pro | 10M | ~95% | Good across all positions |
| GPT-5.5 | 1M | ~98% | Uniform across positions |
| Claude Opus 4.8 | 1M | ~97% | Slight degradation at midpoint |
| DeepSeek V4 Pro | 1M | ~96% | Good with hybrid attention |
| Llama 4 Maverick | 10M | ~90% | iRoPE helps with position encoding |
| Kimi K2 | 256K | ~94% | Strong retention |

### MRCR (Multi-needle Retrieval and Comprehension)

Tests retrieval of multiple needles AND reasoning across them:

- Most models degrade significantly when asked to find and reason about multiple needles
- DeepSeek V4 Pro shows strong multi-needle performance due to CSA attention
- Gemini 3.5 Pro maintains reasonable MRCR at 1M but degrades at 10M

## Technical Challenges

- **Positional encoding degradation**: RoPE-based models lose precision at very long contexts
- **Attention dilution**: With 1M+ tokens, attention weights become diffuse
- **KV cache growth**: Context grows quadratically without optimization
- **Retrieval vs reasoning**: Finding a needle is easier than reasoning across multiple needles

## Solutions

- **Hybrid attention** (DeepSeek CSA+HCA): Combines selective detailed attention with compressed global view
- **iRoPE** (Meta): Interleaved NoPE/RoPE layers maintain position encoding at scale
- **Periodic RoPE**: Extends RoPE to longer contexts via periodic extrapolation
- **Context caching** (Anthropic/Google): Cache repeated prefixes to reduce cost

## Related

- [[kv-cache-optimization]] — Long context requires efficient KV cache management
- [[prompt-caching]] — Caching repeated prefixes reduces long context cost
- [[moE-architecture]] — MoE models have different context handling requirements