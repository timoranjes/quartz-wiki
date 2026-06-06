# Zhipu AI (Z.ai): Comprehensive Research Report (2026)

## Executive Summary

Zhipu AI, now operating globally under the brand name **Z.ai**, is a Beijing-based artificial intelligence company founded in 2019 as a spinout from Tsinghua University. The company is the developer of the **GLM (General Language Model)** family of large language models and is recognized as one of China's "Six AI Tigers" — the leading cohort of Chinese AI startups building foundation models to compete with global leaders like OpenAI and Anthropic.

In January 2026, Zhipu AI made history by becoming the **world's first major large language model company to go public**, listing on the Hong Kong Stock Exchange (SEHK: 2513). The IPO raised approximately HK$4.35 billion (~US$558 million) and valued the company at approximately HK$51.16 billion (~US$6.8 billion) at debut, with shares rising 13.1% on the first trading day.

As of mid-2026, Z.ai has evolved from an open-source LLM provider into a comprehensive enterprise AI platform, with the GLM model family spanning open-source variants (GLM-4.5 under MIT License) to flagship enterprise models (GLM-5 with 744B MoE architecture). The company has also developed multimodal products including the Ying text-to-video model, AutoGLM autonomous agent platform, and Qingyan conversational assistant.

## Company Overview

### Legal Identity and Branding

| Attribute | Detail |
|-----------|--------|
| **Legal Name** | Knowledge Atlas Technology Joint Stock Co., Ltd. (北京智谱华章科技有限公司) |
| **Trade Name** | Z.ai (global brand), Zhipu AI (China, pre-2025) |
| **Founded** | 2019 (Tsinghua University spinout) |
| **Headquarters** | Beijing, China |
| **CEO** | Zhang Peng |
| **Founders** | Tang Jie, Li Juanzi |
| **Employees** | 800+ (2024) |
| **Stock Listing** | SEHK: 2513 — IPO on January 8, 2026 |
| **Websites** | zhipuai.cn (China), z.ai (global) |
| **Status** | Public company, China's first major LLM IPO |

### Origins: Tsinghua University Connection

Zhipu AI emerged from the **Knowledge Engineering Group (KEG)** at Tsinghua University, one of China's most prestigious institutions. The founding team's academic roots provided deep expertise in:

- Natural language processing
- Knowledge graphs and representation learning
- Large-scale machine learning systems
- Academic research and publication

The company's early work on the GLM architecture was published in peer-reviewed venues, establishing scientific credibility before commercial launch.

### AMiner Integration

Zhipu AI acquired **AMiner**, an academic search engine and knowledge graph created by co-founder Jie Tang in 2006. AMiner provides:

- Academic paper search and discovery
- Researcher profiles and networks
- Knowledge graph construction
- Integration into Z.ai's broader ecosystem

This acquisition gave Zhipu unique access to academic data and researcher networks, supporting both model training and product development.

## The GLM Model Family

GLM stands for "General Language Model" and represents the core technology platform of Z.ai. The architecture was first introduced in a 2022 ACL paper:

> "GLM: General Language Model Pretraining with Autoregressive Blank Infilling"
> — Du et al., ACL 2022

### Key Architectural Features

- **Autoregressive blank infilling**: Cloze-style training objective
- **Multimodal reasoning**: Text, image, audio, and video processing
- **Tool-calling**: Native support for function calling and external tool use
- **Voice capabilities**: End-to-end speech language models
- **Coding proficiency**: Strong performance on code generation and understanding
- **Long-horizon agentic tasks**: Extended reasoning and multi-step execution
- **Domestic chip optimization**: Runs on Huawei Ascend, Cambricon, and Moore Threads hardware

### Model Timeline (2024–2026)

