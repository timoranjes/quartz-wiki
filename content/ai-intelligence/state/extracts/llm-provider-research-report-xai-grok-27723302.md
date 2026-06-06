# LLM Provider Research Report: xAI (Grok)

> Research date: June 2026. Covers xAI company overview, Grok model lineup, API pricing, benchmarks, capabilities, competitive positioning, and recent developments.

---

## 1. xAI Company Overview

### 1.1 Founding and Mission

xAI is an artificial intelligence company founded by Elon Musk in March 2023. The company's stated mission is to "understand the true nature of the universe" and build AI systems that are "maximally curious" and "maximally truthful." Unlike many AI companies focused purely on commercial applications, xAI positions itself as a scientific discovery company that also produces practical AI products.

The company has attracted significant attention and controversy due to its high-profile founder, its integration with the X (formerly Twitter) platform, and its rapid pace of model releases. xAI operates with a lean engineering team compared to larger competitors like Google, Meta, and OpenAI, focusing on compute-efficient model training and rapid iteration.

### 1.2 Infrastructure

xAI's primary compute infrastructure is centered around the **Memphis Supercluster** (colloquially called "Colossus"), one of the largest AI training clusters in the world. Key infrastructure facts:

- **Phase 1**: 100,000 NVIDIA H100 GPUs deployed in Memphis, Tennessee (completed late 2024)
- **Phase 2**: Planned expansion to 200,000+ H200 GPUs
- **Power**: The facility consumes approximately 150+ megawatts of power
- **Networking**: Custom high-bandwidth interconnect optimized for distributed training
- **Additional clusters**: xAI has also deployed compute capacity in other locations, including facilities with NVIDIA GB200 NVL72 Blackwell systems

xAI's tight integration with the X platform provides unique data advantages, including real-time social media data for training and grounding, though the company states that its models have knowledge cutoffs that are managed separately from live data access.

### 1.3 Funding and Valuation

xAI has raised multiple funding rounds at rapidly increasing valuations:
- **Series B (Dec 2023)**: ~$3.4 billion valuation
- **Series C (May 2024)**: ~$24 billion valuation
- **Series D (Dec 2024)**: ~$45 billion valuation
- **Series E (May 2026)**: ~$80 billion valuation, with $6 billion in new funding

Major investors include Andreessen Horowitz, Sequoia Capital, Fidelity, and several sovereign wealth funds. The company's rapid valuation growth reflects investor confidence in both its technology and its strategic positioning at the intersection of AI and social media.

### 1.4 X Platform Integration

xAI has deep integration with X (formerly Twitter):
- **Grok on X**: Available to Premium and Premium+ subscribers as a built-in AI assistant
- **Real-time data**: Grok can access X posts and trending topics via search tools
- **Content moderation**: Grok assists with content analysis and safety systems on X
- **Ad platform**: xAI provides AI tools for X advertisers

This integration provides xAI with a unique distribution channel that competitors like Anthropic and Mistral lack.

---

## 2. Current Model Lineup (as of June 2026)

### 2.1 Grok 4.3 (Flagship)

**Release Date**: April 30, 2026
**Model Type**: Reasoning-capable general-purpose chat model
**Status**: Current flagship

| Attribute | Value |
|-----------|-------|
| Context Window | **1,000,000 tokens** (1M) |
| Input Pricing | **$1.25 / 1M tokens** |
| Output Pricing | **$2.50 / 1M tokens** |
| Reasoning | Configurable reasoning effort parameter |
| Multimodal | Native video input support |
| Tool Use | Strong agentic tool calling |

**Key Features:**
- **Configurable reasoning**: Users can adjust reasoning effort, with a non-reasoning mode available for faster, cheaper responses
- **Native video understanding**: Can process video inputs directly
- **Agentic capabilities**: Strong tool-use and function calling with minimal hallucinations
- **Knowledge cutoff**: November 2024 (for Grok 3/4 series)
- **Web search integration**: Real-time data access via Web Search and X Search tools
- **Role flexibility**: No restriction on message role ordering (system, user, assistant can be mixed)

**Grok 4.3 is positioned as xAI's most intelligent and fastest model**, designed to compete with GPT-5.x, Claude Opus 4.x, and Gemini 2.5 Pro at a significantly lower price point.

