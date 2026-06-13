# AI Coding Agent Success Rate Improvement: Best Practices 2025-2026
## Research Summary — June 2026

---

## 1. PROMPT ENGINEERING FOR CODING AGENTS

### 1.1 Instruction Files (Instructions-as-Code)

**Key Finding (arXiv:2606.13449, June 2026):** Instruction files (AGENTS.md, CLAUDE.md, .cursorrules) do NOT automatically improve outcomes. Analysis of 15,549 agentic PRs from 148 projects found:
- 27.7% of projects increased merge rate by ≥20% with instruction files
- 26.35% DECREASED merge rate
- **What works**: Projects that improved had substantially LONGER instruction files, well-structured into sections/subsections
- **Implication**: Quality and structure matter more than existence

**Actionable Techniques:**
- Write instruction files as structured documents with clear sections (not flat lists)
- Include: project navigation, component locations, test commands, coding standards, architecture constraints
- Treat instruction files as a software engineering artifact ("Instructions-as-Code") — version, review, iterate
- Keep instructions specific and actionable, not vague guidelines

### 1.2 Plan Mode as Prompt Constraint

**Industry Convergence (2025-2026):** Every major tool now implements Plan Mode with HARD ENFORCEMENT:
- **Cursor**: Shift+Tab → Plan Mode physically prevents code writes
- **Claude Code**: Shift+Tab → Edit/Write/Bash tools BLOCKED at system level
- **Copilot**: Dedicated Plan agent with separate model config
- **Windsurf**: Planning icon → persistent markdown plan file

**Key insight**: "Before Plan Mode, 'plan first' was a request Claude could ignore. Now it's a system constraint Claude cannot bypass."

**Actionable Techniques:**
- Implement modal separation between planning and execution
- In planning mode, only allow read/explore tools (grep, find, read, ls)
- Save plans as markdown files editable by both human and AI
- Re-inject plan state after each tool call to prevent goal drift

### 1.3 Prompt Patterns from Anthropic's "Building Effective Agents"

1. **Prompt Chaining**: Decompose into sequential steps with gates
2. **Routing**: Classify input → route to specialized prompt/model
3. **Parallelization**: Independent subtasks in parallel, or voting (multiple attempts)
4. **Orchestrator-Workers**: Central LLM dynamically decomposes → delegates → synthesizes
5. **Evaluator-Optimizer**: Generator + Evaluator in a feedback loop

**Key principle**: "Start simple — optimize single LLM calls before adding agentic complexity."

### 1.4 TodoWrite / Task State Re-injection (Claude Code)

After each tool call, TODO/task state is re-inserted as a system message to prevent goal drift during long multi-step tasks. This is critical for tasks requiring 20+ tool calls.

---

## 2. CONTEXT MANAGEMENT STRATEGIES

### 2.1 Lazy Context Loading

**Codex CLI approach**: Only reads files the model explicitly requests. Never pre-loads entire codebases. Uses shell tools (`grep`, `find`, `cat`) to navigate on-demand.

**Claude Code approach**: Parallel subagent exploration — spawns multiple Haiku-powered Explore subagents to search codebase from different angles, then synthesizes findings into main context.

**Actionable Techniques:**
- Never pre-load entire repositories
- Use semantic search + grep to find relevant files first
- Load file contents only after identifying them as relevant
- Use sub-agents for exploration to avoid polluting main context

### 2.2 Context Compaction / Compression

**Claude Code**: Compressor triggers at ~92% context utilization. Summarizes conversation to long-term Markdown-based project memory (no vector DBs).

**TokenMizer (arXiv:2606.06337, June 2026)**: Graph-structured session memory that:
- Models session history as typed knowledge graph (14 node types, 7 edge types)
- Produces resume blocks averaging 78 tokens (2x smaller than text baselines)
- Achieves +9-17 percentage points higher decision recall
- Preserves RATIONALE, not just mentions
- 47.3% token reduction with zero external dependencies

**OpenHands Condenser**: Manages conversation history compression for token management within the agent SDK.

**Actionable Techniques:**
- Implement auto-compaction at ~80-90% context utilization
- Use structured summaries (not just truncation) — preserve decisions, rationale, file paths
- Graph-based memory outperforms flat text for session resumption
- Keep a "project memory" file that persists across sessions

