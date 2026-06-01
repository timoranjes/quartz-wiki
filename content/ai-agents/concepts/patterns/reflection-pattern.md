---
title: Reflection Pattern
created: 2026-05-29
updated: 2026-05-29
type: pattern
tags: [reasoning, evaluation]
sources: []
confidence: high
---

# Reflection Pattern

## Problem Solved

Agents make mistakes on first pass. Self-review catches errors, gaps, and improvements before the result reaches the user.

## How It Works

```
Generate: [initial output]
Reflect: What is wrong with this?
  - Does it meet all requirements?
  - Are there factual errors?
  - Is the formatting correct?
  - What is missing?
Revise: [improved output]
```

## Variants

### Single-Pass Reflection
Generate -> Self-critique -> Revise (one cycle)
- Good for: code review, writing polish
- Cost: ~2x tokens of single generation

### Multi-Pass Reflection
Generate -> Critique -> Revise -> Critique -> Revise (N cycles)
- Good for: high-stakes output, complex analysis
- Cost: Nx tokens. Diminishing returns after 2-3 passes.

### External Reflection
Agent A generates -> Agent B reviews -> Agent A revises
- Better than self-review (different perspective)
- More expensive (two agents)

## When to Use

- Code before committing (catch bugs, style issues)
- Analysis before presenting (check logic gaps)
- Writing before publishing (tone, accuracy, completeness)
- Any output where "good enough" is not good enough

## When NOT to Use

- Quick lookups (overhead > value)
- Low-stakes tasks
- When the agent already has a strong track record on that task type

## Reflection Prompt Template

```
Review the following output against these criteria:
1. Completeness: Does it address all parts of the request?
2. Accuracy: Are there factual errors?
3. Format: Does it match the requested structure?
4. Quality: Is it clear, concise, and correct?

For each criterion: PASS or FAIL + specific issue.

If any FAIL: revise the output to fix all issues.
If all PASS: confirm and return the output.
```

## Pitfalls

1. **Rubber-stamp reflection** — Agent says "looks good" without actually checking. Fix: require specific pass/fail per criterion.
2. **Over-correction** — Agent "fixes" things that are not broken. Fix: only revise FAIL items.
3. **Infinite loop** — Agent keeps finding new issues. Fix: max 2 revision cycles.
4. **Self-blindness** — Agent cannot see its own errors. Fix: use external reviewer for critical output.

## Related Patterns
- [[react-pattern]] — reflect after gathering information
- [[planning-pattern]] — reflect after executing plan
- [[orchestrator-workers]] — workers reflect before returning results
