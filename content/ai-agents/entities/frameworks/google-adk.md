---
title: Google Agent Development Kit
created: '2026-05-29T00:00:00.000Z'
updated: '2026-05-29T00:00:00.000Z'
type: entity
tags:
  - framework
  - multi-agent
  - platform
  - proprietary
sources: []
confidence: medium
---

# Google Agent Development Kit

## Overview

Google's framework for building and deploying AI agents. Integrates tightly with Vertex AI, Gemini models, and Google Cloud services. Provides AgentRunner for orchestration, built-in tool support, and state management for multi-step workflows.

## Key Concepts

### AgentRunner
The core execution engine. Manages agent lifecycle, tool invocation, and state transitions.

```python
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    instruction="Research and summarize topics.",
    tools=[web_search, document_reader]
)

session_service = InMemorySessionService()
runner = Runner(agent=agent, app_name="my-app", session_service=session_service)
```

### Tools
Built-in tool definitions that agents can call. Integrates with Google Cloud services (BigQuery, Vertex AI Search, etc.) and supports custom Python functions.

```python
from google.adk.tools import google_search

search_tool = google_search.GoogleSearchTool()
```

### State Management
Sessions maintain conversation state across multiple turns. Supports both in-memory and persistent storage (Firestore).

### Root Agents
Top-level agents that orchestrate sub-agents. Similar to orchestrator pattern in multi-agent systems.

```python
root_agent = Agent(
    name="root",
    model="gemini-2.0-pro",
    instruction="Coordinate research and writing tasks.",
    sub_agents=[researcher, writer, reviewer]
)
```

## When to Use Google ADK

- Deep Google Cloud / Vertex AI integration needed
- Building agents that use Gemini models exclusively
- Enterprise workflows requiring Google Cloud infrastructure
- When strong tool integration with Google services is valuable
- Teams already invested in Google ecosystem

## When NOT to Use Google ADK

- Multi-model strategies (ADK is Gemini-focused)
- Open-source / self-hosted requirements
- When you need mature third-party integrations (ecosystem is newer)
- Quick prototyping without Google Cloud setup
- Cost-sensitive projects (Gemini pricing + Cloud infrastructure costs)

## Comparison vs Alternatives

| Dimension | Google ADK | LangGraph | CrewAI |
|-----------|-----------|-----------|--------|
| Model support | Gemini-first | Model-agnostic | Model-agnostic |
| Ecosystem maturity | Newer | Mature | Moderate |
| Cloud dependency | High (GCP) | Low | Low |
| Tool integration | Strong (Google services) | Broad (MCP ecosystem) | Moderate |
| Learning curve | Moderate | Steep | Shallow |
| Open source | Partial | Full | Full |

## Known Limitations

- **Gemini-centric** — best experience with Gemini models, other models have limited support
- **Newer ecosystem** — fewer community resources, examples, and third-party integrations
- **Google Cloud dependency** — full features require GCP, not ideal for local-only setups
- **Limited community** — smaller user base means fewer StackOverflow answers and tutorials
- **Vendor lock-in risk** — heavy integration with Google services creates migration friction
- **Evolving API** — framework is actively developed, breaking changes possible
- **Documentation gaps** — some advanced patterns lack detailed docs

## Cost Considerations

| Factor | Impact |
|--------|--------|
| Gemini API calls | Per-token pricing (varies by model tier) |
| Vertex AI infrastructure | Additional compute/storage costs |
| Tool integrations | Some Google tools have separate pricing |
| Session storage | Firestore/Cloud Storage if using persistence |

**Note:** ADK itself is free, but the underlying Google Cloud services carry costs.

## Related
- [[google-adk]] — Google's architecture framework, alternative to LangGraph

- [[mcp-protocol]] — alternative tool integration standard
- [[multi-agent-orchestration]] — orchestrator patterns in agent systems
- [[cost-optimization]] — managing cloud-based agent spend
- vertex-ai — Google's broader AI platform
