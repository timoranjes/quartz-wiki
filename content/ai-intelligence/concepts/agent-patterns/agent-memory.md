---
title: "Agent Memory"
type: concept
tags: [memory, agent-architecture, reasoning]
created: "2026-06-13"
updated: "2026-06-18"
status: drafted
sources: [raw/papers/unknown-learning-what-to-remember-a-cognitively-grounded-multi-factor-value-model-for-ag.md, raw/papers/unknown-control-plane-placement-shapes-forgetting-an-architectural-study-of-agent-memory.md, raw/papers/unknown-memslides-a-hierarchical-memory-driven-agent-framework-for-personalized-slide-ge.md, raw/papers/unknown-a-survey-on-long-term-memory-security-in-llm-agents-attacks-defenses-and-governa.md]
---

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

## Control-Plane Placement Shapes Forgetting (June 2026)

**ForgetEval** (arXiv:2606.15903) is the first benchmark targeting **forgetting failures** in agent memory — the dominant production failure mode, yet existing benchmarks measure only recall.

### Architecture
- **Recall plane** vs **control plane**: The recall plane retrieves stored facts (extensively benchmarked); the control plane mutates memory via supersede, release, purge (largely untested)
- **Where the LLM sits** in this pipeline shapes which forgetting failure modes the system can recover from
- **13 system configurations** compared on a 385-case adversarial surface

### Three Placement Regimes
| Regime | Strengths | Weaknesses |
|--------|-----------|------------|
| **Deterministic primitives** | Lexical/temporal categories | Fail canonicalization (5% on identifier-obfuscation, 0% cross-lingual) |
| **Inscribe-time LLM** | Recovers canonicalization (100%) | Cannot help intent-aware deletion (0% on prefix-collision, compound-fact) |
| **Mutation-time LLM hook** | Recovers intent-aware deletion (78-85%), brightens nearly all categories | $0.17 per 385-case run, 2.3s/case mutation latency vs 64-191ms deterministic |

### Key Results
- Mutation-time hook achieves **91.7-93.2% overall** accuracy
- Recall path unchanged (no latency impact on queries)
- **ForgetEval**: 1000-case templated suite + 385-case adversarial layer (132 hand-crafted + 253 LLM-drafted oracle-validated)
- Six-method **Adapter Protocol** (130 lines) lets heterogeneous memory stores enter evaluation
- Admission corroborated by 10-annotator IAA (Fleiss' kappa = 0.958)
- 77-case external-authored subset replicates canonicalization asymmetry and amplifies joint-placement lift (+27.8 pt)

### Key Insight
Production failures are predominantly **forgetting failures** rather than recall failures. The control plane (mutation operations) is the under-benchmarked frontier. The three regimes have **partly complementary coverage** — no single placement dominates.

Sources: [arXiv:2606.15903](https://arxiv.org/abs/2606.15903) ^[raw/papers/unknown-control-plane-placement-shapes-forgetting-an-architectural-study-of-agent-memory.md]

## Hierarchical Memory Architecture: MemSlides (June 2026)

**MemSlides** (arXiv:2606.17162) demonstrates that effective personalization requires separating memory into three distinct stores with different lifetimes and purposes.

### Three-Tier Memory Design
| Memory Type | Lifetime | Purpose |
|-------------|----------|---------|
| **User profile memory** | Long-term, cross-task | Intent-conditioned profiles for personalization |
| **Working memory** | Session-level | Active preferences and constraints across revision rounds |
| **Tool memory** | Reusable execution experience | Reliable localized editing from past operations |

### Key Design Principles
- **Scoped slide-local revision**: Targeted updates act on smallest affected region instead of regenerating full deck
- User profile memory improves persona-alignment judgments
- Tool-memory injection improves closed-loop modify behavior
- Working memory carries preferences across multi-turn revision

### Implications
Effective agent memory is not a single store — it requires **separation by lifetime and access pattern**. This mirrors the episodic/semantic/procedural/working dimensions but adds the crucial insight that **tool memory** (execution experience) is a distinct category from user preferences or session state.

Sources: [arXiv:2606.17162](https://arxiv.org/abs/2606.17162) ^[raw/papers/unknown-memslides-a-hierarchical-memory-driven-agent-framework-for-personalized-slide-ge.md]

## Long-Term Memory Security: Lifecycle Framework (June 2026)

A comprehensive survey (arXiv:2604.16548) proposes a **Memory Lifecycle Framework** for securing persistent agent memory, organized along two axes:

### Six Lifecycle Phases
1. **Write** — Memory insertion
2. **Store** — Persistence and versioning
3. **Retrieve** — Query-time access
4. **Execute** — Memory-influenced actions
5. **Share & Propagate** — Cross-agent memory transfer
6. **Forget & Rollback** — Deletion and recovery

### Four Security Objectives
- Integrity, Confidentiality, Availability, Governance

### Key Finding
Robust LTM security **cannot be retrofitted** at retrieval or execution time alone — must be anchored in **storage-time provenance, versioning, and policy-aware retention** from the outset.

### Verifiable Memory Governance (VMG)
Five architectural primitives specifying what verifiable mechanisms a long-term-memory system must provide for auditable, recoverable control over memory state.

Sources: [arXiv:2604.16548](https://arxiv.org/abs/2604.16548) ^[raw/papers/unknown-a-survey-on-long-term-memory-security-in-llm-agents-attacks-defenses-and-governa.md]

## Related

- [[architectures]] — Memory as architectural component
- [[tool-use-pattern]] — Tool usage memory
- [[agent-safety]] — Memory poisoning, containment, guardrail DoS
- [[evaluation-benchmarks]] — LongMemEval, ForgetEval benchmarks
- [[multi-agent-orchestration]] — Shared memory across agents (cf. Arbor search tree)
