---
title: Tool Use Patterns
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [tool-use, pattern, agent-architecture]
sources: []
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

## Related Concepts

- [[agent-anti-patterns]] — Tool Overprovisioning: giving agents too many tools
- [[debugging-agents]] — Common tool failure modes and recovery strategies
- [[mcp-protocol]] — Standardized tool interface for agent-tool communication
