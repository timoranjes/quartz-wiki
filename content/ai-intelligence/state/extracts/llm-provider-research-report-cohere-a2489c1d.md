# LLM Provider Research Report: Cohere

> Research date: June 2026. Covers Cohere company overview, model lineup, API pricing, benchmarks, capabilities, competitive positioning, and recent developments.

---

## 1. Cohere Company Overview

### 1.1 Founding and Mission

Cohere is a Canadian artificial intelligence company founded in 2019 by:
- **Aidan Gomez** (CEO): Co-author of the original "Attention Is All You Need" transformer paper, former Google Brain researcher
- **Nick Frosst**: Former Google Brain researcher
- **Ivan Zhang**: Former Google Brain researcher

The company emerged from the University of Toronto and Google Brain research ecosystem with a clear enterprise-first focus. Unlike consumer-facing AI companies, Cohere was built from day one to serve enterprise customers with mission-critical AI needs.

### 1.2 Mission and Philosophy

Cohere's core philosophy centers on:
1. **Enterprise trust**: Building AI systems that enterprises can rely on for production workloads
2. **RAG excellence**: Best-in-class retrieval, embedding, and reranking capabilities
3. **Customization**: Enabling organizations to build AI systems tuned to their specific data and workflows
4. **Data privacy**: Strong data governance, SOC 2 compliance, and zero-retention policies
5. **Multilingual capability**: Supporting global enterprise deployments

### 1.3 Funding and Valuation

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| Seed | 2019 | $4.5M | — | Amplify Partners |
| Series A | 2021 | $40M | ~$200M | Index Ventures |
| Series B | 2021 | $125M | ~$1B | Tiger Global |
| Series C | 2023 | $270M | ~$2.2B | In-Q-Tel, Oracle |
| Series D | 2024 | $500M | ~$5.5B | NVIDIA, Oracle |
| Later rounds | 2025-2026 | ~$1B+ | ~$10B+ | NVIDIA, Salesforce, multiple |

Total raised: Approximately $2-2.5 billion across all rounds.