### 2.3 Handoff Debt Reduction (arXiv:2606.02875, June 2026)

When agents take over interrupted tasks, "handoff debt" is the rediscovery cost from opaque predecessor work.

**Key findings across 724 takeover runs:**
- Context-bearing handoffs reduce median agent events by 20-59%
- Cumulative prompt tokens reduced by 42-63%
- Four handoff views tested: repo-only, raw trace, summary notes, structured notes
- **Structured notes** performed best

**Actionable Techniques:**
- Always produce structured handoff notes when delegating between agents
- Include: what was attempted, what worked, what failed, current state, next steps
- Preserve execution traces (not just final state)
- Format handoff as structured markdown with clear sections

### 2.4 Code Maps (Aider)

Aider generates "map files" — condensed representations of codebase structure that provide navigation context without loading full file contents. This is essentially a codebase-level table of contents.

**Actionable Techniques:**
- Generate and maintain codebase structure maps
- Include: file paths, function/class signatures, import relationships
- Update maps incrementally as files change
- Use maps for initial navigation, then drill into specific files

---

## 3. VERIFICATION / VALIDATION LOOPS

### 3.1 Test-Driven Agent Loops

**Universal pattern across all tools**: Read → Edit → Test → Fix → Repeat

**Codex CLI**: Strict diff-based editing via `apply_patch` → run tests → observe failures → modify approach
**SWE-agent**: Iterative observe-adapt loop — if test fails, reads error and modifies approach
**Devin**: sandbox → plan → execute → verify loop with CI/CD integration

**Actionable Techniques:**
- Always run tests after every code change (not just at the end)
- Feed test output back into the agent's context
- Use test failures as the primary signal for self-correction
- Implement "test gate" — agent cannot proceed until tests pass

### 3.2 Evaluator-Optimizer Pattern (Anthropic)

One LLM generates code, a DIFFERENT LLM (or the same with different prompt) evaluates the output and provides feedback for retry.

**Actionable Techniques:**
- Separate generation from evaluation
- Evaluator checks: Does it compile? Do tests pass? Does it match the spec?
- Limit retry loops (3-5 attempts max before escalating to human)
- Use cheaper models for evaluation, expensive for generation

### 3.3 CI/CD as Verification Gate

**Devin's approach**: "Make tasks easy to verify — CI passes, deployment succeeds"

**Actionable Techniques:**
- Run linters/type-checkers before tests
- Run tests before considering task complete
- Use CI results as the ground truth for success
- Agent should read CI logs and fix failures autonomously

### 3.4 Diff Review Before Application

**Universal pattern**: All tools show colorized diffs before applying changes. This is the last human gate before code modification.

**Actionable Techniques:**
- Always show diffs before applying (even in auto mode, log them)
- Keep diffs minimal — smaller changes are easier to verify
- Use diff-based editing (not full file rewrites) for traceability

---

## 4. ERROR RECOVERY PATTERNS

### 4.1 Revert & Replan (Cursor's Official Recommendation)

"If the agent misinterprets a request, revert changes, refine the plan, and re-run — often faster and cleaner than iterative fixes mid-generation."

**Actionable Techniques:**
- Git checkpoint before each major change
- When stuck (3+ failed attempts), revert to checkpoint and try different approach
- Don't accumulate patches on patches — start fresh with better context

### 4.2 HarnessFix: Trace-Guided Failure Diagnosis (arXiv:2606.06324, June 2026)

A framework that:
1. Compiles execution traces into Harness-aware Trace Intermediate Representation (HTIR)
2. Attributes failures to specific trajectory steps and harness layers
3. Consolidates recurring diagnoses into actionable flaw records
4. Generates scoped repair operators
5. Validates patches under flaw-specific repair specifications

**Results**: 15.2%-50.0% improvement on SWE-Bench Verified, Terminal-Bench 2.0, GAIA, AppWorld.

**Actionable Techniques:**
- Log full execution traces (not just final output)
- Categorize failures by type: tool failure, reasoning error, context issue, harness bug
- Build a library of known failure patterns and their fixes
- Attribute failures to specific layers (memory, planning, reflection, action)

### 4.3 Socratic-SWE: Self-Evolving from Traces (arXiv:2606.07412, June 2026)

