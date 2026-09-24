> Migrated from the retired `wiki-ai-agents` site (May 2026 generation). Kept as the classic reference alongside the June 2026 research updates.

---
title: Prompt Chaining
created: 2026-05-28
updated: '2026-05-28'
type: concept
tags:
- prompt-chaining
- multi-step
- architecture
sources: [https://arxiv.org/abs/2205.11916, https://langchain-ai.github.io/langgraph/]
confidence: high
---

# Prompt Chaining

## Definition

**Prompt chaining** is the pattern of connecting multiple LLM calls in sequence,
where each call's output becomes the next call's input. Instead of a single monolithic
prompt attempting to solve a complex task end-to-end, prompt chaining decomposes the
task into smaller, focused steps — each with its own prompt optimized for that specific
subtask.

Prompt chaining is one of the most fundamental multi-step patterns. It underlies more
complex patterns like [[concepts/agent-patterns/react-pattern-classic|react-pattern]] (which adds tool use between steps) and
[[concepts/agent-patterns/reflection-pattern-classic|reflection-pattern]] (which adds a critique step).

## How It Works

A prompt chain consists of:

1. **Step 1** — Initial prompt processes raw input and produces intermediate output
2. **Step 2** — Receives Step 1's output, performs a different transformation
3. **Step N** — Final step produces the end result

Each step is independently prompt-engineered, allowing:
- **Specialization** — Each prompt is optimized for its specific subtask
- **Isolation** — Errors in one step don't cascade in the same way as a single complex prompt
- **Composability** — Steps can be reused across different chains

### Common Chain Patterns

- **Decompose → Solve → Aggregate** — Break a problem into subproblems, solve each,
  combine results
- **Extract → Transform → Format** — Extract entities, transform/normalize them,
  format for output
- **Draft → Critique → Revise** — Generate initial output, evaluate it, improve it
  (this is the [[concepts/agent-patterns/reflection-pattern-classic|reflection-pattern]])
- **Classify → Route → Execute** — Determine the task type, select the handler,
  execute the specialized prompt

## When to Use

**Best suited for:**
- Tasks that are too complex for a single prompt to handle reliably
- Workflows where intermediate outputs are useful on their own
- Scenarios requiring different model capabilities at different stages
- Multi-language or multi-format transformations

**Trade-offs:**
- **Latency** — Each step adds an LLM call, multiplying total response time
- **Error propagation** — A mistake in an early step cascades through all subsequent steps
- **Token cost** — Intermediate outputs consume tokens in subsequent prompts
- **Debugging complexity** — Harder to diagnose which step failed compared to a single prompt

## Comparison with Related Patterns

| Pattern | Structure | Tool Use | Feedback Loop |
|---------|-----------|----------|---------------|
| Prompt chaining | Linear sequence | No | No |
| [[concepts/agent-patterns/react-pattern-classic|react-pattern]] | Thought → Action → Observation | Yes | No |
| [[concepts/agent-patterns/reflection-pattern-classic|reflection-pattern]] | Generate → Critique → Revise | Optional | Yes |
| [[concepts/agent-patterns/planning-pattern-classic|planning-pattern]] | Plan → Execute → Replan | Yes | Yes |
| [[concepts/agent-patterns/routing-classic|routing]] | Classify → Delegate | Optional | No |

## Framework Support

- [[langchain]] offers `LCEL` (LangChain Expression Language) for composing chains
  with `|` operator: `prompt | model | output_parser`
- [[langgraph]] models chains as linear graphs with explicit state passing between nodes
- [[openai-agents-sdk]] supports chains through its agent loop with custom step functions
- [[crewai]] implements chains through sequential task execution within a crew

## Related Concepts

[[concepts/agent-patterns/react-pattern-classic|react-pattern]], [[concepts/agent-patterns/reflection-pattern-classic|reflection-pattern]], [[concepts/agent-patterns/planning-pattern-classic|planning-pattern]], [[concepts/agent-patterns/routing-classic|routing]],
[[tool-use-pattern]]

## Sources

- Chain-of-Thought prompting research (Wei et al.)
- LangChain LCEL documentation
- LangGraph state machine patterns
