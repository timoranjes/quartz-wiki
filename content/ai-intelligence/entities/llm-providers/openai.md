---
title: OpenAI
created: 2026-06-02
updated: 2026-06-14
type: provider
tags: [provider, lab, cloud-platform, model, reasoning, coding, vision, audio, multimodal, agentic, tool-use, pricing, api, closed, token-cost, timeline, controversy]
sources: [raw/articles/llm-provider-openai-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge premium">Premium</span>
    <span class="provider-badge us">🇺🇸 San Francisco, CA</span>
  </div>
  <div class="entity-meta">
    <div><span class="entity-meta-key">Latest Model</span><span class="entity-meta-value">GPT-5.5</span></div>
    <div><span class="entity-meta-key">Valuation</span><span class="entity-meta-value">$500B+</span></div>
    <div><span class="entity-meta-key">Revenue</span><span class="entity-meta-value">$30B+</span></div>
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

**Model releases (2025-2026):** GPT-5 (August 2025), GPT-5.1 (November 2025), GPT-5.2 (December 2025), GPT-5.3 Codex (February 2026), GPT-5.4 family (March 2026), GPT-5.5 (May 2026), GPT-oss open-weights (August 2025). **GPT-Realtime-2** (May 2026): First voice model with GPT-5-class reasoning, available via WebRTC API for low-latency audio-to-audio interactions. Sep 30, 2024 knowledge cutoff. Not yet available in ChatGPT iPhone app as of June 2026.

**Strategic acquisitions:** Promptfoo (March 2026, LLM evaluation), Astral (March 2026, Python tooling), Neptune (December 2025, ML experiment tracking), Software Applications Inc./Sky (October 2025, browser technology leading to ChatGPT Atlas), **Ona (announced June 11, 2026)** — to expand Codex with secure, persistent cloud environments for long-running AI agents across enterprise workflows.

**Product launches:** ChatGPT Go lightweight tier (January 2026), ChatGPT Atlas browser (October 2025), Codex standalone coding app (February 2026), ChatGPT Health (January 2026).

**Safety & governance:** Frontier Governance Framework (May 2026), Safety Bug Bounty Program (March 2026), joint safety evaluation with [[anthropic]] (August 2025).

**Enterprise & partnerships (May-June 2026):** Dell Technologies partnership (May 18, 2026) to bring Codex to hybrid and on-premises enterprise environments. Named a Leader in enterprise coding agents by Gartner (May 22, 2026). Self-improving tax agents built with Codex (May 27, 2026). Personal finance experience in ChatGPT (May 15, 2026). Rosalind Biodefense initiative for societal resilience (May 29, 2026). **Oracle Cloud partnership (June 10, 2026)**: access OpenAI models and Codex through existing Oracle Cloud commitments with enterprise security and governance.

**Corporate & governance (June 2026):** Confidential S-1 filing submitted to the SEC (June 8, 2026), marking OpenAI's first formal step toward an IPO — timing not yet determined. Public Benefit Corporation transition ongoing. Published "Built to Benefit Everyone" plan outlining vision for AGI access, safety, and shared prosperity (June 8, 2026). Launched OpenAI Economic Research Exchange to study AI's impact on jobs, productivity, and economy (June 8, 2026).

**Research milestones:** An OpenAI model disproved a central conjecture in discrete geometry (May 20, 2026). Content provenance advancement for AI ecosystem transparency (May 19, 2026). Trustworthy third-party evaluation frameworks (May 29, 2026).

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

## Security & Safety (June 2026)

- **Lockdown Mode**: New feature to prevent data exfiltration from prompt injection attacks in ChatGPT. Limits outbound network requests using deterministic mechanisms. Rolling out to eligible personal accounts and ChatGPT Business. See [[../agent-patterns/agent-safety]] for details.

