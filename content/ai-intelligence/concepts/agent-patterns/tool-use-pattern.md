---
title: "Tool Use Pattern"
type: concept
tags: [tool-use, agent-architecture]
created: "2026-06-03"
updated: "2026-06-03"
status: seed
---

# Tool Use Pattern

## Overview

Tool use (function calling) is the primary mechanism by which agents interact with the external world — APIs, filesystems, browsers, databases.

## Tool Lifecycle

1. **Discovery** — Agent learns available tools from schema
2. **Selection** — Agent chooses the right tool for the current step
3. **Execution** — Tool runs and returns structured output
4. **Integration** — Agent incorporates the result into its reasoning

## Best Practices

- **Typed schemas** — Use JSON Schema with descriptions, not just function names
- **Error handling** — Tools should return structured errors, not throw
- **Idempotency** — Prefer idempotent tools to avoid side effects on retry
- **Rate limits** — Track tool call budgets per session
- **Timeouts** — Every tool call needs a timeout

## Common Tool Categories

| Category | Examples |
|----------|----------|
| Web | search, scrape, browser automation |
| Code | execute, debug, lint |
| Data | query, read_file, write_file |
| Communication | send_message, email |
| Analysis | chart, summarize, compare |

## Related

- [[architectures]]
- [[agent-safety]]