| Model | Release Date | License | Parameters | Key Features |
|-------|--------------|---------|------------|--------------|
| GLM-4-Plus | Aug 2024 | Proprietary | — | Enhanced reasoning and multilingual support |
| GLM-4-Voice | Oct 2024 | Source-available | — | End-to-end speech LLM; tone/dialect control |
| GLM-4.1V-Thinking | Jul 2025 | MIT | — | Vision-language model with reasoning capabilities |
| GLM-4.5 / GLM-4.5 Air | Jul 2025 | MIT | — | First under MIT License; runs on 8× NVIDIA H20 |
| GLM-4.5V | Aug 11, 2025 | Open | 106B | Visual understanding model; open-sourced |
| GLM-4.6 | Sep 2025 | — | — | First FP8/Int4 quantization on Cambricon chips |
| GLM-4.6V | Dec 2025 | — | — | Vision-language model with native tool-calling |
| GLM-4.7 | Dec 2025 | — | — | Strong coding; outperforms Gemini 3.0 Pro in some benchmarks |
| GLM-5 | Feb 11, 2026 | Proprietary | 744B MoE | 40B active params; 28.5T tokens; 200K context |
| GLM-5 Turbo | 2026 | Proprietary | — | Optimized for tool invocation, timed tasks |
| GLM-5.1 | Apr 8, 2026 | MIT | — | AI coding agents run autonomously for hours |

### GLM-5 Technical Specifications

GLM-5 represents Z.ai's flagship model with significant architectural advances:

| Specification | Value |
|---------------|-------|
| **Architecture** | Mixture-of-Experts (MoE) |
| **Total Parameters** | 744B |
| **Active Parameters/Inference** | ~40B |
| **Training Data** | 28.5 trillion tokens |
| **Context Window** | 200K tokens |
| **Training Hardware** | Huawei Ascend chips (no NVIDIA dependency) |
| **Release Theme** | "From Vibe Coding to Agentic Engineering" |

### Open-Source Strategy

In April 2025, Zhipu released its 32B and 9B GLM model series (base, reasoning, and rumination variants) under the **MIT License**, marking a significant shift toward open-source accessibility. This strategy:

- Enables commercial use without licensing restrictions
- Builds developer community and adoption
- Provides transparent benchmarks and reproducibility
- Creates a lower-friction path into the Z.ai ecosystem

### Hardware Independence

A key strategic advantage for Z.ai is its ability to train and run models on **domestic Chinese chips**:

- **Huawei Ascend**: Primary training hardware for GLM-5
- **Cambricon**: Native FP8/Int4 quantization support (GLM-4.6 onward)
- **Moore Threads**: Native FP8 support on domestic GPUs
- **NVIDIA H20**: Used for GLM-4.5 (8× H20 configuration)

This hardware independence protects Z.ai from US export restrictions on advanced semiconductors.

## Product Ecosystem

### Qingyan AI (Conversational Assistant)

- Consumer-facing conversational interface
- RAG (Retrieval-Augmented Generation) capabilities
- Web browsing and search integration
- Data visualization
- Multi-step reasoning
- Document analysis

### Ying (影) — Text-to-Video Model

| Feature | Detail |
|---------|--------|
| **Launch** | July 2024 |
| **Output** | 6-second video clips from image/text prompts |
| **Generation Time** | ~30 seconds |
| **Positioning** | Competitor to OpenAI's Sora |
| **Architecture** | Built on Z.ai's diffusion and transformer technologies |

Ying represents Z.ai's entry into the competitive text-to-video generation market, providing an alternative to OpenAI's Sora and other video models.

### AutoGLM — Autonomous Agent Platform

AutoGLM is Z.ai's platform for autonomous AI agents:

- **Planning and tool orchestration**: Multi-step task execution
- **Persistent state**: Long-running agent sessions
- **AutoGLM Phone**: Action-taking agent extending beyond chat to real-world app interaction
- **AutoGLM 2.0** (August 2025): World's first mobile agent capable of handling tasks across different apps

**Key capabilities**:
- Voice command interaction
- Cross-app task completion (ordering items, repeat orders using shopping history)
- Real-world agentic AI demonstrations
- Enterprise deployment options

### CodeGeeX

- Code generation tool supporting multiple programming languages
- Integrated development environment (IDE) plugins
- Code completion and generation
- Part of Z.ai's developer tooling ecosystem

### CogVLM and CogView

- **CogVLM**: Vision-language model for image understanding
- **CogView**: Text-to-image generation model
- Earlier vision models that laid groundwork for GLM-4.5V and GLM-4.6V

### CogVideoX

- Released in 2024 under Apache 2.0 License
- DiT-based (Diffusion Transformer) open-source text-to-video model
- Uses 3D causal variational autoencoder architecture
- Open-weight availability for community development

## Developer Access and Integration

### API Platform

