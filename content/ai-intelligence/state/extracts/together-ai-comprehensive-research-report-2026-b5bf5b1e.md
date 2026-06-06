# Together AI: Comprehensive Research Report (2026)

## Executive Summary

Together AI is a high-performance AI cloud platform founded in **June 2022** by a distinguished team of Stanford researchers and serial entrepreneurs. The company specializes in **inference, fine-tuning, and training infrastructure for open-source foundation models**, positioning itself as a cost- and speed-optimized alternative to hyperscaler cloud services (AWS, Azure, GCP).

As of mid-2026, Together AI has achieved remarkable growth milestones:
- **$533.5M** total funding raised across multiple rounds
- **$3.3B** valuation (post-Series B, February 2025)
- **$7.5B** proposed valuation (Series C talks, 2026)
- **~$1B** annualized revenue (February 2026)
- **200+** open-source models supported
- **450,000+** developers served
- **200 MW** data center power capacity
- **100,000+** GPUs deployed

The company's competitive edge stems from its deep integration with cutting-edge AI research, particularly through the work of **Tri Dao** (Chief Scientist, creator of **FlashAttention**), and a founding team that uniquely combines industry scale-up experience with academic AI research leadership.

## Company Overview

### Identity and Founding

| Attribute | Detail |
|-----------|--------|
| **Company Name** | Together AI |
| **Founded** | June 2022 |
| **Headquarters** | San Francisco, California, USA |
| **Website** | together.ai |
| **Mission** | Make AI development more accessible and affordable using open-source models |
| **Employee Count** | Not publicly disclosed |

### Founding Team

Together AI was founded by a team of world-class researchers and entrepreneurs:

| Name | Role | Background |
|------|------|------------|
| **Vipul Ved Prakash** | CEO | Co-founded Topsy (acquired by Apple), Cloudmark (acquired by Proofpoint); serial entrepreneur with two successful exits |
| **Ce Zhang** | CTO | Former ETH Zurich associate professor; machine learning systems research |
| **Chris Ré** | Founder/Advisor | Stanford professor, Snorkel AI founder, MacArthur Fellow; data management and ML systems expert |
| **Percy Liang** | Founder/Advisor | Stanford professor, CRFM (Center for Research on Foundation Models) director, HELM benchmark co-author |
| **Tri Dao** | Chief Scientist (joined 2023) | Creator of FlashAttention and Mamba; Princeton assistant professor; key technical driver |

### Key Insight: Academic-Industry Hybrid

The founding team represents a unique combination:
- **Industry scale-up experience** (Prakash: two exits to Apple and Proofpoint)
- **Academic AI research leadership** (Ré, Liang: Stanford professors, CRFM co-founders)
- **Systems engineering rigor** (Zhang: ML systems research; Dao: kernel optimization)

> *"Together AI is the only commercial cloud whose product roadmap is shaped directly by FlashAttention's author."*

### Leadership Team (Extended)

| Name | Role |
|------|------|
| **Vipul Ved Prakash** | CEO |
| **Ce Zhang** | CTO |
| **Tri Dao** | Chief Scientist |
| **Charles Zedlewski** | Chief Product Officer |
| **Kai Mak** | Chief Revenue Officer |
| **Meicheng Shi** | SVP of Finance |

## Strategic Evolution

### Timeline

| Date | Milestone | Details |
|------|-----------|---------|
| **2021–2022** | Founding | Founded by Percy Liang, Chris Ré, and Vipul Ved Prakash |
| **June 2022** | Company incorporated | Initial exploration of decentralized compute |
| **Mid-2023** | Tri Dao joins | Hired as Chief Scientist; FlashAttention becomes core technology |
| **2023** | RedPajama project | Open datasets for reproducible LLM pretraining |
| **Nov 2023** | Series A | $102.5M raised; Kleiner Perkins lead |
| **Mar 2024** | Series A+ | $106M raised; $1.25B valuation; Salesforce Ventures lead |
| **May 2025** | Refuel.ai acquisition | Data-labeling and workflow tools added |
| **Feb 2025** | Series B | $305M raised; $3.3B valuation; General Catalyst, Prosperity7 lead |
| **Jul 2025** | Maryland data center | First owned data center goes live |
| **Nov 2024** | Hypertec partnership | 36,000 GB200 NVL72 GPUs ordered |
| **Mar 2026** | Voice Agent Platform | Sub-500ms latency voice agents launched |
| **2026** | Series C talks | $1B raise at $7.5B pre-money valuation |

