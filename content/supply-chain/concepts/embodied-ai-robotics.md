---
title: Embodied AI Robotics
created: 2026-06-04
updated: 2026-06-05
type: concept
tags: [components, bottleneck]
sources: [raw/articles/深圳具身公司星尘智能完成超10亿b轮融资估值破百亿硬氪首发-a979f6a6b5ece892.md, raw/articles/36氪首发-浙大教授团队获财通商汤投资做高危场景具身机器人大脑-7e0eba9ec8abf818.md, raw/articles/机器人先挣钱还是先追求agi具身智能路线之争摆上台面-3487bc7ead04e0c0.md, raw/articles/硬氪独家-唐文斌原力灵机并购物流机器人公司并获智谱商汤阶跃等投资-c9807cc2067fbb87.md]
confidence: medium
---

# Embodied AI Robotics

Embodied AI — robots powered by AI models that interact with the physical world — is emerging as a significant new demand driver for AI compute at the edge. The sector is transitioning from demo-stage to commercial deployment, with multiple Chinese companies achieving unicorn valuations.

## Market Dynamics (June 2026)

- The industry is shifting from "stage demo" competition to real-world deployment in complex physical environments; technical routes have not yet converged
- Key differentiation areas: transmission mechanisms, model architectures, data strategies
- Two competing strategic philosophies: (1) monetize early with specific applications, vs. (2) pursue AGI-level general-purpose intelligence first

## Key Players

### Astribot (星尘智能)

- **Shenzhen-based** cable-driven (绳驱) AI robotics company; valuation exceeded **10B RMB** after B-round financing
- Raised **10B+ RMB** across three rounds in three months; backers include Tencent, Alibaba, ByteDance-affiliated funds, 中科创达
- Secured thousand-unit industrial/commercial service orders with 中科创达, expanding overseas; built application innovation center in Jiangdu for cultural/hotel scenarios
- Founded 2022; CEO 来杰 (ex-Tencent Robotics Lab #1 employee, ex-Baidu Xiaodu team lead), 17+ years in AI/robotics
- **Full-stack architecture:** "AI Model – Embodied OS – Cable-Driven Body" all self-developed

**Technical Architecture:**
- **Lumo:** End-to-end whole-body VLA (Vision-Language-Action) base model for high-level reasoning, complex semantic understanding, abstract instruction decomposition, and unknown scene generalization
- **DuoCore framework:** Fast-slow协同 (coordinated) architecture — nearly identical to Figure's Helix architecture released around the same time
  - **Fast system:** Millisecond-level real-time response for posture adjustment, obstacle avoidance, joint buffering
  - **Slow system:** Long-horizon task decomposition, cross-space path planning, global strategy generation
- **Cable-driven transmission:** Global first to mass-produce cable-driven AI robots; tendon-like actuation with rear-mounted motors, providing "rigid-flexible coupling" — sufficient rigidity for operation + flexible buffering for safety

### KuangXing Technology (旷行科技)

- **Hangzhou-based** (founded 2025), focused on high-risk industrial scenarios (mining, energy, petrochemical, transportation)
- Pre-A round funded by 财通资本 and 商汤国香; founder 舒江鹏 is Zhejiang University researcher with 15+ years of industry negative-sample data accumulation
- Product: Engineering brain "KX" + embodied intelligence full-solution suite
- Represents the "vertical scenario first" approach vs. Astribot's general-purpose strategy

### 原力灵机 (Yuanli Lingji / ForceSpirit)

- **Founded March 2025** by 唐文斌 (ex-旷视/ Megavii co-founder & CTO); core team from 旷视 original roster
- **DM0** general embodied foundation model: industry-first "three-class data fusion" combining internet semantics, autonomous driving physical rules, and robot operational data for cross-domain training. 2.4B parameter model achieves sub-millimeter precision in long-sequence continuous tasks; extends chain-of-thought reasoning to physical space. Hardware-agnostic — can migrate across different robot configurations.
- **Merged with Atomix (原力聚合)** logistics robot company via equity acquisition — Atomix has 500+ served projects across 20+ countries, nearly ¥1B annual revenue, #2 global pallet 4-way shuttle sales. The merger creates a data flywheel: Atomix's real-world deployment data fuels 原力灵机 model training, while 原力灵机's models enable Atomix robots' intelligent upgrades.
- **Funding:** Backed by 智谱, 阶跃星辰, 商汤科技 (first time all four major Chinese LLM companies invested in same embodied AI startup), plus 华勤, 上汽恒旭 as strategic investors
- Signals: embodied AI industry transitioning from "data deadlock" to closed-loop data-model-scenario integration; M&A consolidation accelerating (Skild AI also acquired Zebra Robotics around same time)

## Supply Chain Implications

- Embodied AI robots require significant edge compute — each unit is essentially a mobile AI inference node
- Cable-driven vs. rigid transmission mechanisms represent different supply chain requirements: cable-driven needs precision tendon systems, motors, and control electronics; rigid needs gearboxes, harmonic drives
- Mass production of humanoid/cable-driven robots will create new demand for sensors, actuators, and edge AI SoCs
- If the sector scales, it adds a significant incremental demand vector for [[nvidia]]-class edge inference chips and potentially custom AI accelerators
- Insurance "patient capital" (险资耐心资本) is flowing into the sector, signaling long-term state-aligned commitment

## Open Questions

- Technical route convergence: cable-driven, hydraulic, electric — which will dominate?
- General-purpose (Astribot) vs. vertical-specific (KuangXing) — which model wins commercially?
- Timeline to mass production at scale (10K+ units/year)
- Edge compute requirements per robot and implications for AI chip demand

## Related

- [[ai-data-center-infrastructure]]
- [[china-semiconductor-localization]]
