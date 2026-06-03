---
title: "Single Agent vs. Multi-Agent"
type: comparison
tags: [multi-agent, agent-architecture]
created: "2026-06-03"
updated: "2026-06-03"
status: seed
---

# Single Agent vs. Multi-Agent

## Overview

When should you use a single agent versus orchestrating multiple specialized agents?

## Comparison

| Dimension | Single Agent | Multi-Agent |
|-----------|-------------|-------------|
| **Complexity** | Low — one model, one loop | High — coordination, handoff |
| **Cost** | Lower — fewer model calls | Higher — N agents × M steps |
| **Latency** | Faster — serial execution | Slower — orchestration overhead |
| **Accuracy** | Limited by one model's capability | Can exceed single model via specialization |
| **Debugging** | Easy — trace one conversation | Hard — trace inter-agent communication |
| **Scalability** | Bounded by context window | Scales horizontally |

## Decision Guide

### Use Single Agent When
- Task fits in one context window
- Tool use is straightforward (<5 tools)
- Cost sensitivity is high
- You need fast turnaround

### Use Multi-Agent When
- Task requires diverse expertise
- Parallel execution reduces wall-clock time
- Single agent keeps making errors on subtasks
- You need separation of concerns (e.g., researcher vs. writer)

## Hybrid Approach

Route by complexity: single agent handles 80% of tasks; escalate to multi-agent only for the hardest 20%.

## Related

- [[architectures]]
- [[multi-agent-orchestration]]
- [[model-selection-for-agents]]