- **OpenAI-compatible** SDKs and endpoints
- **API endpoint**: `openapi.zhipu.ai`
- Supports cURL, Python, Java SDKs
- Drop-in replacement for existing OpenAI integrations
- Enterprise SLAs and support

### Model-as-a-Service (MaaS)

Z.ai offers a MaaS platform providing:

- Hosted model access via API
- Custom deployment options
- Enterprise security controls
- Local deployment capabilities
- AutoGLM integration for autonomous agents

### Hugging Face Integration

- GLM-4.5 open weights available on Hugging Face
- Community fine-tunes and adaptations
- Local quantized inference support
- Open-source licensing (MIT for select models)

## Funding and Financials

### Funding History

| Date | Round | Amount | Valuation | Key Investors |
|------|-------|--------|-----------|---------------|
| Oct 2023 | Series B | ¥2.5B (~$350M) | — | Alibaba, Tencent, Meituan, Ant Group, Xiaomi, HongShan |
| May 2024 | Series C | $400M | ~$3B | Led by Prosperity7 Ventures (Saudi Arabia) |
| May 2025 | Government Deal | ¥61.28M | — | Hangzhou city projects |
| Jan 2026 | IPO | ~HK$4.35B (~$558M) | ~HK$51.16B (~$6.8B) | Public offering on HKEX |

### IPO Details (January 8, 2026)

| Detail | Value |
|--------|-------|
| **Ticker** | 2513.HK |
| **Offer Price** | HK$116.20 per share (~$15) |
| **Shares Offered** | 37.42 million H-shares |
| **Amount Raised** | HK$4.35 billion (~US$558 million) |
| **IPO Valuation** | ~HK$51.16 billion (~US$6.8 billion) |
| **First Day Close** | HK$131.5 (+13.1%) |
| **First Day High** | +16% above offer price |
| **Use of Proceeds** | 70% for general-purpose AI model R&D (2026–2028) |

### Revenue

| Year | Revenue | Notes |
|------|---------|-------|
| 2024 | 312.4 million yuan (~$43M) | Per prospectus |
| 2025 | Growing | Post-IPO expansion |

### Post-IPO Performance

- Shares rose 11.5% following GLM-5.1 release in April 2026
- February 2026: Shares dropped 23% amid broader market concerns
- Market capitalization fluctuated between HK$40–55 billion range

## Global Expansion and Partnerships

### International Presence

| Region | Activity |
|--------|----------|
| **Middle East** | Offices established; Prosperity7 Ventures invested $400M (May 2024) |
| **United Kingdom** | Office established (2025) |
| **Singapore** | Office established (2025) |
| **Malaysia** | Office established (2025) |
| **Southeast Asia** | Innovation centers in Indonesia and Vietnam (2025) |

### Strategic Partnerships

| Partner | Nature of Partnership |
|---------|----------------------|
| **Huawei** | GLM models optimized for Ascend chips (August 2025) |
| **Cambricon** | Native FP8/Int4 quantization support |
| **Moore Threads** | Native FP8 on domestic GPUs |
| **Prosperity7 Ventures** | $400M investment; Saudi sovereign wealth connection |

### US Entity List Placement

- **Date**: June 26, 2025
- **Action**: Added to US Commerce Department's Entity List
- **Reason**: National security concerns; alleged work with China's military
- **Impact**: Restrictions on access to advanced US semiconductor technology
- **Response**: Continued model development on domestic Chinese chips

## Competitive Positioning

### Among China's "Six AI Tigers"

Z.ai is one of six leading Chinese AI startups collectively known as the "Six AI Tigers" (大模型六小虎):

| Company | HQ | Notable Founders | Major Products |
|---------|----|------------------|----------------|
| **Z.ai (Zhipu AI)** | Beijing | Tang Jie, Zhang Peng | GLM-4/5, AutoGLM, Ying |
| **Moonshot AI** | Beijing | Yang Zhilin | Kimi chatbot |
| **MiniMax** | Shanghai | Yan Junjie | abab series, Hailuo AI, Talkie |
| **Baichuan AI** | Beijing | Wang Xiaochuan | Baichuan-4, Baixiaoying |
| **01.AI** | Beijing | Kai-Fu Lee | Yi series |
| **StepFun** | Shanghai | Jiang Daxin | Step series |

### Market Position

- **IDC Ranking**: #3 LLM player in China (2024)
- **First to IPO**: World's first major LLM company to go public
- **Open-source leadership**: MIT-licensed GLM models for developer adoption
- **Platform strategy**: Unified models, APIs, agents, and applications

