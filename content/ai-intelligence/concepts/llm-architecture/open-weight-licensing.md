---
title: Open-Weight Licensing
created: 2026-06-01
updated: 2026-06-02
type: concept
tags:
  - open-source
  - compliance
  - licensing
sources:
  - raw/articles/llm-provider-deepseek-2026.md
  - raw/articles/llm-provider-meta-llama-2026.md
  - raw/articles/llm-provider-mistral-2026.md
  - raw/articles/llm-provider-alibaba-qwen-2026.md
  - raw/articles/llm-provider-xai-grok-2026.md
  - raw/articles/llm-provider-stability-ai-2026.md
  - raw/articles/llm-provider-stepfun-2026.md
  - raw/articles/llm-provider-zhipu-ai-2026.md
  - raw/articles/llm-provider-microsoft-phi-2026.md
  - raw/articles/llm-provider-minimax-2026.md
  - raw/articles/llm-provider-cohere-2026.md
  - raw/articles/llm-provider-openai-2026.md
  - raw/articles/llm-provider-moonshot-ai-2026.md
confidence: high
---

# Open-Weight Licensing

## Overview

Open-weight models release model weights for download and modification but may restrict commercial use. True open-source models use permissive licenses (Apache 2.0, MIT) allowing unrestricted use. The landscape is diverse, ranging from fully open to heavily restricted.

## License Spectrum

| License | Restriction Level | Commercial Use | Redistribution | Training Derivatives | Examples |
|---------|------------------|---------------|---------------|--------------------|----------|
| MIT | None | ✅ Yes | ✅ Yes | ✅ Yes | DeepSeek V4, Kimi K2, Phi-3.5 |
| Apache 2.0 | None | ✅ Yes | ✅ Yes | ✅ Yes | Mistral Small 4, Gemma 3.5 |
| Llama 4 Community | Moderate | ✅ Yes (≤700M MAU) | ✅ Yes | ⚠️ Restricted | Llama 4 Maverick, Scout |
| Qwen Community | Moderate | ✅ Yes (≤100M MAU) | ✅ Yes | ✅ Yes | Qwen3.6-35B-A3B |
| Grok Non-Commercial | Restricted | ❌ No | ⚠️ Limited | ❌ No | Grok 4.3 weights |
| Stability AI | Restricted | ✅ Yes (revenue ≤$1M) | ✅ Yes | ✅ Yes | Stable Image 3.5 |

## Provider Licensing (Mid-2026)

| Provider | License Model | Commercial Use | Notes |
|----------|--------------|---------------|-------|
| DeepSeek | MIT License | ✅ Yes | Most open of frontier models; V4 Pro and Flash fully open |
| Meta | Llama 4 Community License | ✅ Yes (≤700M MAU) | Free for nearly all companies; >700M MAU requires license |
| Mistral | Apache 2.0 (Small 4) / Community (Large 3) | ✅ Yes | Most open models under Apache 2.0 |
| Alibaba | Qwen3.7 Community License | ✅ Yes (≤100M MAU) | Similar to Llama but lower MAU threshold |
| Microsoft | MIT (Phi-3.5 variants) | ✅ Yes | Phi designed for unrestricted local deployment |
| Moonshot | Modified MIT (Kimi K2) | ✅ Yes | Open-source with minor restrictions |
| xAI | Custom Non-Commercial | ❌ No | Grok 4.3 weights viewable but not commercially usable |
| Zhipu AI | MIT (GLM-4.5) / Enterprise (GLM-5) | ✅ Yes (open variants) | GLM-4.5 fully open; GLM-5 enterprise only |
| StepFun | Custom open license | ⚠️ Review | Step-3.5-Flash available for research |
| MiniMax | Custom license | ⚠️ Review | M2 available for research use |
| Cohere | Command R+ open weights | ✅ Yes | Command A+ weights available for research |
| NVIDIA | Nematron community license | ✅ Yes | Nematron-5-22B available |
| Stability AI | Stability Community License | ✅ Yes (≤$1M revenue) | Revenue threshold restriction |
| Together AI | Hosts all open-weight models | N/A | Platform, not model creator |

## Open Debates

- **"Open weight" vs "open source"**: Most frontier models are open-weight, not open-source. OSI definition requires no usage restrictions.
- **MAU thresholds**: Are 700M MAU limits effectively unrestricted for all but Meta-scale companies?
- **Training derivatives**: Can you train on an open-weight model's outputs? License terms vary.
- **Chinese open models**: DeepSeek MIT license vs Alibaba Qwen community license — different philosophies on openness.

## Related

- [[distillation]] — Distilled models inherit license restrictions from teacher
- [[quantization]] — Quantized weights are derivative works under most licenses
- [[moE-architecture]] — MoE routing patterns may be covered by license terms
