---
title: Quantization
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - optimization
  - inference
  - deployment
sources:
  - "NVIDIA FP8 Inference Technical Blog"
  - "AWQ: Activation-Aware Weight Quantization Paper"
  - "GGUF Format Documentation (llama.cpp)"
  - "GPTQ: Accurate Post-Training Quantization Paper"
  - "Give Me BF16 or Give Me Death: Accuracy-Performance Trade-Offs"
  - "InfoQuant: Shaping Activation Distributions for Low-Bit LLM Quantization"
  - "NVFP4 QAT Recipes: How Architecture and Scale Shape Model Quality"
  - "HARP: Hadamard Preconditioned Adaptive Rotation Processor"
confidence: high
---

# Quantization

Quantization reduces the numerical precision of model weights and/or activations from the standard FP32/BF16 to lower-precision formats (FP8, INT8, INT4, or even lower), dramatically reducing memory requirements and increasing inference speed with minimal quality loss. It is essential for deploying large models on consumer hardware and for cost-efficient production serving.

---

## Definition

Quantization maps high-precision floating-point values to a smaller set of representable values. The key challenge is minimizing the accuracy degradation caused by this lossy compression. Two main approaches:

- **Post-training quantization (PTQ)**: Quantize a pre-trained model without additional training. Fast and simple, but may lose more accuracy.
- **Quantization-aware training (QAT)**: Simulate quantization during training so the model learns to be robust to low precision. Better accuracy but requires retraining.

### Quantization Levels

| Precision | Bits | Memory vs BF16 | Use Case |
|-----------|------|----------------|----------|
| **BF16/FP16** | 16 | 1× (baseline) | Training, high-quality inference |
| **FP8** | 8 | 2× reduction | Training and inference on Hopper+ GPUs |
| **INT8** | 8 | 2× reduction | Production inference, edge deployment |
| **INT4** | 4 | 4× reduction | Consumer GPU/CPU deployment |
| **FP4/NVFP4** | 4 | 4× reduction | Next-gen inference on Blackwell GPUs |
| **1.58-bit** | ~1.58 | ~10× reduction | Extreme compression, research |

## FP8 Training and Inference

FP8 has emerged as the sweet spot for both training and inference on modern GPUs:

- **NVIDIA Hopper (H100, H200)**: First architecture with native FP8 tensor core support. FP8 training achieves near-BF16 accuracy with 2× throughput and 2× memory reduction.
- **FP8 formats**: E4M3 (4-bit exponent, 3-bit mantissa) for forward pass; E5M2 for backward pass gradients.
- **NVIDIA Blackwell (B200)**: Enhanced FP8 support with higher throughput and improved numerical stability.
- **FP8 inference**: H100 and B200 support FP8 inference natively. Models quantized to FP8 typically lose <1% accuracy on most benchmarks.
- **Training with FP8**: DeepSeek V4, Qwen, and other frontier models use FP8 for parts of training, reducing memory and enabling larger models.
- **HiF8 W8A8** (2025): Near-lossless FP8 quantization-aware training recipe that preserves model quality at W8A8 (weight 8-bit, activation 8-bit) precision.

### NVIDIA FP8 Inference Stack

- **TensorRT-LLM**: Supports FP8 quantization with automatic calibration, achieving 1.5–2× throughput over FP16.
- **FP8 calibration**: Uses a small calibration dataset to determine optimal scaling factors for each layer.
- **Mixed precision**: Some layers (typically the first and last) remain at higher precision to minimize accuracy loss.

## AWQ: Activation-Aware Weight Quantization

AWQ is one of the most effective PTQ methods for INT4 quantization:

- **Core insight**: Only ~1% of weights are "salient" — they have large activation values and contribute disproportionately to output. These weights should be kept at higher precision.
- **Method**: Analyze activation statistics on a calibration dataset, identify salient weights, and apply per-channel scaling to protect them during quantization.
- **W4A16**: 4-bit weights with 16-bit activations. Achieves near-lossless quality for most models.
- **AutoAWQ**: Open-source implementation that works with HuggingFace models. Supports Marlin kernel for fast inference.
- **Performance**: AWQ-quantized models achieve ~95–99% of BF16 quality on most benchmarks, with 4× memory reduction and 1.5–3× speedup on compatible hardware.
- **Provider support**: Together AI, Groq, and other inference providers use AWQ-quantized models for cost-efficient serving.

## GGUF: Local Deployment Format

GGUF (GGML Universal Format) is the standard format for running LLMs on consumer hardware:

- **llama.cpp**: The primary engine for GGUF models. Supports CPU, GPU (via Vulkan, CUDA, Metal), and hybrid inference.
- **Quantization types**: GGUF supports many quantization levels:
  - **Q4_0 / Q4_K_M**: 4-bit quantization, good quality/speed trade-off
  - **Q5_0 / Q5_K_M**: 5-bit, higher quality
  - **Q6_K**: 6-bit, near-lossless
  - **Q8_0**: 8-bit, minimal quality loss