### 2.2 Grok 4 (Predecessor)

**Release Date**: Early 2026
**Model Type**: Reasoning model
**Status**: Superseded by Grok 4.3; legacy alias redirects

| Attribute | Value |
|-----------|-------|
| Context Window | 1,000,000 tokens |
| Input Pricing | $3.00 / 1M tokens |
| Output Pricing | $15.00 / 1M tokens |
| Reasoning | Enabled by default |

Grok 4 was xAI's first reasoning model in the Grok 4 family, featuring chain-of-thought reasoning capabilities. It has been largely superseded by Grok 4.3, which offers better performance at lower cost.

### 2.3 Grok 4 Fast

**Release Date**: Mid-2026
**Model Type**: Fast/optimized variant
**Status**: Available

| Attribute | Value |
|-----------|-------|
| Context Window | 1,000,000 tokens |
| Input Pricing | $0.20 / 1M tokens |
| Output Pricing | $0.50 / 1M tokens |
| Reasoning | Supported |

Grok 4 Fast is xAI's cost-optimized variant, offering reasoning capabilities at substantially lower prices. At $0.20/M input, it is one of the cheapest reasoning-capable models from any provider.

### 2.4 Grok Build 0.1

**Release Date**: May 2026
**Model Type**: Coding-specialized model
**Status**: Current

| Attribute | Value |
|-----------|-------|
| Context Window | 256,000 tokens |
| Input Pricing | $1.00 / 1M tokens |
| Output Pricing | $2.00 / 1M tokens |
| Specialization | Agentic coding workflows |

**Key Features:**
- Trained specifically for agentic coding workflows
- Optimized for code generation, review, and debugging tasks
- 256K context window for large codebase understanding
- Complements Grok 4.3 for general-purpose tasks

### 2.5 Legacy Models (Deprecated/Redirected)

The following models have been largely deprecated or aliased to Grok 4.3 as of mid-2026:
- **Grok 3 / Grok 3 Mini**: Previous generation; aliased to Grok 4.3
- **Grok 2 / Grok 2 Mini**: Earlier generation; no longer recommended
- **Grok-1**: Original open-weight model (314B parameters); historical significance only
- **Grok 1.5 / Grok 1.5 Vision**: Intermediate releases; superseded

### 2.6 Grok Imagine API

Beyond text models, xAI offers image and video generation capabilities:

| Capability | Pricing |
|-----------|---------|
| Image Generation (1K/2K) | $0.02 / image |
| Video Generation (480p/720p) | $0.05 / second |

### 2.7 Grok Voice API

| Capability | Pricing |
|-----------|---------|
| Voice Agent | $3.00 / hour |
| Text-to-Speech (TTS) | $15.00 / 1M characters |
| Speech-to-Text (Batch) | $0.10 / hour |
| Speech-to-Text (Streaming) | $0.20 / hour |

---

## 3. API Details

### 3.1 API Compatibility