### Global Competitive Context

Z.ai competes with:

- **OpenAI**: GPT series, ChatGPT ecosystem
- **Anthropic**: Claude family of models
- **Google**: Gemini models
- **Meta**: Llama open-weight models
- **Chinese peers**: DeepSeek, MiniMax, Moonshot AI, Baichuan AI

## Challenges and Controversies

### US Entity List

- Placement on US Commerce Department Entity List (June 2025)
- Restrictions on advanced semiconductor access
- Potential limitations on international partnerships
- Necessitated development of domestic chip ecosystem

### Market Volatility

- Post-IPO share price volatility
- February 2026: 23% single-day drop
- Revenue gap concerns relative to valuation
- Competition from well-funded Chinese and global peers

### Regulatory Environment

- Chinese AI regulations evolving
- Data privacy and security requirements
- Cross-border data transfer restrictions
- Compliance with both Chinese and international regulations

### Technical Challenges

- Maintaining pace with global model advancements
- Hardware constraints due to US sanctions
- Balancing open-source strategy with commercial interests
- Scaling agent capabilities and reliability

## Enterprise Applications

### Evaluation Framework for Enterprises

Z.ai provides guidance for enterprise evaluation:

1. **Quality & Reasoning Consistency**: Build golden datasets, test hallucination rates, check persona consistency
2. **Latency & Throughput**: Measure TTFT, test tokens/sec under load, negotiate SLAs
3. **Total Cost of Ownership**: Analyze prompt-to-completion ratio, compare tokens per task
4. **Safety & Governance**: Understand refusal rates, content filtering, data privacy controls

### Deployment Options

- **Cloud API**: OpenAI-compatible endpoints for rapid integration
- **Local Deployment**: Enterprise on-premises deployment with security controls
- **MaaS Platform**: Managed service with AutoGLM integration
- **Custom Fine-tuning**: Domain-specific model adaptation

## Future Outlook

### Strategic Direction

- **Platform-first approach**: Shift from chat interfaces to agent-based workflows
- **Coding automation**: GLM-5.1 enables AI coding agents to run autonomously
- **Multimodal execution**: Combining text, vision, audio, and video capabilities
- **Long-horizon reasoning**: Extended context windows and persistent task execution
- **Global expansion**: International offices and partnerships

### Product Roadmap

- Continued GLM model evolution (beyond GLM-5.1)
- AutoGLM expansion to more platforms and use cases
- Ying video model improvements
- Enterprise agent platform development
- Integration with Chinese chip ecosystem

### Industry Impact

As the first major LLM company to go public, Z.ai's trajectory provides a benchmark for:

- Valuation multiples for AI model companies
- Revenue growth expectations
- Open-source vs. proprietary model strategies
- International expansion under geopolitical constraints
- Enterprise AI adoption patterns in Asia

## Key Statistics Summary

| Metric | Value |
|--------|-------|
| Founded | 2019 |
| Headquarters | Beijing, China |
| CEO | Zhang Peng |
| Founders | Tang Jie, Li Juanzi |
| Employees | 800+ (2024) |
| Stock Ticker | 2513.HK |
| IPO Date | January 8, 2026 |
| IPO Price | HK$116.20 |
| IPO Valuation | ~HK$51.16B (~US$6.8B) |
| Flagship Model | GLM-5 (744B MoE) |
| Open-Source Model | GLM-4.5 (MIT License) |
| Context Window | 200K tokens (GLM-5) |
| 2024 Revenue | 312.4M yuan |
| Total Funding | ~$750M+ pre-IPO |
| US Entity List | Yes (June 2025) |

## References and Sources

- Wikipedia: Z.ai
- ChoZan: Zhipu AI Explained: GLM Capabilities, Use Cases, and Risks
- CNBC: The first of China's 'AI tigers' goes public as Zhipu climbs in Hong Kong debut
- Reuters: Chinese tech firms rise in Hong Kong debut
- Caixin Global: China's Zhipu AI Jumps in Hong Kong Debut
- South China Morning Post: China's Zhipu AI launches US$560 million share sale
- PRNewswire: Z.ai Unveils New GLM Open-Source Models
- 36Kr: Zhipu Releases 100-Billion-Parameter Large Vision Model
- TechTimes: Z.ai Launches GLM-4.5: China's Most Advanced Open-Source AI Model
- AI Wiki: Z.ai
- HKEX prospectus filings

