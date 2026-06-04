---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge competitive">Competitive</span>
    <span class="provider-badge us">🇺🇸 San Francisco</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge multimodal"><span class="cap-icon">🔀</span> Multimodal</span>
    <span class="capability-badge tool-use"><span class="cap-icon">🔧</span> Tool Use</span>
  </div>
</div>

title: Together AI
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, cloud-platform, us, inference, fine-tuning, open-weight, pricing, api, token-cost, timeline, agentic]
sources: [raw/articles/llm-provider-together-ai-2026.md]
confidence: 0.95
---
# Together AI

## Overview

Together AI is a San Francisco-based AI cloud platform founded in June 2022 by Stanford researchers and serial entrepreneurs. The company provides **inference, fine-tuning, and training infrastructure for 200+ open-source foundation models**, positioning itself as a cost- and speed-optimized alternative to hyperscaler clouds (AWS, Azure, GCP). As of mid-2026, Together AI has raised $533.5M+, achieved ~$1B annualized revenue (Feb 2026), and serves 450,000+ developers. The founding team includes CEO Vipul Ved Prakash (two exits to Apple and Proofpoint), CTO Ce Zhang (ETH Zurich), and Chief Scientist Tri Dao (creator of [[meta-llama]]-used FlashAttention). Together AI competes with [[deepseek]]'s API platform, OpenRouter, and Fireworks.ai.

## Product Suite

| Product | Description |
|---------|-------------|
| **Inference API** | Serverless, OpenAI-compatible; 200+ models added within days of release |
| **Fine-Tuning Platform** | SFT, DPO, RLHF; up to 1T parameter models; 6× faster throughput |
| **GPU Clusters** | H100/H200/B200 instant clusters; 100,000+ GPUs, 200 MW capacity |
| **Voice Agent Platform** | Sub-500ms latency; STT + LLM + TTS co-located |
| **RL Platform** | Open-source RL framework with Meta PyTorch team |
| **Data Management** | Refuel.ai acquisition; processes billions of tokens/week |

## Key Technology

Together AI's performance advantage comes from proprietary kernel optimizations:

| Technology | Performance | Description |
|-----------|-------------|-------------|
| **FlashAttention-4** | Up to 4× at long sequences | Algorithm + kernel pipelining co-design |
| **ThunderAgent** | 3.6× throughput for agentic workloads | Specialized agent inference optimization |
| **ATLAS-2** | 1.5× faster inference | Adaptive speculative decoding |
| **FP4 Quantization** | Significant memory reduction | 4-bit quantization for efficient inference |

FlashAttention, created by Tri Dao, reduces inference GPU hours by double-digit percentages and enables 20-40% higher throughput — making Together AI the only commercial cloud whose product roadmap is shaped directly by FlashAttention's author.

## Benchmarks

Together AI claims leadership on open-model benchmarks:

| Metric | Claim | Comparison |
|--------|-------|------------|
| Inference speed | 2-3× faster than hyperscalers | Proprietary kernel optimizations |
| Throughput (Llama/DeepSeek) | 4× vs vanilla vLLM | Same hardware, Together stack |
| Blackwell benchmarks | #1 for top open models | Independent tests |
| Pricing | ~80% cheaper than hyperscalers | Competitive GPU + optimizations |

## GPU Pricing

| GPU Type | Price/GPU-Hour | Use Case |
|----------|----------------|----------|
| HGX H100 | $1.76–$2.39 | Training, inference |
| HGX H200 | $3.15–$3.79 | Large model training |
| HGX B200 | $4.00–$5.50 | Next-gen training/inference |

**Fine-tuning:** SFT (LoRA) ≤16B at $0.48/1M tokens; SFT (Full) ≤16B at $0.54/1M tokens.

## API Ecosystem

Together AI provides OpenAI-compatible REST API at `https://api.together.xyz/v1` supporting chat completions, embeddings, images, audio, and vision. Features include batch API (50% cheaper, up to 50k requests/batch, 24h SLA), Together Reasoning Clusters for low-latency token-heavy workloads, and streaming support. Official SDKs available for Python and other languages.

## Strengths / Weaknesses

**Strengths:**
- **FlashAttention integration:** Only cloud with direct access to FlashAttention's creator
- **Model variety:** 200+ models, added within days of release
- **Cost efficiency:** ~80% cheaper than hyperscalers; often described as "the $44M/year Vercel of generative AI"
- **Full stack:** Inference, fine-tuning, training, and GPU clusters in one platform
- **Revenue growth:** ~400% YoY growth from ~$130M (2024) to ~$1B (Feb 2026)
- **Open-source commitment:** RedPajama datasets, open-source kernel optimizations
- **Developer experience:** OpenAI-compatible APIs, self-service clusters

**Weaknesses:**
- **Model dependency:** Relies on open-source releases (Meta [[meta-llama]], [[mistral]], etc.); risk of model providers building own platforms
- **Infrastructure costs:** Massive capex for GPU procurement and data center construction
- **Competition:** Hyperscaler response, GPU cloud rivals (CoreWeave, Lambda Labs), inference specialists (Fireworks.ai)
- **Margin pressure:** ~45% gross margin needs improvement to justify $7.5B valuation
- **Pricing pressure:** Race to the bottom on per-token pricing across the industry

## Key Relationships

- **NVIDIA** — Strategic GPU supplier and Series C investor; Blackwell deployment partnership
- **General Catalyst** — Series B co-lead; leading VC firm
- **Prosperity7 Ventures** — Saudi sovereign wealth fund; Series B co-lead and Series C participant
- **Hypertec** — 36,000 GB200 NVL72 GPU supply agreement
- **Salesforce Ventures** — Enterprise AI integration potential; Series A+ lead
- **Kleiner Perkins** — Series A lead; historic Silicon Valley VC
- **Meta (PyTorch team)** — Open-source RL framework co-development
- **Pegatron/5C** — GB300 NVL72 and HGX B200 deployment partnership

## Recent Developments

**Funding:** Series B $305M at $3.3B valuation (Feb 2025); Series C ~$1B at $7.5B pre-money in talks (2026). Total raised: $533.5M+.

**Infrastructure:** Maryland data center live (July 2025); 200 MW power capacity secured; 100,000+ GPUs deployed; 36,000 GB200 NVL72 ordered from Hypertec.

**Product launches:** Voice Agent Platform with sub-500ms latency (Mar 2026); Refuel.ai acquisition for data management (May 2025); RedPajama open dataset project (2023).
