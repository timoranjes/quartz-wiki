---
title: Extended Thinking / Reasoning Mode
created: 2026-06-01
updated: 2026-06-02
type: concept
tags:
  - reasoning
  - inference
sources:
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-anthropic-2026.md
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-google-gemini-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
  - raw/articles/llm-provider-stepfun-2026.md
  - raw/articles/llm-provider-minimax-2026.md
  - raw/articles/llm-provider-perplexity-2026.md
  - raw/articles/llm-provider-cohere-2026.md
  - raw/articles/llm-provider-nvidia-2026.md
  - raw/articles/llm-provider-microsoft-phi-2026.md
confidence: high
---

# Extended Thinking / Reasoning Mode

## Overview

Extended thinking (also called reasoning mode, thinking mode, or chain-of-thought mode) allows LLMs to generate internal reasoning traces before producing a final answer. This significantly improves performance on complex reasoning tasks including mathematics, coding, logical analysis, and multi-step planning.

## Provider Implementations

| Provider | Feature Name | Control Method | Best For |
|----------|-------------|----------------|----------|
| OpenAI | Reasoning Effort | `effort` parameter (low/medium/high) | Math, science, analysis |
| Anthropic | Extended Thinking | `thinking` parameter with token budget | Complex reasoning, analysis |
| DeepSeek | Thinking Mode | `thinking` parameter (true/false) | Math, coding, logic |
| Google | Gemini Thinking | Built-in reasoning with adjustable depth | Research, analysis |
| xAI | Grok Thinking | Reasoning toggle for complex queries | Analysis, debate |
| Mistral | Codestral Thinking | Extended reasoning for code tasks | Code generation, debugging |
| MiniMax | Thinking Mode | Reasoning parameter | Math, multi-modal reasoning |
| StepFun | Advisor Mode | Step-3.7-Flash reasoning mode | Enterprise analysis |
| Perplexity | Research Mode | Deep research with citations | Fact-checking, research |
| Cohere | Command Reasoning | Reasoning-optimized variant | Enterprise logic |
| Microsoft | Phi Reasoning | Extended thinking for Phi-4 | On-device reasoning |
| NVIDIA | Nemotron Reasoning | Reasoning-optimized Nemotron variants | Enterprise logic |

## Performance Impact

### Benchmarks with Extended Thinking

| Model | Reasoning Mode | AIME 2025 | GPQA Diamond | Codeforces |
|-------|---------------|-----------|-------------|------------|
| DeepSeek V4 Pro Max | Thinking ON | — | — | 3206 (Grandmaster) |
| Claude Opus 4.6 | Thinking ON | — | — | — |
| GPT-5.5 | High effort | Leading | Leading | — |
| Gemini 3.5 Pro | Thinking ON | — | — | — |
| Grok 4.3 | Thinking ON | Competitive | Competitive | — |
| Kimi K2 | Reasoning ON | — | — | — |

### Token Overhead

- Extended thinking typically adds 2-10× more tokens to each response
- DeepSeek V4 Flash: thinking mode costs $0.28/M output tokens (same as regular)
- OpenAI: reasoning effort high costs significantly more per output token
- Anthropic: thinking budget controlled by user (e.g., 1024, 4096 tokens)

## Use Cases

- **Mathematics**: AIME, Putnam, IMO-level problems require extended reasoning
- **Coding**: Complex debugging, architecture design, algorithm optimization
- **Research**: Multi-step analysis, hypothesis generation, literature synthesis
- **Planning**: Multi-objective optimization, constraint satisfaction
- **Legal/Financial**: Contract analysis, risk assessment, compliance checking

## Open Debates

- **CoT leakage**: Should reasoning traces be exposed to users or hidden? Security implications of leaked reasoning
- **Over-reliance**: Does extended thinking mask fundamental model weaknesses?
- **Cost vs benefit**: When is the token overhead justified? For simple queries, thinking mode wastes tokens
- **Alignment interference**: Does alignment training conflict with honest reasoning traces?

## Related

- [[rlhf-training]] — Reasoning modes require specialized alignment techniques
- [[context-windows]] — Extended thinking consumes context budget rapidly
- [[distillation]] — Reasoning capabilities are distilled from large models into smaller ones
