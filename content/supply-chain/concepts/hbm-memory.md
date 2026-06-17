---
title: HBM Memory
created: 2026-05-29
updated: 2026-06-17
type: concept
tags: [hbm, memory, bottleneck, supply-demand]
sources: [raw/articles/bytedive-hbm-market-hbm4-hbf.md, raw/articles/fusionww-ai-bottleneck-cowos-hbm.md, raw/articles/informedclearly-semiconductor-bottleneck-2026.md, raw/articles/供应商变股东存储芯片三巨头联手入股anthropicai供应链的权力结构正在重组-80b0813c97de5a7c.md, raw/articles/数智周报华为发表半导体韬定律5年内冲刺等效14nm制程minimax将a股上市宇树科技冲刺科创板anthropic融资6-b7f2a636989c6ab0.md, raw/articles/samsung-shows-first-hbm5-mockup-with-heat-path-block-cooling-33fafbe1ddad8412.md, raw/articles/9点1氪豆包推出付费后月活减少610万anthropic呼吁全球放缓ai开发警告ai自我改进风险罗永浩卸任锤子软件公司执-6957f1cc76adc611.md, raw/articles/银河证券ai算力建设需求爆发推动存储长周期涨价hbm投片比重将持续提升-7d89e121abd27c79.md, raw/articles/amd-takes-over-mext-to-address-growing-memory-constraints-in-5e7d88dd3d58339f.md]
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
| HBM4E | Samples shipping Jun–Jul 2026, MP 2027 | Next enhancement of HBM4, [[sk-hynix]] leading customer validation |
| HBF (future) | Target: early 2027 | NAND flash stacking, 8–16x capacity vs DRAM, 2.69x power efficiency improvement |

## HBM4 Technology Advances

- Base operating speed: 11.7Gbps, 46% faster than JEDEC standard of 8Gbps
- Wafer thickness decreased to 20–30 micrometers, requiring femtosecond laser grooving technology
- SK Hynix adopted femtosecond (one-quadrillionth of a second) laser technology for wafer thinning

## HBM4 Mass Production Status (June 2026)

- **All three suppliers certified:** [[nvidia]] CEO Jensen Huang confirmed at Seoul visit (Jun 2026) that [[sk-hynix]], [[samsung]], and [[micron]] have all passed certification and begun mass production of HBM4 for NVIDIA AI accelerators
- This marks the transition from development/ramp phase to full-scale production — all three memory makers are now actively supplying HBM4
- Huang stated: "三家供应商均已通过认证" (all three suppliers have been certified) and "三家企业都已投产，都在竞相支持Vera Rubin" (all three have started production, all competing to support Vera Rubin)
- Vera Rubin is NVIDIA's latest AI chip platform, and HBM4 supply from all three vendors simultaneously reduces single-supplier risk for NVIDIA

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

## HBM5 — Next Generation (Computex 2026)

- **[[samsung]]** displayed the first physical HBM5 mockup at Computex 2026, pairing it with a new **Heat Path Block** in-package cooling structure — thermal management becoming a differentiator as HBM density increases
- Thermal race between [[samsung]] and [[sk-hynix]] shaping up for HBM5 era; cooling-in-package design signals that thermal constraints are now a first-order design consideration, not an afterthought
- HBM5 expected to further increase bandwidth and capacity per stack, but heat dissipation at higher densities is a growing challenge that may favor vendors with proprietary cooling solutions

## DDR5 Evolution — MRDIMM & Clocked Modules (June 2026)

While HBM dominates the AI accelerator memory layer, conventional DDR5 is also evolving rapidly to serve AI PCs and server host memory:

- **DDR5 MRDIMM (Multiplexed Rank DIMM):** New architecture enables higher data rates and densities while remaining **pin-compatible** with traditional DIMM slots. Transformational evolution — allows server/mainboard upgrades without redesigning memory subsystems.
- **Clocked DDR5 Client Memory Modules:** Enabling scaling to **9,600 MT/s** for AI PCs — requires tight coordination between clocking, power delivery, and system-level management. Represents a step-change from standard DDR5-4800/5600 speeds.
- These DDR5 innovations address the host memory bottleneck: AI workloads increasingly demand high-bandwidth system memory for data preprocessing, context management, and inference serving — not just GPU-adjacent HBM
- Supply chain implication: Memory makers must simultaneously ramp HBM4/HBM5 production AND develop next-gen DDR5 modules — stretching R&D and fab capacity across multiple memory architectures

## Wall Street Leverage Crackdown on Memory Stocks (June 2026)

