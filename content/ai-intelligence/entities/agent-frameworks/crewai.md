---
title: "CrewAI"
type: entity
tags: [agent-framework, multi-agent, orchestrator, role-based]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/openai]]
  - [[../llm-providers/anthropic]]
  - [[../llm-providers/google-gemini]]
used_by: []
---

# CrewAI

## Overview

**CrewAI** is a role-based multi-agent framework that models workflows like workplace teams. Agents are defined by roles, goals, and backstories, and tasks are assigned to specific agents with structured expected outputs.

- **Core Philosophy**: Role-based collaboration (like a workplace team)
- **Key Strength**: Intuitive, structured task delegation
- **License**: MIT (open-source)
- **Website**: [crewai.com](https://www.crewai.com/)

## Architecture

CrewAI uses a **role-based organizational metaphor**:
- **Agents**: Defined by role, goal, and backstory (e.g., "Senior Research Analyst")
- **Tasks**: Descriptions + expected outputs, assigned to specific agents
- **Crew**: A collection of agents working together on a set of tasks
- **Process**: Sequential or hierarchical task execution

## Key Features

| Feature | Description |
|---------|-------------|
| **Role-Based Design** | Agents = roles + goals + backstories — intuitive for non-engineers |
| **Task Delegation** | Structured task definitions with expected outputs |
| **Human-in-the-loop** | Task-level checkpoints (`human_input=True`) |
| **Tool Integration** | Custom tools, web scraping, code interpreter |
| **Memory** | Short-term, long-term, entity memory, and contextual memory |
| **Parallel Execution** | Horizontal agent replication for parallel tasks |
| **Output Files** | Tasks can write results to files directly |
| **LLM Agnostic** | Works with any LLM provider |

## Code Example

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Senior Research Analyst",
    goal="Find accurate, current data on the topic",
    backstory="You are a meticulous researcher who always verifies facts.",
    tools=[search_tool, web_scraper],
    llm=llm
)

writer = Agent(
    role="Technical Writer",
    goal="Create clear, engaging content from research",
    backstory="You write technical content that's accessible.",
    llm=llm
)

research_task = Task(
    description="Research {topic}. Find key statistics, trends, and expert opinions.",
    expected_output="A structured research brief with sources.",
    agent=researcher
)

crew = Crew(agents=[researcher, writer], tasks=[research_task])
result = crew.kickoff()
```

## Comparison with Other Frameworks

| Dimension | CrewAI | LangGraph | AutoGen |
|-----------|--------|-----------|---------|
| Architecture | Role-based team metaphor | Graph-based state machines | Conversational multi-agent |
| Ease of Use | Easiest — intuitive roles | Moderate — graph mental model | Medium — conversational setup |
| Control | Moderate — limited flow control | Highest — explicit logic | Medium — conversation-driven |
| Token Efficiency | Moderate | Best | Highest overhead |
| Multi-Agent | Strong — role-defined teams | Strong — graph nodes | Strong — group chats |
| Human-in-the-loop | Task-level checkpoints | Workflow pause/resume | Embedded in conversation |
| Benchmark (medium tasks) | 71% | 76% | 68% |

## When to Use

- Rapid prototyping — working prototype in a day
- Workflows that naturally map to team roles (researcher → writer → editor)
- Non-engineers need to understand or help design the agent system
- Task-oriented teams with clear role boundaries

## When NOT to Use

- Workflows requiring complex branching or conditional logic (use [[langchain]])
- Production systems requiring fine-grained control and observability
- Conversational agent collaboration patterns (use [[autogen]])

## Related

- [[langchain]] — Chain/graph-based orchestration
- [[autogen]] — Microsoft's conversational multi-agent framework
- [[llamaindex]] — Retrieval-centric agent framework
- [[multi-agent-orchestration]] — Orchestration patterns
- [[architectures]] — Agent architecture patterns

## Sources

- [[../../raw/sources/2026-06-02-top-agentic-frameworks-2026-jetbrains]]
- [[../../raw/sources/datacamp-crewai-vs-langgraph-vs-autogen]]
- [[../../raw/sources/pecollective-agent-frameworks-compared-2026]]
