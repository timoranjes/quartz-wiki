---
title: "Evaluation Benchmarks"
type: concept
tags: [evaluation, benchmark]
created: "2026-06-03"
updated: "2026-06-13"
status: seed
---

# Evaluation Benchmarks

## Overview

Benchmarks measure agent capability across dimensions: reasoning, tool use, code generation, and multi-step planning.

## Key Benchmarks

| Benchmark | Measures | Scope |
|-----------|----------|-------|
| SWE-bench | Code issue resolution | GitHub PRs |
| GAIA | General AI assistant | Multi-modal |
| AgentBench | Agent tool use | 8 environments |
| WebArena | Web automation | Browser tasks |
| OSWorld | Desktop/OS automation | Full OS |
| Terminal-Bench | CLI tasks | Shell commands |
| BigCodeBench | Code generation | Complex functions |

## Evaluation Principles

1. **Real tasks, not synthetic** — Evaluate on tasks that matter
2. **End-to-end** — Measure the full agent loop, not just the LLM
3. **Cost-aware** — Track $/task alongside accuracy
4. **Reproducible** — Same inputs should produce comparable results


## MMLU Benchmark (June 2026 Update)

**MMLU** (Massive Multitask Language Understanding) evaluates LLMs across 57 subjects using standardized multiple-choice questions covering legal, math, reasoning, finance, general, healthcare, and language tasks.

- **Current tracking**: 99 models tracked on [llm-stats.com](https://llm-stats.com/benchmarks/mmlu)
- **Score range**: 0–1.0 (maximum possible score)
- **Use case**: Broad knowledge assessment across academic and professional domains
- **Limitation**: Multiple-choice format; doesn't measure agentic or coding capabilities

## New Benchmarks (June 2026)

### SciAgentArena
- **Purpose**: Evaluate AI agents in real-world scientific research scenarios
- **Scale**: ~200 tasks with stepwise verification, interactive agent-agnostic environment
- **Key finding**: Current agents effective for well-specified data-analysis workflows but **struggle with novel insights, self-directed exploration, and open-ended research questions**
- **Source**: [arXiv:2606.12736](https://arxiv.org/abs/2606.12736)

### DailyReport
- **Purpose**: Evaluate search agents on daily, real-world information-seeking tasks
- **Scale**: 150 open-ended tasks, 3,546 rubrics, cascade evaluation across disentangled dimensions
- **Key finding**: 17 agentic systems tested — **all fall short of user expectations**
- **Innovation**: Subtask decomposition + cascade performance attribution + user-centric aggregation
- **Source**: [arXiv:2606.12871](https://arxiv.org/abs/2606.12871)

### ToolSense
- **Purpose**: Diagnostic framework for auditing parametric tool knowledge in LLMs
- **Method**: Auto-generates three benchmarks from any tool catalog: Realistic Retrieval Benchmark (3 ambiguity tiers), MCQ probing, QA probing
- **Key finding**: **Knowledge-retrieval dissociation** — models with strong retrieval scores can score near-random on factual probes about their tools. Under realistic queries, performance collapses 50-64 percentage points vs. standard ToolBench benchmarks
- **Source**: [arXiv:2606.12451](https://arxiv.org/abs/2606.12451), [GitHub](https://github.com/SAP/toolsense)

### MCP-Bench (via Evoflux)
- **Purpose**: Evaluate tool workflow execution over live MCP servers
- **Scale**: 250 tools across live MCP servers
- **Key finding**: Small planners achieve ~3% execution feasibility at zero-shot; evolutionary search (Evoflux) raises to 17-24%
- **Source**: [arXiv:2606.12674](https://arxiv.org/abs/2606.12674)

### Terminal-Bench 2.0 (via HarnessBridge)
- **Purpose**: Evaluate CLI agent harness quality
- **Key finding**: Learnable harness controller (HarnessBridge) matches/surpasses strong specialized harnesses while reducing token usage and trajectory length
- **Also evaluated on**: [[swe-bench]] Verified
- **Source**: [arXiv:2606.12882](https://arxiv.org/abs/2606.12882)

## Related

- [[model-selection-for-agents]]
- [[architectures]]
- [[tool-use-pattern]] — ToolSense benchmark implications
- [[mcp-protocol]] — MCP-Bench evaluation
- [[agent-safety]] — Containment Gap safety audit