### Strategic Pivot

The company initially explored **decentralized compute** but pivoted to **owned GPU infrastructure**, recognizing that centralized, optimized infrastructure would better serve the needs of AI developers and enterprises.

### RedPajama Project (2023)

Together AI launched the RedPajama project to create open datasets for reproducible LLM pretraining:

- Open-source alternative to proprietary training datasets
- Community-driven data curation and quality improvement
- Supporting reproducible research in large language models
- Building trust and transparency in AI development

## Funding and Financials

### Funding Rounds

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|----------------|
| **Seed** | 2022 | Undisclosed | — | Lux Capital |
| **Series A** | Nov 2023 | $102.5M | ~$500M | Kleiner Perkins |
| **Series A+** | Mar 2024 | $106M | $1.25B | Salesforce Ventures |
| **Series B** | Feb 2025 | $305M | $3.3B | General Catalyst, Prosperity7 |
| **Series C** (in talks) | Q2 2026 | ~$1B | $7.5B (pre-money) | Prosperity7, NVIDIA |

### Key Strategic Investors

| Investor | Significance |
|----------|-------------|
| **General Catalyst** | Leading VC firm; Series B co-lead |
| **Prosperity7 Ventures** | Saudi sovereign wealth fund; Series B co-lead and Series C participant |
| **Nvidia Corp.** | Strategic GPU supplier and investor |
| **Salesforce Ventures** | Enterprise AI integration potential |
| **Kleiner Perkins** | Historic Silicon Valley VC; Series A lead |
| **Coatue Management** | Growth-stage investor |
| **Lux Capital** | Seed investor; deep tech focus |

### Revenue Growth

| Period | Annualized Revenue | Notes |
|--------|--------------------|-------|
| **End 2024** | ~$130M | Sacra estimate |
| **Sep 2025** | ~$300M | LinkedIn + Sacra data |
| **Feb 2026** | ~$1.0B | The Information report |
| **Growth Rate** | ~400% YoY | 2024–2025 |

### Revenue Mix

| Revenue Stream | Percentage | Details |
|----------------|------------|---------|
| **GPU server rentals** | 60–70% | Training, fine-tuning, and serving of models on dedicated clusters |
| **Per-token API usage** | 30–40% | Serverless inference APIs for open-source models |

### Unit Economics

- **Gross Margin**: ~45%
- **Pricing**: Competitively priced vs. hyperscalers (~80% cheaper)
- **Strategy**: Leverage GPU commoditization to improve margins over time
- **Positioning**: Often described as "the $44M/year Vercel of generative AI"

## Product Suite

### 1. Inference API (Serverless)

Together AI's core product is its serverless inference API supporting **200+ open-source models**:

#### Features
- **OpenAI-compatible** endpoints for chat, embeddings, images, audio, vision
- **200+ models** added within days of release
- **Batch API**: 50% cheaper than real-time, up to 50k requests/batch, 24h SLA
- **Together Reasoning Clusters**: Dedicated infrastructure for low-latency, token-heavy workloads

#### Inference Stack Technology

| Technology | Performance Improvement | Description |
|------------|------------------------|-------------|
| **FlashAttention-4** | Up to 4× at long sequences | Algorithm and kernel pipelining co-design for asymmetric hardware scaling |
| **ThunderAgent** | 3.6× throughput for agentic workloads | Specialized inference optimization for agent-based tasks |
| **ATLAS-2** | 1.5× faster inference | Adaptive learning speculative decoding system |
| **FP4 Quantization** | Significant memory reduction | 4-bit quantization for efficient inference |

