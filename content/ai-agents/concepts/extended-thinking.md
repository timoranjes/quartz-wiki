---
title: Extended Thinking
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - reasoning
  - inference
  - chain-of-thought
sources:
  - "OpenAI o1 and o3 Technical Reports"
  - "Anthropic Extended Thinking API Documentation"
  - "DeepSeek R1 Reasoning Model Paper"
  - "Google Gemini Extended Thinking Release Notes"
  - "xAI Grok Thinking Mode Documentation"
  - "Modeling Hierarchical Thinking in Large Reasoning Models"
  - "Chain-of-Thought Reasoning in the Wild Is Not Always Faithful"
  - "Evaluating Chain-of-Thought Monitorability"
  - "Reasoning Models Struggle to Control Their Chains of Thought"
confidence: high
---

# Extended Thinking

Extended thinking (also called reasoning mode, thinking mode, or chain-of-thought inference) enables LLMs to generate internal reasoning traces before producing a final answer. By allocating additional compute to the thinking process, models achieve significantly higher accuracy on complex reasoning, math, coding, and analysis tasks compared to standard inference.

---

## Definition

Standard LLM inference produces output tokens directly from the input prompt. Extended thinking introduces an intermediate reasoning phase: the model generates a hidden chain of thought (the "thinking tokens") that is not directly shown to the user (or is shown in a collapsible format), then produces the final answer conditioned on both the input and the reasoning trace. This allows the model to "think before it speaks."

### Key Properties

- **Compute scaling**: Accuracy improves monotonically with more thinking tokens — a fundamental shift from the fixed-compute inference of standard models.
- **Internal monologue**: The thinking trace is the model's internal reasoning process, which may include planning, self-correction, verification, and exploration of alternative approaches.
- **Non-determinism**: Different thinking traces for the same input can lead to different answers, enabling self-consistency voting.
- **Token cost**: Thinking tokens consume compute and may be billed differently than output tokens depending on the provider.

## OpenAI: o-Series and Reasoning Effort Levels

OpenAI's o-series models (o1, o3, o4-mini) pioneered commercial extended thinking:

- **o1** (Sep 2024): First commercial reasoning model. Trained with reinforcement learning on reasoning tasks. Automatically generates extended thinking for all queries. Achieves ~83% on AIME 2024 math competition, ~90% on GPQA (science PhD questions).
- **o3-mini** (Jan 2025): Faster, cheaper variant with configurable reasoning effort levels (low, medium, high). High effort produces longer thinking traces and higher accuracy.
- **o3** (Apr 2025): Full reasoning model with multimodal thinking — can reason about images, not just text. Achieves near-human performance on many reasoning benchmarks.
- **o4-mini** (Apr 2025): Optimized for speed with reduced thinking overhead, suitable for interactive use.
- **GPT-5 reasoning** (Aug 2025): GPT-5 incorporates reasoning capabilities with configurable thinking effort. Users can enable "thinking mode" for complex queries.
- **GPT-5.1** (Nov 2025): Improved reasoning with better self-correction and reduced hallucination in thinking traces.
- **Reasoning effort levels**:
  - **Low**: Minimal thinking, fast response, suitable for straightforward queries
  - **Medium**: Moderate thinking depth, balanced speed/accuracy
  - **High**: Maximum thinking depth, slower but most accurate for complex problems
- **Thinking token billing**: OpenAI charges separately for thinking tokens at a reduced rate compared to output tokens.

## Anthropic: Extended Thinking for Claude

Anthropic introduced extended thinking as an API feature for Claude models:

- **Claude 3.5 Sonnet with extended thinking**: First Claude model to support configurable thinking tokens via the API.
- **API control**: Developers specify `thinking` parameter with `type: "enabled"` and optionally `budget_tokens` to control maximum thinking length.
- **Transparent thinking**: Claude's thinking tokens are returned in the API response, allowing developers to inspect the reasoning process.
- **Claude Code integration**: Claude Code uses extended thinking internally for complex code analysis and multi-step debugging tasks.
- **Claude Opus 4.8** (May 2026): Extended thinking integrated with improved self-correction, reducing errors in math and coding by ~40% compared to non-thinking mode.
- **Thinking budget**: Users can set a token budget (e.g., 16K, 32K, 64K tokens) for thinking, trading latency for accuracy.
- **Safety considerations**: Anthropic's containment research shows that extended thinking traces are monitored for safety-relevant patterns.

## DeepSeek: R1 and Native Reasoning

DeepSeek's R1 represents a different approach — reasoning is baked into the model's core training:

