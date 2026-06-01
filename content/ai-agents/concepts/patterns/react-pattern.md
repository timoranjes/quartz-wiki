---
title: ReAct Pattern
created: 2026-05-29
updated: 2026-05-29
type: pattern
tags: [agent-architecture, reasoning, tool-use]
sources: []
confidence: high
---

# ReAct Pattern

## Problem Solved

How to make an agent alternate between reasoning about a problem and taking action to gather information, rather than just guessing or just acting blindly.

## How It Works

```
Thought: I need to find X. Let me search for it.
Action: search_files("X")
Observation: Found 3 files mentioning X
Thought: The most relevant is file A. Let me read it.
Action: read_file("file_a")
Observation: [file content]
Thought: Now I understand X. The answer is...
```

The loop continues until the agent has enough information to answer.

## When to Use

- Tasks requiring information gathering
- Tool use with 2-5 steps
- When the path to the answer is not known upfront
- Debugging: agent investigates root cause

## When NOT to Use

- Tasks where the steps are already known (use Plan-and-Execute)
- Very long chains (context window fills up)
- When you need parallel work (use Orchestrator-Workers)

## Prompt Template

```
You are a careful investigator. For each step:
1. Think about what you know and what you need
2. Take ONE action to gather information
3. Observe the result
4. Repeat until you have enough information

Format each step as:
Thought: [what you know + what you need]
Action: [tool call]
Observation: [tool result]
```

## Pitfalls

1. **Thought bloat** — Agent writes paragraphs of reasoning instead of concise thoughts. Fix: enforce brevity in system prompt.
2. **Action looping** — Agent repeats the same tool call. Fix: track previous actions in context.
3. **Observation overload** — Tool returns too much data. Fix: use targeted queries, pagination.
4. **Giving up too early** — Agent stops after one failed tool call. Fix: encourage retry with different approach.

## Related Patterns
- [[planning-pattern]] — when you need structure before action
- [[reflection-pattern]] — when you need to verify the answer
- [[prompt-chaining]] — when steps should be separated
