# LLM Provider Research Report: Moonshot AI (月之暗面)

> **Research Date:** June 2026
> **Scope:** Company overview, Kimi model family, capabilities, pricing, API, benchmarks, competitive positioning, recent developments

---

## 1. Company Overview & Backing

| Attribute | Detail |
|-----------|--------|
| **Legal Name** | Beijing Moonshot AI Technology Co., Ltd. (北京月之暗面科技有限公司) |
| **Trade Name** | Moonshot AI (月之暗面 / Yuè Zhī Ànmiàn) |
| **Founded** | March 2023 (3 years old as of 2026) |
| **Founders** | Yang Zhilin (CEO), Zhou Xinyu, Wu Yuxin — all Tsinghua University classmates |
| **Headquarters** | Beijing, China |
| **CEO** | Yang Zhilin |
| **Employees** | ~200 (2024); estimated 400–500+ (2026) |
| **Website** | [moonshot.ai](https://www.moonshot.ai/) |
| **Industry** | Artificial Intelligence — large language models (LLMs), AGI research |
| **Status** | Privately held; considered one of China's "Six AI Tigers" |
| **Key Products** | Kimi chatbot, Kimi K2 series, Mooncake serving platform, Muon optimizer |

Moonshot AI is one of China's fastest-growing AI startups, founded in March 2023 by Yang Zhilin, a Tsinghua University graduate with prior experience at Meta AI Research (FAIR) and Tsinghua's IIIS (Institute for Interdisciplinary Information Sciences). The company name is inspired by Pink Floyd's album *The Dark Side of the Moon*, released 50 years prior in 1973, which is Yang's favorite album.

### 1.1 Vision & Strategic Philosophy

Moonshot AI's stated goal is to build foundation models to achieve Artificial General Intelligence (AGI). Yang Zhilin has articulated three strategic milestones:

1. **Long context length** — enabling models to process and reason over extremely large inputs
2. **Multimodal world model** — integrating vision, audio, and text into unified representations
3. **Scalable general architecture** — capable of continuous self-improvement without human input

### 1.2 Funding & Valuation History

| Date | Round | Amount | Valuation | Lead Investor(s) | Notes |
|------|-------|--------|-----------|------------------|-------|
| Mar 2023 | Seed | ~$10M | — | — | Initial seed round |
| Apr 2023 | Series A | — | — | — | Early growth funding |
| Oct 2023 | — | $300M | $2.5B | Alibaba, Tencent, Meituan, HongShan | Major round to scale Kimi |
| Mar 2024 | Series B | ~$400M | ~$3B | Alibaba, Tencent, HongShan | Continued scaling |
| 2024 | — | ~$200M+ | — | Multiple investors | Growth capital for K2 development |
| 2025 | — | — | — | — | Post-K2 valuation growth |

Total disclosed funding exceeds **$1 billion**, making Moonshot AI one of the best-funded AI startups in China. The company competes with Zhipu AI (Z.ai), MiniMax, and other "Six AI Tigers" for market share.

---

## 2. Model Family: Kimi Series

### 2.1 Model Release Timeline

| Version | Release Date | Key Features | Architecture |
|---------|--------------|--------------|-------------|
| **Kimi (v1)** | Oct 2023 | First chatbot; supports up to 200K Chinese characters per conversation | Proprietary |
| **Kimi K1.5** | Jan 20, 2025 | Matches OpenAI o1 in math, coding, and multimodal reasoning | Proprietary |
| **Kimi K2** | Jul 11, 2025 | 1T-parameter MoE model, 32B active params; trained on 15.5T tokens; open-source under modified MIT license | MoE: 1T total / 32B active / 384 experts / 8 activated per token |
| **Kimi-K2-Instruct-0905** | Sep 9, 2025 | Doubled context window to 256K tokens; improved agentic coding performance | MoE 1T |
| **Kimi K2 Thinking** | Nov 6, 2025 | Advanced reasoning & agentic tasks; outperforms GPT-5 and Claude Sonnet 4.5 on benchmarks | MoE 1T + reasoning traces |
| **Kimi K2.5** | Jan 2026 | Multimodal upgrade with MoonViT (400M-parameter vision encoder); supports image/video processing; Agent Swarm v1 | MoE 1T + native multimodal |
| **Kimi K2.6** | Apr 21, 2026 | 12-hour runs, 300-agent swarms, full-stack generation, automatic context compression | MoE 1T + enhanced execution layer |

### 2.2 Kimi K2 Architecture Details

Kimi K2 represents Moonshot AI's flagship open-source model and one of the largest MoE models publicly available.

**Core Architecture:**
- **Total Parameters:** 1 trillion
- **Active Parameters per Request:** 32 billion
- **Total Layers:** 61
- **Number of Experts:** 384
- **Experts Activated per Token:** 8
- **Attention Mechanism:** Multi-Head Latent Attention (MLA)
- **Activation Function:** SwiGLU
- **Training Stabilization:** MuonClip-stabilized training
- **Training Tokens:** 15.5 trillion (mixed visual and textual)
- **Context Window:** 262,144 tokens (K2.6), up from 256K in K2.5
- **License:** Modified MIT License (requires attribution for products with >100M monthly users or >$20M monthly revenue)

**Training Optimizer — Muon:**
Moonshot AI developed the Muon optimizer in joint research with UCLA. Key properties:
- 2× faster than AdamW in training MoE LLMs
- Scalable to large models (tested on 16B params, 3B active configurations)
- Paper: "Muon is Scalable for LLM Training" (arXiv:2502.16982)
- Open-sourced on GitHub: [github.com/moonshotai/muon](https://github.com/moonshotai/muon)
- Hugging Face checkpoints available

**Native Multimodal Integration (K2.5+):**
- **MoonViT Encoder:** 400M dedicated vision parameters
- **Multi-Head Latent Attention:** compresses KV projections, yielding 40–50% memory bandwidth reduction
- Trained end-to-end on 15T mixed tokens (not post-hoc adapters)
- Supports image, video, and text processing natively

**Quantization-Aware Training:**
- Native INT4 quantization during training (not post-hoc)
- 2× inference speedup without accuracy loss
- Enables local deployment on consumer-grade GPUs

### 2.4 Model Comparison Matrix: All Kimi Variants

| Feature | Kimi K2 | K2-Instruct-0905 | K2 Thinking | K2.5 | K2.6 |
|---------|---------|-------------------|-------------|------|------|
| Release | Jul 2025 | Sep 2025 | Nov 2025 | Jan 2026 | Apr 2026 |
| Total Params | 1T | 1T | 1T | 1T | 1T |
| Active Params | 32B | 32B | 32B | 32B | 32B |
| Context | 128K | 256K | 256K | 256K | 262K |
| Multimodal | No | No | No | Yes (MoonViT) | Yes (MoonViT) |
| Reasoning Traces | No | No | Yes | Yes | Yes |
| Agent Swarm | No | No | No | Yes (100 agents) | Yes (300 agents) |
| Max Task Duration | — | — | — | Hours | 12 hours |
| Coordinated Steps | — | — | — | ~hundreds | 4,000+ |
| Context Compression | No | No | No | Basic | Automatic |
| License | Modified MIT | Modified MIT | Modified MIT | Modified MIT | Modified MIT |
| Hugging Face | Yes | Yes | Yes | Yes | Yes |

### 2.5 Expert Specialization

Kimi K2's 384 experts are not randomly organized — they develop specialized capabilities through training:

- **Math notation experts:** Specialize in mathematical reasoning, equation parsing, symbolic manipulation
- **Code syntax experts:** Focus on programming language grammar, AST generation, debugging patterns
- **Natural language reasoning experts:** Handle prose generation, summarization, logical argumentation
- **Vision-language experts (K2.5+):** Process image-text alignment, visual grounding, chart interpretation
- **Tool-use experts:** Manage API calling patterns, function signatures, response parsing

This specialization emerges naturally from the MoE training process and contributes to Kimi K2's strong performance across diverse benchmarks.

### 2.6 Token Training Corpus Breakdown

Kimi K2 was trained on 15.5 trillion tokens, comprising:
- **Multilingual text:** ~60% (Chinese ~35%, English ~20%, other languages ~5%)
- **Code:** ~20% (Python, JavaScript, Java, C++, and others)
- **Mathematics:** ~8% (textbooks, research papers, competition problems)
- **Scientific literature:** ~7%
- **Web content:** ~5%

Kimi K2.5 expanded this to include 15 trillion mixed visual and textual tokens, with image-text pairs integrated from the beginning of training rather than as a post-training adaptation.

---

## 3. Capabilities & Benchmarks

### 3.1 Detailed Kimi K2.5 Benchmark Analysis

**Coding Benchmarks:**

| Benchmark | Kimi K2.5 | Claude Opus 4.5 | GPT-5.2 | Notes |
|-----------|-----------|------------------|---------|-------|
| SWE-Bench Verified | 76.8% | 80.9% | 80.0% | Real GitHub issues |
| SWE-Bench Multilingual | 73.0% | — | — | Non-English codebases |
| LiveCodeBench | 85.0% | — | — | Competitive programming |
| HumanEval | — | — | — | Standard coding eval |
| MBPP | — | — | — | Basic programming problems |

Kimi K2.5's coding performance is particularly notable for its multilingual capabilities. The 73.0% on SWE-Bench Multilingual demonstrates strength beyond English-dominant codebases, a critical advantage for global development teams.

**Math & Reasoning Benchmarks:**

| Benchmark | Kimi K2.5 | Claude Opus 4.5 | GPT-5.2 | Notes |
|-----------|-----------|------------------|---------|-------|
| AIME 2025 | 96.1% | 93% (100% w/ tools) | 100% | Math competition |
| HMMT 2025 | 95.4% | — | — | Harvard-MIT Math Tournament |
| GPQA-Diamond | 87.6% | — | — | Graduate-level QA |
| Humanity's Last Exam | 50.2% | — | — | With tool use |
| MATH | — | — | — | Math problem solving |

The AIME 2025 score of 96.1% places Kimi K2.5 among the top performers on this challenging competition math benchmark. The gap to GPT-5.2's 100% is narrowing with each Kimi release.

**Vision & Multimodal Benchmarks:**

| Benchmark | Kimi K2.5 | Notes |
|-----------|-----------|-------|
| MMMU Pro | 78.5% | Academic multimodal reasoning |
| MathVision | 84.2% | Diagrams, charts, geometry |
| VideoMMMU | 86.6% | Temporal video understanding |
| ChartQA | — | Chart interpretation |
| DocVQA | — | Document visual QA |

The MoonViT encoder enables strong performance on visual reasoning tasks. The 84.2% on MathVision is particularly impressive, as it requires understanding mathematical diagrams and geometric proofs from images.

### 3.2 Kimi K2 Thinking Benchmarks (Nov 2025)

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Humanity's Last Exam (HLE) | 44.9% | Open-ended reasoning across all domains |
| BrowseComp | 60.2% | Web browsing and complex comprehension |
| SWE-Bench Verified | 71.3% | Real-world GitHub issue resolution |
| AIME 2025 | Competitive | Math competition (on par with o1) |
| LiveCodeBench | Competitive | Competitive programming tasks |

Kimi K2 Thinking introduced chain-of-thought reasoning traces that significantly improved performance on complex reasoning tasks. The model outputs intermediate reasoning steps, making it more transparent and debuggable for developers.

### 3.3 Agentic Workflow Benchmarks

| Benchmark | Kimi K2.5 | Claude Opus 4.5 | GPT-5.2 |
|-----------|-----------|------------------|---------|
| BrowseComp (swarm) | 78.4% | — | — |
| Wide Search | 79.0% | — | — |
| Agent Swarm Speedup | 4.5× | — | — |
| Sequential Tool Calls | 300+ | ~100 | ~50 |

The Agent Swarm technology represents a significant differentiator for Moonshot AI. While most providers offer single-agent tool calling, Kimi's ability to coordinate hundreds of parallel agents enables it to tackle tasks that would be infeasible for sequential approaches.

### 3.4 Kimi K2.6 Benchmarks (Apr 2026)

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Terminal-Bench 2.0 | 66.7% | Terminal command execution |
| SWE-Bench Pro | 58.6% | Harder subset (filters out 1-file fixes) |
| MathVision (w/ Python) | 93.2% | Tool use + reasoning |

**Partner-Reported Improvements (Independent Third-Party Data):**

| Partner | Improvement |
|---------|-------------|
| CodeBuddy | +12% code generation accuracy, +18% long-context stability |
| Vercel | >50% improvement on internal Next.js benchmark |
| Factory.ai | +15% on both evaluated benchmarks |

---

## 4. API Details & Platform

### 4.1 API Platform

Moonshot AI provides API access through its platform at [platform.moonshot.ai](https://platform.moonshot.ai/). The API is compatible with OpenAI's API format, making it easy to integrate with existing tooling.

**API Base URL:** `https://api.moonshot.cn/v1`

**Authentication:** Bearer token via API key

### 4.2 API Pricing (as of Jan–Apr 2026)

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Context |
|-------|---------------------|----------------------|---------|
| **Kimi K2.5** | $0.60 | $2.50 | 256K |
| **Kimi K2.6** | $0.60 | $2.50 | 262K |
| **Kimi K2 Thinking** | $0.60 | $2.50 | 256K |

**Consumer Pricing (China, Kimi app):**

| Plan | Duration | Price (CNY) |
|------|----------|-------------|
| Basic | 4 days | ¥5.2 |
| Monthly | 1 month | ¥28 |
| Quarterly | 3 months | ¥78 |
| Half-Year | 6 months | ¥198 |
| Annual | 1 year | ¥399 |

### 4.3 Four Operational Modes

| Mode | Use Case | Key Parameters | Notes |
|------|----------|----------------|-------|
| **Instant** | Fast, simple queries | `thinking: False`, temp=0.6, top_p=0.95 | Skips reasoning traces; 60–75% fewer tokens |
| **Thinking** | Step-by-step reasoning | temp=1.0, top_p=0.95, includes reasoning_content | Ideal for math, logic, debugging |
| **Agent** | Multi-step tool use | Up to 300 sequential tool calls | Stable across long workflows |
| **Agent Swarm** | Parallel orchestration | 100+ autonomous agents | 4.5× speedup on parallelizable tasks |

**Enabling Instant Mode via API:**
```python
extra_body={'chat_template_kwargs': {"thinking": False}}
```

### 4.4 Agent Swarm Technology

Kimi K2.5 introduced Agent Swarm, a technology that coordinates up to 100 specialized AI agents in parallel:

- **Orchestrator** decomposes tasks into independent subtasks
- **Dynamically spawns** domain-specific agents
- **Example:** "Research top YouTube creators across 100 domains" → 100 search agents
- **Parallel-Agent Reinforcement Learning** training approach:
  - Early phase: Rewards parallel execution to avoid serial collapse
  - Final reward: 80% task quality, 20% critical path efficiency
- Uses *critical steps* metric (slowest sub-agent), not total steps

**K2.6 Swarm Upgrades:**
- Up to **300 sub-agents** (from 100 in K2.5)
- **4,000+ coordinated steps**
- **12-hour maximum task duration**
- Native primitives for spawning, scheduling, and reconciling agents

### 4.5 Mooncake Serving Platform

Mooncake is Moonshot AI's backend serving infrastructure:
- Processes **100 billion tokens per day**
- Won **Erik Riedel Best Paper Award** at USENIX FAST 2025
- Powers all Kimi services with low-latency inference
- Designed for MoE model serving efficiency

---

## 5. Reinforcement Learning with LLMs

Moonshot AI published a technical report: "Kimi k1.5: Scaling Reinforcement Learning with LLMs" (arXiv:2501.12599). Key findings:

- Achieved state-of-the-art reasoning on par with OpenAI o1
- Key innovations:
  - Long context scaling for RL
  - Improved policy optimization
  - **No Monte Carlo tree search**, value functions, or process reward models needed
  - Pure RL scaling approach

This represents a significant contribution to the field, demonstrating that RL scaling can achieve competitive results without the complex tree-search mechanisms used by competitors.

---

## 6. Competitive Positioning

### 6.1 Versus Western Providers

| Dimension | Kimi K2.5 | GPT-5.2 | Claude Opus 4.5 | Gemini 3.0 Pro |
|-----------|-----------|---------|------------------|----------------|
| Architecture | MoE 1T/32B active | Proprietary | Proprietary | Proprietary |
| SWE-Bench Verified | 76.8% | 80.0% | 80.9% | ~78% |
| AIME 2025 | 96.1% | 100% | 93% | ~95% |
| Context Window | 262K | — | — | — |
| API Price ($/1M in) | $0.60 | $2.50–$10 | $3.75–$15 | $1.25–$5 |
| License | Modified MIT | Closed | Closed | Closed |

### 6.2 Versus Chinese Providers

| Dimension | Kimi K2.5 | Qwen3.7 Max | GLM-5.1 | DeepSeek-V3 |
|-----------|-----------|-------------|---------|-------------|
| Architecture | MoE 1T/32B | MoE ~1T | Proprietary | MoE |
| SWE-Bench | 76.8% | 60.6% (SWE-Pro 60.6) | 58.4% | ~70% |
| Open Source | Modified MIT | Apache 2.0 | MIT | Apache 2.0 |
| API Price ($/1M in) | $0.60 | $1.25–$2.50 | ~$0.50–$1 | $0.14–$0.55 |
| Agent Swarm | Yes (300 agents) | Limited | Limited | No |

### 6.3 Market Position

- **User Adoption:** As of Aug 2024, Kimi was #3 in active monthly users in China. Dropped to #7 by Jun 2025. The K2 release (Jul 2025) led to the most-downloaded model on Hugging Face that day.
- **Open-Source Impact:** Kimi K2's release under a modified MIT license made it one of the most significant open-weight models of 2025.
- **Cost Efficiency:** Kimi K2.5 is 76% cheaper than Claude Opus 4.5 on benchmark tasks ($0.27 vs $1.14 per benchmark suite).
- **Strengths:** Agentic coding, parallel agent orchestration, long-context reasoning, multimodal understanding
- **Weaknesses:** Less brand recognition outside China, smaller ecosystem than OpenAI/Anthropic, consumer GPU requirements for local deployment are still significant

---

## 7. Recent Developments (Mid-2026)

### 7.1 K2.6 Release (April 2026)

K2.6 was released on April 21, 2026, with a remarkably fast 8-day preview-to-GA transition:

- **Context window expanded** to 262,144 tokens
- **Automatic context compression** — summarizes/elides history as window fills
- **Agent Swarm v2** — up to 300 sub-agents, 4,000+ coordinated steps
- **12-hour task duration** support
- **Proactive autonomy** — recognizes "I am stuck" and either replans or escalates
- **Three shipped use cases:**
  1. Inference optimization in Zig (~193 tokens/sec, 20% faster than LM Studio)
  2. Performance engineering on `exchange-core` (185% median throughput improvement)
  3. Design-to-code full-stack generation (Vercel >50% Next.js benchmark gain)

### 7.2 K3 Anticipation

Moonshot has maintained a 2–3 month major-update cadence for nearly a year. Given the compressed K2.6 preview-to-GA timeline, K3 may arrive on a similarly accelerated schedule in mid-to-late 2026.

### 7.3 Ecosystem Growth

- **Kimi Code CLI** recommended for long-horizon coding workflows
- **API defaults** emphasize `temperature=1.0, top_p=1.0` — users are advised not to lower these reflexively
- **Hugging Face availability** for self-hosting with quantized INT4 weights
- Growing integration with third-party developer tools and platforms

---

## 8. Key Strengths & Weaknesses Summary

### Strengths:
1. **Open-weight leadership** — Kimi K2 series released under modified MIT, enabling broad adoption
2. **Agentic capabilities** — Agent Swarm technology with 300+ parallel agents is unique
3. **Cost efficiency** — 76% cheaper than comparable Western models
4. **Research contributions** — Muon optimizer, RL scaling paper
5. **Infrastructure excellence** — Mooncake platform processes 100B tokens/day
6. **Rapid iteration** — 2–3 month major release cadence
7. **Multimodal native** — MoonViT encoder trained end-to-end, not bolted-on

### Weaknesses:
1. **Geographic focus** — Primarily China-focused, limited international presence
2. **Brand recognition** — Less known outside China compared to OpenAI, Anthropic
3. **Hardware requirements** — Consumer GPU deployment still requires high-end hardware
4. **License restrictions** — Modified MIT requires attribution for large-scale commercial use
5. **Ecosystem maturity** — Smaller third-party tool ecosystem than established providers

---

## 9. Deployment & Self-Hosting

### 9.1 Self-Hosting Requirements

Kimi K2 can be self-hosted using the open-source weights available on Hugging Face. Requirements vary by configuration:

| Configuration | GPU Memory | GPU Type | Notes |
|---------------|------------|----------|-------|
| INT4 Quantized | ~256 GB | 8× H100 80GB or 4× H200 | Recommended for production |
| INT4 Quantized (minimal) | ~128 GB | 4× H100 80GB | Reduced throughput |
| FP16 (full precision) | ~2 TB | Multiple H100 nodes | Research/evaluation only |
| FP8 | ~1 TB | Multiple H100/H200 | Balanced precision/performance |

The INT4 quantization is native (trained into the model), not post-hoc, which means there is no accuracy loss compared to higher precision inference.

### 9.2 Inference Frameworks

Supported inference frameworks:
- **vLLM:** Full support with MoE optimization
- **SGLang:** Recommended for agent workflows
- **TensorRT-LLM:** NVIDIA-optimized path
- **Custom Moonshot inference:** Highest performance, proprietary

### 9.3 Cloud Deployment

Moonshot AI offers managed API access through platform.moonshot.ai. The API is OpenAI-compatible, allowing drop-in replacement for existing applications.

**Rate Limits (approximate, subject to change):**
- Free tier: Limited requests per day
- Paid tier: Higher throughput, priority access
- Enterprise: Custom limits, dedicated capacity

---

## 10. Research Contributions

### 10.1 Muon Optimizer

The Muon optimizer is a significant contribution to LLM training methodology:

**Key Properties:**
- 2× faster than AdamW for MoE model training
- Uses matrix preconditioning instead of scalar per-parameter updates
- Scales efficiently to large parameter counts
- Reduces training time and compute costs

**Applications:**
- Used to train Kimi K2 and all subsequent models
- Available as open-source library on GitHub
- Adopted by other research groups for MoE training

### 10.2 Reinforcement Learning Scaling

The Kimi K1.5 RL paper demonstrated that pure reinforcement learning scaling can achieve competitive results without:
- Monte Carlo tree search (MCTS)
- Value function networks
- Process reward models
- Human preference data

This approach contrasts with competitors who rely heavily on these mechanisms, suggesting a more direct path to improved reasoning capabilities.

### 10.3 Mooncake Architecture

Mooncake won the Erik Riedel Best Paper Award at USENIX FAST 2025 for its innovative serving architecture:

**Key Innovations:**
- Efficient MoE model serving with expert routing optimization
- KV-cache management for long-context inference
- Dynamic batching for throughput optimization
- Memory-efficient expert loading/unloading

---

## 11. Industry Partnerships & Ecosystem

### 11.1 Developer Platform Integration

Kimi models are available through multiple platforms:
- **Hugging Face:** Open weights for self-hosting
- **OpenRouter:** Third-party API access
- **litellm:** Python library integration
- **Various AI agent frameworks:** LangChain, LlamaIndex, etc.

### 11.2 Enterprise Adoption

Kimi K2's combination of open weights, competitive performance, and low API pricing has attracted enterprise adoption in:
- Software development teams (agentic coding)
- Research institutions (math and science reasoning)
- Financial services (document analysis and reasoning)
- Healthcare (medical literature analysis)

### 11.3 Academic Impact

Moonshot AI's open-source releases have spawned:
- 200K+ Hugging Face derivatives
- Academic papers analyzing MoE routing patterns
- Integration into university AI curricula
- Benchmark comparison studies

---

## 12. Future Outlook

### 12.1 K3 Expectations

Based on Moonshot's 2–3 month release cadence, K3 is expected in mid-to-late 2026. Anticipated improvements:
- Larger active parameter count
- Enhanced multimodal capabilities
- Improved agent orchestration
- Better cost efficiency
- Possibly larger context windows

### 12.2 Market Trajectory

Moonshot AI is positioned to compete globally as:
- The leading Chinese open-weight LLM provider
- A cost-effective alternative to Western models
- An agentic AI pioneer with Agent Swarm technology
- A research contributor with Muon and RL scaling work

Key challenges include:
- Building international brand awareness
- Expanding developer ecosystem
- Navigating geopolitical technology restrictions
- Competing with well-funded Western alternatives

---

## 13. References & Sources

- Wikipedia: Moonshot AI — https://en.wikipedia.org/wiki/Moonshot_AI
- Codecademy: Kimi K2.5 Complete Guide — https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model
- Kimi K2.6 Official Release Blog — https://kimi-k2.org/blog/24-kimi-k2-6-release
- Moonshot AI Official Site — https://www.moonshot.ai/
- Kimi API Platform — https://platform.moonshot.ai/
- GitHub: MoonshotAI/Kimi-K2 — https://github.com/moonshotai/Kimi-K2
- Hugging Face: moonshotai/Kimi-K2-Thinking — https://huggingface.co/moonshotai/Kimi-K2-Thinking
- arXiv:2501.12599 — Kimi k1.5: Scaling Reinforcement Learning with LLMs
- arXiv:2502.16982 — Muon is Scalable for LLM Training
- HPC Wire: Moonshot AI's Kimi K2.5 Expands What Open-Weight Models Can Do