---
title: Mistral AI
created: 2026-06-01
updated: 2026-06-02
type: provider
tags: [provider, lab, model, open-weight, reasoning, coding, multimodal, agentic, pricing, api, licensing, token-cost, timeline]
sources: [raw/articles/llm-provider-mistral-2026.md]
confidence: high
---
# Mistral AI

## Overview

Mistral AI is a French artificial intelligence company founded in April 2023 by former Meta and DeepMind researchers — Arthur Mensch (CEO, ex-DeepMind/Cerebras), Timothée Lacroix (ex-Meta), and Guillaume Lample (ex-Meta/Cerebras). The company emerged from the European AI research community with a mission to build open, sovereign AI that competes with American and Chinese giants while maintaining European values of transparency, privacy, and openness.

**Funding & Valuation:** Mistral has raised approximately $2.5-3B total across five rounds, reaching a $15B+ valuation (Series D, early 2026). Major investors include Andreessen Horowitz, General Catalyst, and Lightspeed Venture Partners.

**Headquarters:** Paris, France, with offices in London and New York. Team size ~250-350+ employees (mid-2026).

**Positioning:** Europe's leading AI company — open-weight champion alongside [[meta-llama]], price disruptor undercutting US competitors, enterprise-friendly with GDPR-compliant EU hosting.

## Model Lineup (Mid-2026)

### General Purpose

| Model | Context | Input $/1M | Output $/1M | License | Notes |
|-------|---------|-----------|------------|---------|-------|
| **Mistral Large 3** | 128K | $0.50 | $1.50 | Open | Flagship multimodal, 40+ languages |
| **Mistral Medium 3.5** | 128K | $1.50 | $7.50 | Open | 128B dense, strong instruction-following |
| **Mistral Small 4** | 128K | $0.10 | $0.30 | Apache 2.0 | SOTA small model, edge-friendly |

### Ministral Family (Edge)

| Model | Input/Output $/1M | Use Case |
|-------|-------------------|----------|
| Ministral 3B | $0.10 / $0.10 | On-device, ultra-lightweight |
| Ministral 8B | $0.10 / $0.10 | Lightweight general-purpose |
| Ministral 14B | $0.20 / $0.20 | Balanced performance/efficiency |

### Code Models

| Model | Context | Input $/1M | Output $/1M | License |
|-------|---------|-----------|------------|---------|
| **Codestral** | 256K | $0.30 | $0.90 | Premier |
| **Devstral 2** | 128K+ | $0.40 | $2.00 | Open |
| Devstral Small 2 | — | $0.10 | $0.30 | Labs |

Codestral features fill-in-the-middle (FIM) support and multi-language code understanding. Devstral 2 is designed for agentic coding with IDE integration (VS Code, JetBrains).

### Reasoning & Specialized

| Model | Input $/1M | Output $/1M | Purpose |
|-------|-----------|------------|---------|
| **Magistral Medium** | $2.00 | $5.00 | Complex math, multi-step logical analysis |
| Magistral Small | $0.50 | $1.50 | Lightweight reasoning |
| **OCR 3** | — | $2/1K pages | Document extraction |
| Voxstral TTS | $0.016/1K chars | — | Text-to-speech, voice cloning |
| Embeddings | — | — | Semantic search (Apache 2.0) |

### Historical Models

**Mixtral 8x7B** (45B total, 12.9B active MoE) and **Mixtral 8x22B** (~141B total, ~39B active MoE) — breakthrough open-weight MoE models that popularized sparse activation in the open-source community.

## Vibe Platform (Consumer/Team Products)

Mistral operates "Vibe," a consumer-facing AI assistant:

| Plan | Price | Features |
|------|-------|----------|
| Free | $0 | Limited messages, searches, coding |
| Pro | $14.99/mo | 6× messages, all-day coding |
| Team | $24.99/user/mo | Storage, domain verification |
| Enterprise | Custom | Custom models, SSO, private deployments |

**Interfaces:** Vibe web (long-horizon tasks), Vibe CLI (terminal coding agent), IDE plugin (VS Code, JetBrains), mobile apps. Verified students get Pro for $5.99/mo.


### Upcoming Models
- **Mistral Large 2411**: Potentially a multimodal Large 2.1 model (identified in codebase)
- **Mistral-NEXT**: New open-source model with impressive capabilities across a range of tasks

## API & Availability

- **la Plateforme:** Mistral's native API with dedicated Python/JS SDKs
- **Batch API:** 50% discount on batch processing
- **Fine-tuning:** $1/1M tokens training, custom model deployment available
- **Cloud platforms:** Azure AI Foundry, AWS Bedrock, NVIDIA NIM, GCP Vertex AI
- **Local deployment:** vLLM, Ollama, llama.cpp (open-weight models)
- **Framework support:** LangChain, LlamaIndex, LiteLLM all fully supported

## Licensing

Mistral uses a multi-tier licensing strategy:
- **Apache 2.0:** Small 4, Ministral series, embeddings — most permissive
- **Open (modified):** Large 3, Medium 3.5, Devstral 2 — open with some restrictions
- **Premier (restricted):** Codestral, Magistral, OCR 3, Moderation 2 — commercial API only

## Strengths / Weaknesses

**Strengths:**
- European sovereignty — GDPR-compliant, EU-hosted infrastructure
- Most diverse open-weight portfolio: text, code, vision, OCR, speech, embeddings
- Price-to-performance leader — Large 3 is ~95% cheaper input vs. GPT-5.4
- Developer experience — clean APIs, strong SDKs, comprehensive documentation
- 50% batch API discount for offline processing
- Full fine-tuning pipeline with competitive pricing
- Unified models (Medium 3.5: instruct + reasoning + coding in one)

**Weaknesses:**
- Raw performance gap — still behind GPT-5.x and Claude Opus on some benchmarks
- Smaller compute budget — less training capacity than [[meta-llama]] or [[google-gemini]]
- Fewer third-party integrations than [[openai]]'s ecosystem
- Primarily European team, though expanding globally
- May face compute constraints for future frontier models

## Recent Developments

**April 2026:** Mistral Large 3 released — open license, $0.50/$1.50 pricing, multimodal, competitive with GPT-5.x at fraction of cost.

**March 2026:** Small 4 (119B MoE, 6.5B active, Apache 2.0) and Devstral 2 (agentic coding) released.

**Early 2026:** Series D — ~$1B raised at $15B+ valuation for compute expansion and geographic growth.

**2026:** Vibe platform expanded with CLI, IDE, mobile apps, and student discount program. Specialized releases: Magistral (reasoning), OCR 3 (document AI), Voxstral (TTS).

[[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[alibaba-qwen]] · [[deepseek]] · [[open-weight-licensing]]
