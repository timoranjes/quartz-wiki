---
title: "Tool Use Pattern"
type: concept
tags: [tool-use, agent-architecture]
created: "2026-06-03"
updated: "2026-06-18"
status: seed
---

# Tool Use Pattern

## Overview

Tool use (function calling) is the primary mechanism by which agents interact with the external world — APIs, filesystems, browsers, databases.

## Tool Lifecycle

1. **Discovery** — Agent learns available tools from schema
2. **Selection** — Agent chooses the right tool for the current step
3. **Execution** — Tool runs and returns structured output
4. **Integration** — Agent incorporates the result into its reasoning

## Best Practices

- **Typed schemas** — Use JSON Schema with descriptions, not just function names
- **Error handling** — Tools should return structured errors, not throw
- **Idempotency** — Prefer idempotent tools to avoid side effects on retry
- **Rate limits** — Track tool call budgets per session
- **Timeouts** — Every tool call needs a timeout

## Common Tool Categories

| Category | Examples |
|----------|----------|
| Web | search, scrape, browser automation |
| Code | execute, debug, lint |
| Data | query, read_file, write_file |
| Communication | send_message, email |
| Analysis | chart, summarize, compare |

## Evoflux: Evolutionary Tool Workflow Repair (June 2026)

**Evoflux** (arXiv:2606.12674) addresses a critical failure mode: compact LMs can generate plausible-looking tool workflow graphs that fail under actual execution.

### Problem
- [[mcp-protocol]]-style tool use requires: tool discovery from live catalogs, schema satisfaction, dependency preservation across intermediate outputs, execution grounding
- Small planners generate workflow graphs that fail at tool resolution, parameter validation, dependency tracking, or execution
- Few hundred teacher traces can teach format but not recovery behavior over changing tool catalogs

### Method
- **Inference-time evolutionary search** treating tool use as repair of executable workflows
- Evolves typed workflow graphs through: structured edits, execution feedback, adaptive intensity, meta-guided redesign, diversity pruning
- Evaluated on **MCP-Bench**: live MCP servers, 250 tools

### Results
- Execution feasibility: ~3% (zero-shot) → **17-24%** (Evoflux) across small planners
- SFT and SFT+DPO on same data match, underperform, or collapse below zero-shot
- ReAct reaches higher peaks but with higher variance and token cost
- **Execution-grounded search is more reliable under scarce teacher-trace budgets**

Sources: [arXiv:2606.12674](https://arxiv.org/abs/2606.12674) ^[raw/papers/unknown-evoflux-inference-time-evolution-of-executable-tool-workflows-for-compact-agents.md]

## ToolSense: Knowledge-Retrieval Dissociation (June 2026)

**ToolSense** (arXiv:2606.12451, SAP) reveals a critical blind spot in parametric tool retrieval evaluation.

### Key Discovery
- Parametric tool retrieval encodes each tool as a virtual token appended to LLM vocabulary, fine-tuned in two stages (memorization → retrieval SFT)
- Standard ToolBench benchmarks use verbose, fully-specified queries with constrained decoding — **neither reveals whether the model actually understands its tools**
- ToolSense auto-generates three diagnostic benchmarks from any tool catalog:
  1. **Realistic Retrieval Benchmark** (RRB) — queries at three ambiguity tiers
  2. **MCQ probing** — factual knowledge about tools
  3. **QA probing** — open-ended tool understanding

### Findings (ToolBench, ~47K tools)
- **Knowledge-retrieval dissociation**: models with strong retrieval scores score near-random on factual probes
- Under realistic queries: performance **collapses 50-64 percentage points** vs. standard ToolBench benchmarks, falling below embedding-model baseline
- Open-sourced: [github.com/SAP/toolsense](https://github.com/SAP/toolsense)

Sources: [arXiv:2606.12451](https://arxiv.org/abs/2606.12451) ^[raw/papers/unknown-toolsense-a-diagnostic-framework-for-auditing-parametric-tool-knowledge-in-llms.md]

## Teach-and-Repeat: GUI Agent Knowledge Extraction (June 2026)

**Teach-and-Repeat** (arXiv:2606.12817) introduces a paradigm for converting mobile screen demonstrations into reusable operational knowledge for GUI agents.

### Method
- **Teach VLM**: Core model that translates mobile screen trajectories into step-wise operational knowledge (action types, target UI elements, textual arguments, execution orders)
- Extracts and analyzes operation-related keyframes from demonstration videos
- Systematic data flywheel for scalable data acquisition (addresses aligned training data scarcity)
- **Teach-and-Repeat paradigm**: Generated operational knowledge serves as interpretable procedural reference for downstream execution agents

### Results
- Teach VLM significantly outperforms strong VLM baselines in operation semantics prediction (SOTA)
- Chinese Mobile Screen Teach Benchmark introduced for fine-grained evaluation
- Android World experiments: consistent Task Success Rate improvements for downstream agents

Sources: [arXiv:2606.12817](https://arxiv.org/abs/2606.12817) ^[raw/papers/unknown-teach-and-repeat-accurately-extracting-operational-knowledge-from-mobile-screen.md]

## PASTE: Speculative Tool Execution (June 2026)

**PASTE** (arXiv:2603.18897) addresses a fundamental inefficiency: today's serving systems serialize the generate-then-execute loop, leaving tool latency exposed on the task critical path.

### Key Innovation
- **Predicts concrete future tool invocations** from recurring agent patterns
- **Executes tools speculatively** while the LLM is still generating
- Isolates speculative results until confirmed by the LLM
- Jointly schedules tool execution and returning LLM sessions to avoid shifting bottlenecks to GPU

### Results
- Across deep research, coding, and scientific-agent workloads:
  - **43.5% reduction** in average task completion time
  - **1.8× lower** observed tool latency
- Works because many agent workflows have recurring patterns that make future tool calls predictable

### Implications
The sequential generate→execute loop is not architecturally necessary — **speculative execution** (borrowed from CPU design) applies to agent serving. This is particularly impactful for workloads with predictable tool patterns (deep research, multi-step coding, scientific workflows).

Sources: [arXiv:2603.18897](https://arxiv.org/abs/2603.18897) ^[raw/papers/unknown-parallelizing-tool-execution-and-llm-generation-for-low-latency-agent-serving.md]

## Related

- [[architectures]]
- [[agent-safety]]
- [[mcp-protocol]] — MCP tool catalogs, Evoflux evaluation
- [[evaluation-benchmarks]] — ToolSense, MCP-Bench
- [[agent-memory]] — Memory for tool use context