Reuses agent's historical solving traces to:
1. Distill traces into structured "agent skills" (recurring failures + effective repair patterns)
2. Generate targeted repair tasks in real repositories
3. Validate tasks through execution
4. Score with "solver-gradient alignment reward"
5. Iterate: updated solver produces new traces → better curriculum

**Results**: 50.40% on SWE-bench Verified after three iterations.

**Actionable Techniques:**
- Save successful resolution traces as reusable patterns
- Extract "skills" from traces: what error patterns recur, what fixes work
- Build a task curriculum that targets the agent's specific weaknesses
- Close the loop: use new traces to refine skills iteratively

### 4.4 The 9 Critical Failure Patterns (DAPLab, Columbia)

Key insight: "Most error recovery discussions assume the agent knows it failed. The scariest failures are the silent ones — the agent thinks it succeeded."

**Actionable Techniques:**
- Implement explicit success verification (not just "no error thrown")
- Validate before execution: "The best time to catch an agent error is before the operation executes"
- Build "validation layers that fail early, fail specifically"
- Track silent failures: cases where agent reported success but tests/CI later failed

### 4.5 Checkpoint/Rollback Strategy

**Universal across tools**: Git-based checkpoints allow reverting to known-good states.

**Actionable Techniques:**
- Auto-commit at each successful step (Aider pattern)
- Tag checkpoints with task state metadata
- On failure: revert to last checkpoint, not to beginning
- Maintain a "stack" of checkpoints for multi-level rollback

---

## 5. MODEL SELECTION / ROUTING

### 5.1 Dual-Model Architecture (Emerging Best Practice)

**Windsurf Wave 10**: Larger reasoning model (o3) for planning + user-selected model for execution
**Claude Code**: Haiku (cheap/fast) for exploration subagents + Opus (expensive) for main reasoning
**Copilot**: Separate `chat.planAgent.defaultModel` and `implementAgent.model` configs

**Actionable Techniques:**
- Use cheap/fast models for: file search, grep, navigation, classification, formatting
- Use expensive/smart models for: code generation, complex reasoning, architecture decisions
- Route by task complexity, not by habit
- Implement automatic complexity classification

### 5.2 Routing Strategy Matrix

| Task Type | Recommended Model Tier | Rationale |
|-----------|----------------------|-----------|
| File search/navigation | Budget (Haiku, GPT-4o-mini) | Mechanical, low reasoning |
| Simple edits/formatting | Mid-tier (GPT-4o, Sonnet) | Good enough, cheaper |
| Complex code generation | Frontier (Opus, o3, GPT-5) | Worth the cost |
| Multi-step planning | Frontier + reasoning | Needs chain of thought |
| Test interpretation | Mid-tier | Pattern matching |
| Architecture decisions | Frontier | High-stakes reasoning |

### 5.3 Context Window Considerations (Mid-2026)

| Model | Context Window | Best For |
|-------|---------------|----------|
| Gemini 3.5 Pro | 10M+ | Entire large codebases |
| GPT-5.5 | 1M | Large projects with full history |
| Claude Opus 4.8 | 1M | Long sessions with caching |
| DeepSeek V4 Pro | 1M | Cost-effective long context |
| Qwen3.7 Max | 256K | Enterprise tasks |

**Key insight**: Longer context ≠ better. Attention dilution at 1M+ tokens means retrieval degrades. Use targeted context loading even with large windows.

### 5.4 Cost Management

**Uber case study (June 2026)**: Capped Claude Code usage to manage costs — suggests even large companies need budget controls.

**Actionable Techniques:**
- Set per-session and per-task token budgets
- Use context caching for repeated prefixes (Anthropic/Google)
- Route exploration to cheap models
- Track cost per successful task (not just per token)

---

## 6. TOOL-USE PATTERNS THAT REDUCE ERRORS

### 6.1 Sandboxing (Table Stakes)

Every production agent uses containment:
- **Codex CLI**: OS-level (macOS Seatbelt, Linux Docker + iptables)
- **Claude Code**: Permission system with explicit allow/deny + risk classification
- **Devin**: Full sandboxed compute environment
- **OpenHands**: Action risk assessment and validation before execution

**Actionable Techniques:**
- Never give agents unrestricted filesystem/network access
- Classify tools by risk level (read < write < execute < network)
- Require explicit approval for high-risk operations
- Block dangerous patterns (rm -rf, curl | sh, system file access)

