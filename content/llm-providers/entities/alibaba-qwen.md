---
title: Alibaba Qwen
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, cloud-platform, model, reasoning, coding, vision, audio, multimodal, open-weight, pricing, api, token-cost, timeline]
sources: [raw/articles/llm-provider-alibaba-qwen-2026.md]
confidence: 0.95
---
# Alibaba Qwen

## Overview

Qwen (通义千问, Tongyi Qianwen) is a family of large language models developed by [[alibaba-group]]'s Tongyi Lab. First released in 2023, Qwen has grown into China's leading LLM provider, powering internal Alibaba applications and external customer deployments through Alibaba Cloud's Model Studio (百炼, Bailian) platform. Many Qwen models are released as open weights under the Apache 2.0 license.

As of mid-2026, the latest generation is Qwen 3.7 (Max, Plus, Flash variants), with the Qwen Omni line offering full multimodal support across text, image, audio, and video. Model Studio uniquely hosts both Qwen models and competing third-party models including [[deepseek]], [[moonshot-ai]] Kimi, [[zhipu-ai]] GLM, and [[minimax]].

## Model Lineup

| Model | API ID | Context | Type |
|-------|--------|---------|------|
| **Qwen 3.7 Max** | `qwen3.7-max` | 131K tokens | Flagship text generation |
| **Qwen 3.7 Plus** | `qwen3.7-plus` | 131K tokens | Multimodal enhanced |
| **Qwen 3.6 Flash** | `qwen3.6-flash` | 131K tokens | Lightweight, cost-efficient |
| **Qwen 3.5 Omni Plus** | `qwen3.5-omni-plus` | 32K tokens | Text + image + audio + video |
| **Qwen 3.5 Omni Realtime** | `qwen3.5-omni-plus-realtime` | 32K tokens | Real-time voice dialogue |

**Specialized models:** Wan 2.7 Image Pro (text-to-image), Qwen-Image 2.0 Pro (image gen/edit), HappyHorse 1.0 (video generation: T2V/I2V/R2V/edit), Tripo H3.1/P1.0 (3D generation), CosyVoice V3.5 Plus (TTS), Fun-ASR (speech recognition), Fun-Music V1 (music generation).

**Embedding & Reranking:** Text Embedding V4, Tongyi Embedding Vision Plus, Qwen3 Rerank.

## Benchmarks

Qwen 3.7 Max delivers competitive performance across major evaluation suites:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMLU | ~85-88% | Strong general knowledge |
| CMMLU | ~90%+ | Industry-leading Chinese understanding |
| C-Eval | ~88-90% | Chinese evaluation benchmark |
| GSM8K | ~90%+ | Mathematical reasoning |
| HumanEval | ~85%+ | Code generation |
| LiveCodeBench | ~75-80% | Competitive programming |

## API Ecosystem

Qwen models are served through Alibaba Cloud's DashScope platform (`dashscope.aliyuncs.com`), offering an OpenAI-compatible REST API. Official SDKs are available for Python (`dashscope`), JavaScript, and Java. The API supports streaming, vision inputs, and omni-modal realtime audio.

Model Studio provides unified access to all Qwen models plus hosted third-party models, an Agent Builder with visual workflow orchestration, fine-tuning capabilities, and a pre-built template marketplace. Billing options include pay-as-you-go, token plan subscriptions, and PTU dedicated deployment. New users receive 70M free tokens.

Rate limits range from 60 RPM (free tier) to 1,000+ RPM (token plan). Enterprise custom limits are available through Alibaba Cloud account managers.

## Strengths / Weaknesses

**Strengths:**
- **China market leader:** Dominant position in China's AI model market
- **Full modal coverage:** Most comprehensive multimodal family among Chinese providers (text, image, video, audio, 3D)
- **Open-source:** Regular Apache 2.0 open-weight releases building a global community
- **Cost efficiency:** Competitive pricing with active promotional discounts (50% off Qwen 3.7 Max)
- **Platform depth:** Model Studio is a comprehensive one-stop AI development platform
- **Alibaba ecosystem:** Deep integration with Alibaba Cloud, Taobao, DingTalk

**Weaknesses:**
- **Global brand recognition:** Less known outside China compared to [[openai]], [[anthropic]], [[google-gemini]]
- **English benchmark gap:** Still trails top Western models on some English benchmarks
- **Geopolitical risk:** US-China tech tensions limit Western market adoption
- **Documentation:** Primarily Chinese-language with limited English resources

## Key Relationships

- **Alibaba Group / Tongyi Lab** — Parent organization and primary research lab
- **DeepSeek** — Hosted as third-party model on Model Studio alongside Qwen
- **Moonshot AI** — Kimi K2.6 available on Model Studio
- **Zhipu AI** — GLM-5.1 available on Model Studio
- **MiniMax** — M2.7 model available on Model Studio

## Recent Developments

**Model releases (2025-2026):** Qwen 3.5 Omni with real-time voice (2025), Qwen 3.6 Flash for cost-efficient inference (2025), Qwen 3.7 Max/Plus (2026, current flagship), Qwen-Image 2.0 Pro, HappyHorse 1.0 video generation family, CosyVoice V3.5 Plus, Text Embedding V4, Qwen3 Rerank.

**Platform updates:** Model Studio PTU now supports [[deepseek]] V4 Pro deployment; token plan subscription packages compatible with mainstream AI toolchains; enhanced Agent Builder with visual workflow orchestration; 70M free token trial for new users.

**Open-source:** Continued regular releases on Hugging Face under Apache 2.0, growing community of fine-tunes and derivatives, active research paper publications.
