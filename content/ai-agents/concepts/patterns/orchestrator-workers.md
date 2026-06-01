---
title: Orchestrator-Workers Pattern
created: 2026-05-29
updated: 2026-05-29
type: pattern
tags: [multi-agent, orchestration]
sources: []
confidence: high
---

# Orchestrator-Workers Pattern

## Problem Solved

Single agents hit context window limits and can only do one thing at a time. Complex projects need parallel execution and isolated contexts.

## How It Works

```
Orchestrator
    -> Worker 1 (isolated context) -> Task A
    -> Worker 2 (isolated context) -> Task B
    -> Worker 3 (isolated context) -> Task C
    -> Synthesize results
```

Key property: Workers have NO shared context. Each gets its own tools, terminal, and conversation. The orchestrator is the only one who sees everything.

## When to Use

- Research multiple sources simultaneously
- Process N files where each is independent
- Code review across multiple PRs
- Build + test in parallel

## When NOT to Use

- Tasks that need shared state between workers
- Sequential dependencies (A->B->C)
- Simple tasks (orchestration overhead > value)

## Implementation in Hermes

```python
delegate_task(
    tasks=[
        {"goal": "Research X", "context": "...", "toolsets": ["web"]},
        {"goal": "Research Y", "context": "...", "toolsets": ["web"]},
        {"goal": "Research Z", "context": "...", "toolsets": ["web"]},
    ]
)
```

Each task gets its own subagent with isolated context and terminal.

## Context Design (CRITICAL)

Subagents have NO memory of your conversation. You must pass everything they need:

- **Background:** What problem are we solving?
- **Constraints:** What rules apply?
- **Output format:** What should the result look like?
- **Files to check:** Which specific files are relevant?

**Too little context** -> subagent goes off-track, wastes tokens.
**Too much context** -> burns tokens on irrelevant info.

## Pitfalls

1. **Context starvation** — Subagent does not know what the user wants. Fix: be specific in goal + context.
2. **Tool mismatch** — Subagent needs web but only gets terminal. Fix: match toolsets to task type.
3. **Result synthesis failure** — Orchestrator just concatenates instead of synthesizing. Fix: explicit synthesis prompt.
4. **Parallel limit** — Most systems cap at 3-5 concurrent workers. Fix: batch tasks.

## Cost Analysis

| Pattern | Token Cost | Wall Time | Quality |
|---------|-----------|-----------|---------|
| Single agent | Low | High (sequential) | Variable |
| Orchestrator-Workers (3) | Medium-High | Low (parallel) | Consistent |
| Orchestrator-Workers (5) | High | Very Low | Best |

## Related Patterns
- [[planning-pattern]] — orchestrator should plan before delegating
- [[reflection-pattern]] — workers can self-review before returning
- [[model-selection-for-agents]] — different models for orchestrator vs workers
