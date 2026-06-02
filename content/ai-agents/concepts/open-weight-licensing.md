---
confidence: high
created: '2026-06-02T00:00:00.000Z'
sources: []
tags:
  - licensing
  - open-weight
  - open-source
  - legal
  - apache
  - mit
  - llama
title: Open-Weight Licensing
type: concept
updated: '2026-06-02T00:00:00.000Z'
---
# Open-Weight Licensing

Open-weight licensing governs the legal terms under which AI model weights are made available to the public. Unlike open-source software licenses, open-weight licenses must address unique concerns around AI models — including acceptable use restrictions, commercial deployment terms, liability for model outputs, and the distinction between releasing weights versus releasing full training infrastructure. The 2026 licensing landscape features a spectrum from permissive (Apache 2.0, MIT) to restricted (Community Licenses, custom terms), with significant implications for who can use models and how.

---

## Definition

**Open-weight** models make their trained parameters (weights) publicly available for download and use. This is distinct from **open-source**, which traditionally implies access to the full training code, data, and reproducibility instructions. An open-weight model may have restricted usage terms even if its weights are freely downloadable. The term "open-weight" has become the standard descriptor for models like Llama, Qwen, Mistral, and DeepSeek that publish weights under various license terms.

## Open-Weight vs Open-Source

| Aspect | Open-Source | Open-Weight |
|--------|------------|-------------|
| **Weights available** | Yes | Yes |
| **Training code** | Yes | Sometimes |
| **Training data** | Yes | Rarely |
| **Reproducibility** | Full | Partial |
| **Commercial use** | Generally allowed | Depends on license |
| **Derivative models** | Allowed | Depends on license |

The **Open Source Initiative (OSI)** definition of open source does not perfectly map to AI models. In 2024, the OSI clarified that truly open-source AI should include training data and code, not just weights. Most "open-weight" models fall short of this standard.

## Major License Types

### Apache 2.0

The most permissive license in the open-weight ecosystem. Allows commercial use, modification, distribution, and patent rights with minimal restrictions.

**Models under Apache 2.0:**
- **Qwen series** (Alibaba): Qwen3, Qwen 3.7, and all derivatives are Apache 2.0
- **Mistral series** (Mistral AI): Mistral 7B, Mixtral, and most open releases
- **DeepSeek series**: R1 distilled models (1.5B–70B) released under Apache 2.0
- **Gemma series** (Google): Gemma and Gemma 2 weights under modified Apache 2.0
- **Phi series** (Microsoft): Phi-3, Phi-4 under MIT/Apache 2.0

**Key terms**: No acceptable use restrictions; no user-count limits; no revenue caps; full commercial freedom.

### MIT License

The most permissive open-source license, even simpler than Apache 2.0 (no patent clause).

**Models under MIT:**
- **DeepSeek** (base models): Original DeepSeek base models use MIT
- **Microsoft Phi**: All Phi models released under MIT
- **Various community models**: Many fine-tunes and merges use MIT

**Key terms**: Minimal restrictions — just preserve copyright notice; full commercial and modification rights.

### Meta Llama Community License

Meta's custom license, the most widely used open-weight license by model count. It sits between permissive and restricted.

**Llama Community License terms:**
- **Free for most uses**: Research, commercial deployment, and internal use
- **User cap**: Organizations with >700 million monthly active users must request a special license
- **Acceptable Use Policy**: Restrictions on illegal activity, harmful content generation
- **No restrictions on derivatives**: Fine-tunes and derivatives can use different licenses
- **Llama 4** (2025–2026): Updated terms with clearer commercial permissions

**Impact**: The 700M MAU cap affects only the largest tech companies (Meta, Google, Microsoft, Apple, Amazon, TikTok). Everyone else gets full access.

### Restricted Open-Weight Licenses

Some providers use more restrictive terms:

- **Stability AI**: Custom license with commercial revenue caps
- **Cohere Command R**: Research and evaluation use; commercial requires separate agreement
- **xAI Grok**: Weights available but with usage restrictions and API-first commercial model

## Licensing Landscape 2026

### Industry Trends

