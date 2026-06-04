---
title: Optical Transceivers
created: 2026-05-29
updated: 2026-06-04
type: concept
tags: [optical, bottleneck, cpo, supply-demand]
sources: [raw/articles/techtimes-optical-component-shortage-2026.md, raw/articles/华泰证券光模块功耗提升驱动液冷加速渗透-d4d1cddddd863554.md, raw/articles/lambda-offers-glimpse-into-nvidias-cpo-switch-enabling-more--af33bef83d3dc68c.md]
confidence: high
---

# Optical Transceivers

Optical transceivers are the high-speed lasers, fiber optic cables, and modules that form the nervous system connecting racks inside AI training clusters. AI training clusters require roughly six high-speed optical transceivers per GPU — far more than conventional servers.

## Market Size

- Global market for AI-focused optical transceivers: $16.5 billion (2025) → $26 billion (2026), +57% YoY
- 800G+ transceiver shipments: 24 million units (2025) → 63 million units (2026), 2.6x jump
- McKinsey projects 800G transceiver production will fall 40–60% short of demand through 2027
- 1.6T devices: 30–40% shortfall likely through 2029

## The EML Laser Crisis

At the heart of the crisis is the **electro-absorption modulated laser (EML)**:

- EMLs encode data onto light signals at speeds up to 200 gigabits per lane
- Fewer than 5 companies manufacture EMLs at commercial scale: **Lumentum**, **Coherent**, **Mitsubishi**, **Sumitomo**, **Broadcom**
- On March 2, 2026, **NVIDIA** committed $2 billion each to Lumentum and Coherent — a **$4 billion lockup** of EML laser supply
- Lead times at key EML suppliers stretched beyond 2027 for any buyer who is not NVIDIA
- Lumentum is the only supplier shipping 200G-per-lane EMLs at volume
- Indium phosphide fabrication yields range from 15% to 50% depending on wafer generation

## Fiber Optic Cable Shortage

- AI data centers need ~36x more fiber than traditional CPU server racks
- Data center fiber demand grew 76% YoY in 2025
- North American demand growth: 22–25% (2026) vs supply expansion: 12–19%
- Lead times: 20 weeks for large buyers, up to 1 year for smaller purchasers
- Optical fiber preform manufacturing takes 18–24 months to expand

## Hyperscaler Supply Agreements

- **Meta:** $6 billion supply agreement with **Corning** (January 2026)
- **NVIDIA:** $300 million investment in Corning for three new fiber manufacturing plants
- **Fujikura:** 300 billion yen ($1.88 billion) investment to triple production across Japan and US

## Chinese Suppliers in Module Assembly

- **Innolight** and **Eoptolink** (China-based) supply ~60% of NVIDIA's 800G module demand
- 7 of the top 10 global optical module suppliers in 2024 were Chinese companies
- However, export controls restrict access to epitaxial growth equipment (MOCVD, MBE) needed for EMLs and DSP chips
- Critical components remain concentrated among Western and Japanese suppliers with significant pricing power

## Liquid Cooling for Optical Modules (June 2026)

- **Huatai Securities (June 2026):** AI compute expansion drives surging demand for 800G/1.6T optical transceivers, but power consumption is escalating rapidly with each generation
- Liquid cooling is becoming **mandatory** for high-speed optical modules, creating a new market for liquid-cooled optical module cages (液冷Cage)
- Global production of optical module cages is concentrated in Chinese manufacturers
- Traditional cage makers are actively developing liquid-cooled variants and expanding配套 production capacity
- Leveraging existing customer relationships to accelerate product testing and certification for liquid-cooled cages
- This represents a new sub-segment of the optical supply chain: thermal management for optical components, parallel to the broader data center liquid cooling trend

## CPO Progress — Lambda Showcases NVIDIA CPO Switch (June 2026)

- **Lambda** (Microsoft-backed neocloud) showcased NVIDIA's **Quantum-X Q3450-LD** CPO (co-packaged optics) switch with liquid cooling, highlighting **substantial power savings** vs. traditional pluggable transceiver architectures
- Key advantage: CPO switches eliminate the need for traditional transceivers entirely, reducing power consumption per port and enabling "more tokens" per watt of compute
- Confirms CPO is moving from R&D to production deployment; neoclouds are early adopters as power constraints tighten
- This validates the [[optical-transceivers]] bottleneck thesis: CPO is the structural solution to the EML laser/transceiver shortage, but adoption timeline remains uncertain

## Timeline

- LightCounting projects InP laser shortages begin to ease by mid-2026 as new capacity comes online
- No forecast for full cycle downturn
- New preform manufacturing capacity won't meaningfully ease supply until late 2027 at earliest

## Related

- [[ai-supply-chain-bottlenecks]]
- [[lumentum]]
- [[corning]]
- [[nvidia]]