## API Reference

### REST API Endpoints

#### Chat Completions (OpenAI-Compatible)

```bash
curl https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{
    "model": "glm-5",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Explain the GLM architecture."}
    ],
    "temperature": 0.7,
    "max_tokens": 4096
  }'
```

#### Streaming Completions

```bash
curl https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{
    "model": "glm-4.5",
    "messages": [{"role": "user", "content": "Write a poem."}],
    "stream": true
  }'
```

#### Vision-Language (GLM-4.5V)

```bash
curl https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{
    "model": "glm-4.5v",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
      ]
    }]
  }'
```

#### Text-to-Video (Ying API)

```bash
curl https://open.bigmodel.cn/api/paas/v4/videos/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{
    "model": "cogvideox",
    "prompt": "A serene lake at sunset with mountains in the background",
    "size": "720p"
  }'
```

#### Embeddings

```bash
curl https://open.bigmodel.cn/api/paas/v4/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{
    "model": "embedding-3",
    "input": "Hello, world!"
  }'
```

### Authentication

Z.ai uses a unique JWT-based authentication system:

```python
import jwt
import time

def get_zhipu_token(api_key, api_secret):
    timestamp = int(time.time())
    payload = {
        "api_key": api_key,
        "exp": timestamp + 3600,
        "timestamp": timestamp
    }
    return jwt.encode(payload, api_secret, algorithm="HS256")
```

Or use the official ZhipuAI SDK which handles token generation automatically.

### Request Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | — | `glm-5`, `glm-5-turbo`, `glm-5.1`, `glm-4.5`, `glm-4.5v`, `glm-4-plus` |
| `messages` | array | — | Array of message objects |
| `max_tokens` | integer | — | Maximum tokens to generate |
| `temperature` | float | 0.95 | Sampling temperature (0.0–1.0) |
| `top_p` | float | 0.7 | Nucleus sampling threshold |
| `stream` | boolean | false | Enable streaming responses |
| `tools` | array | — | Function definitions for tool use |
| `response_format` | object | — | JSON output mode |
| `request_id` | string | — | Custom request identifier for tracking |

## Python SDK

### Installation

```bash
pip install zhipuai
# or use OpenAI SDK (Z.ai is OpenAI-compatible)
pip install openai
```

### Using Official SDK

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

# Standard chat completion
response = client.chat.completions.create(
    model="glm-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the GLM model family?"}
    ],
    max_tokens=2048
)
print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="glm-4.5",
    messages=[{"role": "user", "content": "Tell me a story."}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Using OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    api_key="zhipu-api-key",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

response = client.chat.completions.create(
    model="glm-5",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=1024
)
```

### Tool Use

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Search the company database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "limit": {"type": "integer", "description": "Max results"}
                },
                "required": ["query"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="glm-5",
    messages=[{"role": "user", "content": "Find all Q3 revenue reports."}],
    tools=tools,
    tool_choice="auto"
)
```

### Vision-Language

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

response = client.chat.completions.create(
    model="glm-4.5v",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What objects are in this image?"},
            {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg"}}
        ]
    }]
)
```

### AutoGLM Agent

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

# Create an AutoGLM agent session
agent = client.auto_glm.create(
    model="glm-5.1",
    instruction="You are a coding assistant that can browse files and make edits.",
    tools=["file_browser", "code_editor", "terminal"]
)

# Execute a multi-step task
result = agent.execute(
    task="Find all Python files with TODO comments and list them.",
    max_steps=20
)
```

## Rate Limits and Quotas

### Default Rate Limits

| Model | Requests per Minute | Tokens per Minute | Concurrent Requests |
|-------|-------------------|------------------|--------------------|
| **GLM-5** | 500 | 5M | 100 |
| **GLM-5 Turbo** | 1,000 | 10M | 200 |
| **GLM-5.1** | 500 | 5M | 100 |
| **GLM-4.5** | 1,000 | 10M | 200 |
| **GLM-4.5V** | 300 | 2M | 50 |

