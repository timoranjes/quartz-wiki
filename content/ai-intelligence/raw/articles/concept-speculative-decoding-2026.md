---
title: Speculative Decoding
researched: 2026-06-05
sources:
  - https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/
  - https://research.google/blog/looking-back-at-speculative-decoding/
  - https://arxiv.org/abs/2308.04623
  - https://medium.com/ai-science/speculative-decoding-make-llm-inference-faster-c004501af120
---

# Speculative Decoding

## Overview

Speculative decoding is an inference optimization technique that accelerates large language model generation by predicting and verifying multiple tokens in parallel, significantly reducing latency without sacrificing output quality. The core idea uses a lightweight draft mechanism to propose several tokens at once, then verifies them in a single forward pass of the larger target model, collapsing multiple sequential inference steps into one.

Standard autoregressive decoding is inherently sequential — each token requires a full forward pass through the model. This leads to underutilized GPU compute, high latency due to repeated weight reloading, and poor system efficiency at scale. Speculative decoding addresses this by introducing a draft-verify cycle where a smaller, faster model proposes tokens that the larger model then validates in parallel.

## Key Details

### Draft-Target Approach (Classic)
A two-model system where:
- **Target model**: Large, high-quality LLM (e.g., Llama-3.2-70B)
- **Draft model**: Smaller, faster model (e.g., distilled 1B version), trained to mimic target behavior

#### Workflow
1. **Draft Generation**: Draft model proposes 3-12 tokens in one pass
2. **Parallel Verification**: Target model processes input + draft tokens in one forward pass, computing probabilities for all positions
3. **Rejection Sampling**: Tokens accepted only if P_target ≥ P_draft. If rejected, all subsequent draft tokens are discarded

#### Key Properties
- **Output Quality**: Identical to what the target model would have produced (no quality degradation)
- **Acceptance Rate**: Ratio of accepted tokens to total draft tokens; higher acceptance = greater speedup
- **Worst Case**: All draft tokens rejected → 1 token generated (same as baseline)
- **Speedup**: Typically 2-3x improvement in inference speed

### EAGLE-3: Draft-Free Speculative Decoding
EAGLE (Extrapolation Algorithm for Greater Language-Model Efficiency) eliminates the need for a separate draft model:
- Uses a lightweight **EAGLE head** attached to internal layers of the target model
- Takes multi-layer embeddings (low/mid/high-level) from target model
- Generates a **tree of candidate tokens** via multi-step autoregressive prediction
- Target model verifies all branches in parallel using **tree attention**, pruning invalid paths
- Instance-adaptive: stops drafting when confidence drops below threshold

### Multi-Token Prediction (MTP)
Used in models like DeepSeek-R1:
- Multiple prediction heads attached to the target model
- Head 1 predicts 1st draft token, Head 2 predicts 2nd, etc.
- Target model verifies in order and keeps longest matching prefix
- No separate draft model needed

### Benefits
- **No Quality Loss**: Output is provably identical to target model's own generation
- **Latency Reduction**: Collapses multiple sequential steps into single forward passes
- **GPU Utilization**: Better uses GPU compute by batching token verification
- **Training Efficiency**: Draft model can be distilled from target model

### Trade-offs
- Requires additional compute for draft generation (though draft model is much smaller)
- Effectiveness depends on draft-target alignment (how well draft mimics target)
- EAGLE-3 adds model complexity with additional heads
- Not effective for highly creative/unpredictable generation tasks

### Google Research Perspective
Google's retrospective on speculative decoding notes it has proven to be "an effective technique for faster and cheaper inference from LLMs without compromising quality," establishing it as a fundamental strategy for production LLM serving.

## Sources
- https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/
- https://research.google/blog/looking-back-at-speculative-decoding/
- https://arxiv.org/abs/2308.04623
- https://medium.com/ai-science/speculative-decoding-make-llm-inference-faster-c004501af120
