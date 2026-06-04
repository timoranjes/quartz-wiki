---
title: Quantization - GGUF, GPTQ, AWQ
researched: 2026-06-05
sources:
  - https://newsletter.maartengrootendorst.com/p/which-quantization-method-is-right
  - https://www.linkedin.com/pulse/demystifying-llm-quantization-gptq-awq-gguf-explained-xiao-fei-zhang-1lmbe
  - https://joydeep31415.medium.com/llm-quantization-techniques-4229b7eac20c
---

# Quantization - GGUF, GPTQ, AWQ

## Overview

Quantization is the process of reducing the numerical precision of a model's weights (and sometimes activations) from high-precision formats like float32 or float16 to lower-precision formats like int8, int4, or even lower. This dramatically reduces model size and memory requirements, enabling large language models to run on consumer hardware. For example, a 7B parameter model in float16 requires ~14GB of VRAM, but in 4-bit quantization it requires only ~3.5GB.

Three major pre-quantized formats dominate the ecosystem: **GPTQ** (optimized for GPU inference), **GGUF** (optimized for CPU inference with optional GPU offloading, based on llama.cpp), and **AWQ** (Activation-aware Weight Quantization that identifies and preserves salient weights). Each has distinct trade-offs in terms of speed, quality retention, and hardware compatibility.

## Key Details

### Why Quantization Matters
- **Memory Reduction**: 4-bit quantization reduces model size to ~25% of original
- **Speed Improvement**: Smaller models load faster and generate tokens more quickly
- **Accessibility**: Enables running large models on consumer GPUs, laptops, and edge devices
- **Cost Efficiency**: Reduces inference costs in production deployments

### Quantization Methods

#### GGUF (GPT-Generated Unified Format)
- **Hardware**: Optimized for CPU inference, with optional GPU layer offloading
- **Ecosystem**: Based on llama.cpp; great for Apple Silicon or low-end GPUs
- **Loading**: Uses ctransformers or llama.cpp libraries
- **Best For**: CPU-only systems, Apple Silicon, low-end GPUs, edge deployment
- **Quantization Types**: Q4_K_M, Q5_K_M, Q8_0, etc. (varying precision levels)

#### GPTQ (GPT Quantization)
- **Hardware**: Optimized for GPU inference
- **Method**: Minimizes mean squared error during quantization; dequantizes weights to float16 during inference
- **Ecosystem**: Widely adopted, stable, fast; uses auto-gptq library
- **Best For**: GPU users who want decent performance without much quality loss
- **Loading**: Compatible with HuggingFace Transformers via optimum library

#### AWQ (Activation-aware Weight Quantization)
- **Hardware**: GPU-optimized (similar to GPTQ)
- **Method**: Analyzes which weights are "salient" (most important for preserving activation fidelity); salient weights remain at higher precision while others are quantized
- **Key Difference from GPTQ**: Assumes not all weights are equally important; protects critical weights
- **Ecosystem**: Growing adoption; available via autoawq library
- **Best For**: Users who want better quality retention at aggressive quantization levels

#### Bitsandbytes (4-bit NF4)
- **Method**: Converts weights from float32 to 4-bit NormalFloat (NF4) via normalization → quantization → dequantization during inference
- **Configuration**: `load_in_4bit=True`, `bnb_4bit_quant_type='nf4'`, double quantization enabled
- **Best For**: Quick prototyping; on-the-fly quantization at load time
- **Limitation**: Requires re-quantization each time the model is loaded (not pre-quantized)

### Quantization Levels
- **8-bit**: Minimal quality loss; ~50% size reduction
- **4-bit**: Good quality retention; ~75% size reduction
- **2-bit/1-bit**: Significant quality degradation; experimental

### Choosing a Method
| Scenario | Recommended Method |
|----------|-------------------|
| CPU-only or Apple Silicon | GGUF |
| GPU with good performance needs | GPTQ |
| GPU with quality at aggressive compression | AWQ |
| Quick prototyping | Bitsandbytes |
| Edge/IoT deployment | GGUF (low-bit variants) |

### Trade-offs
- **Quality Loss**: Lower precision = more approximation error; AWQ generally retains quality better at same bit width
- **Speed**: GGUF on CPU is slower than GPTQ/AWQ on GPU
- **Setup**: Pre-quantized models (GPTQ, GGUF, AWQ) save time vs. on-the-fly quantization
- **Compatibility**: Not all models support all formats; check community availability

## Sources
- https://newsletter.maartengrootendorst.com/p/which-quantization-method-is-right
- https://www.linkedin.com/pulse/demystifying-llm-quantization-gptq-awq-gguf-explained-xiao-fei-zhang-1lmbe
- https://joydeep31415.medium.com/llm-quantization-techniques-4229b7eac20c
