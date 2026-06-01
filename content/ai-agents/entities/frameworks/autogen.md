---
title: Microsoft AutoGen
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

# Microsoft AutoGen

## Overview

A conversational multi-agent framework from Microsoft Research. Agents communicate through group chats, can execute code, and support human-in-the-loop interactions. More exploratory and conversational compared to CrewAI's structured approach.

## Key Concepts

### Agents
```python
import autogen

config_list = [{"model": "gpt-4o", "api_key": "..."}]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful assistant."
)

coder = autogen.AssistantAgent(
    name="coder",
    llm_config={"config_list": config_list},
    system_message="You write Python code to solve problems."
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding", "use_docker": False},
)
```

### Group Chats
Multiple agents converse in a shared channel. A GroupChatManager selects who speaks next based on conversation context.

```python
groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, assistant],
    messages=[],
    max_round=10
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list}
)
```

### Human-in-the-Loop
Set `human_input_mode="ALWAYS"` or `"TERMINATE"` to inject human feedback at each step or only when an agent requests termination.

### Code Execution
Agents can write and execute code in a sandbox. Supports Docker isolation for safety.

## When to Use AutoGen

- Research and exploration tasks where agents need to discuss and iterate
- Code generation workflows where agents write, test, and refine code collaboratively
- Tasks requiring human oversight and feedback loops
- Brainstorming and multi-perspective problem solving
- When you want agents to self-organize rather than follow a fixed pipeline

## When NOT to Use AutoGen

- Production pipelines requiring deterministic, predictable outputs
- Cost-sensitive applications (conversation loops can spiral)
- When you need strict role separation and task boundaries
- Simple tasks that a single agent can handle

## Cost Implications

| Pattern | Risk Level | Notes |
|---------|------------|-------|
| Group chat with 3 agents | High | Each round = 1 LLM call per speaking agent |
| max_round not set | Critical | Can loop indefinitely |
| Code execution errors | High | Agents retry failed code, multiplying calls |
| Human-in-the-loop | Variable | Depends on human response speed, not cost |

**Critical:** Always set `max_round` in GroupChat. Without it, agents can spiral into endless conversation.

## Comparison vs CrewAI

| Dimension | AutoGen | CrewAI |
|-----------|---------|--------|
| Communication | Conversational (free-form) | Structured (role-based handoff) |
| Control | Lower (emergent behavior) | Higher (defined processes) |
| Code execution | Built-in | Via tools/plugins |
| Human-in-loop | First-class | Limited |
| Predictability | Lower | Higher |
| Best for | Exploration/research | Production pipelines |

## Known Pitfalls

- **Conversation loops** — agents can talk in circles without clear termination criteria
- **Cost explosion** — group chats with many rounds consume tokens rapidly
- **Inconsistent outputs** — conversational nature means non-deterministic results
- **Code execution risks** — agents may run unsafe code if not sandboxed
- **Agent personality conflicts** — poorly designed system messages cause agents to argue rather than collaborate
- **Speaker selection bugs** — GroupChatManager sometimes picks wrong speaker

## Mitigation Strategies

1. Always set `max_round` (start with 5-10)
2. Use `termination_msg` functions to detect completion
3. Enable Docker for code execution sandboxing
4. Start with `human_input_mode="TERMINATE"` for safety
5. Log all messages for debugging conversation flow

## Related

- [[multi-agent-orchestration]] — multi-agent communication patterns
- tool-use — agent code execution and tool patterns
- [[cost-optimization]] — managing conversational agent spend
- [[mcp-protocol]] — alternative tool integration approach
