---
title: DeepSeek
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, model, reasoning, coding, open-weight, pricing, api, token-cost, timeline]
sources: [raw/articles/llm-provider-deepseek-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge budget">Low Cost</span>
    <span class="provider-badge cn">🇨🇳 Hangzhou</span>
  </div>
  <div class="entity-meta">
    <div><span class="entity-meta-key">Latest Model</span><span class="entity-meta-value">DeepSeek-V3.2</span></div>
    <div><span class="entity-meta-key">Strength</span><span class="entity-meta-value">LiveCodeBench Top-3</span></div>
    <div><span class="entity-meta-key">Pricing</span><span class="entity-meta-value">~1/10 of GPT-4</span></div>
  </div>
</div>

# DeepSeek

## Overview

DeepSeek (深度求索) is a Chinese AI company founded in 2023, backed by quantitative hedge fund High-Flyer (幻方量化). Led by founder and CEO Liang Wenfeng (梁文锋), DeepSeek has rapidly emerged as a disruptive force in the global LLM market, known for frontier-level coding performance at dramatically lower costs than Western competitors. Most DeepSeek models are released as open weights under the MIT license.

The current flagship is the V4 family (April 2026), featuring novel CSA+HCA hybrid attention, Muon optimizer, and FP4 quantization-aware training. DeepSeek V4 Pro achieves #1 on LiveCodeBench (93.5) and perfect 120/120 on Putnam 2025, while costing approximately 1/12th the price of comparable Western models.

## Model Lineup

| Model | ID | Total Params | Active Params | Context | License |
|-------|----|-------------|--------------|---------|---------|
| **DeepSeek V4 Pro** | `deepseek-v4-pro` | 1.6T | 49B | 1M tokens | MIT |
| **DeepSeek V4 Flash** | `deepseek-v4-flash` | 284B | 13B | 1M tokens | MIT |

**Legacy:** `deepseek-chat` and `deepseek-reasoner` names are deprecated; they map to non-thinking and thinking modes of V4 Flash respectively.

**Architecture innovations (V4):** Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) hybrid; Manifold-Constrained Hyper-Connections (mHC); Muon optimizer replacing AdamW; FP4 Quantization-Aware Training. These innovations deliver 27% of V3.2 FLOPs and 10% of V3.2 KV cache at 1M context.

## Benchmarks

DeepSeek V4 Pro Max is the world's leading coding model:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| LiveCodeBench Pass@1 | **93.5** | #1 of all models globally |
| Codeforces Rating | **3206** | Grandmaster level |
| SWE-bench Verified | **80.6%** | 0.2% behind Claude Opus 4.6 |
| Putnam 2025 | **120/120** | Perfect score |
| MMLU-Pro | 87.5% | Behind Gemini 3.1 Pro (91.0%) |
| GPQA Diamond | 90.1% | Behind Gemini 3.1 Pro (94.3%) |
| HLE | 37.7% | Behind Claude Opus 4.6 (40.0%) |

V4 Pro Max leads all coding benchmarks but trails on the hardest general knowledge and scientific reasoning benchmarks compared to top closed-source models.

## API Pricing

DeepSeek's pricing is its primary market disruptor:

| Model | Input (Cache Miss) | Output | Concurrency |
|-------|-------------------|--------|-------------|
| **V4 Flash** | $0.14/M tokens | $0.28/M tokens | 2,500 |
| **V4 Pro** | $0.435/M tokens | $0.87/M tokens | 500 |

Cache hit pricing is $0.0028/M (Flash) and $0.003625/M (Pro). At these rates, a daily coding session (50K in + 10K out × 20 requests) costs just $0.20/day for Flash vs. $30/day for Claude Opus 4.6.

## API Ecosystem

DeepSeek offers dual-compatible API endpoints: OpenAI format (`api.deepseek.com`) and Anthropic format (`api.deepseek.com/anthropic`), enabling seamless migration from either ecosystem. The API supports thinking mode control, JSON output, tool use/function calling, chat prefix completion, and FIM (Fill-In-the-Middle) code completion.

Models are available on [[alibaba-qwen]] Model Studio, Hugging Face, [[together-ai]], Ollama, vLLM, OpenRouter, and DeepInfra. Official Python SDK and comprehensive documentation are available at api-docs.deepseek.com.

## Strengths / Weaknesses

**Strengths:**
- **Unmatched pricing:** 10-50× cheaper than Western competitors for comparable capability
- **Coding leadership:** #1 on LiveCodeBench, Codeforces grandmaster, near-#1 on SWE-bench
- **Open-source:** MIT-licensed models with full weights available for self-hosting
- **Architecture innovation:** Novel CSA+HCA hybrid attention and Muon optimizer
- **1M context:** Full million-token context window at low cost
- **Dual API compatibility:** Both OpenAI and Anthropic format endpoints
- **Strong backing:** Financial support from High-Flyer quantitative hedge fund

**Weaknesses:**
- **No multimodal:** No image, video, audio, or vision capabilities (text-only)
- **General knowledge gap:** Trails [[google-gemini]] 3.1 Pro and [[anthropic]] Claude on MMLU-Pro, GPQA, HLE
- **Geopolitical risk:** Chinese company facing US-China tech tensions
- **Limited model range:** Only two primary models (Pro, Flash) vs. broader competitor families
- **Western adoption barriers:** Data sovereignty concerns limit enterprise uptake
- **Compute access:** Potential GPU export restrictions from US controls

## Key Relationships

- **High-Flyer (幻方量化)** — Parent company; quantitative hedge fund providing compute resources
- **Alibaba Cloud** — V4 Pro and V4 Flash hosted on Model Studio (百炼) alongside [[alibaba-qwen]] models
- **Hugging Face** — Primary open-weight distribution platform under MIT license
- **Together AI** — Third-party API access provider
- **OpenRouter** — Aggregated access through multiple backends

## Recent Developments

**Model releases:** DeepSeek-R1 (January 2025, breakthrough reasoning model that went viral), DeepSeek-R1-Zero (January 2025), DeepSeek-V4 family (April 24, 2026, major architectural leap with V4 Pro/Flash/Pro Max).

**Pricing updates:** April 26, 2026 — cache hit prices reduced to 1/10 of launch price; May 31, 2026 — V4 Pro promotional 75% discount became permanent ($0.435/M input, $0.87/M output).

**Ecosystem:** Growing community fine-tunes on Hugging Face; integration into [[alibaba-qwen]] Model Studio as a third-party hosted model; wide support from LangChain, LlamaIndex, and AI frameworks.

**Research publications:** Hybrid attention mechanisms (CSA+HCA), manifold-constrained hyper-connections, Muon optimizer for large-scale training, FP4 quantization-aware training, Mixture-of-Experts scaling.
