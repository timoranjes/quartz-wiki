---
title: "Financial Reasoning Benchmarks"
created: 2026-06-04
updated: 2026-06-20
type: entity
status: drafted
tags: ["finance/benchmark", "evaluation", "reasoning"]
sources: [raw/articles/ai-finance-financial-reasoning-2026.md]
---

# Financial Reasoning Benchmarks

## Overview

Benchmarks designed to evaluate LLMs on financial knowledge, reasoning, and decision-making tasks. Critical for selecting models for finance-specific applications.

## Key Benchmarks

| Benchmark | Scope | Metrics | Notes |
|-----------|-------|---------|-------|
| FinQA | Financial QA with calculations | Exact match, program accuracy | Multi-step numerical reasoning |
| ConvFinQA | Conversational financial QA | Answer accuracy | Multi-turn context |
| TAT-QA | Tabular + text financial QA | Exact match | SEC filings focus |
| FinanceBench | Real-world finance tasks | Task completion | 10-K analysis |
| MultiFin | Multi-domain finance | Accuracy | Covers banking, insurance, markets |
| CFLUE | Chinese financial NLP | Various tasks | A-share market focus |

## Emerging Benchmarks (2026)

- **BloombergGPT Evaluation** — proprietary financial language tasks
- **LLM-as-Financial-Analyst** — end-to-end research report generation
- **Regulatory Compliance Benchmark** — rule extraction and application

### AgentFinVQA: Auditable Financial Chart QA (June 2026)

**AgentFinVQA** (arXiv:2606.19782) addresses a gap: financial chart QA in regulated settings requires **auditability** and **on-premise deployability**, not just accuracy.

**Architecture**: Multi-agent pipeline decomposes each query into planning, OCR, legend grounding, visual inspection, and verification — recording every step in a traceable **Model Evaluation Packet (MEP)** per sample.

**Results on FinMME:**
- **+7.68 pp** over zero-shot baseline with proprietary backbone (Gemini-3 Flash: 71.24% vs. 63.56%)
- **+4.84 pp** with open-weights Qwen3.6-27B-FP8 served locally
- Verifier verdict serves as confidence signal: **68.2% vs. 55.6%** exact accuracy on confirmed vs. revised answers
- Enables human-in-the-loop review routing
- Error analysis: question misunderstanding, legend confusion, and extraction error account for ~2/3 of failures

**Key insight**: Auditable, on-premise financial chart QA is practical. Open-weights systems keep most accuracy gains while enabling full data residency.

## Model Performance Trends

- GPT-4 and Claude 3 lead on general financial reasoning
- Domain-specific fine-tuned models (BloombergGPT, FinLLM) outperform on narrow tasks
- Open-weight models (Llama 3, Qwen) competitive on structured financial QA
- Reasoning mode (extended thinking) significantly improves multi-step financial calculations

## Use Cases

- Model selection for financial AI products
- Compliance testing of LLM outputs
- Investment due diligence automation
- Regulatory filing analysis

## Cross-References

- [[evaluation-benchmarks]] — General LLM benchmarks
- [[ai-alpha-generation]] — Alpha generation applications
- [[earnings-call-analysis]] — Earnings call NLP