1. **Shift toward permissiveness**: Qwen (Apache 2.0) and DeepSeek (Apache 2.0/MIT) have pressured competitors to relax terms. Mistral moved from BSL to Apache 2.0 for new releases.

2. **Llama's influence**: Meta's Community License has become the de facto standard for large model releases, balancing openness with protection against the largest competitors.

3. **Chinese model providers**: Alibaba (Qwen), DeepSeek, and 01.AI have predominantly chosen Apache 2.0 or MIT, making their models the most commercially accessible.

4. **US provider caution**: Anthropic, OpenAI, and Google keep their frontier models closed-weight. Their smaller models (Haiku, GPT-oss, Gemma) use restricted or permissive licenses respectively.

5. **OpenAI gpt-oss** (August 2025): OpenAI released gpt-oss-120b and gpt-oss-20b as open-weight reasoning models, marking a significant shift in their previously closed approach.

### License Comparison Matrix

| License | Commercial Use | Derivatives | User Cap | AUP Restrictions | Examples |
|---------|---------------|-------------|----------|-----------------|----------|
| **Apache 2.0** | ✅ Yes | ✅ Yes | ❌ None | ❌ None | Qwen, DeepSeek distills, Mistral |
| **MIT** | ✅ Yes | ✅ Yes | ❌ None | ❌ None | Phi, DeepSeek base |
| **Llama Community** | ✅ Yes | ✅ Yes | 700M MAU | ✅ Yes | Llama 3, Llama 4 |
| **BSL (Business Source)** | ❌ Time-limited | ⚠️ Restricted | Varies | ✅ Yes | Older Mistral |
| **Custom Restricted** | ⚠️ Limited | ⚠️ Restricted | Varies | ✅ Yes | Stability AI, xAI |

## Practical Implications

### For Developers

- **Apache 2.0/MIT models**: Safest for commercial products — no license review needed
- **Llama models**: Safe for most businesses; check MAU threshold if serving at massive scale
- **Restricted models**: Require legal review before commercial deployment

### For Enterprises

- **Self-hosting**: Open-weight models enable full data sovereignty — no API calls leave your infrastructure
- **Fine-tuning**: Most open-weight licenses allow fine-tuning; derivatives may need to comply with original license
- **Indemnification**: Open-weight licenses typically provide no liability protection; enterprises must self-insure

### For Researchers

- **Reproducibility**: Open-weight enables independent evaluation and benchmarking
- **Modification**: Permissive licenses allow architecture modifications, weight merging, and experimental fine-tuning
- **Publication**: No restrictions on publishing results from open-weight model research

## Recent Licensing Developments

- **DeepSeek R1 distills** (January 2025): All distilled models (1.5B–70B) released under Apache 2.0, catalyzing the open-weight reasoning ecosystem
- **Mistral license change** (2025): Moved from BSL to Apache 2.0 for newer releases, responding to competitive pressure
- **Meta Llama 4** (2025): Updated Community License with clearer commercial terms and maintained 700M MAU cap
- **OpenAI gpt-oss** (August 2025): First open-weight release from OpenAI, using Apache 2.0
- **Alibaba Qwen 3.7** (May 2026): Continued Apache 2.0 licensing across the full model family
- **EU AI Act compliance**: Open-weight providers must ensure licensing terms align with EU AI Act transparency requirements

## Best Practices

1. **Always verify the specific license** — license terms can vary between model versions from the same provider
2. **Check derivative obligations** — fine-tuning an Apache 2.0 model produces a derivative with its own licensing considerations
3. **Monitor license changes** — providers may change license terms for new model releases
4. **Document your model's license** — maintain a bill of materials for all models used in production
5. **Consider downstream impact** — if your customers will redistribute your model-based product, ensure the license permits it

## Related Concepts

- [[distillation]] — distilled models inherit licensing from both base model and training data
- [[kv-cache-optimization]] — open-weight models enable self-hosted KV cache optimization with full control
- [[cost-optimization]] — open-weight models eliminate per-token API costs in favor of infrastructure costs
- [[speculative-decoding]] — open-weight models can serve as draft models without licensing restrictions