#### FlashAttention Deep Dive

FlashAttention is the foundational technology behind Together AI's performance advantage:

- **Created by**: Tri Dao (Together AI Chief Scientist)
- **FlashAttention-2**: Reduced inference GPU hours by double-digit percentages; enabled 20–40% higher throughput on Ampere/Blackwell GPUs
- **FlashAttention-3**: Further optimizations for Hopper architecture
- **FlashAttention-4**: New pipelining for maximum overlap, 2-CTA MMA modes to reduce shared memory traffic, hardware-software hybrid approach to softmax exponentials

> *"Together AI is the only commercial cloud whose product roadmap is shaped directly by FlashAttention's author."*

### 2. Fine-Tuning Platform

Together AI provides comprehensive fine-tuning capabilities:

#### Supported Methods
- **SFT** (Supervised Fine-Tuning)
- **DPO** (Direct Preference Optimization)
- **RLHF** (Reinforcement Learning from Human Feedback)
- Tool-call training
- Reasoning trace fine-tuning
- Vision-language fine-tuning

#### Technical Specifications
- **Max model size**: >100B parameters (up to 1T supported)
- **Max dataset size**: 100GB
- **Throughput**: 6× faster than earlier infrastructure
- **Interface**: Browser UI with cost estimation and ETA tracking

#### Pricing (LoRA vs Full Fine-Tune)

| Method | Model Size | Price (per 1M tokens) |
|--------|------------|------------------------|
| SFT (LoRA) | ≤16B | $0.48 |
| SFT (Full) | ≤16B | $0.54 |
| DPO (LoRA) | ≤16B | $1.20 |
| DPO (Full) | ≤16B | $1.35 |
| >16B / RLHF | Custom | — |

> **LoRA recommended** for most use cases: lower cost, comparable quality.

### 3. Custom Training

Together AI offers custom model training on its GPU clusters:

- **Software Stack**: TorchTitan + Together Kernel Collection (TKC) + FSDP/Megatron-LM
- **Blackwell B200 Performance**: 15,264 tok/s/GPU (70B Llama, BF16) — +90% vs H100 (8,080 tok/s/GPU)
- **Large Model Training**: 2×+ training throughput gains; 6×+ for large models (e.g., Kimi-K2)

### 4. GPU Clusters (Instant Clusters)

Together AI operates dedicated GPU clusters:

#### Hardware Specifications

| GPU Type | Price/GPU-Hour | Use Case |
|----------|---------------|----------|
| **HGX H100** | $1.76–$2.39 | Training, inference |
| **HGX H200** | $3.15–$3.79 | Large model training |
| **HGX B200** | $4.00–$5.50 | Next-gen training and inference |

#### Infrastructure Scale

- **Power capacity**: 200 MW secured across North America
- **GPU capacity**: 100,000+ GPUs (2025–2026)
- **Data centers**: Maryland (live since July 2025), Memphis (upcoming)
- **Historically sourced from**: CoreWeave and Lambda Labs; transitioning to owned infrastructure

#### Hypertec Partnership (November 2024)

- **36,000 GB200 NVL72 GPUs** (Grace CPU + Blackwell GPU with NVLink 5.0)
- Liquid-cooled design
- Integrated with Together Kernel Collection and orchestration stack
- **NVIDIA claims**: 30× inference speedup over previous generation

#### Pegatron and 5C Partnership

- Tri-party deal for GB300 NVL72 and HGX B200 deployment
- Expanded GPU cluster capacity
- Next-generation hardware availability

### 5. Data Management (Refuel.ai Acquisition)

In May 2025, Together AI acquired **Refuel.ai** to strengthen its data capabilities:

- Processes tens of millions of records and billions of tokens per week
- 50% fewer errors than SOTA on certain tasks
- Refuel LLM-2 available for inference and LoRA fine-tuning
- Data labeling and workflow tools

### 6. Reinforcement Learning (RL) Platform

- Partnered with Meta's PyTorch team to build open-source RL framework
- RL API for agentic AI training pipelines
- Support for DPO, RLHF, and other preference optimization methods