- **Citi, JPMorgan, Goldman Sachs** raising financing costs for hedge fund leveraged bets on SK Hynix, Samsung, and TSMC via equity swaps
- Some banks **refusing new swap requests** entirely; others evaluating case-by-case
- Trigger: sharp YTD rally in Asian chip stocks raising correction concerns
- Significance: Financial layer signaling overcrowded positioning even as physical supply-demand remains structurally tight. Could create short-term selling pressure that temporarily disconnects stock prices from fundamental shortage dynamics.

## Xbox Memory Cost Explosion — Memory Famine Extends to Gaming (June 2026)

- **Microsoft Xbox CEO Asha Sharma** admitted next-gen Xbox Helix will pay **5x more for memory and storage** in 2027 vs. two years prior
- Called the hardware cost gap "unsustainable" and said it "cannot continue"
- Confirms memory bottleneck is no longer contained to AI — it is now disrupting consumer electronics, gaming consoles, and any product that uses DRAM/NAND
- Extends the [[ai-supply-chain-bottlenecks]] narrative: memory famine forcing even Microsoft-scale buyers to acknowledge structural cost inflation

## HBM Capacity Share — Structural Shift in DRAM Industry (June 2026)

- **Galaxy Securities (June 2026):** AI compute demand explosion driving long-cycle memory price increases; HBM wafer starts as share of total DRAM production rising sharply:
  - HBM wafer starts: **18% of DRAM (2025) → ~30% by 2027** (TrendForce estimate)
  - HBM bit supply share: **8% → ~13% by 2027**
  - NVIDIA Rubin Ultra platform: each GPU configured with **384GB HBM** — further increasing per-GPU HBM consumption
  - AI ASIC shipments also increasing, adding incremental HBM demand
  - 3D stacked DRAM emerging as key technology path for edge AI, breaking through traditional memory bottlenecks
- Significance: HBM is consuming an increasing share of the global DRAM production base — every percentage point of DRAM wafer capacity diverted to HBM reduces supply of conventional DDR5, reinforcing the memory bottleneck across all segments simultaneously
- This confirms the long-cycle price increase thesis: memory pricing power persists not just from AI demand, but from the structural capacity migration toward HBM

## AMD Acquires MEXT — Memory Tiering for Data Centers (June 2026)

- **AMD** acquired **MEXT**, a startup with "Predictive Memory Engine" technology that offloads infrequently accessed data from DRAM to NAND flash storage
- Technology enables **flash to appear as DRAM** to applications — memory tiering that addresses growing data center memory constraints without requiring additional DRAM capacity
- Significance: As DRAM becomes increasingly expensive and scarce (diverted to HBM), data center operators are turning to tiered memory architectures that supplement DRAM with cheaper NAND — a workaround for the memory bottleneck
- Supply chain implication: Memory tiering reduces the effective DRAM demand per server, but also signals that memory constraints are severe enough to drive architectural innovation at the CPU/platform level

## NAND Supply Crisis — AI Data Centers Swallowing Consumer Supply (June 2026)

- **Silicon Motion SVP Nelson Duann** stated publicly that **"the retail SSD market has almost disappeared"** — PC OEMs are now buying third-party SSD drives because direct NAND supply from manufacturers has dried up
- Root cause: NAND makers are **prioritizing shipments to AI data centers** over consumer/PC channels
- **PCIe 6.0 SSD controllers** for consumer SSDs are coming next year (Silicon Motion), but **severe NAND shortages will get even worse in 2027** as AI data center demand continues to absorb supply
- Significance: The memory famine is no longer confined to HBM/DRAM — it has now extended to NAND flash. AI data centers are consuming NAND for high-speed storage (training data pipelines, checkpoint storage) at the expense of consumer SSD supply. This creates a **dual memory squeeze**: HBM consuming DRAM capacity + AI storage consuming NAND capacity, leaving both consumer DRAM and consumer NAND markets structurally undersupplied.
- Combined with Xbox's 5x memory cost admission and AMD's MEXT acquisition (flash-as-DRAM tiering), the NAND crisis confirms that memory scarcity is the broadest bottleneck in the AI supply chain — affecting every memory technology simultaneously
- See [[ai-supply-chain-bottlenecks]] for the full cascade analysis

## Related

- [[hbm-competitive-landscape]]
- [[ai-supply-chain-bottlenecks]]
- [[sk-hynix]]
- [[samsung]]
- [[micron]]
- [[nvidia]]
- [[pcb-ccl-materials]]
