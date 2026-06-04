---
title: Microsoft Phi
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, model, reasoning, coding, vision, audio, multimodal, open-weight, pricing, edge, token-cost, timeline]
sources: [raw/articles/llm-provider-microsoft-phi-2026.md]
confidence: 0.95
---
# Microsoft Phi

## Overview

The Phi family is a line of small language models (SLMs) developed by [[microsoft]] Research, demonstrating that carefully curated training data and efficient architectures can produce models rivaling systems orders of magnitude larger. Originating from the 2023 "Textbooks Are All You Need" paper, Phi has evolved from Phi-1 (1.3B parameters) through the current Phi-4 family (14B parameters), with multimodal and reasoning variants expanding across text, vision, and audio domains.

Phi occupies a distinct niche within Microsoft's AI portfolio: while GPT models target frontier capabilities, Phi targets cost-efficiency, low latency, and edge deployment. All Phi models are open-weight under the MIT license, available through Azure AI Foundry, Hugging Face, NVIDIA API Catalog, Ollama, and third-party providers.

## Model Lineup

| Model | Params | Context | Type |
|-------|--------|---------|------|
| **Phi-4** | 14.7B | 16K tokens | Dense text generation |
| **Phi-4-mini** | 3.8B | 128K tokens | Edge-optimized text |
| **Phi-4-multimodal** | 5.6B | 128K tokens | Text + audio + vision |
| **Phi-4-reasoning** | 14B | 16K tokens | Chain-of-thought optimized |
| **Phi-4-reasoning-vision-15B** | 15B | 16K tokens | Visual reasoning with task-aware CoT |

**Lineage highlights:** Phi-1/1.5 (2023, 1.3B), Phi-2 (2023, 2.7B), Phi-3 family (2024, introduced vision), Phi-3.5-MoE (2024, first MoE variant), Phi-4 (2024, 9.8T training tokens on 1,920 H100 GPUs).

**Architecture principles:** Data-centric training over raw parameter scaling; synthetic textbook-quality data generation; curriculum learning (simple to complex); rigorous data decontamination; dense Transformer (no architectural novelty needed); grouped-query attention (mini); shared embeddings (mini); Mixture-of-LoRAs (multimodal).

## Benchmarks

**Phi-4 (14B) vs. larger models:**

| Benchmark | Phi-4 (14B) | Llama 3.3 (70B) | Qwen 2.5 (72B) | GPT-4o |
|-----------|-------------|-----------------|----------------|--------|
| MMLU | **84.8** | 86.3 | 85.3 | 88.1 |
| MATH | **80.4** | 66.3* | 80.0 | 74.6 |
| GPQA | **56.1** | 49.1 | 49.0 | 50.6 |
| HumanEval | **82.6** | 78.9* | 80.4 | 90.6 |
| GSM8K | **95.6** | 95.1 | 90.2 | — |

*Note: Llama scores lower due to strict formatting requirements in this evaluation.

**Phi-4-reasoning-vision-15B:** Leads on ChartQA (83.3) and ScreenSpot_v2 (88.2, strong UI grounding for computer-use agents). Competitive with 32B+ multimodal models across visual reasoning benchmarks.

**Artificial Analysis Indices (mid-2026):** Intelligence 10.4, Coding 11.2, Math 18 (exceptional for size), Agentic 3.8 (weakness).

## API Pricing & Availability

Phi-4 is among the cheapest models in its capability class:

| Channel | Input ($/1M) | Output ($/1M) | Notes |
|---------|--------------|---------------|-------|
| Azure AI Foundry | ~$0.065 | ~$0.14-0.23 | Primary commercial |
| OpenRouter (NextBit/DeepInfra) | ~$0.07 | ~$0.14 | Multiple backends |
| Ollama | Free | Free | Self-hosted, open weights |
| NVIDIA API Catalog | Variable | Variable | Optimized for NVIDIA GPUs |

**Hardware:** Phi-4 runs on a single RTX 4090 with 4-bit quantization (~9 GB VRAM, ~70 tok/s). Phi-4-mini fits in 2.5 GB (Q4), enabling edge deployment. Phi-4-multimodal requires ~4 GB (Q4).

