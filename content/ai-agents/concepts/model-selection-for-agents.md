---
title: Model Selection for Agent Tasks
created: 2026-05-29
updated: 2026-06-03
type: concept
tags: [model, reasoning, coding, agentic]
sources: [raw/papers/unknown-harness-updating-is-not-harness-benefit-disentangling-evolution-capabilities-in.md, raw/articles/2026-06-02-microsofts-new-mai-models.md]
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

## Microsoft MAI Models: Small-Parameter Contenders

**MAI-Thinking-1** (2026-06) — Microsoft's 35B-parameter reasoning model, claiming preference over Sonnet 4.6 in blind human side-by-side evaluations. Trained from scratch on enterprise-grade, clean, commercially licensed data without distillation from third-party models. Available to select early partners.

**MAI-Code-1-Flash** (2026-06) — 5B-parameter code-specialist model purpose-built for GitHub Copilot and VS Code. Rolling out to Copilot individual users in VS Code. Also trained end-to-end by Microsoft on clean and appropriately licensed data.

**Significance:**
- If MAI-Thinking-1's 35B-vs-Sonnet-4.6 claim holds, it suggests small-parameter models with clean training data can compete with much larger proprietary models on reasoning tasks
- Both models emphasize clean/licensed training data — a differentiator in an era where most models train on unlicensed web dumps
- MAI-Code-1-Flash at 5B suggests efficient code models can be deployed at low cost for IDE integration
- **For agent users:** Small-parameter models with strong reasoning could reduce costs significantly for mid-complexity agent tasks. Monitor benchmarks as these models become generally available.

## Harness Evolution: Which Models Benefit from Self-Improvement?

Research on harness self-evolution (2026-05) reveals counterintuitive findings about how different model tiers benefit from updating their external harnesses (prompts, skills, memories, tools) based on execution evidence.

**Key findings:**
- **Harness-updating is flat in base capability:** Models from different capability tiers produce harness updates that lead to surprisingly similar gains. Even Qwen3.5-9B's updates yield gains comparable to Claude Opus 4.6's updates.
- **Harness-benefit is non-monotonic in base capability:** Weak-tier models benefit little (fail to activate relevant harness artifacts or fail to follow them faithfully), mid-tier models benefit MOST, and strong-tier models benefit less than mid-tier.
- **Investment implication:** Invest capability budget in the task-solving agent rather than the evolver. A mid-tier model with updated harnesses outperforms expectations; a strong model's incremental gains from self-evolution are smaller.
- **Training implication:** Target harness invocation and long-horizon instruction following in agent training — these are the bottlenecks, not the ability to generate updates.

**For agent users:**
- Don't assume you need the strongest model to self-improve — mid-tier models may actually gain more from iterative prompt/memory refinement
- If your agents accumulate experience (memory, skill libraries, refined prompts), mid-tier models are the sweet spot for leveraging that accumulated knowledge
- Strong models are less dependent on harness quality — they compensate with raw capability
- Weak models can't effectively use harness artifacts even when they're good
