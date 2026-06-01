---
domain: llm-providers
type: comparison
tags: [comparison/benchmarks, comparison/2026Q2]
aliases: [Benchmark Matrix, Performance Comparison]
created: 2026-06-01
---
# Benchmark Comparison — 2026 Q2

## Intelligence Index (Artificial Analysis)

| Model | Score | Rank |
|-------|-------|------|
| Claude Opus 4.8 | **61.4** | #1 |
| GPT-5.5 | 60.2 | #2 |
| Qwen3.7 Max | 56.6 | — |
| Grok 4.3 | 53.9 | — |
| DeepSeek V4-Pro | 51.5 | Better than 94% |
| Gemini 3.1 Pro | — | — |

## Coding Benchmarks

### SWE-bench Pro (Production Coding)
| Model | Score |
|-------|-------|
| Claude Opus 4.7 | **64.3%** |
| GPT-5.5 | 58.6% |
| Qwen3.7 Max | 60.6% |
| DeepSeek V4-Pro | 55.4% |
| Gemini 3.5 Flash | 55.1% |

### Terminal-Bench 2.0 (Agentic CLI)
| Model | Score |
|-------|-------|
| GPT-5.5 | **82.7%** |
| GPT-5.4 | — |
| Gemini 3.5 Flash | 76.2% |
| Qwen3.7 Max | 69.7% |
| DeepSeek V4-Pro | 67.9% |
| Claude Opus 4.7 | ~70% |

### SWE-bench Verified
| Model | Score |
|-------|-------|
| Claude Opus 4.7 | **87.6%** |
| Mistral Medium 3.5 | 77.6% |
| Qwen3.5 | 76.4% |
| DeepSeek V4-Pro | 80.6% (internal) |

## Reasoning Benchmarks

### GPQA Diamond (PhD Science)
| Model | Score |
|-------|-------|
| GPT-5.5 | **93.6%** |
| Qwen3.7 Max | 92.4% |
| Claude Opus 4.8 | 92.0% |
| DeepSeek V4-Pro | 88.8–90.1% |
| Llama 4 Maverick | 69.8% |

### ARC-AGI-2 (Abstract Reasoning)
| Model | Score |
|-------|-------|
| GPT-5.5 | **85.0%** |
| Gemini 3.1 Pro | 77.1% |
| Gemini 3.5 Flash | 72.1% |
| Claude Opus 4.7 | 68%+ |
| Claude Sonnet 4.6 | 58.3% |

### AIME (Math Competition)
| Model | Score |
|-------|-------|
| GPT-5.2 | **96.7%** |
| DeepSeek R1 v0528 | **87.5%** |
| Claude Opus 4.6 | 93.3% |
| Qwen3.5 | 91.3% |

## Tool Orchestration

### MCP Atlas
| Model | Score |
|-------|-------|
| Gemini 3.5 Flash | **83.6%** |
| Claude Opus 4.7 | **77.3%** |
| Claude Sonnet 4.6 | 69.5% |
| GPT-5.5 | 75.3% |

### τ²-Bench Telecom
| Model | Score |
|-------|-------|
| DeepSeek V4-Pro | **96.2%** |
| Claude Opus 4.8 | 94.4% |
| Qwen3.5 | 86.7% |

## Long Context

### MRCR v2 1M
| Model | Score |
|-------|-------|
| DeepSeek V4-Pro | **83.5%** |
| GPT-5.5 | 74.0% |

### NIAH (Needle in a Haystack)
| Model | Score | Context |
|-------|-------|---------|
| DeepSeek V4-Flash | **97%** | 1M (Engram memory) |
| GPT-5.5 | ~90% | 1M |
| Standard attention | 84.2% | 1M |

## Summary: Best by Category

| Category | Winner | Score |
|----------|--------|-------|
| Overall Intelligence | Claude Opus 4.8 | 61.4 |
| Agentic CLI Coding | GPT-5.5 | 82.7% Terminal-Bench |
| Production Coding | Claude Opus 4.7 | 64.3% SWE-bench Pro |
| Scientific Reasoning | GPT-5.5 | 93.6% GPQA |
| Abstract Reasoning | GPT-5.5 | 85.0% ARC-AGI-2 |
| Tool Orchestration | Gemini 3.5 Flash | 83.6% MCP Atlas |
| Long Context Retrieval | DeepSeek V4-Flash | 97% NIAH at 1M |
| Math | DeepSeek R1 v0528 | 87.5% AIME |
| Telecom Agents | DeepSeek V4-Pro | 96.2% τ²-Bench |

## Related
- [[pricing-comparison-2026Q2]] · [[api-features-comparison]]
- All provider pages: [[openai]] · [[anthropic]] · [[google-gemini]] · [[meta-llama]] · [[xai-grok]] · [[mistral]] · [[alibaba-qwen]] · [[deepseek]]
