---
source_url: https://thebytedive.com/ai/260221-hbm-hbf-sk-hynix-samsung-en/
ingested: 2026-05-29
sha256: 8a5676452f36c0356615561a8a11a715ba06a13b513a8f0caf463ff79d3c54f4
---

# HBM Memory Market Analysis: The Race from HBM4 to HBF Between SK hynix and Samsung
*Source: thebytedive.com | Date: 2026-02-23*

## From PCs to GPUs — A Brief History of the Memory Bottleneck

The heart of an AI data center is widely believed to be the GPU. But the actual time GPUs spend computing is surprisingly low. Research shows that over 50% of attention kernel cycles during LLM inference are stalled waiting for data access. The rest of the time, the GPU is just waiting for data.

## The Birth of HBM and the HBM4 Era

HBM (High Bandwidth Memory) sits right next to the GPU and feeds it data at blazing speeds by stacking memory chips in layers. In February 2026, Samsung Electronics and SK hynix simultaneously began mass production of HBM4, the 6th generation HBM — pushed 3–4 months ahead of the originally targeted mid-2026 timeline.

HBM4's base operating speed is 11.7Gbps, 46% faster than the JEDEC international standard of 8Gbps. A single HBM4 unit costs approximately $700 — 20–30% more expensive than HBM3E, but demand is surging as HBM is essential for AI data centers.

## SK hynix vs. Samsung — The Market Share War

**HBM Market Share (Q3 2025):**
- SK hynix: 57%
- Samsung: 22%
- Micron: 21%

Source: Astute Group (Q3 2025)

SK hynix holds 57% of the HBM market. SK hynix is reportedly set to supply approximately 70% of HBM4 units for NVIDIA's next-generation GPU platform, Rubin. Samsung has set a target to boost its share to the 30% range in 2026. SK hynix surpassing Samsung in annual profits for the first time in 2025 was a symbolic event showcasing the tectonic shift HBM has brought to the industry.

## The Rise of HBF — Solving the Next Bottleneck

**HBM4 vs HBF Comparison:**
| Spec | HBM4 (Current) | HBF (Next Gen) |
|------|---------------|----------------|
| Technology | DRAM stacking | NAND flash stacking |
| Capacity | 24–48 GB | 8–16x capacity vs DRAM |
| Use case | Ultra-fast working memory | High-capacity fast auxiliary storage |
| Production | Feb 2026 | Target: early 2027 |
| Unit price | ~$700 | N/A |

HBF simulations show 8–16x higher capacity than DRAM with 2.69x better performance-per-watt efficiency. SK hynix unveiled a hybrid architecture called "H3" that integrates both HBM and HBF. Simulations combining B200 with 8 stacks of HBM3E and 8 stacks of HBF showed significant LLM inference performance improvements.

## Corporate HBF Strategies

SK hynix is pursuing co-development with SanDisk, targeting sample shipments in H2 2026 and mass production in early 2027. Samsung has chosen the solo development path.

Companies with HBM stacking expertise — like the femtosecond laser grooving technology used to thin HBM4 wafers — will have a structural advantage in HBF. HBM4 wafer thickness has decreased to 20–30 micrometers, hitting the limits of conventional cutting methods. SK hynix has announced adoption of femtosecond laser technology.

## Market Outlook and Risks

The total HBM market in 2026 is projected to reach $54.6 billion, growing 58% year-over-year. Analysts project Samsung and SK hynix are each targeting quarterly operating profit of KRW 30 trillion.

However, the U.S.-China semiconductor war presents a significant risk. When the U.S. banned HBM exports to China in December 2024, China retaliated by banning gallium and germanium exports to the U.S. With China controlling 98% of global gallium production, South Korea's strategic mineral reserves average just 56.8 days' worth — Japan stockpiles up to 180 days.
