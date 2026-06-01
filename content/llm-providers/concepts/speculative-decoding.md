---
domain: llm-providers
type: concept
tags: [concept/optimization, concept/decoding, concept/inference]
aliases: [Speculative Decoding, Speculative Generation, Medusa]
created: 2026-06-01
---
# Speculative Decoding

## Overview
Speculative decoding uses a smaller "draft" model to propose multiple tokens, then verifies them with the larger target model in parallel. This can achieve **2-3× throughput improvement** with **zero quality loss** (mathematically identical output).

## How It Works
1. Draft model (e.g., 7B) generates N tokens autoregressively
2. Target model (e.g., 70B) verifies all N tokens in a single forward pass
3. Accepted tokens are kept; rejected tokens are re-sampled
4. Repeat

## Key Techniques

### Traditional Speculative Decoding
- Separate draft model
- 2-3× speedup when draft model is well-matched
- Used in production by several cloud providers

### Medusa Decoding
- Adds lightweight "heads" to the model during training
- Each head predicts tokens at different offsets
- No separate draft model needed
- **Mistral uses Medusa** for Medium 3.5

### EAGLE/Lookahead Decoding
- Uses internal hidden states for drafting
- More efficient than separate draft models
- Up to 3× speedup

## Provider Adoption

| Provider | Technique | Speedup | Notes |
|----------|-----------|---------|-------|
| **Mistral** | Medusa | 2-3× | Built into Medium 3.5 |
| **DeepSeek** | Internal speculative | ~2× | Used in V4-Pro inference |
| **OpenAI** | Internal | Undisclosed | Not publicly confirmed |
| **Google** | Internal | Undisclosed | Used in Gemini serving |

## Benefits
- **Zero quality loss** — mathematically identical to standard decoding
- **Throughput** — 2-3× improvement
- **Latency** — Reduced per-token latency for long generations
- **Cost** — Fewer target model forward passes

## Limitations
- Requires well-matched draft model
- Speedup depends on token acceptance rate (typically 70-85%)
- Less effective for creative/unpredictable outputs

## Related
- [[moE-architecture]] — MoE models benefit less from speculative decoding
- [[quantization]] — Both are inference optimizations that can be combined
