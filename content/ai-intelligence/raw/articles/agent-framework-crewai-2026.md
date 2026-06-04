---
title: "CrewAI - Role-Based Multi-Agent Orchestration Framework"
researched: 2026-06-05
sources:
  - url: "https://docs.crewai.com/introduction"
    title: "CrewAI Official Documentation"
  - url: "https://github.com/crewaiinc/crewai"
    title: "CrewAI GitHub Repository"
  - url: "https://docs.crewai.com/en/guides/crews/first-crew"
    title: "CrewAI First Crew Guide"
  - url: "https://docs.crewai.com/en/guides/flows/first-flow"
    title: "CrewAI First Flow Guide"
  - url: "https://blog.crewai.com/crewai-oss-1-0-we-are-going-ga/"
    title: "CrewAI OSS 1.0 GA Announcement"
tags:
  - agent-framework
  - multi-agent-orchestration
  - role-playing-agents
  - open-source
---

# CrewAI - Role-Based Multi-Agent Orchestration Framework

## Overview

CrewAI is a **lean, standalone, high-performance Python framework** for orchestrating **role-playing, autonomous AI agents**. Built entirely from scratch and independent of LangChain or other agent frameworks, it enables developers to build complex, collaborative AI systems with both high-level simplicity and low-level control. The framework combines **Crews** (collaborative intelligence) and **Flows** (precise control) to deliver production-ready multi-agent systems.

**GitHub**: [crewAIInc/crewAI](https://github.com/crewaiinc/crewai) · **52.8k+ stars** · **MIT License** · **Python** · **Latest Release: v1.14.6 (May 2026)** · **OSS 1.0 GA**

## Key Features

- **Role-Playing Agents**: Define agents with specialized roles, goals, and backstories. Agents collaborate autonomously to solve tasks delegated to them.
- **Crews (Autonomous Collaboration)**: Teams of agents that plan, execute, and collaborate to achieve high-level goals. Support sequential and hierarchical processes.
- **Flows (Event-Driven Workflows)**: Structured, stateful workflows that manage execution flow with conditional logic, loops, branching, and event-driven triggers.
- **Crews + Flows Integration**: The true power emerges when combining both — Flows orchestrate the overall process while Crews handle complex autonomous tasks within Flow steps.
- **Flexible Tool Integration**: Connect agents to APIs, databases, web search tools, and custom functions.
- **Enterprise Security**: Designed for security and compliance in enterprise deployments with SOC 2 and HIPAA compliance in enterprise edition.
- **Cost-Efficient**: Optimized to minimize token usage and API calls through efficient agent collaboration patterns.
- **CLI Tooling**: `crewai create crew` scaffolds complete project structures with YAML-based agent and task configuration.

## Architecture

CrewAI uses a dual-layer architecture:

1. **Flows Layer (Orchestration)**: The backbone of the application. Flows serve as the "manager" or "process definition" providing:
   - **State Management**: Persist data across steps and executions using Pydantic models.
   - **Event-Driven Execution**: Trigger actions based on events or inputs using `@start()`, `@listen()`, `@router()` decorators.
   - **Control Flow**: Conditional logic, loops, and branching for complex workflow patterns.

2. **Crews Layer (Intelligence)**: The "teams" that perform heavy lifting:
   - **Agent Definition**: YAML or code-based configuration of roles, goals, and backstories.
   - **Task Delegation**: Tasks assigned to agents based on capabilities and roles.
   - **Process Modes**: Sequential (ordered execution) and Hierarchical (manager-agent delegation) processes.
   - **Autonomous Collaboration**: Agents communicate and collaborate like human teams.

The execution model: Flow triggers → Flow manages state → Flow delegates to Crew → Crew agents collaborate → Result returns to Flow → Flow continues.

## Use Cases

- **Research & Analysis**: Multi-agent research teams where one agent researches and another analyzes and reports findings.
- **Content Generation**: Teams of specialized agents (researcher, writer, editor) collaborating on content creation.
- **Business Process Automation**: Flow managing API requests → Crew generating content → Flow saving to database.
- **Market Analysis**: Event-driven workflows analyzing market data with specialized analyst agents.
- **Application Backends**: Flow handling HTTP requests, delegating complex reasoning to Crews, and managing responses.
- **Simple Automation**: Single Flow with Python tasks for straightforward automation needs.

## Pricing & Open-Source Status

- **CrewAI OSS**: **Free and open-source** under the MIT License. Version 1.0 reached GA, powering 1.4 billion+ agentic automations.
- **CrewAI Enterprise**: Commercial offering with SOC 2 and HIPAA compliance, enhanced security, and enterprise support.
- **Community**: Over 100,000 developers certified through community courses. Active community at community.crewai.com.

## Latest Updates (2025-2026)

- **CrewAI OSS v1.0 GA** announced, marking the framework's transition to production-ready status.
- **Flows** introduced as a major architectural addition, complementing the original Crews concept with structured, event-driven orchestration.
- **CrewAI CLI** (`crewai create crew`) provides project scaffolding with YAML-based configuration for agents and tasks.
- The framework has grown to **52.8k+ GitHub stars** and **7.4k+ forks**.
- Coding agent skills integration: `npx skills add crewaiinc/skills` enables adding Claude Code, Codex, and other coding agent capabilities.
- Latest release **v1.14.6** (May 2026) includes ongoing improvements to the Flows/Crews integration and performance optimizations.
- The framework emphasizes being "lean, lightning-fast" and completely independent of LangChain.
