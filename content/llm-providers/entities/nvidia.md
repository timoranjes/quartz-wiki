---
domain: llm-providers
type: provider
tags: [provider/us, model/open-weight, model/inference]
aliases: [Nvidia, Nemotron, NIM]
created: 2026-06-01
---
# Nvidia

## Overview
Nvidia develops language models primarily as **reference implementations** to showcase their GPU hardware capabilities. Models are open-weight and optimized for Nvidia GPUs.

## Key Models (2026)

| Model | Params | Notes |
|-------|--------|-------|
| Nemotron-4 340B | 340B | Large open-weight model |
| Nemotron-H 80B | 80B | Optimized for H100 GPUs |
| Nemotron Mini | ~5B | Edge-optimized |

## Strengths
- **Hardware optimization**: Models are optimized for Nvidia GPUs
- **Open-weight**: All models released openly
- **NIM containers**: One-click deployment via Nvidia Inference Microservices
- **Training frameworks**: NeMo framework for custom model training

## Pricing
| Service | Cost |
|---------|------|
| Models (download) | Free |
| Nvidia API (hosted) | $0.20–$2.00/1M input |
| NIM (self-hosted) | Hardware cost only |

## Positioning
Hardware-first company. LLMs serve to demonstrate GPU capabilities and provide reference implementations. Not competing directly with OpenAI/Anthropic on model quality.

## Related
- [[meta-llama]] — Also open-weight, competing on hardware optimization
