---
title: Extended Thinking / Reasoning Mode
created: 2026-06-01
updated: "2026-06-20"
type: concept
tags:
  - reasoning
  - inference
sources:
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-anthropic-2026.md
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-google-gemini-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
  - raw/articles/llm-provider-stepfun-2026.md
  - raw/articles/llm-provider-minimax-2026.md
  - raw/articles/llm-provider-perplexity-2026.md
  - raw/articles/llm-provider-cohere-2026.md
  - raw/articles/llm-provider-nvidia-2026.md
  - raw/articles/llm-provider-microsoft-phi-2026.md
confidence: high
---

# Extended Thinking / Reasoning Mode

## Overview

Extended thinking (also called reasoning mode, thinking mode, or chain-of-thought mode) allows LLMs to generate internal reasoning traces before producing a final answer. This significantly improves performance on complex reasoning tasks including mathematics, coding, logical analysis, and multi-step planning.

## Provider Implementations

| Provider | Feature Name | Control Method | Best For |
|----------|-------------|----------------|----------|
| OpenAI | Reasoning Effort | `effort` parameter (low/medium/high) | Math, science, analysis |
| Anthropic | Extended Thinking | `thinking` parameter with token budget | Complex reasoning, analysis |
| DeepSeek | Thinking Mode | `thinking` parameter (true/false) | Math, coding, logic |
| Google | Gemini Thinking | Built-in reasoning with adjustable depth | Research, analysis |
| xAI | Grok Thinking | Reasoning toggle for complex queries | Analysis, debate |
| Mistral | Codestral Thinking | Extended reasoning for code tasks | Code generation, debugging |
| MiniMax | Thinking Mode | Reasoning parameter | Math, multi-modal reasoning |
| StepFun | Advisor Mode | Step-3.7-Flash reasoning mode | Enterprise analysis |
| Perplexity | Research Mode | Deep research with citations | Fact-checking, research |
| Cohere | Command Reasoning | Reasoning-optimized variant | Enterprise logic |
| Microsoft | Phi Reasoning | Extended thinking for Phi-4 | On-device reasoning |
| NVIDIA | Nemotron Reasoning | Reasoning-optimized Nemotron variants | Enterprise logic |

## Performance Impact

### Benchmarks with Extended Thinking

| Model | Reasoning Mode | AIME 2025 | GPQA Diamond | Codeforces |
|-------|---------------|-----------|-------------|------------|
| DeepSeek V4 Pro Max | Thinking ON | — | — | 3206 (Grandmaster) |
| Claude Opus 4.6 | Thinking ON | — | — | — |
| GPT-5.5 | High effort | Leading | Leading | — |
| Gemini 3.5 Pro | Thinking ON | — | — | — |
| Grok 4.3 | Thinking ON | Competitive | Competitive | — |
| Kimi K2 | Reasoning ON | — | — | — |

### Token Overhead

- Extended thinking typically adds 2-10× more tokens to each response
- DeepSeek V4 Flash: thinking mode costs $0.28/M output tokens (same as regular)
- OpenAI: reasoning effort high costs significantly more per output token
- Anthropic: thinking budget controlled by user (e.g., 1024, 4096 tokens)

## Use Cases

- **Mathematics**: AIME, Putnam, IMO-level problems require extended reasoning
- **Coding**: Complex debugging, architecture design, algorithm optimization
- **Research**: Multi-step analysis, hypothesis generation, literature synthesis
- **Planning**: Multi-objective optimization, constraint satisfaction
- **Legal/Financial**: Contract analysis, risk assessment, compliance checking

## Open Debates

- **CoT leakage**: Should reasoning traces be exposed to users or hidden? Security implications of leaked reasoning
- **Over-reliance**: Does extended thinking mask fundamental model weaknesses?
- **Cost vs benefit**: When is the token overhead justified? For simple queries, thinking mode wastes tokens
- **Alignment interference**: Does alignment training conflict with honest reasoning traces?

## MARS: Early Stopping for Parallel Test-Time Scaling (June 2026)

**MARS** (Margin-Adversarial Risk-controlled Stopping, arXiv:2606.12935) addresses the computational overhead of parallel test-time scaling — where many reasoning traces are sampled and majority-voted.

### Key Observation
Probing **partial traces** at intermediate checkpoints can extract current answers without disrupting generation, revealing an evolving aggregate vote. This enables early stopping without waiting for all traces to complete.

### Method
- Estimates which active traces are likely to change their answers
- Stops once the leader remains safe under a conservative bound on future vote movement
- Separates two uncertainty sources:
  1. **Trace-level switch probabilities** (learned via 5-feature logistic model, closely matches oracle)
  2. **Switching destination** (handled via adversarial bound calibrated from warmup traces)
- With true switch probabilities: guarantees with high probability that early-stopped answer matches full-budget vote

### Results
- Across 3 reasoning models and 3 competition-math benchmarks:
  - Saves **25-47% of self-consistency tokens**
  - Saves **14-29% on top of DeepConf Online** (a strong confidence-weighted baseline that already filters and truncates weak traces)
  - **Matches accuracy** of full-budget baselines

### Implications
- Test-time compute scaling doesn't need to run all traces to completion
- Early stopping is especially valuable for expensive reasoning models where each trace costs significant compute
- Complements other efficiency methods (can stack with confidence-weighted sampling)

Sources: [arXiv:2606.12935](https://arxiv.org/abs/2606.12935) ^[raw/papers/unknown-mars-margin-adversarial-risk-controlled-stopping-for-parallel-llm-test-time-scal.md]

## SEVRA: Selective Verification for Budget-Aware Reasoning (June 2026)

**SEVRA** (Selective Verification for Reasoning Allocation, arXiv:2606.19808) addresses test-time reasoning as a **deployment allocation problem**, not a new-verifier problem.

### Key Insight
Extra reasoning is not uniformly valuable — it can repair failed attempts, waste compute on already-correct answers, or introduce harmful answer changes. The question is: **when should you verify vs. when should you just think longer?**

### Method
- Serving-layer controller decides whether to preserve a frozen solver's initial answer or invoke active verification
- Trains **recoverability-aware gates** from serving-visible attempt state
- Using frozen Qwen3-4B solver on MathFive:
  - Selective verification: **76.3% accuracy** vs. 75.5% for always verifying
  - **26.8% reduction** in post-generation tokens
  - Harmful flips reduced from **2.2% → 1.0%**
- However, an 8,192-token initial solve reaches 76.0% with **28% fewer total tokens** — showing selective recovery is useful but not always the best cost frontier
- On GSM: selective policy verifies only 3.0% of examples, improves 93.4% → 94.5%, reduces verification tokens by **91.2%**

### Deployment Rule
**Tune the initial budget first, then use selective recovery** when explicit checks, bounded retries, auditability, or regression-risk control matter. Self-Consistency@5 on CommonsenseQA improves accuracy at ~5× the realized token cost — always-on verification hurts.

Sources: [arXiv:2606.19808](https://arxiv.org/abs/2606.19808) ^[raw/papers/unknown-think-again-or-think-longer-selective-verification-for-budget-aware-reasoning.md]

## Related

- [[rlhf-training]] — Reasoning modes require specialized alignment techniques
- [[context-windows]] — Extended thinking consumes context budget rapidly
- [[distillation]] — Reasoning capabilities are distilled from large models into smaller ones
- [[evaluation-benchmarks]] — Test-time scaling evaluation
