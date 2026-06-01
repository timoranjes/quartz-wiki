---
domain: llm-providers
type: concept
tags: [concept/training, concept/alignment, concept/rlhf]
aliases: [RLHF, Reinforcement Learning from Human Feedback, DPO, PPO, GRPO]
created: 2026-06-01
---
# RLHF & Alignment Training

## Overview
Reinforcement Learning from Human Feedback (RLHF) and its successors are the primary methods for aligning LLMs with human preferences, safety requirements, and instruction-following capabilities.

## Training Pipeline

### Traditional RLHF (3-stage)
1. **Supervised Fine-Tuning (SFT)** — Train on high-quality instruction-response pairs
2. **Reward Model Training** — Train a separate model to score responses based on human preferences
3. **RL Optimization (PPO)** — Use the reward model to optimize the SFT model via Proximal Policy Optimization

### Direct Preference Optimization (DPO)
- Eliminates the separate reward model
- Directly optimizes policy on preference pairs
- Simpler, more stable, comparable quality to RLHF
- Adopted by most providers post-2024

### Group Relative Policy Optimization (GRPO)
- **DeepSeek's innovation** — no reward model needed
- Uses group-relative scoring within each prompt's output batch
- Significantly cheaper than PPO (no separate reward model)
- Key to DeepSeek's cost advantage in reasoning training

### Reinforcement Learning with AI Feedback (RLAIF)
- Uses AI (not humans) to generate preference labels
- Scales to much larger datasets than human-labeled RLHF
- Quality depends on the judge model

## Provider Alignment Approaches

| Provider | Primary Method | Reasoning Training |
|----------|---------------|-------------------|
| **OpenAI** | RLHF + RLAIF | o-series trained with RL on verified outputs |
| **Anthropic** | **Constitutional AI** + RLHF | Claude trained with constitutional principles |
| **Google** | RLHF + RLAIF | Gemini uses reinforcement learning at scale |
| **Meta** | DPO-based | Llama 4 uses direct preference optimization |
| **DeepSeek** | **GRPO** (no reward model) | R1 trained via pure RL (cold-start + GRPO) |
| **Alibaba** | DPO + ORPO | Qwen uses direct preference optimization |
| **Mistral** | DPO + ORPO | European approach to alignment |
| **xAI** | RLHF | Grok uses reinforcement learning |

## Reasoning Model Training (2026)

### DeepSeek R1 Approach (Most Documented)
1. **Cold Start** — SFT on a small set of long CoT data
2. **RL Phase** — GRPO with rule-based rewards (correctness, format)
3. **SFT Refinement** — Fine-tune RL outputs for readability
4. **Further RL** — Additional GRPO for general capabilities

### OpenAI o-series Approach
- Trained on verified problem-solving outputs
- Heavy emphasis on correctness verification
- Separate model family from GPT line

### Anthropic Extended Thinking
- Added as a feature to existing models (not separate training)
- Effort levels control internal reasoning depth
- Constitutional AI constraints still apply during thinking

## Key Considerations
- **Data quality > quantity** — Clean preference data is critical
- **Reward hacking** — Models can game reward models; GRPO mitigates this
- **Over-optimization** — Can degrade capabilities on non-aligned tasks
- **Safety tax** — Alignment can reduce raw capability; trade-off varies by provider

## Related
- [[extended-thinking]] — Reasoning models use RL heavily in training
- [[deepseek]] — GRPO is DeepSeek's key training innovation
- [[anthropic]] — Constitutional AI is Anthropic's alignment approach
