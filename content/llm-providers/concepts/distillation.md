---
domain: llm-providers
type: concept
tags: [concept/training, concept/distillation, concept/optimization]
aliases: [Knowledge Distillation, Model Compression, Teacher-Student]
created: 2026-06-01
---
# Knowledge Distillation

## Overview
Knowledge distillation trains a smaller "student" model to mimic the behavior of a larger "teacher" model, achieving comparable quality at a fraction of the parameter count and inference cost.

## Types of Distillation

### Logit Distillation
- Student learns from teacher's output logits (probability distributions)
- Captures teacher's "dark knowledge" — confidence on wrong answers
- Most common approach

### Hidden State Distillation
- Student learns from teacher's intermediate layer activations
- More information transfer, more compute-intensive

### Behavioral Distillation
- Student learns from teacher's API outputs (not internal states)
- Used when teacher is closed-source
- **DeepSeek R1 distills** use this approach

## Notable Distillation Examples (2026)

| Student | Teacher | Method | Result |
|---------|---------|--------|--------|
| **DeepSeek R1 distills** (1.5B–70B) | DeepSeek R1 (671B) | Behavioral | Retain most reasoning capability |
| **Llama 4 Scout** (109B) | Behemoth (~2T, unreleased) | **Codistillation** | Training-time distillation with interleaved layers |
| **Qwen distills** | Qwen-Max | Logit + behavioral | Strong small models (0.5B–7B) |
| **Mistral Small** | Mistral Large | Logit distillation | Competitive mid-tier model |

### Meta's Codistillation (Llama 4)
- Teacher model (Behemoth, ~2T parameters) trained but **not released**
- During student training, Behemoth's outputs are interleaved
- Student sees teacher's predictions during its own gradient updates
- More effective than post-hoc distillation

### DeepSeek R1 Distillation Chain
1. Train R1 (671B MoE) via pure RL
2. Generate high-quality reasoning data from R1
3. Distill into smaller models (1.5B, 7B, 8B, 14B, 32B, 70B)
4. Result: 7B model with reasoning capability approaching R1

## Benefits
- **Cost reduction** — Smaller model = cheaper inference
- **Edge deployment** — Distilled models fit on consumer hardware
- **Latency** — Faster response times
- **Democratization** — Frontier capabilities accessible to all

## Limitations
- Student cannot exceed teacher's capabilities
- Quality gap widens for highly complex tasks
- Distillation data can be expensive to generate

## Related
- [[quantization]] — Distillation + quantization can be combined
- [[deepseek]] — R1 distillation is DeepSeek's key contribution
- [[meta-llama]] — Codistillation is Meta's novel approach
