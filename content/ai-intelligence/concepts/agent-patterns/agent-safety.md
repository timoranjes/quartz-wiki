---
title: "Agent Safety"
type: concept
tags: [safety, agent-architecture]
created: "2026-06-03"
updated: "2026-06-08"
status: seed
---

# Agent Safety

## Overview

Agent safety ensures that autonomous AI systems operate within defined boundaries and don't cause unintended harm.

## Threat Model

| Risk | Example | Mitigation |
|------|---------|------------|
| Unbounded tool use | Agent deletes files it shouldn't | File-level permissions, allowlists |
| Infinite loops | Agent gets stuck in retry cycle | Step budget, timeout |
| Data exfiltration | Agent sends secrets to external APIs | Output filtering, DLP |
| Prompt injection | Malicious input hijacks agent behavior | Input sanitization, sandboxing |
| Hallucinated actions | Agent calls wrong tool with wrong args | Schema validation, pre-flight checks |

## Defense Layers

1. **Input validation** — Sanitize user inputs before agent sees them
2. **Tool guards** — Permission checks on every tool call
3. **Step limits** — Max iterations per task
4. **Output filtering** — Review agent outputs before delivery
5. **Audit logging** — Every action is recorded

## Production Rules

- Never let agents execute destructive commands without confirmation
- Always sandbox file system access
- Rate limit API calls
- Log every tool call with arguments and results


## OpenAI Lockdown Mode (June 2026)

OpenAI introduced **Lockdown Mode** for ChatGPT to prevent data exfiltration from prompt injection attacks.

### What It Does
- Limits outbound network requests that could transfer sensitive data to attackers
- Uses deterministic mechanisms (not evaluated by AI systems) to prevent subversion
- Rolling out to eligible personal accounts (Free, Go, Plus, Pro) and self-serve ChatGPT Business

### What It Does NOT Do
- Does NOT prevent prompt injections from appearing in content ChatGPT processes
- Injections could still affect behavior or accuracy of responses
- Only blocks the exfiltration vector, not the injection itself

### The "Lethal Trifecta"
Prompt injection attacks succeed when three conditions are met:
1. **Access to private data** — LLM can read user's files, emails, etc.
2. **Exposure to untrusted content** — LLM processes web content, uploaded files, etc.
3. **Exfiltration vector** — LLM can send data back to the attacker

Lockdown Mode cuts off leg #3 (exfiltration), which is the easiest to restrict without reducing utility.

### Trade-offs
- Functionality and utility are reduced in Lockdown Mode
- Designed for users with elevated risk profiles (sensitive work, high-value targets)
- Implies that default ChatGPT does NOT provide robust protection against determined exfiltration attacks

Source: [OpenAI Help: Lockdown Mode](https://help.openai.com/en/articles/20001061-lockdown-mode) via Simon Willison

## Related

- [[tool-use-pattern]]
- [[architectures]]
