
# Speculative Decoding

Speculative decoding is a family of inference optimization techniques that reduce latency by having a smaller "draft" model generate candidate tokens in parallel, which a larger "target" model then verifies — accepting correct tokens and rejecting incorrect ones. This can achieve 2–4× speedup without sacrificing output quality.

---

## Definition

Traditional autoregressive decoding generates one token per forward pass, making inference sequential and latency-bound. Speculative decoding breaks this constraint: a lightweight draft model proposes a sequence of $k$ tokens ahead, and the target model evaluates all $k$ candidates in a single forward pass, accepting correct tokens and resampling rejected ones. The result is fewer total forward passes for the same output.

## Variants & Techniques

### EAGLE / EAGLE-2 / EAGLE-3

**EAGLE** (Extrapolation-based Accelerated Generation for LLMs) uses an auxiliary draft head trained to predict future tokens conditioned on the target model's hidden states. EAGLE-2 and EAGLE-3 improve draft quality through better feature extraction and training procedures, achieving higher acceptance rates (often 70–90%) than simple n-gram speculation.

### Medusa

**Medusa** adds multiple independent decoding heads to a model, each trained to predict tokens at different positions ahead (head 1 predicts $t+1$, head 2 predicts $t+2$, etc.). Unlike EAGLE, Medusa heads operate in parallel rather than sequentially, enabling fast speculative generation with a single model rather than a separate draft model.

### Lookahead Decoding

Lookahead decoding uses n-gram matching to identify repeated sequences in the context and speculatively emits matching continuations. This is particularly effective for code generation and repetitive structured text where patterns recur frequently.

## Provider Implementations

### Meta Llama

Meta has integrated speculative decoding into its inference optimization toolchain. Llama models support EAGLE-style draft heads and Medusa configurations for self-hosted deployments. The Llama 4 family (Maverick, Scout) can leverage speculative decoding through vLLM and llama.cpp, with reported 2–3× throughput improvements on generation-heavy workloads.

### DeepSeek

DeepSeek's MoE architecture (V4: 1.6T total / 49B active) pairs naturally with speculative decoding — the sparse activation pattern means draft models can be even more lightweight relative to the full model. DeepSeek V4 supports speculative decoding inference, and together with its aggressive KV cache reuse, achieves exceptional token-per-second throughput.

### Google Gemini

Google Gemini supports lookahead decoding and speculative decoding via its TPU-optimized inference stack. Gemini's infrastructure benefits from speculative decoding's ability to better utilize TPU array parallelism, as the batched verification step maps well to TPU's strength in dense matrix operations.

### xAI Grok

xAI has explored speculative decoding variants for Grok models, leveraging its large-scale inference infrastructure. Speculative decoding is part of xAI's optimization toolkit alongside its own KV cache strategies.

### Together AI

Together AI offers speculative decoding as an inference optimization option for hosted Llama and other open-weight models, allowing users to trade off draft model size against acceptance rate and throughput.

## Trade-offs

| Aspect | Details |
|--------|---------|
| **Speedup** | 2–4× depending on draft quality and task type |
| **Acceptance rate** | 60–90% for well-trained draft models; lower for creative/diverse generation |
| **Memory overhead** | Draft model or additional heads add 10–30% memory cost |
| **Best for** | Generation-heavy workloads (coding, long-form text); less impactful for short responses |
| **Worst case** | Highly creative or unpredictable output where draft acceptance drops below 50% |
| **Hardware** | Benefits from GPUs with strong single-pass throughput (H100, A100); less impactful on latency-bound systems |

## Configuration

Typical speculative decoding parameters:
- **Draft length** ($k$): Number of tokens to speculate ahead (usually 3–8)
- **Draft model size**: 1–10% of target model parameters
- **Verification threshold**: Minimum probability for token acceptance
- **Fallback**: If acceptance rate drops below threshold, switch to standard autoregressive decoding

## Related Concepts

- [[kv-cache-optimization]] — speculative decoding benefits from and interacts with KV cache management
- [[prompt-caching]] — both techniques reduce inference cost through different mechanisms
- [[distillation]] — draft models are often distilled from the target model for better alignment
