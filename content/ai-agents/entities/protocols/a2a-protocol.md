---
title: A2A Protocol
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [a2a, protocol, interop]
sources: []
confidence: medium
---

# A2A (Agent-to-Agent Protocol)

## Definition

Google's protocol for agent-to-agent communication. While MCP connects agents to tools, A2A connects agents to other agents — enabling cross-vendor agent collaboration.

## Why It Exists

Currently, agents from different vendors cannot talk to each other. Anthropic agents cannot delegate to OpenAI agents. Google agents cannot query Anthropic agents. A2A standardizes this communication layer.

## Architecture

```
Agent A (any vendor)
    -> A2A Client
    -> A2A Protocol (HTTP/JSON)
A2A Server -> Agent B (any vendor)
    -> Returns result to Agent A
```

## Key Concepts

### Agent Card
A metadata file that describes what an agent can do:
- Name, description, version
- Supported skills/capabilities
- Authentication requirements
- Endpoint URL

### Task
A unit of work sent from one agent to another:
- Input: task description, context, artifacts
- Output: result, status, artifacts
- Status: submitted, working, completed, failed

### Artifacts
Data exchanged between agents:
- Files, text, structured data
- Can be referenced by URL or embedded

## MCP vs A2A

| Aspect | MCP | A2A |
|--------|-----|-----|
| Purpose | Agent -> Tools | Agent -> Agent |
| Transport | stdio, HTTP/SSE | HTTP/JSON |
| Created by | Anthropic | Google |
| Maturity | More mature, wider adoption | Emerging |
| Use case | Tool integration | Cross-agent collaboration |

## Current Status

- Announced by Google in 2025
- Supported by Google, Anthropic, and other vendors
- Still evolving — not yet as widely adopted as MCP
- Integration with existing agent frameworks in progress

## When It Matters for Me

- **Future:** When I want my Hermes agent to delegate tasks to a specialized external agent
- **Future:** When enterprise agents need to collaborate across vendor boundaries
- **Now:** Still primarily using MCP for tool integration, native delegation for subagents

## Related
- [[mcp-protocol]] — agent-to-tool protocol (complementary)
- [[orchestrator-workers]] — current delegation pattern (native, not A2A)
