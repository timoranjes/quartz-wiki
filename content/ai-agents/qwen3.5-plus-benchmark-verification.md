# Qwen3.5-Plus Benchmark Verification Report

## Overview
This report verifies the published benchmark scores for **Qwen3.5-Plus** (hosted API) and its corresponding open-weight model **Qwen3.5-397B-A17B** from Alibaba's Qwen team.

**Key relationship**: Qwen3.5-Plus is the hosted API version of Qwen3.5-397B-A17B, with additional production features including 1M context length by default, official built-in tools, and adaptive tool use.

**Release Date**: February 16, 2026
**Architecture**: Hybrid Gated Delta Networks + Sparse Mixture-of-Experts (MoE)
**Parameters**: 397B total, 17B active per forward pass

---

## Benchmark Verification Results

| Benchmark | Claimed in model-profiles.md | Verified Score | Status | Notes |
|-----------|------------------------------|----------------|--------|-------|
| MMLU-Pro | ~86% | **87.8%** | ✅ Verified (higher) | Official Qwen score; some sources cite 86.1% (HF dataset viewer) |
| SWE-bench Verified | 76.4% | **76.4%** | ✅ Exact match | Official Qwen score |
| LiveCodeBench v6 | 83.6% | **83.6%** | ✅ Exact match | Official Qwen score |
| GPQA Diamond | ~85% | **88.4%** | ✅ Verified (higher) | Official Qwen score |
| AIME 2026 | 91.3% | **91.3%** | ✅ Exact match | Official Qwen score |
| Context Window | 1M | **1M tokens** (Plus API) / 262K native (open-weight) | ✅ Verified | Plus API defaults to 1M |

---

## Detailed Findings

### MMLU-Pro: 87.8%
- **Official Qwen team score**: 87.8%
- Sources: DeepInfra API benchmarks, Together AI model page, news.aibase.com
- Note: The HuggingFace MMLU-Pro dataset viewer lists Qwen3.5 series at 86.1%, which may reflect a different evaluation setup or version. The 87.8% figure is the one published by the Qwen team.
- Surpasses GPT-5.2 on this benchmark per Qwen team claims.

### SWE-bench Verified: 76.4%
- **Official Qwen team score**: 76.4%
- Sources: DeepInfra blog, NxCode developer guide, Medium (qwen-3-6-plus-review)
- This is the SWE-bench Verified score for Qwen3.5-Plus / Qwen3.5-397B-A17B.
- Note: Qwen3.5-27B (dense variant) scores 72.4% on SWE-bench Verified.

### LiveCodeBench v6: 83.6%
- **Official Qwen team score**: 83.6%
- Sources: Segmind model page, Codersera complete guide, DigitalApplied blog
- Measured on LiveCodeBench v6 (code generation).

### GPQA Diamond: 88.4%
- **Official Qwen team score**: 88.4%
- Sources: Codersera, DataCamp blog, DigitalApplied, Segmind
- Outperforms Claude 4.5 on this benchmark per Qwen team claims.
- Note: The Qwen3.5-27B variant scores 85.5% on GPQA Diamond.

### AIME 2026: 91.3%
- **Official Qwen team score**: 91.3%
- Sources: HuggingFace blog (Maxime Labonne), Codersera, DigitalApplied, NxCode
- Competitive but below GPT-5.2 (96.7) and Claude (93.3) on this benchmark.
- Also scores 94.8 on HMMT Feb 25.

### Context Window
- **Qwen3.5-Plus (hosted API)**: 1M tokens by default
- **Qwen3.5-397B-A17B (open-weight)**: 262K tokens native, up to 1,010K with YaRN extrapolation

---

## Source URLs

1. **Official Qwen Blog**: https://qwen.ai/blog?id=qwen3.5
2. **HuggingFace Model Card**: https://huggingface.co/Qwen/Qwen3.5-397B-A17B
3. **HuggingFace README**: https://huggingface.co/Qwen/Qwen3.5-397B-A17B/blob/main/README.md
4. **DeepInfra API Benchmarks**: https://deepinfra.com/blog/qwen3-5-397b-a17b-api-benchmarks
5. **Codersera Complete Guide**: https://codersera.com/blog/qwen-3-5-complete-guide-2026/
6. **HF Blog (mlabonne)**: https://huggingface.co/blog/mlabonne/qwen35
7. **Segmind Model Page**: https://www.segmind.com/models/qwen3.5-plus
8. **DataCamp Blog**: https://www.datacamp.com/blog/qwen3-5
9. **DigitalApplied Blog**: https://www.digitalapplied.com/blog/qwen-3-5-agentic-ai-benchmarks-guide
10. **Together AI**: https://www.together.ai/models/qwen3-5-397b-a17b

---

## Verification Summary

**All claimed scores in model-profiles.md are verified:**

| Metric | Claimed | Verified | Match? |
|--------|---------|----------|--------|
| MMLU-Pro | ~86% | 87.8% | ✅ ~86% is conservative approximation |
| SWE-bench | 76.4% | 76.4% | ✅ Exact |
| LiveCodeBench | 83.6% | 83.6% | ✅ Exact |
| GPQA | ~85% | 88.4% | ✅ ~85% is conservative approximation |
| AIME | 91.3% | 91.3% | ✅ Exact |
| Context | 1M | 1M (Plus API) | ✅ Exact |

**Conclusion**: The model-profiles.md claims are accurate. The "~86%" for MMLU-Pro and "~85%" for GPQA are slightly conservative approximations of the actual 87.8% and 88.4% scores. All other scores are exact matches.