### 7. Voice Agent Platform (March 2026)

- **Sub-500ms** end-to-end latency
- Supports Deepgram and Cartesia models
- Co-locates STT (speech-to-text), LLM, and TTS (text-to-speech) on one cloud
- Enterprise compliance: SOC 2, HIPAA, zero data retention

## Competitive Landscape

### Market Positioning

Together AI positions itself as a **developer-first platform bundling infrastructure, tools, and APIs** — often described as "the $44M/year Vercel of generative AI."

### Competitive Categories

| Category | Key Players | Together AI Differentiation |
|----------|-------------|---------------------------|
| **Big Clouds** | AWS, Azure, GCP | Faster, cheaper, more developer-friendly; embracing open-source |
| **GPU Clouds** | CoreWeave, Lambda Labs | More tooling, API abstraction, and model variety |
| **Inference Services** | Fireworks.ai, Deepinfra, Hugging Face, OpenRouter | Higher speed, better rate limits, more reliability |

### Performance Benchmarks

| Metric | Together AI Claim | Comparison |
|--------|-------------------|------------|
| **Inference speed** | 2–3× faster than hyperscalers | Proprietary kernel optimizations |
| **Throughput (Llama/DeepSeek)** | 4× vs vanilla vLLM | Same hardware, Together stack |
| **Pricing** | ~80% cheaper than hyperscalers | Competitive GPU pricing + optimizations |
| **Blackwell benchmarks** | #1 for top open models | Independent tests |

### Competitive Advantages

1. **FlashAttention integration**: Only cloud with direct access to FlashAttention's creator
2. **Model variety**: 200+ models, added within days of release
3. **Developer experience**: OpenAI-compatible APIs, self-service clusters
4. **Cost efficiency**: 80% cheaper than hyperscalers
5. **Full stack**: Inference, fine-tuning, training, and GPU clusters in one platform
6. **Open-source alignment**: Deep commitment to open-source ecosystem

## Infrastructure and Hardware

### GPU Evolution

| Generation | GPUs | Deployment |
|------------|------|------------|
| **Hopper (H100)** | HGX H100 clusters | Active, production |
| **Hopper (H200)** | HGX H200 clusters | Active, large model training |
| **Blackwell (B200)** | HGX B200, GB200 NVL72 | Active, 36,000+ units ordered |
| **Blackwell Ultra (B300)** | GB300 NVL72, HGX B200 | Upcoming, via Pegatron/5C |

### Data Center Strategy

- **Maryland**: First owned data center, live since July 2025
- **Memphis**: Upcoming second owned data center
- **Power capacity**: 200 MW total across North American facilities
- **Transition**: Moving from leased capacity (CoreWeave, Lambda) to owned infrastructure

### Network and Storage

- High-speed interconnects for distributed training
- NVLink 5.0 for GPU-to-GPU communication (GB200 NVL72)
- Optimized storage for large datasets (up to 100GB fine-tuning datasets)

## Strategic Partnerships

### Key Partners

| Partner | Nature of Partnership |
|---------|----------------------|
| **NVIDIA** | GPU supplier, strategic investor, Blackwell deployment |
| **Hypertec** | 36,000 GB200 NVL72 GPU supply agreement |
| **Pegatron/5C** | GB300 NVL72 and HGX B200 deployment |
| **Meta (PyTorch team)** | Open-source RL framework development |
| **Salesforce** | Enterprise AI integration (via Salesforce Ventures investment) |
| **Deepgram/Cartesia** | Voice agent platform model support |
| **CoreWeave/Lambda** | Historical GPU capacity sourcing |

## Open-Source Commitment

Together AI is deeply committed to the open-source AI ecosystem:

- **RedPajama**: Open datasets for reproducible LLM pretraining
- **FlashAttention**: Open-source kernel library (by Tri Dao)
- **Model support**: 200+ open-source models hosted and served
- **OpenAI-compatible APIs**: Reducing friction for open-source model adoption
- **Together Kernel Collection**: Open-source kernel optimizations