### Rate Limit Headers

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit` | Maximum requests per minute |
| `X-RateLimit-Remaining` | Remaining requests |
| `X-RateLimit-Reset` | Seconds until reset |
| `X-RateLimit-Tokens-Remaining` | Remaining token quota |

### Increasing Limits

- Contact enterprise@zhipuai.cn for enterprise limit increases
- Committed spend agreements guarantee higher throughput
- Dedicated endpoints available for high-volume customers
- Auto-scaling for verified enterprise accounts

## Enterprise SLAs

### Service Level Agreements

| Tier | Uptime SLA | Response Time | Support | Price |
|------|-----------|---------------|---------|-------|
| **Standard** | 99.5% | < 5s p95 | Email | Pay-as-you-go |
| **Business** | 99.9% | < 2s p95 | Email + WeChat | +20% |
| **Enterprise** | 99.95% | < 1s p95 | Dedicated CSM | Custom |
| **Government** | 99.99% | < 500ms p99 | 24/7 direct | Custom |

### SLA Credits

| Monthly Uptime | Credit |
|---------------|--------|
| 99.0% – 99.5% | 10% of monthly spend |
| 95.0% – 99.0% | 25% of monthly spend |
| < 95.0% | 50% of monthly spend |

### Enterprise Features

- **Dedicated endpoints**: Isolated infrastructure
- **Private deployment**: On-premises GLM deployment
- **Custom models**: Fine-tuned on proprietary data
- **VPC peering**: Direct private connectivity
- **Audit logging**: Complete request/response audit
- **Custom retention**: Configurable data policies
- **China compliance**: Full compliance with Chinese regulations

## Compliance and Data Privacy

### Regulatory Compliance

| Framework | Status | Details |
|-----------|--------|---------|
| **China PIPL** | ✅ Compliant | Personal Information Protection Law |
| **China DSL** | ✅ Compliant | Data Security Law |
| **China CSL** | ✅ Compliant | Cybersecurity Law |
| **China GenAI Regulations** | ✅ Compliant | Generative AI Management Measures |
| **ISO 27001** | In progress | Information security management |
| **SOC 2 Type II** | Planned | Trust services criteria |
| **GDPR** | Partial | EU data processing addendum available |
| **HKEX Listing Compliance** | ✅ Compliant | Listed on Hong Kong Stock Exchange |

### Data Processing

- **API data**: Not used for model training by default
- **Data retention**: 30 days for API logs (configurable)
- **Data residency**: China mainland infrastructure
- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Data deletion**: Available upon request within 7 days
- **Government review**: Content generation subject to Chinese AI content regulations

## Data Residency

### Infrastructure Locations

| Region | Location | Available For |
|--------|----------|---------------|
| **China (Beijing)** | Beijing data center | All customers |
| **China (Shanghai)** | Shanghai data center | All customers |
| **China (Shenzhen)** | Shenzhen data center | All customers |
| **China (Hangzhou)** | Hangzhou data center | All customers |
| **Southeast Asia** | Planned 2026 | Enterprise customers |

### Data Sovereignty

- All data processed and stored within China mainland
- Full compliance with China data localization laws
- No cross-border data transfer without regulatory approval
- Enterprise customers can request dedicated regional endpoints
- Government contracts require full domestic data processing

## Fine-tuning and Custom Models

### Fine-tuning API

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

# Upload training data
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Create fine-tuning job
job = client.fine_tuning.jobs.create(
    model="glm-4.5",
    training_file=file.id,
    hyperparameters={
        "n_epochs": 3,
        "learning_rate": 1e-5,
        "batch_size": 16
    }
)
```

### Fine-tuning Pricing

| Model | Training (per 1M tokens) | Inference Premium |
|-------|-------------------------|-------------------|
| **GLM-4.5** | ¥3.00 (~$0.42) | +30% over base |
| **GLM-5** | ¥15.00 (~$2.10) | +50% over base |
| **GLM-5 Turbo** | ¥8.00 (~$1.10) | +40% over base |

### Supported Techniques

- **Supervised fine-tuning (SFT)**: Full parameter and LoRA
- **RLHF**: Via enterprise program
- **DPO**: Direct preference optimization
- **Domain adaptation**: Industry-specific fine-tuning
- **Chinese language optimization**: Enhanced Chinese performance
- **Custom vocabularies**: Domain-specific token additions

## Competitor Comparison

### Feature Comparison