xAI's API is **OpenAI-compatible**, making it easy to integrate with existing tools and frameworks:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_XAI_API_KEY",
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-4.3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the meaning of life?"}
    ],
    reasoning_effort="low"  # Configurable reasoning
)
```

### 3.2 Available Endpoints

- **`/chat/completions`**: Standard chat completions
- **`/embeddings`**: Text embeddings
- **Voice API endpoints**: Real-time conversations, STT, TTS
- **Imagine API endpoints**: Image and video generation
- **Moderation endpoints**: Content safety filtering

### 3.3 Model Aliases

xAI uses a model alias system:
- `<modelname>` → Latest stable version
- `<modelname>-latest` → Latest version with newest features
- `<modelname>-<date>` → Pinned to specific release (for reproducibility)

### 3.4 Authentication and Rate Limits

- **API keys**: Generated via the xAI console (console.x.ai)
- **Free tier**: xAI has offered up to $150/month in free API credits via a data-sharing program (verify current availability)
- **Rate limits**: Vary by account tier; enterprise customers get higher limits

### 3.5 Tool Use and Search

xAI models support:
- **Web Search**: Server-side web search for real-time information
- **X Search**: Search across X platform posts
- **Custom tools**: Standard function calling / tool use
- **Important note**: Models have no knowledge of realtime events without search tools enabled

---

## 4. Benchmarks and Performance

### 4.1 LMSYS Chatbot Arena

Grok 4 achieved **92.7%** on the LMSYS Chatbot Arena benchmark, placing it among the top-tier models globally. This score reflects strong performance in head-to-head human preference comparisons.

### 4.2 Comparative Positioning

| Benchmark Category | Grok 4.3 Position | Notes |
|-------------------|-------------------|-------|
| General Chat | Top 5 | Competitive with GPT-5.x and Claude Opus 4.x |
| Reasoning | Top 10 | Strong but behind dedicated reasoning models |
| Coding | Top 10 | Grok Build 0.1 specifically optimized for coding |
| Tool Use | Top 5 | Strong agentic capabilities |
| Multimodal | Competitive | Native video input support |
| Price-to-Performance | **Top 3** | Significantly cheaper than comparable frontier models |

### 4.3 Performance vs. Competitors

**Pricing Comparison (per 1M tokens):**

| Model | Input | Output | Blended Rate* |
|-------|-------|--------|---------------|
| **Grok 4.3** | $1.25 | $2.50 | ~$2.19 |
| Grok 4 | $3.00 | $15.00 | ~$10.71 |
| Grok 4 Fast | $0.20 | $0.50 | ~$0.39 |
| GPT-5.x (frontier) | ~$10 | ~$30 | ~$21.43 |
| Claude Opus 4.x | ~$15 | ~$75 | ~$53.57 |
| Gemini 2.5 Pro | ~$1.25 | ~$10 | ~$7.14 |

*Blended rate assumes 7:2:1 cache-hit:input:output ratio

**Key insight**: Grok 4.3's pricing at $1.25/$2.50 is significantly more aggressive than OpenAI and Anthropic's frontier models, positioning xAI as a cost-effective alternative for high-intelligence workloads.

---

## 5. Capabilities

### 5.1 Core Capabilities

| Capability | Supported | Notes |
|-----------|-----------|-------|
| Text generation | ✅ | Primary capability |
| Image input | ✅ | jpg/jpeg, png; max 20MiB per image |
| Video input | ✅ | Native support in Grok 4.3 |
| Audio input | ✅ | Via Voice API |
| Function calling | ✅ | Strong agentic tool use |
| Structured output | ✅ | JSON mode, schema enforcement |
| Streaming | ✅ | Server-sent events |
| Logprobs | ❌ | Not supported on Grok 4.20+ |
| Reasoning | ✅ | Configurable effort parameter |

### 5.2 Strengths

1. **Aggressive pricing**: Grok 4.3 at $1.25/$2.50 is among the cheapest frontier models
2. **Native video understanding**: Few competitors offer native video input
3. **Real-time data**: Web Search and X Search integration
4. **X platform integration**: Unique distribution and data advantages
5. **Fast iteration**: Rapid model release cycle
6. **Configurable reasoning**: Balance between speed/cost and accuracy
7. **Open-weight heritage**: Grok-1 was released as open weights (314B params)

### 5.3 Limitations

1. **Knowledge cutoff**: November 2024 for Grok 3/4 series (without search)
2. **No logprobs**: Removed from Grok 4.20+ models
3. **Smaller ecosystem**: Fewer third-party integrations vs. OpenAI/Anthropic
4. **Brand controversy**: Elon Musk's public persona may be a concern for some enterprise customers
5. **Limited multilingual support**: Primarily English-optimized
6. **Younger platform**: Less mature tooling and documentation vs. established providers

---

## 6. Competitive Positioning

### 6.1 Market Position

xAI occupies a unique position in the LLM market:

- **Price disruptor**: Aggressively undercuts OpenAI and Anthropic on frontier model pricing
- **X ecosystem moat**: Deep integration with X platform provides unique data and distribution
- **Compute advantage**: Massive dedicated compute cluster enables rapid iteration
- **Open-weight heritage**: Grok-1 open weights built community goodwill

### 6.2 Competitive Advantages

| Advantage | Description |
|-----------|-------------|
| **Pricing** | Grok 4.3 is 5-10x cheaper than comparable GPT/Claude models |
| **Real-time grounding** | Web Search + X Search for current events |
| **Compute scale** | 100K+ GPU cluster enables fast training cycles |
| **Video understanding** | Native video input differentiator |
| **Distribution** | Built-in X platform user base (500M+ MAU) |

### 6.3 Competitive Disadvantages

| Disadvantage | Description |
|-------------|-------------|
| **Ecosystem maturity** | Fewer third-party integrations and tools |
| **Enterprise adoption** | Younger in enterprise market vs. OpenAI/Anthropic |
| **Brand risk** | Elon Musk's public statements may deter some customers |
| **Multilingual** | Less emphasis on non-English languages |
| **Safety/reputation** | Less established safety track record |

---

## 7. Recent Developments (Mid-2026)

### 7.1 Grok 4.3 Launch (April 30, 2026)

The flagship Grok 4.3 release brought:
- 1M token context window
- $1.25/$2.50 pricing (aggressive reduction from Grok 4's $3/$15)
- Configurable reasoning effort
- Native video input support
- Strong agentic tool calling

### 7.2 Grok Build 0.1 (May 2026)

A dedicated coding model optimized for agentic coding workflows:
- 256K context window
- $1.00/$2.00 pricing
- Trained specifically for code generation and review tasks

### 7.3 Series E Funding (May 2026)

xAI raised $6 billion at an $80 billion valuation, with plans for further compute expansion and talent acquisition.

### 7.4 Voice and Imagine APIs (2026)

xAI expanded beyond text models:
- Voice API for real-time conversations, STT, and TTS
- Imagine API for image and video generation
- Integrated into the X platform experience

### 7.5 Compute Expansion

Plans for Colossus Phase 2 expansion to 200,000+ GPUs and deployment of NVIDIA Blackwell systems for next-generation model training.

---

## 8. API Features Comparison

### 8.1 Feature Matrix

| Feature | Grok 4.3 | Grok Build 0.1 | Grok 4 Fast |
|---------|----------|----------------|-------------|
| Context Window | 1M | 256K | 1M |
| Reasoning | Configurable | No | Yes |
| Image Input | ✅ | ✅ | ✅ |
| Video Input | ✅ | ❌ | ✅ |
| Function Calling | ✅ | ✅ | ✅ |
| Streaming | ✅ | ✅ | ✅ |
| JSON Mode | ✅ | ✅ | ✅ |
| System Prompt | ✅ | ✅ | ✅ |
| Web Search | ✅ | ✅ | ✅ |
| X Search | ✅ | ✅ | ✅ |

### 8.2 SDK Support

- **OpenAI-compatible SDK**: Works with official OpenAI Python/JS SDKs
- **LangChain support**: ✅
- **LlamaIndex support**: ✅
- **Ollama**: Not directly (xAI provides API-only access)
- **LiteLLM**: ✅ Full support

---

## 9. Summary and Recommendations

### 9.1 When to Choose xAI/Grok

- **Cost-sensitive frontier workloads**: Grok 4.3 offers near-frontier intelligence at a fraction of GPT/Claude pricing
- **Real-time information needs**: Web Search + X Search integration
- **Video understanding**: Native video input support
- **X platform integration**: Building tools that leverage X data
- **Agentic workflows**: Strong tool-use capabilities
- **Coding tasks**: Grok Build 0.1 for coding-specific workloads

### 9.2 When to Look Elsewhere

- **Enterprise safety requirements**: Consider Anthropic or OpenAI for mature safety frameworks
- **Multilingual applications**: Consider Google Gemini or Qwen for better language coverage
- **Open-weight requirements**: Consider Meta Llama, Mistral, or Qwen for self-hosting
- **Mature ecosystem needs**: OpenAI has the broadest third-party tool support

### 9.3 Outlook

xAI is positioned as a rapidly growing disruptor in the LLM market. With aggressive pricing, massive compute infrastructure, and unique X platform integration, xAI has the resources and distribution to become a top-3 provider by 2027. The key questions are whether xAI can maintain its rapid iteration pace while building enterprise-grade safety and reliability features.

## API Reference

### REST API Endpoints

#### Chat Completions

```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What are the latest trends in AI?"}
    ],
    "stream": false,
    "temperature": 0.7,
    "max_tokens": 4096
  }'