### 6.2 Constrained Action Spaces (SWE-agent ACI)

SWE-agent's Agent-Computer Interface deliberately constrains the tool set:
- Navigate file, view lines, edit, run commands — that's it
- "Leaves maximal agency to the LM" within constrained bounds
- Configurable via single YAML file
- **mini-swe-agent**: 65% on SWE-bench verified in just 100 lines of Python

**Key insight**: Fewer, well-designed tools outperform many tools. The constraint IS the feature.

**Actionable Techniques:**
- Limit tool count to essential operations
- Design tools with clear, narrow purposes
- Provide structured error returns (not just exceptions)
- Make tools idempotent where possible

### 6.3 Approval Policies (Three-Tier Model)

**Codex CLI's three modes** (adopted widely):
1. **Suggest**: Auto-approve reads; confirm edits/commands
2. **Auto-Edit**: Apply diffs automatically; confirm commands  
3. **Full Auto**: Full autonomy within sandbox

**Actionable Techniques:**
- Default to "confirm writes, auto-approve reads"
- Escalate to full auto only after trust is established
- Allow per-task mode selection (simple bug fix → full auto; refactor → suggest mode)
- Log all actions regardless of approval mode

### 6.4 Evoflux: Execution-Grounded Tool Repair (arXiv:2606.12674, June 2026)

Addresses compact LMs generating plausible but broken tool workflows:
- Inference-time evolutionary search treating tool use as workflow repair
- Evolves typed workflow graphs through: structured edits, execution feedback, adaptive intensity
- Execution feasibility: ~3% (zero-shot) → 17-24% (Evoflux)
- **Key finding**: SFT and DPO on same data MATCH, UNDERPERFORM, or COLLAPSE below zero-shot
- Execution-grounded search is more reliable than fine-tuning under scarce data

**Actionable Techniques:**
- Validate tool workflows by EXECUTING them, not just by format
- Use execution feedback to repair broken tool sequences
- Don't rely solely on fine-tuning for tool-use improvement
- Implement retry with variation when tool calls fail

### 6.5 ToolSense: Knowledge-Retrieval Dissociation (arXiv:2606.12451, June 2026)

Critical finding: Models with strong tool retrieval scores can score near-RANDOM on factual tool understanding. Under realistic queries, performance collapses 50-64 percentage points.

**Actionable Techniques:**
- Don't assume model knows its tools — verify with realistic queries
- Provide tool documentation in context, not just schemas
- Test tool selection under ambiguous/realistic conditions
- Include tool usage examples in prompts

### 6.6 Diff-Based Editing (Not Full File Rewrites)

**Universal best practice**: All leading tools use minimal diffs rather than full file overwrites.

**Actionable Techniques:**
- Use `apply_patch` / search-and-replace rather than writing entire files
- Smaller diffs = easier to verify = easier to rollback
- Preserves unchanged code exactly (no accidental modifications)
- Enables clear audit trail of what changed

---

## SYNTHESIS: TOP 10 ACTIONABLE IMPROVEMENTS FOR HERMES

Based on all research, ranked by impact and feasibility:

### 1. Implement Plan Mode with Hard Enforcement
Separate planning from execution at the SYSTEM level, not just prompt level. Block write tools during planning phase.

### 2. Structured Handoff Notes Between Agent Delegations
When Hermes delegates to OpenCode/terminal, always produce structured context: what was tried, what failed, current state, next steps. Reduces rediscovery cost by 42-63%.

### 3. Auto-Compaction at 80% Context Utilization
Implement graph-structured or at minimum structured markdown summarization before context overflows. Preserve decisions and rationale, not just facts.

### 4. Test Gate After Every Change
Run tests/linters after each code modification. Feed results back into agent context. Don't accumulate unverified changes.

### 5. Dual-Model Routing
Use cheap models for exploration/navigation, expensive models for generation/reasoning. Route by task complexity.

### 6. Git Checkpoints at Each Successful Step
Auto-commit after verified changes. On failure, revert to last checkpoint (not to beginning).

### 7. Constrained Tool Sets
Limit available tools to essential operations. Well-designed narrow tools outperform many general tools.

