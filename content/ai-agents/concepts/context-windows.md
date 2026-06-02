---
title: Context Windows
created: 2026-06-02
updated: 2026-06-02
type: concept
tags:
  - inference
  - architecture
  - long-context
sources:
  - "Google Gemini 10M Token Context Release"
  - "Kimi K2 256K Context Technical Details"
  - "Anthropic Claude 200K Context Window Documentation"
  - "OpenAI GPT-5.5 1M Context Announcement"
  - "Needle in a Haystack (NIAH) Benchmark Suite"
  - "MRCR (Multi-Retrieval Context Retention) Results"
  - "Periodic RoPE for Infinite Context LLMs"
  - "GPT-5.5 Instant 12M Context SubQ"
confidence: high
---

# Context Windows

The context window is the maximum number of tokens an LLM can process in a single forward pass, encompassing both input (prompt) and output (generation). Larger context windows enable processing of longer documents, longer conversation histories, and more complex multi-step reasoning, but come with significant computational and memory costs.

---

## Definition

The context window size is determined by the model's positional encoding scheme and training data distribution. During training, models see sequences up to a maximum length, and the positional encoding must support positions up to that length. Key constraints:

- **KV cache memory**: Grows linearly with context length and batch size, often the primary bottleneck
- **Attention computation**: Standard attention is $O(n^2)$ in context length, though Flash Attention reduces the constant factor
- **Positional encoding extrapolation**: Models trained on shorter contexts may struggle with positions beyond their training distribution
- **Needle in a Haystack (NIAH)**: Standard benchmark measuring a model's ability to retrieve specific information from long contexts

## Google Gemini: 10M+ Token Context

Google Gemini holds the record for the largest practical context window:

- **Gemini 1.5 Pro**: Supports 1M tokens natively, with experimental support for 10M+ tokens. Can process entire codebases, hours of video, or hundreds of documents in a single prompt.
- **Gemini 2.5 Pro**: Refined long-context handling with improved NIAH performance — achieves ~95% accuracy at 1M tokens, significantly better than Gemini 1.5's ~85% at the same length.
- **Gemini Flash**: Supports 1M tokens with lower cost, optimized for high-throughput long-context processing.
- **Gemini 3.5 Flash** (May 2026): Upgraded context handling with better retention at extreme lengths.
- **Architecture innovations**:
  - **Ring Attention**: Distributes long sequences across multiple devices, enabling context lengths beyond single-device memory
  - **Efficient attention**: Linear-complexity attention variants for extreme contexts
  - **Multi-modal context**: Gemini's context window handles text, images, audio, and video simultaneously
- **Use cases**: Full codebase analysis, legal document review, video understanding, scientific paper analysis

## Kimi K2: 256K Context with Strong Retention

Moonshot AI's Kimi K2 demonstrates excellent long-context capabilities:

- **256K token context**: Optimized for Chinese and English long-document processing.
- **Strong NIAH performance**: Achieves high accuracy across the full 256K window, with minimal degradation at the edges.
- **Agentic use**: Kimi K2 is designed for agentic workflows that require maintaining long conversation histories and processing large documents.
- **Cost optimization**: Competitive pricing for long-context usage, making it attractive for RAG and document analysis applications.
- **Multi-modal**: Supports text and image input within the context window.

## Anthropic Claude: 200K Context Window

Anthropic's Claude models feature a 200K token context window:

- **Claude 3.5 Sonnet / Opus 4.8**: 200K context with strong retention throughout.
- **Prompt caching integration**: Claude's 200K context works seamlessly with prompt caching — the entire codebase or document can be cached and reused across requests.
- **Claude Code benefits**: Code editing workflows leverage the full 200K context to understand large codebases, with the cached context persisting across edits.
- **Extended thinking compatibility**: Claude's extended thinking mode operates within the 200K context, enabling deep reasoning on long documents.
- **NIAH performance**: Claude achieves ~90% accuracy at 200K tokens, with particularly strong performance on code retrieval tasks.
- **Best practices**: Anthropic recommends placing the most important information in the middle of the context (not at the beginning or end) for optimal recall.

## OpenAI: GPT-5.5 1M Context

OpenAI's context window has evolved significantly:

