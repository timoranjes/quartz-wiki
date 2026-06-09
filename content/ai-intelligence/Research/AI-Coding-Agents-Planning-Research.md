# How Production AI Coding Agents Handle Planning
## Research Findings — June 2026

---

## 1. Cursor / Copilot / Windsurf — Planning Workflows

### Cursor: Plan Mode (Shift+Tab)
- **Does it plan before coding?** YES — via explicit **Plan Mode** toggled with `Shift+Tab`.
- In Plan Mode, the agent:
  1. Researches the codebase for relevant files (grep + semantic search)
  2. Asks clarifying questions
  3. Generates a detailed implementation plan with file paths & code references
  4. **Waits for approval before any code changes**
- Plans can be saved to `.cursor/plans/` for team documentation, resuming work, and providing context to future agents.
- **Enforcement**: In Plan Mode, the agent physically cannot write code — it's a hard mode boundary, not a soft prompt request.
- **Best practice from Cursor's official blog**: "The most impactful change you can make is planning before coding."
- **Replanning**: If the agent misinterprets a request, users are advised to revert changes, refine the plan, and re-run — "often faster and cleaner than iterative fixes mid-generation."

**Source**: [Cursor Blog — Best Practices for Coding with Agents](https://cursor.com/blog/agent-best-practices)

### GitHub Copilot: Plan Agent + Autopilot
- **VS Code** has a dedicated **Plan agent** (selectable from agent dropdown or via `/plan` command).
- Workflow:
  1. User describes task → Plan agent researches codebase
  2. Agent asks clarifying questions
  3. Generates high-level plan summary with implementation + verification steps
  4. User iterates on plan until satisfied
  5. Plan is saved to session memory (`/memories/session/plan.md`)
  6. Implementation begins (same session or new Copilot CLI session)
- **Visual Studio 2022** has "Planning Mode" (public preview) that auto-determines whether to respond directly or switch to planning for multi-step tasks.
- **Copilot CLI** has `Shift+Tab` toggle between normal mode and plan mode, plus "autopilot mode" for autonomous execution.
- **Enforcement**: Configurable via settings — `chat.planAgent.defaultModel` for planning model, `github.copilot.chat.implementAgent.model` for implementation. Custom planning agents can enforce architectural guidelines.

**Sources**: [VS Code Planning Docs](https://code.visualstudio.com/docs/agents/planning), [GitHub Copilot CLI Best Practices](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices)

### Windsurf (now Devin Desktop): Cascade Planning Mode
- **Wave 10 Planning Mode** (launched 2025):
  - Toggle via icon under prompt box
  - Cascade generates a **persistent, editable markdown plan file** on disk
  - Plan contains goals and tasks, continuously referenced during execution
  - Users can manually edit the plan or ask Cascade to update it
  - If new information (Memories) requires changes, Cascade modifies the plan and notifies user
- **Dual-model architecture**:
  - Larger reasoning model (e.g., `o3`) handles long-term planning
  - User-selected model handles short-term tool-based actions conditional on the plan
- **Theory**: Based on "shared timelines" — short-term actions + long-term reasoning operating on the same joint timeline.
- **Key innovation**: Plan is a persistent, modifiable object on disk — both human and AI can edit it.

**Source**: [Devin Blog — Wave 10: Planning Mode](https://devin.ai/blog/windsurf-wave-10-planning-mode)

---

## 2. Devin / SWE-agent / OpenHands — Multi-Step Task Structuring

### Devin (Cognition AI)
- **Architecture**: Autonomous agent operating in a **sandboxed compute environment** with shell, code editor, and browser.
- **Planning approach**: 
  - "Long-term reasoning and planning" enabling tasks requiring "thousands of decisions"
  - Self-correcting — can recall relevant context at each step and learn over time
  - Operates with a **sandbox → plan → execute → verify** loop
  - Can convert completed workflows into **reusable playbooks** (Devin 2.0)
- **Multi-step handling**:
  - Breaks complex tasks into steps autonomously
  - Runs tests, browses docs, writes code, debugs — all within sandbox
  - Supports **parallel task execution** across multiple tickets
  - Human can take over at any point via embedded IDE
- **Enforcement**: Rule of thumb — "if you can do it in ≤3 hours, Devin likely can too." Clear prompts with explicit completion criteria improve success rate.

**Sources**: [Cognition Blog](https://cognition.ai/blog/introducing-devin), [Devin Docs](https://docs.devin.ai/get-started/devin-intro)

### SWE-agent (Princeton/Stanford)
- **Architecture**: Based on **Agent-Computer Interface (ACI)** design — a deliberately constrained tool set.
- **Planning approach**:
  - **No explicit planning phase** — uses a ReAct-style loop (Reason → Act → Observe)
  - Well-defined action space with constrained tools (navigate file, view lines, edit, run commands)
  - "Leaves maximal agency to the LM" — free-flowing, generalizable
  - Configurable via single YAML file
- **Multi-step handling**:
  - Takes a GitHub issue → autonomously navigates codebase → identifies relevant files → creates patch → validates
  - Iterative: read → understand → edit → test → fix → repeat
  - **mini-swe-agent** (successor): achieves 65% on SWE-bench verified in just 100 lines of Python
- **Error handling**: The agent observes tool output and adapts — if a test fails, it reads the error and modifies its approach.

**Sources**: [SWE-agent Docs](https://swe-agent.com/latest/), [GitHub Repo](https://github.com/swe-agent/swe-agent), [NeurIPS 2024 Paper](https://arxiv.org/abs/2405.15793)

### OpenHands
- **Architecture**: Composable SDK with four packages (sdk, tools, workspace, agent_server).
- **Planning approach**:
  - **DelegatorAgent** acts as orchestrator — breaks tasks into subtasks, dispatches to specialized **micro-agents**
  - Micro-agents are customizable (e.g., "never use GPL dependencies")
  - Event-driven architecture with typed events (actions, observations, messages)
  - **Condenser** manages conversation history compression for token management
- **Multi-step handling**:
  - Agent implements reasoning-action loop
  - Security layer: action risk assessment and validation before execution
  - Supports both local (single process) and production (sandboxed containers) deployment
  - Same agent code works across deployment modes

**Sources**: [OpenHands Docs](https://docs.openhands.dev/sdk/arch/overview), [ICLR 2025 Paper](https://openreview.net/forum?id=OJd3ayDDoF)

---

## 3. OpenAI Codex CLI / Claude Code — Task Decomposition

### OpenAI Codex CLI
- **Architecture**: Single-agent, ReAct-style loop — `Think → Tool Call → Observe → Repeat`
- **Planning approach**:
  - **Implicit planning** — iterates (read → edit → test) rather than producing big upfront plans
  - Shell-first toolkit: `cat`, `grep`, `find`, `ls`, `git`, test/linter execution
  - Strict diff-based editing via `apply_patch` (not full file overwrites)
  - Lazy context loading — only reads what model requests
  - Relies on `AGENTS.md` for project awareness
- **Plan/Spec Mode** (under discussion, GitHub Discussion #7355):
  - OpenAI is exploring explicit planning mode with community input
  - Design axes: modal vs non-modal, ephemeral vs persisted, interview-style vs freeform
  - Community strongly prefers **modal toggle** (like Cursor/Claude Code Shift+Tab)
  - Plans should be **Markdown files**, editable by both human and AI
  - Support both lightweight plans (small bugs) and formal specs (large refactors)
- **Three operational modes**:
  1. **Suggest**: Auto-approve reads; confirm edits/commands
  2. **Auto-Edit**: Apply diffs automatically; confirm commands
  3. **Full Auto**: Full autonomy within sandbox
- **Enforcement**: OS-level sandboxing (macOS Seatbelt, Linux Docker + iptables), blocks system file access, network commands, dangerous patterns.

**Sources**: [ZenML Case Study](https://www.zenml.io/llmops-database/building-production-ready-ai-agents-openai-codex-cli-architecture-and-agent-loop-design), [PromptLayer Deep Dive](https://blog.promptlayer.com/how-openai-codex-works-behind-the-scenes-and-how-it-compares-to-claude-code/), [GitHub Discussion #7355](https://github.com/openai/codex/discussions/7355)

### Claude Code (Anthropic)
- **Architecture**: Single-threaded master loop (`while` loop continues while model responses include tool calls).
- **Planning approach**:
  - **Explicit planning via TodoWrite tool** — creates structured JSON task lists with IDs, content, status, priority
  - **Plan Mode** (Shift+Tab toggle):
    - **Hard enforcement**: Edit, Write, Bash, NotebookEdit, and all MCP write operations are BLOCKED
    - Only read/explore tools available: Read, LS, Glob, Grep, WebFetch, WebSearch, Task (Explore subagent), TodoRead, TodoWrite
    - "Claude physically cannot modify files until you approve the plan"
  - **Parallel subagent exploration**: Spawns multiple Explore subagents (using cheaper Haiku model) simultaneously to explore codebase from different angles
  - Plans saved to `~/.claude/plans/` as plain markdown
- **Task Management Evolution**:
  - **TodoWrite** (legacy): Session-only, ephemeral, single-agent
  - **Tasks API** (v2.1.16+): Disk-persisted (`~/.claude/tasks/`), multi-session, dependency tracking (`blockedBy`), multi-agent coordination
- **Context management**: Compressor triggers at ~92% context utilization, summarizes to long-term Markdown-based project memory (no vector DBs).
- **Enforcement**: 
  - Permission system with explicit allow/deny
  - Risk level classification + safety notes
  - Sanitization blocks injection vectors (backticks, shell expansion)
  - Three modes: Default (approval required), Auto-Accept Edits, Plan Mode

**Sources**: [ZenML Architecture Analysis](https://www.zenml.io/llmops-database/claude-code-agent-architecture-single-threaded-master-loop-for-autonomous-coding), [Claude Code Docs — Tools Reference](https://code.claude.com/docs/en/tools-reference), [paddo.dev — Plan Mode Mandatory](https://paddo.dev/blog/plan-mode-mandatory-auto-compact-yes/)

---

## 4. Plan Failures and Replanning

### Common Patterns Across Agents

| Strategy | Description | Used By |
|----------|-------------|---------|
| **Revert & Replan** | Undo changes, refine plan, re-run from scratch | Cursor (official recommendation) |
| **Iterative Self-Correction** | Agent observes test/lint failures, modifies approach in-loop | SWE-agent, OpenHands, Devin |
| **Mid-Task Steering** | User injects new instructions while agent is working | Claude Code (dual-buffer queue `h2A`) |
| **Plan-as-Contract** | Plan is a persistent file; both human and AI edit it when new info emerges | Windsurf/Cascade, Claude Code |
| **Todo State Re-injection** | After each tool use, TODO state is re-inserted as system message to prevent goal drift | Claude Code |
| **Context Compaction** | At ~92% context, summarize history to preserve important info, prevent drift | Claude Code, Codex CLI |
| **Checkpoint/Rollback** | Git-based checkpoints allow reverting to known-good states | Devin, Cursor |
| **Sub-agent Exploration** | Spawn parallel sub-agents to explore alternatives without polluting main context | Claude Code (Opus 4.5) |
| **Evaluator-Optimizer** | One LLM generates, another evaluates and provides feedback for retry | Anthropic's recommended pattern |

### Key Insights on Failure Handling

1. **Silent failures are the biggest risk**: "Most error recovery discussions assume the agent knows it failed. The scariest failures are the silent ones — the agent thinks it succeeded." (Anthropic SDK discussion)

2. **Validation before execution**: "The best time to catch an agent error is before the operation executes. Validation layers should fail early, fail specifically."

3. **Plan Mode as failure prevention**: "Before Plan Mode, 'plan first' was a request Claude could ignore. Now it's a system constraint Claude cannot bypass."

4. **Diffs-first workflow enables recovery**: Both Codex and Claude Code use minimal diffs → colorized changes → user review → apply → test. This makes rollback trivial.

5. **Stanford framework**: Maps every error to specific modules (memory, planning, reflection, action) and hunts for root causes systematically.

**Sources**: [Anthropic SDK Discussion #1341](https://github.com/anthropics/anthropic-sdk-python/discussions/1341), [DAPLab — 9 Critical Failure Patterns](https://daplab.cs.columbia.edu/general/2026/01/08/9-critical-failure-patterns-of-coding-agents.html), [Towards AI — Building Retries in Agents](https://pub.towardsai.net/building-retries-in-agents-how-to-build-ai-agents-that-survive-failures-32eedd2623f0)

---

## 5. Enforcement Mechanisms

### Config Flags & Mode Toggles

| Agent | Mechanism | Details |
|-------|-----------|---------|
| **Cursor** | `Shift+Tab` toggle | Hard switch between Plan Mode and Agent Mode |
| **Copilot (VS Code)** | Agent dropdown + `/plan` | Selectable Plan agent; `chat.planAgent.defaultModel` config |
| **Copilot CLI** | `Shift+Tab` + autopilot | Toggle plan mode; autopilot for autonomous execution |
| **Windsurf** | Planning icon toggle | Enables persistent plan file on disk |
| **Claude Code** | `Shift+Tab` cycle | Default → Auto-Accept Edits → Plan → Default |
| **Claude Code** | `--enable-auto-mode` flag | CLI flag to enable auto-accept |
| **Claude Code** | `defaultMode: "plan"` in settings.json | Force plan mode as default |
| **Codex CLI** | Three modes | Suggest / Auto-Edit / Full Auto |
| **Codex CLI** | `--oss` flag | Use local models |
| **SWE-agent** | YAML config | Single config file governs entire behavior |
| **OpenHands** | Security policies | Action risk assessment before execution |

### Mandatory Steps & Hard Gates

| Mechanism | Agent | Description |
|-----------|-------|-------------|
| **Tool blocking in Plan Mode** | Claude Code | Edit/Write/Bash physically unavailable — not a suggestion |
| **Approval gates** | Codex CLI | Each mode has different approval requirements |
| **OS-level sandboxing** | Codex CLI | macOS Seatbelt / Linux Docker + iptables |
| **Permission system** | Claude Code | Explicit allow/deny for writes, risky Bash, external tools |
| **Risk classification** | Claude Code, OpenHands | Tools classified by risk level; sanitization blocks injection |
| **User confirmation** | Cursor Plan Mode | Agent cannot proceed to coding without user approval |
| **CI/CD validation** | Devin | "Make tasks easy to verify — CI passes, deployment succeeds" |
| **Diff review** | All | Colorized diffs shown before application |

### User Gates & Human-in-the-Loop

| Pattern | Description | Agents |
|---------|-------------|--------|
| **Plan approval gate** | User must explicitly approve plan before execution begins | Cursor, Claude Code, Copilot, Windsurf |
| **Per-action approval** | Each tool call requires user confirmation (Suggest mode) | Codex CLI, Claude Code (default) |
| **Auto-accept with rollback** | Agent proceeds autonomously; user can revert via git | Cursor, Claude Code (auto-accept), Devin |
| **Full autonomy** | Agent operates without interruption in sandbox | Codex (Full Auto), Devin |
| **Mid-task steering** | User can inject instructions while agent works | Claude Code (dual-buffer), Cursor |
| **Take-over capability** | User can pause agent and manually edit | Devin (embedded IDE) |
| **Handoff** | CLI quick task → cloud agent for longer work | Devin CLI `/handoff` command |

### Anthropic's Recommended Patterns (from "Building Effective Agents")

1. **Prompt Chaining**: Decompose into sequential steps with optional gates between them
2. **Routing**: Classify input → route to specialized logic
3. **Parallelization**: Sectioning (independent subtasks) or Voting (multiple attempts, aggregate)
4. **Orchestrator-Workers**: Central LLM dynamically decomposes → delegates → synthesizes
5. **Evaluator-Optimizer**: Generator + Evaluator in a loop

**Key principle**: "Start simple — optimize single LLM calls before adding agentic complexity. Add complexity only when it demonstrably improves outcomes."

**Sources**: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

---

## Summary Table: Planning Approaches Compared

| Agent | Plans Before Coding? | Plan Format | Enforcement Level | Replanning Strategy |
|-------|---------------------|-------------|-------------------|-------------------|
| **Cursor** | Yes (Plan Mode) | Markdown in `.cursor/plans/` | Hard (mode toggle) | Revert + refine + re-run |
| **Copilot** | Yes (Plan agent) | Session memory `plan.md` | Configurable (model selection) | Iterate on plan in chat |
| **Windsurf** | Yes (Planning Mode) | Persistent markdown file | Hard (mode toggle) | Plan evolves with new info |
| **Devin** | Yes (implicit) | Internal reasoning | Autonomous (sandbox) | Self-correction in loop |
| **SWE-agent** | No (reactive) | N/A | Config (YAML) | Observe → adapt |
| **OpenHands** | DelegatorAgent plans | Event-driven | Security policies | Micro-agent dispatch |
| **Codex CLI** | No (implicit) | N/A (planning mode TBD) | OS sandbox + approval modes | Iterate read→edit→test |
| **Claude Code** | Yes (Plan Mode) | `~/.claude/plans/*.md` | Hard (tool blocking) | TodoWrite + re-injection + steering |

---

## Key Takeaways

1. **Industry convergence on Plan Mode**: Cursor, Copilot, Windsurf, and Claude Code all now offer explicit plan modes with hard enforcement (tool blocking, not just prompt requests).

2. **Markdown as the universal plan format**: All tools that persist plans use Markdown files — editable by both human and AI, versionable, readable.

3. **Shift+Tab as the de facto toggle**: Cursor, Claude Code, and Copilot CLI all use Shift+Tab to cycle modes.

4. **Dual-model architectures emerging**: Windsurf uses `o3` for planning + user model for execution; Claude Code uses Haiku for exploration + Opus for reasoning.

5. **Hard enforcement > soft requests**: The shift from "please plan first" (prompt instruction) to "you physically cannot edit files" (tool blocking) is the most significant evolution.

6. **Replanning is still mostly manual**: Most tools rely on human-driven replanning (revert, edit plan, re-run). Autonomous replanning exists in Devin and OpenHands but is less mature.

7. **Sandboxing is table stakes**: Every production agent uses some form of containment — OS-level (Codex), app-level (Claude Code), or full sandbox (Devin).
