---
domain: llm-providers
type: provider
title: Perplexity AI (Sonar)
sources: [raw/articles/llm-provider-perplexity-2026.md]
tags:
  - provider/llm-lab
  - provider/us
  - provider/search
aliases: Perplexity
created: 2026-06-01
updated: 2026-06-02
---
# Perplexity AI (Sonar)

## Overview
- **Founded:** August 2022, San Francisco, California
- **Founders:** Aravind Srinivas (CEO, ex-DeepMind/OpenAI/Google Brain), Denis Yarats (CTO, ex-Meta FAIR), Johnny Ho (ex-Quora), Andy Konwinski (co-founder Apache Spark/Databricks)
- **Valuation:** $21.21B (Series E-6, February 2026)
- **Funding:** $1.5B+ total; investors include Jeff Bezos, Nvidia, SoftBank, IVP, Accel
- **ARR:** $450M+ annualized (March 2026); targeting $656M by end of 2026
- **Users:** 45M MAU (late 2025), 780M queries/month (~30M/day), 800% YoY growth
- **Employees:** ~90-100; ARR per employee ~$2M (highest in AI industry)
- **Retention Rate:** 85%
- **IPO Target:** 2028

## Strategy
Not a traditional LLM provider — an AI-powered search and answer engine. Core innovation is RAG architecture: every response grounded in real-time web search (24-48hr freshness) with automatic citations. Dual-surface business: consumer search (perplexity.ai) + developer APIs (Sonar API, Search API, Agent API). 100% subscription-focused (discontinued ads in Feb 2026; 2024 ad revenue was only $20K).

## Model Family: Sonar (2026)

| Model | API ID | Context | Key Features | Status |
|-------|--------|---------|--------------|--------|
| **Sonar (Standard)** | sonar | 128K | Fastest (~121 t/s), default Free tier; based on Llama 3.3 70B | Active |
| **Sonar Pro** | sonar-pro | 200K | 2× more citations, default on Pro/Max | Active |
| **Sonar Deep Research** | sonar-deep-research | 128K | Agentic multi-step research loop | Active |
| **Sonar Reasoning Pro** | sonar-reasoning-pro | 128K | Enhanced CoT reasoning, <think> section, real-time search | Active (Dec 2025) |
| **R1-1776** | r1-1776 | 128K | Uncensored reasoning, no web search; based on DeepSeek-R1 | Active |

Pro/Max tiers also provide access to frontier models: GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, Kimi K2.6, Sonar 2.

## Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|---------------------|----------------------|
| **Sonar Small Online** | ~$0.20 | ~$0.20 |
| **Sonar (Standard)** | ~$1.00 | ~$1.00 |
| **Sonar Pro** | $3.00 | $15.00 |
| **Sonar Reasoning Pro** | Varies | Varies |
| **Sonar Deep Research** | Multi-component (citation $2/M, reasoning $3/M, search $5/K) | — |

**Subscription Tiers:**
| Plan | Price | Key Features |
|------|-------|--------------|
| Free | $0 | Unlimited basic searches, ~5 Pro Searches/day |
| Pro | $20/mo | Unlimited Pro Search, 20 Deep Research/day, premium model picker, Comet Plus |
| Max | $200/mo | All Pro + 10K Computer credits, Model Council (side-by-side LLM comparison), Sora 2 Pro |
| Enterprise Pro | $40/seat/mo | 500 Deep Research/day, SSO/SCIM, SOC 2 Type II |
| Enterprise Max | $325/seat/mo | Unlimited Deep Research, organization-wide analytics |

## Key Benchmarks

| Benchmark | Sonar Pro | Notes |
|-----------|-----------|-------|
| **SimpleQA F-Score** | **0.858** | Highest at time of test |
| **Citation Error Rate** | **37%** | Best-in-class (ChatGPT Search: 67%, Grok 3: 94%) |
| **Factual Accuracy** | 94% | Incremys 2026 |
| **Citation Accuracy** | 97% | Company claim |
| **GPQA Diamond** | 62.3% | Behind Claude Opus 4.7 (94.4%) |

**Multi-Model Divergence (n=1,324):** Catch Ratio 2.54 (highest in cohort); caught other models 335× vs. caught 132×; 636 unique insights (24.7% of total).

## Key Products
- **Comet Browser:** Chromium-based AI browser (free since Oct 2025); sidecar AI assistant, email/calendar integration, shopping via PayPal
- **Model Council (Feb 2026):** Side-by-side frontier model comparison on Max tier
- **Deep Research:** Agentic multi-step research with multi-component billing
- **Perplexity Pages:** Structured report generation with cited sources
- **Shopping Hub:** AI-driven product recommendations + direct purchases
- **Finance Tools:** Real-time stock quotes, earnings, peer comparisons
- **Perplexity Assistant:** Multi-modal AI assistant (cross-app task automation)

## Strengths
- Best-in-class citation accuracy (37% error rate, lowest among tested platforms)
- Real-time web grounding (24-48hr freshness vs. static training cutoffs)
- Multi-model access via Model Council (GPT, Claude, Gemini in one interface)
- Dual-surface architecture (consumer search + developer APIs)
- Strategic partnerships: $750M Microsoft Azure deal (Jan 2026), Samsung (800M devices)
- High capital efficiency ($2M ARR per employee)
- 85% retention rate indicating strong product-market fit
- Open-source search_evals evaluation framework

## Weaknesses
- 37% citation error rate still substantial (>1 in 3 citations wrong)
- Invisible failure mode: real URLs with invented claims (harder to detect than non-citation hallucinations)
- Academic benchmarks lag frontier models (GPQA Diamond: 62.3% vs. Claude Opus 4.7: 94.4%)
- Active IP litigation from major publishers (NYTimes, Dow Jones, BBC, Reddit unresolved as of May 2026)
- EU AI Act GPAI compliance risk (deadline August 2, 2026)
- Tier-to-model opacity for consumer users (Free tier auto-selects; Pro/Max can't see per-query model without API)
- HLE score stale (21.1% for Deep Research, no update in 14+ months)
- Revenue still below valuation-implied expectations ($450M ARR vs. $21B valuation)

## Recent Developments
- Feb 2026: Series E-6 at $21.21B valuation; Model Council launch
- Feb 2026: Offered $34.5B to acquire Google Chrome (antitrust-related; unlikely to succeed)
- Jan 2026: $750M Microsoft Azure deal (3-year GPU commitment)
- Oct 2025: Comet Browser made free for all users
- Sep 2025: Search API and Agent API launched; open-source search_evals framework
- May 2026: Snap deal collapsed; ARR milestone $450M+ annualized

## Competitive Landscape
Competes with Google Search (AI Overviews), ChatGPT Search (67% citation error rate), OpenAI Operator, Anthropic browser agent. Perplexity's differentiation: native RAG architecture, multi-model aggregation via Model Council, Comet AI browser. Unique position as independent third path — backed by Azure but not owned by any platform.

[[google-gemini]] · [[openai]] · [[anthropic]] · [[xai-grok]] · [[openrouter]] · [[groq]]
