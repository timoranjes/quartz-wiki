---
title: Personal Workflow Lessons
type: concept
category: personal-workflow
created: 2026-05-29
updated: 2026-06-01
tags: [personal, workflow, hermes, lessons-learned]
sources: [raw/articles/2026-05-31-the-solution-might-be-cancelling-my-ai-subscription.md]
confidence: high
---

# Personal Workflow Lessons

Lessons learned from actual agent usage. These capture what worked, what failed, and how to avoid repeating mistakes.

## 1. Orchestrator Profile Lockdown

**Lesson:** Orchestrator profiles must be technically restricted, not just instructed.

**What happened:** Orchestrators spawned with full tool access kept escaping into terminal/file work instead of delegating. SOUL.md rules alone were insufficient — the agent always found a way to "just this once" use a tool directly.

**Fix:** Use `disabled_toolsets` in profile config to mathematically remove terminal, file, code_execution, browser, web, and image_gen. Only kanban, skills, clarify, delegation, messaging, session_search, and todo remain.

**Rule:** If the orchestrator has `terminal` available, it WILL eventually use it. No exceptions.

## 2. RAM Management on M2 Air (8GB)

**Lesson:** GPU-intensive operations must be guarded by explicit RAM checks.

**What happened:** Browser processes (Chrome, Firefox, Safari) opened during sessions accumulated RAM silently. Gateway OOM crashes occurred when RAM dropped below 60MB. GPU deadlock occurred below 100MB available VRAM.

**Fixes:**
- Kill all browser processes at session end (mandatory)
- Set Reduce Motion ON in macOS to reduce GPU load
- Check RAM before any GPU-intensive operation: `memory_pressure` CLI
- Restart GPU services when available memory < 100MB
- Gateway threshold: restart if < 60MB free

**Rule:** Never assume RAM will be available. Always check before expensive operations.

## 3. Model Routing by Evidence, Not Marketing

**Lesson:** Route tasks based on benchmark evidence for specific capabilities, not overall model rankings.

**What happened:** Initially routed all coding to the highest-ranked model overall. Better results came from matching specific strengths: coding models for code work, reasoning models for analysis.

**Current routing (Alibaba DashScope):**
- **Coding tasks** → `MiniMax-M2.5` (80.2 SWE-bench, highest coding score)
- **Review/analysis** → `glm-5` (83.1 Knowledge, 91.3 Math)
- **Research/browsing** → `qwen3.6-plus` (69.6 Agentic, 1M context)

**Rule:** Use Artificial Analysis and other benchmarks for role-specific evidence. Don't trust overall "intelligence" rankings for specialized tasks.

## 4. Dirty Worktrees Are Contagious

**Lesson:** Never mix new fixes into repos with unrelated local modifications.

**What happened:** Made scoped changes to a repo that had unrelated work in progress. Git status showed mixed changes. Commits became noisy and hard to review.

**Fix:**
1. Always run `git status` before any file changes
2. If unrelated modifications exist: isolate your files, commit only scoped changes
3. Or stash unrelated work with verification (`git stash && git stash list`)
4. Or use a clean worktree/clone for the fix

**Rule:** `git status` before every write. Always.

## 5. Credential Verification Before Claiming Blockers

**Lesson:** Never claim "no credentials," "API doesn't support X," or "not configured" without running the actual verification command.

**What happened:** Assumed keys didn't exist because a tool call failed. Later discovered the keys were in `.env` but with slightly different naming conventions.

**Fix:** Before claiming any blocker:
```bash
grep -i '<KEY_PATTERN>' ~/.hermes/.env
```
The `.env` has 60+ keys — most standard provider keys already exist. Don't fabricate blockers from inference.

**Rule:** Execute the check. Report real results. Never assume absence.

## 6. Incremental Patches Corrupt State

**Lesson:** When patching single-file HTML, prefer resetting to git base and rebuilding clean.

**What happened:** Multiple incremental patches on a single-file HTML demo accumulated corrupted state. CSS rules conflicted, JavaScript broke, and the file became unmaintainable.

**Fix:** After 2+ incremental patches on the same file, reset to base and rebuild from scratch. The rebuild is faster and more reliable than debugging accumulated patch artifacts.

**Rule:** Patch threshold = 2. After that, rebuild.

## 7. Subagent-Driven Development for Complex Tasks

**Lesson:** Massive SE tasks should be decomposed algorithmically into 2-5 minute components, not handled in a single conversation.

**What works:**
1. Decompose into atomic tasks (each completable in 2-5 minutes)
2. Fresh subagent per task with isolated context
3. Two-stage review: (1) Spec Compliance, (2) Code Quality (TDD)
4. Final integration review after all tasks pass

**What doesn't work:**
- Single agent handling 20+ steps
- Tasks without explicit review gates
- Skipping spec verification

**Rule:** If a task needs more than 5 tool calls, decompose.

## 8. Cron Delivery Discipline

**Lesson:** Cron alerts must go to explicit channels, never `origin` (current thread).

**What happened:** System-level cron alerts were delivered to random Discord threads, mixing operational noise with ongoing conversations.

**Fix:** All cron deliveries use explicit channel targeting:
- `#hermes` for system-level alerts
- `#portfolio-alerts` for market alerts
- `#ai-supply-chain-wiki` for wiki updates

**Rule:** Cron → explicit channel. Never `origin`.

## 9. Memory vs Skill vs Session

**Lesson:** Different types of information belong in different storage systems.

| Type | Storage | Why |
|------|---------|-----|
| User preferences, environment facts, tool quirks | **Memory** | Persistent, injected every turn |
| Workflows, procedures, complex task patterns | **Skills** | Reusable, loadable on demand |
| Session outcomes, PR numbers, task status | **Session Search** | Temporary, discoverable later |
| Portfolio state, mapping configs | **Files** | Structured data, not memory |

**Common mistake:** Saving PR numbers, commit SHAs, or "Phase N done" to memory. These become stale in days and pollute future sessions.

**Rule:** Memory = facts that matter in 30+ days. Everything else goes elsewhere.

---

## 10. AI Project Sprawl and Discipline

**Lesson:** Coding agents make it trivially easy to spin up fully-formed projects from vague ideas — and equally easy to abandon them. Manage this deliberately or waste hours.

**What happened:** Simon Willison and David Wilson independently noted the same pattern: start a Claude session to "write a quick script for X", and one hour later you have a project with tests, docs, and structure that looks like weeks of careful evolution. But it's abandoned. The original itch was never scratched.

**Key insights:**
- Coding agents are a "thermonuclear ADHD amplifier" — low friction + cheap rewards = compulsive project creation
- The limit isn't creation speed, it's how many projects you can sensibly maintain
- **Counter-perspective:** Some ADHD users report the opposite — agents help them *finish* projects for the first time because they can get things working before boredom hits
- The HN thread suggests the critical skill here is *discipline*, not tool restriction

**Fix strategies:**
- Set a project completion quota before starting new sessions
- When a session starts producing "interesting but unrelated" tangents, note them and return to the original task
- Delete abandoned projects within 48 hours — don't let them accumulate as guilt-inducing clutter
- If the pattern is compulsive (not just productive), the fix may be curtailing usage entirely

**Rule:** If you can't commit to maintaining it, don't create it. The agent's enthusiasm for building is not your enthusiasm for maintaining.

---

## Related
- [[hermes-agent]] — Primary agent framework
- [[cost-optimization]] — Token cost strategies
- [[debugging-agents]] — Failure modes and fixes
- [[single-vs-multi-agent]] — Delegation decision matrix
