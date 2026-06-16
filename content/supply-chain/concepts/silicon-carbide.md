---
title: Silicon Carbide (SiC)
created: 2026-06-09
updated: 2026-06-16
type: concept
tags: [silicon-carbide, materials, supply-demand, components]
sources: [raw/articles/36氪首发-创维独家投资数千万这家企业将碳化硅切割损耗降至40微米内-b191a2d58af0e145.md, raw/articles/chinas-supreme-court-bans-infineon-from-selling-gan-power-ch-8b22a5dac3021ea5.md]
confidence: medium
---

# Silicon Carbide (SiC)

Silicon carbide (SiC) is a wide-bandgap semiconductor material used in power electronics — MOSFETs, diodes, and substrate/epitaxial wafers. While not directly part of the AI compute chain, SiC is increasingly relevant to AI infrastructure power delivery and thermal management.

## Supply-Demand Dynamics (June 2026)

- Since Q4 2025, SiC industry wafer capacity expansion has **slowed**, but demand across three main applications — **automotive, solar+storage (光储), and charging stations** — remains in a high-growth cycle
- Domestic SiC MOSFET device demand growing rapidly
- **New demand surge:** Consumer electronics and AI emerging applications driving concentrated demand spikes
- Semiconductor industry-wide price increase expectations accelerating terminal manufacturers' inventory buildup
- Leading SiC substrate (衬底片) and epitaxial (外延片) manufacturers starting a **new round of capacity expansion**, generating substantial new orders for upstream equipment suppliers

## Relevance to AI Supply Chain

- **Data center power delivery:** SiC power devices are increasingly used in data center power supplies and PDUs due to higher efficiency and thermal performance vs. silicon
- **Liquid cooling systems:** SiC pumps and controllers used in data center liquid cooling infrastructure
- **EV charging infrastructure:** AI data centers co-located with EV charging (growing trend) share SiC supply chain
- **Energy storage:** SiC inverters for solar+storage systems that power data centers

## Industry Structure

- **Upstream:** SiC substrate (衬底片) and epitaxial (外延片) manufacturers — leading players expanding capacity
- **Midstream:** SiC device manufacturers (MOSFETs, diodes)
- **Downstream:** Automotive, solar+storage, charging, consumer electronics, AI infrastructure

## SiC Laser Slicing Equipment — 8-Inch Transition Bottleneck (June 2026)

- **中微精仪 (Zhongwei Jingyi):** Shenzhen startup making SiC wafer laser slicing equipment, completed angel+ round (tens of millions RMB) exclusively funded by Skyworth Investment (创维投资)
- Core innovation: programmable pulse + directional crack propagation technology, achieving **<40μm cut loss** vs. industry standard 80–120μm — every 8 wafers cut yields 1 extra wafer
- 6-inch slicing speed: 15–20 min; 8-inch: 25–30 min; entering head customer mass production validation
- Also develops diamond laser processing equipment (no graphitization/blackening, direct re-growth possible)
- Expanding to quantum chip fabrication (customer deliveries starting Jul–Aug 2026)
- **8-inch SiC transition timeline:** H2 2026 is "8寸线建设元年" (Year One of 8-inch line construction) — head customers have obtained environmental permits, civil construction starting, equipment selection underway
- **Industry context:** 6-inch SiC "selling at a loss per wafer" — entire cost chain optimized except cutting loss, which becomes the decisive bottleneck at 8-inch scale
- Platform company (not just SiC cutter): validated 12-inch silicon ultra-thin slicing at <1μm loss
- Relevance: SiC cutting equipment historically monopolized by foreign companies — 中微精仪 claims full domestic IP covering mechanism research, process development, optical optimization, and system design

## China's Supreme Court Bans Infineon from Selling GaN Power Chips (June 2026)

- **China's Supreme People's Court** upheld an injunction **prohibiting Infineon from selling disputed GaN (gallium nitride) products in mainland China**
- Case brought by **Innoscience (英诺赛科)**, China's market-leading GaN manufacturer — a major victory in a multi-region patent war
- GaN power chips are increasingly used in fast charging, data center power delivery, and EV applications — overlapping with the [[silicon-carbide]] power semiconductor ecosystem
- Significance: This is a landmark IP enforcement action by China's highest court against a major European semiconductor company. It signals:
  - China's growing willingness and ability to use patent litigation to protect domestic semiconductor champions
  - Potential supply disruption for Infineon's GaN products in the world's largest power semiconductor market
  - Competitive shift: Innoscience and other domestic GaN makers gain market share as a global competitor is barred from China
- AI supply chain relevance: GaN power devices are used in high-efficiency data center power supplies and chargers — any supply disruption in the GaN segment affects AI infrastructure power delivery efficiency improvements

## Related

- [[ai-data-center-infrastructure]]
- [[ai-supply-chain-bottlenecks]]
- [[pcb-ccl-materials]]
