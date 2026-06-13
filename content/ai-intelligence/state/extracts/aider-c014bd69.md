title: Aider
tags: coding-agent, open-source, llm-provider
# Aider

Open-source AI pair programming tool for terminal-based coding. Works with any OpenAI-compatible API.

## Overview

- **Developer**: Open source community (Paul Gauthier)
- **Backend Models**: Any OpenAI-compatible model (GPT-4o, Claude via proxy, local models)
- **Interface**: CLI (`aider`)
- **Pricing**: Free (open source) + your own API costs
- **Open Source**: Fully open source (Apache 2.0)

## Key Capabilities

- Git-aware pair programming
- Automatic commit management
- Multi-file editing
- Codebase map generation
- Works with local models (Ollama, LM Studio)

## Workflow

1. Run `aider` in project directory
2. Describe changes in natural language
3. Aider edits files, commits automatically
4. Review and iterate

## Notable Features

- **Model agnostic**: Works with any OpenAI-compatible API
- **Local model support**: Run with Ollama, LM Studio for privacy
- **Git integration**: Automatic commits with descriptive messages
- **Map files**: Generates code maps for context efficiency
- **Voice input**: Speech-to-code support

## Competitive Positioning

- Best option for privacy-conscious developers (local models)
- Lightweight and fast compared to full agent systems
- Lower quality than Codex/Claude Code with premium models
- Strong community and active development

## Related

- [[openai]] — Default model provider
- [[quantization]] — Enables local model usage
- [[open-weight-licensing]] — Open model ecosystem
- [[model-selection-for-agents]] — Model selection for agent workloads