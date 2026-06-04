---
title: "Evaluation Benchmarks"
type: concept
tags: [evaluation, benchmark]
created: "2026-06-03"
updated: "2026-06-03"
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

## Related

- [[model-selection-for-agents]]
- [[architectures]]
