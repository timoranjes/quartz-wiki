---
domain: llm-providers
type: concept
tags: [concept/optimization, concept/quantization, concept/inference]
aliases: [Quantization, Q4, Q8, GGUF, GPTQ, AWQ]
created: 2026-06-01
---
# Quantization

## Overview
Quantization reduces model precision from FP16/BF16 to lower-bit representations (INT8, INT4, etc.), dramatically reducing memory requirements with minimal quality loss. Essential for running large models on consumer hardware.

## Quantization Formats

### GGUF (GGML Unified Format)
- **Used by**: llama.cpp, Ollama, LM Studio
- **Types**: Q2_K, Q3_K_M, Q4_0, Q4_K_M, Q5_K_M, Q6_K, Q8_0
- **Trade-off**: Q4_K_M ≈ 95% quality at 50% size; Q8_0 ≈ 99% at 75% size
- **Hardware**: CPU + GPU, runs on Apple Silicon efficiently

### GPTQ
- **Used by**: AutoGPTQ, vLLM, ExLlama
- **Per-channel quantization** — better quality than GGUF at same bit depth
- **GPU-optimized** — requires CUDA
- **Types**: 3-bit, 4-bit, 8-bit

### AWQ (Activation-Aware Weight Quantization)
- **Used by**: vLLM, SGLang
- Preserves salient weights at higher precision
- Better quality than GPTQ at 4-bit for some models
- **Hardware**: CUDA only

### FP8
- **Used by**: NVIDIA H100, cloud inference
- New standard for cloud providers
- Near-FP16 quality with 50% memory reduction

## Impact on Model Quality

| Quantization | Size Reduction | Quality Retention | Use Case |
|-------------|---------------|------------------|----------|
| FP16/BF16 | 1× (baseline) | 100% | Training, maximum quality |
| Q8_0 | ~50% | 99% | Near-lossless inference |
| Q6_K | ~40% | 98% | High-quality local inference |
| Q5_K_M | ~33% | 97% | Balanced local inference |
| Q4_K_M | ~25% | 95% | Most popular local format |
| Q3_K_M | ~20% | 90% | Resource-constrained |
| Q2_K | ~15% | 80% | Extreme compression |

## Hardware Requirements Examples (70B model)

| Format | VRAM/RAM | Hardware |
|--------|----------|----------|
| FP16 | 140 GB | 2× A100 80GB |
| Q8_0 | 70 GB | 1× A100 80GB |
| Q4_K_M | 35 GB | 1× RTX 4090 48GB / Mac Studio 64GB |
| Q3_K_M | 26 GB | 1× RTX 3090 24GB + offload |

## Provider Support

| Provider | Self-Host Quantization | Cloud Quantization |
|----------|----------------------|-------------------|
| Meta Llama 4 | GGUF community releases | — |
| Alibaba Qwen | Official GPTQ + AWQ + GGUF | FP8 on DashScope |
| Mistral | Official GPTQ + AWQ | — |
| DeepSeek | Official GGUF (V3/R1) | Internal FP8 |

## Related
- [[moE-architecture]] — MoE models are harder to quantize (experts need separate quantization)
- [[open-weight-licensing]] — Quantization requires open-weight access
