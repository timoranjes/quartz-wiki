---
title: Anthropic
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, model, reasoning, coding, agentic, tool-use, pricing, api, closed, token-cost, timeline, safety, constitutional-ai]
sources: [raw/articles/llm-provider-anthropic-2026.md]
confidence: 0.95
---
# Anthropic

## Overview

Anthropic is an AI safety and research company founded in 2021 by Dario Amodei, Daniela Amodei, and several former [[openai]] researchers. Headquartered in San Francisco, the company was established with a focus on developing safe, reliable, and beneficial AI systems. It is known for its research-first approach to AI development and its emphasis on constitutional AI and model alignment.

As of mid-2026, Anthropic employs ~3,000+ people, generates a $4.7B revenue run rate, and is valued at approximately $96.5B+. Major investors include Google (multi-billion dollar investment), Amazon ($4B total across multiple rounds), Menlo Ventures, Spark Capital, and Zoom. The company's flagship product is the Claude model family, accessible via API and the Claude consumer application.

Anthropic has pursued strategic cloud partnerships across AWS (Claude Platform on AWS), Google Cloud (Vertex AI), and Microsoft Foundry. In May 2026, it announced a multi-billion dollar Microsoft partnership and a $4.5B agreement with SpaceX for AI infrastructure. Notable personnel changes include Andrej Karpathy joining the company (May 2026) and the acquisition of Stainless API framework company.

## Model Lineup

Anthropic maintains a focused three-tier model family:

| Model | API ID | Context | Pricing in/out (per 1M) | Type |
|-------|--------|---------|-------------------------|------|
| **Claude Opus 4.8** | `claude-opus-4-8` | 1M tokens | $5.00 / $25.00 | Flagship, adaptive thinking |
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | 1M tokens | $3.00 / $15.00 | Balanced, extended thinking |
| **Claude Haiku 4.5** | `claude-haiku-4-5` | 200K tokens | $1.00 / $5.00 | Fast, latency-optimized |
| **Claude Mythos** | — | — | Invitation-only | Cybersecurity (Project Glasswing) |

Starting with Claude 4.6, Anthropic uses dateless but pinned model IDs (e.g., `claude-opus-4-8`) rather than date-suffixed versions. The `claude-haiku-4-5` ID is a convenience alias pointing to `claude-haiku-4-5-20251001`.

Opus 4.8 introduces **adaptive thinking** (automatic reasoning depth adjustment) and replaces extended thinking entirely. Sonnet 4.6 supports both extended thinking and adaptive thinking. Haiku 4.5 supports extended thinking but not adaptive thinking.

## Benchmarks

Claude models consistently rank among top performers:

| Benchmark | Claude Opus 4.8 | Notes |
|-----------|-----------------|-------|
| MMLU-Pro | ~88-90% | Among top models globally |
| GPQA Diamond | ~75-80% | Strong scientific reasoning |
| HLE | ~40% | Frontier reasoning benchmark |
| SWE-bench Verified | ~80.8% (Opus 4.6) | Near-parity with best models |
| LiveCodeBench | ~90%+ | Strong competitive programming |

Claude Code (the terminal-based coding assistant) has become one of the most popular AI coding tools, competing directly with [[openai]] Codex, GitHub Copilot, Cursor IDE, and Devin (Cognition).

## API Ecosystem

Anthropic's developer platform centers on several key features:

- **Messages API** — Primary interface for chat completions
- **Batch API** — Async processing at 50% cost discount
- **Tool Use** — Native function calling with structured outputs
- **Extended Thinking** — Configurable reasoning depth for Sonnet and Haiku
- **Adaptive Thinking** — Automatic reasoning adjustment (Opus 4.8, Sonnet 4.6)
- **Computer Use** — Desktop automation via Claude (beta)
- **Memory Tool** — Persistent memory across conversations

Official SDKs are available for Python, TypeScript, Go, and Java. Models are accessible through four cloud platforms:

| Platform | Notes |
|----------|-------|
| Claude API | Direct access at api.anthropic.com |
| AWS Bedrock | Billed via Claude Consumption Units (1 CCU = $0.01) |
| Google Cloud Vertex AI | Global, multi-region, and regional endpoints |
| Microsoft Foundry | Opus 4.8 limited to 200K context on this platform |

Prompt caching is available with 5-minute (1.25x) and 1-hour (2x) write windows, with cache hits at 0.1x base cost. Data residency is available for Opus 4.6+, with US-region inference at 1.1x pricing.

## Strengths / Weaknesses

**Strengths:**
- **Safety-first approach:** Industry-leading investment in AI alignment and constitutional AI methodology
- **Model quality:** Claude Opus 4.8 competes directly with [[openai]] GPT-5.5 on capability benchmarks
- **Honesty and truthfulness:** Specifically trained for reduced hallucination and higher truthfulness
- **Cloud integration:** Deepest cross-platform presence across AWS, GCP, and Microsoft
- **Developer tools:** Claude Code has strong and growing adoption
- **Transparency:** Detailed model cards, system cards, and safety evaluations

**Weaknesses:**
- **Limited model range:** Only three tiers vs. competitors' broader portfolios
- **No image/video generation:** Claude analyzes images but cannot generate them
- **New tokenizer opacity:** Opus 4.7+ uses a tokenizer that may consume up to 35% more tokens for the same text
- **Smaller scale:** Smaller team and compute resources compared to [[openai]] and Google
- **Pricing premium:** Output costs are 5x input across all models

## Key Relationships

- **Google** — Major investor; Vertex AI integration; strategic cloud partnership
- **Amazon** — $4B total investment; Claude Platform on AWS via Marketplace
- **Microsoft** — Multi-billion dollar partnership (May 2026); Microsoft Foundry integration
- **SpaceX** — $4.5B AI infrastructure agreement (May 2026)
- **OpenAI** — Primary competitor; joint safety evaluation conducted August 2025

## Recent Developments

**Model releases (2025-2026):** Claude 4 (May 2025, new architecture), Claude 4.1 Opus, Claude 4.5 series, Claude 4.6 Sonnet (introduced dateless ID format), Claude 4.7 Opus, Claude Opus 4.8 (May 2026, current flagship with adaptive thinking).

**Business milestones:** Hit $4.7B revenue run rate and ~$96.5B+ valuation (May 2026). Andrej Karpathy joined Anthropic. Acquired Stainless API framework company.

**Research:** Containment framework published (May 2026), self-improving agents research, ProgramBench evaluation framework, joint safety evaluation with OpenAI (August 2025).

**Product:** Claude Code at Scale for enterprise deployment, extended output beta (up to 300K tokens via batch API), fast mode research preview for Opus models, Project Glasswing (invitation-only cybersecurity initiative with Claude Mythos).
