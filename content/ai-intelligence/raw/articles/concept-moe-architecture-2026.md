---
title: Mixture of Experts Architecture
researched: 2026-06-05
sources:
  - https://huggingface.co/blog/moe
  - https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/
  - https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts
---

# Mixture of Experts Architecture

## Overview

Mixture of Experts (MoE) is an architectural pattern for neural networks that splits computation across multiple specialized sub-networks called "experts." Instead of using all parameters for every input (as in dense models), MoE models use a gating network or router to dynamically select which experts process each token. This enables models to scale to hundreds of billions or even trillions of parameters while keeping per-token compute roughly constant.

The concept dates back to 1991 with "Adaptive Mixture of Local Experts" by Jacobs et al., but has seen a renaissance in LLM development. Models like Mixtral 8x7B, Google's Switch Transformers (1.6T parameters), and GShard (600B+ parameters) have demonstrated that MoE architectures can achieve superior performance with faster inference and pretraining compared to dense models of equivalent parameter count.

## Key Details

### Architecture Components
- **Experts**: Multiple feed-forward networks (FFNs), typically 4-8 or more per MoE layer. Each expert is a specialized sub-network
- **Gate Network / Router**: A learned network that decides which tokens go to which expert(s). The router outputs gating weights for each expert
- **Sparse Activation**: Only a subset of experts (top-k, typically k=1 or k=2) is activated per token

### MoE Layer Formula
```
y = Σ G(x)_i · E_i(x)
```
Where G(x) is the gating weights (softmax over router logits) and E_i(x) is the output of expert i.

### Sparsity and Top-k Gating
- **Dense models**: All parameters used for all inputs
- **Sparse models (MoEs)**: Only subset of experts activated per token
- **Top-k routing**: Keep top-k experts by router logits, apply softmax, compute weighted sum
- Switch Transformers use top-1 routing (simpler, faster, less communication overhead)

### Key Historical Milestones
- **1991**: Adaptive Mixture of Local Experts (foundational paper)
- **2017**: Sparsely-Gated MoE in LSTM (137B params), introduced Top-k gating
- **2020**: GShard — MoE in Transformers (600B+ params), top-2 routing
- **2022**: Switch Transformers — 1.6T params, top-1 routing, 4x faster pretraining
- **2023**: Mixtral 8x7B — high-quality open MoE outperforming Llama 2 70B

### Benefits
- **Faster Pretraining**: Same compute budget trains faster than dense models
- **Faster Inference**: Same parameter count but fewer active parameters per token
- **Scalability**: Scale model size without proportional compute increase
- **Parameter Efficiency**: Mixtral 8x7B has 47B total params but only ~12B FLOPs/token (top-2)

### Challenges
- **High VRAM Usage**: All experts must be loaded in memory (Mixtral 8x7B ≈ 47B dense params)
- **Load Balancing**: Router may converge to favor few experts; requires auxiliary loss to encourage uniform usage
- **Training Stability**: Router z-loss (from ST-MoE) penalizes large router logits to reduce numerical instability
- **Fine-tuning**: More challenging than dense models, though recent instruction-tuning work shows promise

### Expert Capacity
- Concept introduced in Switch Transformers: buffer for imbalanced routing
- Expert Capacity = (tokens per batch / number of experts) × capacity factor
- Recommended capacity factor: 1.0-1.25
- Tokens exceeding expert capacity are dropped

## Sources
- https://huggingface.co/blog/moe
- https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/
- https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts
