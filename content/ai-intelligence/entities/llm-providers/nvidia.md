---
title: NVIDIA
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, infrastructure, model, reasoning, agentic, tool-use, open-weight, token-cost, multimodal, nvidia-gpu, nemotron, nim]
sources: [raw/articles/llm-provider-nvidia-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge enterprise">NIM Cloud</span>
    <span class="provider-badge us">🇺🇸 Santa Clara</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge vision"><span class="cap-icon">👁️</span> Vision</span>
    <span class="capability-badge multimodal"><span class="cap-icon">🔀</span> Multimodal</span>
    <span class="capability-badge tool-use"><span class="cap-icon">🔧</span> GPU/NIM</span>
  </div>
</div>

# NVIDIA

## Overview

NVIDIA Corporation is the world's leading AI computing company, founded in 1993 by Jensen Huang, Chris Malachowsky, and Curtis Priem. While originally known for GPUs, NVIDIA has become the foundational infrastructure provider for the AI revolution — controlling 80-95% of AI training GPU shipments with over $100B in annual data center revenue (FY2025-2026).

NVIDIA occupies a unique position in the AI model space: it is both the **primary infrastructure provider** for AI training/inference AND an **AI model developer** through its Nemotron family. This structural advantage provides first access to new silicon (Blackwell, Rubin), deep software optimization via CUDA/TensorRT-LLM, and hardware-software co-design. The Nemotron 3 family (Nano, Super, Ultra) represents NVIDIA's latest generation of open foundation models with hybrid Mamba2-Transformer architectures and up to 1M token context windows.

## Model Lineup (Nemotron 3)

| Model | Total / Active Params | Context | Pricing | Type |
|-------|----------------------|---------|---------|------|
| **Nemotron 3 Ultra** | ~500B / 50B | 1M+ tokens | Varies | Largest, most capable (pending release) |
| **Nemotron 3 Super** | 120B / 12B | 1M tokens | Free (OpenRouter tier) | Balanced, Hybrid MoE |
| **Nemotron 3 Nano** | 31.6B / 3.2B | 1M tokens | Varies by provider | Cost-efficient, Mamba2+MoE |
| **Nemotron 3 Nano Omni** | ~30B / ~3B | 1M tokens | Varies by provider | Multimodal (text+vision+video) |

Nemotron 3 Super was the first model pre-trained in 4-bit NVFP4 precision on Blackwell architecture. Nano Omni achieves 9x faster throughput than comparable models and runs on just 25GB RAM.

### NIM Model Catalog

NVIDIA NIM (Inference Microservices) hosts **42+ models** including [[openai]] competitors' models (Llama, Qwen, DeepSeek, Gemma, [[minimax]], Kimi K2, GLM-5). Third-party models via NIM range from $0.04-$1.20/M input and $0.16-$1.20/M output, with median at $0.095/$0.425.

## Benchmarks

| Benchmark | Nemotron 3 Nano | Nemotron 3 Super | Notes |
|-----------|-----------------|------------------|-------|
| RULER (64K) | **87.5%** | — | Long-context retrieval |
| RULER (512K) | **70.56%** | — | Very long context |
| Inference Throughput | — | **2.2x faster** | vs. gpt-oss-120b via MTP |
| Intelligence Index | Competitive | Competitive | Used 110M tokens for eval |
| Cost Efficiency | **Best-in-class** | — | Lowest cost/token in class |

On pure LLM reasoning benchmarks, GPT-5 and o3-Pro still outperform Nemotron 3 for complex text and coding tasks. Nemotron models are optimized for agentic reasoning, multi-agent applications, and cost-efficient inference rather than raw reasoning capability.

## API Ecosystem

- **NIM API:** OpenAI-compatible endpoints at `https://integrate.api.nvidia.com/v1`
- **Free Tier:** Developer credits for evaluation (efficient models like Nemotron-3-Super maximize credits-per-insight)
- **Inference Engines:** vLLM, SGLang, TensorRT-LLM (best performance), LM Studio, Ollama
- **NeMo Framework:** End-to-end model development (pre-training, fine-tuning, synthetic data, evaluation, deployment)
- **Nemotron-4-340B:** 340B parameter model specifically for synthetic data generation
- **Self-Hosting:** Open weights support multiple inference engines

NIM APIs support OpenAI-compatible chat completions with standard message format. TensorRT-LLM provides kernel optimization, FP8/INT4 quantization, speculative decoding for MTP models, and multi-GPU deployment.

## Strengths / Weaknesses

**Strengths:**
- **Hardware-software co-design:** Models optimized for NVIDIA GPUs with first access to new silicon
- **Novel architectures:** Hybrid Mamba2-Transformer, NVFP4 4-bit training, Multi-Token Prediction (MTP)
- **Cost efficiency:** Low active parameter counts via MoE; Nano runs on 25GB RAM
- **Open models:** Free weights, open licenses across the Nemotron family
- **NIM ecosystem:** Single platform for 42+ models, OpenAI-compatible API
- **NeMo framework:** Full model development pipeline from training to deployment
- **Enterprise infrastructure:** Complete stack from silicon to software
- **1M token context:** Across the entire Nemotron 3 family

**Weaknesses:**
- **Raw reasoning gap:** Behind GPT-5 and [[anthropic]] Claude on complex reasoning and coding
- **Newer model family:** Less battle-tested than GPT or Claude lineages
- **Not coding-optimized:** No dedicated coding model in the lineup
- **Ecosystem maturity:** Less third-party tooling vs. OpenAI
- **Ultra availability:** Nemotron 3 Ultra not yet widely released

## Key Relationships

- **OpenAI** — Competitor in API model space; [[openai]] partnership for 10 GW GPU deployment and Stargate data center project
- **Meta** — Llama models hosted on NIM; [[meta-llama]] community is larger than Nemotron's
- **Google Gemini** — Cloud integration competitor; Gemini models also available via NIM
- **Mistral** — European open-model competitor; [[mistral]] models on NIM catalog
- **Together AI / DeepInfra** — API platform competitors that NIM directly challenges

## Recent Developments

**Nemotron 3 launch (2026):** Three-model family (Nano, Super, Ultra) with hybrid Mamba-Transformer architecture, NVFP4 4-bit training on Blackwell, and multi-environment RL training.

**Nemotron 3 Nano Omni:** Multimodal extension covering text + vision + video in a single efficient model; 9x faster throughput; best-in-class on MediaPerf benchmark.

**Blackwell architecture:** NVIDIA's GPU platform enabling NVFP4 precision training, higher MoE throughput, and lower power per token — foundation for Nemotron 3 training.

**NIM expansion:** Now hosts 42+ models with growing third-party catalog, OpenAI-compatible API, free developer tier, and enterprise pricing.

**Rubin platform:** Announced as next-generation GPU architecture after Blackwell, targeting AI token generation improvements through 2026 and beyond.
