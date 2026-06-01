---
title: Cost Optimization
created: 2026-05-29
updated: 2026-06-02
type: concept
tags: [cost-optimization, workflow]
sources: [raw/papers/unknown-a-policy-driven-runtime-layer-for-agentic-llm-serving.md, raw/papers/unknown-slat-segment-level-adaptive-trimming-for-efficient-cot-reasoning.md]
confidence: high
---

# Cost Optimization for Agent Work

## Problem

Agents consume tokens on every tool call, every thought, every retry. Without discipline, costs spiral fast — especially with multi-agent patterns.

## High-Impact Strategies

### 1. Model Routing
Route tasks to the cheapest model that can handle them:
- **Simple lookups:** Budget model ($0.1-3/1M tokens)
- **Standard agent work:** Mid-tier model ($3-15/1M tokens)
- **Critical decisions:** Premium model ($15-60/1M tokens)

**Savings:** 60-80% vs using premium model for everything.

### 2. Context Compression
- **Summarize before delegating:** Instead of passing 10K lines of raw data, pass a 500-line summary.
- **Pre-filter tool outputs:** If a tool returns 50 results, filter to top 5 before the agent sees them.
- **Strip whitespace/comments:** When passing code to agents, remove unnecessary content.

**Savings:** 40-60% on context tokens.

### 3. Batch Processing
- Process multiple similar items in one agent call instead of N calls.
- Example: Review 5 PRs in one pass vs 5 separate reviews.
- **Trade-off:** Risk of shallow treatment per item. Mitigate with explicit per-item criteria.

**Savings:** 50-70% on orchestration overhead.

### 4. Caching
- Cache tool outputs that are deterministic (file contents, API responses).
- Re-use across agent calls instead of re-reading.
- Example: Read SCHEMA.md once, reuse across all wiki operations.

**Savings:** Eliminates redundant input tokens.

### 5. Tool Selection
- Use cheaper tools when possible: `web_search` (5 results) vs `browser_navigate` (full page load).
- Use `search_files` instead of `grep` in terminal (no shell overhead).
- Use `read_file` with `limit` instead of reading entire files.

**Savings:** 30-50% on tool-related tokens.

### 6. Prompt Efficiency
- **System prompts:** Keep them short. Every token in the system prompt is paid on every turn.
- **Examples:** Use 1-2 high-quality examples instead of 5 mediocre ones.
- **Instructions:** Be specific, not verbose. "Fix the bug at line 42" > "Please carefully examine the code and identify any issues..."

**Savings:** 20-30% on per-turn overhead.

### 7. KV Cache Optimization (Serving Layer)
Research on agentic LLM serving reveals that inserting a runtime layer between the agent framework and serving engine enables agent-aware policies like KV caching across sessions. **CacheSage** learns per-workload agent transition matrices online and uses survival-based eviction + between-step prefetch, achieving +13 to +37pp cache hit-rate lift, 12-29% lower TTFT, and 6-14% higher throughput.

**For self-hosted agents:** If you run local models, cache agent session states between turns — the agent's next action is predictable from its current state, enabling prefetch.

**Savings:** 12-29% latency reduction, 6-14% throughput increase.

### 8. CoT Reasoning Trimming (SLAT)

**SLAT** (Segment-Level Adaptive Trimming, 2026-05) addresses the "overthinking" problem in reasoning models — where generated reasoning chains contain structural redundancy that incurs high computational overhead without improving answer correctness.

**Key findings:**
- Inefficiency concentrates in high-probability segments with low marginal utility (not uniformly across the chain)
- SLAT uses theoretically grounded segment-aware trimming to selectively suppress redundant segments
- **Result:** 50% reasoning length reduction while maintaining competitive accuracy
- Superior to token-uniform length penalties, which can inadvertently suppress useful reasoning alongside redundancy

**For agent users:** When using reasoning models (R1, o-series, etc.) for agent tasks:
- Not all "thinking" tokens are equally valuable — prune low-utility segments
- If you control the model, segment-aware trimming beats blanket length penalties
- For API users: set max_tokens conservatively; models often over-generate CoT beyond what's needed

## My Current Cost Stack

| Resource | Type | Cost Profile | Usage |
|----------|------|-------------|-------|
| Alibaba (DashScope) | Flat monthly | Already paid, use freely | Coding tasks, general agent work |
| OpenAI | Per-token | Expensive for heavy use | Reserve for premium tasks only |
| Anthropic | Per-token | Expensive | Critical reasoning/review only |

## Cost Tracking by Pattern

| Pattern | Typical Token Range | Cost Tier |
|---------|-------------------|-----------|
| Single Q&A | 2-5K | Low |
| ReAct (5 steps) | 10-30K | Medium |
| Plan-and-Execute | 15-40K | Medium |
| Orchestrator (3 workers) | 50-150K | High |
| Orchestrator (5 workers) | 100-300K | Very High |
| Multi-pass reflection | 2x base cost | Medium-High |

## Related Concepts
- [[model-selection-for-agents]] — cheapest capable model per task
- [[orchestrator-workers]] — cost of parallel delegation
- [[tool-use-pattern]] — efficient tool selection
