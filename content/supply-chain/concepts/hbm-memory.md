---
title: HBM Memory
created: 2026-05-29
updated: 2026-06-03
type: concept
tags: [hbm, memory, bottleneck, supply-demand]
sources: [raw/articles/bytedive-hbm-market-hbm4-hbf.md, raw/articles/fusionww-ai-bottleneck-cowos-hbm.md, raw/articles/informedclearly-semiconductor-bottleneck-2026.md, raw/articles/供应商变股东存储芯片三巨头联手入股anthropicai供应链的权力结构正在重组-80b0813c97de5a7c.md, raw/articles/数智周报华为发表半导体韬定律5年内冲刺等效14nm制程minimax将a股上市宇树科技冲刺科创板anthropic融资6-b7f2a636989c6ab0.md]
confidence: high
---

# HBM (High Bandwidth Memory)

HBM is memory that sits directly adjacent to GPUs, dramatically increasing data transfer speeds by stacking memory chips in layers. During LLM inference, over 50% of GPU attention kernel cycles are stalled waiting for memory access — HBM was designed to solve this bottleneck.

## Market Size and Growth

- 2026 HBM market projected at **$54.6 billion**, growing 58% year-over-year
- Revenues for memory in 2026 are likely about $200 billion (25% of total semiconductor revenues)
- HBM demand exceeds supply by 50–67% through 2026

## HBM Generations

| Generation | Status | Key Specs |
|-----------|--------|-----------|
| HBM3 | In production | Base standard for AI training |
| HBM3E | In production, sold out through 2026 | Higher bandwidth than HBM3 |
| HBM4 | Mass production began Feb 2026 | 11.7Gbps (46% above JEDEC 8Gbps standard), ~$700/unit, 24–48 GB capacity |
| HBF (future) | Target: early 2027 | NAND flash stacking, 8–16x capacity vs DRAM, 2.69x power efficiency improvement |

## HBM4 Technology Advances

- Base operating speed: 11.7Gbps, 46% faster than JEDEC standard of 8Gbps
- Wafer thickness decreased to 20–30 micrometers, requiring femtosecond laser grooving technology
- SK Hynix adopted femtosecond (one-quadrillionth of a second) laser technology for wafer thinning

## HBF — The Next Generation

HBF (High Bandwidth Flash) stacks NAND flash like HBM to increase capacity, placed right next to HBM to boost speed. HBF simulations show 8–16x higher capacity than DRAM with 2.69x better performance-per-watt efficiency.

SK Hynix unveiled a hybrid architecture called "H3" that integrates both HBM and HBF. Simulations combining B200 with 8 stacks of HBM3E and 8 stacks of HBF showed significant LLM inference performance improvements.

## Competitive Landscape

**Market Share (Q3 2025):**
- [[sk-hynix]]: 57% (dominant leader, set to supply ~70% of HBM4 for NVIDIA Rubin)
- [[samsung]]: 22% (targeting 30%+ share in 2026)
- [[micron]]: 21%

SK Hynix surpassed Samsung in annual profits for the first time in 2025, a symbolic event showcasing the tectonic shift HBM has brought to the industry.

## Supply Chain Restructuring: Memory Suppliers Become AI Lab Shareholders (May 2026)

In a landmark shift in AI supply chain power dynamics, the three HBM suppliers — [[sk-hynix]] (57% share), [[samsung]] (22%), and [[micron]] (21%) — jointly invested in Anthropic as part of its $65 billion funding round (post-money valuation exceeding OpenAI). This marks the first time upstream component suppliers have taken equity positions in downstream AI labs, fundamentally restructuring the traditional supplier-customer relationship:

- **Demand security:** Equity stakes lock in long-term HBM purchase commitments, reducing revenue volatility for memory makers
- **Design influence:** Shareholder positions give memory suppliers direct influence over Anthropic's hardware architecture decisions
- **Competitive moat:** Competing AI labs without memory supplier backing face structural disadvantage in securing HBM allocation
- **Industry precedent:** If successful, this model could spread to other bottleneck layers (e.g., [[tsmc]] taking equity in AI labs, or [[lumentum]] in optical component suppliers)

## HBF Corporate Strategies

- **SK Hynix:** Co-development with SanDisk, targeting sample shipments H2 2026, mass production early 2027
- **Samsung:** Solo development path for HBF

## Supply Chain Risks

- China controls 98% of global gallium production
- US banned HBM exports to China in December 2024; China retaliated with gallium/germanium export bans
- South Korea's strategic mineral reserves average just 56.8 days (Japan: up to 180 days)
- **Capacity expansion race (June 2026):** [[sk-hynix]] announced plan to double memory wafer capacity within 5 years, signaling structural shortage expected to persist through the decade. [[samsung]] targeting 30%+ HBM share. [[micron]] expanding as alternative supplier. Combined expansion could ease bottleneck by 2028–2029 but also risks overcapacity if AI demand slows.

## Related

- [[hbm-competitive-landscape]]
- [[ai-supply-chain-bottlenecks]]
- [[sk-hynix]]
- [[samsung]]
- [[micron]]
