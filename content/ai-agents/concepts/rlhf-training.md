---
title: RLHF Training
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - alignment
  - training
  - reinforcement-learning
sources:
  - "DeepSeek GRPO Technical Report"
  - "Anthropic Constitutional AI Paper"
  - "OpenAI InstructGPT and PPO Research"
  - "Google RLAIF and Sparrow Paper"
  - "Meta Llama 4 Alignment Technical Report"
  - "Tournament-GRPO: Group-Wise Tournament Rewards"
  - "GRPO is Secretly a Process Reward Model"
  - "Constitutional Arms Races in the Public Goods Game"
  - "Alignment Tampering: How RLHF is Exploited"
  - "Detecting and Reducing Scheming in AI Models"
confidence: high
---

# RLHF Training

Reinforcement Learning from Human Feedback (RLHF) is the dominant paradigm for aligning large language models with human preferences. By training a reward model on human preference data and then optimizing the language model against that reward signal using reinforcement learning, RLHF transforms a base model that predicts text into an instruction-following assistant that produces helpful, honest, and harmless outputs.

---

## Definition

RLHF consists of three stages:

1. **Supervised Fine-Tuning (SFT)**: The base model is fine-tuned on high-quality instruction-response pairs, establishing basic instruction-following capability.
2. **Reward Model Training**: A separate reward model is trained on human preference data — pairs of responses ranked by human annotators — to predict which responses humans prefer.
3. **Reinforcement Learning Optimization**: The SFT model is optimized against the reward model using RL (typically PPO), maximizing reward while staying close to the original model via a KL penalty.

## OpenAI: PPO and the RLHF Pipeline

OpenAI pioneered RLHF with InstructGPT (2022) and has iterated extensively:

- **Proximal Policy Optimization (PPO)**: The canonical RL algorithm for LLM alignment. PPO updates the policy using clipped surrogate objectives, preventing destructive large updates.
- **Reward model architecture**: Typically a transformer-based classifier trained on pairwise preference data (chosen vs. rejected responses).
- **KL penalty**: Critical regularization that prevents the policy from drifting too far from the SFT model, which would produce degenerate outputs.
- **Process supervision**: OpenAI's research (2023) showed that supervising individual reasoning steps (process rewards) outperforms outcome-only supervision on math tasks by ~30%.
- **Deliberative alignment** (Dec 2024): New approach using reasoning traces to enable safer language models, combining chain-of-thought with alignment objectives.
- **Model distillation for alignment** (Oct 2024): OpenAI's distillation API transfers alignment behaviors from larger models (GPT-4o) to smaller ones (GPT-4o-mini), preserving safety characteristics.
- **GPT-5 system card** (Aug 2025): Introduced refined alignment pipeline with improved reward modeling and reduced sycophancy through adversarial training.

## DeepSeek: Group Relative Policy Optimization (GRPO)

DeepSeek introduced GRPO as a simpler, more efficient alternative to PPO:

- **Group-based comparison**: Instead of training a separate reward model, GRPO samples multiple outputs from the current policy for each prompt, ranks them, and uses the relative ranking as the reward signal. This eliminates the need for a separate reward model.
- **No critic network**: Unlike PPO which requires a value function (critic), GRPO uses group-relative advantages, reducing memory requirements by ~50%.
- **DeepSeek-R1**: Trained using GRPO on reasoning tasks, achieving state-of-the-art results on math and coding benchmarks without RLVR (RL with verifiable rewards).
- **Simplicity advantage**: GRPO's lack of a separate reward model and critic means fewer hyperparameters to tune and less training infrastructure.
- **Research validation**: "GRPO is Secretly a Process Reward Model" (arXiv 2025) showed that GRPO implicitly learns process-level reward signals, explaining its strong performance on reasoning tasks.
- **Tournament-GRPO**: Extension that uses tournament-style comparisons instead of simple group rankings, improving reward signal quality.

## Anthropic: Constitutional AI and Claude Alignment

Anthropic developed Constitutional AI as a scalable alternative to human-in-the-loop RLHF:

- **Constitutional AI pipeline**:
  1. Generate responses from a base model
  2. Use AI feedback (guided by a "constitution" of principles) to critique and revise responses
  3. Train the model on revised responses (SFT phase)
  4. Train an AI preference model using constitutional critiques
  5. Optimize the model against the AI preference model (RL phase)
