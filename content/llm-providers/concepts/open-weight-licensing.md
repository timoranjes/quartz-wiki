---
domain: llm-providers
type: concept
tags: [concept/licensing, concept/open-source]
aliases: [Open Weights, Open Source, Licensing]
created: 2026-06-01
---
# Open-Weight Licensing

## Overview
Open-weight models provide model weights for download and self-hosting, but licensing terms vary significantly. **Not all open-weight models are open source** (OSI-compliant).

## License Types in LLM Space (2026)

### Fully Permissive
| License | Providers | Restrictions |
|---------|-----------|-------------|
| **Apache 2.0** | Mistral (Small 4, NeMo), Alibaba (most Qwen), DeepSeek (MIT) | None |
| **MIT** | DeepSeek (V3, R1 distills, V4 planned) | None |

### Restricted Open-Weight
| License | Providers | Restrictions |
|---------|-----------|-------------|
| **Llama 4 Community License** | Meta | Free under 700M MAU; >700M requires Meta approval |
| **Modified MIT** | Mistral (Medium 3.5, Large 3) | More permissive than Apache-with-restrictions |
| **Open v25.12** | Mistral (Large 3) | Mistral's own open license |

### Closed-Source
| Provider | Models | Notes |
|----------|--------|-------|
| OpenAI | All GPT models | API-only |
| Anthropic | All Claude models | API-only |
| Google | All Gemini models | API-only |
| xAI | All Grok models | API-only |

## Why Licensing Matters
- **Self-hosting**: Open weights enable deployment on own infrastructure
- **Fine-tuning**: Open weights allow domain adaptation
- **Data privacy**: Self-hosting = zero data leaves infrastructure
- **Cost at scale**: Free to self-host at any volume
- **Vendor lock-in**: Open weights eliminate dependency on single provider

## Provider Open-Weight Portfolios (2026)

| Provider | Open-Weight Models | License | Count |
|----------|-------------------|---------|-------|
| **Alibaba** | Qwen3.5-9B through 397B-A17B, Qwen3.6 series | Apache 2.0 | 100+ |
| **Meta** | Llama 4 Scout, Maverick | Community License | 2 released |
| **Mistral** | Small 4, Large 3, Medium 3.5, Ministral series | Apache 2.0 / MIT | 8+ |
| **DeepSeek** | V3, R1 distills (1.5B–70B), V4 planned | MIT | 10+ |

## Related
- [[meta-llama]] — Llama 4 Community License details
- [[mistral]] — Most diverse licensing (Apache 2.0 + MIT + Premier)
- [[alibaba-qwen]] — 100+ Apache 2.0 models
- [[deepseek]] — MIT-licensed, most permissive among frontier providers
