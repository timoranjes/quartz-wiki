---
title: "AutoGen"
type: entity
tags: [agent-framework, multi-agent, orchestrator, microsoft]
created: "2026-06-04"
updated: "2026-06-04"
status: drafted
related_entities:
  - [[../llm-providers/microsoft-phi]]
  - [[../llm-providers/openai]]
  - [[../llm-providers/google-gemini]]
  - [[../llm-providers/anthropic]]
used_by: []
---

<div class="entity-header">
  <div class="entity-badges">
    <span class="provider-badge us">🇺🇸 US</span>
    <span class="pricing-badge free">Free</span>
    <span class="open-weight-yes">● Open weights</span>
  </div>
  <div class="entity-meta">
    <span class="entity-meta-key">Type</span>Agent Framework<span class="entity-meta-key">HQ</span>Open Source (Microsoft)<span class="entity-meta-key">Key Models</span>Any LLM
  </div>
</div>
# AutoGen

## Overview

**AutoGen** is a multi-agent conversation framework developed by **Microsoft Research**. It enables agents to collaborate through structured dialogues, with built-in support for human-in-the-loop interaction and code execution.

- **Core Philosophy**: Conversational multi-agent interaction
- **Key Strength**: Human-in-the-loop, dynamic dialogue, code execution
- **Parent**: Microsoft Research
- **License**: MIT (open-source)
- **Website**: [microsoft.github.io/autogen](https://microsoft.github.io/autogen/)

## Architecture

AutoGen uses a **conversational multi-agent** model:
- **Agents**: Autonomous entities that can send/receive messages
- **Group Chat**: Multiple agents converse in a shared channel
- **UserProxyAgent**: Special agent for human-in-the-loop interaction
- **CodeExecutorAgent**: Built-in code execution capability
- **Conversation Patterns**: Round-robin, speaker selection, dynamic routing

## Key Features

| Feature | Description |
|---------|-------------|
| **Conversational Orchestration** | Agents collaborate through message passing |
| **Human-in-the-loop** | Embedded via `UserProxyAgent` in the conversation |
| **Code Execution** | Integrated `CodeExecutorAgent` for running code |
| **Group Chats** | Multi-agent discussions with speaker selection |
| **LLM Caching** | Disk/Redis caching shared across agents |
| **Tool Integrations** | Flexible tool integration via conversational interface |
| **Message-based Memory** | Conversation history as memory context |

## Code Example

```python
import autogen

llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": "sk-..."}],
    "temperature": 0,
}

# Create a human proxy agent for HITL
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "coding"},
)

# Create an assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

# Start a conversation
user_proxy.initiate_chat(
    assistant,
    message="Write a Python script to analyze this dataset."
)
```

## Comparison with Other Frameworks

| Dimension | AutoGen | LangGraph | CrewAI |
|-----------|---------|-----------|--------|
| Architecture | Conversational multi-agent | Graph-based state machines | Role-based team metaphor |
| Ease of Use | Medium — conversational setup | Moderate — graph mental model | Easiest — intuitive roles |
| Control | Medium — conversation-driven | Highest — explicit logic | Moderate — limited flow control |
| Token Efficiency | Highest overhead | Best | Moderate |
| Human-in-the-loop | Embedded in conversation | Workflow pause/resume | Task-level checkpoints |
| Code Execution | Integrated (CodeExecutorAgent) | Native/external in nodes | Tool-based (CodeInterpreterTool) |
| Scalability | Limited large-scale support | Distributed graph execution | Parallel task execution |
| Benchmark (medium tasks) | 68% | 76% | 71% |

## Strengths

- **Human-in-the-loop**: Natural conversation interface for human oversight
- **Code execution**: Built-in, secure code execution environment
- **Flexible conversation patterns**: Group chats, round-robin, speaker selection
- **Active community**: Clear documentation, active development

## Weaknesses

- **High token overhead**: Conversational approach consumes more tokens
- **Complex conversation management**: Hard to control at scale
- **Limited large-scale support**: Not designed for very large agent teams
- **Debugging difficulty**: Tracing failures across conversations is challenging

## When to Use

- Applications requiring natural human-agent conversation
- Code generation and execution workflows
- Multi-agent debate or collaborative problem-solving
- Teams that want conversational agent interaction patterns

## When NOT to Use

- Production systems requiring deterministic control flow (use [[langchain]])
- Token-constrained environments (conversational overhead is high)
- Role-based task delegation workflows (use [[crewai]])

## Related

- [[langchain]] — Chain/graph-based orchestration
- [[crewai]] — Role-based multi-agent framework
- [[llamaindex]] — Retrieval-centric agent framework
- [[multi-agent-orchestration]] — Orchestration patterns
- [[tool-use-pattern]] — Tool integration patterns

## Sources

- [[../../raw/sources/2026-06-02-top-agentic-frameworks-2026-jetbrains]]
- [[../../raw/sources/datacamp-crewai-vs-langgraph-vs-autogen]]
- [[../../raw/sources/pecollective-agent-frameworks-compared-2026]]
