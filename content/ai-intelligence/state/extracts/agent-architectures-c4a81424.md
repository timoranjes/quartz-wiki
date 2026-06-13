title: Agent Architectures
tags: agent-architecture, multi-agent, orchestrator
# Agent Architectures

## Overview

Agent architecture refers to the structural design of how an AI agent reasons, acts, and interacts with its environment. The choice of architecture determines capability, cost, latency, and failure modes.

## Core Patterns

### ReAct (Reason + Act)
Interleaves reasoning traces with tool calls. The agent thinks, acts, observes, then repeats. Simple but effective for single-step tool use.

### Planning
The agent generates a multi-step plan upfront, then executes step-by-step. More robust for complex tasks but fragile when the plan becomes outdated.

### Reflection
The agent critiques its own output before finalizing. Adds a self-review loop that improves accuracy at the cost of extra tokens.

### Orchestrator-Workers
A central orchestrator decomposes a task and delegates subtasks to specialized worker agents. Best for complex, multi-domain problems.

### Multi-Agent Debate
Multiple agents independently solve the same problem, then debate to converge on the best answer. High accuracy, high cost.

## Design Principles

1. **Start simple** — single agent with ReAct before adding orchestration
2. **Fail fast** — detect bad plans or hallucinations early
3. **Budget-aware** — track token spend per step
4. **Observability** — log every decision point

## Related

- [[tool-use-pattern]]
- [[multi-agent-orchestration]]
- [[evaluation-benchmarks]]
- [[single-vs-multi-agent]]