title: Meta (Llama)
tags: provider, open-weight, model, architecture, multimodal, pricing, api, licensing, benchmark, controversy
# Meta (Llama)

## Overview

Meta (formerly Facebook) develops and releases the Llama family of open-weight large language models through its Meta Superintelligence Labs division. Headquartered in Menlo Park, California, Meta's AI strategy has been described as the "Android strategy for AI" — releasing open-weight models to become the de facto standard and drive engagement across its platforms (Facebook, Instagram, WhatsApp, Threads).

Llama is the most widely deployed open-weight LLM family globally, with hundreds of derivative models and fine-tunes. The company also operates the Meta AI assistant, a consumer product powered by Llama across its social platforms.

## Model Lineup (Mid-2026)

### Llama 4 Family (April 2025)

Llama 4 introduced native multimodality via early fusion of text and vision data, with a massive 10M token context window.

| Model | Architecture | Active / Total Params | Context | Key Features |
|-------|-------------|----------------------|---------|-------------|
| **Llama 4 Maverick** | 128-expert MoE | 17B / ~400B | 10M tokens | Memory, personalization, complex reasoning |
| **Llama 4 Scout** | 16-expert MoE | 17B / ~109B | 10M tokens | Long documents, single-H100 efficiency |

**Maverick Benchmarks:** MMLU Pro 80.5, GPQA Diamond 69.8, LiveCodeBench 43.4, MMMU 73.4, LMArena ELO 1417. SWE-bench Verified ~65-70%.

### Llama 3 Family (Production-Tested)

| Model | Parameters | Notes |
|-------|-----------|-------|
| Llama 3.1 (8B / 70B / 405B) | Multiple | Tool use, 128K context, multilingual |
| Llama 3.2 (1B / 3B / 11B Vision / 90B Vision) | Multiple | Edge-optimized, image + text reasoning |
| Llama 3.3 (70B) | 70B | 405B-quality at lower cost |

### Llama Guard (Safety Models)

Llama Guard 3 is available in 1B and 8B variants for content safety classification of LLM inputs and responses.

## Licensing

The Llama License is a custom permissive license (NOT OSI open source):
- Permitted: research, commercial use, modification, distribution
- Restricted: using outputs to improve other LLMs; entities with >700M MAU need separate written permission
- Requires: attribution and implementation of Llama Guard or equivalent safety measures

## API & Availability

Meta does not offer a direct hosted API. Access is available through:

| Channel | Notes |
|---------|-------|
| **Open weights** | Hugging Face, llama.com (registration required) |
| **Cloud platforms** | AWS Bedrock, Google Cloud Vertex AI, Azure AI |
| **Inference providers** | Together AI, Groq (sub-100ms TTFT), OpenRouter, DeepInfra |
| **Local deployment** | Ollama, vLLM, llama.cpp, LM Studio, TensorRT-LLM |

**Cost efficiency:** Distributed inference ~$0.19/M tokens (3:1 blended), single H100 ~$0.30-$0.49/M tokens — significantly lower than closed-source alternatives.

## Muse Spark (April 2026)

Meta Superintelligence Labs launched Muse Spark, the company's first proprietary closed-weight AI model. This represents a strategic shift toward competing directly with [[openai]] and [[anthropic]], creating tension with Meta's open-source positioning.

## Strengths / Weaknesses

**Strengths:**
- Most deployed open-weight LLM family with massive community ecosystem
- 10M token context window — among the largest available
- Dramatically lower inference costs than closed-source models
- Full deployment flexibility: self-hosting, edge, cloud-agnostic
- Customization allowed: fine-tuning, distillation, modification
- Native multimodality in Llama 4 with early fusion

**Weaknesses:**
- Open-weight models can be used without safety guardrails
- License restrictions prevent true OSI open-source classification
- Capability gap on hardest benchmarks vs. top closed-source models
- No direct Meta-hosted API
- LMArena benchmark controversy (April 2025): Meta submitted an "experimental chat version" that differed from the public release
- Muse Spark's closed-weight release creates tension with open-source positioning

## Recent Developments

**April 2025:** Llama 4 released (Maverick + Scout) with native multimodality and 10M context window.

**December 2024:** Llama 3.3 70B released, matching Llama 3.1 405B performance at lower cost.

**April 2026:** Muse Spark launched — Meta's first closed-weight proprietary model.

**Case studies:** Stoque achieved 50% reduction in repetitive support queries; Shopify reported +76% token throughput and 33% compute cost savings.

[[openai]] · [[anthropic]] · [[google-gemini]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]] · [[open-weight-licensing]]