- **Hardware support**: Runs on Mac (M-series Neural Engine), Linux (CPU + GPU), Windows (CPU + GPU), and even mobile devices.
- **Community ecosystem**: Thousands of GGUF-quantized models available on HuggingFace, enabling anyone to run frontier models on consumer hardware.
- **Speculative decoding**: llama.cpp supports speculative decoding with GGUF models, using smaller quantized models as draft models.

### Performance Benchmarks

| Quantization | Model Size | Memory | Quality Loss | Speed (tok/s on M2 Max) |
|-------------|-----------|--------|-------------|------------------------|
| **BF16** | 70B | 140 GB | 0% | ~8 |
| **Q8_0** | 70B | 70 GB | <1% | ~15 |
| **Q6_K** | 70B | 52 GB | <2% | ~20 |
| **Q5_K_M** | 70B | 44 GB | ~3% | ~25 |
| **Q4_K_M** | 70B | 38 GB | ~5% | ~30 |
| **Q4_0** | 70B | 35 GB | ~8% | ~35 |

## GPTQ: GPU-Optimized Quantization

GPTQ is a PTQ method optimized for GPU inference:

- **Method**: Uses a small calibration dataset to compute optimal quantization parameters per layer, minimizing reconstruction error.
- **GPTQ-For-LLaMa**: Popular implementation that supports GPTQ quantization for Llama-family models.
- **ExLlamaV2**: Fastest GPTQ inference engine, optimized for NVIDIA GPUs. Achieves 2–3× speedup over standard GPTQ.
- **Marlin kernel**: Optimized GPTQ kernel for AWQ-quantized models, achieving high throughput on H100/A100.
- **W4A16 GPTQ**: Standard configuration — 4-bit weights, 16-bit activations. Near-lossless for most models.

### GPTQ vs AWQ

| Aspect | GPTQ | AWQ |
|--------|------|-----|
| **Approach** | Layer-wise optimization | Activation-aware scaling |
| **Calibration** | Requires calibration data | Requires calibration data |
| **Quality** | Good | Slightly better (protects salient weights) |
| **Speed** | Fast with ExLlamaV2/Marlin | Fast with Marlin |
| **Hardware** | GPU-focused | GPU-focused |
| **Best for** | GPU serving | GPU serving with maximum quality |

## Advanced Quantization Research

### Rotation-Based Methods

- **HARP** (2025): Hadamard preconditioned adaptive rotation processor for extreme LLM quantization. Rotates weight matrices to make them more amenable to quantization, enabling INT3/INT2 with acceptable quality loss.
- **SpinQuant**: Uses subspace residual rotation to improve low-bit quantization quality.

### Activation Distribution Shaping

- **InfoQuant** (2025): Shapes activation distributions to be more quantization-friendly, reducing outliers that cause quantization error.

### Quantization-Aware Training Advances

- **NVFP4 QAT** (2025): NVIDIA's FP4 quantization-aware training recipe. Shows that architecture and model scale significantly affect QAT quality — larger models tolerate lower-bit quantization better.
- **SVDQuant-GPTQ** (2025): Combines SVD-based compression with GPTQ for W4A4 quantization of video generation models.

## Trade-offs

| Aspect | Details |
|--------|---------|
| **Quality loss** | INT8: <1%; INT4: 2–8%; INT3/2: 10–30% (varies by model and task) |
| **Memory reduction** | INT4: 4×; INT8: 2×; FP8: 2× |
| **Speedup** | INT4: 1.5–3×; INT8: 1.5–2×; FP8: 1.5–2× (hardware-dependent) |
| **Hardware requirements** | FP8: Hopper+ GPUs; INT4: Any GPU with tensor cores; GGUF: CPU or GPU |
| **Best for** | Production serving, edge deployment, consumer hardware |
| **Worst for** | Training (except FP8), tasks requiring maximum precision |

## Open Questions

- **Extreme quantization**: Can we reliably quantize to INT2 or lower without unacceptable quality loss?
- **Dynamic quantization**: Can models dynamically adjust precision per layer or per token based on input complexity?
- **Quantization + MoE**: How does quantization interact with MoE architectures? Can we quantize individual experts differently?
- **Quantization safety**: Does quantization affect model safety/alignment? Some research suggests quantized models may be less aligned.
- **FP4 adoption**: Will FP4 become the new standard for production inference on Blackwell GPUs?

## Related Concepts

- [[kv-cache-optimization]] — KV cache can also be quantized for additional memory savings
- [[speculative-decoding]] — draft models are often quantized to reduce overhead
- [[distillation]] — distilled models are smaller and thus less in need of quantization
- [[moe-architecture]] — MoE models present unique quantization challenges due to expert routing
