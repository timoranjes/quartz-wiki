---
title: CrewAI
created: '2026-05-29T00:00:00.000Z'
updated: '2026-05-29T00:00:00.000Z'
type: entity
tags:
  - framework
  - multi-agent
  - open-source
sources: []
confidence: high
---

# CrewAI

## Overview

A role-based multi-agent orchestration framework. Agents are assigned specific roles and tasks, then organized into crews that execute workflows via sequential or hierarchical processes. More opinionated than LangGraph — trades flexibility for simplicity.

## Key Concepts

### Roles and Tasks
Each agent has a defined **role** (e.g., "Researcher", "Writer") with a goal and backstory. **Tasks** specify what needs to be done, with expected output format.

### Agents
```python
from crewai import Agent

researcher = Agent(
    role="Senior Research Analyst",
    goal="Find and analyze market trends",
    backstory="You are a senior analyst at a top research firm.",
    llm="gpt-4o",
    verbose=True
)
```

### Processes
- **Sequential** — tasks run one after another, output passes downstream
- **Hierarchical** — a manager agent delegates and coordinates work

### Crews
```python
from crewai import Crew, Task

research_task = Task(
    description="Research latest AI agent frameworks",
    expected_output="A structured report with pros/cons",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process="sequential",
    verbose=True
)

result = crew.kickoff()
```

## When to Use CrewAI

- Structured multi-agent workflows with clear role separation
- Tasks that naturally decompose into specialist roles (research → write → review)
- Teams wanting a simple setup without learning complex DAG abstractions
- When you want opinionated defaults and don't need fine-grained control

## When NOT to Use CrewAI

- Highly dynamic workflows where agent topology changes at runtime
- Fine-grained control over agent loops and state transitions
- When cost is critical — multiple agents = multiple LLM calls per task
- When you need complex conditional logic between tasks

## Cost Implications

| Pattern | LLM Calls | Notes |
|---------|-----------|-------|
| 3-agent sequential crew | 3+ per kickoff | Each agent calls LLM independently |
| Hierarchical process | 4+ per kickoff | Manager + worker agents all call LLM |
| With tool use | Multiplied | Each tool-using agent adds calls |
| Memory enabled | Additional overhead | Embeddings and retrieval per agent |

**Rule of thumb:** A 3-agent crew with tools can easily cost 5-10x a single-agent call for the same task.

## Comparison vs LangGraph

| Dimension | CrewAI | LangGraph |
|-----------|--------|-----------|
| Abstraction | Role/task-oriented | Graph/state-oriented |
| Flexibility | Lower (opinionated) | Higher (build any graph) |
| Learning curve | Simpler | Steeper |
| Debugging | Easier (clear roles) | Harder (graph traversal) |
| Cost control | Limited | Fine-grained |

## Known Pitfalls

- **Cost explosion** — each agent makes independent LLM calls
- **Redundant work** — agents may re-search/re-compute what others already did
- **Process rigidity** — sequential crews can't backtrack or retry failed tasks
- **LLM dependency** — heavy reliance on system prompts for role behavior

## Related
- [[crewai]] — Role-based framework for orchestrator-worker patterns

- [[multi-agent-orchestration]] — crew patterns in agent systems
- langgraph — alternative graph-based framework
- [[cost-optimization]] — managing multi-agent LLM spend
