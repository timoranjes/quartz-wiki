---
title: OpenCode
researched: 2026-06-05
sources:
  - https://opencode.ai/
  - https://github.com/anomalyco/opencode
  - https://www.nxcode.io/resources/news/aider-vs-opencode-ai-coding-cli-2026
  - https://webkul.com/blog/opencode-terminal-coding-agent/
---
# OpenCode

## Company Facts
- **Developer**: Anomaly (https://anoma.ly/)
- **License**: MIT
- **Type**: Open-source AI coding agent
- **GitHub**: https://github.com/anomalyco/opencode (170K+ stars, 925+ contributors, 13,773+ commits)
- **Latest Release**: v1.15.13 (May 30, 2026)
- **Adoption**: 7.5M+ developers monthly
- **Tech Stack**: TypeScript (67.8%), MDX (28.6%), Rust/Tauri (desktop)

## Model Lineup
OpenCode supports 75+ LLM providers via Models.dev:

| Provider | Models |
|----------|--------|
| Anthropic | Claude (all models, including Pro/Max direct login) |
| OpenAI | GPT series, ChatGPT Plus/Pro login |
| Google | Gemini series |
| AWS | Bedrock models |
| Local | Ollama, llama.cpp (optimized for offline use) |
| Zen Models | Curated, benchmarked models optimized for coding agents |
| Total | 75+ providers |

## Capabilities
- **LSP Integration**: Automatically loads correct Language Server Protocols — provides type information, symbol definitions, and real-time diagnostics
- **Multi-Session**: Run multiple agents in parallel on the same project; shareable session links
- **Built-in Agents**:
  - `build`: Default agent for active development (full file access, edits, commands)
  - `plan`: Read-only analysis agent (no file edits by default, asks permission before bash)
  - `@general`: Subagent for complex multistep searches and reasoning
- **Multi-Interface**: Terminal CLI, Desktop App (macOS, Windows, Linux — beta), IDE Extensions (VS Code, JetBrains)
- **Privacy-First**: Zero data retention — no code or context data stored
- **One-Line Install**: `curl -fsSL https://opencode.ai/install | bash`
- **Package Manager Support**: npm, bun, brew, scoop, chocolatey, pacman, nix, mise, paru

## Key Facts
1. OpenCode has 170K+ GitHub stars and 7.5M+ monthly active developers, making it one of the most popular open-source AI coding agents.
2. The LSP integration differentiates OpenCode from competitors — it provides type-aware code understanding for TypeScript, Rust, Go, Java, and other type-safe languages.
3. OpenCode's multi-session capability allows parallel agent execution (e.g., frontend + backend simultaneously), a feature most CLI coding agents lack.
4. The project is developed by Anomaly and licensed under MIT, with 925+ contributors and 814 releases as of May 2026.
5. Zen Models provide curated, benchmarked models optimized specifically for coding agent workloads.
6. Anthropic briefly blocked OpenCode from accessing Claude API in early 2026 — access was restored after developer outcry.
7. OpenCode's core philosophy is "IDE-level intelligence in the terminal," contrasting with Aider's "git-first" approach.

## Sources