- **Scalability**: By replacing human annotators with AI feedback guided by principles, Constitutional AI can generate orders of magnitude more training data.
- **Claude family**: All Claude models (Haiku, Sonnet, Opus) are trained using Constitutional AI variants, with each generation incorporating lessons from the previous.
- **Constitution evolution**: Anthropic's constitution has evolved across Claude generations, adding more nuanced principles for harmlessness, helpfulness, and honesty.
- **Claude Opus 4.8** (May 2026): Latest iteration with improved alignment on edge cases, reduced refusal rates on benign requests, and better handling of ambiguous instructions.
- **Containment research** (May 2026): Anthropic published detailed analysis of how Claude is contained across products, including alignment mechanisms and safety evaluation results.

## Google: RLAIF and Sparrow

Google's approach emphasizes AI-assisted feedback:

- **RLAIF (Reinforcement Learning from AI Feedback)**: Similar to Constitutional AI but developed independently. Uses a larger model to generate preference labels for training the reward model.
- **Sparrow**: Google's dialogue agent trained with RLAIF, demonstrating that AI-generated preference data can substitute for human annotations.
- **Gemma alignment**: Google's open-weight Gemma models are aligned using techniques distilled from Gemini, including preference optimization and safety fine-tuning.
- **Gemini 2.5 Pro** (2025): Uses refined RLAIF with multi-modal preference data (text + image + reasoning trace preferences).
- **Self-improvement loop**: Google research explores models that iteratively improve their own alignment by generating and evaluating their own training data.

## Meta Llama 4: Alignment at Scale

Meta's alignment approach for Llama 4:

- **Llama 4 Maverick/Scout alignment**: Uses a combination of SFT, DPO (Direct Preference Optimization), and RLHF to align open-weight models.
- **Open-weight alignment challenge**: Aligning open-weight models requires balancing helpfulness with safety guardrails that can't be easily removed by downstream users.
- **DPO preference**: Meta increasingly uses DPO over PPO for its simplicity and stability. DPO directly optimizes the policy to prefer chosen over rejected responses without a separate reward model.
- **Community alignment**: Meta provides alignment tools and recipes so the community can fine-tune Llama models with custom preference data.
- **Safety benchmarks**: Llama 4 models are evaluated on comprehensive safety benchmarks before release, with detailed model cards documenting known limitations.

## Key Algorithms Compared

| Algorithm | Reward Model | Critic Network | Memory | Complexity | Primary Users |
|-----------|-------------|----------------|--------|------------|---------------|
| **PPO** | Yes (separate) | Yes | High | High | OpenAI, Anthropic |
| **GRPO** | No (group ranking) | No | Low | Low | DeepSeek |
| **DPO** | Implicit (pairwise) | No | Medium | Low | Meta, community |
| **RLAIF** | Yes (AI-generated) | Yes | High | High | Google |
| **Constitutional AI** | Yes (AI-guided) | Yes | High | Medium | Anthropic |

## Open Debates & Questions

- **Sycophancy**: RLHF-trained models tend to agree with user opinions even when incorrect. OpenAI's GPT-5 addressed this through adversarial training, but it remains an active research area.
- **Reward hacking**: Models can learn to game the reward model rather than genuinely improving helpfulness. How can we build reward models resistant to gaming?
- **Alignment tax**: Aligned models often sacrifice some capability compared to base models. What's the minimum capability loss needed for safe alignment?
- **Scheming detection** (Sep 2025): OpenAI research on detecting models that strategically comply with alignment objectives during evaluation while pursuing different goals in deployment.
- **Chain-of-thought monitorability** (Dec 2025): Can we verify that reasoning traces in aligned models faithfully represent the model's actual decision process?
- **Multi-model alignment**: When multiple AI systems interact, individual alignment may not guarantee collective safety. How do we align systems in multi-agent environments?

## Related Concepts

- [[distillation]] — alignment behaviors can be distilled from larger models to smaller ones
- [[extended-thinking]] — reasoning models combine extended thinking with alignment objectives
- [[agent-safety]] — RLHF is one component of comprehensive agent safety strategies
- [[evaluation-benchmarks]] — alignment quality is measured through specialized evaluation benchmarks
