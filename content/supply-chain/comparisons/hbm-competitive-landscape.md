---
title: HBM Competitive Landscape
created: 2026-05-29
updated: 2026-05-31
type: comparison
tags: [hbm, competitive-analysis, memory]
sources: [raw/articles/bytedive-hbm-market-hbm4-hbf.md, raw/articles/fusionww-ai-bottleneck-cowos-hbm.md, raw/articles/供应商变股东存储芯片三巨头联手入股anthropicai供应链的权力结构正在重组-80b0813c97de5a7c.md, raw/articles/数智周报华为发表半导体韬定律5年内冲刺等效14nm制程minimax将a股上市宇树科技冲刺科创板anthropic融资6-b7f2a636989c6ab0.md]
confidence: high
---

# HBM Competitive Landscape: SK Hynix vs Samsung vs Micron

The HBM market is a three-player oligopoly with SK Hynix as the dominant leader, Samsung aggressively challenging, and Micron gaining share as a credible alternative.

## Market Share (Q3 2025)

| Company | HBM Share | Strategy | HBF Approach |
|---------|-----------|----------|-------------|
| [[sk-hynix]] | 57% | Dominant leader, ~70% of NVIDIA Rubin HBM4 | Co-development with SanDisk, standardization |
| [[samsung]] | 22% | Targeting 30%+ in 2026, aggressive pricing | Solo development |
| [[micron]] | 21% | Alternative supplier, requalification focus | N/A (focus on HBM) |

## Technology Comparison

| Spec | SK Hynix | Samsung | Micron |
|------|----------|---------|--------|
| HBM4 mass production | Feb 2026 (3–4 months early) | Feb 2026 (simultaneous) | Committed |
| Operating speed | 11.7Gbps (46% above JEDEC) | 11.7Gbps | 11.7Gbps |
| Wafer thinning | Femtosecond laser (20–30μm) | Femtosecond laser | In development |
| HBF roadmap | H3 hybrid architecture (HBM+HBF) | Independent HBF | Not disclosed |
| 2026 pricing | Premium (market leader) | Raising prices 15–20% | Competitive alternative |

## Strategic Dynamics

### SK Hynix: The Incumbent Advantage
- 57% market share gives economies of scale
- ~70% of NVIDIA Rubin HBM4 supply locks in future revenue
- Surpassed Samsung in annual profits for the first time in 2025
- Co-development with SanDisk reduces R&D risk and accelerates HBF timeline

### Samsung: The Aggressive Challenger
- Targeting 30%+ share in 2026
- Raising HBM prices by high-teens to low-twenties percent in 2026 contracts
- Solo HBF development path: higher risk but potentially higher reward if successful
- Leverages existing NAND and DRAM manufacturing scale

### Micron: The Credible Alternative
- 21% share and growing
- Positioned as the diversification choice for buyers seeking to reduce SK Hynix/Samsung dependency
- "Our HBM capacity for calendar 2025 and 2026 is fully booked" — strong demand signal
- Less exposure to geopolitical risk (US-based, not Korea/China)

## Industry Verdict

The HBM market is structurally tight through 2026 and likely beyond. All three players are sold out, and demand growth (58% YoY in 2026) far outpaces capacity expansion. The competitive battleground is shifting from HBM to HBF — companies with stacking expertise (femtosecond laser grooving, wafer thinning) will have structural advantages.

SK Hynix's co-development strategy with SanDisk may prove more resilient than Samsung's solo approach, as HBF requires both DRAM and NAND expertise. Micron's position as a credible alternative provides procurement flexibility but it lacks the NAND expertise needed for HBF.

## Supply Chain Restructuring: Memory Suppliers Become AI Lab Shareholders (May 2026)

In the most significant structural shift in the AI supply chain to date, all three HBM suppliers jointly invested in Anthropic as part of its $65 billion funding round (post-money valuation exceeding OpenAI). This transforms the competitive dynamic:

- **All three players aligned:** Previously competitors, SK Hynix, Samsung, and Micron now share a common shareholder interest in Anthropic's success
- **Demand lock-in:** Each supplier secures a guaranteed HBM allocation baseline from Anthropic, reducing the risk of demand-side disruption
- **Competitive implications for other AI labs:** Labs without memory supplier backing (e.g., xAI, Mistral, domestic Chinese AI companies) may face structural disadvantage in HBM procurement
- **Precedent for other layers:** If this model proves successful, expect similar vertical integration at other bottleneck nodes — [[tsmc]] (foundry), [[lumentum]] (optical), or equipment makers could follow

## Market Size

- 2026 HBM market projected at **$54.6 billion** (+58% YoY)
- Total memory revenues in 2026 likely ~$200 billion (25% of total semiconductor revenues)
- Samsung and SK Hynix each targeting quarterly operating profit of KRW 30 trillion

## Related

- [[hbm-memory]]
- [[sk-hynix]]
- [[samsung]]
- [[micron]]
