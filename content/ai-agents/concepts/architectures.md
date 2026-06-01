---
title: Agent Architectures
created: 2026-05-29
updated: 2026-06-02
type: concept
tags: [agent-architecture, orchestration]
sources: [raw/papers/unknown-anticipate-and-learn-unleashing-idle-time-compute-in-proactive-agents.md, raw/papers/unknown-autosci-a-memory-centric-agentic-system-for-the-full-scientific-research-lifecyc.md]
confidence: high
---

# Agent Architectures

## Definition

Structural patterns for organizing AI agent behavior. The architecture determines how an agent thinks, plans, uses tools, and decomposes complex tasks.

## Core Architectures

### 1. Single-Agent (ReAct)
**Pattern:** Think -> Act -> Observe -> Repeat
- Model alternates between reasoning and tool use in one loop
- Simple, reliable, good for tasks with clear steps
- **When to use:** Straightforward tasks, tool calls < 5, no decomposition needed
- **Limitation:** Context window fills up with tool outputs; loses track of multi-step plans
- **See:** [[react-pattern]]

### 2. Plan-and-Execute
**Pattern:** Plan first -> Execute plan -> Verify -> Revise if needed
- Separate planning phase from execution
- Model creates a step-by-step plan, then follows it
- **When to use:** Multi-step tasks with known structure (build X, test Y, deploy Z)
- **Limitation:** Plan may be wrong; requires revision mechanism
- **See:** [[planning-pattern]]

### 3. Orchestrator-Workers (Multi-Agent)
**Pattern:** Orchestrator decomposes -> Workers execute in parallel -> Orchestrator synthesizes
- One agent acts as coordinator, spawns sub-agents for parallel work
- Each sub-agent has isolated context and toolset
- **When to use:** Complex tasks with independent subtasks, large data processing, research synthesis
- **Limitation:** Overhead of coordination; sub-agents cannot share context mid-flight
- **See:** [[orchestrator-workers]], [[multi-agent-orchestration]]

### 4. Reflection / Self-Correction
**Pattern:** Generate -> Critique -> Revise -> Repeat
- Agent reviews its own output and iterates
- Can be single pass (generate + self-critique) or multi-pass
- **When to use:** Quality-critical output (code review, writing, analysis)
- **Limitation:** Uses extra tokens; model may not catch its own errors
- **See:** [[reflection-pattern]]

### 5. Agentic RAG
**Pattern:** Query -> Retrieve -> Synthesize -> Decide if more retrieval needed
- Agent decides what to retrieve, when to stop, how to synthesize
- More flexible than fixed RAG pipelines
- **When to use:** Open-ended research, knowledge-intensive tasks
- **Limitation:** Retrieval quality bottleneck; can get stuck in loops

### 6. Hierarchical / Swarm
**Pattern:** Top-level goal -> Layer of managers -> Layer of workers
- Multiple levels of delegation
- Each level handles abstraction at its own granularity
- **When to use:** Massive projects (100+ tasks), team simulation
- **Limitation:** Very expensive; coordination overhead grows exponentially

### 7. Proactive Agent
**Pattern:** Analyze dialogue history + memory -> Predict upcoming needs -> Pre-compute during idle time -> Present prepared results
- Agents use idle compute time between interactions to anticipate user needs
- ProAct architecture reduces required turns by 14.8%, user effort by 11.7%, and hallucination by 28.1%
- **When to use:** Repetitive workflows where next steps are predictable from context
- **Limitation:** Wasted compute if predictions are wrong; requires persistent memory
- **See:** [[planning-pattern]] — planning is the reactive version of this

### 8. Memory-Centric Persistent Agent (AutoSci)
**Pattern:** Schema-governed persistent memory + lifecycle execution + self-evolution
- **SciMem:** Dual-layer memory — Long-Term Knowledge Memory (reusable scientific knowledge) + Active Research Memory (project-level artifacts: ideas, experiments, manuscripts, reviews)
- **SciFlow:** Five-stage lifecycle execution (literature understanding → rebuttal) with state/context/verification/feedback orchestration
- **SciDAG:** DAG-shaped multi-agent operators for difficult skills with reusable stage-specific templates
- **SciEvolve:** Converts feedback from users, experiments, reviews, and external environments into versioned updates to memory organization, skills, and templates
- **Key insight:** Agents that persist across projects need structured memory, not just context windows. Schema-governed memory prevents knowledge drift.
- **When to use:** Long-running research projects, knowledge accumulation across sessions, agents that need to "remember and evolve"
- **Limitation:** Requires schema design overhead; memory quality degrades without curation

## Selection Matrix

| Task Complexity | Recommended | Why |
|-----------------|-------------|-----|
| Simple Q&A | Single-Agent | No decomposition needed |
| Tool use (3-5 steps) | ReAct | Alternating think/act works well |
| Build a feature | Plan-and-Execute | Structured, verifiable steps |
| Research + synthesis | Orchestrator-Workers | Parallel research, single synthesis |
| Code review | Reflection | Self-correction catches issues |
| Massive project | Hierarchical | Decomposition at multiple levels |

## Related Concepts
- [[model-selection-for-agents]] - which model for which architecture
- [[cost-optimization]] - token cost per architecture pattern
- [[debugging-agents]] - what goes wrong in each architecture
- [[personal-workflow-lessons]] - practical Hermes agent workflow patterns