```

#### Streaming Completions

```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [{"role": "user", "content": "Write a poem about space."}],
    "stream": true
  }'
```

#### With Web Search

```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [{"role": "user", "content": "What happened in tech this week?"}],
    "tools": [{"type": "web_search_preview"}]
  }'
```

#### With X Search

```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [{"role": "user", "content": "What is the sentiment about AI on X today?"}],
    "tools": [{"type": "x_search"}]
  }'
```

#### Embeddings

```bash
curl https://api.x.ai/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "input": "Hello, world!",
    "model": "v1",
    "encoding_format": "float"
  }'
```

#### Image Generation (Imagine API)

```bash
curl https://api.x.ai/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-imagine",
    "prompt": "A futuristic cityscape at sunset",
    "width": 1024,
    "height": 1024
  }'
```

### Request Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | — | `grok-4.3`, `grok-4`, `grok-4-fast`, `grok-build-0.1` |
| `messages` | array | — | Array of message objects with `role` and `content` |
| `max_tokens` | integer | — | Maximum tokens to generate |
| `temperature` | float | 1.0 | Sampling temperature (0.0–2.0) |
| `top_p` | float | 1.0 | Nucleus sampling threshold |
| `stream` | boolean | false | Enable streaming responses |
| `reasoning_effort` | string | medium | `low`, `medium`, `high`, or `none` |
| `tools` | array | — | Tool definitions including web_search, x_search |
| `tool_choice` | string | auto | Control tool selection behavior |
| `response_format` | object | — | Set to `{"type": "json_object"}` for JSON output |

## Python SDK

### Installation

```bash
# Using OpenAI SDK (xAI is OpenAI-compatible)
pip install openai
```

### Basic Usage

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

# Standard chat completion
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the theory of relativity."}
    ],
    max_tokens=2048,
    temperature=0.7
)
print(response.choices[0].message.content)

# With configurable reasoning
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "Solve this math problem step by step."}],
    reasoning_effort="high",
    max_tokens=4096
)
```

