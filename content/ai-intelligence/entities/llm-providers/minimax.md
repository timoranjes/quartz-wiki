---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge low-cost">Low Cost</span>
    <span class="provider-badge cn">🇨🇳 Shanghai</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge reasoning"><span class="cap-icon">🧠</span> Reasoning</span>
    <span class="capability-badge coding"><span class="cap-icon">💻</span> Coding</span>
    <span class="capability-badge multimodal"><span class="cap-icon">🔀</span> Multimodal</span>
    <span class="capability-badge audio"><span class="cap-icon">🎙️</span> Audio</span>
  </div>
</div>

title: MiniMax
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, model, reasoning, coding, agentic, tool-use, pricing, api, open-weight, token-cost, timeline, china, multimodal]
sources: [raw/articles/llm-provider-minimax-2026.md]
confidence: 0.95
---
# MiniMax

## Overview

MiniMax Group (Chinese: 稀宇科技, *Xīyǔ Kējì*) is a Shanghai-based AI company founded in December 2021 by former [[zhipu-ai]] peer SenseTime researchers Yan Junjie (CEO), Yang Bin, and Zhou Yucong. Classified among China's "AI Tigers" alongside [[cohere]] peer [[deepseek]] and [[moonshot-ai]] (Kimi), MiniMax has built a multimodal AI platform spanning text, audio, image, video, and music generation. The company completed a landmark Hong Kong Stock Exchange IPO in January 2026, raising ~HK$4.8B (~$619M), with shares surging over 400% post-listing. Yan Junjie's net worth is estimated at $3.2B.

As of mid-2026, MiniMax operates at minimax.io with 200M+ global users across consumer products (Talkie, Xing Ye, Hailuo AI) and an API platform. The flagship M-series models (M2 through M3.0) feature Mixture-of-Experts architecture with ~10B activated parameters, up to 1M token context windows, and industry-leading cost efficiency — priced at a fraction of Western alternatives like Claude and [[openai]] GPT-5.

## Model Lineup

| Model | Release | Context | Pricing in/out (per 1M) | Type |
|-------|---------|---------|-------------------------|------|
| **M3.0** | Jun 2026 | 1M tokens | Higher than M2 series | Flagship, multimodal |
| **M2.7** | Mar 2026 | 205K tokens | $0.26 / $1.20 | Self-evolving, open-weight |
| **M2.5** | Feb 2026 | 197K tokens | $0.15 / $1.15 | Cost-optimized |
| **M2.1** | Dec 2025 | 197K tokens | $0.29 / $0.95 | MMLU: 87.5, GPQA: 83.0 |
| **M2** | Oct 2025 | 197K tokens | $0.26 / $1.00 | Open-weight, MoE ~10B active |
| **MiniMax-01** | Jan 2025 | 1M tokens | $0.20 / $1.10 | Multimodal, large context |

M2.7 features a revolutionary self-evolving architecture where the model participates in its own training loop (100+ optimization cycles, 30-50% RL automation). Both M2.7 Standard and M2.7-highspeed produce identical results with different throughput.

## Benchmarks

| Benchmark | M2.7 | Notes |
|-----------|------|-------|
| SWE-bench Verified | **78%** | +23% over Claude Opus 4.6 (55%) |
| SWE-Pro | 56.22% | Tied with Opus ~57% |
| GPQA Diamond | 87.4% | Scientific reasoning |
| VIBE-Pro | 55.6% | End-to-end delivery |
| TerminalBench 2 | 57.0% | Agentic terminal tasks |
| τ²-Bench | 84.8% | Conversational agent |
| MLE-Bench Lite | 66.6% | Tied with Gemini 3.1 |
| IFBench | 75.7% | Instruction following |
| GDPval-AA (Office) | ELO 1495 | Highest among open-source |

Artificial Analysis Intelligence Index: Intelligence 49.6 (#20/371), Coding 41.9 (#34/308), Agentic 62.1 (#50/283).

## API Ecosystem

- **API Platform:** platform.minimax.io for direct access
- **OpenRouter:** 9 MiniMax models available (M3, Hailuo 2.3, M2.7, etc.)
- **Multiple Providers:** Morph, Fireworks, Together, Novita, SambaNova, Mara, WaveSpeedAI
- **Hugging Face:** Open weights for self-hosting (M2, M2.5, M2.7)
- **Cross-Harness Compatible:** Claude Code, Cursor, Cline, Codex CLI, Roo Code, Kilo Code, OpenCode, and more

Cache optimization reduces effective costs to as low as $0.06/M tokens with high cache utilization. Blended rate at typical 7:2:1 ratio is $0.22/M tokens. M2.5 claims "one hour of continuous operation costs just one dollar."

## Strengths / Weaknesses

**Strengths:**
- **Cost leadership:** Among cheapest frontier-level models (M2.5 at $0.15/M input), 50x cheaper than Claude Opus
- **Self-evolving architecture:** M2.7 pioneered model self-optimization in training loops
- **Strong coding performance:** 78% SWE-bench Verified, outperforming Opus by 23 points
- **Native agentic design:** 62.1 agentic index, purpose-built for multi-agent workflows
- **Open weights:** M2, M2.5, M2.7 available on Hugging Face
- **Rapid cadence:** 4 model releases in 9 months (Oct 2025 – Jun 2026)
- **HKEX-listed:** Public company with Shanghai STAR Market dual-listing plans

**Weaknesses:**
- **High output costs:** $1.20/M output is expensive relative to input pricing
- **Legal controversies:** Copyright lawsuit (Disney, Universal, Warner Bros.) and Anthropic data-harvesting accusation (Feb 2026)
- **Financial losses:** Reported $250M net loss on $79M revenue in 2025
- **Limited Western adoption:** Less ecosystem maturity vs. OpenAI/Anthropic
- **State capital backing:** May raise data sovereignty concerns for some enterprises
- **English fluency:** Occasional ESL patterns in generated text

## Key Relationships

- **Alibaba Group** — Led $600M funding round, significant strategic investor
- **Tencent** — Early backer, distribution partnership
- **MiHoYo** — Early investor, gaming and character AI partnership
- **Shanghai STVC Group** — State-owned capital, led Series B extension ($300M at ~$4B)
- **HongShan / IDG / Hillhouse** — Participated in major funding rounds

## Recent Developments

**M3.0 release (June 2026):** Frontier coding model with 1M context and native multimodality, higher API pricing than M2 series.

**M2.7 launch (March 2026):** Revolutionary self-evolving architecture, 100+ self-optimization cycles, competitive benchmarks against frontier models, open-weight release on Hugging Face.

**Shanghai listing plans (June 2026):** Preparing for STAR Market dual listing alongside [[zhipu-ai]], per Caixin Global.

**Data harvesting accusation (February 2026):** Anthropic accused MiniMax of using fraudulent accounts to distill Claude training data (16M+ interactions).

**HKEX IPO (January 2026):** Raised HK$4.8B, shares opened at 42.67% premium, surged 400%+ post-listing.