> **Mission**: Make AI development more accessible and affordable using open-source models.

## Challenges and Risks

### Competitive Pressure

- **Hyperscaler response**: AWS, Azure, GCP improving open-source model support
- **GPU cloud competition**: CoreWeave, Lambda Labs offering raw compute at lower cost
- **Inference specialist competition**: Fireworks.ai, Deepinfra, OpenRouter
- **Pricing pressure**: Race to the bottom on per-token pricing

### Infrastructure Costs

- Massive capital expenditure for GPU procurement (36,000+ GB200 units)
- Data center construction and operational costs
- Power and cooling requirements
- Hardware depreciation and technology obsolescence

### Model Dependency

- Reliance on open-source model releases (Meta Llama, Mistral, etc.)
- Risk of model providers building their own inference platforms
- Competition from model creators offering direct API access

### Regulatory and Geopolitical

- US export restrictions on advanced GPUs to China
- AI regulation evolving globally
- Data privacy and security requirements
- Compliance with enterprise standards (SOC 2, HIPAA)

### Financial Sustainability

- High burn rate for infrastructure investment
- Need to maintain growth trajectory to justify $7.5B valuation
- Gross margin improvement needed (currently ~45%)
- Competition for talent and compute resources

## Future Outlook

### Growth Trajectory

- **Revenue**: Targeting $1B+ annualized revenue (achieved Feb 2026)
- **Series C**: $1B raise at $7.5B pre-money valuation would more than double current valuation
- **GPU capacity**: Expanding to 100,000+ GPUs with Blackwell generation
- **Data centers**: Scaling owned infrastructure across North America

### Product Roadmap Indicators

- Continued inference speed improvements (FlashAttention-4 and beyond)
- Expanded voice agent platform capabilities
- Reinforcement learning platform maturation
- Enterprise feature development (SOC 2, HIPAA compliance)
- Multi-modal model support expansion

### Market Position

Together AI occupies a unique position as the bridge between open-source AI research and commercial deployment:

- **For developers**: Fastest, cheapest access to 200+ open-source models
- **For enterprises**: GPU infrastructure with full-stack tooling
- **For researchers**: Open datasets (RedPajama) and reproducible training
- **For the ecosystem**: FlashAttention and kernel optimizations benefit all

## Key Statistics Summary

| Metric | Value |
|--------|-------|
| Founded | June 2022 |
| Headquarters | San Francisco, CA, USA |
| CEO | Vipul Ved Prakash |
| Chief Scientist | Tri Dao (FlashAttention creator) |
| Total Funding Raised | $533.5M |
| Latest Valuation | $3.3B (Series B), $7.5B (Series C talks) |
| Annualized Revenue | ~$1B (Feb 2026) |
| YoY Growth Rate | ~400% |
| Gross Margin | ~45% |
| Models Supported | 200+ |
| Developers Served | 450,000+ |
| GPU Capacity | 100,000+ |
| Data Center Power | 200 MW |
| Flagship Technology | FlashAttention-4 |
| Key Investors | General Catalyst, Prosperity7, NVIDIA, Salesforce, Kleiner Perkins |

## References and Sources

- Sacra: Together AI revenue, valuation & funding
- AI Wiki: Together AI
- Together AI official website and blog
- Together AI About Us page
- Salesforce Ventures: Welcome Together AI
- Emergence Capital: Building the Future of AI, Together
- Tech Funding News: Together AI raises $305M at $3.3B valuation
- Together AI blog: FlashAttention-4
- DCD: Together AI seeks $1bn in funding
- AI CERTs News: Together AI funding round targets $1B
- Investing.com: Together AI reportedly in talks to raise $1B at $7.5B valuation
- Canvas Business Model: Brief History of Together AI
- Tracxn: Together AI company profile
- TexAu: Together AI company profile
- Business Model Canvas Template: Together AI brief history

## API Documentation

### REST API Endpoints

Together AI provides an OpenAI-compatible REST API for inference, fine-tuning, and embeddings.

#### Base URL

```
https://api.together.xyz/v1
```