## API Ecosystem

Phi models are first-class citizens in Azure AI Foundry with optimized inference pipelines and SOC 2 Type II compliance. They are also available through Microsoft Foundry Models Catalog, Hugging Face (open weights), NVIDIA API Catalog, Ollama (`ollama pull phi4`), OpenRouter, llama.cpp (GGUF quantization), and vLLM (AWQ-INT4 support). Official Python SDK via Hugging Face Transformers.

Fine-tuning is accessible on consumer hardware: full fine-tuning on single A100, LoRA on 24GB+ VRAM. Phi-4-mini supports function calling and tool use across 23+ languages. Phi-4-multimodal supports speech recognition (#1 on Hugging Face OpenASR at 6.14% WER), speech translation, and speech summarization.

## Strengths / Weaknesses

**Strengths:**
- **Exceptional math performance:** 80.4% on MATH, 95.6% on GSM8K — outperforms models 5-10× larger
- **Cost efficiency:** Among cheapest per token (~$0.065/M input on Azure)
- **Edge deployment:** Designed for resource-constrained hardware; runs on 12GB consumer GPU
- **Open weights:** MIT License enables unrestricted commercial use and modification
- **Fine-tuning accessibility:** Full fine-tuning on single A100 GPU
- **Low latency:** ~5× faster inference than 70B+ models (~70 tok/s on RTX 4090)
- **Multimodal range:** Phi-4-multimodal handles text, audio, and vision in unified 5.6B model
- **Windows integration:** Native support in Copilot+ PCs for always-on AI
- **Speech recognition leadership:** #1 on Hugging Face OpenASR leaderboard

**Weaknesses:**
- **Limited context (base Phi-4):** 16K tokens restricts long-document processing
- **No vision (base Phi-4):** Requires multimodal or reasoning-vision variant
- **Poor agentic performance:** 3.8 agentic index limits autonomous task execution
- **Weak terminal/CLI:** 3.8% on TerminalBench Hard
- **Low factual accuracy:** 3.0% on SimpleQA — prioritizes reasoning over memorization
- **English-only focus (base):** Only ~8% multilingual training data in base Phi-4
- **Competition math gap:** 12.0% on AIME 2024 vs. [[deepseek]]-R1 at 79.8%

## Key Relationships

- **Microsoft Research** — Developer; led by team including Marah Abdin, Sébastien Bubeck, Yuanzhi Li, and others
- **Azure AI Foundry** — Primary commercial distribution platform
- **NVIDIA** — Optimized inference via NVIDIA API Catalog; training on H100/A100 GPUs
- **Hugging Face** — Open-weight distribution platform; Phi-4 achieves 893K+ monthly downloads
- **OpenAI** — [[openai]] partnership context; Phi complements proprietary GPT models in Microsoft's portfolio
- **Google Gemma / Meta Llama** — Competing open-weight SLM families in similar parameter ranges

## Recent Developments

**Model releases (2024-2026):** Phi-4 (December 2024, 14.7B), Phi-4-mini (February 2025, 3.8B edge-optimized), Phi-4-multimodal (February 2025, 5.6B unified text/audio/vision), Phi-4-reasoning (2025, native chain-of-thought), Phi-4-reasoning-vision-15B (March 4, 2026, task-aware visual reasoning).

**Research:** "Textbooks Are All You Need" series (Phi-1 through Phi-2), Phi-3 Technical Report (April 2024), Phi-4 Technical Report (arXiv:2412.08905), Phi-4-reasoning-vision Technical Report (March 2026).

**Integration:** Phi models integrated into Windows Copilot+ PCs for always-on low-power AI experiences. First open-sourced model with speech summarization capability. Active GGUF quantization support via llama.cpp community.

## Coding Agents Using Microsoft Models

- [[../coding-agents/github-copilot]] — GitHub Copilot (Microsoft-owned, supports Phi models)

## Agent Frameworks Supporting Microsoft

- [[../agent-frameworks/langchain]] — Full LangChain/LangGraph integration
- [[../agent-frameworks/autogen]] — Microsoft Research's own framework — primary developer
- [[../agent-frameworks/llamaindex]] — Microsoft/Azure model support
