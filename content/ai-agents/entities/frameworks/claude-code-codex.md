---
title: Claude Code & OpenAI Codex
created: 2026-05-29
updated: 2026-06-02
type: entity
tags: [framework, sdk, coding]
sources: [raw/articles/2026-05-29-how-braintrust-turns-customer-requests-into-code-with-codex.md, raw/articles/2026-05-30-how-we-contain-claude-across-products.md, raw/articles/2026-06-01-openai-frontier-models-and-codex-are-now-available-on-aws.md]
confidence: high
---

# Claude Code & OpenAI Codex

## Overview

Both are specialized coding agents — AI systems designed to read, write, and modify code in real projects. They differ in their approach, tool access, and integration patterns.

## Claude Code

### What It Is
Anthropic's coding agent CLI. Runs locally, reads project files, makes edits, runs tests, and commits changes.

### Key Features
- **Sandbox modes:** read-only, workspace-write, danger-full-access
- **Sandbox technologies:** Seatbelt (macOS — system-level sandbox profiles), Bubblewrap (Linux — namespace isolation)
- **Tool access:** File read/write, terminal execution, web search
- **Approval policies:** Configurable approval for shell commands
- **Model:** Claude Sonnet 4 (default), Claude Opus for complex tasks

### When to Use
- Code modifications in existing projects
- Test-driven development
- Code review with inline suggestions
- Projects needing Claude's reasoning quality

### My Setup
- Transport: ACP (Agent Communication Protocol) via `codex --acp --stdio`
- Integrated with Hermes delegate_task for coding subagents
- Sandbox: workspace-write (can edit, cannot delete arbitrary files)

## OpenAI Codex

### What It Is
OpenAI's coding agent, powered by GPT-4o-Codex. Similar concept to Claude Code but with OpenAI's model capabilities.

### Key Features
- **Model:** GPT-4o-Codex (specialized for code)
- **Sandbox:** Configurable (read-only to full-access)
- **Config:** profile-based via config.toml
- **Approval:** Command approval policies (untrusted, on-failure, on-request, never)

### When to Use
- Code tasks where GPT-4o-Codex outperforms (specific benchmarks)
- When OpenAI ecosystem integration is needed
- Projects already on OpenAI infrastructure

### Real-World Usage
- **Braintrust** (2026-05): Uses Codex with GPT-5.5 to turn customer requests into code and run engineering experiments. Demonstrates Codex's viability for production coding workflows beyond internal testing.
- **AWS Availability** (2026-06): OpenAI frontier models and Codex are now generally available on AWS, giving enterprises a path to build with OpenAI through AWS environments, controls, and procurement workflows. Moves from evaluation to production via existing AWS infrastructure.

### My Setup
- Currently not actively configured (Claude Code is primary)
- Available as fallback via Hermes ACP routing

## Comparison

| Aspect | Claude Code | Codex |
|--------|------------|-------|
| Model | Claude Sonnet 4 | GPT-4o-Codex |
| SWE-bench | ~75% | ~70% |
| Reasoning quality | Higher (GPQA 91) | Good but lower |
| Code execution | Shell + file ops | Shell + file ops |
| Approval system | Policy-based | Policy-based |
| Best for | Complex reasoning + code | Straightforward code tasks |

## Integration with Hermes

```python
# Hermes routes coding tasks to Claude Code via ACP
delegate_task(
    goal="Fix the bug in auth.py",
    context="Error: ValueError at line 42",
    toolsets=["terminal", "file"],
    acp_command="codex"  # or "claude-code"
)
```

## When to Use Coding Agents vs General Agents for Code

| Task | Use | Why |
|------|-----|-----|
| Fix a bug | Coding agent | Has file system access, understands project context |
| Write a script | General agent + terminal | Simpler, faster |
| Code review | Coding agent | Can read full project, run tests |
| Research best practice | General agent + web | Coding agents are not good at web research |
| Multi-file refactor | Coding agent | Understands cross-file dependencies |

## Related
- [[claude-code-codex]] — Specialized coding agents for code tasks
- [[hermes-agent]] — how I route coding tasks
- [[model-selection-for-agents]] — which model for coding
- [[orchestrator-workers]] — delegating coding tasks to subagents