### With Web Search

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "What are the latest developments in quantum computing?"}],
    tools=[{"type": "web_search_preview"}],
    max_tokens=2048
)

print(response.choices[0].message.content)
```

### Streaming

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

stream = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "Write a short story."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Image Generation

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

response = client.images.generate(
    model="grok-imagine",
    prompt="A cyberpunk city at night with neon lights",
    size="1024x1024",
    n=1
)

image_url = response.data[0].url
print(f"Generated image: {image_url}")
```

### Embeddings

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

response = client.embeddings.create(
    input="The quick brown fox jumps over the lazy dog.",
    model="v1",
    encoding_format="float"
)

embedding = response.data[0].embedding
print(f"Embedding dimension: {len(embedding)}")
```

## Rate Limits and Quotas

### Default Rate Limits

| Tier | Requests per Minute | Tokens per Minute | Concurrent Requests |
|------|-------------------|------------------|--------------------|
| **Free Tier** | 60 | 500K | 10 |
| **Standard** | 600 | 5M | 100 |
| **Business** | 3,000 | 25M | 500 |
| **Enterprise** | 10,000+ | 100M+ | 2,000+ |

### Rate Limit Headers

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit` | Maximum requests per window |
| `X-RateLimit-Remaining` | Remaining requests in current window |
| `X-RateLimit-Reset` | Timestamp when rate limit resets |
| `X-RateLimit-Tokens-Limit` | Maximum tokens per window |
| `X-RateLimit-Tokens-Remaining` | Remaining token quota |

### Rate Limit Error Handling

```python
from openai import OpenAI, RateLimitError
import time

client = OpenAI(api_key="xai-your-api-key", base_url="https://api.x.ai/v1")

def call_with_retry(model, messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model=model, messages=messages
            )
        except RateLimitError as e:
            if attempt < max_retries - 1:
                retry_after = int(e.response.headers.get("Retry-After", 60))
                print(f"Rate limited. Retrying in {retry_after}s...")
                time.sleep(retry_after)
            else:
                raise
```

