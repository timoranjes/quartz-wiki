---
domain: llm-providers
type: provider
tags: [provider/us, model/closed-source, model/open-weight]
aliases: [Microsoft, Phi, Phi-4, Phi-3, Orca]
created: 2026-06-01
---
# Microsoft (Phi / Orca)

## Overview
Microsoft pursues a **small language model** strategy through the Phi series — high-quality models at small sizes, optimized for edge deployment and cost efficiency.

## Key Models (2026)

| Model | Params | Context | Type | Notes |
|-------|--------|---------|------|-------|
| Phi-4 | 14B | 16K | Open-weight | Best small model at launch |
| Phi-4-mini | 3.8B | 128K | Open-weight | Edge-optimized |
| Phi-4-multimodal | 5.6B | — | Multimodal | Image + text understanding |
| Orca 3 | — | — | Open-weight | Distilled from GPT-4o |

## Strategy
- **SLM focus**: Phi models punch above their weight class (14B competes with 70B models on some benchmarks)
- **Edge-first**: Designed to run on laptops, phones, edge devices
- **Azure integration**: Tight integration with Azure AI Foundry
- **Data quality > scale**: "Textbook-quality" synthetic data for training

## Pricing
| Endpoint | Input | Output |
|----------|-------|--------|
| Azure AI (Phi-4) | $0.07/1M | $0.14/1M |
| Azure AI (Phi-4-mini) | $0.01/1M | $0.05/1M |

## Related
- [[openai]] — Microsoft is OpenAI's primary investor and cloud provider
- [[meta-llama]] — Competing in the open-weight SLM space
