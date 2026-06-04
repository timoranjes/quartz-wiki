---
title: OpenAI Codex Agent
researched: 2026-06-05
sources:
  - https://openai.com/index/introducing-codex/
  - https://developers.openai.com/codex/pricing
  - https://openai.com/index/introducing-upgrades-to-codex/
---

# OpenAI Codex Agent

## Overview

Codex is a cloud-based, multi-tasking software engineering agent powered by the codex-1 model — a version of OpenAI's o3 optimized specifically for software engineering tasks. The Codex agent operates entirely within a secure, isolated container in the cloud, capable of writing features, fixing bugs, answering codebase questions, proposing pull requests, and running tests, linters, and type checkers.

Codex was introduced as a research preview in May 2025 and has since expanded across OpenAI's subscription tiers. It integrates with GitHub and supports AGENTS.md for custom workflow guidance. Each task runs in an isolated cloud sandbox preloaded with the user's repository, with progress visible in real time and completion typically taking 1-30 minutes depending on complexity.

## Key Details

### Features
- **Parallel Task Execution**: Multiple tasks run simultaneously in isolated cloud sandboxes
- **codex-1 Model**: Based on OpenAI o3, fine-tuned for software engineering using reinforcement learning on real-world coding tasks
- **192K Token Context**: Handles large codebases with extended context window
- **AGENTS.md Support**: Human-provided instructions for Codex (like a README for agents), with nested file precedence rules
- **GitHub Integration**: Proposes pull requests, integrates with existing workflows
- **Secure Sandboxes**: No internet access during task execution; runs in isolated containers
- **Verifiable Outputs**: Citations (file paths + terminal logs), test results, and diff summaries
- **ChatGPT Interface**: Accessible via ChatGPT sidebar with "Code" (assign task) and "Ask" (query codebase) actions

### How Codex Works
1. Task starts in isolated sandbox preloaded with repo
2. Progress visible in real time
3. Completion time: 1-30 minutes depending on complexity
4. Changes committed in sandbox
5. Output includes citations, test results, and diff summary
6. User can review, request revisions, or open a GitHub PR

### Model: codex-1
- Based on OpenAI o3, fine-tuned for software engineering
- Trained using reinforcement learning on real-world coding tasks
- Optimized to mirror human coding style and PR preferences
- Produces cleaner patches ready for human review compared to base o3
- Tested at 192K token context with medium reasoning effort

### Security & Trust
- No internet access during task execution
- Runs in secure, isolated containers
- Cannot access external APIs, websites, or services
- Explicitly refuses malicious requests
- Published o3 System Card Addendum with safety evaluations
- Users must manually review and validate all agent-generated code

### Pricing & Availability
- **Included with Plans**: ChatGPT Plus, Pro, Business, Edu, and Enterprise
- **Usage Scales by Plan**: Plus, Edu, Pro, Business, Enterprise tiers have increasing usage limits
- **CLI**: Open-source CLI available with `codex-mini-latest` model
- **Free Trial**: Generous usage at no extra cost during initial weeks
- **Rate Limiting**: Applied after trial period
- **Shared Usage**: Codex usage limits are shared with other agentic features

### Early Adopters
- **Cisco**: Evaluating Codex for real-world product use cases
- **Temporal**: Feature development, debugging, testing, refactoring
- **Superhuman**: Test coverage and code quality improvements

## Sources
- https://openai.com/index/introducing-codex/
- https://developers.openai.com/codex/pricing
- https://openai.com/index/introducing-upgrades-to-codex/