- **GPT-4o**: 128K context, sufficient for most use cases.
- **GPT-5** (Aug 2025): Extended to 1M context, enabling processing of very long documents and conversation histories.
- **GPT-5.1** (Nov 2025): Improved long-context retention with better positional encoding.
- **GPT-5.5** (Apr 2026): 1M context with enhanced NIAH performance, achieving ~92% accuracy at full context length.
- **GPT-5.5 Instant** (May 2026): Supports SubQ 12M context for specialized long-context queries, using a different architecture optimized for retrieval-heavy tasks.
- **Prompt caching**: 1M context works with OpenAI's prompt caching (50% discount on cached tokens), making long-context usage more economical.
- **Positional encoding**: Uses advanced RoPE variants with extrapolation support, maintaining accuracy beyond training context length.

## NIAH Benchmark Results

Needle in a Haystack is the standard benchmark for evaluating long-context retention:

### Methodology

- Insert a single factual statement (the "needle") at a random position in a long document (the "haystack")
- Ask the model a question that requires retrieving the needle
- Measure accuracy across different context lengths and needle positions

### Representative Results (2025–2026)

| Model | 32K | 128K | 200K | 1M | Notes |
|-------|-----|------|------|----|-------|
| **Gemini 2.5 Pro** | 99% | 98% | 97% | 95% | Best-in-class long-context |
| **GPT-5.5** | 98% | 96% | 94% | 92% | Strong across all lengths |
| **Claude Opus 4.8** | 99% | 97% | 93% | N/A | 200K max context |
| **DeepSeek V4** | 97% | 95% | 92% | 90% | Excellent for cost |
| **Kimi K2** | 98% | 96% | 94% | N/A | 256K max context |
| **Qwen 3.7** | 96% | 93% | 90% | 85% | Good value |

## MRCR: Multi-Retrieval Context Retention

MRCR extends NIAH by testing multiple needles simultaneously:

- **Challenge**: Real-world tasks often require retrieving multiple pieces of information from long contexts, not just one.
- **Methodology**: Insert $N$ needles at random positions, ask $N$ questions, measure retrieval accuracy for each.
- **Key finding**: Models that perform well on NIAH (single needle) often degrade significantly on MRCR (multiple needles), revealing that long-context understanding is more fragile than NIAH suggests.
- **Results**: Even top models show 10–20% accuracy drop on MRCR vs. NIAH at 1M+ context lengths.
- **Implication**: NIAH alone is insufficient for evaluating long-context capability; MRCR provides a more realistic benchmark.

## Positional Encoding for Long Context

Several techniques enable context windows beyond training length:

- **RoPE (Rotary Position Embedding)**: The dominant positional encoding, with extrapolation variants (YaRN, Dynamic YaRN) that extend beyond training length.
- **Periodic RoPE** (2025): Introduces periodicity in positional encoding, theoretically supporting infinite context with bounded memory. Early implementations show promising results.
- **ALiBi (Attention with Linear Biases)**: Alternative to RoPE that naturally extrapolates to arbitrary lengths, but generally underperforms RoPE at training length.
- **NoPE (No Positional Encoding)**: Research showing that some models can learn positional information implicitly, though results are mixed.

## Trade-offs

| Aspect | Details |
|--------|---------|
| **Memory** | KV cache grows linearly with context; 1M context requires ~10–50GB GPU memory |
| **Compute** | Attention is $O(n^2)$; Flash Attention reduces constant but doesn't change complexity |
| **Quality degradation** | Most models show declining NIAH accuracy as context length increases |
| **Cost** | Longer contexts cost more to process; prompt caching mitigates but doesn't eliminate |
| **Latency** | Time-to-first-token increases with context length due to longer prefill |
| **Position bias** | Information at the beginning and end of context is recalled better than the middle |

## Open Questions

- **Infinite context**: Can models truly support arbitrary context lengths, or is there a fundamental limit?
- **Context compression**: Can we compress long contexts while preserving retrieval accuracy?
- **Multi-needle understanding**: How can models improve MRCR performance — is it a retrieval problem or a reasoning problem?
- **Context window vs. RAG**: When is a large context window preferable to retrieval-augmented generation?
- **Streaming context**: Can models process and reason about contexts that grow indefinitely over time?

## Related Concepts

- [[kv-cache-optimization]] — KV cache management is the primary bottleneck for long contexts
- [[prompt-caching]] — caching reduces the cost of repeatedly processing long contexts
- [[extended-thinking]] — thinking tokens consume context window capacity
- [[agent-anti-patterns]] — context stuffing (dumping too much into the context) is a common anti-pattern
