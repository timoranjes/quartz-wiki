---
title: Grok Build
researched: 2026-06-05
sources:
  - https://x.ai/news/grok-build-cli
  - https://www.eigent.ai/blog/grok-build-cli
  - https://www.linkedin.com/posts/mervinpraison_xai-just-entered-the-terminal-coding-agent-activity-7465338414171639809-vuF5
  - https://www.ciodive.com/news/xAI-coding-agents-Grok-Build/820422/
---
# Grok Build

## Company Facts
- **Developer**: xAI
- **Launch Date**: May 25, 2026 (early beta)
- **Type**: Terminal-native AI coding agent
- **Access**: SuperGrok and X Premium Plus subscribers
- **Install**: `curl -fsSL https://x.ai/cli/install.sh | bash`

## Model Lineup
Grok Build is powered by xAI's Grok models:

| Model | Description |
|-------|-------------|
| Grok (latest) | xAI's flagship reasoning model, optimized for coding and agentic tasks |
| Grok 3 | Previous generation with strong reasoning capabilities |

## Capabilities
- **Plan Mode**: For complex tasks, start in plan mode to review, approve, comment on, or rewrite plans before execution
- **Clean Diffs**: Every change shows up as a clean diff after plan approval
- **AGENTS.md Support**: Picks up project conventions from AGENTS.md files instantly
- **Plugin Marketplace**: Install community plugins (e.g., browser-review v0.8.2)
- **Hooks, Skills, MCP Servers**: Works with existing AGENTS.md, plugins, hooks, skills, and MCP servers out of the box
- **Parallel Subagents**: Delegates work to specialized subagents that run in parallel for larger tasks
- **Deep Worktree Integration**: Launch subagents in their own worktrees
- **Headless Mode (-p)**: Run agents inside scripts and automations
- **ACP Support**: Full Agent Client Protocol support for building custom bots and agent orchestration apps
- **Terminal-Native**: Full agentic loop — read context, reason, plan, generate diffs, iterate

## Key Facts
1. Grok Build launched on May 25, 2026 as an early beta terminal coding agent for SuperGrok and X Premium Plus subscribers.
2. The tool supports parallel subagent execution, differentiating it from single-session competitors like Claude Code and Codex CLI.
3. Grok Build supports the Agent Client Protocol (ACP), enabling integration with ACP-compatible editors and orchestration platforms.
4. The plan-approve-execute workflow with clean diffs follows the human-in-the-loop pattern now standard across serious AI coding tools.
5. Headless mode (-p flag) enables scripting and automation integration, making Grok Build suitable for CI/CD pipelines.
6. Grok Build leverages xAI's real-time reasoning and live data integration via X/Twitter for current information access.

## Sources
