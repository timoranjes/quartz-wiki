---
title: Prompt Chaining
created: 2026-05-29
updated: 2026-05-29
type: pattern
tags: [prompt-pattern, workflow]
sources: []
confidence: high
---

# Prompt Chaining

## Problem Solved

Complex tasks fail when crammed into a single prompt. Chaining breaks the task into focused steps, each handled by a separate agent call with a specific prompt.

## How It Works

```
Prompt 1: Extract data from this document
    -> Output: structured data

Prompt 2: Analyze this data for trends
    -> Output: trend analysis

Prompt 3: Write a report based on this analysis
    -> Output: final report
```

Each step has a narrow, well-defined prompt. The output of step N becomes the input of step N+1.

## When to Use

- Multi-step data processing (extract -> analyze -> report)
- When each step requires a different prompt style
- When you want to inspect/validate intermediate results
- When context would overflow in a single prompt

## When NOT to Use

- Tasks where steps are interdependent in complex ways (use ReAct)
- When latency matters (each chain step adds a round-trip)
- Simple tasks (overhead > value)

## Chain Design Principles

1. **Narrow prompts:** Each prompt should do ONE thing well.
2. **Structured I/O:** Pass structured data between steps, not free text.
3. **Validation gates:** Check each step's output before proceeding.
4. **Graceful degradation:** If step N fails, can you skip it or use a fallback?

## Example: Research Pipeline

```python
# Step 1: Search
results = web_search("AI agent benchmarks 2025")

# Step 2: Extract (focused on content only)
content = web_extract(urls=[r["url"] for r in results[:3]])

# Step 3: Synthesize (focused on analysis only)
synthesis = agent(
    prompt="Synthesize these articles into key findings about AI agent benchmarks",
    context=content
)

# Step 4: Format (focused on presentation only)
report = agent(
    prompt="Format these findings as a structured report with sections",
    context=synthesis
)
```

## Pitfalls

1. **Chain breakage** — Step N fails, steps N+1 cannot proceed. Fix: add error handling, fallback values.
2. **Information loss** — Each step loses some context from the original. Fix: pass original context as reference.
3. **Drift accumulation** — Small errors in early steps compound. Fix: validate at each gate.
4. **Over-chaining** — Too many steps creates latency and failure points. Fix: combine steps that share a prompt style.

## Chaining vs Single Prompt

| Aspect | Chaining | Single Prompt |
|--------|----------|--------------|
| Focus per step | High (narrow prompt) | Low (broad prompt) |
| Context usage | Efficient (per-step budget) | Inefficient (full context each turn) |
| Debugging | Easy (inspect each step) | Hard (one long trace) |
| Latency | Higher (N round-trips) | Lower (1 round-trip) |
| Reliability | Higher (each step validated) | Lower (all-or-nothing) |

## Related Patterns
- [[react-pattern]] — when steps are not known upfront
- [[planning-pattern]] — chain as a predefined plan
- [[orchestrator-workers]] — chain steps can be workers
