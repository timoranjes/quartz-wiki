---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/uk, model/open-weight, model/multimodal]
aliases: [Stability AI, Stable Diffusion, Stable LM]
created: 2026-06-01
updated: 2026-06-02
---
# Stability AI

## Overview
- **Founded:** 2019, London, United Kingdom
- **Founders:** Emad Mostaque (former CEO, departed Mar 2024), Christian Laforte (CTO), Cyrus Hodes
- **Current CEO:** Prem Akkaraju (since Jun 2024; former Weta Digital CEO)
- **Valuation:** $1B peak (Oct 2022 Series A); current undisclosed
- **Funding:** ~$181M+ total; Coatue, Lightspeed, Greycroft, O'Shaughnessy Ventures, Sean Parker
- **Revenue:** ~$50M (2024 est.); triple-digit growth reported; debt eliminated under Akkaraju
- **Employees:** ~170 (2024, post-layoffs)
- **Board:** Sean Parker (Executive Chairman), James Cameron (film director)
- **Status:** Privately held; stabilized after 2024 leadership crisis

## Strategy
Primarily an image/audio generation company that also develops language models. Core differentiator: open-weight model philosophy — democratized AI image generation via Stable Diffusion. Multi-modal coverage: image → video → audio → 3D → text. Enterprise focus under Akkaraju with partnerships in entertainment (film/TV), advertising, and music. Getty lawsuit victory (Nov 2025) established important legal precedent for AI training data.

## Product Portfolio (2026)

| Product | Type | Notes |
|---------|------|-------|
| **Stable Diffusion 3.5** | Image generation | Flagship; Large (8B), Large Turbo, Medium variants; Oct 2024 |
| **Stable Diffusion 3** | Image generation | MMDiT architecture; improved text rendering |
| **Stable Video 4D (SV4D)** | Video/4D | Image-to-4D generation; SV4D 2.0 for real-world video |
| **Stable Video Diffusion** | Video | Image-to-video (14 frames); open-weight |
| **Stable Audio 2.5** | Audio | Enterprise-grade; Arm-optimized for mobile |
| **Stable LM 2** | Language | Decoder-only; 1.6B compact variant |
| **Stable Code** | Code generation | Multi-language support; developer workflows |
| **SPAR3D / Fast 3D** | 3D generation | 3D reconstruction and asset generation |

## Developer Platform
- RESTful API: api.stability.ai/v1
- Endpoints for image, video, audio, and text generation
- Enterprise-grade SLAs
- Integration with AWS, Microsoft Azure
- Self-service developer portal

## Getty Images Lawsuit: Victory (Nov 2025)
Landmark UK High Court ruling — first AI copyright case to reach trial:
- **Copyright claims:** Dismissed — model weights ≠ "infringing copies" under UK law
- **Trademark claims:** Extremely narrow finding — only 2 instances across all versions
- **Significance:** Established that training on copyrighted data does not automatically constitute secondary infringement; model weights are not copies of training data
- **US case:** Still ongoing in Delaware federal court (separate proceeding)

## Leadership History
| Date | Event |
|------|-------|
| 2019 | Founded by Mostaque, Laforte, Hodes |
| Oct 2022 | $101M Series A at $1B valuation; Stable Diffusion released |
| Jul 2023 | Cyrus Hodes lawsuit (alleged fraud over 15% stake) |
| Feb 2023 | Getty Images files copyright suit |
| Mar 2024 | Emad Mostaque resigns as CEO |
| Apr 2024 | 10% staff layoffs; interim co-CEOs appointed |
| Jun 2024 | Prem Akkaraju named CEO; $80M+ funding closed |
| Sep 2024 | James Cameron joins Board |
| Nov 2025 | Getty lawsuit victory in UK High Court |

## Key Partnerships

| Partner | Nature |
|---------|--------|
| **Electronic Arts (EA)** | Generative AI in game development workflows |
| **WPP** | Advertising and marketing applications |
| **Universal Music Group** | Music and audio generation |
| **Warner Music Group** | Audio generation, music industry |
| **AWS** | Cloud infrastructure and model hosting |
| **Microsoft Azure** | Cloud services and enterprise deployment |
| **Arm** | Mobile optimization of Stable Audio (Mar 2025) |

## Strengths
- Market leader in open-weight image generation (Stable Diffusion democratized AI art)
- Multi-modal coverage: image, video, audio, 3D, text — broadest portfolio among image-focused labs
- Open-weight philosophy creates massive community ecosystem (thousands of fine-tunes on Hugging Face)
- Getty lawsuit victory provides legal confidence and industry precedent
- High-profile board connections (Sean Parker, James Cameron) signal entertainment ambitions
- Enterprise partnerships across gaming, advertising, music industries
- Stable financial position under Akkaraju (debt eliminated, triple-digit growth)

## Weaknesses
- Language models are secondary to diffusion models (Stable LM 2 is 1.6B — much smaller than frontier LLMs)
- History of financial instability and near-collapse (2024 crisis)
- Founder disputes and leadership turbulence damaged reputation
- Black Forest Labs (founded by ex-Stability researchers) competes directly with FLUX.1 models
- US Getty lawsuit still ongoing — legal uncertainty remains
- Revenue (~$50M) still modest relative to capital raised (~$181M)
- Employee count reduced to ~170 post-layoffs — limited scale vs. hyperscaler competitors
- Competitive pressure from Midjourney (consumer), Adobe Firefly (enterprise), Google Imagen

## Competitive Landscape
Competes with Midjourney (closed model, high aesthetic quality), OpenAI DALL-E 3, Google Imagen 3, Adobe Firefly (commercially safe training data), Runway (video focus), Black Forest Labs FLUX.1 (ex-Stability team). Stability's differentiation: open-weight availability, multi-modal breadth, enterprise API platform.

## Recent Developments
- Nov 2025: Getty Images lawsuit victory in UK High Court
- Nov 2025: Stable Audio partnership with Arm for mobile optimization
- Oct 2024: Stable Diffusion 3.5 released (Large, Large Turbo, Medium)
- Sep 2024: James Cameron joins Board of Directors
- Jun 2024: Prem Akkaraju appointed CEO; company stabilized, debt eliminated

[[google-gemini]] · [[meta-llama]] · [[openai]] · [[runway]] · [[adobe-firefly]]
