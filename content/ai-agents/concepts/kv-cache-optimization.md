
# KV Cache Optimization

KV cache optimization encompasses techniques for managing the key-value cache that stores intermediate attention computations during LLM inference. The KV cache grows linearly with sequence length and batch size, often becoming the primary memory bottleneck for long-context generation.

---

## Definition

During autoregressive generation, an LLM must attend to all previously generated tokens at each step. Recomputing attention for all previous tokens at every step would be prohibitively expensive. Instead, models cache the key and value vectors for each token — the **KV cache** — enabling O(1) attention computation per new token. The trade-off: the cache grows linearly with context length and batch size, consuming significant GPU memory.

## Core Techniques

### Paged Attention

**Paged Attention** (vLLM) applies virtual memory paging concepts to KV cache management. Instead of requiring contiguous GPU memory blocks, the KV cache is divided into fixed-size blocks that can be allocated and freed dynamically, like OS page tables. This enables:

- **Higher throughput**: 2–4× improvement by reducing memory fragmentation
- **Continuous batching**: Multiple requests can share GPU memory efficiently
- **Longer sequences**: Non-contiguous allocation enables sequences that wouldn't fit in contiguous memory
- **Zero-copy swapping**: Pages can be swapped to CPU memory without reorganization

Paged Attention is the foundation of vLLM, the most widely adopted open-source serving framework, used by Together AI, Groq, and many other inference providers.

### Flash Attention / Flash Attention 2 / Flash Attention 3 / Flash Attention 4

**Flash Attention** is an I/O-aware exact attention algorithm that minimizes memory reads/writes between GPU HBM (high-bandwidth memory) and on-chip SRAM. Instead of materializing the full attention matrix in HBM, Flash Attention computes attention in tiles, keeping intermediate results in fast on-chip memory.

- **Flash Attention 2**: Reduced synchronization overhead, better parallelism across warps and thread blocks
- **Flash Attention 3**: Further optimized for Hopper architecture (H100), supports FP8 precision, achieves 1.5–2× speedup over FA2 on H100
- **Flash Attention 4** (2025–2026): Optimized for Blackwell architecture (B200), supports FP4 precision for training, introduces block-sparse attention patterns that skip low-attention token pairs, achieves up to 3× speedup over FA2 on Blackwell GPUs

Flash Attention is used by DeepSeek, Qwen, and most modern training and inference frameworks. During training, it reduces memory footprint and increases throughput by 2–3× over naive attention. Flash Attention 4's FP4 support enables training at half the memory cost of FP8, critical for trillion-parameter models.

### KV Cache Compression

KV cache compression reduces the memory footprint of cached key-value vectors through:

- **Quantization**: Storing KV entries in INT8 or INT4 instead of FP16/BF16
- **Token pruning**: Evicting low-attention tokens from the cache when memory is constrained
- **Prefix sharing**: Reusing KV cache entries across requests with shared prefixes
- **Layer-wise compression**: Storing earlier layers at higher precision, compressing later layers

### NVIDIA cuDNN & GPU Memory Optimization

NVIDIA's cuDNN library provides GPU-optimized primitives for deep learning operations, including attention:

- **cuDNN Flash Attention**: NVIDIA's own optimized Flash Attention implementation, integrated into PyTorch's `sdpa` (scaled dot-product attention) backend
- **cuDNN KV cache primitives**: Dedicated kernels for KV cache read/write with memory coalescing, reducing HBM bandwidth pressure
- **Multi-Instance GPU (MIG)**: NVIDIA's MIG technology partitions H100/B200 GPUs into isolated instances, each with dedicated KV cache memory
- **TensorRT-LLM**: NVIDIA's inference optimization library includes advanced KV cache management with FP8/FP4 support, continuous batching, and Paged Attention

**GPU memory optimization strategies**:
- **HBM utilization**: Modern GPUs (H100: 80GB HBM3, B200: 192GB HBM3e) are primarily limited by KV cache size rather than compute
- **KV cache offloading**: Moving less-frequently-accessed KV entries to CPU memory or NVMe storage with fast retrieval
- **Chunked prefill**: Breaking long prompts into chunks to bound peak KV cache memory during prefill phase
- **Memory pooling**: Pre-allocating KV cache memory pools to avoid dynamic allocation overhead during inference

### Context Caching

Context caching (also called prompt caching) persists KV cache entries across API calls when the prompt prefix matches a previous request. Providers charge significantly less for cache hits:

