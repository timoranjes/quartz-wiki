---
title: Cohere
created: 2026-06-02
updated: 2026-06-02
type: provider
tags: [provider, lab, model, rag, embeddings, reranking, multilingual, tool-use, pricing, api, closed, enterprise, cloud-platform]
sources: [raw/articles/llm-provider-cohere-2026.md]
confidence: 0.95
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge enterprise">Enterprise</span>
    <span class="provider-badge ca">🇨🇦 Toronto</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge rag"><span class="cap-icon">📚</span> RAG</span>
    <span class="capability-badge reranking"><span class="cap-icon">📊</span> Reranking</span>
    <span class="capability-badge tool-use"><span class="cap-icon">🔧</span> Tool Use</span>
    <span class="capability-badge multilingual"><span class="cap-icon">🌐</span> Multilingual</span>
  </div>
</div>

# Cohere

## Overview

Cohere is a Canadian AI company founded in 2019 by Aidan Gomez (CEO, co-author of the "Attention Is All You Need" transformer paper), Nick Frosst, and Ivan Zhang — all former Google Brain researchers. Headquartered in Toronto with offices in Palo Alto, London, and Tokyo, Cohere was built from day one as an enterprise-first AI provider, distinct from consumer-facing competitors like [[openai]].

As of mid-2026, Cohere employs ~400-500+ people and is valued at ~$10B+. Strategic investors include [[nvidia]], Oracle, Salesforce, and In-Q-Tel (CIA's venture arm), reflecting its importance to enterprise and government AI infrastructure. The company's core strengths lie in RAG (retrieval-augmented generation), embeddings, reranking, and multilingual support across 70-100+ languages. Cohere maintains deep cloud partnerships with [[anthropic]] peer platforms AWS Bedrock, Azure AI Foundry, and Oracle GenAI.

## Model Lineup

| Model | API ID | Context | Pricing in/out (per 1M) | Type |
|-------|--------|---------|-------------------------|------|
| **Command A+** | `command-a-plus-05-2026` | 128K tokens | TBD | Flagship MoE, vision, reasoning |
| **Command A** | `command-a-03-2025` | 256K tokens | $2.50 / $10.00 | Highest single-model performance |
| **Command R+** | `command-r-plus-08-2024` | 128K tokens | $2.50 / $10.00 | Enterprise RAG, tool use |
| **Command R** | `command-r-08-2024` | 128K tokens | $0.15 / $0.60 | Mid-tier conversational |
| **Command R7B** | `command-r7b-12-2024` | 128K tokens | $0.0375 / $0.15 | Small, cost-optimized |
| **Aya Vision** | — | — | — | 32B param, 70+ languages, multimodal |

Specialized variants include Command A Translate (23 languages, SOTA translation), Command A Reasoning (256K context, 23 languages), and Command A Vision (OCR, charts, tables).

### Embed & Rerank Models

| Model | Pricing | Modality |
|-------|---------|----------|
| Embed v3 English | $0.10 / 1M tokens | Text |
| Embed v3 Multilingual | $0.10 / 1M tokens | 100+ languages |
| Embed v4.0 | TBD | Text + images + PDFs |
| Rerank v3 | $2 / 1M searches | 100+ languages |

## Benchmarks

Command A offers solid instruction following and strong RAG capabilities but trails [[openai]] GPT-5 and [[anthropic]] Claude on general reasoning benchmarks. Cohere's differentiating strengths:

| Capability | Assessment | Notes |
|------------|------------|-------|
| RAG / Retrieval | **Best-in-class** | Native citation and grounding in Command models |
| Embedding quality | **Top-tier** | High MTEB rankings, multilingual excellence |
| Reranking | **Best-in-class** | High accuracy, fast latency, 100+ languages |
| Reasoning | Modest | Behind dedicated reasoning models |
| Coding | Modest | Not coding-optimized |
| Tool use | Strong | Native tool calling for agents |

## API Ecosystem

- **Endpoints:** `/chat`, `/embed`, `/embed-jobs`, `/rerank`, `/classify`, `/summarize`, `/detect-language`
- **Python SDK:** `cohere.ClientV2` with OpenAI-style chat interface
- **Cloud Platforms:** Available via Amazon Bedrock, Azure AI Foundry, Oracle GenAI, Amazon SageMaker
- **Features:** Tool use, RAG with native citations, streaming, multi-turn, system prompts, vision, structured output (JSON mode)
- **Private Deployment:** ~20% of revenue from custom model deployment within customer infrastructure

Pricing principles: pay-as-you-go with no upfront costs, tiered enterprise contracts with volume discounts, custom pricing for high-volume clients.

## Strengths / Weaknesses

**Strengths:**
- **RAG leadership:** Best-in-class embeddings, reranking, and RAG-native chat models
- **Enterprise trust:** SOC 2 compliance, zero-retention policies, strong data governance
- **Cloud partnerships:** Deep integration with AWS, Azure, and Oracle — accessible through existing cloud infrastructure
- **Multilingual capability:** 70-100+ language support, Aya family specializes in underrepresented languages
- **API simplicity:** Clean, well-documented API with purpose-built endpoints
- **Private deployment:** Custom model deployment within customer infrastructure

**Weaknesses:**
- **Raw performance gap:** Command models trail GPT-5 and Claude Opus on general benchmarks
- **Premium pricing:** Command A/R+ at $2.50/$10 is high relative to capability tier
- **No open weights:** Models are closed-weight, unlike Meta/Mistral
- **Limited coding focus:** Not optimized for coding tasks
- **Output limits:** Some models capped at 4K-8K output tokens
- **Smaller model range:** Fewer specialized models vs. competitors

## Key Relationships

- **Nvidia** — Strategic investor and Series D participant; [[nvidia]] GPU infrastructure for training
- **Oracle** — Series C/D investor; Oracle GenAI platform integration
- **Salesforce** — Strategic investor; enterprise CRM AI integration
- **In-Q-Tel** — CIA's venture arm; government AI infrastructure relevance
- **Amazon / Microsoft** — Deep cloud platform partnerships (Bedrock, Azure AI Foundry)

## Recent Developments

**Command A+ launch (May 2026):** Cohere's first MoE model combining vision, reasoning, translation (23 languages), agentic tool use, 128K context with 64K output limit.

**Embed v4.0:** Latest generation embedding model with PDF support, mixed modality (text + images), improved multilingual performance.

**Aya Vision (2026):** 32B parameter multimodal multilingual model covering 70+ languages with text + image understanding; open-weight variants available.

**Funding growth:** Continued investment from strategic investors ([[nvidia]], Oracle, Salesforce); growing enterprise customer base; expanded private deployment offerings.

**Cloud expansion:** Models now available across all major cloud platforms — Amazon Bedrock, Azure AI Foundry, Oracle GenAI, and Amazon SageMaker for custom deployment.
