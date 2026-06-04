---
title: xAI (Grok)
created: 2026-06-01
updated: 2026-06-02
type: provider
tags: [provider, lab, model, reasoning, coding, multimodal, agentic, tool-use, pricing, api, closed, token-cost, timeline]
sources: [raw/articles/llm-provider-xai-grok-2026.md]
confidence: high
---
<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge competitive">Competitive</span>
    <span class="open-weight-partial">● Partial weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>LLM Provider<span class="entity-meta-key">HQ</span>San Francisco, US<span class="entity-meta-key">Valuation</span>$80B<span class="entity-meta-key">Key Models</span>Grok 4, Grok Code Fast 1
  </div>
</div>
# xAI (Grok)

## Overview

xAI is an artificial intelligence company founded by Elon Musk in March 2023, with a stated mission to "understand the true nature of the universe" and build AI systems that are "maximally curious" and "maximally truthful." Unlike many competitors focused purely on commercial applications, xAI positions itself as a scientific discovery company that also produces practical AI products.

The company operates with a lean engineering team compared to larger competitors, focusing on compute-efficient model training and rapid iteration. Its deep integration with the X (formerly Twitter) platform provides unique data advantages, including real-time social media data for training and grounding.

**Funding & Valuation:** xAI has raised multiple rounds at rapidly increasing valuations — from $3.4B (Series B, Dec 2023) to $80B (Series E, May 2026, $6B new funding). Major investors include Andreessen Horowitz, Sequoia Capital, and Fidelity.

**Infrastructure:** The Memphis Supercluster ("Colossus") is one of the world's largest AI training clusters: Phase 1 deployed 100,000 NVIDIA H100 GPUs (late 2024), with Phase 2 planned for 200,000+ H200 GPUs, consuming 150+ megawatts of power.

## Model Lineup (Mid-2026)

| Model | Context | Input $/1M | Output $/1M | Type |
|-------|---------|-----------|------------|------|
| **Grok 4.3** | 1M tokens | $1.25 | $2.50 | Flagship, configurable reasoning |
| **Grok 4 Fast** | 1M tokens | $0.20 | $0.50 | Cost-optimized reasoning |
| **Grok Build 0.1** | 256K tokens | $1.00 | $2.00 | Agentic coding specialist |
| **Grok 4** (legacy) | 1M tokens | $3.00 | $15.00 | Superseded by 4.3 |

**Grok 4.3 Key Features:** Configurable reasoning effort (non-reasoning mode available), native video understanding, strong agentic tool calling, web search + X search integration, 1M token context window, role-flexible message ordering.

**Legacy Models:** Grok 3/3 Mini aliased to Grok 4.3. Grok-1 (314B open-weight) holds historical significance as xAI's first open release.

## Specialized APIs

| Capability | Pricing |
|------------|---------|
| Image Generation (Imagine) | $0.02 / image |
| Video Generation (Imagine) | $0.05 / sec (480p/720p) |
| Voice Agent | $3.00 / hour |
| Text-to-Speech | $15.00 / 1M characters |
| Speech-to-Text (streaming) | $0.20 / hour |

## API Details

xAI's API is **OpenAI-compatible**, enabling use with standard SDKs:

```python
from openai import OpenAI
client = OpenAI(api_key="KEY", base_url="https://api.x.ai/v1")
response = client.chat.completions.create(model="grok-4.3", messages=[...], reasoning_effort="low")
```

- Endpoints: `/chat/completions`, `/embeddings`, Voice API, Imagine API, moderation
- Model aliasing: `<name>` (latest stable), `<name>-latest` (newest features), `<name>-<date>` (pinned)
- Free tier: up to $150/month in API credits via data-sharing program (verify current availability)
- Tool use: Web Search, X Search, custom function calling

## Benchmarks

Grok 4 achieved **92.7%** on LMSYS Chatbot Arena, placing it among top-tier models. Grok 4.3 is positioned as competitive with GPT-5.x and Claude Opus 4.x at significantly lower pricing:

| Model | Input | Output | Blended Rate* |
|-------|-------|--------|---------------|
| **Grok 4.3** | $1.25 | $2.50 | ~$2.19 |
| Grok 4 Fast | $0.20 | $0.50 | ~$0.39 |
| GPT-5.x (frontier) | ~$10 | ~$30 | ~$21.43 |
| Claude Opus 4.x | ~$15 | ~$75 | ~$53.57 |

*Blended rate assumes 7:2:1 cache-hit:input:output ratio.

## Strengths / Weaknesses

**Strengths:**
- Aggressive pricing — Grok 4.3 is 5-10x cheaper than comparable GPT/Claude models
- Native video understanding — few competitors offer this
- Real-time grounding via Web Search + X Search integration
- Unique distribution moat through X platform (500M+ MAU)
- Massive dedicated compute cluster enabling rapid training cycles
- Configurable reasoning — balance speed/cost vs. accuracy per request
- Grok Build 0.1 purpose-built for agentic coding workflows

**Weaknesses:**
- Fully proprietary/closed-source — no self-hosting or fine-tuning
- Knowledge cutoff November 2024 without search tools
- No logprobs support on Grok 4.20+ models
- Smaller ecosystem and fewer third-party integrations than [[openai]] or [[anthropic]]
- Primarily English-optimized, limited multilingual support
- Brand risk — founder's public persona may deter enterprise customers

## Recent Developments

**April 2026:** Grok 4.3 launched — 1M context, $1.25/$2.50 pricing, configurable reasoning, native video input.

**May 2026:** Grok Build 0.1 released — agentic coding model at $1.00/$2.00.

**May 2026:** Series E funding — $6B raised at $80B valuation.

**2026:** Voice and Imagine APIs expanded beyond text, integrated into X platform. Colossus Phase 2 expansion planned with NVIDIA Blackwell systems.

[[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]] · [[extended-thinking]]