| Feature | GLM-5 | Qwen Max | DeepSeek V4 Pro | Kimi | MiniMax |
|---------|-------|----------|-----------------|------|---------|
| **Input Price** | ¥3.00/1K | ¥0.70/1K | ¥3.14/1K | ¥0.50/1K | ¥1.00/1K |
| **Output Price** | ¥12.00/1K | ¥1.40/1K | ¥6.28/1K | ¥2.00/1K | ¥5.00/1K |
| **Context** | 200K | 200K | 1M | 2M | 200K |
| **Parameters** | 744B MoE | — | 1.6T MoE | — | — |
| **Open Source** | ❌ | ✅ Apache | ✅ MIT | ❌ | ❌ |
| **Vision** | ✅ (GLM-4.5V) | ✅ | ❌ | ✅ | ✅ |
| **Voice** | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Video** | ✅ (Ying) | ❌ | ❌ | ❌ | ✅ |
| **Agents** | ✅ (AutoGLM) | ✅ | ✅ | ✅ | ✅ |
| **Domestic Chips** | ✅ Ascend | ✅ | ✅ | ✅ | ✅ |

### Market Position Among Chinese Providers

| Provider | Market Rank | Key Strength | IPO Status |
|----------|------------|-------------|------------|
| **Baidu (ERNIE)** | #1 | Ecosystem integration | Public |
| **Alibaba (Qwen)** | #2 | Cloud + open-source | Public |
| **Z.ai (Zhipu)** | #3 | Platform + agents | **Public (HKEX)** |
| **DeepSeek** | #4 | Coding + pricing | Private |
| **Moonshot (Kimi)** | #5 | Long context | Private |
| **MiniMax** | #6 | Voice + multimodal | Private |

### When to Choose Z.ai

- **Chinese enterprise market**: Full regulatory compliance
- **Hardware independence**: Runs on Huawei Ascend, Cambricon
- **Agent workflows**: AutoGLM platform for autonomous agents
- **Multimodal**: Unified text, vision, voice, video
- **IPO transparency**: Public company with financial disclosure
- **Government contracts**: Approved for government use

## Case Studies

### Case Study 1: Chinese Financial Institution

**Challenge**: Deploy AI assistant for compliance and risk analysis with full regulatory compliance.

**Solution**: Deployed GLM-5 with custom fine-tuning for financial domain on domestic hardware.

**Results**:
- Full compliance with Chinese financial regulations
- 70% reduction in compliance review time
- Running on Huawei Ascend — no NVIDIA dependency
- $2.10/1K tokens vs. $5.00+ for foreign providers

### Case Study 2: E-Commerce Platform

**Challenge**: Build autonomous shopping assistant across multiple apps.

**Solution**: Deployed AutoGLM 2.0 for cross-app task completion.

**Results**:
- Cross-app ordering using shopping history
- Voice command interaction for accessibility
- 40% increase in customer engagement
- 25% reduction in customer service costs

### Case Study 3: Academic Research Institution

**Challenge**: Process Chinese academic literature with domain-specific understanding.

**Solution**: Fine-tuned GLM-4.5 on AMiner academic corpus.

**Results**:
- 90% accuracy on information extraction
- Integration with AMiner researcher network
- 5× lower costs than foreign providers
- Open-source GLM-4.5 base for research transparency

## Ecosystem and Partnerships

### Cloud Platform Integrations

| Platform | Integration Type | Models Available |
|----------|-----------------|-----------------|
| **Huawei Cloud** | Native | GLM-5, GLM-4.5 (Ascend optimized) |
| **Alibaba Cloud** | Native | GLM-5, GLM-4.5 |
| **Tencent Cloud** | Native | GLM-5, GLM-4.5 |
| **Baidu Cloud** | API | GLM-5 |
| **China Telecom** | Native | GLM-5, GLM-4.5 |
| **Hugging Face** | Open weights | GLM-4.5, GLM-4.5V |

### Strategic Partnerships

| Partner | Partnership Type | Details |
|---------|-----------------|---------|
| **Huawei** | Hardware optimization | GLM on Ascend chips |
| **Cambricon** | Chip optimization | FP8/Int4 quantization |
| **Moore Threads** | GPU support | Native FP8 support |
| **Prosperity7 Ventures** | Investment | $400M Series C |
| **AMiner** | Data integration | Academic knowledge graph |

### Framework Support

