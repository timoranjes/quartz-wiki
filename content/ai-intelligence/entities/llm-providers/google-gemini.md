---
title: Google Gemini
created: 2026-06-02
updated: 2026-06-08
type: provider
tags: [provider, lab, cloud-platform, model, reasoning, coding, vision, audio, multimodal, agentic, tool-use, pricing, api, closed, token-cost, timeline]
sources: [raw/articles/llm-provider-google-gemini-2026.md]
confidence: 0.95
---
# Google Gemini

## Overview

Google Gemini is Google's family of large language models developed by Google DeepMind, formed from the merger of Google Brain and DeepMind. First released in December 2023 (as Gemini 1.0, succeeding the earlier Bard product), Gemini represents Google's unified AI strategy for multimodal understanding, reasoning, and generation.

Gemini is distinguished by its deep integration across Google's product ecosystem — including Search, Workspace (Docs, Sheets, Gmail, Slides), Android, and Chrome. The company leverages custom TPU (Tensor Processing Unit) hardware and Google Cloud data centers for compute infrastructure. In April 2026, Google began selling TPUs to external customers for the first time.

The developer access path is split between Google AI for Developers (ai.google.dev) for individual developers and Google Cloud Vertex AI for enterprise users. Google offers the most generous free tier among major providers, with limited-rate-limit access to most models.

## Model Lineup

### Gemini 3 Family (Current Generation)

| Model | ID | Status | Pricing in/out (per 1M) | Type |
|-------|-----|--------|-------------------------|------|
| **Gemini 3.5 Pro** | — | Announced for June 2026 | TBD | Reasoning-focused flagship |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Stable | $1.50 / $9.00 | Production flagship |
| **Gemini 3.1 Pro** | `gemini-3.1-pro-preview` | Preview | $2.00 / $12.00 (≤200K) | Premium preview |
| **Gemini 3.1 Flash-Lite** | `gemini-3.1-flash-lite` | Stable | $0.25 / $1.50 | Cost-optimized |
| **Gemini 3.1 Flash Live** | `gemini-3.1-flash-live-preview` | Preview | $0.75 audio in / $12.00 audio out | Real-time voice |
| **Gemini 3.1 Flash TTS** | `gemini-3.1-flash-tts-preview` | Preview | $1.00 in / $20.00 out | Speech generation |

### Gemini 2.5 Family

| Model | Status | Pricing | Type |
|-------|--------|---------|------|
| **Gemini 2.5 Pro** | Stable | — | Complex reasoning & coding |
| **Gemini 2.5 Flash** | Stable | — | Price-performance optimized |
| **Gemini 2.5 Flash-Lite** | Stable | $0.10 / $0.40 | Budget multimodal |

### Generative Media

| Model | Status | Description |
|-------|--------|-------------|
| **Nano Banana 2** | Stable | High-efficiency image generation |
| **Nano Banana Pro** | Stable | SOTA studio-quality image generation |
| **Imagen 4** | Stable | Text-to-image, up to 2K clarity |
| **Veo 3.1** | Preview | SOTA cinematic video with audio sync |
| **Lyria 3 Pro** | Preview | Flagship full-length song generation |

### Tool & Agent Models

Computer Use (UI automation), Gemini Deep Research / Deep Research Max (autonomous multi-step research), and Antigravity Agent (autonomous complex task completion) are all in preview status.

## Benchmarks

Gemini models perform competitively across evaluation suites:

| Benchmark | Gemini 3.5 Flash | Gemini 3.1 Pro | Notes |
|-----------|-----------------|----------------|-------|
| MMLU-Pro | ~87-89% | ~91% | Among top models globally |
| GPQA Diamond | ~72-76% | ~94% | Pro excels at scientific reasoning |
| SWE-bench Verified | ~75-80% | — | Competitive with leading models |
| LiveCodeBench | ~85-88% | — | Strong competitive programming |
| MMMU | ~75-78% | — | Multimodal understanding |
| ChartQA | ~90%+ | — | Chart interpretation |
| DocVQA | ~94%+ | — | Document understanding |

Google's multimodal benchmarks (MMMU, MathVista, ChartQA, DocVQA) are particularly strong, reflecting Gemini's leadership in cross-modal understanding.

## API Ecosystem

Google provides multiple access paths for developers:

- **Gemini API** — Primary REST API via generativelanguage.googleapis.com
- **Google AI Studio** — Web-based playground for prompt engineering and testing
- **Vertex AI API** — Enterprise-grade access via Google Cloud
- **Grounding API** — Integration with Google Search and Maps for factual grounding
- **Batch API** — Async processing at 50% cost reduction
- **Live API** — Real-time audio-to-audio interactions

