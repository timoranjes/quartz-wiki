---
title: "Multi-Agent Orchestration"
type: concept
tags: [multi-agent, orchestrator, agent-architecture]
created: "2026-06-03"
updated: "2026-06-03"
status: seed
---

# Multi-Agent Orchestration

## Overview

Multi-agent orchestration coordinates multiple specialized agents to solve problems that exceed a single agent's capability.

## Patterns

### Orchestrator-Workers
Central agent decomposes tasks and assigns to workers. Workers are independent; orchestrator synthesizes results.

### Supervisor-Workers
Similar to orchestrator but the supervisor actively monitors and can reassign tasks mid-flight.

### Peer-to-Peer
Agents communicate directly without a central coordinator. Emergent behavior, harder to control.

### Hierarchical
Multi-level hierarchy where orchestrators delegate to sub-orchestrators. Scales to very large problems.

## Challenges

- **Coordination overhead** — More agents ≠ more throughput
- **Information loss** — Handoff between agents loses context
- **Cost multiplication** — Each agent step costs tokens
- **Debugging** — Tracing failures across agents is harder

## When to Use

- Task requires diverse expertise (code + research + analysis)
- Parallel execution reduces wall-clock time
- Single agent context window is insufficient

## Related

- [[architectures]]
- [[single-vs-multi-agent]]
- [[model-selection-for-agents]]
