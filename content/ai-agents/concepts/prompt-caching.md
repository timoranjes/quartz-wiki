
# Prompt Caching

Prompt caching (also called context caching or KV cache reuse) is an inference optimization where providers persist the KV cache state for repeated prompt prefixes across API calls, dramatically reducing both cost and latency for requests that share common context.

---

## Definition

When an LLM processes a prompt, it computes key-value (KV) vectors for each token in the attention layers. If two requests share a common prefix — such as a system prompt, few-shot examples, or a large document — recomputing the KV state for the shared portion is wasteful. Prompt caching stores the KV state for processed prefixes and reuses it when a matching prefix appears in a subsequent request.

## How It Works

### Prefix Matching

Providers match incoming requests against cached KV states using prefix comparison:

1. **Exact prefix match**: The beginning of the new prompt exactly matches a cached prefix
2. **Minimum cache unit**: Most providers require a minimum prefix length (e.g., 1K–10K tokens) for caching to activate
3. **Cache lifetime**: Cached entries persist for a defined window (minutes to hours, depending on provider)

### Cache Hit Economics

The cost difference between cache hits and misses is dramatic. In real-world workloads, **80–98% of input tokens can be cached** when prompts share stable prefixes:

| Provider | Cache Hit Price | Cache Miss Price | Discount | Typical Cache Reuse |
|----------|----------------|-----------------|----------|-------------------|
| **DeepSeek V4-Flash** | $0.0028/M | $0.14/M | **~98%** | 80–95% of input tokens |
| **OpenAI GPT-4o** | 50% of regular | Regular | **50%** | 70–90% of input tokens |
| **Anthropic Claude** | ~10% of regular | Regular | **~90%** | 80–98% of input tokens |
| **Google Gemini** | Cached discount | Regular | **~75%** | 70–85% of input tokens |
| **Together AI** | Substantial savings | Regular | Variable | 60–90% of input tokens |
| **Alibaba Qwen** | Significant discount | Regular | **~80%** | 75–95% of input tokens |

**Cache reuse percentages by workload type**:
- **Code assistants** (Claude Code, Codex): 90–98% — codebase context is stable across edits
- **RAG systems**: 80–95% — system prompt + retrieved documents form stable prefix
- **Agent loops**: 70–90% — system prompt + tool definitions are constant, conversation grows
- **Chat applications**: 40–70% — only system prompt is cached, conversation varies per turn
- **Batch processing**: 95–98% — identical prompt template applied to different data

### Latency Benefits

Beyond cost savings, prompt caching provides substantial latency reduction:

- **Skip recomputation**: Cached prefixes skip the forward pass entirely for the cached portion
- **Faster time-to-first-token (TTFT)**: Only the novel suffix needs processing
- **Throughput improvement**: Reduced compute per request increases overall system throughput

## Provider Implementations

### DeepSeek

DeepSeek offers the most aggressive prompt caching in the industry:

- **Automatic caching**: No configuration needed — caching activates automatically for repeated prefixes
- **98%+ discount**: Cache hits cost $0.0028/M tokens vs $0.14/M for V4-Flash input
- **1M context support**: Caching works across DeepSeek's full 1M token context window
- **Hybrid thinking mode**: Both thinking and non-thinking modes benefit from caching

**Impact**: For applications with repeated system prompts (agents, code assistants, RAG systems), DeepSeek's caching can reduce costs by 90–98% on input tokens.

### OpenAI

OpenAI introduced prompt caching to its API in October 2024:

- **Automatic prefix caching**: Activates when requests share a prefix of at least 1K tokens
- **50% discount**: Cached input tokens cost half the regular input price
- **API transparency**: Usage reports distinguish cached vs. non-cached tokens
- **Model support**: Available across GPT-4o, GPT-4.1, GPT-5, and o-series models
- **Cache TTL**: Cached entries persist for approximately 5–10 minutes of inactivity

### Anthropic

Anthropic's Claude models support prompt caching with explicit API controls:

- **Cache control markers**: Developers can explicitly mark which prompt sections should be cached using `cache_control` type
- **Automatic prefix detection**: Anthropic also automatically caches matching prefixes
- **Cost savings**: Significant discount for cached prefix tokens
- **Claude Code benefits**: Code editing workflows with large codebases benefit enormously — the codebase context is cached across edits
- **Extended thinking**: Cached prefixes work with Claude's extended thinking mode

**Best practice**: Place the most stable content (system prompts, tool definitions, codebase context) at the beginning of the prompt to maximize cache hits.

### Google Gemini

Google Gemini supports context caching through its API:

- **Cached content API**: Explicit cache creation and management via `CachedContent` resource
- **Long-lived caches**: Caches can persist for hours, suitable for large document analysis
- **Gemini 2.5 Pro**: Supports 1M+ token context with caching for document-heavy workflows
- **Cost efficiency**: Significant savings for repeated analysis of the same large documents

### Together AI

Together AI serves open-weight models with vLLM-backed caching:

- **Automatic caching**: Built into vLLM's Paged Attention serving layer
- **Multi-model support**: Caching works across Llama, Mistral, and other open models
- **No explicit configuration**: Caching is transparent to the API consumer

### Alibaba Qwen

Qwen's Model Studio provides caching for API calls:

- **Automatic context caching**: Reuses KV state for repeated prefixes
- **Multi-model support**: Works across Qwen 3.7 series and third-party models on Model Studio
- **Cost optimization**: Significant savings for high-volume API usage

## Prompt Design for Caching

### Effective Patterns

```
# Good: Stable prefix first, variable content last
System: "You are a code assistant..." [CACHED]
Tools: [tool definitions] [CACHED]
Codebase: [files A, B, C] [CACHED]
User query: "Fix the bug in file A" [NOT CACHED]
```

### Anti-Patterns

```
# Bad: Variable content first breaks cache matching
User query: "Fix the bug in file A" [NOT CACHED]
System: "You are a code assistant..." [CACHED but never reached]
```

### Strategies for Maximizing Cache Hits

1. **Prefix stability**: Keep the most static content at the very beginning of the prompt
2. **Batched requests**: Group requests with shared prefixes to hit the cache window
3. **System prompt consolidation**: Use a single comprehensive system prompt rather than per-request variations
4. **Tool definition reuse**: Cache tool/function definitions that don't change between requests
5. **Codebase snapshotting**: For code agents, cache the full codebase context and only diff changes

## Cost Impact Examples

| Use Case | Monthly API Calls | Avg Tokens/Call | Without Caching | With Caching | Savings |
|----------|------------------|-----------------|-----------------|--------------|---------|
| **Code Assistant** | 100,000 | 50K (40K cached) | $700 | $112 | **~84%** |
| **RAG System** | 50,000 | 30K (20K cached) | $210 | $68 | **~68%** |
| **Agent Loop** | 500,000 | 10K (8K cached) | $700 | $140 | **~80%** |

*Assuming DeepSeek V4-Flash pricing; savings vary by provider.*

## Related Concepts

- [[kv-cache-optimization]] — prompt caching is a KV cache reuse strategy
- [[mcp-protocol]] — MCP tool definitions benefit from caching as stable prefix content
- [[speculative-decoding]] — both techniques reduce inference cost through different mechanisms
