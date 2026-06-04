---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge low-cost">Low Cost</span>
    <span class="provider-badge cn">🇨🇳 Beijing</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge reasoning"><span class="cap-icon">🧠</span> Reasoning</span>
    <span class="capability-badge coding"><span class="cap-icon">💻</span> Coding</span>
    <span class="capability-badge vision"><span class="cap-icon">👁️</span> Vision</span>
    <span class="capability-badge multimodal"><span class="cap-icon">🔀</span> Multimodal</span>
  </div>
</div>

domain: llm-providers
type: provider
title: Zhipu AI (GLM)
sources: [raw/articles/llm-provider-zhipu-ai-2026.md]
tags:
  - provider/china
  - provider/generative-ai
  - open-source
aliases: Zhipu Ai
created: 2026-06-01
updated: 2026-06-02
---
# Zhipu AI (Z.ai)

## Overview
- **Legal Name:** Knowledge Atlas Technology Joint Stock Co., Ltd. (北京智谱华章科技有限公司)
- **Founded:** 2019, Tsinghua University spinout (Knowledge Engineering Group)
- **Founders:** Tang Jie, Li Juanzi; **CEO:** Zhang Peng
- **HQ:** Beijing, China; global brand: Z.ai
- **Stock:** SEHK: 2513 — world's first major LLM company IPO (Jan 8, 2026)
- **IPO:** HK$4.35B raised (~$558M); debut valuation HK$51.16B (~$6.8B); first day +13.1%
- **Revenue:** 312.4M yuan (~$43M) in 2024
- **Employees:** 800+ (2024)
- **US Entity List:** Added Jun 26, 2025 (national security concerns)
- **Pre-IPO Investors:** Alibaba, Tencent, Meituan, Ant Group, Xiaomi, HongShan, Prosperity7 ($400M)

## Strategy
One of China's "Six AI Tigers." Spun out of Tsinghua's academic research group — deep NLP and knowledge graph pedigree. Strategy: open-weight GLM models (MIT License) for developer adoption + proprietary flagship models (GLM-5) for enterprise. Hardware independence via Huawei Ascend/Cambricon chips — protected from US export restrictions. Unified platform: models, APIs, agents (AutoGLM), and consumer apps (Qingyan).

## Model Lineup: GLM Family (2026)

| Model | Release | License | Parameters | Key Features |
|-------|---------|---------|------------|--------------|
| **GLM-5** | Feb 2026 | Proprietary | 744B MoE (40B active) | 28.5T tokens, 200K context, Huawei Ascend |
| **GLM-5.1** | Apr 2026 | MIT | — | AI coding agents run autonomously for hours |
| **GLM-4.7** | Dec 2025 | — | — | Strong coding; outperforms Gemini 3.0 Pro in some benchmarks |
| **GLM-4.6V** | Dec 2025 | — | — | Vision-language with native tool-calling |
| **GLM-4.5V** | Aug 2025 | Open | 106B | Visual understanding; open-sourced |
| **GLM-4.5 / Air** | Jul 2025 | MIT | — | First under MIT License; runs on 8× NVIDIA H20 |
| **GLM-4-Plus** | Aug 2024 | Proprietary | — | Enhanced reasoning, multilingual |

## Hardware Independence
Key strategic advantage — trains and runs on domestic Chinese chips:
- **Huawei Ascend:** Primary training hardware for GLM-5
- **Cambricon:** Native FP8/Int4 quantization (GLM-4.6+)
- **Moore Threads:** Native FP8 on domestic GPUs
- This independence protects Z.ai from US semiconductor export restrictions

## Product Ecosystem

| Product | Type | Notes |
|---------|------|-------|
| **Qingyan AI** | Conversational assistant | RAG, web browsing, data visualization, document analysis |
| **Ying (影)** | Text-to-video | 6-second clips; ~30s generation; competitor to Sora |
| **AutoGLM 2.0** | Autonomous agent platform | World's first mobile agent; cross-app task completion |
| **CodeGeeX** | Code generation | IDE plugins; multi-language support |
| **CogVideoX** | Text-to-video (open) | Apache 2.0; DiT-based architecture |
| **CogVLM / CogView** | Vision / Image | Earlier vision models; groundwork for GLM-4.xV |

## API & Developer Access
- OpenAI-compatible SDKs and endpoints
- Base URL: openapi.zhipu.ai
- Supports cURL, Python, Java SDKs
- Drop-in replacement for existing OpenAI integrations
- GLM-4.5 open weights on Hugging Face (MIT License)

## Pricing (API)
GLM-4-Flash offers a generous free tier. GLM-4-Plus: ~¥0.05/1K tokens (input and output). GLM-5 pricing at enterprise tier. MIT-licensed models (GLM-4.5, GLM-5.1) available for commercial use without licensing fees.

## Global Expansion

| Region | Activity |
|--------|----------|
| **Middle East** | Offices established; Prosperity7 $400M investment (May 2024) |
| **United Kingdom** | Office (2025) |
| **Singapore** | Office (2025) |
| **Malaysia** | Office (2025) |
| **Southeast Asia** | Innovation centers in Indonesia and Vietnam (2025) |

## Key Benchmarks
- GLM-4.7 outperforms Gemini 3.0 Pro in some coding benchmarks
- GLM-5.1 enables AI coding agents to run autonomously for hours
- GLM-4.5 runs on 8× NVIDIA H20 — efficient for its capability class
- Strong performance on Chinese NLP tasks (native advantage)

## Strengths
- World's first major LLM company to go public (HKEX, Jan 2026)
- Academic pedigree: Tsinghua University KEG origins
- MIT-licensed open weights (GLM-4.5, GLM-5.1) for developer adoption
- Hardware independence (Huawei Ascend, Cambricon) — immune to US export bans
- Comprehensive platform: models, APIs, agents, consumer apps
- Strong Chinese NLP capabilities (native advantage)
- AMiner integration (academic search engine) provides unique data access
- AutoGLM 2.0 — world's first mobile agent with cross-app task completion
- Government-backed investors (Alibaba, Tencent, Meituan, Ant Group)

## Weaknesses
- US Entity List placement (Jun 2025) restricts access to advanced US semiconductors
- Post-IPO share price volatility (23% single-day drop in Feb 2026)
- Revenue (~$43M) modest relative to IPO valuation (~$6.8B)
- Balancing open-source strategy with commercial monetization
- Regulatory environment: Chinese AI regulations evolving
- Competition from well-funded Chinese peers (DeepSeek, MiniMax, Moonshot)
- International brand recognition lags behind OpenAI, Anthropic, Google

## Recent Developments
- Apr 2026: GLM-5.1 released (MIT License); shares rose 11.5%
- Feb 2026: GLM-5 released (744B MoE, 40B active, 200K context)
- Feb 2026: Shares dropped 23% amid broader market concerns
- Jan 2026: IPO on HKEX (2513.HK); raised ~$558M at ~$6.8B valuation
- Dec 2025: GLM-4.7 and GLM-4.6V released
- Jun 2025: Added to US Entity List

## Competitive Positioning
Among China's Six AI Tigers: Z.ai ranks #3 by IDC (2024 LLM player). Differentiates through hardware independence, open-weight strategy, and comprehensive platform. Competes globally with OpenAI (GPT), Anthropic (Claude), Google (Gemini), Meta (Llama). In China, competes with DeepSeek, Qwen, MiniMax, Moonshot, Baichuan.

[[deepseek]] · [[alibaba-qwen]] · [[minimax]] · [[moonshot-ai]] · [[stepfun]] · [[baichuan]]
