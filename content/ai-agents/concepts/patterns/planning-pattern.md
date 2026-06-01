---
title: Planning Pattern
created: 2026-05-29
updated: 2026-05-29
type: pattern
tags: [planning, agent-architecture]
sources: []
confidence: high
---

# Planning Pattern

## Problem Solved

Complex tasks fail when the agent jumps straight into execution without understanding the full scope. Planning separates "what to do" from "doing it."

## How It Works

```
Phase 1: Plan
- Analyze the task
- Break into steps
- Identify dependencies
- Choose tools for each step

Phase 2: Execute
- Follow the plan step by step
- Mark steps complete
- Revise plan if stuck

Phase 3: Verify
- Check all steps completed
- Verify the result
```

## When to Use

- Building features (multiple files, tests, integration)
- Multi-step data processing
- Tasks with dependencies (A must finish before B)
- When you can preview the plan before execution

## When NOT to Use

- Simple lookups (overhead > value)
- Exploratory tasks where the plan cannot be known upfront (use ReAct)
- Real-time tasks where planning introduces latency

## Plan-First Prompt Template

```
Before taking any action, create a plan:

## Plan
1. [Step 1] -- [tool/method] -- [expected output]
2. [Step 2] -- [tool/method] -- [expected output]
3. [Step 3] -- [tool/method] -- [expected output]

Dependencies: [which steps depend on others]
Risks: [what could go wrong]

Execute the plan step by step, marking each as done.
```

## Pitfalls

1. **Over-planning** — Agent creates 20-step plan for a 3-step task. Fix: constrain plan depth.
2. **Plan rigidity** — Agent follows a broken plan instead of adapting. Fix: include revision step.
3. **Missing dependencies** — Plan does not account for step ordering. Fix: require dependency analysis.
4. **Plan execution drift** — Agent starts improvising mid-plan. Fix: re-read plan before each step.

## Plan-and-Execute vs ReAct

| Aspect | Plan-and-Execute | ReAct |
|--------|-----------------|-------|
| Structure | Upfront plan | Emergent |
| Best for | Known tasks | Unknown tasks |
| Verification | Built-in | Ad-hoc |
| Cost | Higher (planning overhead) | Lower |
| Flexibility | Lower | Higher |

## Related Patterns
- [[react-pattern]] — when the path is not known
- [[orchestrator-workers]] — when steps can be parallelized
- [[reflection-pattern]] — verify plan results
