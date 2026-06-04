---
title: RLHF and Alignment Training
created: 2026-06-01
updated: 2026-06-02
type: concept
tags:
  - training
  - alignment
  - optimization
sources:
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-anthropic-2026.md
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-google-gemini-2026.md
  - raw/articles/llm-provider-meta-llama-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
confidence: high
---

# RLHF and Alignment Training

## Overview

Reinforcement Learning from Human Feedback (RLHF) and its variants (DPO, GRPO, RLAIF, PPO) are the primary methodologies for aligning LLM outputs with human preferences after pre-training. These techniques transform a raw, next-token predictor into a helpful, harmless, and honest assistant.

## Alignment Methodologies

### PPO (Proximal Policy Optimization)

The original RLHF approach:
1. Collect human preference data (pairwise comparisons)
2. Train a reward model to predict human preferences
3. Fine-tune the base model using PPO to maximize reward
4. Used by OpenAI for GPT series alignment

**Status in 2026**: Still used for GPT-5.5 refinements but largely superseded by simpler alternatives for most providers.

### DPO (Direct Preference Optimization)

Simplifies PPO by directly optimizing the policy on preference data without a separate reward model:
- **Advantage**: More stable, easier to implement, lower compute cost
- **Adoption**: Widely used across open-weight providers (Mistral, DeepSeek distills, Meta Llama)
- **Variants**: IPO, KTO, ORPO — each with different loss formulations

### GRPO (Group Relative Policy Optimization)

Introduced by DeepSeek for mathematical reasoning:
- Uses group-relative scoring instead of pairwise comparisons
- Particularly effective for math and coding tasks where correctness is verifiable
- DeepSeek R1 and V4 families use GRPO for reasoning alignment
- Eliminates the need for a separate reward model

### RLAIF (Reinforcement Learning from AI Feedback)

Uses an AI model (rather than humans) to generate preference labels:
- **Advantage**: Scales to millions of training examples without human cost
- **Adoption**: Google Gemini uses RLAIF at scale for alignment
- **Risk**: Potential for reward hacking if the AI judge has blind spots

### Constitutional AI (Anthropic)

Anthropic's distinctive approach:
1. Generate responses from the base model
2. Evaluate against a "constitution" of principles (harmlessness, helpfulness, honesty)
3. Revise responses that violate principles
4. Train the model on revised examples
5. **Result**: Claude models aligned to constitutional principles without extensive human labeling

## Provider Alignment Strategies (2026)

| Provider | Primary Method | Notes |
|----------|---------------|-------|
| OpenAI | PPO | GPT-5.5 uses PPO with refined reward models |
| Anthropic | Constitutional AI + RLHF | Claude Opus 4.8: constitutional principles + human feedback |
| DeepSeek | GRPO | V4 and R1 families use GRPO for reasoning alignment |
| Google | RLAIF | Gemini 3.5: AI-generated feedback at massive scale |
| Meta | DPO + Codistillation | Llama 4 aligned via DPO; teacher model provides preference signal |
| xAI | DPO + Reinforcement | Grok 4.3 uses DPO with real-time feedback |
| Mistral | DPO | Open-weight models aligned via DPO on public preference datasets |
| Alibaba | RLHF + DPO | Qwen3.7 combines both for Chinese and English alignment |
| Zhipu AI | RLHF | GLM-5 uses RLHF with Chinese preference data |
| Cohere | RLHF | Command A+ aligned for enterprise safety and instruction following |
| MiniMax | RLHF + DPO | Multi-modal alignment for text and image outputs |

## Alignment Challenges

- **Reward hacking**: Models learn to game the reward model rather than genuinely improving
- **Over-refusal**: Excessive alignment can cause models to refuse benign requests
- **Capability loss**: Alignment can reduce raw performance on coding and reasoning tasks
- **Cultural bias**: Human preference data reflects cultural biases of the labeling population
- **Alignment tampering**: Recent research shows aligned models can develop deceptive behavior under distribution shift

## Open Debates

- **Is RLHF necessary?**: Some argue continued scaling reduces the need for post-training alignment
- **GRPO vs DPO**: Which is more sample-efficient for reasoning tasks? DeepSeek's GRPO results are compelling but not yet widely replicated
- **AI vs human judges**: Can RLAIF replace human-labeled data entirely, or do human judgments capture nuances AI misses?

## Related

- [[extended-thinking]] — Reasoning modes require specialized alignment to prevent CoT leakage
- [[distillation]] — Aligned models are often distilled into smaller, cheaper models
- [[moE-architecture]] — MoE routing affects how alignment signals propagate through experts
