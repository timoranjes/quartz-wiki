title: Anthropic Claude Code
tags: coding-agent, anthropic, llm-provider
<div class="entity-header">
  <div class="entity-badges">
    <span class="pricing-badge premium">Premium</span>
    <span class="provider-badge us">🇺🇸 San Francisco (Anthropic)</span>
  </div>
  <div class="entity-meta">
    <div><span class="entity-meta-key">Model</span><span class="entity-meta-value">Opus 4.5 / Sonnet 4.5</span></div>
    <div><span class="entity-meta-key">Capability</span><span class="entity-meta-value">Dynamic Workflows</span></div>
    <div><span class="entity-meta-key">SWE-bench</span><span class="entity-meta-value">Verified 87.6%</span></div>
  </div>
</div>


# Anthropic Claude Code

Anthropic's autonomous coding agent, available as a CLI tool and integrated into the Claude web interface. Powered by Claude Fable 5 (June 2026) or Claude Opus 4.8 for deepest reasoning.

## Overview

- **Developer**: Anthropic
- **Backend Model**: Claude Fable 5 (June 2026, new frontier), Claude Opus 4.8 (previous flagship), Claude Sonnet 4.6 (cheaper turns)
- **Interface**: CLI (`claude`), Claude Code for web, Claude Cowork, claude.ai chat
- **Pricing**: Base (~$20/mo, Claude Pro), Max ($100-200/mo, 20× limits), Teams (custom). Fable 5 included on subscription plans until June 22, 2026, then billed extra.
- **Open Source**: SDK and core are open source

## Key Capabilities

- Autonomous code editing with natural language instructions
- Full codebase context awareness
- Built-in terminal, file editing, and web search
- 200K+ context window for large codebase understanding
- Permission model for tool use control
- **Dynamic Workflows**: Adaptive task decomposition and execution
- **Subagents**: Parallel task execution for independent work items
- **LSP Support**: Language Server Protocol integration for real-time code analysis
- **Async Sub Agents**: Background task execution for parallel processing
- **Ultrathink**: Enhanced deep reasoning mode for complex tasks

### Sub-Agents (June 2026)
- **Plugin agents**: Appear in `/agents` alongside custom agents, can be invoked explicitly
- **Agent ID display**: Claude Code displays the agent ID when a subagent completes work
- **Use case**: Parallel execution of independent work items (testing, linting, documentation)

- **Slack Handover**: Ability to hand off tasks via Slack integration
- **AutoCloud**: Cloud-based execution support

## Recent Updates (May–June 2026)

- **Claude Fable 5 (June 9, 2026)**: New frontier model available across all Claude Code surfaces (CLI, web, Cowork). Demonstrated exceptional coding ability — built LLM 0.32a3 (Datasette Agent human-in-the-loop features with `ask_user()`, `PauseChain`, tool call resumption) almost entirely via Claude Code in one day, including identifying and fixing 4 bugs in the underlying LLM library. Described as "very proactive" — spots and fixes issues without being asked. $110/day real-world usage observed via $100/month Max subscription
- **Claude Opus 4.8 (May 28, 2026)**: SOTA reasoning (GPQA 92%), coding (SWE-bench Verified 87.6%), 1M context
- **Dynamic Workflows**: Adaptive task decomposition for complex multi-step work
- **Limits doubled (May 6, 2026)**: Increased usage limits for Pro and Max tiers
- **Anthropic S-1 filing (June 1, 2026)**: Confidentially submitted draft S-1 to SEC — IPO preparation
- **$65B Series H (May 28, 2026)**: Raised at $965B post-money valuation
- **Project Glasswing expanded (June 2, 2026)**: AI security initiative with AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks
- **Claude Partner Network (June 3, 2026)**: New Services Track and Partner Hub launched

## Notable Features

- **Permission modes**: Always allow, default (ask), read-only
- **CLAUDE.md**: Project-level instructions file for custom behavior
- **Slash commands**: `/help`, `/clear`, `/compact`, `/cost`
- **Multi-file editing**: Can modify many files in a single turn
- **MCP support**: Model Context Protocol for third-party tool integrations

## Competitive Positioning

- Strong in code quality and safety consciousness
- Claude Opus 4.8 is current #1 by AA Intelligence Index (61.4)
- Best for architectural refactors and multi-file reasoning
- Direct competitor to OpenAI Codex
- Known for more cautious, thorough approach vs. faster but riskier agents
- Supports ACP protocol — can run inside ACP-compatible editors (Devin Desktop, JetBrains)

## "Relentlessly Proactive" Behavior (June 11, 2026)

Simon Willison documented an extreme example of Fable 5's autonomous problem-solving in Claude Code. Given a screenshot of a CSS scrollbar bug and a one-line prompt, Fable 5 autonomously:

1. **Fired up local dev server** with fake environment variables
2. **Launched Playwright Chrome**, enabled visible scrollbars (`defaults write com.google.chrome.for.testing AppleShowScrollBars Always`)
3. **Cycled through Firefox and WebKit** in Playwright, failing to recreate the bug
4. **Detected Safari as default browser**, built custom HTML test pages
5. **Invented a screenshot pipeline**: used `uv run --with pyobjc-framework-Quartz` to iterate CGWindowList, find Safari windows by name, then `screencapture -x -o -l <windowID>` to capture PNGs
6. **Injected JavaScript into Datasette templates** to auto-trigger the `/` keyboard shortcut 1.2s after page load
7. **Built a custom CORS web server** (Python `http.server`) to receive `fetch()` POST data from the browser
8. **Scripted through Web Component shadow DOM** to extract textarea measurements
9. **Confirmed the fix** in real Safari

When Fable hit an invisible guardrail and downgraded to Opus 4.8, Opus inherited the full transcript and continued using all the tricks Fable had pioneered, eventually finding and verifying the two-line CSS fix.

### Cost
- **Session cost**: ~$12.11 (68,606 output tokens, 113,178 peak context) at full API pricing
- **Models used**: claude-fable-5 + claude-opus-4-8 (fallback)
- Measured via [AgentsView](https://www.agentsview.io)

### Security Implications
- Coding agents can do **anything you can do** via terminal — frontier models know "every trick in the book, and evidently a few that nobody has ever written down before"
- If subverted by prompt injection, the same proactivity enables extreme data exfiltration or mischief
- **Running coding agents outside a sandbox is a "Challenger disaster" waiting to happen** (Simon Willison's top prediction for 2026)
- The smartness is a double-edged sword: more capable agents are more dangerous if compromised

Sources: [Simon Willison](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) ^[raw/sources/2026-06-11-claude-fable-is-relentlessly-proactive.md]

## Related

- [[anthropic]] — Provider
- [[openai-codex]] — Competitor
- [[cursor]] — Uses Claude as one of its model backends
- [[model-selection-for-agents]] — Model selection for agent workloads
- [[acp-protocol]] — Supported protocol for editor integration
- [[agent-safety]] — Sandboxing and security implications