Official SDKs are available for Python, Node.js, Go, Java, Dart, and Swift — the widest language support among major providers. Additional integrations include Firebase (mobile apps), Google Workspace Add-ons, Android SDK, LangChain, and LlamaIndex.

Context caching is available in Paid and Enterprise tiers, priced per 1M tokens per hour. Grounding (Google Search integration) offers 5,000 free queries/month for Gemini 3.5 Flash, then $14/1,000 queries. The enterprise tier includes custom security, dedicated support, volume discounts, and Model Garden integration.

## Strengths / Weaknesses

**Strengths:**
- **Google ecosystem integration:** Unmatched access to Search, Workspace, Android, and Chrome
- **TPU infrastructure:** Custom silicon optimized for AI workloads, now sold externally
- **Multimodal leadership:** Leading capabilities across text, image, audio, and video understanding and generation
- **Generative media:** Strong image (Nano Banana, Imagen), video (Veo), and music (Lyria) generation
- **Free tier:** Most generous free tier among major providers
- **Search grounding:** Unique native Google Search integration for factual accuracy
- **Pricing:** Competitive pricing with Flash-Lite models significantly cheaper than competitor equivalents

**Weaknesses:**
- **Fragmented API experience:** Multiple access paths (AI Studio, Vertex AI, Gemini API) create confusion
- **Model proliferation:** Large number of variants makes selection complex
- **Pricing complexity:** Multiple tiers (Standard, Batch, Flex, Priority) with different rates per model
- **Enterprise maturity:** Less mature enterprise offering compared to [[openai]] and [[anthropic]]
- **Brand perception:** Consumer Gemini brand still recovering from early Bard issues

## Key Relationships

- **Google DeepMind** — Parent research organization; Gemini is DeepMind's unified model family
- **Google Cloud** — Enterprise distribution channel via Vertex AI and Model Garden
- **OpenAI** — Primary competitor in closed-source segment; competing on developer ecosystem
- **Anthropic** — Competitor; Google is a major investor in Anthropic while also competing with Gemini
- **Meta** — Competitor in the open-weight space via [[meta-llama]]

## Recent Developments

**Model releases (2025-2026):** Gemini 2.0 (December 2024), Gemini 2.5 family (2025), Gemini 3 family (2025-2026), Gemini 3.5 Flash (May 19, 2026, current production flagship), Gemini 3.1 Pro and Flash-Lite (2026), **Gemini 3.5 Pro (announced for June 2026, reasoning-focused)**, Nano Banana 2 (2026), Veo 3.1 (2026), **Gemma 4 12B** (June 2026, unified encoder-free multimodal open model), **Gemma 4 QAT models** (June 2026, quantization-aware training for mobile/laptop efficiency).

**Strategic initiatives:** Google I/O 2026 — "Welcome to the agentic Gemini era." Gemini app becomes more agentic with proactive, 24/7 help. Gemini Spark and Antigravity Agent announced. TPU sales opened to external customers (April 2026). Gemini Enterprise Agent Platform launched for enterprise agentic workflows on Google Cloud. Gemini for Science: AI experiments and tools for discovery.

**Product integrations:** Gemini integrated into Google Search (AI-powered search features), Google Workspace (Docs, Sheets, Gmail, Slides), Android (on-device and cloud), Chrome (browser features), and Google Maps (AI-enhanced navigation).

**Infrastructure:** Continued TPU development and global data center expansion. Multi-region API endpoint support (global, multi-region, regional) for enterprise compliance requirements.

## Coding Agents Using Google Models

- [[../coding-agents/gemini-cli]] — Google's own coding agent (Gemini 2.5 Pro backend)
- [[../coding-agents/cursor]] — Cursor IDE (supports Gemini models)
- [[../coding-agents/aider]] — Aider (supports Gemini models)

## Agent Frameworks Supporting Google

- [[../agent-frameworks/langchain]] — Full LangChain/LangGraph integration
- [[../agent-frameworks/crewai]] — Supported LLM provider
- [[../agent-frameworks/autogen]] — Supported LLM backend
- [[../agent-frameworks/llamaindex]] — Google completion + embedding support

## Recent API Updates (June 2026)

- **Interactions API** (Beta): New API for interactive workflows with Gemini 2.5 Flash Native Audio
- **Live API**: Improved complex workflow handling for Gemini 2.5 Flash

