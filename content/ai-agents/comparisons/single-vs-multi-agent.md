---
title: Single vs Multi-Agent
created: 2026-05-29
updated: 2026-05-29
type: comparison
tags: [comparison, agent-architecture, multi-agent]
sources: []
confidence: high
---

# Single vs Multi-Agent: When to Choose Which

## Definition

Comparing single-agent execution vs multi-agent delegation for task completion. This is the most common architecture decision in agent work.

## Comparison

| Dimension | Single Agent | Multi-Agent (Orchestrator-Workers) |
|-----------|-------------|-----------------------------------|
| Context | Shared, grows over time | Isolated per worker |
| Parallelism | Sequential | Parallel (up to N workers) |
| Complexity handling | Limited by context window | Scales with worker count |
| Cost | Lower (no orchestration overhead) | Higher (N+1 agents) |
| Wall time | Sequential sum | Max of individual tasks |
| State sharing | Natural (in-context) | Requires explicit passing |
| Error isolation | None (one error = all lost) | Per-worker (one fails, others continue) |
| Debugging | Simpler (one trace) | Harder (N traces + synthesis) |
| Best for | Simple tasks, exploration | Complex projects, parallel work |

## Decision Tree

```
Task has >3 independent subtasks?
  Yes -> Multi-Agent
  No -> Can it be done in <5 tool calls?
    Yes -> Single Agent
    No -> Does it need parallel execution?
      Yes -> Multi-Agent
      No -> Single Agent (Plan-and-Execute)
```

## Real Examples

### Single Agent is Better
- "Search for the latest news on NVIDIA earnings"
- "Read this file and summarize it"
- "Fix the typo in line 42"
- "What is the weather in Hong Kong?"

### Multi-Agent is Better
- "Research these 5 companies and write a comparison"
- "Build the frontend, backend, and tests for this feature"
- "Review these 3 PRs and summarize findings"
- "Process 100 files and extract specific patterns"

## Cost Breakdown (Example: Research 3 Topics)

### Single Agent (Sequential)
- 3 research sessions x 15K tokens = 45K input + 30K output
- Total: ~75K tokens
- Wall time: ~90 seconds

### Multi-Agent (Parallel, 3 workers)
- Orchestrator: 5K input + 3K output (delegation + synthesis)
- Workers: 3 x (15K input + 10K output) = 45K + 30K
- Total: ~83K tokens
- Wall time: ~35 seconds

**Trade-off:** 11% more tokens for 61% less wall time.

## Pitfalls

1. **Over-delegating** — Using multi-agent for simple tasks wastes tokens on orchestration.
2. **Under-delegating** — Using single agent for complex tasks leads to context overflow and quality loss.
3. **Wrong worker count** — Too few workers = no speedup. Too many = diminishing returns + parallelism limits.
4. **Missing context** — Workers do not know what each other are doing. Orchestrator must synthesize.

## Related
- [[orchestrator-workers]] — multi-agent implementation details
- [[react-pattern]] — single-agent execution pattern
- [[cost-optimization]] — when the cost trade-off makes sense