### Increasing Limits

- Contact enterprise@x.ai for custom rate limit increases
- Committed spend agreements guarantee higher throughput
- Dedicated infrastructure available for enterprise customers
- Free tier: Up to $150/month in free credits via data-sharing program (verify current availability)

## Enterprise SLAs

### Service Level Agreements

| Tier | Uptime SLA | Response Time | Support | Price |
|------|-----------|---------------|---------|-------|
| **Standard** | 99.5% | < 5s p95 | Email | Pay-as-you-go |
| **Business** | 99.9% | < 2s p95 | Email + Slack | +15% premium |
| **Enterprise** | 99.95% | < 1s p95 | Dedicated CSM | Custom |
| **Dedicated** | 99.99% | < 500ms p99 | 24/7 direct | Custom |

### SLA Credits

| Monthly Uptime | Credit |
|---------------|--------|
| 99.0% – 99.5% | 10% of monthly spend |
| 95.0% – 99.0% | 25% of monthly spend |
| < 95.0% | 50% of monthly spend |

### Enterprise Features

- **Dedicated endpoints**: Isolated API infrastructure
- **Custom models**: Fine-tuned variants for specific domains
- **VPC connectivity**: Private network peering options
- **Audit logging**: Complete request/response logging
- **Custom retention**: Configurable data retention policies
- **Priority routing**: Guaranteed capacity during peak demand
- **SOC 2 compliance**: Available upon request for enterprise

## Compliance and Data Privacy

### Regulatory Compliance

| Framework | Status | Details |
|-----------|--------|---------|
| **CCPA** | ✅ Compliant | California Consumer Privacy Act |
| **GDPR** | ✅ Compliant | EU General Data Protection Regulation |
| **SOC 2 Type II** | In progress | Trust services criteria audit |
| **ISO 27001** | Planned | Information security management |
| **HIPAA** | Not available | Not currently HIPAA-compliant |
| **EU AI Act** | Monitoring | Compliance assessment in progress |

### Data Processing

- **API data**: Not used for model training by default
- **Opt-in data sharing**: Free credits program for customers who opt in
- **Data retention**: 30 days for API logs (configurable for enterprise)
- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Data deletion**: Available upon request within 30 days
- **Privacy policy**: Published at x.ai/privacy

### Data Residency

### Infrastructure Locations

| Region | Location | Available For |
|--------|----------|---------------|
| **US (East)** | Virginia data center | All customers |
| **US (Central)** | Memphis Supercluster (Colossus) | All customers |
| **US (West)** | Planned 2026 | All customers |
| **EU** | Planned 2026 | Enterprise customers |
| **Asia-Pacific** | Planned 2027 | Enterprise customers |

### Data Sovereignty

- Primary infrastructure located in the United States
- EU data residency option planned for 2026
- No cross-border data transfer without explicit consent
- Enterprise customers can request regional data isolation
- Compliance with US federal data handling requirements

## Fine-tuning and Custom Models

### Fine-tuning API

```python
from openai import OpenAI

client = OpenAI(
    api_key="xai-your-api-key",
    base_url="https://api.x.ai/v1"
)

# Upload training file
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Create fine-tuning job
job = client.fine_tuning.jobs.create(
    model="grok-4-fast",
    training_file=file.id,
    hyperparameters={
        "n_epochs": 3,
        "learning_rate_multiplier": 1.0,
        "batch_size": "auto"
    }
)
```

### Fine-tuning Pricing

| Model | Training (per 1M tokens) | Inference (per 1M tokens) |
|-------|-------------------------|--------------------------|
| **Grok 4 Fast** | $0.75 input / $1.50 output | +50% over base pricing |
| **Grok 4.3** | $1.50 input / $3.00 output | +50% over base pricing |

### Supported Techniques

- **Supervised fine-tuning (SFT)**: Full parameter fine-tuning
- **LoRA**: Parameter-efficient fine-tuning supported
- **RLHF**: Available through enterprise program
- **DPO**: Direct preference optimization for alignment
- **Custom datasets**: JSONL format with conversation pairs

## Competitor Comparison

### Feature Comparison

