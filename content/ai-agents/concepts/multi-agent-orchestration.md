---
title: Multi-Agent Orchestration
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [multi-agent, orchestration, architecture]
sources: [raw/papers/unknown-agentdropoutv2-optimizing-information-flow-in-multi-agent-systems-via-test-time.md, raw/papers/unknown-agents-that-matter-optimizing-multi-agent-llms-via-removal-based-attribution.md, raw/papers/unknown-tcp-mcp-landscape-guided-co-evolution-of-prompts-and-communication-topologies-fo.md, raw/papers/unknown-got-a-secret-llm-agents-cant-keep-it-evaluating-privacy-in-multi-agent-systems.md, raw/papers/unknown-voluntary-collusion-with-secret-tools-in-competing-llm-agents.md]
confidence: high
---

# Multi-Agent Orchestration

Multi-agent orchestration is the coordination layer that manages how specialized agents collaborate on complex tasks. Unlike simple delegation (one agent spawning one subagent), orchestration involves routing work, managing state, handling failures, and synthesizing results across multiple agents.

---

## Definition

Multi-agent orchestration refers to the design patterns and frameworks that enable multiple AI agents to work together on a shared goal. The orchestrator acts as a coordinator — decomposing tasks, assigning subtasks, monitoring progress, handling failures, and merging results.

---

## When to Use

- **Parallel research**: Multiple subagents researching different aspects simultaneously
- **Complex workflows**: Tasks with distinct phases requiring different expertise (e.g., data collection → analysis → report generation)
- **Scale-out workloads**: Processing large datasets where each agent handles a subset

## When NOT to Use

- Simple single-step tasks (overhead exceeds benefit)
- Tasks requiring deep context sharing (context loss between agents)
- When latency is critical (orchestration adds coordination time)

---

## Key Patterns

### Orchestrator-Workers
A central orchestrator decomposes a task and assigns subtasks to specialized workers. Workers operate independently; the orchestrator synthesizes results. This is the most common pattern — used by Hermes `delegate_task` with `tasks` array.

### Hierarchical
Multi-level delegation where workers can themselves become orchestrators for sub-subtasks. Requires depth limits to prevent exponential agent growth (see [[agent-anti-patterns]] — The Delegation Cascade).

### Peer-to-Peer
Agents communicate directly without a central coordinator. Useful for collaborative tasks but harder to debug and control.

### Supervisor
A supervisor agent monitors worker agents and intervenes when quality drops or errors occur. Adds reliability at the cost of additional token consumption.

---

## Implementation Considerations

- **State management**: How do agents share intermediate results? (files, messages, shared memory)
- **Error handling**: What happens when a worker fails? (retry, escalate, skip)
- **Cost tracking**: Each agent adds token overhead for its system prompt and context
- **Depth limits**: Prevent delegation cascades by enforcing maximum nesting levels

### Error Propagation and Pruning

In multi-agent systems, erroneous information from individual agents cascades through the system. **AgentDropoutV2** proposes a test-time rectify-or-reject pruning framework that intercepts agent outputs and employs a retrieval-augmented rectifier to iteratively correct errors, pruning irreparable outputs. This achieved 6.39pp accuracy gain on math benchmarks and 2.28pp on code benchmarks.

### Agent Attribution and Optimization

Not all agents in a MAS contribute equally. Research formalizes agent attribution as a cooperative game (parameterized by coalition distribution, removal protocol, and target metric). **Leave-One-Out (LOO)** identifies bottleneck agents as effectively as combinatorial methods at a fraction of cost. Replacing low-contribution agent backbones improved task performance by up to 17% while reducing cost by up to 35%.

### Prompt-Topology Co-Evolution

Agent behavior depends on both the information received AND how the receiving agent interprets it. **TCP-MCP** jointly evolves prompts and communication topologies as a unified genome, using Pareto-front diagnostics across task performance, token cost, and structural complexity. Achieved competitive accuracy to debate-style systems with up to 5.69× fewer tokens.

### Privacy Risks in Multi-Agent Systems

Multi-agent environments amplify privacy risks: agents are 8× more likely to disclose sensitive information after observing a peer do so. Leakage is socially contagious. Explicit privacy instructions reduce but don't eliminate the effect (still >37.8% leakage). See [[agent-safety]] for mitigation strategies.

---

## Related Concepts

- [[architectures]] — Orchestrator-workers is a core agent architecture pattern
- [[agent-anti-patterns]] — The Delegation Cascade: what happens without depth limits
- [[orchestrator-workers]] — Hermes-specific implementation of this pattern
- [[single-vs-multi-agent]] — Decision matrix for choosing orchestration vs single agent
