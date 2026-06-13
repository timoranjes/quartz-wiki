title: Agent Memory
tags: memory, agent-architecture, reasoning
# Agent Memory

## Overview

Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Agent memory systems must solve the **consolidation problem** — deciding what to remember before the future query is known.

## The Core Problem

Production systems default to **semantic similarity** or **recency** for memory management — both are mis-specified for the forgetting decision:
- Semantic similarity requires knowing what will be queried
- Recency discards old-but-critical information arbitrarily
- The forgetting decision is made at consolidation time, before future queries are known

## Multi-Factor Memory Value Model (June 2026)

Research (arXiv:2606.12945) proposes a cognitively grounded approach to the memory consolidation problem.

### Architecture
- **Memory value function**: V(m) = Σᵢ wᵢ fᵢ(m) over seven interpretable factors
- **Seven factors** (drawn from cognitive psychology):
  1. Emotional intensity
  2. Goal relevance
  3. Value alignment
  4. Self/user relevance
  5. Task utility
  6. Reliability
  7. Usage history
- **Single scalar** uniformly controls: encoding depth, forget risk, and retrieval rank
- **Weights learned** from downstream objective via gradient-free optimization

### Key Results (LongMemEval benchmark)
| Method | Gold Evidence Retained |
|--------|----------------------|
| Learned multi-factor | **0.770 ± 0.011** |
| Uniform weights | 0.657 |
| Best single factor | 0.518 |
| Recency | 0.368 |

- Every paired gap's 95% bootstrap CI is above zero
- Neural network over same factors ties the linear model
- **Learned weights are interpretable**: reliability, emotional intensity, and self/user relevance dominate; query-time goal similarity is correctly down-weighted for the forgetting decision
- Controlled synthetic task with planted confounds: learned weighting achieves 1.00 retention vs. 0.62 for uniform
- Open-source substrate; all experiments run on single CPU with no API calls

### Methodological Insight
Scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at ≈0.98 — but this **measures retrieval, not forgetting**. In the realistic blind regime (no knowledge of future queries), the multi-factor approach significantly outperforms all baselines.

## Memory Dimensions for Agents

| Dimension | Description | Example |
|-----------|-------------|---------|
| Episodic | Specific interactions and outcomes | "User asked about X on date Y, result was Z" |
| Semantic | Generalized knowledge extracted from interactions | "User prefers concise answers" |
| Procedural | How to perform tasks successfully | "For deployment, always run tests first" |
| Working | Current task context (in-context) | Active conversation state |

## Relationship to Other Patterns

- **Consolidation timing**: The forgetting decision must happen at write time, not query time
- **Factor interpretability**: Learned weights should be auditable — opaque memory systems are dangerous for safety-critical agents
- **Budget constraints**: Fixed memory budget forces hard trade-offs between retention and capacity
- [[tool-use-pattern]] — Memory of tool usage patterns and outcomes
- [[agent-safety]] — Memory poisoning attacks (see [[agent-safety|Containment Gap]])

## Open Questions

- How should memory systems handle **contradictory** information across time?
- What is the right **forgetting curve** for different types of agent knowledge?
- How to detect and resist **memory poisoning** attacks (demonstrated to achieve 88.9% wrongful denial rates in [[agent-safety|Containment Gap]] research)?
- Can emotional intensity proxies be computed reliably for non-conversational agent tasks?

## Related

- [[architectures]] — Memory as architectural component
- [[tool-use-pattern]] — Tool usage memory
- [[agent-safety]] — Memory poisoning, containment
- [[evaluation-benchmarks]] — LongMemEval benchmark
- [[multi-agent-orchestration]] — Shared memory across agents (cf. Arbor search tree)