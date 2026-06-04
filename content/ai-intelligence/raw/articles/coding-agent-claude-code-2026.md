---
title: Claude Code - Anthropic Agentic Coding System
researched: 2026-06-05
sources:
  - https://www.anthropic.com/product/claude-code
  - https://docs.anthropic.com/en/docs/about-claude/models
---

# Claude Code - Anthropic Agentic Coding System

## Overview

Claude Code is an agentic coding system developed by Anthropic that enables users to describe what they want to build, test, iterate, or ship — and handles the rest autonomously. Unlike traditional autocomplete tools, Claude Code operates at the project level, reading entire codebases, planning multi-file changes, executing them, running tests, and iterating on failures, all while maintaining human oversight.

The system democratizes software development by enabling non-engineers (founders, PMs, designers, ops) to build working software using natural language, while augmenting engineers by shifting their focus from implementation to architecture and orchestration of multiple agents. Claude Code uses real development tools natively (GitHub CLI, Git, Kubernetes) without requiring users to memorize syntax.

## Key Details

### Features
- **Agentic Workflow**: Reads codebase → Plans actions → Executes across files → Runs tests → Iterates on failures
- **Full Codebase Context**: Searches directories, traces dependencies, understands module relationships
- **Toolchain Integration**: Uses CLI tools natively (GitHub CLI, Git, Kubernetes) via natural language instructions
- **CI/CD Monitoring**: Automatically detects CI failures (GitHub/GitLab), diagnoses, fixes, and re-runs tests
- **Autonomy Control**: Users choose autonomy level — approve every action or let built-in classifiers distinguish safe vs risky actions
- **Default Cautious Mode**: Requires approval before modifying files or running commands
- **Human-in-the-Loop**: Final decisions about what code ships remain with the user

### Use Cases
- Navigating unfamiliar codebases (helps newcomers get up to speed in minutes)
- Developing across the whole codebase (large-scale work: new features, multi-file refactors)
- Executing across toolchain (Git, Kubernetes, etc. via natural language)
- Running tests and managing CI failures (reads test errors, fixes code, re-runs until passing)

### Real-World Impact
- **Stripe**: Deployed across 1,370 engineers; one team completed a 10,000-line Scala-to-Java migration in 4 days (vs. 10 engineer-weeks estimated)
- **Ramp**: Cut incident time by 80%; non-engineers now query data warehouse in natural language
- **Wiz**: Migrated 50,000-line Python library to Go in ~20 hours (vs. 2-3 months manually)
- **Rakuten**: Reduced average feature delivery time from 24 days to 5 days; engineers run multiple sessions in parallel

### Model Support
- Powered by Claude models including Claude Sonnet 4.5 ($3/$15 per million tokens) and Claude Opus 4.8 ($5/$25 per million tokens)
- Up to 90% cost savings with prompt caching and 50% savings with batch API
- Supports extended thinking mode for complex reasoning tasks

### Pricing
- Claude Code is billed based on Claude model usage (API token pricing)
- Model pricing: Claude Sonnet 4.5 at $3 input / $15 output per million tokens; Claude Opus 4.8 at $5 input / $25 output per million tokens
- Prompt caching provides up to 90% cost savings on repeated prompts

## Sources
- https://www.anthropic.com/product/claude-code
- https://docs.anthropic.com/en/docs/about-claude/models
