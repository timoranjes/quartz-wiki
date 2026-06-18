---
title: PCB and CCL Materials
created: 2026-05-29
updated: 2026-06-18
type: concept
tags: [pcb, ccl, materials, bottleneck, supply-demand]
sources: [raw/articles/atlaspcb-taiwan-pcb-ccl-second-sourcing-2026.md, raw/articles/中富电路拟定增募资不超85亿元用于ai用pcb产线改扩建等项目-918317d03bbbdb45.md, raw/articles/nov-terraflow-partner-on-fiberglass-solutions-for-ai-data-ce-575b1bd4722351ca.md, raw/articles/铜价奔向105万背后-新能源吃铜铜也正在改变新能源的胃口-ed818e409ba9c630.md, raw/articles/电子布100涨价背后真正的瓶颈不是织机是配方-4712be44d5720b41.md, raw/articles/中信证券硅片涨价如期落地上行周期才刚开始-15ba2e4282e8a5ed.md]
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

## E-Glass Fabric 100% Price Surge — Bottleneck Is Formulation, Not Looms (June 2026)

- **E-glass cloth (电子布) prices have doubled (100% increase)** — the most severe material cost spike in the PCB/CCL supply chain
- **True bottleneck is not weaving looms but chemical formulations and certification:**
  - The real barriers to entry are proprietary resin/glass formulations and the lengthy customer certification process, not equipment capacity
  - Lo织机 (weaving looms) can be purchased and installed relatively quickly, but formulation know-how and qualification cycles take years
  - This creates a structural supply constraint that cannot be easily expanded by capital investment alone
- Implication: E-glass fabric supply cannot respond elastically to demand spikes — the formulation/certification bottleneck means prices will remain elevated even as loom capacity expands. This is a persistent, not cyclical, constraint.

## Silicon Wafer Price Increases Confirmed — Upcycle Just Beginning (June 2026)

- **CITIC Securities (中信证券, June 2026):** Silicon wafer price increases confirmed in Q2 2026, expected to continue through H2 2026 both domestically and internationally
- **Heavily-doped (重掺) silicon wafers** and **overseas lightly-doped (轻掺) wafers** face confirmed tightness
- Domestic lightly-doped wafers expected to benefit from order overflow as overseas buyers seek alternative supply
- Industry entering a **2-year global supply-shortage period** for silicon wafers
- Significance: Silicon wafers are the foundational raw material for all semiconductors — price increases at this layer cascade through the entire supply chain (foundry, memory, power devices). The upcycle is "just beginning" per CITIC, suggesting further price increases ahead.

## Impact

- Lead time extension: Standard multi-layer boards now quote 5–7 weeks vs 3–4 weeks
- Cost pressure: 8–15% increases on boards requiring advanced materials through Q3 2026

## Related

- [[ai-supply-chain-bottlenecks]]

## PCB Sector Super-Cycle Confirmed — Index +116% YTD (June 2026)

- **国证PCB主题指数 (CITIC PCB Theme Index)** has surged **+116.03% YTD** as of June 17, 2026 — making PCB the hottest A-share investment theme
- **深南电路 (Shennan Circuits)** hit daily limit up at ¥444.27, market cap broke through **¥300 billion** — YTD gain of 92.42%
- Multiple PCB stocks hitting daily limit: 科翔股份, 南亚新材, among others
- **PCB-focused funds** generating 100%+ returns YTD
- Significance: Confirms the AI-driven PCB/CCL capex super-cycle is now fully reflected in equity markets. The combination of AI server motherboards (20+ layer ultra-low-loss boards), E-glass fabric price doubling, silicon wafer price increases, and copper price surges has created a multi-layer material cost cascade that is driving massive revenue and profit expansion for PCB manufacturers.
- Supply chain implication: PCB makers are in a pricing sweet spot — demand from AI server buildout is structurally strong, while material cost increases can be passed through to customers (hyperscalers) who are themselves in a capex boom