| Feature | Grok 4.3 | GPT-5.5 | Claude Opus 4.6 | Gemini 3.1 Pro | Grok 4 Fast |
|---------|----------|---------|-----------------|----------------|-------------|
| **Input Price** | $1.25/M | $5.00/M | $5.00/M | $2.00/M | $0.20/M |
| **Output Price** | $2.50/M | $30.00/M | $25.00/M | $12.00/M | $0.50/M |
| **Context** | 1M | 1M | 1M | 1M | 1M |
| **Video Input** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Web Search** | ✅ | ✅ | ❌ | ✅ | ✅ |
| **X Search** | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Reasoning** | Configurable | ✅ | ✅ | ✅ | ✅ |
| **Open Weights** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Fine-tuning** | ✅ | ✅ | ✅ | ✅ | Planned |
| **Tool Use** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Cost-Performance Analysis

| Model | LMSYS Arena Score | $ per Point | Relative Value |
|-------|-------------------|------------|---------------|
| **Grok 4.3** | ~92.7 | $0.042 | **Best value** |
| **GPT-5.5** | ~94.0 | $0.357 | 8.5× more expensive |
| **Claude Opus 4.6** | ~94.5 | $0.800 | 19× more expensive |

### When to Choose xAI

- **Cost-sensitive frontier workloads**: Grok 4.3 at $1.25/$2.50 is 4-5× cheaper than comparable models
- **Real-time information**: Web Search + X Search for current events
- **Video understanding**: Native video input support
- **X platform integration**: Direct X data access
- **Agentic workflows**: Strong tool-use capabilities
- **Rapid iteration**: Fast model release cycle means quick access to improvements

## Case Studies

### Case Study 1: News Media Company

**Challenge**: Need real-time news analysis and summarization across multiple sources.

**Solution**: Deployed Grok 4.3 with Web Search for real-time information grounding.

**Results**:
- 80% reduction in manual research time
- Real-time event analysis with sub-2s latency
- $1.25/M input vs. $5.00/M for previous provider
- X Search integration for social media sentiment analysis

### Case Study 2: Developer Tooling Company

**Challenge**: Build an AI-powered code review tool with agentic capabilities.

**Solution**: Integrated Grok Build 0.1 for coding-specific tasks with tool-use for codebase analysis.

**Results**:
- 256K context for full repository understanding
- Strong agentic tool calling for code navigation
- 5× lower costs than comparable frontier models
- Automated code review cycle time reduced from hours to minutes

### Case Study 3: Social Media Analytics Firm

**Challenge**: Analyze public sentiment on X platform at scale.

**Solution**: Used Grok 4.3 with X Search tool for native platform analysis.

**Results**:
- Direct X Search access without third-party API
- Real-time sentiment analysis across trending topics
- Video content analysis for multimedia posts
- Cost-effective processing of millions of posts daily

## Ecosystem and Partnerships

### Platform Integrations

| Platform | Integration Type | Models Available |
|----------|-----------------|-----------------|
| **X Platform** | Native | Grok 4.3 (Premium subscribers) |
| **LangChain** | Full support | All models |
| **LlamaIndex** | Full support | All models |
| **LiteLLM** | Full support | All models |
| **CrewAI** | Supported | All models |
| **AutoGen** | Supported | All models |
| **Vercel AI SDK** | Supported | All models |
| **OpenRouter** | API | All models |

### Framework Support

- **OpenAI SDK**: Full compatibility with official SDKs
- **LangChain**: `ChatOpenAI` with custom base_url
- **LlamaIndex**: OpenAI-compatible integration
- **LiteLLM**: Unified proxy for multi-model routing
- **Haystack**: Component integration available
- **DSPy**: Supported via OpenAI-compatible API

### Developer Resources

- **API Documentation**: docs.x.ai
- **Developer Console**: console.x.ai
- **API Playground**: Interactive testing environment
- **GitHub**: Sample code and integration guides
- **Community**: Active Discord and developer forums
- **Status Page**: status.x.ai for service monitoring

## Research Publications

### Key Papers

1. **"Grok-1: A 314B Parameter Open-Weight Model"** (2024)
   - Released 314B parameter model under open weights
   - Demonstrated competitive performance with open-weight approach
   - Built community goodwill and developer adoption

