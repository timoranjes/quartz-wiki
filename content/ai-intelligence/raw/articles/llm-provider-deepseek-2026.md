---
title: DeepSeek
researched: 2026-06-05
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://www.reuters.com/business/retail-consumer/deepseek-slated-draw-7-billion-maiden-fundraising-sources-say-2026-06-03/
  - https://techcrunch.com/2026/05/06/deepseek-could-hit-45b-valuation-from-its-first-investment-round/
  - https://evolink.ai/blog/deepseek-v4-release-window-prep
---

# DeepSeek

## Company Facts
- Founded: 2023
- HQ: Hangzhou, China
- CEO: Liang Wenfeng (Founder)
- Funding: ~$7B maiden fundraising round (June 2026); valuation ~$45B. First external VC round.

## Model Lineup
| Model | ID | Context | Input $/1M | Output $/1M | Type |
|-------|-----|---------|------------|-------------|------|
| DeepSeek-V4-Flash | deepseek-v4-flash | 1M | $0.14 (cache miss) / $0.0028 (cache hit) | $0.28 | LLM (MoE) |
| DeepSeek-V4-Pro | deepseek-v4-pro | 1M | $0.435 (cache miss) / $0.003625 (cache hit) | $0.87 | LLM (MoE) |

Note: `deepseek-chat` and `deepseek-reasoner` deprecated 2026-07-24; mapped to non-thinking and thinking modes of `deepseek-v4-flash` respectively.

## Capabilities
- **Reasoning**: Supports both non-thinking and thinking (default) modes via Thinking Mode API
- **Tool Use**: Native tool calling support
- **Coding**: FIM (Fill-In-the-Middle) completion in non-thinking mode
- **JSON Output**: Structured JSON output mode supported
- **Chat Prefix Completion**: Beta feature for prefix-guided generation
- **Vision**: Not natively multimodal (text-only models as of V4)

## Key Facts
1. DeepSeek was founded in 2023 by Liang Wenfeng and is one of China's most prominent AI startups.
2. In June 2026, DeepSeek announced its first external funding round of ~$7B at a ~$45B valuation (Reuters, TechCrunch).
3. DeepSeek-V4 models feature aggressive prompt caching with cache-hit prices as low as $0.0028/1M input tokens.
4. Maximum output is 384K tokens with 1M context window across all V4 models.
5. Concurrency limits: 2,500 for Flash tier, 500 for Pro tier.