- **LangChain**: Full support via `ChatZhipuAI`
- **LlamaIndex**: OpenAI-compatible wrapper
- **LiteLLM**: Unified API proxy
- **AutoGen**: Multi-agent support
- **CrewAI**: Agent orchestration
- **Haystack**: Component integration

## Research Publications

### Key Papers

1. **"GLM: General Language Model Pretraining with Autoregressive Blank Infilling"** (ACL 2022)
   - Du et al., foundational paper for GLM architecture
   - Introduced autoregressive blank infilling objective
   - Established unified pre-training framework

2. **"GLM-130B: An Open Bilingual Pre-trained Model"** (ICLR 2023)
   - First open 100B+ Chinese-English bilingual model
   - Demonstrated competitive performance with closed models
   - Published methodology for large-scale training

3. **"CogVLM: Visual Expert for Pretrained Language Models"** (2024)
   - Vision-language model architecture
   - Visual expert module for image understanding
   - Foundation for GLM-4.5V

4. **"CogVideoX: Text-to-Video Generation with 3D Causal VAE"** (2024)
   - Open-source text-to-video model
   - 3D causal variational autoencoder architecture
   - Apache 2.0 licensed

5. **"AutoGLM: Autonomous Mobile Agent Platform"** (2025)
   - Cross-app autonomous agent capabilities
   - Real-world task execution framework
   - Voice command interaction system

## Prompt Engineering Guide

### Best Practices

1. **Use GLM-5 Turbo for tool-heavy workflows** — Optimized for function calling
2. **Use GLM-4.5 for cost-sensitive tasks** — MIT licensed, open weights
3. **Use GLM-5.1 for coding agents** — Extended autonomous execution
4. **Use GLM-4.5V for vision tasks** — 106B visual understanding model
5. **Set temperature 0.1-0.3 for structured output** — More deterministic results
6. **Use Chinese system prompts for Chinese tasks** — Better Chinese comprehension
7. **Leverage 200K context for document analysis** — Full document processing

### Prompt Templates

```python
# Chinese customer service template
CUSTOMER_SERVICE_PROMPT = """你是一个专业的客户服务助手。请用中文回答客户的问题。
要求：
1. 语气友好、专业
2. 回答准确、简洁
3. 如遇不确定信息，请说明

客户问题：{question}"""

# Code analysis template (GLM-5.1)
CODE_ANALYSIS_PROMPT = """You are an autonomous coding agent. Analyze the following codebase:
1. Identify architecture patterns
2. Find potential bugs
3. Suggest optimizations
4. Generate test cases

You may use available tools to explore the codebase.

Codebase root: {path}"""

# Document analysis template (200K context)
DOCUMENT_ANALYSIS_PROMPT = """Analyze the following document and extract:
1. Key findings and conclusions
2. Supporting evidence
3. Methodology used
4. Limitations and caveats
5. Recommendations

Document:
{document}"""
```

### Multi-Turn Conversations

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="***")

messages = [
    {"role": "system", "content": "You are a coding tutor."},
    {"role": "user", "content": "What is a binary search tree?"},
    {"role": "assistant", "content": "A binary search tree is..."},
    {"role": "user", "content": "Can you show me an implementation?"}
]

response = client.chat.completions.create(
    model="glm-5",
    messages=messages,
    max_tokens=2048
)
```

## Security Features

### API Security

| Feature | Description |
|---------|-------------|
| **JWT Authentication** | Token-based auth with expiration |
| **API Key Management** | Programmatic key rotation |
| **IP Allowlisting** | Restrict access to specific IPs |
| **Usage Alerts** | Configurable spending alerts |
| **Audit Logging** | Complete request logging |
| **Request Signing** | HMAC-based request verification |

### Model Security

| Feature | Status |
|---------|--------|
| **Content Filtering** | Built-in safety per Chinese regulations |
| **Prompt Injection Protection** | System prompt enforcement |
| **PII Detection** | Automatic PII scanning |
| **Government Compliance** | Content generation compliance |
| **Output Validation** | Schema enforcement |

### Enterprise Security

- **China PIPL compliance**: Full personal data protection
- **Penetration testing**: Annual third-party audits
- **Government certification**: Approved for government contracts
- **Incident response**: 24-hour notification SLA
- **Data processing agreement**: Available for enterprise
- **Right to audit**: Enterprise security audit rights
- **On-premises deployment**: Full air-gapped deployment option