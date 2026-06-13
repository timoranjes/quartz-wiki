title: Model Selection for Agents
tags: model-selection, agent-architecture
# Model Selection for Agents

## Overview

Choosing the right model for agent workloads involves balancing reasoning quality, tool-calling ability, latency, and cost.

## Decision Factors

### Reasoning Depth
- **Deep reasoning** (coding, math, analysis) → frontier models
- **Mechanical ops** (formatting, routing, extraction) → smaller/cheaper models

### Tool Use Quality
- Some models excel at function calling (structured output, correct argument types)
- Others hallucinate tool arguments or skip tool calls entirely

### Context Window
- Longer windows enable more conversation history + RAG context
- But cost scales with context size

### Latency
- Interactive agents need <3s response time
- Batch agents can tolerate longer

## Routing Strategy

| Task Type | Model Tier | Rationale |
|-----------|-----------|-----------|
| Complex reasoning | Frontier | Worth the cost |
| Simple classification | Mid-tier | Good enough, cheaper |
| Formatting/extraction | Budget | Mechanical, low reasoning |
| Multi-step planning | Frontier + reasoning | Needs chain of thought |

## Related

- [[evaluation-benchmarks]]
- [[multi-agent-orchestration]]