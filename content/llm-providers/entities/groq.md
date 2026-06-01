---
domain: llm-providers
type: provider
tags: [provider/us, model/inference, model/hardware]
aliases: [Groq, LPU]
created: 2026-06-01
---
# Groq

## Overview
Groq is a hardware company that built the **LPU** (Language Processing Unit), a specialized chip for ultra-fast LLM inference.

## Key Offerings
- **LPU Inference Engine**: 500+ tokens/sec on Llama 70B
- **Model hosting**: Llama, Mixtral, Gemma, and other open models
- **OpenAI-compatible API**: Drop-in replacement

## Strengths
- **Speed**: Fastest inference in the industry
- **Low latency**: Sub-100ms first token
- **Deterministic**: Consistent performance (no queuing)

## Pricing
| Model | Input | Output |
|-------|-------|--------|
| Llama 3 70B | $0.27/1M | $0.35/1M |
| Mixtral 8x7B | $0.05/1M | $0.07/1M |

## Positioning
Hardware-first company. Not a model creator — provides the fastest inference for other people's models. Competes with Together AI, Nvidia, cloud providers on serving speed.

## Related
- [[together-ai]] — Both fast inference platforms
- [[nvidia]] — Both hardware-focused AI inference
