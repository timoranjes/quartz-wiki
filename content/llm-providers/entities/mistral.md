---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/europe, provider/open-weight]
aliases: [Mistral AI, la Plateforme, Le Chat]
created: 2026-06-01
---
# Mistral AI

## Overview
- **Founded:** April 2023 (Paris, France)
- **Founders:** Former Meta FAIR researchers (Guillaume Lample, Timothée Lacroix) + Google DeepMind (Guillaume de Chocquee)
- **Philosophy:** "Best intelligence per watt" — frontier performance with fewer parameters
- **Partnerships:** Microsoft Azure, AWS, NVIDIA
- **Positioning:** European answer to US-dominated AI, EU data sovereignty

## Model Lineup (2026)

| Model | Architecture | Active | Total | Context | License | Input $/1M | Output $/1M |
|-------|-------------|--------|-------|---------|---------|-----------|------------|
| **Mistral Medium 3.5** | Dense | 128B | 128B | 256K | Modified MIT | $1.50 | $7.50 |
| **Mistral Large 3** | MoE | 41B | 675B | 256K | Open v25.12 | $0.50 | $1.50 |
| **Mistral Small 4** | MoE | 6.5B | 119B | 256K | Apache 2.0 | $0.15 | $0.60 |
| **Mistral NeMo** | — | — | — | — | Open | $0.02 | $0.03 |

## Edge Models (Ministral 3)
| Model | Context | License | Input/Output $/1M |
|-------|---------|---------|------------------|
| Ministral 3 14B | 256K | Open | $0.20 / $0.20 |
| Ministral 3 8B | 256K | Open | $0.15 / $0.15 |
| Ministral 3 3B | 256K | Open | $0.10 / $0.10 |

## Specialty Models
- Codestral 2508 (code, 32K, Premier)
- Devstral 2 (agentic coding, 256K, Open)
- Voxtral Small (audio input, Open)
- Pixtral 12B (vision, Open)
- OCR 3 (document AI, Premier)
- Magistral Medium (reasoning, Premier)

## Benchmarks
- Medium 3.5 SWE-bench Verified: **77.6%**
- Large 3: competitive with GPT-4o-class
- Small 4: outperforms heavier alternatives on agentic workloads (6.5B active)

## API & Availability
- la Plateforme (API): OpenAI-compatible endpoint
- Le Chat (consumer): Free (~25 msgs/day), Pro ($14.99/mo), Team ($24.99/user/mo)
- Cloud: Azure AI Foundry, AWS Bedrock, NVIDIA NIM, GCP Vertex AI
- Self-deploy: vLLM, Ollama, llama.cpp

## Licensing
- Apache 2.0: NeMo, Ministral series, Pixtral 12B, Devstral Small 1.1, Small 4
- Modified MIT: Medium 3.5, Large 3, Voxtral Small
- Premier (restricted): Codestral, OCR 3, Embed, Moderation 2

## Strengths
- EU data sovereignty (strongest GDPR compliance)
- Most diverse open-weight portfolio
- Efficiency-first philosophy
- Unified models (Medium 3.5: instruct + reasoning + coding in one)
- Document AI stack (OCR + annotations + QnA)
- Cheapest Le Chat ($14.99/mo vs $20 for competitors)

## Cost Comparison
- Large 3: 80% cheaper input, 90% cheaper output vs GPT-5.4
- 83% cheaper input, 90% cheaper output vs Sonnet 4.6

## Recent Developments
- Apr 2026: Medium 3.5 released (128B dense, SWE-bench 77.6%)
- Mar 2026: Small 4 released (119B MoE, 6.5B active, Apache 2.0)
- Mar 2026: Devstral 2 (agentic coding)
- Feb 2026: Voxtral Mini Transcribe + TTS

[[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[alibaba-qwen]] · [[deepseek]]
