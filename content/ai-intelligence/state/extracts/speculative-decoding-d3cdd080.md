title: Speculative Decoding
tags: optimization, inference, latency
# Speculative Decoding

## Overview

Speculative decoding accelerates autoregressive generation by having a smaller, faster "draft" model predict multiple tokens ahead, which the larger target model verifies in a single forward pass. This achieves **2-4× throughput improvement** without quality degradation.

## Core Mechanism

1. **Drafting**: Lightweight model generates k candidate tokens in parallel
2. **Verification**: Target model runs one forward pass over all k tokens
3. **Acceptance**: Tokens matching target distribution are accepted; rejected ones resampled
4. **Speedup**: Achieved when acceptance rate offsets draft/verify overhead

## Key Approaches

### Medusa
- Attaches multiple independent decoding heads to the target model
- Each head predicts tokens at different future positions (t+1, t+2, ..., t+k)
- No separate draft model needed — heads share hidden states
- Best for code and structured text (60-80% acceptance)

### EAGLE / EAGLE-3
- Trains auxiliary draft model on target's hidden states
- EAGLE-3 achieves 75-90% acceptance across general benchmarks
- Default speculative backend in vLLM and HuggingFace TGI

### MoE + Speculation Synergy
- DeepSeek V4's sparse MoE creates natural synergy: draft model mirrors sparse routing, reducing draft latency
- Mistral's Mixtral: draft model predicts expert activations alongside tokens
- Acceptance rates improve when draft and target share MoE routing patterns

## Provider Support (2026)

| Provider | Implementation | Speedup | Notes |
|----------|---------------|---------|-------|
| NVIDIA | TensorRT-LLM batched speculation | 3-4× | Hopper/Blackwell kernel fusion |
| Together AI | EAGLE-3 default across platform | 2-3× | ThunderAgent framework |
| Mistral | Native speculative decoding in inference stack | 2.5× | Mixtral expert-aware drafting |
| DeepSeek | Sparse drafting for MoE models | 3.2× | Math/logic tasks best |
| Meta | vLLM integration for Llama 4 | 2.8× | EAGLE-3 backend |

## Trade-offs

- **Best for**: Repetitive, deterministic, or code-heavy generation
- **Worst for**: Creative writing, high temperature (>0.9), short responses (<20 tokens)
- **Memory overhead**: Draft model adds 10-30% VRAM; Medusa heads add <5%
- **TTFT**: Time-to-first-token remains similar or slightly increases

## Related

- [[kv-cache-optimization]] — Draft and target share KV cache efficiently
- [[prompt-caching]] — Both reduce generation cost; complementary in production
- [[distillation]] — Draft models distilled from target for distribution alignment
- [[quantization]] — Draft models often quantized to INT4/FP8