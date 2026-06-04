---
title: Knowledge Distillation
researched: 2026-06-05
sources:
  - https://redis.io/blog/model-distillation-llm-guide/
  - https://link.springer.com/article/10.1007/s10462-025-11423-3
  - https://aclanthology.org/2025.sigdial-1.39/
  - https://neurips.cc/virtual/2025/poster/119420
---
# Knowledge Distillation

## Overview
Knowledge distillation (KD) is a model compression technique where a smaller *student* model learns to mimic the behavior of a larger *teacher* model. Instead of learning only from hard labels, the student learns from *soft targets* — probability distributions over possible outputs that encode richer relational knowledge.

## How Distillation Works

1. **Select Teacher Model**: Pre-trained large model (typically frozen during distillation)
2. **Design Student Architecture**: Significantly smaller, yet expressive enough to learn from teacher
3. **Generate Soft Labels**: Run training data through teacher to get output probability distributions
4. **Train with Combined Loss**:
   ```
   Total Loss = α × Distillation Loss + (1 - α) × Student Loss
   ```
   - **Distillation Loss**: How closely student matches teacher's soft outputs (KL divergence)
   - **Student Loss**: Standard cross-entropy against ground truth labels
   - **Temperature (T)**: Softens probability distributions (Hinton used T=20)
5. **Validate Performance**: Compare teacher, student baseline, and distilled student accuracy

## Benefits

| Benefit | Example |
|---------|---------|
| **Inference speed** | DistilBERT is ~60% faster |
| **Memory footprint** | TinyBERT-4 uses only 13.3% of BERT-base parameters (86.7% reduction) |
| **Cost reduction** | Lower GPU/energy usage |
| **Performance retention** | DistilBERT retains 97% accuracy on GLUE while being 40% smaller |

## Real-World Examples

### DistilBERT
- 40% smaller than BERT-base
- 60% faster inference
- 97% accuracy retention on GLUE benchmark

### TinyBERT
| Model | Parameters vs BERT | Inference Time | GLUE Performance |
|-------|-------------------|----------------|------------------|
| TinyBERT-4 | 13.3% | 10.6% | Slightly lower |
| TinyBERT-6 | ~100% | ~100% | On-par with BERT-Base |

## Types of Knowledge Distillation

| Category | Description | Key Techniques |
|----------|-------------|----------------|
| **Rationale-Based KD** | Distill reasoning steps (Chain-of-Thought), not just answers | CoT distillation, KPOD (Keypoint-based Progressive CoT) |
| **Uncertainty-Aware KD** | Bayesian approach with teacher-informed priors | BKD, uncertainty quantification via posterior sampling |
| **Multi-Teacher KD** | Combine knowledge from multiple teacher models | Ensemble fusion, confidence-aware weighting, DIVERSEDISTILL |
| **Dynamic/Adaptive KD** | Simultaneous training of teacher and student | BiLD Loss, self-distillation |
| **Task-Specific KD** | Domain-specific distillation | Instruction tuning, RLVR fine-tuning |

## Distillation vs. Other Compression Techniques

| Technique | Best For | Tradeoffs |
|-----------|----------|-----------|
| **Quantization** | Fast deployment, memory savings | Modest quality loss; 4-bit can drop 10–15% on agent benchmarks |
| **Pruning** | Reducing FLOPs and parameter count | Up to 60% sparsity with minimal accuracy loss |
| **Distillation** | Preserving capability during compression | Requires retraining; best when long-term inference savings justify upfront cost |

### Optimal Compression Ordering: P-KD-Q
Research shows the sequence **Pruning → Distillation → Quantization** is most effective. Quantizing before distillation can cause 10x perplexity increase.

## Dataset Distillation (DD)
- Complements KD by condensing large training datasets into compact synthetic ones
- Preserves essential learning signals while drastically reducing data demands
- Methods: gradient/trajectory matching, GAN-based synthesis, coreset selection, Data Shapley
- DD acts as a critical enabler for KD by identifying high-impact training examples

## Recent Advances (2024–2026)
- **Data efficiency**: Some methods achieve effective distillation using <3% of original training data
- **Rationale-based distillation**: Transferring Chain-of-Thought reasoning, not just final answers
- **Progressive distillation**: KPOD quantifies step difficulty for progressive student learning
- **Bayesian KD**: Uncertainty-aware distillation with teacher-informed priors over student weights
- **Self-distillation**: Model acts as both teacher and student (e.g., AlphaFold's iterative self-training)

## Key Facts
1. Knowledge distillation transfers knowledge from teacher to student via soft targets (probability distributions) that encode richer relational information than hard labels.
2. DistilBERT achieves 97% accuracy retention on GLUE while being 40% smaller and 60% faster than BERT-base.
3. The optimal compression sequence is Pruning → Distillation → Quantization (P-KD-Q); quantizing before distillation degrades quality 10x.
4. Modern distillation can use <3% of original training data while maintaining performance.
5. Rationale-based distillation (RBKD) transfers reasoning steps (Chain-of-Thought) rather than just final answers.
6. Dataset Distillation (DD) complements KD by synthesizing compact, high-impact training datasets.

## Sources
