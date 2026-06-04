---
title: "OpenCode"
type: entity
tags: [coding-agent, open-source, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
sources: [raw/articles/coding-agent-opencode-2026.md]
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge free">Free/OSS</span>
    <span class="provider-badge open">📦 Open Source</span>
  </div>
  <div class="capability-badges">
    <span class="capability-badge cli"><span class="cap-icon">⌨️</span> CLI</span>
    <span class="capability-badge multi-file"><span class="cap-icon">📁</span> Multi-File</span>
    <span class="capability-badge testing"><span class="cap-icon">🧪</span> Testing</span>
  </div>
</div>


# OpenCode

Open-source AI coding agent with a focus on simplicity and multi-model support.

## Overview

- **Developer**: Open source community
- **Backend Models**: Multiple (Anthropic, OpenAI, Google, OpenRouter, local)
- **Interface**: CLI (`opencode`)
- **Pricing**: Free (open source) + your own API costs
- **Open Source**: Fully open source

## Key Capabilities

- Multi-model provider support
- Code editing and terminal execution
- Project context awareness
- Configuration-driven behavior
- Lightweight and fast

## Workflow

1. Configure providers and models in config
2. Run `opencode` with task description
3. Agent edits code, runs commands, reports results
4. Iterate until satisfied

## Notable Features

- **Provider flexibility**: Switch between Anthropic, OpenAI, Google, or any OpenAI-compatible API
- **OpenRouter support**: Access to 100+ models through single API
- **Configuration-first**: YAML-based config for providers, models, and behavior
- **Lightweight**: Fast startup, minimal dependencies

## Competitive Positioning

- Best for developers who want model flexibility
- Simpler and lighter than full agent frameworks
- Growing adoption in open-source community
- Good alternative to commercial agents for cost-conscious users

## Related

- [[openai]] — Model provider option
- [[anthropic]] — Model provider option
- [[google-gemini]] — Model provider option
- [[model-selection-for-agents]] — Model selection for agent workloads
