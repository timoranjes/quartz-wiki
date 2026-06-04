---
title: RLHF Training
researched: 2026-06-05
sources:
  - https://huggingface.co/blog/rlhf
  - https://www.ibm.com/think/topics/rlhf
  - https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/
  - https://arxiv.org/abs/2504.12501
---

# RLHF Training

## Overview

Reinforcement Learning from Human Feedback (RLHF) is a machine learning technique that aligns large language models with human values by using human preferences as a signal to optimize model behavior via reinforcement learning. RLHF enables models to go beyond next-token prediction and generate outputs that are more helpful, honest, and harmless. It was a key component in the development of ChatGPT, InstructGPT, Sparrow, and GopherCite.

The technique uniquely suits tasks where success is nebulous — like humor, helpfulness, or ethical alignment — because it leverages human judgment instead of rigid algorithmic definitions. RLHF has demonstrated that it can yield better performance than scaling model size alone; InstructGPT (1.3B parameters) was preferred by human labelers over the much larger GPT-3.5 (175B parameters).

## Key Details

### Four-Phase Training Pipeline

#### 1. Pre-training
- Starts with a pretrained LLM trained via standard next-token prediction
- Model size varies (OpenAI used ~175B GPT-3 variant; Anthropic used 10M-52B)
- RLHF training uses less than 2% of the compute/data needed for pre-training

#### 2. Supervised Fine-Tuning (SFT)
- Aligns model output format with user expectations
- Human experts provide labeled (prompt, response) pairs
- DeepMind used filtering heuristics on MassiveWeb to extract high-quality SFT data
- Example: Transforming terse completions into comprehensive step-by-step guides

#### 3. Reward Model Training
- **Goal**: Convert human preferences into a scalar reward signal
- **Data Collection**: Prompts from user-submitted API calls or crowdsourced (e.g., Anthropic's HH-RLHF dataset)
- **Ranking Methods**: Head-to-head comparisons (Elo rating), binary feedback, multi-dimensional feedback
- **Model Size**: Reward model should have comparable capacity to the LM to understand nuanced outputs
- **Key Insight**: Ranking (not scoring) is preferred to avoid noisy, uncalibrated scores

#### 4. Policy Optimization
- **RL Formulation**:
  - Policy: Fine-tuned LM (generates text from prompts)
  - Action space: Vocabulary tokens (~50k)
  - Reward function: r = r_θ − λ · r_KL (preference score minus KL divergence penalty)
- **KL Penalty**: Prevents degenerate outputs that fool the reward model
- **PPO (Proximal Policy Optimization)**: Industry standard; clips updates to prevent drastic policy shifts
- **Parameter Freezing**: Open-source RLHF often uses PEFT (LoRA/adapters); large labs may fine-tune full model

### Key Results
- **InstructGPT**: 1.3B model with RLHF outperformed 175B GPT-3.5 on human preference
- **GPT-4 + RLHF**: Doubled accuracy on adversarial questions
- **Data Efficiency**: RLHF training uses less than 2% of pre-training compute

### Open-Source Tools
- **TRL**: Hugging Face ecosystem library for RL fine-tuning (PPO, easy integration)
- **TRLX**: Fork for large-scale RLHF (supports up to 33B models)
- **RL4LMs**: Modular RL library (PPO, NLPO, A2C, TRPO; 2000+ benchmarked experiments)

### Limitations
- **Data Quality Dependency**: Performance heavily depends on quality of human feedback
- **Reward Hacking**: Models may learn to game the reward model rather than genuinely improve
- **Scalability**: Collecting high-quality human preferences is expensive and time-consuming
- **Value Alignment**: Whose values? Preferences vary across cultures and contexts
- **Training Instability**: PPO can be unstable; requires careful hyperparameter tuning

## Sources
- https://huggingface.co/blog/rlhf
- https://www.ibm.com/think/topics/rlhf
- https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/
- https://arxiv.org/abs/2504.12501