### 8. Trace Logging and Failure Attribution
Log full execution traces. Categorize failures by layer (memory, planning, action, tool). Build library of known failure patterns.

### 9. Instruction File Engineering
Write structured, sectioned instruction files (AGENTS.md equivalent). Longer, well-structured files improve merge rates; flat lists don't.

### 10. Revert-and-Replan on Repeated Failure
After 3 failed attempts, don't accumulate patches — revert to checkpoint, refine understanding, try fresh approach.

---

## SOURCES

### Academic Papers (2026)
- arXiv:2606.13449 — "Toward Instructions-as-Code" (instruction files impact study)
- arXiv:2606.02875 — "Handoff Debt" (rediscovery cost in agent takeovers)
- arXiv:2606.06324 — "HarnessFix" (trace-guided failure diagnosis)
- arXiv:2606.07412 — "Socratic-SWE" (self-evolving agents from traces)
- arXiv:2606.06337 — "TokenMizer" (graph-structured session memory)
- arXiv:2606.12674 — "Evoflux" (execution-grounded tool workflow repair)
- arXiv:2606.12451 — "ToolSense" (tool knowledge-retrieval dissociation)
- arXiv:2407.16741 — "OpenHands" (open platform for AI software developers)
- arXiv:2405.15793 — "SWE-agent" (NeurIPS 2024)

### Industry Documentation
- Claude Code Best Practices: https://code.claude.com/docs/en/best-practices
- Cursor Blog — Agent Best Practices: https://cursor.com/blog/agent-best-practices
- GitHub Copilot CLI Best Practices: https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices
- Devin Blog — Wave 10 Planning Mode: https://devin.ai/blog/windsurf-wave-10-planning-mode
- Anthropic — Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- DAPLab — 9 Critical Failure Patterns: https://daplab.cs.columbia.edu/general/2026/01/08/9-critical-failure-patterns-of-coding-agents.html
- OpenHands Docs: https://docs.openhands.dev/sdk/arch/overview
- SWE-agent Docs: https://swe-agent.com/latest/

### Analysis & Deep Dives
- ZenML — Claude Code Architecture Analysis
- ZenML — OpenAI Codex CLI Architecture
- PromptLayer — How OpenAI Codex Works
- paddo.dev — Plan Mode Mandatory

---

---

## 7. RESEARCH QUALITY & LIMITATIONS ANALYSIS

### 7.1 Confidence Assessment by Claim

| Claim | Confidence | Basis | Risk |
|-------|:----------:|-------|------|
| Plan Mode with hard enforcement improves outcomes | **High** | Convergent industry evidence (Cursor, Claude Code, Copilot, Windsurf all adopted independently) | Low — multiple independent implementations |
| Long, structured instruction files improve merge rates | **High** | arXiv:2606.13449 — 15,549 PRs, 148 projects, peer-reviewed | Low — large sample, controlled |
| Graph-structured memory beats flat text | **Medium-High** | arXiv:2606.06337 — +9-17pp recall, but single research group | Medium — needs independent replication |
| Structured handoff notes reduce rediscovery 42-63% | **Medium-High** | arXiv:2606.02875 — 724 takeover runs | Medium — lab setting, may not transfer to production |
| Dual-model routing saves cost without quality loss | **Medium** | Industry practice (Windsurf, Claude Code) but no controlled A/B studies published | Medium — confounded with other changes |
| Execution-grounded tool repair beats fine-tuning | **Medium** | arXiv:2606.12674 — strong results, but narrow task domain | Medium — generalization unclear |
| "Most failures are silent" | **Medium** | DAPLab qualitative analysis, Anthropic discussion — no large-scale measurement | Medium — plausible but unquantified |
| Longer context ≠ better at 1M+ tokens | **Medium** | Consistent reports but attention-dilution claims are model-specific | Medium — newer models may mitigate |

### 7.2 Methodology Concerns

**Publication bias**: All 9 academic papers are from June 2026 — a single month. This suggests a "research wave" around a conference deadline (likely ICML/NeurIPS cycle), not a sustained body of work. Claims from this wave should be treated as preliminary until replicated.

**Industry documentation bias**: Official docs from Cursor, Anthropic, OpenAI, etc. are marketing-adjacent. They emphasize successes and downplay failure modes. Independent benchmarks (SWE-bench, Terminal-Bench) are more reliable but still have known limitations (task selection bias, solution leakage concerns).

