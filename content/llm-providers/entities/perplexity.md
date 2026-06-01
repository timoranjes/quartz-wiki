---
domain: llm-providers
type: provider
tags: [provider/us, model/closed-source, model/search]
aliases: [Perplexity AI, Sonar, Perplexity Search]
created: 2026-06-01
---
# Perplexity AI (Sonar)

## Overview
Perplexity AI builds **search-grounded** language models (Sonar family) that integrate real-time web search into responses.

## Key Models (2026)

| Model | Context | Notes |
|-------|---------|-------|
| Sonar Pro | 200K | Search-grounded, fast |
| Sonar Deep Research | — | Multi-step research agent |
| Sonar Reasoning | — | Extended thinking + search |

## Strengths
- **Real-time search**: Every response grounded in current web results
- **Citations**: Automatic source attribution
- **Deep Research**: Multi-step autonomous research capability
- **Speed**: Fast response times

## Pricing
| Plan | Cost |
|------|------|
| Free tier | Limited |
| Pro | $20/month |
| API (Sonar Pro) | $1.00/1M input |
| Enterprise | Custom |

## Positioning
Not a traditional LLM provider — a search+answer product. Uses other providers' models internally (OpenAI, Anthropic) plus proprietary search layer. Sonar is their own model built for search-grounded generation.

## Related
- [[google-gemini]] — Also has search grounding (Google Search)
- [[xai-grok]] — Also has real-time social search
