---
title: PCB and CCL Materials
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [pcb, ccl, materials, bottleneck, supply-demand]
sources: [raw/articles/atlaspcb-taiwan-pcb-ccl-second-sourcing-2026.md]
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

| Material | Price Change (YoY) | Supply Status |
|----------|-------------------|---------------|
| Copper (LME) | +38% to $13,300/tonne | Tight allocation |
| E-glass fiber cloth | Quota-based | 8–12 week lead times |
| Low-loss resin systems | +22% | Allocation for top 5 customers |
| BT resin (IC substrates) | +15% | Managed supply |

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

## Impact

- Lead time extension: Standard multi-layer boards now quote 5–7 weeks vs 3–4 weeks
- Cost pressure: 8–15% increases on boards requiring advanced materials through Q3 2026

## Related

- [[ai-supply-chain-bottlenecks]]
