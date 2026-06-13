title: Multi-Agent Orchestration
tags: multi-agent, orchestrator, agent-architecture
# Multi-Agent Orchestration

## Overview

Multi-agent orchestration coordinates multiple specialized agents to solve problems that exceed a single agent's capability.

## Patterns

### Orchestrator-Workers
Central agent decomposes tasks and assigns to workers. Workers are independent; orchestrator synthesizes results.

### Supervisor-Workers
Similar to orchestrator but the supervisor actively monitors and can reassign tasks mid-flight.

### Peer-to-Peer
Agents communicate directly without a central coordinator. Emergent behavior, harder to control.

### Hierarchical
Multi-level hierarchy where orchestrators delegate to sub-orchestrators. Scales to very large problems.

## Challenges

- **Coordination overhead** — More agents ≠ more throughput
- **Information loss** — Handoff between agents loses context
- **Cost multiplication** — Each agent step costs tokens
- **Debugging** — Tracing failures across agents is harder

## When to Use

- Task requires diverse expertise (code + research + analysis)
- Parallel execution reduces wall-clock time
- Single agent context window is insufficient

## Arbor: Tree Search as a Cognition Layer (June 2026)

**Arbor** (arXiv:2606.12563) introduces structured tree search as a shared working memory across agents — a significant advance over stateless multi-agent optimization.

### Architecture
- **Orchestrator agent**: Drives optimization by delegating to Domain Specialists across the inference stack
- **Critic agent**: Safeguards stability through root-cause analysis, introspection, and measurement validation
- **Checks-and-balances**: Neither agent can unilaterally drive the system
- **Search tree**: Explicit tree of scored hypotheses serves as shared working memory, evolving with every measurement
- **Skill decomposition**: Hard skills (domain expertise) + soft skills (coordination protocols)

### Results (Full-Stack LLM Inference Optimization)
- Up to **193% inference throughput-latency Pareto improvement** over vendor-optimized baselines
- Single agent without harness: plateaus at +33% throughput and **crashes irrecoverably within hours**
- Generalizes across hardware generations; run-to-run variance within 2 percentage points
- Enables **fully autonomous multi-day optimization campaigns**

### Key Insight
The tree search structure transforms failures into diagnostic signal that reshapes subsequent exploration, and successes shift the bottleneck distribution for expansion. This is fundamentally different from isolated target optimization with stateless evaluation.

Sources: [arXiv:2606.12563](https://arxiv.org/abs/2606.12563) ^[raw/papers/unknown-arbor-tree-search-as-a-cognition-layer-for-autonomous-agents.md]

## HarnessBridge: Learnable Agent Harness (June 2026)

**HarnessBridge** (arXiv:2606.12882) demonstrates that agent harnesses can be learned rather than manually engineered.

### Architecture
- **Observation projection**: Distills raw trajectories into compact, decision-relevant states
- **Action projection**: Converts proposed actions into executable transitions or trajectory-grounded rejections
- **Bidirectional controller**: Learnable plug-in module trained end-to-end via unified instruction tuning

### Results
- Matches or surpasses strong specialized harnesses on [[evaluation-benchmarks|Terminal-Bench 2.0]] and [[swe-bench]] Verified
- Substantially reduces token usage and trajectory length
- Generalizes from smaller generators to larger commercial models

Sources: [arXiv:2606.12882](https://arxiv.org/abs/2606.12882) ^[raw/papers/unknown-harnessbridge-learnable-bidirectional-controller-for-llm-agent-harness.md]

## Related

- [[architectures]]
- [[single-vs-multi-agent]]
- [[model-selection-for-agents]]
- [[tool-use-pattern]] — Tool workflows in multi-agent settings
- [[agent-safety]] — Containment Gap in multi-agent frameworks