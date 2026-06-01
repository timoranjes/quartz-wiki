---
title: Debugging Agents
created: 2026-05-29
updated: 2026-05-30
type: concept
tags: [debugging, error-handling]
sources: [raw/papers/unknown-diagnosing-live-within-policy-instruction-conflicts-in-llm-agents-with-witnessed.md, raw/papers/unknown-when-context-flips-safety-breaks-diagnosing-brittle-safety-in-aligned-language-m.md, raw/articles/unknown-captchas-can-still-detect-ai-agents.md]
confidence: high
---

# Debugging Agents

## Common Failure Modes

### 1. Tool Misuse
**Symptom:** Agent calls the wrong tool, or calls the right tool with wrong arguments.
**Root cause:** Agent does not understand the tool's purpose or parameter schema.
**Fix:**
- Add tool description to system prompt
- Use fewer tools (confusion increases with tool count)
- Validate tool arguments before execution (if possible)

### 2. Context Overflow
**Symptom:** Agent "forgets" earlier instructions, repeats tool calls, or produces garbled output.
**Root cause:** Context window full of tool outputs and reasoning traces.
**Fix:**
- Summarize intermediate results
- Compact the conversation (remove old tool outputs)
- Use subagents to isolate context

### 3. Model Confusion
**Symptom:** Agent seems to reason in circles, contradict itself, or produce nonsensical output.
**Root cause:** Task is beyond the model's capability for this domain.
**Fix:**
- Switch to a stronger model
- Break the task into simpler subtasks
- Add more specific instructions/examples

### 4. Tool Output Overload
**Symptom:** Agent gets stuck processing a huge tool output (e.g., reading a 10K-line file).
**Root cause:** No filtering or pagination on tool output.
**Fix:**
- Use `limit` parameters on read operations
- Pre-filter results before agent sees them
- Use targeted search instead of full-file reads

### 5. Silent Failure
**Symptom:** Agent reports "done" but nothing changed.
**Root cause:** Tool call succeeded but had no effect (e.g., writing to wrong path).
**Fix:**
- Require verification step after every action
- Use reflection pattern: "Did the action actually work?"
- Check the actual state after tool execution

### 6. Infinite Loop
**Symptom:** Agent keeps calling the same tool with the same arguments.
**Root cause:** Agent does not recognize that the tool output did not change the state.
**Fix:**
- Add loop detection: "Have you tried this before? If so, try something different."
- Limit maximum iterations
- Use a different approach entirely

### 7. Policy Conflict (Hidden Instruction Contradictions)
**Symptom:** Agent violates one of its own rules in specific situations, seemingly at random.
**Root cause:** Two or more standing rules in the system prompt can co-govern a realistic state and produce contradictory requirements. Research found 64.6% of hard-collision candidates violate at least one rule; only 35.4% achieve joint compliance.
**Fix:**
- Audit system prompt for rule pairs that could conflict in edge cases
- Use priority labels (must/should/may) to resolve conflicts explicitly
- Test with concrete scenarios where rules might collide
- Keep system prompts short — every additional rule increases collision risk exponentially

### 8. Brittle Safety (Context-Flip Failures)
**Symptom:** Agent follows a safety rule even when the situation has flipped and following it would cause harm.
**Root cause:** Model prioritizes rigid rule adherence over situational awareness. Failures stem from policy override, not miscomprehension — the model understands the context change but persists with the wrong rule.
**Fix:**
- Use state-aware validation, not action-level content moderation
- Train agents to check "what would happen if I follow this rule right now?"
- Don't rely on benchmark safety scores — they don't predict brittleness (among models above 90% baseline accuracy, brittleness rates range from 13.7% to 90.0%)

### 9. CAPTCHA / Bot Detection
**Symptom:** Agent's web browsing fails when encountering CAPTCHAs, Cloudflare challenges, or bot-detection systems. The agent cannot proceed past the verification page.
**Root cause:** CAPTCHAs are explicitly designed to distinguish humans from automated agents. Modern CAPTCHA systems (reCAPTCHA v3, hCaptcha, Cloudflare Turnstile) analyze behavioral signals (mouse movement, timing, browser fingerprint) that agents cannot replicate. Research (2026-05) shows CAPTCHAs remain effective at detecting AI agents even as models improve.
**Fix:**
- Use browser-based tools with human-in-the-loop for CAPTCHA resolution
- Pre-filter URLs to avoid known CAPTCHA-protected sites
- Use alternative data sources (APIs, cached versions, RSS feeds) when web browsing is blocked
- Consider headless browser fingerprinting mitigation (limited effectiveness against modern systems)

## Debugging Workflow

```
1. Identify the symptom (what looks wrong?)
2. Check the tool trace (what did the agent actually call?)
3. Check the context (is it full? are there duplicate tool outputs?)
4. Check the model (is this the right model for this task?)
5. Check the prompt (is the instruction clear and specific?)
```

## Debugging Checklist

- [ ] Is the agent using the right tools?
- [ ] Are tool arguments correct?
- [ ] Is context window full?
- [ ] Is the model capable enough for this task?
- [ ] Is the system prompt clear and specific?
- [ ] Are there conflicting instructions?
- [ ] Is the task too complex for a single agent?
- [ ] Are tool outputs being filtered appropriately?

## Related Concepts
- [[architectures]] — Relevant architecture patterns for debugging multi-agent systems
- [[react-pattern]] — debugging the ReAct loop
- [[reflection-pattern]] — self-diagnosis
- [[cost-optimization]] — reducing wasted tokens from retries
- [[agent-safety]] — policy conflicts and brittle safety as debugging targets
