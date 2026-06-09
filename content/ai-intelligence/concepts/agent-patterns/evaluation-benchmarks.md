---
title: "Evaluation Benchmarks"
type: concept
tags: [evaluation, benchmark]
created: "2026-06-03"
updated: "2026-06-08"
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

## Related

- [[model-selection-for-agents]]
- [[architectures]]
