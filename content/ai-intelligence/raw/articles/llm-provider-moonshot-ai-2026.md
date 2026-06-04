---
title: Moonshot AI
researched: 2026-06-05
sources:
  - https://platform.kimi.ai/docs/pricing/chat-v1
  - https://www.moonshot.ai/
  - https://en.wikipedia.org/wiki/Moonshot_AI
  - https://www.scmp.com/tech/article/3352751/kimi-developer-moonshot-ai-valued-us20b-it-navigates-chinas-new-ipo-rules
  - https://deepinfra.com/blog/kimi-k2-6-pricing-guide-deployment-tradeoffs
---

# Moonshot AI

## Company Facts
- Founded: 2023
- HQ: Beijing, China
- CEO: Yang Zhilin (Founder)
- Funding: ~$3.9B+ total raised; $500M Series C at $4.3B (2024); latest round valued company at $20B+ with ~$2B from Meituan Ventures and China Mobile

## Model Lineup
| Model | ID | Context | Input $/1M | Output $/1M | Type |
|-------|-----|---------|------------|-------------|------|
| Kimi K2.6 | kimi-k2.6 | 256K | $0.60–$1.20 | $2.80–$4.50 | LLM (open-weight MoE, 1T/32B active) |
| Kimi K2.5 | kimi-k2.5 | 256K | — | — | LLM (open-weight MoE) |
| moonshot-v1-128k | moonshot-v1-128k | 131K | $2.00 | $5.00 | LLM |
| moonshot-v1-32k | moonshot-v1-32k | 33K | $1.00 | $3.00 | LLM |
| moonshot-v1-8k | moonshot-v1-8k | 8K | $0.20 | $2.00 | LLM |
| moonshot-v1-*-vision-preview | moonshot-v1-*-vision-preview | 8K–131K | $0.20–$2.00 | $2.00–$5.00 | Vision |

Note: Kimi K2.6 pricing varies by provider; native Kimi API pricing is approximately $1.71/1M blended. Moonshot V1 pricing is from native Kimi API Platform.

## Capabilities
- **Reasoning**: K2.5/K2.6 compete with frontier models on HLE, GPQA, reasoning benchmarks
- **Coding**: "Powerful coding capabilities" with SWE-Bench Pro performance competitive with GPT-5.4
- **Vision**: Native multimodal input (K2.6); vision preview models in V1 series
- **Agentic**: Multi-agent orchestration, tool calling, function calling
- **Long Context**: 256K context window on K2 series; 131K on V1-128K
- **JSON Mode**: Structured output support
- **DeepSearchQA**: 83.0 accuracy on DeepSearchQA (vs. Claude Opus 4.6: 80.6)

## Key Facts
1. Moonshot AI was founded in 2023 by Yang Zhilin and is based in Beijing. Creator of the Kimi assistant.
2. Dubbed one of China's "AI Tiger" companies; received a $1B funding round led by Alibaba in early 2024.
3. Kimi K2.6 (April 2026) is a 1T-parameter MoE model with only 32B active parameters, released under modified MIT license.
4. Total funding exceeds $3.9B with the company valued at over $20B (SCMP, 2026).
5. K2.6 outperforms GPT-5.4 on HLE-Full with tools (54.0 vs 52.1) and DeepSearchQA (83.0 vs various competitors).
