---
title: PCB and CCL Materials
created: 2026-05-29
updated: 2026-06-15
type: concept
tags: [pcb, ccl, materials, bottleneck, supply-demand]
sources: [raw/articles/atlaspcb-taiwan-pcb-ccl-second-sourcing-2026.md, raw/articles/中富电路拟定增募资不超85亿元用于ai用pcb产线改扩建等项目-918317d03bbbdb45.md, raw/articles/nov-terraflow-partner-on-fiberglass-solutions-for-ai-data-ce-575b1bd4722351ca.md, raw/articles/铜价奔向105万背后-新能源吃铜铜也正在改变新能源的胃口-ed818e409ba9c630.md]
confidence: medium
---

# PCB and CCL Materials

AI server motherboards require ultra-low-loss copper-clad laminates (CCL) and advanced prepreg materials. The global CCL market has expanded sharply, creating severe allocation constraints.

## Material Requirements for AI Servers

AI server motherboards (particularly for NVIDIA B200 and H200 platforms) require:
- Ultra-low-loss laminates with **Dk values below 3.3** and **Df under 0.002 at 10 GHz**
- 20+ layer PCBs with tight impedance tolerance
- Advanced materials replacing standard FR-4:

| Material | Supplier | Key Spec |
|----------|----------|----------|
| Megtron 7 | Panasonic | Df: 0.001 at 12 GHz |
| T-Glass reinforced CCL | AGC | Dk: 3.15, improved dimensional stability |
| Low-CTE hybrid stackups | Multiple | Required for 20+ layer boards |

## Market Pressures

| Material                 | Price Change (YoY)                                                                                                      | Supply Status                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Copper (LME)             | +38% to $13,300/tonne; China domestic price surging toward ¥105,000/tonne (~$14,500) driven by new energy sector demand | Tight allocation, forcing downstream tech sector adjustments |
| E-glass fiber cloth      | Quota-based                                                                                                             | 8–12 week lead times                                         |
| Low-loss resin systems   | +22%                                                                                                                    | Allocation for top 5 customers                               |
| BT resin (IC substrates) | +15%                                                                                                                    | Managed supply                                               |

## Market Size

- Global PCB industry projected to grow 12.5% to reach **$95.8 billion in 2026**
- Growth disproportionately concentrated in advanced multi-layer and HDI segments

## Taiwan PCB Makers' Response

1. **Second-source qualification:** TPCA organizing joint evaluation of domestic CCL producers (EMC, ITEQ) for applications previously served exclusively by Japanese suppliers. EMC's EM-891K approaches Megtron 6 performance at 30% lower cost.

2. **Material development partnerships:** Zhen Ding Technology announced five-year research collaboration with National Tsing Hua University for next-generation resin systems.

3. **Inventory strategy shifts:** Safety stock extended from 2–3 weeks to 6–8 weeks for critical CCL grades — roughly $200–400 million in additional working capital.

## Key Players

**CCL suppliers:** Mitsubishi Gas Chemical (MGC), Panasonic, AGC, EMC (Elite Material Co.), ITEQ
**PCB manufacturers:** Unimicron, Zhen Ding Technology, Compeq Manufacturing
**PCB equipment:** Han's Laser / 大族激光 (002008.SZ)

**China AI PCB expansion:**
- **中富电路 (Zhongfu Circuit, 300814.SZ):** Announced 8.5B RMB private placement (May 2026) for AI-use PCB production line expansion in Heshan, plus digital upgrade projects. Signals growing domestic China capacity for AI server PCBs, complementing Taiwan's dominant position.

## Han's Laser (大族激光) — PCB Equipment Market Boom (June 2026)

- **Han's Laser / 大族激光 (002008.SZ)** market capitalization surged by **79 billion RMB (~$11B)** — described as a "PCB 卖铲人" (PCB picks-and-shovels play)
- The company is a leading supplier of laser processing equipment for PCB manufacturing — drilling, cutting, and structuring advanced multi-layer boards
- Market cap explosion reflects the AI-driven PCB/CCL capex cycle: as AI server motherboards require 20+ layer ultra-low-loss PCBs, demand for precision laser processing equipment has surged
- Confirms the "卖铲人" (picks-and-shovels) thesis: equipment suppliers benefit disproportionately from downstream capacity expansion booms, as PCB makers race to add AI-grade production lines
- Supply chain implication: PCB equipment lead times likely extending as manufacturers like Han's Laser operate at high utilization — another bottleneck layer in the AI supply chain

## Impact

- Lead time extension: Standard multi-layer boards now quote 5–7 weeks vs 3–4 weeks
- Cost pressure: 8–15% increases on boards requiring advanced materials through Q3 2026

## Related

- [[ai-supply-chain-bottlenecks]]
