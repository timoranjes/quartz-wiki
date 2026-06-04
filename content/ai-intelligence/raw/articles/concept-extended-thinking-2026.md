---
title: Extended Thinking in LLMs
researched: 2026-06-05
sources:
  - https://platform.claude.com/docs/en/build-with-claude/extended-thinking
  - https://pub.towardsai.net/test-time-compute-what-thinking-models-actually-do-and-what-they-dont-8d587c1d93cd
  - https://hammansamuel.medium.com/what-thinking-mode-actually-does-in-llms-e310609d1a76
---

# Extended Thinking in LLMs

## Overview

Extended thinking is a capability in modern reasoning LLMs (such as OpenAI's o1/o3 models and Claude's extended thinking mode) that allows models to generate internal reasoning tokens before producing a final answer. Rather than predicting the next output token directly, the model generates a sequence of "thinking" tokens that represent step-by-step internal reasoning, enabling more complex problem-solving on tasks requiring math, logic, or multi-step analysis.

This approach shifts computation from training-time to inference-time (test-time compute), allowing a single model to effectively "think through" problems before responding. OpenAI's o1 and o3 models use this internally, while Claude provides API-level access to extended thinking with varying levels of transparency into the reasoning process. The technique has been shown to significantly improve performance on reasoning-heavy benchmarks compared to standard autoregressive generation.

## Key Details

### How It Works
- The model generates `thinking` content blocks containing internal reasoning before the `text` content block with the final response
- Thinking tokens are part of the model's output and count toward the token budget
- The model can be instructed to think step-by-step internally without exposing the reasoning to end users

### Claude Extended Thinking API
- **Manual Extended Thinking**: `thinking: {type: "enabled", budget_tokens: N}` — sets explicit token budget for reasoning
- **Adaptive Thinking**: `thinking: {type: "adaptive", effort: "low"|"medium"|"high"}` — model decides when and how much to think (recommended for Opus 4.6+, Sonnet 4.6+)
- **Display Options**:
  - `"summarized"`: Returns summarized reasoning (default on Opus 4.6, Sonnet 4.6, earlier 4.x)
  - `"omitted"`: Returns empty thinking field; only signature populated (default on Opus 4.8, 4.7, Mythos Preview)
- **Streaming**: Thinking can be streamed with `thinking_delta` events alongside `text_delta`

### Model Support
- **Claude Opus 4.8/4.7**: Adaptive thinking only (manual mode returns 400 error)
- **Claude Opus 4.6/Sonnet 4.6**: Adaptive thinking recommended; manual mode deprecated but still works
- **Claude Opus 4.5/4.1, Sonnet 4.5/4, Haiku 4.5 & earlier**: Both manual and adaptive supported
- **OpenAI o1/o3**: Uses extended thinking internally (no direct API control)

### Benefits
- Improved performance on complex reasoning tasks (math, logic, science)
- Transparency into model reasoning process (when display is not omitted)
- Controllable reasoning depth via budget_tokens or effort parameter

### Trade-offs
- Increased latency due to additional thinking tokens
- Higher token costs (thinking tokens are billed the same as output tokens)
- `display: "omitted"` reduces latency (no thinking streamed) but full thinking tokens are still billed

## Sources
- https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- https://pub.towardsai.net/test-time-compute-what-thinking-models-actually-do-and-what-they-dont-8d587c1d93cd
- https://hammansamuel.medium.com/what-thinking-mode-actually-does-in-llms-e310609d1a76
