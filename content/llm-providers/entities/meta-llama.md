---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/us, provider/open-weight]
aliases: [Llama, Meta AI, Meta Platforms]
created: 2026-06-01
---
# Meta (Llama)

## Overview
- **Parent:** Meta Platforms (formerly Facebook)
- **Strategy:** "Android strategy for AI" — open-source to become de facto standard
- **Infrastructure:** Colossus supercomputer cluster; AWS Bedrock, Azure, GCP hosting
- **Consumer Products:** Meta AI across WhatsApp, Instagram, Messenger (40+ countries)

## Model Lineup (Llama 4, April 2025)

| Model | Active | Total | Context | Status |
|-------|--------|-------|---------|--------|
| **Llama 4 Scout** | 17B | 109B | **10M tokens** (iRoPE) | Released |
| **Llama 4 Maverick** | 17B | 400B | 1M tokens | Released |
| **Llama 4 Behemoth** | 288B | ~2T | 16K tokens | **Delayed** (not released) |

## Architecture
- MoE with iRoPE (Interleaved Rotary Position Encoding)
- Native early-fusion multimodal (text+image+video, no audio)
- Codistillation: Behemoth (unreleased teacher) distilled into Scout/Maverick
- 200+ languages, <2% refusal rate
- Inference: Scout ~143 tok/s, Maverick ~109 tok/s

## Licensing
- Llama 4 Community License (NOT OSI open source)
- Free commercial use under 700M MAU
- >700M MAU requires separate license from Meta

## Benchmarks (Maverick)
| Benchmark | Maverick | GPT-4o | Gemini 2.5 Pro |
|-----------|----------|--------|----------------|
| MMLU | 85.5 | ~87.2 | 91.0 |
| MMLU Pro | 80.5 | ~74.4 | 86.5 |
| GPQA Diamond | 69.8 | ~53.6 | 86.4 |
| MMMU (vision) | 73.4 | 69.1 | 81.7 |
| AA Intelligence Index | 18/100 | — | 35/100 |

## API & Availability
- Weights on Hugging Face, llama.com
- Self-hosting: Scout on single H100 (INT4), Maverick needs 8× H100 DGX
- Third-party APIs: DeepInfra ($0.15/$0.60), OpenRouter ($0.10/$0.60), Together AI ($0.20/$0.60)
- Available on Ollama, Bedrock, Replicate, Groq

## Strengths
- Most widely deployed open-weight model family
- 10M-token context (longest public)
- Privacy-first (self-hosting)
- No vendor lock-in
- ~15× cheaper than GPT-4o via third parties

## Weaknesses
- EU gap (blocked by regulation)
- Behemoth delayed (benchLM 12/100)
- LMArena benchmark controversy (April 2025)
- Maverick AA Index 18/100 (27/43) — behind Gemini 2.5 Pro

## Recent Developments
- Apr 2025: Llama 4 Scout + Maverick released
- Apr 2025: LMArena controversy
- May 2026: Llama 4 Search integration (Instagram, Facebook)

[[openai]] · [[anthropic]] · [[google-gemini]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
