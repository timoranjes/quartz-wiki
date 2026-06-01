---
domain: llm-providers
type: provider
tags: [provider/llm-lab, provider/us, provider/closed-source]
aliases: [Claude, Anthropic]
created: 2026-06-01
---
# Anthropic

## Overview
- **Founded:** 2021
- **CEO:** Dario Amodei
- **HQ:** San Francisco, CA
- **Key Products:** Claude (chat), Claude API, MCP protocol, Computer Use
- **Platform:** platform.anthropic.com
- **Funding:** >$10B raised; backed by Google, Amazon, Spark Capital
- **Philosophy:** Safety-first AI, Constitutional AI, transparency

## Strategy
Safety-conscious alternative with strong alignment research. MCP protocol creator. Multi-cloud availability (AWS, GCP, Azure, Anthropic API).

## Model Lineup (2026)

| Model | Context | Input $/1M | Output $/1M | Release |
|-------|---------|-----------|------------|---------|
| **Claude Opus 4.8** | 1M | $5.00 | $25.00 | May 2026 |
| **Claude Opus 4.7** | 1M | $5.00 | $25.00 | Apr 2026 |
| **Claude Sonnet 4.6** | 1M (beta) | $3.00 | $15.00 | Feb 2026 |
| **Claude Haiku 4.5** | 200K | $1.00 | $5.00 | 2025 |

## Key Benchmarks (Opus 4.8)
- SWE-bench Pro: **64.3%** (highest)
- SWE-bench Verified: **87.6%** (Opus 4.7)
- MCP Atlas: **77.3%** (Opus 4.7)
- GPQA Diamond: **92.0%**
- Humanity's Last Exam: **45.7%**
- τ²-Bench Telecom: **94.4%**

## API & Ecosystem
- Messages API (v2023-06-01+)
- Extended thinking: low/medium/high/xhigh/max effort levels
- Prompt caching (up to 90% savings)
- Computer Use (beta)
- MCP protocol (industry standard for tool connections)
- File System Memory (persistent across sessions)
- Hosting: Anthropic API, AWS Bedrock, GCP Vertex, Azure, OpenRouter

## Strengths
- Safety & alignment leader (Constitutional AI)
- MCP protocol creator (industry standard)
- Best SWE-bench performance
- Computer Use pioneer
- Prompt caching implementation
- Extended thinking with granular effort control
- Multi-cloud availability (broadest hosting)

## Recent Developments
- May 2026: Opus 4.8 (Dynamic Workflows + Effort Control)
- Apr 2026: Opus 4.7 (1M context, 3.75 MP vision, xhigh effort)
- Feb 2026: Sonnet 4.6 (1M context beta, 70% more token-efficient)

[[openai]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
