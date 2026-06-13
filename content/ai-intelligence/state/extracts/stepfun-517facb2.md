title: StepFun
tags: provider, lab, china, model, multimodal, reasoning, coding, open-weight, pricing, api, token-cost, timeline, agentic
# StepFun

## Overview

StepFun (阶跃星辰) is a Shanghai-based AI startup founded in April 2023 by Jiang Daxin, former Chief Scientist of Microsoft Software Technology Center Asia. The company specializes in **multimodal AI foundation models** capable of processing text, audio, image, and video. StepFun is a member of China's **"Six AI Tigers"** and achieved unicorn status in December 2024 at a $2B valuation, having raised $718M+ total. The current flagship is the Step-3.7-Flash MoE model (May 2026), a 198B-parameter vision-language model with ~11B active parameters that competes with models 5-10× larger. [[minimax]] and [[zhipu-ai]] are fellow AI Tigers headquartered in Shanghai and Beijing respectively.

StepFun is planning a Hong Kong IPO targeting a $10B valuation and began unwinding its offshore VIE structure in April 2026.

## Model Lineup

| Model | Total Params | Active Params | Context | License | Notes |
|-------|-------------|--------------|---------|---------|-------|
| **Step-3.7-Flash** | 198B (196B + 1.8B ViT) | ~11B | 256K tokens | Apache 2.0 | Flagship MoE VLM, 3 reasoning depths, Advisor Mode |
| **Step-3.5-Flash** | 196B | 11B | 262K tokens | Apache 2.0 | Breakthrough MoE, Feb 2026 |
| **Step-1** | 1T | — | — | Open-weight | First Chinese 1T model release |

**Architecture philosophy ("Small Sparse"):** StepFun's MoE approach uses only 11B active parameters per token, enabling single H100 serving with strong math/coding performance despite small total footprint.

## Benchmarks

Step-3.7-Flash with Advisor Mode reaches 97% of [[anthropic]] Claude Opus 4.6 on SWE-bench at 1/9 the cost:

| Benchmark | Step 3.7 Flash + Advisor | Claude Opus 4.6 | Notes |
|-----------|--------------------------|------------------|-------|
| SWE-Bench | 76.3% | 78.7% | Near-parity at fraction of cost |
| SWE-Bench Pro | 56.26% | — | Harder subset |
| Terminal-Bench 2.1 | 59.55% | — | Terminal command execution |
| BrowseComp | 75.82% | 79.30% | Web browsing comprehension |
| ResearchRubrics | 71.68% | — | Above GPT-5.5 (61.50%) |
| DeepSearchQA (F1) | 92.82% | — | Above Kimi K2.6 (92.50%) |
| Android Daily | 61.87% | — | Long-horizon UI tasks |

**Step-3.5-Flash vs larger models:** Outscores [[deepseek]] V3.2 (671B) and Kimi K2.5 (1T) on SWE-bench (74.4%), AIME 2025 (97.3), and LiveCodeBench-V6 (86.4%) despite being 3-5× smaller in total parameters.

## API Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|---------------------|----------------------|
| Step-3.7-Flash | $0.08–$0.10 | $0.25–$0.30 |
| Step-3.5-Flash | $0.10 | $0.30 |

At these rates, a $1,000/mo GPT-4o workload costs ~$40/mo — **25× cheaper**. Cheapest model tier starts at ¥3/MTok (~$0.42).

## API Ecosystem

StepFun provides a REST API compatible with OpenAI's format at `https://platform.stepfun.com/v1`. Models are also available via OpenRouter. The API supports chat completions, multimodal inputs, and the Step-3.7-Flash's three reasoning depth modes (Low, Medium, High). 11+ models are hosted on Hugging Face.

## Strengths / Weaknesses

**Strengths:**
- **Cost efficiency:** 25× cheaper than GPT-4o, among the cheapest frontier models
- **Small Sparse architecture:** 11B active params deliver top-tier math/coding performance
- **Agent-first design:** Models optimized for agentic workflows; Advisor Mode achieves near-Claude performance at 1/9 cost
- **Open-source:** Apache 2.0 licensing for flagship models; 11+ models on Hugging Face
- **Multimodal capability:** Native video, audio, image, and text processing
- **Cross-scaffold consistency:** Narrowed variance across agent scaffolds (64.5%–71.5% range)

**Weaknesses:**
- **Emerging ecosystem:** Smaller developer ecosystem than OpenAI, [[anthropic]], or [[google-gemini]]
- **IPO uncertainty:** HK listing subject to regulatory approval and VIE restructuring
- **Geopolitical risk:** Chinese company facing US-China tech tensions and GPU export restrictions
- **Name recognition:** Less brand awareness outside China
- **Revenue model:** Still establishing commercial viability at low price points

## Key Relationships

- **Fortera Capital** — Series B lead (Shanghai government-backed)
- **Tencent** — Series B participant
- **Shanghai State-owned Capital Investment** — Key pre-IPO backer
- **Geely** — Partnership integrating StepFun models into smart car AI systems (Feb 2025)
- **Agibot** — Data-sharing partnership for embodied AI and robotics (Mar 2025)
- **Hugging Face** — 11+ models hosted; open-source distribution platform
- **Huaqin Technology, Longcheer, OmniVision, ZTE** — Supply chain strategic investors

## Recent Developments

**Model releases:** Step-1 (2024, 1T parameter milestone), Step-3.5-Flash (February 1, 2026), Step-3.7-Flash (May 29, 2026) with Advisor Mode and 3 reasoning depths.

**IPO preparation:** April 2026 — Reuters reported StepFun unwinding offshore VIE structure; target HK IPO filing by June 2026 at $10B valuation. Raised nearly $2.5B from supply chain investors.

**Strategic partnerships:** Geely automotive integration (Feb 2025), Agibot robotics data-sharing (Mar 2025), "Step Up" ecosystem developer event (Feb 2025, Shanghai).