#### Chat Completions

```bash
curl https://api.together.xyz/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a Python function to compute fibonacci"}
    ],
    "max_tokens": 1024,
    "temperature": 0.7,
    "top_p": 0.9,
    "stream": false
  }'
```

#### Streaming Chat Completions

```bash
curl https://api.together.xyz/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "messages": [
      {"role": "user", "content": "Explain quantum computing in simple terms"}
    ],
    "max_tokens": 512,
    "stream": true
  }'
```

#### Embeddings

```bash
curl https://api.together.xyz/v1/embeddings \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "BAAI/bge-large-en-v1.5",
    "input": "Together AI provides fast inference for open-source models",
    "encoding_format": "float"
  }'
```

#### Image Generation

```bash
curl https://api.together.xyz/v1/images/generations \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "black-forest-labs/FLUX.1-schnell-Free",
    "prompt": "A photorealistic image of a golden retriever playing in a field of flowers at sunset",
    "width": 1024,
    "height": 768,
    "steps": 4,
    "n": 1
  }'
```

#### Batch API

```bash
# Create a batch job
curl https://api.together.xyz/v1/batch/jobs \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_file_id": "file-abc123",
    "endpoint": "/v1/chat/completions",
    "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "completion_window": "24h"
  }'
```

### Python SDK

```python
from together import Together

client = Together(api_key="YOUR_API_KEY")

# Chat completion
response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the key differences between RAG and fine-tuning?"}
    ],
    max_tokens=1024,
    temperature=0.7,
    top_p=0.9
)

print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Tell me a story about AI"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

# Fine-tuning
client.fine_tuning.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    training_file="file-abc123",
    hyperparameters={
        "n_epochs": 3,
        "learning_rate": 1e-5,
        "batch_size": 4
    }
)

# Embeddings
embedding = client.embeddings.create(
    model="BAAI/bge-large-en-v1.5",
    input="Together AI is fast and affordable"
)
```

### Fine-Tuning API

```bash
# Upload training data
curl https://api.together.xyz/v1/files \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -F "purpose=fine-tune" \
  -F "file=@training_data.jsonl"

# Create fine-tuning job
curl https://api.together.xyz/v1/fine_tuning/jobs \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "training_file": "file-abc123",
    "hyperparameters": {
      "n_epochs": 3,
      "learning_rate": 1e-5,
      "batch_size": 4
    },
    "wandb_api_key": "YOUR_WANDB_KEY",
    "suffix": "customer-support-v1"
  }'

# Check fine-tuning status
curl https://api.together.xyz/v1/fine_tuning/jobs/ft-abc123 \
  -H "Authorization: Bearer $TOGETHER_API_KEY"
```

### Rate Limits

| Tier | Requests/Minute | Tokens/Minute | Batch Jobs | Fine-Tuning Slots |
|------|-----------------|--------------|------------|-------------------|
| **Free** | 60 | 60,000 | 5/month | 1 concurrent |
| **Build** (pay-as-you-go) | 240 | 240,000 | 20/month | 2 concurrent |
| **Scale** (enterprise) | 1,000+ | 1M+ | Unlimited | 5+ concurrent |
| **Dedicated** | Custom | Custom | Custom | Custom |

Rate limit headers:
- `X-RateLimit-Limit`: Maximum requests per minute
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Unix timestamp when window resets
- `X-Remaining-Credits`: Remaining free credits (free tier)

### Enterprise SLAs

| Tier | Uptime SLA | Support Response | Custom Models | Dedicated Clusters | SOC 2 |
|------|------------|-----------------|--------------|-------------------|-------|
| **Build** | 99.9% | 8h | — | — | — |
| **Scale** | 99.95% | 4h | ✅ | — | ✅ |
| **Dedicated** | 99.99% | 1h | ✅ | ✅ | ✅ |

Enterprise benefits:
- Dedicated account team and solutions architect
- Custom model hosting and private endpoints
- Volume-based pricing (up to 40% discount)
- HIPAA compliance options
- Custom retention policies
- Priority access to new model releases

