title: Mixture of Experts (MoE) Architecture
tags: architecture, training, inference
# Mixture of Experts (MoE) Architecture

## Overview

MoE is a neural network architecture where each token is processed by only a subset of the model's parameters ("experts") rather than activating the entire network. A gating network routes each token to the most relevant experts, enabling **massive total parameter counts** with **manageable inference costs**. This has become the dominant architecture for frontier models since 2024.

## How It Works

- Model contains many "expert" feed-forward networks (FFNs)
- A gating/router network selects which experts to activate per token
- Only active experts consume compute; inactive ones are skipped
- Total parameters can scale independently of active compute budget
- Result: frontier capability at a fraction of dense model cost

## Provider Implementations (Mid-2026)

| Provider | Model | Total Params | Active per Token | Expert Count | Key Innovation |
|----------|-------|-------------|-----------------|-------------|----------------|
| DeepSeek | V4 Pro | 1.6T | 49B | — | CSA+HCA hybrid attention |
| DeepSeek | V4 Flash | 284B | 13B | — | Ultra-sparse routing |
| Meta | Llama 4 Maverick | ~400B | 17B | 128 + 1 shared | iRoPE interleaved encoding |
| Meta | Llama 4 Scout | 109B | 17B | 16 | Codistillation from Behemoth |
| Mistral | Small 4 | 119B | 6.5B | 128 experts, 4 active | Granular MoE |
| Mistral | Large 3 | 675B | 41B | — | Mixtral load balancing |
| Alibaba | Qwen3.7 Max | ~1T | Undisclosed | Sparse | High sparsity ratio |
| Alibaba | Qwen3.6-35B-A3B | 35B | 3B | — | 3B active sub-model |
| Moonshot | Kimi K2 | 1T | 32B | — | Muon optimizer at MoE scale |
| StepFun | Step-3.5-Flash | — | — | — | "Small Sparse" architecture |
| StepFun | Step-3.7-Flash | — | — | — | MoE vision-language |
| Zhipu AI | GLM-5 | 744B | — | MoE | Enterprise MoE flagship |
| xAI | Grok 4.3 | — | — | — | Sparse activation patterns |
| MiniMax | MiniMax-M2 | ~10B activated | ~10B | MoE | Multi-modal MoE |
| Cohere | Command A+ | — | — | First MoE | Cohere's first MoE model |
| Microsoft | Phi-3.5-MoE | 41B | 16B (6.6B active) | 16 experts | Small-scale MoE research |

## Architecture Variants

- **Granular MoE** (Mistral): Fine-grained expert selection with speculative decoding integration; Small 4 uses 128 experts with only 4 active per token
- **iRoPE MoE** (Meta Llama 4): Interleaved Rotary Position Encoding — every 4th layer uses NoPE with full attention; others use RoPE with 8K chunked attention
- **Sparse MoE** (Alibaba Qwen): High sparsity ratio with many experts and few active per token
- **Codistillation** (Meta): Unreleased teacher model (Behemoth ~2T) distilled into smaller MoE models during pre-training
- **Muon-optimized MoE** (Moonshot/DeepSeek): Muon optimizer for stable training at trillion-parameter MoE scale

## Advantages

- **Cost efficiency**: 1.6T total params at ~49B active cost (DeepSeek V4 Pro); Kimi K2 at 1T/32B active
- **Scaling**: Total parameters can grow without proportional inference cost increase
- **Specialization**: Different experts learn different domains, improving performance across diverse tasks
- **Memory efficiency**: Sparse activation reduces per-token compute by 30-100× vs dense

## Disadvantages

- **Training complexity**: Routing stability and expert load balancing are harder than dense training
- **Memory footprint**: All parameters must be loaded into VRAM even if not all active
- **KV cache**: Still scales with total model size in some implementations
- **Expert collapse**: Poor routing can lead to some experts being under-utilized

## Open Debates

- **Optimal sparsity**: How many experts should be active per token? DeepSeek uses ~3%, Mistral Small uses ~3% (4/128), but the sweet spot is still researched
- **Routing strategies**: Top-K vs soft routing vs learned routing — which generalizes best?
- **MoE + quantization**: Can MoE models be quantized to FP4/INT4 without routing degradation? DeepSeek V4 uses FP4 QAT on expert weights

## Related

- [[quantization]] — FP4 QAT on MoE expert weights (DeepSeek V4)
- [[speculative-decoding]] — Draft models benefit from MoE sparse activation patterns
- [[distillation]] — Meta codistills Behemoth → Llama 4 MoE models
- [[kv-cache-optimization]] — MoE models have different KV cache requirements than dense models