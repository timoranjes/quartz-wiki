---
title: Model Selection for Agent Tasks
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [model, reasoning, coding, agentic]
sources: []
confidence: medium
---

# Model Selection for Agent Tasks

## Definition

Choosing the right model for the right agent task is the single highest-leverage optimization. A model that is "smart" on benchmarks may be terrible at tool use, and vice versa.

## Task-to-Model Mapping

### Coding Tasks
**Requirements:** Code understanding, file manipulation, test writing, debugging
- **Best:** Codex models (GPT-4o-Codex, Claude Sonnet), Qwen Coder series
- **Why:** Trained on code execution patterns, understand file systems
- **Avoid:** General reasoning models — they hallucinate APIs

### Reasoning / Analysis
**Requirements:** Multi-step logic, weighing evidence, synthesis
- **Best:** Claude Sonnet 4, o3, DeepSeek R1
- **Why:** Strong chain-of-thought, handles ambiguity well
- **Avoid:** Fast models — they skip steps

### Browsing / Web Interaction
**Requirements:** Navigate complex pages, extract data, handle dynamic content
- **Best:** GPT-4o, Claude Opus (vision + browsing)
- **Why:** Visual understanding of page layout
- **Avoid:** Text-only models for complex UIs

### Multi-Agent Orchestration
**Requirements:** Task decomposition, routing decisions, synthesis
- **Best:** Claude Sonnet 4 (balanced speed/quality)
- **Why:** Good at structural thinking without over-costing
- **Avoid:** Overkill models for simple routing

### Content Generation
**Requirements:** Writing, formatting, creative output
- **Best:** Claude Sonnet 4, GPT-4o
- **Why:** Good prose, follows formatting instructions
- **Avoid:** Coding-specialized models — weak prose

## My Current Model Routing (Hermes)

| Profile | Model | Primary Use |
|---------|-------|-------------|
| coder | MiniMax-M2.5 | SWE-bench 80.2, code fixes, PRs |
| reviewer | glm-5 | Code review, knowledge-heavy checks |
| researcher | qwen3.6-plus | Web research, 1M context for long docs |
| analyst | glm-5 | Data analysis, math reasoning |
| writer | qwen3.6-plus | Content generation, summaries |

## Benchmarks That Matter for Agents

| Benchmark | What It Measures | Relevance |
|-----------|-----------------|-----------|
| SWE-bench | Real GitHub issue resolution | Coding agents |
| GPQA | Graduate-level reasoning | Analysis agents |
| AgentBench | Multi-environment tool use | General agents |
| WebArena | Web task completion | Browsing agents |
| ToolBench | Tool call accuracy | Any agent using tools |

## Cost Considerations

| Model Tier | $/1M input | $/1M output | Best For |
|------------|-----------|-------------|----------|
| Premium | $15-60 | $60-240 | Final review, critical decisions |
| Mid-tier | $3-15 | $12-60 | General agent work |
| Budget | $0.1-3 | $0.5-10 | High-volume, low-stakes tasks |

**Rule of thumb:** Route 80% of work to mid-tier, 15% to budget, 5% to premium.

## Related Concepts
- [[architectures]] — architecture influences model choice
- [[cost-optimization]] — saving money with smart routing
- [[orchestrator-workers]] — different models for orchestrator vs workers