- **DeepSeek**: 98%+ discount on cache hits ($0.0028/M vs $0.14/M for V4-Flash)
- **OpenAI**: 50% discount on cached tokens via prompt caching API
- **Anthropic**: Significant discount on cached prefix tokens
- **Together AI**: Automatic context caching with substantial cost savings

## Provider Implementations

### DeepSeek

DeepSeek V4's MoE architecture (1.6T parameters, 49B active) requires sophisticated KV cache management. Key features:

- **Automatic context caching**: Identifies repeated prefixes across requests and reuses KV state
- **Aggressive pricing**: Cache hits cost ~$0.0028/M tokens — among the cheapest in the industry
- **Multi-head latent attention (MLA)**: Compresses KV cache through latent variable projection, reducing per-token memory footprint compared to standard multi-head attention

### Google Gemini

Google's Gemini models benefit from TPU-optimized KV cache management:

- **TPU memory hierarchy**: TPUs' large on-chip memory enables efficient KV cache storage
- **Paged Attention variants**: Google has implemented its own paged memory management for Gemma serving
- **Extended context**: Gemini models support up to 1M+ token contexts, requiring careful KV cache eviction policies

### OpenAI

OpenAI introduced prompt caching in its API (October 2024):

- **Automatic caching**: Reuses KV cache for matching prompt prefixes across requests
- **50% discount**: Cached input tokens cost half the regular input price
- **Transparency**: API responses indicate cache hit/miss status
- **Best practices**: Structuring prompts with stable prefixes (system instructions, few-shot examples) maximizes cache hits

### Together AI

Together AI serves open-weight models with vLLM-backed Paged Attention and has become a leader in KV cache optimization for open models:

- **High-throughput serving**: Paged Attention enables continuous batching across multiple models simultaneously
- **Open-weight focus**: Llama, Mistral, Qwen, and other open models benefit from vLLM's optimizations on Together's infrastructure
- **Inference optimization toolkit**: Provides speculative decoding and KV cache management options for API consumers
- **Custom vLLM forks**: Together maintains vLLM optimizations for their specific hardware configuration (NVIDIA H100 clusters)
- **KV cache sharing**: Shared prefix detection across users for common system prompts and tool definitions
- **Performance claims**: Up to 4× throughput improvement over naive KV cache management on comparable hardware

### Alibaba Qwen

Qwen's Model Studio and inference infrastructure include KV cache optimizations:

- **MLA (Multi-head Latent Attention)**: Qwen's attention architecture compresses KV cache through latent variable projection
- **Context caching**: Automatic KV cache reuse for repeated prefixes in Model Studio API calls
- **Multi-model support**: Optimizations work across Qwen 3.7 series and third-party models hosted on Model Studio

### Anthropic

Anthropic's Claude models implement prompt caching with automatic prefix detection:

- **Prompt caching API**: Enables explicit control over cacheable prefix segments
- **Cost savings**: Significant discount for cached tokens
- **Developer ergonomics**: Cache-aware prompt design patterns for repeated system prompts

### Meta Llama

Llama models are served through multiple frameworks with different KV cache strategies:

- **vLLM**: Paged Attention for high-throughput serving
- **llama.cpp**: Optimized KV cache for CPU and edge deployment
- **TensorRT-LLM**: Nvidia GPU-optimized cache management with FP8 support
- **Groq**: Sub-100ms TTFT through proprietary KV cache optimization on LPU architecture

## Performance Impact

| Technique | Memory Reduction | Throughput Gain | Latency Impact |
|-----------|-----------------|-----------------|----------------|
| Paged Attention | 30–50% (less fragmentation) | 2–4× | Neutral to improved |
| Flash Attention | 50–75% (I/O reduction) | 2–3× (training) | Minimal (inference) |
| KV Compression (INT8) | 50% | 1.5–2× | Slight quality trade-off |
| Context Caching | Variable (depends on reuse) | Variable | Dramatically reduced for cache hits |

## Configuration Guidelines

- **Batch size**: Paged Attention enables larger effective batch sizes; monitor GPU memory utilization
- **Cache eviction**: For long contexts (>100K tokens), implement sliding window or attention-based eviction
- **Quantization**: INT8 KV cache is safe for most tasks; INT4 may degrade quality on reasoning-heavy prompts
- **Prompt design**: Structure prompts to maximize cache reuse — stable system prompt first, variable content last

## Related Concepts

- [[prompt-caching]] — context caching is a specific KV cache optimization for repeated prefixes
- [[speculative-decoding]] — speculative decoding generates tokens faster, putting more pressure on KV cache
- [[open-weight-licensing]] — open-weight models enable self-hosted KV cache optimization with full control
