---
title: MCP Protocol - Model Context Protocol
researched: 2026-06-05
sources:
  - https://www.anthropic.com/news/model-context-protocol
  - https://modelcontextprotocol.io/docs/getting-started/intro
  - https://cloud.google.com/discover/what-is-model-context-protocol
---

# MCP Protocol - Model Context Protocol

## Overview

The Model Context Protocol (MCP) is an open-source standard introduced by Anthropic in November 2024 for connecting AI applications to external systems. MCP provides a standardized way for AI applications like Claude, ChatGPT, and others to connect to data sources (local files, databases), tools (search engines, calculators), and workflows (specialized prompts), enabling them to access key information and perform tasks.

MCP is often compared to a USB-C port for AI applications — just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems. The protocol uses a client-server architecture where MCP servers expose data and tools, and MCP clients (AI applications) connect to them.

## Key Details

### Architecture
- **MCP Hosts**: AI applications like Claude Desktop, VS Code, Cursor, ChatGPT
- **MCP Clients**: Protocol clients within each host application
- **MCP Servers**: Lightweight servers that expose data, tools, and prompts
- **Transport**: Local (stdio) or remote (HTTP/SSE) communication

### What MCP Enables
- AI agents can access Google Calendar, Notion, and other personal data sources
- Claude Code can generate web apps using Figma designs
- Enterprise chatbots can connect to multiple organizational databases
- AI models can create 3D designs in Blender or print via 3D printers
- Any external tool or data source can be exposed to AI through a standardized interface

### Ecosystem Support
MCP is supported across a wide range of clients and servers:
- **AI Assistants**: Claude, ChatGPT
- **Development Tools**: Visual Studio Code, Cursor, MCPJam
- **Cloud Providers**: Google Cloud, AWS integrations
- **Open Source**: Fully open protocol with SDKs for building custom servers and clients

### Building with MCP
- **Build Servers**: Create MCP servers to expose your data and tools
- **Build Clients**: Develop applications that connect to MCP servers
- **Build MCP Apps**: Create interactive apps that run inside AI clients

### Why MCP Matters
- **Developers**: Reduces development time and complexity when building or integrating with AI applications
- **AI Applications**: Provides access to an ecosystem of data sources, tools, and apps
- **End Users**: Results in more capable AI applications that can access personal data and take actions

### Benefits Over Custom Tool Integration
- **Build Once, Use Everywhere**: A single MCP server can be used by any MCP-compatible client
- **Standardized Interface**: No need to write custom tool schemas for each AI application
- **Secure Connections**: Designed with security in mind for two-way communication
- **Active Ecosystem**: Growing library of pre-built servers for common tools and services

## Sources
- https://www.anthropic.com/news/model-context-protocol
- https://modelcontextprotocol.io/docs/getting-started/intro
- https://cloud.google.com/discover/what-is-model-context-protocol