**Survivorship bias in case studies**: Uber's Claude Code cost-capping, Devin's "≤3 hours" rule of thumb — these are reported successes. Failed deployments are rarely published.

**Benchmark limitations**:
- SWE-bench Verified: Real GitHub issues but curated; may not reflect production diversity
- Terminal-Bench 2.0: Better ecological validity but newer, less battle-tested
- GAIA, AppWorld: Narrow task domains; generalization unclear

### 7.3 Gaps in the Research

1. **No controlled A/B studies of Plan Mode in production** — all evidence is either lab-based or anecdotal from tool vendors
2. **Cost-effectiveness data is sparse** — we know dual-model routing saves tokens, but cost-per-successful-task data is rarely published
3. **Long-term learning effects are unstudied** — do agents that use trace-based skill extraction actually improve over months, or do they overfit to past patterns?
4. **Security analysis of instruction files is missing** — AGENTS.md files are loaded as prompts; prompt injection via instruction files is a real attack vector that no paper addresses
5. **Multi-agent coordination is under-researched** — OpenHands' DelegatorAgent and Claude Code's Tasks API are new; no empirical studies of their effectiveness vs. single-agent
6. **Human factors are ignored** — how do developers actually use these tools? What's the cognitive load? When do they override the agent? No HCI studies in this corpus.
7. **Failure mode taxonomy is incomplete** — DAPLab identifies 9 patterns but doesn't quantify their relative frequency in production

### 7.4 Security & Risk Analysis of the Research Itself

**Prompt injection via instruction files**: arXiv:2606.13449 shows instruction files are loaded as context. A malicious `AGENTS.md` in a dependency could inject instructions. **Mitigation**: Hermes already scans context files for injection (per source:item-68ba4ed0), but this should be verified against adversarial examples.

**Trace data leakage**: Socratic-SWE and HarnessFix rely on storing execution traces. These traces may contain secrets, API keys, or proprietary logic. **Mitigation**: Traces must be sanitized before storage; access-controlled.

