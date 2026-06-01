---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/us, provider/closed-source]
aliases: [Gemini, Google AI, Google]
created: 2026-06-01
---
# Google (Gemini)

## Overview
- **Founded:** 1998 (Google); Gemini launched Dec 2023
- **CEO:** Sundar Pichai; DeepMind led by Demis Hassabis
- **HQ:** Mountain View, CA
- **Key Products:** Gemini API, Gemini App, Vertex AI, AI Studio, Veo, Imagen, Lyria
- **Platforms:** ai.google.dev (developer), cloud.google.com/vertex-ai (enterprise)
- **Integration:** Deeply integrated into Google Workspace, Search, Android, Chrome

## Strategy
Leverage unparalleled infrastructure (TPUs, global data centers) + massive existing user base + broadest multimodal portfolio (text, image, video, audio, music).

## Model Lineup (2026)

| Model | Context | Input $/1M | Output $/1M | Release |
|-------|---------|-----------|------------|---------|
| **Gemini 3.5 Flash** | 1M | $1.50 | $9.00 | May 2026 |
| **Gemini 3.1 Pro Preview** | 1M | $2.00 (≤200K) / $4.00 (>200K) | $12.00 / $18.00 | Early 2026 |
| **Gemini 3.1 Flash-Lite** | 1M | $0.25 | $1.50 | 2026 |
| **Gemini 2.5 Flash** | 1M | $0.30 | $2.50 | Late 2025 |

## Specialty Models
| Model | Type | Notes |
|-------|------|-------|
| Veo 3.1 Generate | Video generation | Cinematic video with synchronized audio |
| Gemini 3 Pro Image (Nano Banana Pro) | Image generation | 4K studio-quality |
| Imagen 4 | Image generation | Fast text-to-image up to 2K |
| Lyria 3 Pro | Music generation | Full-length song generation |
| Gemini Deep Research | Agentic research | Autonomous multi-source research |
| Antigravity | Managed agent | Secure Linux sandbox with web browsing |

## Key Benchmarks (Gemini 3.5 Flash)
- Terminal-Bench 2.1: **76.2%**
- MCP Atlas: **83.6%**
- Toolathlon: **56.5%**
- Finance Agent v2: **57.9%**
- CharXiv: **84.2%**
- MMMU-Pro: **83.6%**
- ARC-AGI-2: 72.1%

## API & Ecosystem
- Gemini API (REST + gRPC)
- Function calling, thinking mode, structured output
- Native Google Search grounding (5K free/month)
- Context caching
- 1M context on free tier (unique)
- Hosting: Google AI Studio, Vertex AI, OpenRouter

## Strengths
- Best price-performance (4× faster output)
- Broadest multimodal portfolio (text, image, video, audio, music)
- Google Search grounding
- Free tier with 1M context
- Massive TPU infrastructure
- Workspace/Android integration

## Recent Developments
- May 2026: Gemini 3.5 Flash at Google I/O (4× faster)
- Apr 2026: Deep Research preview
- 2026: Flash-Lite released ($0.25/$1.50)

[[openai]] · [[anthropic]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
