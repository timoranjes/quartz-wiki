---
title: OpenAI
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, cloud-platform, model, reasoning, coding, vision, audio, multimodal, agentic, tool-use, pricing, api, closed, token-cost, timeline, controversy]
sources: [raw/articles/llm-provider-openai-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge premium">Premium</span>
    <span class="open-weight-no">Closed weights</span>
    <span class="provider-badge open">🏢 Lab → Platform</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>
    <span class="entity-meta-value">AI Research Lab / Cloud Platform</span>
    <span class="entity-meta-key">HQ</span>
    <span class="entity-meta-value">San Francisco, CA</span>
    <span class="entity-meta-key">Valuation</span>
    <span class="entity-meta-value">$500B+ (2026)</span>
    <span class="entity-meta-key">Employees</span>
    <span class="entity-meta-value">~8,000+</span>
    <span class="entity-meta-key">Key Models</span>
    <span class="entity-meta-value">GPT-5.5, GPT-5.4 family, GPT-oss (12B/20B)</span>
    <span class="entity-meta-key">API</span>
    <span class="entity-meta-value">$5.00 / $30.00 per 1M tokens (GPT-5.5)</span>
  </div>
</div>

# OpenAI

## Overview

OpenAI is a San Francisco-based AI research and deployment company founded in December 2015. Originally established as a non-profit with the mission to ensure artificial general intelligence benefits all of humanity, it transitioned to a capped-profit structure (OpenAI Global LLC) in 2019 while maintaining its non-profit parent (OpenAI Inc.) as the controlling entity. [[microsoft-phi]] investor Microsoft has been the primary backer since 2019, holding approximately 49% profit share.

As of early 2026, OpenAI employs roughly 8,000+ people, generates an estimated $15-16B in annual revenue, and has been valued at over $500B. The company operates the ChatGPT product family (reaching 800M+ users) alongside a comprehensive developer API platform. Strategic initiatives include the $500B+ [[nvidia]]-partnered Stargate data center project and an ongoing transition to a Public Benefit Corporation structure.

## Model Lineup

| Model | ID | Context | Pricing in/out (per 1M) | Type |
|-------|-----|---------|-------------------------|------|
| **GPT-5.5** | `gpt-5.5` | 1M tokens | $5.00 / $30.00 (short) | Flagship, closed |
| **GPT-5.5 Pro** | `gpt-5.5-pro` | 1M tokens | $30.00 / $180.00 | Premium reasoning |
| **GPT-5.4** | `gpt-5.4` | 1M tokens | $2.50 / $15.00 (short) | General-purpose |
| **GPT-5.4 Mini** | `gpt-5.4-mini` | 400K tokens | $0.75 / $4.50 | Latency-optimized |
| **GPT-5.4 Nano** | `gpt-5.4-nano` | 128K tokens | $0.20 / $1.25 | Ultra-lightweight |
| **GPT-oss** (12B/20B) | — | — | Open-weights | Open-weight, free |
| **Sora 2** | `sora-2` | — | $0.10-0.70/sec | Video generation |
| **GPT Image 2** | `gpt-image-2` | — | $5 in / $30 out | Image generation |

## Benchmarks

GPT-5.5 ranks among the top performers across major evaluation suites:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| MMLU-Pro | ~88-90% | Graduate-level knowledge across 57 subjects |
| GPQA Diamond | ~75-80% | Graduate-level science questions |
| HLE (Humanity's Last Exam) | ~40% | Frontier reasoning benchmark |
| SWE-bench Verified | ~78-82% | Real-world GitHub issue resolution |
| LiveCodeBench | ~85-90% | Competitive programming problems |

GPT-5.5 also demonstrates strong performance on agentic benchmarks including BrowseComp, SWE-Lancer, and MLE-bench.

## API Ecosystem

OpenAI provides a comprehensive API portfolio:

- **Responses API** — Unified interface for text, vision, and tool use (recommended)
- **Chat Completions API** — Legacy-compatible, still fully supported
- **Realtime API** — Low-latency audio-to-audio interactions
- **Assistants API** — Agent-building framework with tools and file search
- **Batch API** — Async processing at 50% cost reduction
- **Codex API** — Coding-as-a-service API for autonomous software engineering

Official SDKs are available for Python, Node.js, Go, .NET, and Java. Models are also accessible via Amazon Bedrock and Azure OpenAI Service. The AgentKit framework (launched October 2025) supports building custom AI agents, and the Apps SDK enables third-party app integration within ChatGPT.

Fine-tuning is being deprecated for new users, though existing fine-tuned models remain operational.

## Strengths / Weaknesses

**Strengths:**
- **Model leadership:** GPT-5.5 remains among the most capable models for general reasoning and tool use
- **Ecosystem depth:** Broadest integration across enterprise tools, developer platforms, and consumer products
- **Multimodal range:** Strongest model family covering text, vision, audio, image generation, and video generation
- **Infrastructure:** Massive compute through Stargate partnerships with Nvidia, Oracle, AMD, and others
- **Scale:** ChatGPT is the most widely used AI product globally at 800M+ users
- **Safety investment:** Significant alignment research and safety infrastructure

**Weaknesses:**
- **Premium pricing:** Higher output token costs compared to open-source alternatives and some competitors
- **Closed source:** Limited open-weight offerings (GPT-oss at 12B/20B params only)
- **API dependency:** Rate limits and availability constraints on hosted access
- **Governance uncertainty:** Ongoing for-profit transition creating organizational risk

## Key Relationships

- **Microsoft** — Primary investor and strategic cloud partner since 2019; Azure OpenAI Service integration
- **Nvidia** — 10 GW GPU deployment partnership (September 2025); Stargate infrastructure collaboration
- **Anthropic** — Competitor in premium segment; joint safety evaluation (August 2025)
- **Google Gemini** — Competitor with strong multimodal and ecosystem integration
- **Meta Llama** — Dominant [[meta-llama]] open-source alternative competing on cost

## Recent Developments

**Model releases (2025-2026):** GPT-5 (August 2025), GPT-5.1 (November 2025), GPT-5.2 (December 2025), GPT-5.3 Codex (February 2026), GPT-5.4 family (March 2026), GPT-5.5 (May 2026), GPT-oss open-weights (August 2025).

**Strategic acquisitions:** Promptfoo (March 2026, LLM evaluation), Astral (March 2026, Python tooling), Neptune (December 2025, ML experiment tracking), Software Applications Inc./Sky (October 2025, browser technology leading to ChatGPT Atlas).

**Product launches:** ChatGPT Go lightweight tier (January 2026), ChatGPT Atlas browser (October 2025), Codex standalone coding app (February 2026), ChatGPT Health (January 2026).

**Safety & governance:** Frontier Governance Framework (May 2026), Safety Bug Bounty Program (March 2026), joint safety evaluation with [[anthropic]] (August 2025).

## Coding Agents Using OpenAI Models

- [[../coding-agents/openai-codex]] — OpenAI's own coding agent (gpt-5.3 Codex backend)
- [[../coding-agents/github-copilot]] — GitHub Copilot (uses gpt-4o and o-series models)
- [[../coding-agents/cursor]] — Cursor IDE (supports gpt-4o, o1, o3)
- [[../coding-agents/aider]] — Aider (supports all OpenAI models)
- [[../coding-agents/opencode]] — OpenCode (supports OpenAI via LiteLLM)

## Agent Frameworks Supporting OpenAI

- [[../agent-frameworks/langchain]] — Full LangChain/LangGraph integration
- [[../agent-frameworks/crewai]] — Default LLM provider for CrewAI
- [[../agent-frameworks/autogen]] — Primary LLM backend for AutoGen
- [[../agent-frameworks/llamaindex]] — OpenAI embedding + completion support
