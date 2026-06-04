---
title: "Ollama"
created: 2026-06-04
updated: 2026-06-04
type: entity
status: drafted
tags: ["open-source/tool", "local-inference", "deployment"]
sources: []
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge global">🌐 GLOBAL</span>
    <span class="pricing-badge free">Free</span>
    <span class="open-weight-yes">● Open weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Tool<span class="entity-meta-key">HQ</span>Open Source<span class="entity-meta-key">Key Models</span>Any GGUF model
  </div>
</div>
# Ollama

## Overview

Ollama is a local-first tool for running open-weight LLMs on consumer hardware. It simplifies downloading, quantizing, and serving models via a local API.

## Key Features

- **One-command model runs** — `ollama run llama3` downloads and starts inference
- **Quantization** — Automatic GGUF quantization for memory efficiency
- **Local API** — OpenAI-compatible API endpoint at `localhost:11434`
- **Model Library** — Curated catalog of supported models
- **Modelfile** — Custom model configurations with system prompts

## Supported Models

Llama 3, Qwen 2, Mistral, Phi 3, Gemma, DeepSeek Coder, CodeLlama, and 100+ more via community contributions.

## Use Cases

- Local development and testing
- Privacy-sensitive applications
- Cost-effective inference for non-critical workloads
- Agent prototyping before cloud deployment

## Competitive Position

- **vs. LM Studio**: Ollama is CLI-first, LM Studio is GUI-first
- **vs. vLLM**: Ollama is consumer hardware focused, vLLM is server/GPU focused
- **vs. llama.cpp**: Ollama wraps llama.cpp with UX improvements

## Integration with Agents

Ollama's OpenAI-compatible API makes it a drop-in backend for agent frameworks that support OpenAI API format. This enables local agent testing and development.

## Cross-References

- [[lm-studio]] — GUI alternative
- [[quantization]] — Quantization technology
- [[open-weight-vs-open-source]] — Model licensing
