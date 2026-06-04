---
title: xAI (Grok)
researched: 2026-06-05
sources:
  - https://docs.x.ai/developers/models
  - https://x.ai/news/series-e
  - https://en.wikipedia.org/wiki/SpaceXAI
  - https://mem0.ai/blog/xai-grok-api-pricing
---

# xAI (Grok)

## Company Facts
- Founded: 2023
- HQ: San Francisco / Austin, USA
- CEO: Elon Musk (Founder)
- Funding: $20B Series E (January 2026); valuation ~$230B. xAI was folded into SpaceX on May 6, 2026.

## Model Lineup
| Model | ID | Context | Input $/1M | Output $/1M | Type |
|-------|-----|---------|------------|-------------|------|
| Grok 4.3 | grok-4.3 | 1M | $1.25 | $2.50 | LLM (flagship, agentic) |
| Grok Build 0.1 | grok-build-0.1 | 256K | $1.00 | $2.00 | Coding model (agentic workflows) |
| Imagine API (Image) | — | — | — | $0.02/image | Image generation (1K/2K) |
| Imagine API (Video) | — | — | — | $0.05/sec | Video generation (480p/720p) |
| Voice API (Agent) | — | — | — | $3.00/hour | Real-time voice conversations |
| Voice API (TTS) | — | — | — | $15.00/1M chars | Text-to-speech |
| Voice API (STT) | — | — | — | $0.10–$0.20/hour | Speech-to-text |

Note: Grok 4.1 Fast (legacy) priced at $0.20 input / $0.50 output per 1M tokens. Grok 4.20 also available. Model aliases: `grok` → latest stable, `grok-latest` → latest features, `grok-<date>` → specific release.

## Capabilities
- **Reasoning**: Grok 4.3 supports configurable reasoning effort; non-reasoning mode available
- **Tool Use**: Strong agentic tool calling with minimal hallucinations (Grok 4.3)
- **Coding**: Grok Build 0.1 trained specifically for agentic coding workflows
- **Vision**: Image input support (up to 20MiB per image, no limit on number of images; jpg/jpeg, png)
- **Image Generation**: Imagine API for image generation and editing
- **Video Generation**: Imagine API for video generation (480p/720p)
- **Voice**: Full Voice API stack — real-time agent conversations, TTS, STT (batch & streaming)
- **Search**: Web Search and X Search tools for real-time event access
- **Knowledge Cutoff**: November 2024 for Grok 3 and Grok 4 series

## Key Facts
1. xAI was founded by Elon Musk and 11 researchers in 2023. It was folded into SpaceX on May 6, 2026.
2. Completed a $20B Series E round in January 2026, achieving a ~$230B valuation.
3. Grok 4.3 is the current flagship model with 1M context, strong agentic tool calling, and configurable reasoning.
4. xAI offers dedicated APIs for chat, coding, images, video, and voice — a full multimodal stack.
5. Grok models have no knowledge of real-time events without search tools enabled.
6. `logprobs` and `top_logprobs` are not supported by models `grok-4.20` and newer.