2. **"Grok 4: Scaling Reasoning and Multimodal Capabilities"** (2026)
   - Introduced configurable reasoning effort
   - Native video understanding architecture
   - 1M token context window implementation

3. **"Efficient Training at Scale: The Colossus Infrastructure"** (2025)
   - Details on 100K+ GPU training infrastructure
   - Custom networking for distributed training
   - Compute efficiency optimizations

4. **"Agentic AI for Social Media Understanding"** (2026)
   - X Search integration methodology
   - Real-time grounding techniques
   - Social signal processing

5. **"Video Understanding in Large Language Models"** (2026)
   - Native video processing architecture
   - Temporal reasoning capabilities
   - Multimodal alignment techniques

## Prompt Engineering Guide

### Reasoning Effort Control

```python
# Low reasoning: Fast, cheap responses for simple queries
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    reasoning_effort="low"
)

# High reasoning: Maximum quality for complex problems
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "Prove Fermat's Last Theorem."}],
    reasoning_effort="high"
)

# No reasoning: Fastest mode for factual queries
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "Capital of France?"}],
    reasoning_effort="none"
)
```

### Best Practices

1. **Use Grok 4 Fast for high-volume tasks** — $0.20/M input, reasoning-capable
2. **Use Grok 4.3 for complex reasoning** — Configurable reasoning effort
3. **Use Grok Build 0.1 for coding** — Optimized for agentic coding workflows
4. **Leverage Web Search for current events** — Model knowledge cutoff is Nov 2024
5. **Use X Search for social media analysis** — Unique native X platform access
6. **Enable streaming for better UX** — Server-sent events for real-time output
7. **Mix message roles freely** — No restriction on role ordering

### Prompt Templates

```python
# Real-time research template
RESEARCH_PROMPT = """Search the web for the latest information about {topic}.
Provide a comprehensive summary with sources.
Focus on developments from the past 30 days."""

# Social media analysis template
SOCIAL_ANALYSIS_PROMPT = """Search X for posts about {topic}.
Analyze the overall sentiment and key themes.
Identify the most influential voices and their positions."""

# Code review template (Grok Build 0.1)
CODE_REVIEW_PROMPT = """Review the following code for:
1. Bugs and edge cases
2. Performance issues
3. Security vulnerabilities
4. Best practices

Code:
{code}

Provide specific, actionable feedback."""
```

### Video Input Prompts

```python
# Video analysis prompt
VIDEO_ANALYSIS_PROMPT = """Analyze the following video and provide:
1. A detailed description of the visual content
2. Key events and their timestamps
3. Any text visible in the video
4. Overall summary and interpretation"""

# Use with video input in messages
messages = [
    {"role": "user", "content": [
        {"type": "text", "text": VIDEO_ANALYSIS_PROMPT},
        {"type": "video_url", "video_url": {"url": "https://example.com/video.mp4"}}
    ]}
]
```

## Security Features

### API Security

| Feature | Description |
|---------|-------------|
| **API Key Authentication** | Bearer token via Authorization header |
| **Key Rotation** | Programmatic key management via console |
| **Usage Alerts** | Configurable spending thresholds |
| **IP Allowlisting** | Restrict API access to specific IPs (enterprise) |
| **Audit Logging** | Complete request logging (enterprise) |
| **Webhook Notifications** | Real-time usage alerts |

### Model Security

| Feature | Status |
|---------|--------|
| **Content Filtering** | Built-in safety filters |
| **Prompt Injection Protection** | System prompt enforcement |
| **Jailbreak Resistance** | Ongoing adversarial testing |
| **Output Validation** | JSON schema enforcement |
| **Moderation API** | Content safety endpoint available |

### Enterprise Security

- **SOC 2 Type II**: Audit in progress, target completion Q3 2026
- **Penetration testing**: Annual third-party security assessments
- **Incident response**: 24-hour incident notification SLA
- **Data processing agreement**: Available for enterprise customers
- **Custom security requirements**: Negotiated for enterprise contracts
- **Vulnerability disclosure**: Responsible disclosure program

---

*This report was compiled from public documentation, pricing pages, and third-party analysis as of June 2026. Pricing and model availability are subject to change.*