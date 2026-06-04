---
title: Google Gemini CLI / Antigravity CLI
researched: 2026-06-05
sources:
  - https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
  - https://antigravity.google/blog/google-io-2026
  - https://cloud.google.com/blog/topics/developers-practitioners/choosing-antigravity-or-gemini-cli
  - https://github.com/google-gemini/gemini-cli/discussions/27274
---
# Google Gemini CLI / Antigravity CLI

## Company Facts
- **Developer**: Google
- **Previous Name**: Gemini CLI (launched 2025)
- **Current Name**: Antigravity CLI (GA May 19, 2026)
- **Platform**: Google Antigravity ecosystem
- **GitHub Stars**: >100,000 (Gemini CLI)
- **Merged PRs**: ~6,000 (Gemini CLI)
- **Deprecation**: Gemini CLI stops serving requests for free/Pro/Ultra tiers on June 18, 2026

## Model Lineup

| Model | Description |
|-------|-------------|
| Gemini 3.5 Flash | Default agent model; SOTA agentic and coding model; 4x faster than frontier models, 12x faster on Antigravity |
| Gemini 3.1 Pro | Previous default model |
| Gemini API Agent | Programmatic access via Gemini API |

### Performance Benchmarks (Gemini 3.5 Flash)
- **Terminal-Bench 2.1**: 76.2%
- **GDPval-AA**: 1656 Elo
- **MCP Atlas**: 83.6%
- **CharXiv Reasoning**: 84.2%

## Capabilities
- **Agent Skills**: Built-in skills for domain-specific tasks
- **Hooks**: Pre/post execution hooks for custom workflows
- **Subagents**: Parallel task execution for independent work items
- **Extensions → Antigravity Plugins**: Third-party tool integrations
- **Asynchronous Workflows**: Run large refactors or research in background without blocking terminal
- **Unified Agent Harness**: Shares backend with Antigravity 2.0 desktop app
- **Scheduled Tasks**: Cron-based agent invocation with user-defined tasks
- **Live Voice Transcription**: Powered by Gemini Audio models
- **Projects & Worktree Support**: Streamlined agent management
- **Android Skills**: End-to-end Android app development
- **Firebase Skills**: Agent context for Firebase development
- **Agent Team Capability** (Preview): Multi-agent orchestration; demonstrated by building a functional OS autonomously

## Pricing & Plans
| Plan | Price | Description |
|------|-------|-------------|
| Free Tier | $0 | Limited access (ending June 18, 2026) |
| Google AI Pro | — | Pro tier access |
| Google AI Ultra | $100/mo | Priority access, 5x capacity, $100 bonus credits |
| Enterprise | Custom | Via Gemini Enterprise Agent Platform |

## Key Facts
1. Gemini CLI launched in 2025 and gained >100K GitHub stars and ~6K merged PRs from hundreds of contributors.
2. Antigravity CLI became generally available on May 19, 2026 (Google I/O 2026), replacing Gemini CLI for consumer/Pro/Ultra tiers.
3. Gemini CLI stops serving requests for free, Pro, and Ultra tier users on June 18, 2026. Enterprise users retain access via paid API keys.
4. Antigravity CLI is built in Go for faster, more responsive performance compared to the previous Python-based CLI.
5. The Antigravity ecosystem includes: CLI (terminal), Antigravity 2.0 (desktop app), SDK (preview), and Enterprise platform.
6. Gemini 3.5 Flash delivers 12x speedup on Antigravity (limited-time optimization) and powers the Agent Team capability preview.
7. Enterprise users on Gemini Code Assist Standard/Enterprise or GitHub via Google Cloud experience no service changes.

## Sources
