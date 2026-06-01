---
title: Agent Evaluation Benchmarks
type: concept
category: AI Agents
created: 2026-05-29
tags: [evaluation, benchmarks, agent-selection, SWE-bench, LiveCodeBench]
sources: [raw/papers/unknown-tracegraph-shared-decision-landscapes-for-diagnosing-and-improving-agent-traject.md]
updated: 2026-06-02
confidence: high
---

# Agent Evaluation Benchmarks

Evaluation benchmarks provide standardized measures for comparing AI agent capabilities. Understanding what each benchmark measures — and what it doesn't — is critical for selecting the right model for a given task.

---

## SWE-bench / SWE-bench Verified

**What it measures:** Ability to resolve real GitHub issues — read a codebase, understand a bug report or feature request, and produce a working patch that passes the repository's test suite.

**Why it matters for agent selection:** This is the closest publicly available proxy to "can this agent do real software engineering work?" It tests multi-file reasoning, test comprehension, and codebase navigation — the exact skills needed for coding agents in production. SWE-bench Verified is a curated subset with confirmed issue reproducibility, reducing noise from flaky tests.

**Known issues:** 
- **Contamination:** Popular models may have seen benchmark repos in training data, inflating scores. Verified subset partially addresses this.
- **Narrow scope:** Only tests Python repos from a specific set of projects. Performance on JavaScript, Go, or other ecosystems may differ significantly.
- **Time-bounded:** Agents get generous compute/time budgets that don't reflect real-world latency expectations.

---

## Aider Polyglot

**What it measures:** Multi-language coding ability across 20+ programming languages using the Aider pair-programming agent framework. Tests both single-file edits and multi-file refactoring.

**Why it matters for agent selection:** If your work spans multiple languages (common in hedge fund tech stacks — Python for research, JavaScript for dashboards, SQL for queries), this benchmark reveals whether a model's coding skill is Python-centric or genuinely polyglot. Many models score well on Python but collapse on less common languages.

**Known issues:**
- **Framework bias:** Optimized for Aider's specific interaction pattern. Models tuned for other agent frameworks may underperform.
- **Language imbalance:** Some languages have far fewer evaluation instances, making cross-language comparisons noisy.
- **Shallow depth:** Tests syntactic correctness and basic logic, not architectural reasoning or system design.

---

## GPQA (Graduate-Level Problem Questions Answering)

**What it measures:** Graduate-level reasoning across biology, physics, and chemistry. Questions are written by domain experts and designed to be extremely difficult for non-experts.

**Why it matters for agent selection:** Probes deep reasoning capability rather than surface pattern matching. If you need an agent to analyze scientific literature, evaluate research claims, or reason through complex multi-step problems, GPQA score is a reasonable indicator. High GPQA correlates with better chain-of-thought quality.

**Known issues:**
- **Domain specificity:** A model strong in physics may be weak in biology. Aggregate scores can mask important gaps.
- **Multiple-choice format:** Easier to game than open-ended tasks. Models can use elimination strategies without genuine understanding.
- **Not coding-focused:** High GPQA doesn't imply strong coding ability — these are orthogonal skills.

---

## LiveCodeBench

**What it measures:** Competitive programming problems sourced from platforms like Codeforces and AtCoder. Designed with anti-contamination: new problems are added continuously so models can't memorize solutions.

**Why it matters for agent selection:** Tests algorithmic reasoning, edge case handling, and optimization skills under constraints. If your agent needs to solve complex computational problems or generate efficient code, this is more reliable than static benchmarks. The rolling dataset makes score manipulation much harder.

**Known issues:**
- **Competitive programming bias:** Favors algorithmic cleverness over practical engineering. A model may ace LiveCodeBench but produce unreadable production code.
- **Time pressure:** Problems are designed for human time limits; agent performance depends heavily on how compute budget is allocated.
- **Language preference:** Most problems are language-agnostic but solutions tend to favor C++/Python.

---

## Tau-Bench

**What it measures:** End-to-end task automation — completing multi-step workflows that involve API calls, data retrieval, decision-making, and error handling across simulated environments.

**Why it matters for agent selection:** This is the closest benchmark to real agent work: executing a complex task across multiple tools and services with partial observability. If you're building agents for trading workflows, data pipelines, or operational automation, Tau-Bench is highly relevant.

**Known issues:**
- **Simulated environments:** Tasks run in sandboxed environments that may not capture real-world API rate limits, network failures, or data quality issues.
- **Reward design:** Success metrics may not align with your specific use case. An agent optimized for Tau-Bench rewards may over-optimize for completeness at the expense of speed or cost.
- **Early benchmark:** Less established than SWE-bench; fewer independent evaluations and reproducibility studies.

---

## Benchmarks vs Reality

**Why benchmark scores don't always translate to real-world performance:**

### Context Window Mismatch
Benchmarks typically use problems that fit within a model's context window. In production, agents face codebases of millions of tokens. A model scoring 70% on SWE-bench may fail when the relevant code is spread across 50 files that exceed context limits.

### Tool Use Gap
Most benchmarks evaluate raw model capability, not tool integration. An agent's real performance depends on:
- How well the model uses available tools (file search, terminal, API calls)
- Quality of the tool-calling loop and error recovery
- Whether the agent framework handles tool output truncation gracefully

### Prompt Quality Dependency
Benchmark scores assume carefully crafted prompts with clear instructions. In production, prompt quality varies dramatically. A model that requires precise prompting to achieve its benchmark score will underperform compared to a more robust model with a lower peak score.

### Compute Budget Differences
Benchmarks often allow generous retry budgets and compute time. Real agents face latency constraints and cost limits that force trade-offs between thoroughness and speed.

### Recommendation
Use benchmarks as a **first filter**, not a final answer. After narrowing candidates by benchmark scores, test them on your actual workload with your actual prompt templates and tool configurations.

---

## Related Concepts

- [[agent-anti-patterns]]
- [[model-selection-for-agents]]

## Process-Level Evaluation (TraceGraph)

**TraceGraph** (2026-05) introduces a graph-based framework that turns released multi-model agent trajectories into shared decision landscapes, enabling diagnosis of where models diverge beyond aggregate pass rates.

**Key methodology:**
- For each task, builds a graph over observable action-observation states from pooled rollouts across models
- Overlays outcome-informed **productive cores** and **trap regions**
- Summarizes each rollout with three events: **Access** (reached productive core), **Trap exposure** (entered trap region), **Repair** (recovered from trap)
- Reveals navigation differences hidden by aggregate scores — some splits reward avoiding traps, others reward recovering from them

**Real-world impact:** Applied to SWE-bench, a trap-aware recovery pipeline raises official resolved rate from 40.4% to 43.5% on fired instances by detecting trap states and applying lightweight continuation policies.

**For agent users:** When evaluating agent performance:
- Aggregate pass rates hide *where* and *why* agents fail
- Trap region analysis reveals whether your agent needs better avoidance (planning) or better recovery (debugging)
- Process-level evaluation is more actionable than score-level evaluation
