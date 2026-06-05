---
title: "LLM Release Tracker"
type: tracking
tags: [llm, models, releases, benchmarks, frontier]
created: "2026-06-04"
updated: "2026-06-05"
status: drafted
---

# LLM Release Tracker

Tracking frontier and notable model launches, benchmark rankings, and capability shifts. Updated as new models ship.

> **Data Sources**: [AI Flash Report Model Timeline](https://aiflashreport.com/model-releases.html), [AI/ML API Top Models 2026](https://aimlapi.com/blog/top-llm-models-in-2026-the-best-ai-models-for-reasoning-coding-multimodal-tasks), [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard)
>
> **Release Cadence**: ~1 model every 3 days (59 models in last 90 days as of June 2026)
> **Last Automated Update**: 2026-06-05

## Latest Releases (Recent)

| Model | Company | Date | Context | License | AA Index | Cost (in/out per 1M tok) |
|-------|---------|------|---------|---------|----------|---------------------------|
| **Claude Opus 4.8** |  | 2026-05-28 | 1M |  |  |  |
| **MiniCPM** |  | 2026-05-28 | 1M |  |  |  |
| **Qwen3.7 Max** |  | 2026-05-25 | 128K |  |  |  |
| **MiniCPM5-1B** | OpenBMB | 2026-05-25 | 128K | Apache-2.0 | 17.9 | Free |
| **Gemini 3.5 Flash** |  | 2026-05-19 | 1M |  |  |  |
| **GPT-5.5** |  | 2026-05-08 | 262K |  |  |  |
| **Mistral** |  | 2026-04-29 | 131K |  |  |  |
| **DeepSeek V4 Pro** |  | 2026-04-24 | 1M |  |  |  |
| **Kimi K2.6** |  | 2026-04-20 | 256K |  |  |  |
| **Llama 4** |  |  |  |  |  |  |

## Top 10 Models by AA Intelligence Index (June 2026)

| Rank | Model | Company | AA Index | Context | License | GPQA | HLE | LiveCodeBench |
|------|-------|---------|----------|---------|---------|------|-----|---------------|
| 1 | **Claude Opus 4.8** | Anthropic | **61.4** | 1M | Proprietary | 92.0% | 45.7% | 61.4% |
| 2 | **GPT-5.5** | OpenAI | **60.2** | 922K | Proprietary | 93.5% | 44.3% | 60.2% |
| 3 | **Qwen3.7 Max** | Alibaba | **56.6** | 1M | Proprietary | 92.3% | 38.1% | 56.6% |
| 4 | **Claude Opus 4.7** | Anthropic | **57.3** | 1M | Proprietary | 91.4% | 39.6% | 57.3% |
| 5 | **Kimi K2.6** | Moonshot/Kimi | **53.9** | 256K | Modified MIT | 91.1% | 35.9% | 53.9% |
| 6 | **GPT-5.4** | OpenAI | **56.8** | 1M | Proprietary | 92.0% | 41.6% | 56.8% |
| 7 | **Gemini 3.1 Pro** | Google | **57.2** | 1M | Proprietary | 94.1% | 44.7% | 57.2% |
| 8 | **MiMo-V2.5-Pro** | Xiaomi | **53.8** | 1M | MIT | 86.6% | 33.8% | 53.8% |
| 9 | **Grok 4.3** | xAI | **53.2** | 1M | Proprietary | 90.1% | 35.0% | 53.2% |
| 10 | **DeepSeek V4 Pro** | DeepSeek | **51.5** | 1M | MIT | 88.8% | 35.9% | 51.5% |

## Frontier Model Profiles

### Claude Opus 4.8 (Anthropic, May 2026)
- **AA Index**: 61.4 — current #1
- **Strengths**: SOTA reasoning (GPQA 92%), coding (SWE-Bench Verified 87.6%), 1M context
- **Pricing**: $6.25 input / $25.00 output per 1M tokens
- **Best For**: Code review, repository reasoning, complex analysis

### GPT-5.5 (OpenAI, April 2026)
- **AA Index**: 60.2 — current #2
- **Strengths**: Best agentic execution breadth, 922K context, largest tool ecosystem
- **Weaknesses**: Highest output price ($30/M)
- **Best For**: General-purpose frontier, multimodal workflows, computer use

### Qwen3.7 Max (Alibaba, May 2026)
- **AA Index**: 56.6 — #3, top Chinese model
- **Strengths**: GPQA 92.3% (beats GPT-5.5), 1M context, multilingual
- **Pricing**: $2.50 / $7.50 — aggressive frontier pricing
- **Best For**: Agentic coding, Chinese/English bilingual, cost-sensitive frontier

### Gemini 3.5 Flash (Google, May 2026)
- **AA Index**: 55.3
- **Strengths**: 289 tokens/sec (4× faster than peers), MCP Atlas 83.6%, native multimodal
- **Pricing**: $1.50 / $9.00 — most competitive frontier pricing
- **Best For**: Speed-critical agents, cost-sensitive multimodal, tool-use-heavy workflows

### DeepSeek V4 Pro (DeepSeek, April 2026)
- **AA Index**: 51.5
- **Strengths**: MIT open-weight, $0.435 / $0.87 pricing, 92.5% HumanEval
- **Best For**: Self-hosted frontier, coding at lowest cost, agentic tasks

## Key Trends (2026)

### 1. Open-Weight Dominance in Mid-Tier
- DeepSeek V4 Flash/Pro, Qwen3.6 series, Granite 4.1, Gemma 4, MiniCPM all open-source
- Cost: $0.00–$0.30 input vs. $2.50–$30+ for proprietary APIs

### 2. 1M+ Token Context Standard
| Model | Context |
|-------|---------|
| Kimi K2 | 2M |
| Grok 4.20 v2 | 2M |
| Gemini 3.1 Pro | 2M |
| Llama 4 Scout | 10M |
| Claude Opus 4.6–4.8 | 1M |
| GPT-5.5 | 922K |

### 3. Multimodal Is Now Standard
- Text + image + audio + video: Gemini 3.5 Flash, Qwen3.7 Max, Kimi K2.6, GPT-5.5, Grok 4.3
- Text + image + PDF: GPT-5.4 mini, Claude Sonnet 4.6, Gemini 3.1 Flash-Lite

### 4. Coding Specialization
- **Claude Opus 4.5**: 80.9% SWE-bench Verified (first >80%)
- **GPT-5.3 Codex**: SOTA on SWE-Bench Pro, 1,000+ tok/s
- **Agent Teams**: Claude Sonnet 4.6 orchestrates 2–16 Claude instances in parallel

### 5. Pricing Collapse
- Frontier reasoning now accessible to startups
- DeepSeek V4 Pro delivers ~90% of GPT-5.4 at 1/50th the price
- Gemini 3.1 Flash Lite: 1M tokens at $0.25 per million

## Benchmark Evolution

| Old Metric | Status | Replacement |
|------------|--------|-------------|
| MMLU | **Obsolete** — memorization-based | GPQA Diamond (expert reasoning) |
| HumanEval | **Weakened** — model contamination | LiveCodeBench (live coding challenges) |
| Simple QA | **Irrelevant** | Humanity's Last Exam (HLE) |
| Synthetic benchmarks | **Declining** | Terminal-Bench, SWE-Bench Pro |

## Agent Framework Compatibility

| Model | LangGraph | CrewAI | AutoGen | smolagents | OpenAI SDK | Semantic Kernel |
|-------|-----------|--------|---------|------------|------------|-----------------|
| GPT-5.5 | Yes | Yes | Yes | Yes | Native | Yes |
| Claude Opus 4.8 | Yes | Yes | Yes | Yes | Limited | Yes |
| Qwen3.7 Max | Yes | Yes | Yes | Yes | Limited | Yes |
| Gemini 3.5 Flash | Yes | Yes | Yes | Yes | Limited | Via OpenAI-compatible |
| DeepSeek V4 Pro | Yes | Yes | Yes | Yes | Limited | Via OpenAI-compatible |
| Llama 4 Scout | Yes | Yes | Yes | Yes | Limited | Via OpenAI-compatible |

## Sources

- [AI Flash Report: Model Release Timeline](https://aiflashreport.com/model-releases.html)
- [AI/ML API: Top LLM Models in 2026](https://aimlapi.com/blog/top-llm-models-in-2026-the-best-ai-models-for-reasoning-coding-multimodal-tasks)
- [Vellum: LLM Leaderboard 2026](https://www.vellum.ai/llm-leaderboard)
- [LLM Gateway: Model Timeline](https://llmgateway.io/timeline)
