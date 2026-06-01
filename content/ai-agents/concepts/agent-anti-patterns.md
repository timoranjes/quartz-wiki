---
title: Agent Anti-Patterns
type: concept
category: AI Agents
created: 2026-05-29
tags: [anti-patterns, agent-design, debugging, best-practices]
sources: []
updated: 2026-05-29
confidence: high
---

# Agent Anti-Patterns

Common design mistakes that degrade agent performance, increase costs, or cause failures. Each pattern includes symptoms, root cause, fix, and a real-world example.

---

## 1. The Infinite Loop

Agents that retry the same action without learning from failures, burning through tokens until hitting rate limits or cost caps.

**Symptoms:** Agent repeats identical tool calls or reasoning steps. Logs show the same error message followed by the same attempted fix. Token usage spikes with no task progress.

**Root Cause:** Missing or incorrect failure feedback in the agent loop. The model doesn't receive structured error information that would let it change strategy. Common when tool errors are swallowed or returned as generic "try again" messages.

**Fix:**
- Return specific error context: what failed, why, and what constraints exist
- Implement retry budgets (max N attempts per action type)
- Add escalation paths: after N failures, ask the user or switch strategies
- Log each attempt with a dedup check to detect loops early

**Real-world example:** A trading data agent tries to fetch from a rate-limited API. Each retry returns a 429 error, but the agent's prompt only says "if the tool fails, try again." It loops 50 times, burning $12 in tokens before the parent process kills it. Fix: return the 429 status and retry-after header; the agent learns to wait or use cached data.

---

## 2. Context Stuffing

Dumping entire files, full conversation histories, or all available data into the context window "just in case."

**Symptoms:** Degraded reasoning quality as tasks get harder. Model ignores critical instructions buried in noise. Context window fills up quickly, truncating recent (important) information. Cost per task balloons.

**Root Cause:** Fear of missing relevant information. It's safer-seeming to include everything than to curate, but models pay an attention tax for every token in context. Retrieval quality drops linearly with context size.

**Fix:**
- Use retrieval-augmented patterns: fetch only what's needed when it's needed
- Implement context compression: summarize older conversation turns
- Set hard context budgets per agent type
- Use `patch_note`-style targeted reads instead of loading entire files

**Real-world example:** An agent loads a 200K-token codebase into context before answering a question about one function. The model's answer is vague and misses the relevant code section that's 180K tokens deep. Fix: use grep-like search to find the specific function, load only that file.

---

## 3. Tool Overprovisioning

Giving an agent 50 tools when it only needs 3 for the task at hand.

**Symptoms:** Tool selection becomes random or stuck on popular tools. The model spends reasoning tokens deciding which tool to use instead of solving the problem. Longer latencies as the model parses long tool schemas.

**Root Cause:** "More tools = more capable" assumption. In reality, each additional tool adds: (a) token cost in the system prompt, (b) decision complexity, (c) risk of hallucinated tool calls. Tool selection accuracy degrades past ~10-15 tools.

**Fix:**
- Profile tool usage: keep only tools actually called in the last N tasks
- Use tool groups: dynamically load tool sets based on task type
- Set hard limits: max 10 tools per agent session
- Regularly audit and remove unused tools

**Real-world example:** A research agent has 30 tools including web search, database query, file operations, email, calendar, and image generation. For a simple "summarize this PDF" task, it occasionally calls `send_email` or `generate_image` because those tools appear in its prompt. Fix: use a "document analysis" tool profile with only 4 relevant tools.

---

## 4. The Delegation Cascade

Sub-agents spawning their own sub-agents, which spawn more sub-agents, until the system runs out of memory or hits concurrent task limits.

**Symptoms:** Exponential growth in agent count. Memory usage climbs until OOM kills. Tasks that should take seconds take minutes as each layer adds overhead.

**Root Cause:** No depth limit on delegation. Each sub-agent independently decides whether to delegate further, creating a branching tree with no global coordination. Common when the delegation prompt doesn't include "do not delegate further" constraints.

