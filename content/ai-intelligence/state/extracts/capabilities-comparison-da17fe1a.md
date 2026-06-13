title: Capabilities Comparison
tags: benchmark, capabilities
# Capabilities Comparison

## Coding Performance

| Provider | Model | SWE-bench Verified | LiveCodeBench | HumanEval+ | MBPP |
|----------|-------|-------------------|---------------|------------|------|
| DeepSeek | V4 Pro Max | 80.6% | 93.5 | 96.0 | 94.2 |
| OpenAI | GPT-5.5 | 82.0% | 94.0 | 97.0 | 95.0 |
| Anthropic | Claude Opus 4.6 | 80.8% | 93.0 | 96.5 | 94.8 |
| Google | Gemini 3.5 Pro | 78.0% | 91.0 | 95.0 | 93.0 |
| Alibaba | Qwen3.7 Max | 75.0% | 89.0 | 93.0 | 91.0 |
| xAI | Grok 4.3 | 76.0% | 88.0 | 94.0 | 92.0 |
| Meta | Llama 4 Maverick | 72.0% | 85.0 | 91.0 | 89.0 |
| Mistral | Codestral | 70.0% | 87.0 | 92.0 | 90.0 |
| Moonshot | Kimi K2 | 74.0% | 86.0 | 90.0 | 88.0 |
| MiniMax | M2.5 | 68.0% | 82.0 | 88.0 | 85.0 |
| StepFun | Step-3.7-Flash | 70.0% | 84.0 | 89.0 | 87.0 |
| NVIDIA | Nematron-5 | 71.0% | 83.0 | 90.0 | 88.0 |
| Microsoft | Phi-4 | 55.0% | 70.0 | 78.0 | 75.0 |

## Reasoning Performance

| Provider | Model | AIME 2025 | GPQA Diamond | MATH 500 | GSM8K |
|----------|-------|-----------|-------------|----------|-------|
| OpenAI | GPT-5.5 | Leading | Leading | 98.0 | 97.0 |
| Anthropic | Claude Opus 4.6 | Leading | Leading | 97.5 | 96.5 |
| DeepSeek | V4 Pro Max | — | — | 97.0 | 96.0 |
| Google | Gemini 3.5 Pro | Competitive | Competitive | 96.0 | 95.0 |
| xAI | Grok 4.3 | Competitive | Competitive | 95.0 | 94.0 |
| Meta | Llama 4 Maverick | — | — | 93.0 | 92.0 |
| Alibaba | Qwen3.7 Max | — | — | 94.0 | 93.0 |
| Moonshot | Kimi K2 | — | — | 92.0 | 91.0 |
| Cohere | Command A+ | — | — | 88.0 | 87.0 |
| NVIDIA | Nematron-5 | — | — | 89.0 | 88.0 |
| MiniMax | M2.5 | — | — | 85.0 | 84.0 |
| StepFun | Step-3.7-Flash | — | — | 86.0 | 85.0 |

## Multi-Modal Capabilities

| Provider | Model | Image Input | Image Output | Video | Audio |
|----------|-------|------------|-------------|-------|-------|
| Google | Gemini 3.5 Pro | ✅ | ✅ | ✅ | ✅ |
| MiniMax | M2.5 | ✅ | ✅ (text-to-image) | — | — |
| xAI | Grok 4.3 | ✅ | ✅ | — | — |
| Anthropic | Claude Opus 4.6 | ✅ | — | — | — |
| OpenAI | GPT-5.5 | ✅ | ✅ (DALL-E) | — | ✅ (Whisper) |
| Meta | Llama 4 Maverick | ✅ | — | — | — |
| Alibaba | Qwen3.7 Max | ✅ | ✅ | — | — |
| NVIDIA | Nematron-5 | ✅ | ✅ | — | — |
| Stability AI | Stable Image 3.5 | — | ✅ | — | — |
| StepFun | Step-3.7-Flash | ✅ (vision-language) | — | — | — |
| Zhipu AI | GLM-5 | ✅ | ✅ (Ying video) | ✅ | — |
| Moonshot | Kimi K2 | ✅ | — | — | — |

## Key Takeaways

- **Coding**: DeepSeek V4 Pro Max and GPT-5.5 are tied at the top; DeepSeek offers 54× better price-performance
- **Reasoning**: OpenAI and Anthropic lead; DeepSeek V4 Pro Max competitive with extended thinking
- **Multi-modal**: Google Gemini 3.5 Pro is the most comprehensive (image + video + audio)
- **Open-weight coding**: Mistral Codestral punches above its weight in code-specific benchmarks
- **Edge**: Microsoft Phi-4 achieves 70B-class coding performance at 3.8B parameters

## Related

- [[pricing-comparison]] — DeepSeek leads on price-performance ratio
- [[context-windows]] — Long context affects coding and reasoning capabilities
- [[extended-thinking]] — Reasoning modes boost all reasoning benchmarks significantly