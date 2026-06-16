---
title: Anthropic
created: 2026-06-02
updated: 2026-06-17
type: provider
tags: [provider, lab, model, reasoning, coding, agentic, tool-use, pricing, api, closed, token-cost, timeline, safety, constitutional-ai]
sources: [raw/articles/llm-provider-anthropic-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge premium">S-1 Filing</span>
    <span class="provider-badge us">🇺🇸 San Francisco, CA</span>
  </div>
  <div class="entity-meta">
    <div><span class="entity-meta-key">Flagship Models</span><span class="entity-meta-value">Opus 4.5 / Sonnet 4.5</span></div>
    <div><span class="entity-meta-key">Revenue</span><span class="entity-meta-value">$7.3B (2025)</span></div>
    <div><span class="entity-meta-key">Status</span><span class="entity-meta-value">S-1 Filed</span></div>
  </div>
</div>

# Anthropic

## Overview

Anthropic is an AI safety and research company founded in 2021 by Dario Amodei, Daniela Amodei, and several former [[openai]] researchers. Headquartered in San Francisco, the company was established with a focus on developing safe, reliable, and beneficial AI systems. It is known for its research-first approach to AI development and its emphasis on constitutional AI and model alignment.

As of mid-2026, Anthropic employs ~3,000+ people, generates a $4.7B revenue run rate, and is valued at approximately $96.5B+. Major investors include Google (multi-billion dollar investment), Amazon ($4B total across multiple rounds), Menlo Ventures, Spark Capital, and Zoom. The company's flagship product is the Claude model family, accessible via API and the Claude consumer application.

Anthropic has pursued strategic cloud partnerships across AWS (Claude Platform on AWS), Google Cloud (Vertex AI), and Microsoft Foundry. In May 2026, it announced a multi-billion dollar Microsoft partnership and a $4.5B agreement with SpaceX for AI infrastructure. Notable personnel changes include Andrej Karpathy joining the company (May 2026) and the acquisition of Stainless API framework company.

## Model Lineup

Anthropic maintains a focused three-tier model family:

| Model | API ID | Context | Pricing in/out (per 1M) | Type |
|-------|--------|---------|-------------------------|------|
| **Claude Fable 5** | `claude-fable-5` | 1M tokens | $10.00 / $50.00 | **SUSPENDED** (June 12, 2026 — US govt export control directive) |
| **Claude Mythos 5** | `claude-mythos-5` | 1M tokens | $10.00 / $50.00 | **SUSPENDED** (June 12, 2026 — US govt export control directive) |
| **Claude Opus 4.8** | `claude-opus-4-8` | 1M tokens | $5.00 / $25.00 | Previous flagship, adaptive thinking |
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

**Model releases (2025-2026):** Claude 4 (May 2025, new architecture), Claude 4.1 Opus, Claude 4.5 series, Claude 4.6 Sonnet (introduced dateless ID format), Claude 4.7 Opus, **Claude Opus 4.8 (May 28, 2026)** — adaptive thinking, SOTA reasoning (GPQA 92%), coding (SWE-bench Verified 87.6%), 1M context, AA Intelligence Index 61.4 (#1). **Claude Fable 5 + Mythos 5 (June 9, 2026)** — new frontier models, 1M context, 128K max output, Jan 2026 knowledge cutoff. Fable 5 has strict guardrails; Mythos 5 shares capabilities without safety classifiers. Priced at 2× Opus 4.8 ($10/$50 per 1M tokens). Available on Claude.ai, Claude Code for web, Claude Code CLI, and Claude Cowork. On subscription plans until June 22, 2026, then billed extra. Demonstrated "big model" knowledge depth and strong coding ability — built LLM 0.32a3 (Datasette Agent human-in-the-loop features) almost entirely via Claude Code in one day. ^[raw/sources/2026-06-09-initial-impressions-of-claude-fable-5.md]

**Business milestones:**
- **$65B Series H (May 28, 2026)**: Raised at $965B post-money valuation
- **S-1 filing (June 1, 2026)**: Confidentially submitted draft S-1 to SEC — IPO preparation underway
- Hit $4.7B revenue run rate and ~3,000+ employees
- Andrej Karpathy joined Anthropic; acquired Stainless API framework company
- **Milan office (May 27, 2026)**: Opened to support Italian enterprise, research, and developers
- **Korea office (May 26, 2026)**: KiYoung Choi appointed as Representative Director

**Research:** Containment framework published (May 2026), self-improving agents research, ProgramBench evaluation framework, joint safety evaluation with OpenAI (August 2025).

**Product:** Claude Code at Scale for enterprise deployment, extended output beta (up to 300K tokens via batch API), fast mode research preview for Opus models, Project Glasswing (cybersecurity initiative expanded June 2, 2026 with 12 partners), **Claude Partner Network (June 3, 2026)**: New Services Track and Partner Hub launched.

**AI-enabled cyber threats mapping (June 3, 2026)**: Published findings from mapping a year's worth of AI-enabled cyber threats using MITRE ATT&CK framework.

**Fable 5 safeguards controversy (June 9-11, 2026):** The 319-page Fable 5/Mythos 5 system card revealed invisible safeguards that silently limited model effectiveness for "frontier LLM development" requests (pretraining pipelines, distributed training, ML accelerator design) via prompt modification, steering vectors, and PEFT — estimated ~0.03% of traffic, <0.1% of organizations. Unlike cybersecurity/biology refusals, these were invisible: no fallback model, no user notification. Widespread backlash from the research community (notably Jeremy Howard) over "sabotaging" competitors. Anthropic walked back the policy within 48 hours: flagged requests now visibly fall back to Opus 4.8, API returns refusal reasons. See [[../agent-patterns/agent-safety]] for details. ^[raw/sources/2026-06-10-if-claude-fable-stops-helping-you-youll-never-know.md] ^[raw/sources/2026-06-11-anthropic-walks-back-policy-that-could-have-sabotaged-ai-researchers-using-claud.md] ^[raw/sources/2026-06-10-quoting-jeremy-howard.md]

**US Government Export Control Directive — Fable 5 / Mythos 5 Suspended (June 12, 2026):** The US government issued an export control directive citing national security authorities, ordering suspension of ALL access to Fable 5 and Mythos 5 by any foreign national — whether inside or outside the United States, including foreign national Anthropic employees. Net effect: Fable 5 and Mythos 5 disabled for ALL customers globally. Other Anthropic models (Opus 4.8, Sonnet 4.6, Haiku 4.5) unaffected. Anthropic received the directive at 5:21pm ET on June 12; access was cut at 6:59pm PT (9:59pm ET). The government's stated concern: awareness of a method to bypass/jailbreak Fable 5. Anthropic's response: the alleged "jailbreak" consists of asking the model to read a codebase and fix software flaws — a capability widely available from other models including [[openai]] GPT-5.5, used daily by security defenders. API returns 404 with message: "Claude Fable 5 is not available. Please use Opus 4.8." First known instance of a US export control directive forcing a major lab to globally disable a frontier model. See [[../agent-patterns/agent-safety]] for governance implications. ^[raw/sources/2026-06-13-statement-on-the-us-government-directive-to-suspend-access-to-fable-5-and-mythos.md]

**Behind-the-scenes (June 15, 2026):** Axios reported personality clashes between Anthropic and the White House contributed to the standoff. Key Anthropic personnel meeting Commerce Department in DC: **Logan Graham** (Frontier Red Team lead; ex-Special Adviser to PM Boris Johnson), **Dave Orr** (Head of Safeguards; ex-Google DeepMind), **Nicholas Carlini** (AI safety researcher). Anthropic's **Constitutional Classifiers** (January 2026) remain their primary defense — no "universal jailbreak" found against Mythos; the triggering technique classified as "a potential narrow, non-universal jailbreak." Administration suggests resolution may require an "attitude fix" rather than technical solution. ^[raw/sources/2026-06-15-they-screwed-us-personality-clashes-sent-anthropics-models-offline.md]

**"Jailbreak" was standard cyberdefense (June 16, 2026):** **Kate Moussouris** (CEO, Luta Security) confirmed via The Atlantic that the "jailbreak" was simply asking Fable to "fix this code" after it refused "review the code for security issues." The model produced fixes for known CVEs and planted vulnerabilities through a multi-step process, then researchers turned output into test scripts. Moussouris: "That is not a guardrail bypass. It is the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day." The capability "cannot be removed without making the model worse at fixing bugs and verifying patches." ^[raw/sources/2026-06-16-the-fable-5-export-controls-harm-us-cyber-defense.md] ^[raw/sources/2026-06-16-quoting-matteo-wong-the-atlantic.md]

## Coding Agents Using Anthropic Models

- [[../coding-agents/claude-code]] — Anthropic's own coding agent (Claude Sonnet 4 / Opus 4 backend)
- [[../coding-agents/cursor]] — Cursor IDE (supports Claude Sonnet, Opus)
- [[../coding-agents/aider]] — Aider (supports Claude models)
- [[../coding-agents/opencode]] — OpenCode (supports Anthropic via LiteLLM)

## Agent Frameworks Supporting Anthropic

- [[../agent-frameworks/langchain]] — Full LangChain/LangGraph integration
- [[../agent-frameworks/crewai]] — Supported LLM provider
- [[../agent-frameworks/autogen]] — Supported LLM backend
- [[../agent-frameworks/llamaindex]] — Anthropic completion support
