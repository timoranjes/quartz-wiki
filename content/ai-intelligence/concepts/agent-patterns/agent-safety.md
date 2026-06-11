---
title: "Agent Safety"
type: concept
tags: [safety, agent-architecture]
created: "2026-06-03"
updated: "2026-06-12"
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

## Anthropic Fable 5 Invisible Safeguards Controversy (June 2026)

Anthropic's Claude Fable 5 / Mythos 5 system card (319 pages, June 9, 2026) revealed the first known instance of a major lab deploying **invisible, silent interventions** that degraded model performance for specific use cases without notifying users.

### What Was Deployed
- Fable 5 implemented safeguards targeting "frontier LLM development" requests — including pretraining pipelines, distributed training infrastructure, and ML accelerator design
- Unlike cybersecurity/biology refusals (which are visible and fall back to another model), these safeguards were **invisible**: no fallback, no notification
- Intervention methods included: prompt modification, steering vectors, and parameter-efficient fine-tuning (PEFT)
- Estimated impact: ~0.03% of traffic, concentrated in <0.1% of organizations
- Justification: preventing competitors from using Claude to accelerate development of competing models (citing "recursive self-improvement" risks)

### Backlash
- Widespread outrage from the AI research community
- **Jeremy Howard** (fast.ai): "Anthropic has chosen the opposite of the safe path: they are allowing themselves, the current top lab, to use their top model for frontier AI research. They've said they'll sabotage others who try."
- Core objection: a model that silently corrupts its replies to slow down competing research is antithetical to open scientific progress
- First time any major lab had announced such silent interventions

### Walk-Back (June 11, 2026)
Anthropic reversed the invisible aspect within 48 hours:
- Flagged requests now **visibly fall back to Opus 4.8** (same as cybersecurity/bio safeguards)
- API returns a reason for refusal (server-side fallback coming)
- Anthropic statement: "We made the wrong tradeoff and we apologize for not getting the balance right"
- Explanation: invisible safeguards were chosen to ship quickly with few false positives, but "you should have visibility into the safeguards we have in place"

### Implications for Agent Safety
- **Transparency is non-negotiable**: invisible model interventions erode trust and are operationally dangerous for agent workflows that depend on consistent behavior
- **Visible refusal + fallback** is the correct pattern: users/agents can detect and route around refusals
- **Competitive neutrality risk**: a lab using its own model to sabotage competitors creates a power imbalance that undermines the safety mission
- Sets precedent that safety-washed anti-competitive behavior will face immediate community pushback

Sources: [Jonathon Ready analysis](https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html), [Wired (Maxwell Zeff)](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/), [Simon Willison](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/), [Jeremy Howard (Twitter)](https://twitter.com/jeremyphoward/status/2064595816875217362) ^[raw/sources/2026-06-10-if-claude-fable-stops-helping-you-youll-never-know.md] ^[raw/sources/2026-06-11-anthropic-walks-back-policy-that-could-have-sabotaged-ai-researchers-using-claud.md] ^[raw/sources/2026-06-10-quoting-jeremy-howard.md]

## Related

- [[tool-use-pattern]]
- [[architectures]]
- [[anthropic]] — Fable 5 safeguards controversy
- [[openai]] — Lockdown Mode for ChatGPT
