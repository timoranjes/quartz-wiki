---
title: "Single vs Multi-Agent"
type: concept
tags: [agent-architecture, multi-agent, model-selection, trade-offs]
created: "2026-06-04"
updated: "2026-06-04"
status: seed
---

# Single vs Multi-Agent

## Overview

Choosing between a single-agent and multi-agent architecture is one of the most important design decisions in building AI systems.

## Single-Agent

**When to use:**
- Task is well-defined and linear
- Single model has sufficient capability
- Cost and latency are primary concerns
- Simpler debugging and observability needed

**Characteristics:**
- One LLM handles all reasoning, tool use, and output
- Lower token cost (no coordination overhead)
- Easier to debug and trace
- Simpler prompt engineering

## Multi-Agent

**When to use:**
- Task requires diverse expertise (code + research + analysis)
- Parallel execution reduces wall-clock time
- Single agent context window is insufficient
- Different models excel at different subtasks

**Characteristics:**
- Multiple specialized agents coordinate
- Higher token cost (coordination overhead)
- More complex debugging
- Requires orchestration framework (see [[multi-agent-orchestration]])

## Rule of Thumb

> "Most applications don't need multi-agent systems. A single agent with good tools and a clear system prompt handles 80% of real-world use cases." — PE Collective, 2026

## Related

- [[architectures]]
- [[multi-agent-orchestration]]
- [[model-selection-for-agents]]
- [[evaluation-benchmarks]]
