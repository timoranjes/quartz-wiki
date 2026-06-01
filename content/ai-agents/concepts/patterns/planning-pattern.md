---
title: Planning Pattern
created: 2026-05-29
updated: 2026-06-02
type: pattern
tags: [planning, agent-architecture]
sources: [raw/papers/unknown-planner-centric-reinforcement-learning-for-deep-research-with-structure-aware-re.md, raw/papers/unknown-lintree-improving-llm-reasoning-with-explicitly-structured-search-histories.md]
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

## Planner-Centric RL (DecomposeR)

**DecomposeR** (2026-05) introduces a planner-centric deep research framework that represents research plans as typed directed acyclic graphs (DAGs), enabling explicit, structured, and rewardable planning.

**Key findings:**
- **DAG-structured planning:** Research plans as typed DAGs allow planning to be explicit and rewardable, rather than buried in monolithic trajectories
- **Two-stage RL:** First, planner RL learns graph structure and query decomposition. Then, answerer RL learns branch-level execution and synthesis conditioned on the plan
- **Structured rewards:** Assigning rewards to explicit planner tokens and structured components enables finer-grained optimization than flat trajectory rewards
- **Result:** DecomposeR-8B improves over comparable open baselines by 5.1-8.0 points on long-form benchmarks
- **Implication:** Explicit plan structure (not just "make a plan") enables better credit assignment and training signal

**For agent users:** When agents perform deep research or multi-branch investigation:
- Structure the plan as a DAG with typed nodes (not just a numbered list)
- Separate planning from execution with clear handoff points
- Evaluate plan quality separately from execution quality

## Explicit Search History Structure (LinTree)

**LinTree** (2026-05) shows that LLMs' ability to utilize search history depends on making the underlying tree structure explicit.

**Key findings:**
- Raw access to search history alone is NOT enough to reliably outperform heuristic search
- In LLM reasoning traces, the underlying search tree is only implicitly represented — when the model backtracks, the trace doesn't explicitly identify which earlier state is being revisited
- Adding simple parent pointers to explicitly represent the linearized tree structure improves both task performance and search efficiency
- **Implication:** When agents backtrack or branch, explicitly mark which prior state they're returning to

**For agent users:** When prompting agents that explore alternatives:
- Don't just let the agent "go back and try again" — explicitly reference which branch/decision point
- Use structured markers: "Returning to Step 2, alternative B" vs "Let me try something else"
- Structured search history improves both reasoning quality and efficiency

## Related Patterns
- [[react-pattern]] — when the path is not known
- [[orchestrator-workers]] — when steps can be parallelized
- [[reflection-pattern]] — verify plan results
