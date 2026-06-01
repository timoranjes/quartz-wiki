---
domain: llm-providers
type: concept
tags: [concept/architecture, concept/moe]
aliases: [Mixture of Experts, MoE]
created: 2026-06-01
---
# Mixture of Experts (MoE) Architecture

## Overview
MoE is a neural network architecture where only a subset of model parameters ("experts") are activated per token, rather than the entire model. This enables **massive total parameter counts** with **manageable inference costs**.

## How It Works
- Model contains many "expert" feed-forward networks (FFNs)
- A gating network selects which experts to activate per token
- Only active experts consume compute; inactive ones are skipped
- Result: frontier capability at fraction of dense model cost

## Key Providers Using MoE (2026)

| Provider | Model | Total Params | Active Params | Expert Count |
|----------|-------|-------------|---------------|-------------|
| DeepSeek | V4-Pro | 1.6T | 49B | — |
| DeepSeek | V4-Flash | 284B | 13B | — |
| Mistral | Large 3 | 675B | 41B | — |
| Mistral | Small 4 | 119B | 6.5B | 128 experts, 4 active |
| Alibaba | Qwen3.7 Max | ~1T | Undisclosed | Sparse MoE |
| Alibaba | Qwen3.6-35B-A3B | 35B | 3B | — |
| Meta | Llama 4 Scout | 109B | 17B | 16 experts |
| Meta | Llama 4 Maverick | 400B | 17B | 128 + 1 shared |
| OpenAI | GPT-5.5 | Undisclosed | Undisclosed | Rumored MoE |
| Anthropic | Opus 4.8 | Undisclosed | Undisclosed | Undisclosed |

## Architecture Variants
- **Granular MoE** (Mistral Large 3): Fine-grained expert selection with speculative decoding
- **iRoPE MoE** (Meta Llama 4): Interleaved Rotary Position Encoding — every 4th layer uses NoPE with full attention; others use RoPE with 8K chunked attention
- **Sparse MoE** (Qwen): High sparsity ratio, many experts with few active
- **Codistillation** (Meta): Unreleased teacher model (Behemoth ~2T) distilled into smaller MoE models during training

## Advantages
- **Cost efficiency**: 1.6T total params at ~49B active cost (DeepSeek V4-Pro)
- **Scaling**: Total parameters can grow without proportional inference cost increase
- **Specialization**: Different experts can specialize in different domains/tasks

## Disadvantages
- **Training complexity**: More difficult to train than dense models
- **Memory footprint**: All parameters must be loaded (even if not all active)
- **KV cache**: Still proportional to total model size in some implementations

## Related
- [[deepseek]] — MoE architecture mastery (V4-Pro: 1.6T/49B)
- [[mistral]] — Granular MoE with speculative decoding
- [[meta-llama]] — iRoPE + codistillation approach
