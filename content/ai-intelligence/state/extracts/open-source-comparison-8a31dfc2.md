title: Open Source Comparison
tags: open-source, licensing, ecosystem
# Open Source Comparison

## License Tiers

### Tier 1: Fully Open (MIT / Apache 2.0)

| Provider | Model | License | Commercial Use | HF Downloads |
|----------|-------|---------|---------------|-------------|
| DeepSeek | V4 Pro, V4 Flash | MIT | ✅ Unrestricted | Top 10 on HF |
| Mistral | Small 4, Codestral | Apache 2.0 | ✅ Unrestricted | Top 20 on HF |
| Microsoft | Phi-3.5 variants | MIT | ✅ Unrestricted | Top 30 on HF |
| Moonshot | Kimi K2 | Modified MIT | ✅ Unrestricted | Top 15 on HF |
| Zhipu AI | GLM-4.5 | MIT | ✅ Unrestricted | Top 40 on HF |
| Together AI | Hosted variants | Various | Varies | Platform |
| NVIDIA | Nematron-5-22B | Community | ✅ Yes | Growing |

### Tier 2: Community License (MAU/Revenue Threshold)

| Provider | Model | License | Threshold | Notes |
|----------|-------|---------|-----------|-------|
| Meta | Llama 4 Maverick, Scout | Llama 4 Community | ≤700M MAU | Free for nearly all |
| Alibaba | Qwen3.6, Qwen3.7 variants | Qwen Community | ≤100M MAU | Lower threshold |
| Cohere | Command A+ | Community | Research + commercial | Enterprise-focused |
| Stability AI | Stable Image 3.5 | Stability Community | ≤$1M revenue | Revenue cap |

### Tier 3: Restricted

| Provider | Model | License | Restriction |
|----------|-------|---------|------------|
| xAI | Grok 4.3 weights | Custom Non-Commercial | ❌ No commercial use |
| StepFun | Step-3.5-Flash | Custom | Research only |
| MiniMax | M2 | Custom | Research only |

## Ecosystem Strength

### Hugging Face Presence

| Provider | Models on HF | Downloads | Community Activity |
|----------|-------------|-----------|-------------------|
| DeepSeek | V4 Pro, V4 Flash, V3, R1 | Very High | Active, Chinese + global |
| Meta | Llama 4 family | Very High | Largest ecosystem |
| Mistral | Small 4, Large 3, Codestral | High | Active open-source community |
| Microsoft | Phi-3.5, Phi-4 | High | Academic + edge focus |
| Alibaba | Qwen3.6, Qwen3.7 variants | High | Chinese community dominant |
| Moonshot | Kimi K2 | Medium-High | Growing global adoption |
| NVIDIA | Nematron-5 variants | Medium | Enterprise-focused |

### Framework Support

| Provider | llama.cpp | vLLM | Ollama | HuggingFace | TensorRT-LLM |
|----------|-----------|------|--------|-------------|-------------|
| Meta Llama 4 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | ✅ | ✅ | ✅ |
| DeepSeek V4 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Microsoft Phi | ✅ | ✅ | ✅ | ✅ | — |
| Alibaba Qwen | ✅ | ✅ | ✅ | ✅ | — |
| Moonshot Kimi K2 | ✅ | ✅ | ✅ | ✅ | — |
| NVIDIA Nematron | — | ✅ | — | ✅ | ✅ |
| xAI Grok 4.3 | ❌ | ❌ | ❌ | Weights only | — |

## Innovation Impact

- **DeepSeek MIT license**: Most impactful open-weight release — enables unrestricted commercial use at frontier quality
- **Meta Llama ecosystem**: Largest developer base, most integrations, best documentation
- **Mistral Apache 2.0**: True open-source — no usage restrictions at all
- **Microsoft Phi**: Democratizes local AI — runs on consumer hardware

## Related

- [[open-weight-licensing]] — Detailed license analysis per provider
- [[pricing-comparison]] — Open-weight models dramatically reduce serving costs
- [[distillation]] — Open-weight models enable community distillation