---
title: Microsoft (Phi/Copilot)
researched: 2026-06-05
sources:
  - https://azure.microsoft.com/en-us/products/phi
  - https://azure.microsoft.com/en-us/blog/one-year-of-phi-small-language-models-making-big-leaps-in-ai/
  - https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
  - https://en.wikipedia.org/wiki/Microsoft
---

# Microsoft (Phi/Copilot)

## Company Facts
- Founded: April 4, 1975
- HQ: Redmond, WA, USA
- CEO: Satya Nadella (since Feb 2014)
- Funding/Valuation: Public company (MSFT), ~$3.5T+ market cap
- Employees: ~228,000 (2025)

## Model Lineup

### Phi Small Language Models (Open-weight, MIT License)
| Model | Size | Context | Input $/1M | Output $/1M | Type |
|-------|------|---------|------------|-------------|------|
| Phi-4 | 14B | — | Open-weight (free) | Open-weight (free) | Reasoning/math |
| Phi-4-reasoning | 14B | — | Open-weight (free) | Open-weight (free) | Reasoning (SFT from o3-mini data) |
| Phi-4-reasoning-plus | 14B | — | Open-weight (free) | Open-weight (free) | Reasoning (RL-enhanced) |
| Phi-4-mini-reasoning | 3.8B | — | Open-weight (free) | Open-weight (free) | Math reasoning |
| Phi-4-mini | — | — | Open-weight (free) | Open-weight (free) | Instruction-tuned |
| Phi-4-multimodal | — | — | Open-weight (free) | Open-weight (free) | Text + audio + vision |
| Phi-3.5 | — | — | Open-weight (free) | Open-weight (free) | Multilingual |
| Phi-3 | — | — | Open-weight (free) | Open-weight (free) | Language/coding |

*Note: Phi models are open-weight under MIT License. Available via Azure AI Foundry (pay-as-you-go MaaS), Hugging Face, and Ollama. MaaS pricing varies by deployment.*

### Microsoft 365 Copilot (SaaS)
| Plan | Price | Notes |
|------|-------|-------|
| Copilot Chat (Free) | Included with eligible M365 | Web-grounded AI, select M365 apps |
| Copilot Business | $18/user/mo (annual) / $25.20/user/mo (monthly) | Full M365 app integration, Work IQ |
| Copilot Enterprise | Contact sales | Advanced governance, analytics |
| Copilot Studio | Contact sales | Custom agent building |

## Capabilities
- Reasoning: yes (Phi-4-reasoning rivals much larger models on AIME, GPQA)
- Vision: yes (Phi-4-multimodal)
- Audio: yes (Phi-4-multimodal)
- Tool Use: yes (Phi-4-mini has built-in function calling)
- Agentic: yes (Copilot agents, Copilot Studio)
- Coding: moderate (Phi models perform well on coding benchmarks)

## Key Facts
- Phi models are Microsoft's Small Language Model (SLM) family, starting with Phi-1 (1.3B, code-focused) in mid-2023.
- Phi-4-reasoning (14B) outperforms OpenAI o1-mini and DeepSeek-R1-Distill-Llama-70B (5× larger) on reasoning benchmarks; rivals DeepSeek-R1 (671B) on AIME 2025.
- Phi-4-mini-reasoning (3.8B) matches OpenAI o1-mini on math benchmarks (GPQA Diamond, Math-500).
- Phi models are optimized for on-device/edge deployment; Phi Silica variants preloaded on NPU-powered Copilot+ PCs.
- Microsoft invested $13B+ in OpenAI (27% stake); integrates GPT models into Copilot products.
- Microsoft 365 Copilot pricing: $18/user/month annual (discounted from $21 through Jun 2026), $25.20/month for monthly billing.
- 2025 revenue: $281.7B; operating income: $128.5B.

## Sources
- https://azure.microsoft.com/en-us/products/phi
- https://azure.microsoft.com/en-us/blog/one-year-of-phi-small-language-models-making-big-leaps-in-ai/
- https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
- https://en.wikipedia.org/wiki/Microsoft