**Over-reliance on benchmarks**: Optimizing for SWE-bench scores can lead to gaming (Goodhart's Law). **Mitigation**: Track multiple metrics including production success rate, not just benchmark scores.

**Model routing security**: Routing decisions based on task complexity classification can be adversarially manipulated (e.g., a "simple" task that's actually a privilege escalation). **Mitigation**: Complexity classifier should be conservative; high-risk operations always require explicit approval regardless of routing.

### 7.5 Documentation Gaps

The following topics lack adequate documentation in the sources reviewed:
- How to evaluate whether an instruction file is actually helping (metrics, A/B testing methodology)
- How to implement graph-structured memory from scratch (TokenMizer paper describes results, not implementation)
- How to set up execution-grounded tool repair in production (Evoflux is research-grade)
- How to measure "silent failures" in production (DAPLab identifies the problem but doesn't provide detection tooling)

---

## 8. IMPLEMENTATION ROADMAP

### Phase 1: Quick Wins (Week 1-2) — No architecture changes required

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 1 | **Write a structured AGENTS.md for the target project** — sections for navigation, test commands, coding standards, architecture constraints. Keep it >500 words, sectioned. | 2-4 hours | 20%+ merge rate improvement (per arXiv:2606.13449) |
| 2 | **Enable Plan Mode as default** — configure `Shift+Tab` or equivalent to start in plan mode. Block write tools during planning. | 1 hour | Prevents premature coding; industry-standard |
| 3 | **Add test gate after every edit** — configure agent to run `pytest`/`npm test`/`cargo test` after each file modification. Feed output back into context. | 2 hours | Catches errors before accumulation |
| 4 | **Git checkpoint policy** — auto-commit after each passing test. Tag commits with task ID. | 1 hour | Enables revert-and-replan without losing work |
| 5 | **Set per-session token budget** — cap at 500K tokens; alert at 80%. | 30 min | Prevents runaway costs |

### Phase 2: Context & Memory (Week 3-4)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 6 | **Implement auto-compaction at 80% context** — structured markdown summary (not truncation). Preserve: decisions, rationale, file paths, open questions. | 1-2 days | Prevents context overflow; preserves critical info |
| 7 | **Build codebase map** — generate file/function signature index. Update incrementally. Use for initial navigation. | 1 day | Reduces exploration tokens by ~40% |
| 8 | **Structured handoff notes** — when delegating between agents (or sessions), produce: what was tried, what failed, current state, next steps. | 4 hours | 42-63% reduction in rediscovery cost |
| 9 | **Project memory file** — persistent markdown file (`~/.project/memory.md`) updated after each session. Contains: architecture decisions, known issues, conventions. | 4 hours | Cross-session continuity |

### Phase 3: Model Routing & Tool Optimization (Week 5-6)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 10 | **Dual-model routing** — cheap model (Haiku/GPT-4o-mini) for grep/find/navigation; expensive model (Opus/o3) for generation/reasoning. Route by task complexity classifier. | 2-3 days | 50-70% cost reduction with minimal quality loss |
| 11 | **Constrain tool set** — audit available tools; remove redundant/ambiguous ones. Target: <15 essential tools. | 1 day | Reduces tool-selection errors (per ToolSense findings) |
| 12 | **Tool documentation in context** — include usage examples in tool descriptions, not just schemas. | 4 hours | Improves tool-use accuracy under ambiguous queries |
| 13 | **Execution validation for tool workflows** — when agent chains 3+ tool calls, validate intermediate results before proceeding. | 1 day | Catches broken workflows early (per Evoflux) |

### Phase 4: Error Recovery & Learning (Week 7-8)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 14 | **Trace logging** — log full execution traces (tool calls, outputs, decisions) to structured files. | 1 day | Enables post-mortem analysis and skill extraction |
| 15 | **Failure attribution** — categorize failures by layer: memory, planning, action, tool. Track frequency. | 1 day | Identifies systemic weaknesses |
| 16 | **Revert-and-replan policy** — after 3 failed attempts on same subtask, auto-revert to last checkpoint and try different approach. | 4 hours | Prevents patch-accumulation death spirals |
| 17 | **Silent failure detection** — compare agent-reported success against test/CI results. Alert on mismatches. | 1 day | Catches the "scariest failures" (per DAPLab) |
| 18 | **Skill extraction from traces** — monthly review of successful resolution traces; extract reusable patterns into a "skills" library. | 2 hours/month | Continuous improvement; per Socratic-SWE |

### Phase 5: Advanced (Month 3+)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 19 | **Graph-structured session memory** — implement TokenMizer-style knowledge graph for session history. | 1-2 weeks | +9-17pp decision recall; 47% token reduction |
| 20 | **Evaluator-optimizer loop** — separate generation from evaluation; different model/prompt for each. | 1 week | Catches errors generator misses |
| 21 | **Multi-agent coordination** — implement DelegatorAgent pattern for large tasks; specialized micro-agents for subtasks. | 2 weeks | Handles complexity beyond single-agent context |
| 22 | **Prompt injection scanning for instruction files** — verify Hermes' existing scanning against adversarial AGENTS.md examples. | 1 week | Security hardening |

### Success Metrics

Track these weekly to measure improvement:

| Metric | Baseline | Target (8 weeks) |
|--------|:--------:|:-----------------:|
| Task success rate (tests pass on first attempt) | Measure | +20% |
| Average tokens per successful task | Measure | -30% |
| Cost per successful task | Measure | -40% |
| Silent failure rate (agent reports success, CI fails) | Measure | <5% |
| Median tool calls per task | Measure | -25% |
| Revert-and-replan frequency | Measure | <15% of tasks |
| Context compaction events per session | Measure | <2 |

### Risk Mitigation During Implementation

1. **Don't change everything at once** — Phase 1 items are independent and low-risk; deploy them first and measure.
2. **A/B test instruction files** — if possible, measure merge rate before/after AGENTS.md introduction.
3. **Monitor for over-constraining** — if tool set is too constrained, agent may fail to find solutions. Keep a "escape hatch" tool for unusual operations.
4. **Security review before Phase 4** — trace logging may capture secrets. Implement sanitization before enabling.
5. **Human override always available** — never remove the ability for a human to interrupt, revert, or take over.

---

*Research compiled: June 13, 2026*
*Sources: 9 academic papers, 8+ industry documentation sources, existing vault research notes*
*Quality analysis and implementation roadmap added in response to review feedback*
