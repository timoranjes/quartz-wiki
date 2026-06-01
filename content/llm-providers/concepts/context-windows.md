---
domain: llm-providers
type: concept
tags: [concept/long-context, concept/architecture]
aliases: [Context Window, Long Context, Needle in a Haystack]
created: 2026-06-01
---
# Context Windows & Long Context

## Overview
Context window is the maximum number of tokens a model can process in a single request (input + output). Long context capability is a key differentiator among frontier models.

## Provider Context Windows (2026)

| Provider | Model | Max Context | Notes |
|----------|-------|------------|-------|
| **Meta** | Llama 4 Scout | **10M tokens** | Longest public (iRoPE), functional at scale unproven |
| **OpenAI** | GPT-5.5 | 1M (922K in) | Standard for flagship |
| **Anthropic** | Opus 4.8 | 1M | Standard across Opus 4.7+ |
| **Google** | Gemini 3.5 Flash | 1M | 1M on free tier (unique) |
| **DeepSeek** | V4-Pro | 1M | Engram memory: 97% NIAH at 1M |
| **Alibaba** | Qwen3.7 Max | 1M | Strong 800K+ recall (third-party verified) |
| **xAI** | Grok 4.20 Multi-Agent | 2M | Multi-agent variant only |
| **Mistral** | Most models | 256K | Smallest among frontier providers |

## Long Context Benchmarks

### MRCR v2 (Long-Context Reasoning)
| Model | 128K | 1M |
|-------|------|-----|
| GPT-5.5 | **94.8%** | **74.0%** |
| Gemini 3.1 Pro | **84.9%** | — |
| DeepSeek V4-Pro | — | **83.5%** |
| Claude Opus 4.8 | — | 67.7% (AA-LCR) |
| Gemini 3.5 Flash | 77.3% | — |

### NIAH (Needle in a Haystack)
| Model | Score | Context |
|-------|-------|---------|
| DeepSeek V4-Flash | **97%** | 1M tokens (Engram memory) |
| GPT-5.5 | ~90% | 1M tokens |
| Standard attention | 84.2% | 1M tokens |

## Technical Approaches
- **RoPE** (Rotary Position Encoding): Standard position encoding
- **iRoPE** (Interleaved RoPE): Meta's variant — every 4th layer uses NoPE with full attention
- **Engram Memory** (DeepSeek): Conditional memory achieving 97% NIAH at 1M
- **Chunked Attention**: Processing context in chunks with overlap

## When Long Context Matters
- Analyzing entire codebases
- Processing long documents/reports
- Multi-document synthesis
- Legal contract analysis

## Trade-offs
- Longer context = higher cost
- Retrieval accuracy degrades at extreme lengths (functional 10M context unproven)
- Output quality can degrade with very long inputs

## Related
- [[prompt-caching]] — Caching makes long-context workflows economical
- [[moE-architecture]] — MoE models handle large contexts more efficiently
