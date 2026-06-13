title: KV Cache Optimization
tags: optimization, inference
# KV Cache Optimization

## Overview

The KV (Key-Value) cache stores intermediate attention states during autoregressive generation, avoiding recomputation of previous tokens. At long context lengths, the KV cache becomes the primary memory bottleneck — often larger than model weights.

## Key Techniques

### Paged Attention (vLLM)
- Manages KV cache like OS page tables — non-contiguous memory blocks
- Eliminates memory fragmentation in multi-request batching
- 2-4× throughput improvement over naive contiguous allocation
- Standard across most open-weight serving platforms

### Flash Attention 4
- Block-sparse attention patterns for Blackwell architecture
- 3× speedup over Flash Attention 2 on H100/B200
- FP4 support for reduced memory bandwidth
- Kernel fusion eliminates redundant memory reads

### KV Cache Compression
- Quantized KV cache: INT8 or FP8 representation of K/V states
- Lossy compression with <1% quality degradation at 50% memory reduction
- Combined with Paged Attention for maximum throughput

### Multi-Query Attention (MQA) / Grouped-Query Attention (GQA)
- Shares KV heads across multiple query heads
- Reduces KV cache size by 4-8× compared to multi-head attention
- Llama 4, Mistral, and most 2026 models use GQA by default

### DeepSeek Hybrid Attention (CSA+HCA)
- CSA: 4× compression with top-1024 selection + sliding window
- HCA: 128× compression with dense attention over compressed tokens
- Achieves 27% of V3.2 FLOPs at 1M context, 10% of KV cache size

## Provider Implementations

| Provider | Technique | Impact |
|----------|-----------|--------|
| Together AI | Custom vLLM fork + KV cache sharing | 4× throughput claims |
| NVIDIA | cuDNN Flash Attention + TensorRT-LLM | 3× FA2 speedup |
| DeepSeek | CSA+HCA hybrid attention | 90% KV cache reduction at 1M |
| Meta Llama 4 | iRoPE + GQA + chunked prefill | Efficient 10M context |
| Moonshot | Mooncake serving platform | Optimized KV cache distribution |
| Mistral | vLLM integration with PagedAttention | Standard serving |

## Memory Impact

For a 70B model at 128K context:
- **Naive KV cache**: ~64GB (FP16)
- **With GQA**: ~16GB (4× reduction)
- **With PagedAttention + INT8**: ~8GB (8× total reduction)
- **With DeepSeek CSA+HCA**: ~3GB (20× total reduction)

## Related

- [[context-windows]] — KV cache is the limiting factor for long context
- [[prompt-caching]] — Caching reuses KV cache across requests
- [[quantization]] — Quantized KV cache further reduces memory