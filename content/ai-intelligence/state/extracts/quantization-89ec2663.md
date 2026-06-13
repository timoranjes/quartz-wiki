title: Quantization
tags: optimization, inference, training
# Quantization

## Overview

Quantization reduces the numerical precision of model weights and activations from FP32 (32-bit floating point) to lower bit depths (FP8, INT8, INT4, or even lower). This dramatically reduces memory requirements and can improve inference speed with minimal quality loss.

## Quantization Formats

| Format | Bits | Use Case | Quality Impact | Hardware Support |
|--------|------|----------|---------------|-----------------|
| FP32 | 32 | Training reference | None | All GPUs |
| FP16/BF16 | 16 | Standard inference/training | Minimal | All modern GPUs |
| FP8 | 8 | Training + inference | <1% perplexity increase | Hopper (H100), Blackwell (B200) |
| INT8 | 8 | Inference-only | 1-2% degradation | All GPUs |
| INT4/GPTQ | 4 | Local deployment, mobile | 2-5% degradation | Consumer GPUs, edge |
| GGUF (Q4/Q5/Q8) | 4-8 | Local (llama.cpp, Ollama) | Varies by level | CPU + GPU |
| AWQ | 4 | GPU inference | <2% with smart scaling | NVIDIA GPUs |
| NF4 | 4 | QLoRA fine-tuning | Minimal with proper calibration | Consumer GPUs |

## Provider Adoption (2026)

- **DeepSeek V4**: FP4 Quantization-Aware Training (QAT) on MoE expert weights and QK path — reduces memory with no post-training quality loss
- **NVIDIA**: FP8 training and inference on Hopper/Blackwell; NVFP4 QAT recipes for deployment; TensorRT-LLM optimized kernels
- **Meta Llama 4**: Supports GGUF conversion for local deployment; INT8 and INT4 variants via llama.cpp
- **Microsoft Phi**: Designed for INT4 quantization on edge devices; Phi-4 runs on consumer hardware
- **Moonshot Kimi K2**: Quantization-aware training for efficient serving at scale
- **Together AI**: Offers quantized model variants (INT8, INT4) across their hosting platform
- **Zhipu AI**: Quantized GLM models for enterprise on-premise deployment

## Quantization-Aware Training (QAT)

Rather than quantizing after training (post-training quantization, PTQ), QAT simulates quantization during training:
- Model learns to compensate for precision loss during optimization
- DeepSeek V4 uses FP4 QAT on MoE expert weights
- NVIDIA provides QAT tooling in TensorRT-LLM
- Results in near-lossless quantization vs PTQ

## Key Libraries and Tools

| Tool | Purpose | Supported Formats |
|------|---------|------------------|
| llama.cpp | Local inference | GGUF (Q2-Q8) |
| GPTQ/ExLlamaV2 | GPU-optimized quantized inference | GPTQ (INT4) |
| AWQ | Activation-aware quantization | INT4 with smart scaling |
| BitsAndBytes | QLoRA fine-tuning | NF4, INT8 |
| TensorRT-LLM | NVIDIA optimized serving | FP8, FP4, INT8 |
| HuggingFace Optimum | Multi-format conversion | All major formats |

## Trade-offs

- **Speed**: INT4 can achieve 2-4× speedup over FP16 on compatible hardware
- **Memory**: INT4 reduces a 70B model from ~140GB (FP16) to ~35GB
- **Quality**: QAT models show <1% perplexity degradation; PTQ can lose 5-10%
- **Fine-tuning**: QLoRA enables fine-tuning of 70B+ models on 24GB GPUs

## Related

- [[kv-cache-optimization]] — Quantized KV cache further reduces memory pressure
- [[moE-architecture]] — MoE expert weights are primary quantization targets
- [[speculative-decoding]] — Draft models often quantized to minimize overhead