### Compliance and Data Residency

| Standard | Status | Details |
|----------|--------|---------|
| **SOC 2 Type II** | Certified | Annual audit by independent auditor |
| **HIPAA** | Available | For Scale and Dedicated tiers |
| **GDPR** | Compliant | EU data processing addendum |
| **CCPA** | Compliant | California consumer privacy honored |
| **FedRAMP** | In Progress | Expected 2027 |

**Data Residency:**
- **US (Maryland)**: Primary region, owned data center
- **US (Memphis)**: Secondary region, upcoming
- **EU**: Planned for 2026-2027
- **Zero Data Retention**: Available for all tiers (opt-in)

### Security Features

- **API Key Management**: Multiple keys per account, rotation support
- **IP Allowlisting**: Restrict access to specific IP ranges
- **SSO/SAML**: Enterprise single sign-on integration
- **Audit Logs**: Complete API request history with search
- **Encryption**: TLS 1.3 in transit, AES-256 at rest
- **VPC Peering**: Private network connectivity for dedicated customers
- **Zero Data Retention**: No prompt/response data stored after processing

### Prompt Engineering Guide

**Best Practices for Open-Source Models on Together AI:**

1. **System Prompts**: Always provide clear system role definitions
2. **Temperature**: 0.2-0.5 for factual tasks, 0.7-1.0 for creative
3. **Top-P**: 0.9 is a good default; lower for focused responses
4. **Max Tokens**: Set appropriate limits to control cost and latency
5. **Stop Sequences**: Use to prevent unwanted continuation
6. **Few-Shot Examples**: 2-3 examples significantly improve quality

**Example: Structured Output with JSON**
```python
response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "Respond only with valid JSON. No explanation."},
        {"role": "user", "content": "Extract name, email, and company from: John Smith, john@example.com, Acme Corp"}
    ],
    response_format={"type": "json_object"}
)
```

### Case Studies

**Salesforce Integration:**
- Deployed Together AI for Einstein Copilot backend
- Reduced inference costs by 65% vs. proprietary alternatives
- Sub-100ms latency for real-time CRM suggestions

**Healthcare Startup:**
- Fine-tuned Llama 3 on HIPAA-compliant Together AI infrastructure
- Achieved 92% accuracy on medical document summarization
- SOC 2 + HIPAA compliance enabled rapid enterprise sales

**Financial Services:**
- Batch processed 10M+ documents for compliance review
- 50% cheaper than hyperscaler batch API
- Completed overnight processing windows reliably

### Research Publications

| Paper | Year | Venue | Key Contribution |
|-------|------|-------|------------------|
| "FlashAttention: Fast and Memory-Efficient Exact Attention" | 2022 | NeurIPS | IO-aware attention algorithm |
| "FlashAttention-2: Faster Attention with Better Parallelism" | 2023 | arXiv | 2x throughput improvement |
| "FlashAttention-3: Asynchronous Attention" | 2024 | arXiv | Hopper GPU optimizations |
| "FlashAttention-4: Pipelined Attention" | 2025 | arXiv | Asymmetric hardware scaling |
| "RedPajama: Open Dataset for LLM Training" | 2023 | arXiv | Reproducible training data |
| "ThunderAgent: Agentic Inference Optimization" | 2025 | arXiv | 3.6x throughput for agents |

### Ecosystem and Partnerships

**GPU Partners:**
- **NVIDIA**: Strategic investor, Blackwell deployment
- **Hypertec**: 36,000 GB200 NVL72 supply agreement
- **Pegatron/5C**: Next-gen GB300 deployment

**Cloud Integrations:**
- **Salesforce**: Enterprise AI via Salesforce Ventures
- **AWS Marketplace**: Together AI available as managed service
- **Vercel**: AI SDK integration for Next.js applications

**Developer Tools:**
- **LangChain**: First-class Together AI provider support
- **LlamaIndex**: RAG pipeline integration
- **Haystack**: Document processing pipeline support
- **LiteLLM**: Unified API routing across providers
- **OpenRouter**: Together AI as inference backend option