**Fix:**
- Enforce maximum delegation depth (typically 2-3 levels)
- Require parent approval for sub-delegation
- Use task budgets: if a sub-task exceeds its budget, escalate instead of delegating
- Monitor active agent count and pause new delegations at thresholds

**Real-world example:** A market analysis agent delegates to a "sector analyst" sub-agent, which delegates to individual "stock analyst" sub-agents, each of which delegates to a "data fetcher" sub-agent. With 10 sectors and 50 stocks per sector, this creates 500+ concurrent agents on an 8GB Mac. Fix: the sector analyst handles all stocks directly; data fetching is a tool call, not a sub-agent.

---

## 5. Premature Complexity

Building multi-agent architectures with orchestrators, routers, and specialized agents when a single agent with good tools would suffice.

**Symptoms:** High infrastructure cost for simple tasks. Latency from inter-agent communication. Debugging becomes nearly impossible when failures propagate through multiple agents. Task completion rates don't justify the complexity.

**Root Cause:** Over-engineering based on blog posts about multi-agent systems rather than actual task requirements. The assumption that "specialized agents = better results" ignores the coordination overhead and context loss between agents.

**Fix:**
- Start single-agent; only split when a specific bottleneck is measured
- Use the "single agent + tools" pattern as the default architecture
- If splitting is needed, limit to 2-3 agents with clear responsibility boundaries
- Measure before and after: multi-agent should show >2x improvement to justify cost

**Real-world example:** A hedge fund builds a 5-agent pipeline for earnings analysis: data fetcher, sentiment analyzer, financial modeler, report writer, and quality checker. Each agent adds ~30s latency and $0.50 cost. A single agent with the same tools completes the task in 45s for $0.60 total. Fix: consolidate to one agent with well-structured tool calls.

---

## 6. Prompt Sprawl

System prompts that grow to thousands of tokens as new rules, exceptions, and edge cases are appended without removing contradictions or outdated instructions.

**Symptoms:** Agent behavior becomes unpredictable — it follows some instructions but ignores others. New rules conflict with old ones. Prompt tokens become a significant fraction of total cost. Adding new instructions has diminishing or negative impact.

**Root Cause:** Incremental prompt growth without maintenance. Every bug fix or edge case adds a new paragraph. Over time, the prompt contains contradictory instructions (e.g., "always verify data" vs. "minimize API calls for speed").

**Fix:**
- Regular prompt audits: remove contradictions, consolidate overlapping rules
- Use structured prompts with priority levels (must/should/may)
- Move edge cases to tool behavior rather than prompt instructions
- Version control prompts and A/B test changes
- Set a prompt token budget (e.g., max 2K tokens for system prompt)

**Real-world example:** An agent's system prompt grew from 500 to 4,200 tokens over 3 months. It contains "always double-check calculations" and "respond within 10 seconds" — contradictory under load. The model sometimes follows one, sometimes the other, never both. Fix: audit and consolidate to 1,200 tokens with clear priority hierarchy.

---

## 7. Cost Blindness

Running agents without tracking token consumption, leading to unexpected bills and inability to optimize cost-per-task.

**Symptoms:** Monthly API bills are surprises. No visibility into which tasks or agents are the most expensive. Can't calculate ROI on agent automation. Cost per task is unknown.

**Root Cause:** No instrumentation for token tracking. Agents run without logging input/output token counts. Different models have different pricing, but costs aren't attributed to specific tasks.

**Fix:**
- Log token counts (input, output, cached) for every agent call
- Tag costs by task type, agent, and model
- Set budget alerts at 50%, 80%, and 100% of daily/monthly limits
- Calculate cost-per-task and compare against manual alternatives
- For M2 Macs with 8GB RAM, also monitor local model memory usage

**Real-world example:** A team runs 3 agents 24/7 for monitoring. After a month, the DashScope bill is $340 — 4x expected. Investigation reveals one agent was stuck in a loop (Anti-Pattern #1) for 3 days, consuming 80% of tokens. Fix: implement cost tracking with alerts; the loop would have been caught within hours.

---

## Related Concepts

- [[evaluation-benchmarks]]
- [[model-selection-for-agents]]
- [[architectures]]
