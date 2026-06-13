title: Moonshot AI
tags: provider, lab, china, model, reasoning, coding, open-weight, long-context, multimodal, agentic, pricing, api, token-cost, timeline
# Moonshot AI

## Overview

Moonshot AI (月之暗面) is a Beijing-based AI startup founded in March 2023 by Yang Zhilin and Tsinghua University classmates. The company is a member of China's **"Six AI Tigers"** and has raised $1B+ total funding from Alibaba, Tencent, Meituan, and HongShan at valuations reaching $3B. Moonshot AI is best known for the **Kimi** chatbot and the **Kimi K2** series — a 1T-parameter MoE model with only 32B active parameters, released under a modified MIT license. Fellow AI Tigers include [[zhipu-ai]] (Beijing), [[minimax]] (Shanghai), and [[deepseek]] (Hangzhou).

## Model Lineup

| Model | Release | Total Params | Active Params | Context | License | Notes |
|-------|---------|-------------|--------------|---------|---------|-------|
| **Kimi K2.6** | Apr 2026 | 1T | 32B | 262K tokens | Modified MIT | Agent Swarm v2 (300 agents), auto context compression |
| **Kimi K2.5** | Jan 2026 | 1T | 32B | 256K tokens | Modified MIT | Multimodal (MoonViT), Agent Swarm v1 |
| **Kimi K2 Thinking** | Nov 2025 | 1T | 32B | 256K tokens | Modified MIT | Reasoning traces, outperforms GPT-5 and Claude Sonnet 4.5 |
| **Kimi K2** | Jul 2025 | 1T | 32B | 128K tokens | Modified MIT | Open-source breakthrough; #1 Hugging Face download on release day |
| **Kimi K1.5** | Jan 2025 | — | — | — | Proprietary | Matches OpenAI o1 in math/coding/reasoning |

**Architecture:** MoE with 384 experts, 8 activated per token, Multi-Head Latent Attention (MLA), SwiGLU activation, MuonClip-stabilized training on 15.5T tokens.

**Key innovations:** Muon optimizer (2× faster than AdamW for MoE training); MoonViT native multimodal encoder (400M params); INT4 quantization-aware training (2× inference speedup, no accuracy loss).

## Benchmarks

| Benchmark | Kimi K2.5 | Claude Opus 4.5 | GPT-5.2 | Notes |
|-----------|-----------|------------------|---------|-------|
| SWE-Bench Verified | 76.8% | 80.9% | 80.0% | Real GitHub issues |
| SWE-Bench Multilingual | 73.0% | — | — | Non-English codebases |
| AIME 2025 | 96.1% | 93% | 100% | Math competition |
| GPQA-Diamond | 87.6% | — | — | Graduate-level QA |
| MMMU Pro | 78.5% | — | — | Academic multimodal |
| MathVision | 84.2% | — | — | Diagrams and geometry |
| Terminal-Bench 2.0 | 66.7% | — | — | K2.6 only |
| SWE-Bench Pro | 58.6% | — | — | K2.6, harder subset |
| BrowseComp (swarm) | 78.4% | — | — | Agent Swarm mode |

**Agent Swarm:** Coordinates up to 300 parallel agents (4,000+ steps, 12-hour tasks), achieving 4.5× speedup on parallelizable tasks vs. sequential execution.

## API Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Context |
|-------|---------------------|----------------------|---------|
| Kimi K2.5 | $0.60 | $2.50 | 256K |
| Kimi K2.6 | $0.60 | $2.50 | 262K |
| Kimi K2 Thinking | $0.60 | $2.50 | 256K |

Kimi K2.5 is **76% cheaper** than Claude Opus 4.5 on benchmark tasks ($0.27 vs $1.14 per benchmark suite). Consumer plans start at ¥5.2 for 4 days or ¥399/year.

## API Ecosystem

Moonshot AI provides an OpenAI-compatible API at `https://api.moonshot.cn/v1` with four operational modes: **Instant** (fast, no reasoning traces), **Thinking** (step-by-step reasoning), **Agent** (up to 300 tool calls), and **Agent Swarm** (100+ parallel agents). The Mooncake serving infrastructure processes 100B tokens/day and won the Erik Riedel Best Paper Award at USENIX FAST 2025. Models are available on Hugging Face, OpenRouter, and via vLLM/SGLang for self-hosting.

## Strengths / Weaknesses

**Strengths:**
- **Open-weight leadership:** Kimi K2 series under modified MIT enables broad adoption; #1 Hugging Face download on release day
- **Agent Swarm:** Up to 300 parallel agents is a unique differentiator vs. single-agent tool calling
- **Cost efficiency:** 76% cheaper than comparable Western models
- **Research contributions:** Muon optimizer (2× faster than AdamW), RL scaling paper, Mooncake architecture (USENIX award)
- **Rapid iteration:** 2-3 month major release cadence; K2→K2.6 in 9 months
- **Multimodal native:** MoonViT encoder trained end-to-end, not bolted-on
- **Long context:** 262K token context window with automatic compression

**Weaknesses:**
- **Geographic focus:** Primarily China-focused, limited international presence
- **Brand recognition:** Less known outside China compared to [[openai]] and [[anthropic]]
- **License restrictions:** Modified MIT requires attribution for >100M MAU or >$20M monthly revenue products
- **Hardware requirements:** INT4 self-hosting still needs ~256GB GPU memory (8× H100)
- **Ecosystem maturity:** Smaller third-party tool ecosystem than established providers

## Key Relationships

- **Alibaba, Tencent, Meituan** — Major investors from $300M round (Oct 2023)
- **HongShan** — Early and continuing investor across multiple rounds
- **UCLA** — Joint research on Muon optimizer
- **Hugging Face** — Primary open-weight distribution platform
- **OpenRouter, litellm** — Third-party API access
- **CodeBuddy, Vercel, Factory.ai** — Enterprise integration partners reporting 12-50% performance gains with K2.6

## Recent Developments

**Model releases:** Kimi K2 (Jul 2025, open-source 1T MoE), K2-Instruct-0905 (Sep 2025, 256K context), K2 Thinking (Nov 2025, reasoning traces), K2.5 (Jan 2026, multimodal + Agent Swarm), K2.6 (Apr 2026, 300 agents, auto compression).

**Research publications:** "Muon is Scalable for LLM Training" (arXiv:2502.16982); "Kimi k1.5: Scaling Reinforcement Learning with LLMs" (arXiv:2501.12599); Mooncake architecture (USENIX FAST 2025 Best Paper).

**K3 anticipation:** Based on 2-3 month cadence, K3 expected mid-to-late 2026.