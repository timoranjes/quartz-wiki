---
title: "Cursor IDE"
type: entity
tags: [coding-agent, ide, llm-provider]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge competitive">Competitive</span>
    <span class="open-weight-no">● Closed weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Coding Agent (IDE)<span class="entity-meta-key">HQ</span>San Francisco, US<span class="entity-meta-key">Valuation</span>Anysphere<span class="entity-meta-key">Key Models</span>Claude Sonnet 4.6, GPT-5.5, Composer 2.5
  </div>
</div>
# Cursor IDE

AI-first IDE forked from VS Code, with built-in codebase-aware AI agent capabilities. By mid-2026, the largest user base among AI coding IDEs with Composer 2.5 and Bugbot.

## Overview

- **Developer**: Anysphere
- **Backend Models**: Claude Sonnet 4.6, Claude Opus 4.7/4.8, GPT-5.4/5.5, Gemini, Composer 2 (first-party model)
- **Interface**: Desktop IDE (macOS, Windows, Linux)
- **Pricing**: Hobby (limited), Pro ($20/mo, credit-based), Teams Standard ($32/seat/mo annual, $40/mo monthly), Teams Premium ($96/seat/mo annual, $120/mo monthly, 5× usage), Ultra ($200/mo)
- **Open Source**: Based on open-source VS Code

## Key Capabilities

- Codebase-indexed AI: understands entire project context
- Tab autocomplete with multi-file predictions
- Agent mode: autonomous multi-file editing
- Chat with codebase context
- Multi-model support: switch between providers
- **Composer 2.5**: Multi-file editing with enhanced AI agent (May 2026)
- **Build in Parallel**: Fan-out to multiple parallel agents for concurrent task execution
- **Bugbot**: In-editor agent that triages and fixes bugs autonomously (~78% self-resolution rate, v3.3 May 2026)
- **Durable Canvases**: Persist multi-step plans across sessions

## Recent Updates (May–June 2026)

- **v3.3 (May 2026)**: Added durable canvases for multi-step plans and Bugbot
- **Teams Repricing (June 2026)**: Restructured into Standard ($32/seat/mo annual) and Premium ($96/seat/mo annual) tiers for usage predictability
- **Composer 2.5**: Enhanced multi-file editing capabilities
- **Build in Parallel**: Support for fan-out to multiple parallel agents

## Competitive Positioning

- Best-in-class IDE experience for AI coding; largest user base
- Strong for developers who prefer IDE over CLI
- More integrated than standalone CLI agents
- Faces competition from Claude Code, Devin Desktop, and Copilot
- Model-agnostic approach avoids vendor lock-in

## Related

- [[anthropic]] — Primary model backend
- [[openai]] — Alternative model backend
- [[google-gemini]] — Alternative model backend
- [[claude-code]] — Competitor (CLI)
- [[github-copilot]] — Competitor (IDE extension)
- [[devin-desktop]] — Competitor (agent-first IDE)