- **DeepSeek-R1-Zero**: Trained purely with reinforcement learning (GRPO) on reasoning tasks, without SFT. Discovered emergent reasoning behaviors including self-reflection, verification, and strategy switching.
- **DeepSeek-R1**: Enhanced version with a cold-start SFT phase before RL, achieving more stable and interpretable reasoning traces.
- **Native thinking**: Unlike other providers where thinking is an API toggle, DeepSeek-R1 naturally generates reasoning traces as part of its normal output.
- **Hybrid thinking mode** (2025): DeepSeek supports both reasoning mode (with thinking traces) and direct answer mode, with automatic routing based on query complexity.
- **Distilled variants**: R1-Distill-Qwen and R1-Distill-Llama models at 1.5B–70B parameters inherit reasoning capabilities, enabling reasoning at much lower cost.
- **Performance**: R1 achieves ~96% on MATH-500, ~79.8% on AIME 2024, outperforming OpenAI o1 on several benchmarks.

## Google Gemini: Extended Thinking Integration

Google's approach to extended thinking in Gemini:

- **Gemini 2.5 Pro**: Supports extended thinking natively, with thinking traces generated automatically for complex queries.
- **Gemini extended thinking mode** (May 2026): Explicit API support for configurable thinking depth, similar to Anthropic's approach.
- **Flash thinking**: Gemini Flash models include a lightweight thinking mode for faster reasoning with moderate accuracy gains.
- **Multi-modal reasoning**: Gemini can think about images, audio, and video simultaneously, enabling reasoning across modalities.
- **TPU optimization**: Gemini's thinking mode is optimized for TPU hardware, with efficient parallel processing of thinking tokens.

## xAI Grok: Thinking Mode

xAI's Grok models incorporate thinking capabilities:

- **Grok 3 thinking mode**: Configurable reasoning depth for the Grok 3 model, integrated with xAI's real-time knowledge access.
- **Grok 4** (May 2026): Improved thinking with better self-correction and reduced circular reasoning.
- **Integration with X platform**: Grok's thinking mode is accessible through the X platform, with thinking traces optionally visible to users.
- **Colossus infrastructure**: xAI's large GPU cluster enables extended thinking at scale, supporting high concurrent thinking sessions.

## Hierarchical Thinking Research

Recent research reveals that extended thinking is not monolithic:

- **Hierarchical thinking** (2025): Models organize reasoning into hierarchical levels — high-level planning, mid-level strategy, low-level execution. This structure enables more robust reasoning.
- **Thoughts-as-planning**: Thinking traces function as latent world models, enabling the model to simulate outcomes before committing to an answer.
- **Faithfulness concerns**: Research shows that chain-of-thought reasoning in the wild is not always faithful to the model's actual decision process. Models may generate plausible-sounding reasoning that doesn't reflect their true computation.
- **Monitorability** (Dec 2025): OpenAI research on evaluating whether reasoning traces can be reliably monitored for safety-relevant patterns.
- **Self-control limitations** (Mar 2026): Research showing that reasoning models struggle to control their chains of thought, which is actually beneficial — it prevents models from "hiding" problematic reasoning.

## Trade-offs

| Aspect | Details |
|--------|---------|
| **Accuracy gain** | 10–40% improvement on reasoning benchmarks vs. non-thinking mode |
| **Latency** | 2–10× longer time-to-first-token, proportional to thinking budget |
| **Token cost** | Thinking tokens typically cost 50–80% of output tokens |
| **Best for** | Math, coding, complex analysis, multi-step planning, verification |
| **Worst for** | Simple Q&A, creative writing, tasks requiring immediate response |
| **Self-consistency** | Running multiple thinking traces and voting improves accuracy further |

## Open Questions

- **Thinking token optimization**: What's the optimal number of thinking tokens for a given task? Can models learn to self-allocate thinking budget?
- **Reasoning faithfulness**: Do thinking traces faithfully represent the model's computation, or are they post-hoc rationalizations?
- **Thinking compression**: Can we compress thinking traces to reduce token cost while preserving reasoning quality?
- **Multi-agent reasoning**: How should thinking traces be shared in multi-agent systems? Should agents expose their reasoning to each other?
- **Thinking safety**: Can models learn to hide harmful reasoning in their thinking traces? How can we monitor thinking for safety?

## Related Concepts

- [[rlhf-training]] — reasoning models are aligned using RLHF with reasoning-specific rewards
- [[distillation]] — reasoning capabilities can be distilled into smaller models
- [[speculative-decoding]] — thinking mode generates tokens sequentially, benefiting from speculation
- [[context-windows]] — longer thinking traces require larger context windows
- [[agent-safety]] — monitoring thinking traces is a key agent safety technique
