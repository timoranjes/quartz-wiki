---
domain: llm-providers
type: concept
tags: [concept/reasoning, concept/thinking]
aliases: [Extended Thinking, Reasoning Mode, Chain of Thought, o-series]
created: 2026-06-01
---
# Extended Thinking / Reasoning Mode

## Overview
Extended thinking allows models to perform internal reasoning (chain-of-thought) before producing a final answer, improving accuracy on complex tasks at the cost of higher latency and token usage.

## Provider Implementations

### Anthropic — Extended Thinking (Most Granular)
- **Effort levels**: low → medium → high → xhigh → max
- **Available on**: Opus 4.7+ (added xhigh in Opus 4.7)
- **Control**: Developer trades latency for quality per request
- **Output**: Thinking tokens + final answer
- **Best for**: Complex reasoning, debugging, multi-step analysis

### OpenAI — o-series (Reasoning Models)
- **Models**: o3 ($10/$40), o4-mini ($1.10/$4.40)
- **Approach**: Dedicated reasoning model family (separate from GPT line)
- **GPT-5.5**: Has reasoning capability but not a separate model

### Google — Thinking Mode
- **Available on**: Gemini 3.5 Flash
- **Native thinking**: Similar to extended thinking
- **Integrated**: Part of the standard model, not a separate line

### DeepSeek — Hybrid Thinking
- **Modes**: Non-thinking, Think High, Think Max
- **Switchable**: Per request via `reasoning_effort` parameter
- **Pricing**: Thinking tokens billed at same rate
- **R1**: Pure RL reasoning model (671B/37B MoE)

### xAI — Configurable Reasoning
- **Levels**: None → Low → Medium → High
- **Available on**: Grok 4.3
- **Approach**: Configurable per request

### Mistral — Magistral
- **Models**: Magistral Medium (chain-of-thought, $2.00/$5.00)
- **Magistral Small 1.2**: Multimodal reasoning ($0.50/$1.50)
- **Medium 3.5**: Configurable reasoning effort built-in

## Benchmarks Impact
Extended thinking significantly improves scores on reasoning benchmarks:
- SWE-bench Pro, GPQA Diamond, AIME, ARC-AGI-2 all benefit
- Trade-off: 30-60 minutes per task for deepest reasoning (DeepSeek R1)

## When to Use
- Complex multi-step reasoning
- Code debugging and analysis
- Math and scientific problems
- Planning and strategy tasks

## When NOT to Use
- Simple classification/extraction
- Real-time/low-latency requirements
- Cost-sensitive high-volume tasks

## Related
- [[moE-architecture]] — Reasoning models often use MoE
- [[prompt-caching]] — Caching can reduce repeated reasoning costs
