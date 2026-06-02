---
title: Tool Use Patterns
created: 2026-05-29
updated: 2026-06-03
type: concept
tags: [tool-use, pattern, agent-architecture]
sources: [raw/papers/unknown-maven-improving-generalization-in-agentic-tool-calling.md, raw/papers/unknown-atomix-timely-transactional-tool-use-for-reliable-agentic-workflows.md]
confidence: high
---

# Tool Use Patterns

Tool use patterns describe how agents select, invoke, and recover from tool calls. Effective tool use is what separates capable agents from chat-only models.

---

## Definition

Tool use patterns encompass the strategies agents employ to interact with external tools — APIs, file systems, terminals, browsers, and other services. These patterns determine how agents discover available tools, decide when to use them, handle errors, and chain multiple tool calls.

---

## Core Patterns

### Direct Tool Call
The agent selects a tool from its available set and invokes it with specific parameters. This is the simplest pattern — used by most modern agent frameworks.

### Tool Chaining
The agent calls multiple tools in sequence, using the output of one as input to the next. Requires careful error handling at each step.

### Tool Discovery
The agent searches for the right tool before using it — e.g., searching a codebase before editing, or searching the web before summarizing. This pattern reduces hallucinated tool calls.

### Fallback Chain
When a primary tool fails, the agent tries alternatives. Example: `web_extract` fails → fall back to `browser_navigate`.

---

## Common Pitfalls

- **Tool overprovisioning**: Too many tools degrade selection accuracy (see [[agent-anti-patterns]])
- **Missing error context**: Generic "tool failed" messages prevent the agent from adapting
- **Output truncation**: Tools that return massive outputs can overflow context windows
- **Stateful tools**: Tools that modify shared state require careful coordination in multi-agent scenarios

---

## Best Practices

- Limit active tools to 10-15 per agent session
- Return specific error context (status codes, error messages, constraints)
- Set output size limits and implement pagination for large results
- Use tool profiles — dynamically load tool sets based on task type

---

## Verification-Centered Tool Orchestration (MAVEN)

**MAVEN** (Modular Agentic Verification and Execution Network, 2026-05) introduces a lightweight symbolic reasoning scaffold for structured decomposition, adaptive tool orchestration, and intermediate verification.

**Key findings:**
- **Verification gap:** There is a substantial gap between partial reasoning quality and end-to-end task success in multi-step tool-calling tasks
- **Lightweight verification scaffold:** MAVEN improves GPT-OSS-120b from 48% to 71% accuracy on MAVEN-Bench (multi-step mathematical/physical reasoning with adversarial task composition) without additional training
- **Cost efficiency:** Competitive with frontier proprietary baselines while using an open-weight backbone at ~1/10 the cost
- **Implication:** Adding explicit verification steps between tool calls is more effective than scaling model size for complex tool-calling workflows

**For agent users:** When building agents that chain multiple tool calls, insert explicit verification checkpoints between steps rather than relying on the model to "get it right" in one pass.

---

## Transactional Tool Use (Atomix)

**Atomix** (arXiv 2602.14849, 2026-06) addresses a critical gap in agentic tool execution: **fault isolation and clean recovery** when LLM agents execute multi-step workflows that mutate external state through tools.

**Problem:** Common orchestrators treat tool return as the settlement trigger, so faults, speculation, and concurrent agents can leave partial effects — losing-branch residue, stale writes, or irreversible sends. Retries, checkpoint replay, locks, and compensation each conflate two separate concerns: (1) which effects must settle together, and (2) when earlier conflicting work is exhausted.

**Atomix solution — progress-aware transactions:**
- **Record phase:** Runtime records reads and effects during execution
- **Seal phase:** Transaction seals when its footprint is complete
- **Commit phase:** Commits only after per-resource frontiers show no earlier conflicting work can still arrive
- **Abort phase:** Suppresses unreleased effects, compensates externalized reversible effects where possible

**Key properties:**
- Commit is **final settlement**: releases bufferable effects, accepts reversible external effects as final, lets irreversible effects leave the gate
- Abort **suppresses** unreleased effects and compensates reversible ones
- Microsecond-scale wrapper overhead relative to tool latency

**For agent users building reliable workflows:**
- When your agents perform multi-step tool operations that modify state (file writes, database updates, API calls), consider transactional semantics rather than simple retry loops
- Separate "what should settle together" from "when is it safe to commit" — conflating these is the root cause of many agent workflow bugs
- Irreversible actions (sending emails, executing trades) need special handling — Atomix's gate mechanism prevents correctly classified irreversible actions from leaking during abort

[[debugging-agents]] — transactional semantics prevent partial-state corruption from being a debugging nightmare
[[multi-agent-orchestration]] — Atomix isolates contending and speculative work across concurrent agents

---

## Related Concepts

- [[agent-anti-patterns]] — Tool Overprovisioning: giving agents too many tools
- [[debugging-agents]] — Common tool failure modes and recovery strategies
- [[mcp-protocol]] — Standardized tool interface for agent-tool communication
