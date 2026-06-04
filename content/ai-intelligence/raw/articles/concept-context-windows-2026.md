---
title: Context Windows and Long Context
researched: 2026-06-05
sources:
  - https://redis.io/blog/llm-context-windows/
  - https://introl.com/blog/long-context-llm-infrastructure-million-token-windows-guide
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://agenta.ai/blog/top-6-techniques-to-manage-context-length-in-llms
---
# Context Windows and Long Context

## Overview
The context window is the maximum number of tokens (input + output) an LLM can process in a single request. It represents the model's working memory — the total prompt, retrieved documents, conversation history, and generated response that fit within one inference call.

## Current Context Windows (as of 2026)

| Model | Context Window |
|-------|----------------|
| Gemini 2.5 Pro | 2,000,000 tokens (2M) |
| Claude Sonnet 4 | 1,000,000 tokens (1M) |
| GPT-4o | 128,000 tokens |
| Claude 3.5 Sonnet | 200,000 tokens |
| Qwen2.5-1M | 1,000,000 tokens |
| Llama 3.1 | 128,000 tokens |

Context windows have expanded ~100x since early transformers (from ~2K to 1–2M tokens).

## Why Context Windows Exist: Technical Constraints

### O(n²) Self-Attention Complexity
Every token must attend to every other token:
- 10K tokens → 100M comparisons
- 100K tokens → 10B comparisons
- 1M tokens = 250x attention compute vs. 4K tokens

### KV Cache Memory Growth
Key/Value cache stores attention states for each token and grows linearly with context length:
- 1M-token KV cache ≈ 15GB per user (with NVFP4 quantization)
- 70B model + 128K tokens ≈ 42GB KV cache (excluding model weights)
- Eventually exhausts GPU memory, causing inference to slow or fail

### GPU Memory Bandwidth Bottleneck
GPUs use fast SRAM (limited capacity) and slow HBM (large capacity). Constant data shuffling limits scalability.

## Architectural Optimizations

| Technique | Description | Benefit |
|-----------|-------------|---------|
| **FlashAttention** | Tiling + recomputation to reduce memory complexity | 2–4x speedup; O(n) intermediate memory |
| **Sparse Attention** | Sliding windows, global tokens replace full attention | Reduces complexity from O(n²) to O(n) |
| **PagedAttention** | Reduces KV cache fragmentation | Higher concurrency (vLLM, TensorRT-LLM) |
| **Context Parallelism** | Partition input sequences across GPUs | 93% efficiency on 128 H100s for 405B models |
| **Ring Attention** | Coordinated communication for partial attention results | Scales to million-token contexts |
| **LongRoPE** | Extends context beyond 2M tokens via dynamic rotary embeddings | Extended position encoding |
| **Dual Chunk Attention** | Qwen2.5's approach for coherence at scale | 1M-token context support |

## KV Cache Optimization Techniques

| Technique | Benefit |
|-----------|---------|
| **NVFP4 Quantization** | 50% memory reduction, <1% accuracy loss |
| **KV Cache Offloading** | Up to 14x faster prefill vs. recomputation |
| **Prefix Caching** | 3–10x latency reduction for shared prompts |
| **KV-aware Routing** | Prevents fragmented allocations |

## The "Lost in the Middle" Problem

- **U-shaped attention**: Models attend strongly to beginning/end of context, weakly to middle
- **Recall degradation**: ~60% recall at 1M tokens → 40% of facts lost
- **Gemini-specific**: After ~20% context usage, model confuses outdated vs. current state

### Mitigations
- Place critical information at context boundaries
- Redundant retrieval of key facts
- Hybrid RAG: Combine long context with retrieval
- Chunked processing: Summarize before full context ingestion

## Large vs. Small Context Windows: Trade-offs

| Dimension | Large (128K–2M) | Small (<32K) |
|-----------|-----------------|--------------|
| **Accuracy** | Degrades beyond ~32K; lost-in-the-middle effect | Consistent attention |
| **Cost** | Higher per-token cost; prompt caching can reduce 75% | Lower per-token cost |
| **Latency** | Single-digit tokens/sec when exceeding GPU memory | 50–100 tokens/sec |
| **Use Cases** | Full-book summarization, legal docs, full codebase | Real-time agents, focused Q&A, RAG |

## Key Facts
1. Context windows have grown from ~2K to 2M tokens, but larger is not always better due to accuracy degradation and cost.
2. The O(n²) self-attention complexity is the fundamental bottleneck — FlashAttention reduces this to O(n) intermediate memory.
3. KV cache for 1M-token context requires ~15GB per user even with NVFP4 quantization.
4. Context Parallelism achieves 93% efficiency across 128 H100 GPUs for 405B models at 1M context.
5. The "lost in the middle" phenomenon causes ~40% information loss at million-token scale, requiring hybrid RAG strategies.
6. Position encoding innovations like LongRoPE and Dual Chunk Attention are critical for extending beyond training sequence lengths.

## Sources