**Strategic investors**: NVIDIA, Oracle, Salesforce, and In-Q-Tel (CIA's venture arm) have invested in Cohere, reflecting its importance to enterprise and government AI infrastructure.

### 1.4 Headquarters and Global Presence

- **Headquarters**: Toronto, Canada
- **Offices**: Palo Alto, London, Tokyo
- **Team size**: Approximately 400-500+ employees (mid-2026)

### 1.5 Strategic Partnerships

Cohere has deep partnerships with major cloud providers:
- **Amazon Bedrock**: Cohere models available as managed service
- **Azure AI Foundry**: Cohere models available via Microsoft Azure
- **Oracle Cloud Infrastructure (OCI)**: Cohere models available on Oracle GenAI
- **Amazon SageMaker**: Custom model deployment

These partnerships enable Cohere to reach enterprise customers through their existing cloud infrastructure, a key differentiator from API-only providers.

---

## 2. Current Model Lineup (as of June 2026)

### 2.1 Command Family: Text Generation and Chat

The Command family is Cohere's flagship text generation lineup, powering instruction-following, chat, RAG, tool use, translation, and vision tasks.

#### Command A+ (Flagship)

| Attribute | Value |
|-----------|-------|
| Model ID | `command-a-plus-05-2026` |
| Status | ✅ Live |
| Architecture | **MoE** (Cohere's first Mixture-of-Experts model) |
| Context Window | 128K tokens |
| Output Limit | 64K tokens |
| Modality | Text + Images |
| Key Features | Vision, reasoning, translation, agentic capabilities |

Command A+ represents Cohere's most advanced model, combining multiple capabilities:
- Vision understanding (image analysis)
- Reasoning capabilities
- Translation across 23 languages
- Agentic tool use
- First MoE architecture from Cohere

#### Command A

| Attribute | Value |
|-----------|-------|
| Model ID | `command-a-03-2025` |
| Status | ✅ Live |
| Context Window | 256K tokens |
| Output Limit | 8K tokens |
| Modality | Text |
| Key Features | Highest single-model performance, 150% throughput over Command R+ |

Command A offers Cohere's highest single-model performance with a large 256K context window, though with a more limited 8K output ceiling.

**Pricing for Command A:**
- Input: $2.50 / 1M tokens
- Output: $10.00 / 1M tokens
- Blended rate: ~$4.38 / 1M tokens (at typical 7:2:1 ratio)

#### Command R7B

| Attribute | Value |
|-----------|-------|
| Model ID | `command-r7b-12-2024` |
| Status | ✅ Live |
| Context Window | 128K tokens |
| Output Limit | 4K tokens |
| Key Features | Fast, small model for RAG/tool use/reasoning |

**Pricing:**
- Input: $0.0375 / 1M tokens
- Output: $0.15 / 1M tokens

Command R7B is Cohere's cheapest chat model, ideal for high-volume RAG and tool-use applications where cost efficiency matters.

#### Command R+

| Attribute | Value |
|-----------|-------|
| Model ID | `command-r-plus-08-2024` |
| Status | ✅ Live |
| Context Window | 128K tokens |
| Output Limit | 4K tokens |
| Key Features | Best for complex RAG and tool use |

**Pricing:**
- Input: $2.50 / 1M tokens
- Output: $10.00 / 1M tokens

Command R+ remains popular for enterprise RAG pipelines due to its strong retrieval integration and tool-use capabilities.

#### Command R

| Attribute | Value |
|-----------|-------|
| Model ID | `command-r-08-2024` |
| Status | ✅ Live |
| Context Window | 128K tokens |
| Output Limit | 4K tokens |
| Key Features | Conversational and tool use |

**Pricing:**
- Input: $0.15 / 1M tokens
- Output: $0.60 / 1M tokens

Command R is the mid-tier option, balancing cost and capability for general conversational and tool-use tasks.

#### Specialized Command Models

| Model | Model ID | Context | Purpose |
|-------|----------|---------|---------|
| Command A Translate | `command-a-translate-08-2025` | 8K | SOTA translation across 23 languages |
| Command A Reasoning | `command-a-reasoning-08-2025` | 256K | Dedicated reasoning with 23-language support |
| Command A Vision | `command-a-vision-07-2025` | 128K | OCR, charts, tables, visual Q&A |

### 2.2 Embed Family: Embeddings

Cohere's embedding models are among the most widely used in enterprise RAG pipelines.

#### Embed v3 / v4

| Attribute | Value |
|-----------|-------|
| Input Pricing | $0.10 / 1M tokens (input-only) |
| Dimensions | 1024 (configurable) |
| Languages | 100+ languages |
| Modalities | Text, images (some), mixed/PDFs (v4.0) |
| Distance Metrics | Cosine, Dot Product, Euclidean Distance |

**Embed Models:**

| Model | Description | Modalities |
|-------|-------------|------------|
| Embed v3 English | English text embeddings | Text |
| Embed v3 Multilingual | 100+ language embeddings | Text |
| Embed v4.0 | Latest generation, PDF support | Text + Images + PDFs |

### 2.3 Rerank Family: Search Re-ranking

Cohere's rerank models are considered best-in-class for search result re-ranking.

#### Rerank v3

| Attribute | Value |
|-----------|-------|
| Pricing | $2 / 1M searches |
| Languages | 100+ languages |
| Purpose | Fast, accurate document reordering |

**Note**: Rerank models are priced per search (not per token), which makes cost estimation different from chat models.

### 2.4 Aya Family: Multilingual LLMs

#### Aya Vision

| Attribute | Value |
|-----------|-------|
| Parameters | 32B |
| Languages | 70+ languages |
| Modality | Multimodal (text + image) |
| License | Open-weight variants available |
| Purpose | Multilingual LLM, minority language support |

Aya is Cohere's multilingual model family, with particular strength in supporting underrepresented and minority languages. Aya Vision adds multimodal capabilities to the multilingual foundation.

### 2.5 Audio (Transcribe)

| Attribute | Value |
|-----------|-------|
| Purpose | Speech-to-text (ASR) |
| Languages | Multilingual |
| Use Case | Transcribing multilingual audio files |

---

## 3. Pricing Details (2026)

### 3.1 Chat Model Pricing Summary

| Model | Input ($/1M) | Output ($/1M) | Blended Rate* |
|-------|-------------|---------------|---------------|
| **Command A+** | TBD | TBD | TBD |
| **Command A** | $2.50 | $10.00 | ~$4.38 |
| **Command R+** | $2.50 | $10.00 | ~$4.38 |
| **Command R** | $0.15 | $0.60 | ~$0.26 |
| **Command R7B** | $0.0375 | $0.15 | ~$0.07 |

*Blended rate at 7:2:1 cache-hit:input:output ratio

### 3.2 Embedding Pricing

| Model | Pricing |
|-------|---------|
| Embed v3 English | $0.10 / 1M input tokens |
| Embed v3 Multilingual | $0.10 / 1M input tokens |
| Embed v4.0 | TBD |

### 3.3 Rerank Pricing

| Model | Pricing |
|-------|---------|
| Rerank v3 | $2 / 1M searches |

### 3.4 Pricing Principles

- **Pay-as-you-go**: Production API keys use pay-as-you-go pricing
- **No upfront costs**: No minimum commitments for self-serve
- **Tiered enterprise contracts**: Volume discounts for enterprise customers
- **Custom pricing**: For high-volume clients and private deployments
- **Private deployment**: ~20% of revenue from custom model deployment within customer infrastructure

---

## 4. API Details

### 4.1 Platform Support

Cohere models are accessible across multiple platforms:

| Platform | Link |
|----------|------|
| Cohere Dashboard (Playground) | dashboard.cohere.com |
| Amazon Bedrock | us-west-2.console.aws.amazon.com/bedrock |
| Microsoft Azure | ai.azure.com/explore/models |
| Oracle GenAI Service | oracle.com/artificial-intelligence |
| Amazon SageMaker | aws.amazon.com/marketplace |

### 4.2 API Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/chat` | Text generation and chat |
| `/embed` | Text embedding generation |
| `/embed-jobs` | Batch embedding generation |
| `/rerank` | Search result re-ranking |
| `/classify` | Text classification |
| `/summarize` | Text summarization |
| `/detect-language` | Language detection |

### 4.3 Chat API Features

| Feature | Supported | Notes |
|---------|-----------|-------|
| Tool use | ✅ | Built-in tool calling for agents |
| RAG | ✅ | Native citation and grounding |
| Streaming | ✅ | Server-sent events |
| Multi-turn | ✅ | Full conversation context |
| System prompts | ✅ | System-level instructions |
| Vision | ✅ | In Command A Vision and A+ |
| Structured output | ✅ | JSON mode |

### 4.4 Python SDK

```python
import cohere

co = cohere.ClientV2(api_key="YOUR_API_KEY")

response = co.chat(
    model="command-a-plus-05-2026",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
```

### 4.5 Cloud Provider Model IDs

| Model | Amazon Bedrock | Azure AI Foundry | Oracle OCI |
|-------|---------------|------------------|------------|
| Command A+ | N/A | `command-a-plus-05-2026` | N/A |
| Command A | (Coming Soon) | Unique per deployment | `cohere.command-a-03-2025` |
| Command R+ | `cohere.command-r-plus-v1:0` | Unique per deployment | `cohere.command-r-plus v1.2` |
| Command R | `cohere.command-r-v1:0` | Unique per deployment | `cohere.command-r-16k v1.2` |

---

## 5. Benchmarks and Performance

### 5.1 Command A Performance

| Benchmark | Command A | Notes |
|-----------|-----------|-------|
| Context Window | 256K | Strong long-context handling |
| Instruction Following | Solid | Good at following complex instructions |
| Reasoning | Modest | Behind dedicated reasoning models |
| Coding | Modest | Not a coding-optimized model |
| RAG | **Best-in-class** | Strong citation and grounding |
| Tool Use | Strong | Native tool calling support |

### 5.2 Embedding Model Quality

Cohere's Embed v3 is widely regarded as one of the top embedding models, consistently ranking highly on:
- MTEB (Massive Text Embedding Benchmark)
- Multilingual retrieval tasks
- Classification accuracy

### 5.3 Rerank Model Quality

Cohere's Rerank models are considered **best-in-class** for search re-ranking, with:
- High accuracy on standard benchmarks
- Fast inference latency
- 100+ language support
- Support for long documents

### 5.4 Pricing vs. Performance Assessment

**Command A**: At $2.50/$10 per million tokens, Command A is priced at a premium relative to its capability tier. Independent analysis suggests:
- Reasoning benchmarks are modest compared to GPT-5 and Claude
- Coding benchmarks are below coding-optimized models
- Strong instruction following and RAG capabilities justify the price for existing Cohere customers
- May suit enterprise customers already in the Cohere ecosystem

**Command R+**: Similarly priced to Command A but with different strengths — particularly strong for RAG and tool use.

**Command R**: At $0.15/$0.60, offers good value for general conversational tasks.

**Command R7B**: At $0.0375/$0.15, is Cohere's cheapest chat model and competitive with other small models.

---

## 6. Capabilities

### 6.1 Core Capabilities

| Capability | Supported | Notes |
|-----------|-----------|-------|
| Text generation | ✅ | Command family |
| Image understanding | ✅ | Command A Vision, Command A+ |
| Embeddings | ✅ | Embed v3/v4, 100+ languages |
| Reranking | ✅ | Rerank v3, per-search pricing |
| Classification | ✅ | Built-in classification endpoint |
| Summarization | ✅ | Built-in summarization endpoint |
| Language detection | ✅ | 100+ languages |
| Translation | ✅ | Command A Translate, 23 languages |
| Speech-to-text | ✅ | Audio/Transcribe |
| RAG | ✅ | **Core strength** — native citation/grounding |
| Tool use | ✅ | Built-in agent support |
| Multilingual | ✅ | 70-100+ languages |

### 6.2 Strengths

1. **RAG leadership**: Best-in-class embeddings, reranking, and RAG-native chat models
2. **Enterprise trust**: SOC 2 compliance, zero-retention, data governance
3. **Cloud partnerships**: Deep integration with AWS, Azure, Oracle
4. **Enterprise focus**: Built for production from day one
5. **Multilingual**: Strong support for 70-100+ languages
6. **API simplicity**: Clean, well-documented API with multiple endpoints
7. **Private deployment**: Custom model deployment within customer infrastructure
8. **Aya multilingual**: Specialized in underrepresented languages

### 6.3 Limitations

1. **Raw performance gap**: Command models trail GPT-5 and Claude on general benchmarks
2. **Premium pricing**: Command A/R+ pricing is high relative to capability tier
3. **No open weights**: Unlike Meta/Mistral, Cohere models are closed-weight
4. **Smaller model range**: Fewer specialized models vs. competitors
5. **Limited coding focus**: Not optimized for coding tasks
6. **Output limits**: Some models have relatively small output limits (4K-8K)

---

## 7. Competitive Positioning

### 7.1 Market Position

Cohere is positioned as:
- **Enterprise RAG specialist**: The go-to provider for retrieval-augmented generation
- **Embedding and reranking leader**: Best-in-class search infrastructure models
- **Cloud ecosystem player**: Deep AWS, Azure, and Oracle integrations
- **Multilingual AI provider**: Strong support for global enterprise deployments

### 7.2 Competitive Landscape

| Competitor | Cohere's Advantage | Cohere's Disadvantage |
|-----------|-------------------|----------------------|
| **OpenAI** | Embedding quality, RAG specialization, enterprise trust | General model performance, ecosystem |
| **Anthropic** | RAG/embedding specialization, cloud partnerships | General model performance, brand |
| **Google Gemini** | RAG specialization, cloud partnerships | Compute scale, multimodal breadth |
| **Mistral** | RAG/embedding specialization, cloud partnerships | Open weights, pricing, EU presence |
| **Voyage AI** | Full model range (chat + embed + rerank) | Pure embedding/rerank focus |
| **NVIDIA** | RAG specialization, cloud partnerships | GPU/infrastructure ecosystem |

### 7.3 Target Customers

1. **Enterprise RAG pipelines**: Organizations building search and knowledge retrieval systems
2. **Cloud-first enterprises**: Customers already on AWS, Azure, or Oracle
3. **Global deployments**: Organizations needing 70-100+ language support
4. **Regulated industries**: Healthcare, finance, government with strict data governance needs
5. **Search platforms**: Companies needing embedding and reranking infrastructure

---

## 8. Revenue Model

### 8.1 Revenue Streams

| Stream | Share | Description |
|--------|-------|-------------|
| **API Usage (Pay-as-you-go)** | ~60% | Token-based pricing for Production API keys |
| **Private LLM Deployment** | ~20% | Custom model deployment within customer infrastructure |
| **Enterprise Contracts** | ~15% | Tiered enterprise contracts with volume discounts |
| **Custom Solutions** | ~5% | Bespoke AI solutions for high-volume clients |

### 8.2 Pricing Model

- **Usage-based**: Pay-as-you-go for any application using a Production API key
- **No wasted spend**: Only charged for what you use
- **Tiered pricing**: Volume discounts for enterprise customers
- **Custom pricing**: For high-volume clients and private deployments

---

## 9. Recent Developments (Mid-2026)

### 9.1 Command A+ Launch (May 2026)

Cohere's first MoE model, combining:
- Vision understanding
- Reasoning capabilities
- Translation across 23 languages
- Agentic tool use
- 128K context window, 64K output limit

### 9.2 Embed v4.0

Latest generation embedding model with:
- PDF support
- Mixed modality (text + images)
- Improved multilingual performance

### 9.3 Cloud Platform Expansion

Expanded availability on:
- Amazon Bedrock (managed service)
- Azure AI Foundry (managed service)
- Oracle GenAI Service
- Amazon SageMaker (custom deployment)

### 9.4 Aya Vision

32B parameter multimodal multilingual model:
- 70+ languages
- Text + image understanding
- Open-weight variants available

### 9.5 Funding and Growth

- Continued funding from strategic investors (NVIDIA, Oracle, Salesforce)
- Growing enterprise customer base
- Expansion of private deployment offerings

---

## 10. API Features Comparison

### 10.1 Feature Matrix

| Feature | Command A+ | Command A | Command R+ | Command R |
|---------|-----------|-----------|------------|-----------|
| Context Window | 128K | 256K | 128K | 128K |
| Output Limit | 64K | 8K | 4K | 4K |
| Vision | ✅ | ❌ | ❌ | ❌ |
| Reasoning | ✅ | ❌ | ❌ | ❌ |
| Translation | ✅ | ❌ | ❌ | ❌ |
| Tool Use | ✅ | ✅ | ✅ | ✅ |
| RAG/Citation | ✅ | ✅ | ✅ | ✅ |
| Streaming | ✅ | ✅ | ✅ | ✅ |
| MoE Architecture | ✅ | ❌ | ❌ | ❌ |

### 10.2 Integration Support

- **SDKs**: Python, TypeScript, CLI
- **LangChain**: ✅ Full support
- **LlamaIndex**: ✅ Full support
- **Cloud platforms**: AWS Bedrock, Azure AI, Oracle OCI
- **Fine-tuning**: Available via cloud partners

---

## 11. Summary and Recommendations

### 11.1 When to Choose Cohere

- **RAG-first architectures**: Best-in-class embeddings, reranking, and RAG-native models
- **Enterprise compliance**: SOC 2, zero-retention, strong data governance
- **Cloud-native deployments**: Deep AWS, Azure, and Oracle integrations
- **Multilingual applications**: 70-100+ language support
- **Search infrastructure**: Embedding and reranking for search platforms
- **Regulated industries**: Healthcare, finance, government

### 11.2 When to Look Elsewhere

- **Best general performance**: OpenAI GPT-5.x or Claude Opus for general tasks
- **Open-weight requirements**: Meta Llama or Mistral for self-hosting
- **Cost optimization**: Mistral or DeepSeek for cheaper general models
- **Coding tasks**: Codestral, Claude, or GPT for code-specific workloads
- **Cutting-edge research**: Latest frontier models from OpenAI/Google

### 11.3 Outlook

Cohere occupies a defensible niche as the enterprise RAG and search infrastructure specialist. Its deep cloud partnerships, best-in-class embedding/reranking models, and enterprise-focused approach provide a strong moat. Key questions include:
- Can Cohere's Command models close the gap with frontier general models?
- Will open-weight alternatives erode Cohere's embedding/reranking advantage?
- Can Cohere maintain enterprise differentiation as larger competitors improve RAG capabilities?

---

*This report was compiled from public documentation, pricing pages, and third-party analysis as of June 2026. Pricing and model availability are subject to change.*