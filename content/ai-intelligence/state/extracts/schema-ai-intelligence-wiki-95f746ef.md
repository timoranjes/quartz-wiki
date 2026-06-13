# SCHEMA — AI Intelligence Wiki

Unified knowledge base for LLMs, coding agents, and the AI intelligence stack.
Merged from `wiki-llm-providers` + `wiki-ai-agents` on 2026-06-04.

## Page Types

| Type | Directory | Description |
|------|-----------|-------------|
| `entity` | `entities/` | People, companies, organizations in the AI ecosystem |
| `concept` | `concepts/` | Architectures, patterns, techniques, frameworks |
| `comparison` | `comparisons/` | Head-to-head comparisons of approaches, frameworks, or models |
| `source` | `raw/sources/` | Curated articles, blog posts, documentation (immutable) |
| `paper` | `raw/papers/` | Research papers (immutable) |

## Required Frontmatter

Every page MUST have these 6 fields:

```yaml
---
title: "Page Title"
type: entity | concept | comparison
tags: [tag1, tag2]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
status: seed | drafted | reviewed
---
```

## Tag Taxonomy

### LLM Layer
`llm-provider`, `open-weight`, `closed-model`, `moe`, `dense`, `reasoning-model`, `multimodal`, `chinese-llm`

### Architecture
`moe-architecture`, `kv-cache-optimization`, `quantization`, `speculative-decoding`, `context-windows`, `prompt-caching`, `distillation`, `rlhf-training`, `extended-thinking`

### Agent Layer
`coding-agent`, `agent-architecture`, `multi-agent`, `orchestrator`, `planning`, `reflection`, `react`, `tool-use`, `agent-framework`

### Infrastructure
`framework`, `protocol`, `mcp`, `acp`, `evaluation`, `benchmark`, `safety`, `observability`

### Decision
`model-selection`, `cost-optimization`, `pricing`, `trade-offs`

### Capability
`reasoning`, `memory`, `retrieval`, `code-generation`, `web-browsing`, `computer-use`

### Domain
`trading`, `research`, `productivity`, `automation`, `supply-chain`

## Entity Subdirectories

### `entities/llm-providers/`
Model labs and providers: OpenAI, Anthropic, Google, Alibaba/Qwen, DeepSeek, Meta, etc.

### `entities/coding-agents/`
CLI and IDE coding agents: Codex, Claude Code, Gemini CLI, GitHub Copilot, Cursor, Aider, OpenCode, etc.

### `entities/agent-frameworks/`
Multi-agent orchestration platforms: LangChain, CrewAI, AutoGen, etc.

## Concept Subdirectories

### `concepts/llm-architecture/`
Model-level technology: MoE, KV cache, quantization, RLHF, context windows, etc.

### `concepts/agent-patterns/`
Application-level patterns: architectures, orchestration, tool use, evaluation, safety, etc.

### `concepts/protocols/`
Agent-tool communication standards: MCP, ACP, etc.

## Linking Rules

- Use wikilinks for intra-vault references, e.g. `[[openai]]`
- External links use `[text](url)`
- Every concept page should link to ≥2 related pages
- Broken wikilinks are lint errors
- Coding agent pages MUST link to the LLM providers they use (e.g., `[[anthropic]]`)
- LLM provider pages SHOULD link to coding agents that use them as a backend

## Structure

```
wiki-ai-intelligence/
├── SCHEMA.md                          # This file
├── index.md                           # Content index, rebuilt on each update
├── log.md                             # Operation log — append-only
├── entities/
│   ├── llm-providers/                 # Model labs (OpenAI, Anthropic, etc.)
│   ├── coding-agents/                 # CLI/IDE agents (Codex, Claude Code, etc.)
│   └── agent-frameworks/              # Orchestration platforms
├── concepts/
│   ├── llm-architecture/              # Model-level tech
│   ├── agent-patterns/                # Application-level patterns
│   └── protocols/                     # MCP, ACP, etc.
├── comparisons/
│   ├── llm-providers/                 # Model comparisons
│   └── coding-agents/                 # Agent comparisons
└── raw/                               # First-layer: immutable sources
    ├── articles/                      # Provider research articles
    ├── papers/                        # Academic research papers
    └── sources/                       # News, blog posts, announcements
```