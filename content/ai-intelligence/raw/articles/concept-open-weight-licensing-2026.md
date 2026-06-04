---
title: Open-Weight Licensing
researched: 2026-06-05
sources:
  - https://medium.com/ai-simplified-in-plain-english/navigating-the-ai-licensing-labyrinth-truly-open-vs-restricted-open-weight-models-89de5c2e649d
  - https://github.com/xigh/open-weight-models
  - https://onyx.app/insights/best-open-source-llms-2026
  - https://www.reddit.com/r/LocalLLaMA/comments/1mij7fh/list_of_openweight_models_with_unmodified/
---
# Open-Weight Licensing

## Overview
"Open-weight" means model weights are publicly available, but this does not equal "open-source." The licensing landscape creates a spectrum from truly open (OSI-compliant) to restricted "source-available" models. Understanding these distinctions is critical for compliance, commercial deployment, and innovation strategy.

## Licensing Spectrum

| Category | Source Code | Weights | Commercial Use | Modifications | OSI-Compliant? | Examples |
|----------|-------------|---------|----------------|---------------|----------------|----------|
| **Open-Source** | ✅ Full | ✅ Full | ✅ Unrestricted | ✅ Unrestricted | ✅ Yes | DeepSeek R1 (MIT), Mixtral 8x7B (Apache 2.0), GPT-OSS (Apache 2.0) |
| **Open-Weight** | ⚠️ May be restricted | ✅ Available | ⚠️ Restricted | ⚠️ Restricted | ❌ No | Llama 2/3/4, Mistral Large, Stable Diffusion |
| **Source-Available** | ✅ Available | ✅ Available | ❌ Restricted | ❌ Restricted | ❌ No | Claude (proprietary), Gemini (proprietary) |

## Truly Open-Source Licenses (OSI-Compliant)

### MIT License
- Minimal conditions: requires only copyright/license notice
- Highly permissive: commercial use, sublicensing, proprietary integration
- No explicit patent grant
- Examples: DeepSeek R1, MiniMax M2.7 (verify), GPT-OSS (Apache 2.0)

### Apache 2.0 License
- Explicit patent grant
- Clear attribution requirements
- Requires disclosure of modifications
- Trademark protection
- Examples: Mistral AI's Mixtral 8x7B, Gemma 4 series, Qwen3.5 series

## Restricted "Open-Weight" Licenses

### Meta Llama Community License
- Commercial use capped at 700M monthly active users
- Acceptable Use Policy (AUP) bans harmful/illegal use
- Geographical restrictions (e.g., EU limitations for Llama 4 multimodal)
- **Not OSI-compliant** due to user-count and use-based restrictions

### Mistral Research / Commercial License
- Non-commercial use requires research license
- Production use requires separate commercial agreement
- **Not OSI-compliant**

### DeepSeek Model License
- MIT-licensed code, but model weights under restrictive license
- Prohibits military use, harmful content generation
- **Not OSI-compliant** due to use-based restrictions

### Modified MIT Licenses (Revenue/MAU Caps)
- Mistral Medium 3.5, Kimi K2.5, MiniMax M2.5 have commercial restrictions
- Revenue thresholds or 100M MAU caps
- Not interchangeable with standard Apache 2.0/MIT

## Responsible AI Licenses (RAILs)
- Balance openness with ethical responsibility
- Include behavioral restrictions (no military use, no hate speech)
- Examples: CreativeML OpenRAIL-M (Stable Diffusion)
- **Not OSI-compliant** due to "field of endeavor" restrictions

## Motivations Behind Licensing Strategies

| Strategy | Rationale | Examples |
|----------|-----------|----------|
| **Foster Research & Ecosystem** | Encourage academic collaboration, standardization, innovation | Meta's Llama, Mistral open-weight |
| **Control Commercial Exploitation** | Monetize high-scale deployments while allowing early-stage openness | Llama's 700M-user threshold |
| **Mitigate Brand & Legal Risk** | Prevent misuse that could damage reputation | AUPs, RAILs |
| **Ethical Guardrails** | Proactively prevent harmful applications | CreativeML OpenRAIL-M, DeepSeek use limits |

## Key Open-Weight Models by License (2026)

### Apache 2.0 (Fully Open)
- Gemma 4 31B (Google) — GPQA 84.3, MMLU-Pro 85.2
- Gemma 4 12B Unified — encoder-free multimodal, GPQA 78.8
- Qwen3.5-9B — GPQA 81.7 (impressive for 9B)
- GPT-OSS-120B — OpenAI open-weight, Apache 2.0
- Step-3.5-Flash — 11B/196B MoE, SWE-bench 74.4%
- Mellum 2 12B-A2.5B (JetBrains) — LCB v6 69.9, RLVR fine-tuned

### MIT (Fully Open)
- DeepSeek R1/V3 — reasoning-focused MoE
- DeepSeek-V4-Flash — 13B/284B MoE, 1M native context

### Restricted (Open-Weight, Not Open-Source)
- Llama 4 series (Meta) — 700M MAU cap, AUP, EU restrictions on multimodal
- Mistral Large series — research/commercial license split
- Kimi K2.5 (Moonshot) — modified MIT with 100M MAU cap
- MiniMax M2.5 — modified MIT with revenue thresholds

## Actionable Guidance for Practitioners

### Do:
- Always read the license, not just the headline ("open-weight" ≠ "open-source")
- Verify OSI compliance if full freedom is needed (especially commercial products)
- Check for AUPs, commercial thresholds, and geographical clauses
- Tag models appropriately: open-source = MIT/Apache 2.0; open-weight = custom license

### Don't:
- Assume "open" means "unrestricted"
- Deploy models in production without license review
- Ignore ethical clauses — misuse can cause reputational harm

## Key Facts
1. "Open-weight" means weights are available but does not guarantee open-source freedoms — most open-weight models have usage restrictions.
2. Only MIT and Apache 2.0 licensed models are truly OSI-compliant open-source.
3. Meta's Llama Community License caps commercial use at 700M monthly active users and includes Acceptable Use Policy restrictions.
4. Responsible AI Licenses (RAILs) include behavioral restrictions and are not OSI-compliant.
5. Modified MIT licenses with revenue or MAU caps (Mistral Medium 3.5, Kimi K2.5, MiniMax M2.5) are not interchangeable with standard MIT/Apache 2.0.
6. Curated lists like open-weight-models on GitHub help practitioners identify commercially exploitable models without geographic restrictions.

## Sources
