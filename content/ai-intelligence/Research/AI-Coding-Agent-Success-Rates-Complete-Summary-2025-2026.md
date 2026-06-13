# AI Coding Agent Success Rates: Best Practices 2025-2026
## Structured Research Summary — June 2026

**Task**: Research latest best practices for improving AI coding agent success rates in production.
**Focus Areas**: (1) Failure detection & self-healing, (2) Cost-aware model routing, (3) Context window management, (4) Model profiling & task-specific routing.
**Sources**: 16 academic papers (2025-2026), 10+ industry docs (Cursor, Claude Code, Codex, Windsurf/Devin, Copilot, SWE-agent, OpenHands), open-source frameworks.

---

## EXECUTIVE SUMMARY

The production AI coding agent landscape has converged on several best practices through independent implementation across Cursor, Claude Code, Codex CLI, Windsurf, Copilot, and Devin. Key findings:

- **Plan Mode with hard enforcement** (tool blocking, not just prompt requests) is now universal
- **Dual-model architectures** (cheap for exploration, expensive for reasoning) are standard
- **94% of developers fail to detect agent sabotage** in long sessions — automated verification is non-negotiable
- **Coding agents face 100% skill-injection success rates** — domain-specific hardening required
- **Graph-structured memory** outperforms flat text by +9-17pp on decision recall
- **No single agent framework dominates** — framework choice matters as much as model choice

---

## 1. AUTOMATED FAILURE PATTERN DETECTION & SELF-HEALING WORKFLOWS

### 1.1 The 9 Critical Failure Patterns (DAPLab, Columbia, 2026)

**Key insight**: "Most error recovery discussions assume the agent knows it failed. The scariest failures are the silent ones — the agent thinks it succeeded."

| Failure Pattern | Description | Detection Method |
|----------------|-------------|------------------|
| Silent success | Agent reports success but tests/CI fail | Compare agent output vs. test results |
| Goal drift | Agent loses track of original objective over 20+ tool calls | TodoWrite state re-injection |
| Context overflow | Critical info lost during compaction | Structured summarization (not truncation) |
| Tool misuse | Wrong tool or wrong parameters | Execution validation before proceeding |
| Patch accumulation | Stacking failed fixes on failed fixes | Checkpoint/revert after 3 failures |
| Hallucinated APIs | Inventing functions that don't exist | Compile/lint gate after every edit |
| Dependency confusion | Importing malicious/wrong packages | Audit all new imports |
| Infinite loops | Agent retries same failing approach | Attempt counter with escalation |
| Security bypass | Agent circumvents sandbox/permissions | Permission system + risk classification |

### 1.2 HarnessFix: Trace-Guided Failure Diagnosis (arXiv:2606.06324)

A framework that compiles execution traces into a structured intermediate representation, attributes failures to specific trajectory steps and harness layers, and generates scoped repair operators.

**Results**: 15.2%-50.0% improvement on SWE-Bench Verified, Terminal-Bench 2.0, GAIA, AppWorld.

**Implementation pattern**:
1. Log full execution traces (tool calls, outputs, decisions, timestamps)
2. Categorize failures by layer: memory, planning, reflection, action, tool
3. Build a library of known failure patterns and their fixes
4. Attribute failures to specific steps in the trajectory
5. Generate repair operators scoped to the failure type
6. Validate patches under flaw-specific specifications

### 1.3 Socratic-SWE: Self-Evolving from Traces (arXiv:2606.07412)

Reuses agent's historical solving traces to continuously improve:
1. Distill traces into structured "agent skills" (recurring failures + effective repair patterns)
2. Generate targeted repair tasks in real repositories
3. Validate tasks through execution
4. Score with "solver-gradient alignment reward"
5. Iterate: updated solver produces new traces → better curriculum

**Results**: 50.40% on SWE-bench Verified after three iterations.

### 1.4 Evoflux: Execution-Grounded Tool Repair (arXiv:2606.12674)

Addresses compact LMs generating plausible but broken tool workflows:
- Inference-time evolutionary search treating tool use as workflow repair
- Evolves typed workflow graphs through: structured edits, execution feedback, adaptive intensity
- Execution feasibility: ~3% (zero-shot) → 17-24% (Evoflux)
- **Key finding**: SFT and DPO on same data MATCH, UNDERPERFORM, or COLLAPSE below zero-shot
- Execution-grounded search is more reliable than fine-tuning under scarce data

### 1.5 Self-Healing Workflow Architecture

**Universal pattern across all production tools**: Read → Edit → Test → Fix → Repeat

```
┌─────────────────────────────────────────────────────────────┐
│                    SELF-HEALING LOOP                         │
├─────────────────────────────────────────────────────────────┤
│  1. Execute action (code edit, tool call, command)          │
│  2. Verify outcome (tests, linters, compile check)          │
│  3. If failure:                                             │
│     a. Log full trace (action, output, error)               │
│     b. Attribute failure to layer (memory/planning/action)  │
│     c. Check failure pattern library for known fix          │
│     d. If known: apply repair operator                      │
│     e. If unknown: attempt 3 variations, then escalate      │
│  4. If 3+ failures on same subtask:                         │
│     a. Revert to last checkpoint                            │
│     b. Replan with fresh context                            │
│     c. Try different approach                               │
│  5. Extract skill from successful repair                    │
│  6. Update failure pattern library                          │
└─────────────────────────────────────────────────────────────┘
```

### 1.6 Actionable Recommendations for Failure Detection

| Recommendation | Effort | Impact | Source |
|---------------|:------:|--------|--------|
| Log full execution traces (not just final output) | 1 day | Enables post-mortem + skill extraction | HarnessFix, Socratic-SWE |
| Implement test gate after every code change | 2 hours | Catches errors before accumulation | Universal pattern |
| Build failure pattern library (categorized by layer) | 1 week | Reusable repairs; 15-50% improvement | HarnessFix |
| Auto-revert after 3 failed attempts on same subtask | 4 hours | Prevents patch-accumulation death spirals | Cursor official recommendation |
| Silent failure detection: compare agent success vs. CI | 1 day | Catches "scariest failures" | DAPLab |
| Trace-based skill extraction (monthly review) | 2 hrs/month | Continuous improvement | Socratic-SWE |
| Execution validation for tool workflows (3+ calls) | 1 day | Catches broken workflows early | Evoflux |

---

## 2. COST-AWARE MODEL ROUTING STRATEGIES

### 2.1 Dual-Model Architecture (Industry Standard 2025-2026)

Every major production agent now uses a dual-model approach:

| Agent | Planning/Exploration Model | Execution/Reasoning Model |
|-------|---------------------------|--------------------------|
| **Windsurf Wave 10** | o3 (reasoning) | User-selected model |
| **Claude Code** | Haiku (cheap/fast) for Explore subagents | Opus (expensive) for main reasoning |
| **Copilot** | `chat.planAgent.defaultModel` (configurable) | `implementAgent.model` (configurable) |
| **Codex CLI** | Shell tools (no model needed) for navigation | Main model for generation |

**Cost savings**: 50-70% reduction with minimal quality loss when routing exploration to cheap models.

### 2.2 Routing Strategy Matrix

| Task Type | Recommended Model Tier | Cost/Tok | Rationale |
|-----------|----------------------|----------|-----------|
| File search/navigation | Budget (Haiku, GPT-4o-mini) | $0.0001-0.0003 | Mechanical, low reasoning |
| Grep/find/ls operations | No model (shell tools) | $0 | Pure pattern matching |
| Simple edits/formatting | Mid-tier (GPT-4o, Sonnet) | $0.003-0.005 | Good enough, cheaper |
| Complex code generation | Frontier (Opus, o3, GPT-5) | $0.015-0.06 | Worth the cost |
| Multi-step planning | Frontier + reasoning | $0.015-0.06 | Needs chain of thought |
| Test interpretation | Mid-tier | $0.003-0.005 | Pattern matching |
| Architecture decisions | Frontier | $0.015-0.06 | High-stakes reasoning |
| Code review/evaluation | Mid-tier (different from generator) | $0.003-0.005 | Evaluator-optimizer pattern |
| Documentation generation | Mid-tier | $0.003-0.005 | Formulaic, low reasoning |

### 2.3 Complexity Classification for Routing

**Automatic routing requires a complexity classifier**:

```
Input: Task description + codebase context
Output: Model tier (budget / mid / frontier)

Features:
- Number of files likely affected (1 → budget, 10+ → frontier)
- Requires reasoning about architecture (yes → frontier)
- Requires understanding business logic (yes → mid/frontier)
- Mechanical transformation (yes → budget)
- Multi-step dependencies (yes → frontier)
- Security-sensitive (yes → frontier + human approval)
```

**Conservative default**: When uncertain, route to mid-tier. Only route to budget for clearly mechanical tasks.

### 2.4 Cost Management Techniques

| Technique | Savings | Implementation |
|-----------|---------|----------------|
| Context caching (Anthropic/Google) | 50-90% on repeated prefixes | Enable prompt caching for system prompts |
| Per-session token budget | Prevents runaway costs | Cap at 500K tokens; alert at 80% |
| Per-task token budget | Limits individual task cost | Estimate complexity → set budget |
| Route exploration to cheap models | 50-70% cost reduction | Dual-model architecture |
| Compaction before overflow | Reduces total tokens | Auto-compact at 80% utilization |
| Track cost per successful task | Measures true efficiency | Not just cost per token |
| Uber-style usage caps | Hard ceiling on spend | Daily/weekly limits per user/project |

### 2.5 Framework Selection Impact on Cost (ADK Arena, arXiv:2606.05548)

**Key finding**: Generation cost varies 5.6× across frameworks ($0.6 to $3.4 per agent) — proxy for API complexity. Cost alone does not predict success.

**Implication**: Framework choice affects cost as much as model choice. A well-designed framework with fewer API calls can be cheaper than a poorly-designed one even with the same model.

### 2.6 Actionable Recommendations for Cost-Aware Routing

| Recommendation | Effort | Expected Savings |
|---------------|:------:|-----------------|
| Implement dual-model routing (cheap for exploration, expensive for reasoning) | 2-3 days | 50-70% cost reduction |
| Enable context caching for system prompts and repeated prefixes | 1 day | 50-90% on cached portions |
| Set per-session and per-task token budgets | 2 hours | Prevents runaway costs |
| Build complexity classifier for automatic routing | 1 week | Consistent routing decisions |
| Track cost per successful task (not just per token) | 4 hours | Measures true efficiency |
| Audit framework API call patterns | 1 day | Identifies unnecessary calls |
| Conservative default routing (mid-tier when uncertain) | 0 hours | Prevents quality loss from over-optimization |

---

## 3. CONTEXT WINDOW MANAGEMENT FOR LONG CODING SESSIONS

### 3.1 The Context Window Challenge

Long coding sessions (20+ tool calls, multi-hour tasks) face three problems:
1. **Context overflow**: Hitting the model's token limit
2. **Attention dilution**: Performance degrades at 1M+ tokens even if technically within limit
3. **Goal drift**: Agent loses track of original objective over many steps

### 3.2 Lazy Context Loading (Universal Best Practice)

**Codex CLI approach**: Only reads files the model explicitly requests. Never pre-loads entire codebases. Uses shell tools (`grep`, `find`, `cat`) to navigate on-demand.

**Claude Code approach**: Parallel subagent exploration — spawns multiple Haiku-powered Explore subagents to search codebase from different angles, then synthesizes findings into main context.

**Key principle**: Never pre-load entire repositories. Use semantic search + grep to find relevant files first, then load only what's needed.

### 3.3 Context Compaction / Compression

**Claude Code**: Compressor triggers at ~92% context utilization. Summarizes conversation to long-term Markdown-based project memory (no vector DBs).

**TokenMizer (arXiv:2606.06337)**: Graph-structured session memory that:
- Models session history as typed knowledge graph (14 node types, 7 edge types)
- Produces resume blocks averaging 78 tokens (2x smaller than text baselines)
- Achieves +9-17 percentage points higher decision recall
- Preserves RATIONALE, not just mentions
- 47.3% token reduction with zero external dependencies

**Implementation pattern**:
1. Monitor context utilization (track tokens used vs. limit)
2. Trigger compaction at 80% utilization (not 92% — leave buffer)
3. Summarize using structured format (not truncation):
   - Decisions made and rationale
   - Files modified and why
   - Open questions and blockers
   - Next steps planned
4. Store summary as persistent project memory file
5. Re-inject summary as system message after compaction

### 3.4 Handoff Debt Reduction (arXiv:2606.02875)

When agents take over interrupted tasks, "handoff debt" is the rediscovery cost from opaque predecessor work.

**Key findings across 724 takeover runs**:
- Context-bearing handoffs reduce median agent events by 20-59%
- Cumulative prompt tokens reduced by 42-63%
- Four handoff views tested: repo-only, raw trace, summary notes, structured notes
- **Structured notes performed best**

**Structured handoff format**:
```markdown
## Handoff Notes — [Task ID] — [Timestamp]

### What Was Attempted
- [List of actions taken]

### What Worked
- [Successful approaches]

### What Failed
- [Failed approaches and why]

### Current State
- [Files modified, tests passing/failing, blockers]

### Next Steps
- [Recommended approach for successor]

### Key Context
- [Critical information that must be preserved]
```

### 3.5 Decision-Aware Context Loading (arXiv:2606.08151 — CICL)

**Critical finding**: Not all context is equal. A single high-utility memory card can be worth more than all other context combined.

CICL turns instance evidence into a context graph, scores units by:
- **Action shift**: Would this evidence change the agent's next action?
- **Outcome uplift**: Does including this improve success rate?
- **Necessity**: Is this required for the task?
- **Negative-transfer risk**: Could this mislead the agent?

**Results (50 SWE-bench Verified file-retrieval instances)**:
- Hit@1: 0.58 → 0.78 (Qwen3.6-plus reranking of BM25 top-50)
- MRR@10: 0.634 → 0.790
- Removing top-utility semantic unit collapses F1 to 0.000 — proves decision-criticality

**Implementation pattern**:
1. Score context units by decision impact, not just relevance
2. Prioritize "action shift" — evidence that would change the next action
3. Pack high-utility evidence as structured cards (not raw text dumps)
4. Budget context by utility, not just token count
5. Test: removing your top-ranked context unit should cause measurable performance drop

### 3.6 Microskill Architecture for Large Projects (arXiv:2606.05720)

Applies microservices principles to knowledge encapsulation. Instead of feeding the entire codebase, partitions knowledge into atomic, sharply scoped "skill capsules."

**Results (enterprise CMS, 15 features)**:
- Token consumption cut by over 90%
- First-try compilation success rate nearly doubled
- Architectural violations eliminated entirely
- 7 new skill capsules autonomously extracted via self-learning

**Implementation pattern**:
1. Partition project knowledge into atomic, self-contained skill capsules
2. Each capsule: one concept, one pattern, one API — sharply scoped
3. Build a router that selects capsules by semantic relevance to current task
4. Allow autonomous extraction of new capsules from successful task completions
5. Treat capsule library as a living artifact that evolves with the project

### 3.7 Code Maps (Aider Pattern)

Generate "map files" — condensed representations of codebase structure that provide navigation context without loading full file contents.

**Contents**:
- File paths and directory structure
- Function/class signatures
- Import relationships
- Module dependencies

**Usage**: Use maps for initial navigation, then drill into specific files only after identifying them as relevant.

### 3.8 TodoWrite / Task State Re-injection (Claude Code)

After each tool call, TODO/task state is re-inserted as a system message to prevent goal drift during long multi-step tasks.

**Why it works**: Models have limited attention over long contexts. Re-injecting the task state keeps the objective salient.

**Implementation**: Maintain a structured task list (JSON or markdown) with:
- Task ID
- Description
- Status (pending/in-progress/completed/blocked)
- Priority
- Dependencies

Re-inject this list as a system message after every tool call.

### 3.9 Actionable Recommendations for Context Management

| Recommendation | Effort | Impact |
|---------------|:------:|--------|
| Never pre-load entire repositories; use grep/search first | 0 hours (design choice) | Reduces initial context by 80%+ |
| Auto-compact at 80% context utilization (structured summary) | 1-2 days | Prevents overflow; preserves critical info |
| Use graph-structured memory (TokenMizer-style) for session history | 1-2 weeks | +9-17pp decision recall; 47% token reduction |
| Produce structured handoff notes when delegating between agents | 4 hours | 42-63% reduction in rediscovery cost |
| Score context by decision impact, not just relevance (CICL) | 1 week | Higher-quality context; hit@1 0.58→0.78 |
| Partition large projects into skill capsules with dynamic router | 2 weeks | 90% token reduction; doubled compilation success |
| Re-inject task state after every tool call | 4 hours | Prevents goal drift in 20+ step tasks |
| Maintain persistent project memory file across sessions | 4 hours | Cross-session continuity |
| Generate and maintain codebase structure maps | 1 day | Reduces exploration tokens by ~40% |

---

## 4. MODEL PROFILING & TASK-SPECIFIC ROUTING

### 4.1 Framework Selection Matters as Much as Model Selection (ADK Arena, arXiv:2606.05548)

Evaluates 51 Python Agent Development Kit frameworks (204 agent-benchmark pairs) using "LLM-as-a-Developer" methodology — holds the developer constant, varies only the framework.

**Key findings**:
- No single framework dominates: best single-benchmark agents resolve up to 80% of tasks
- Median framework resolves only 32% of tasks
- Generation cost varies 5.6× across frameworks ($0.6 to $3.4 per agent)
- Cost alone does not predict success
- Genuine framework usage stays within narrow 28-40% band regardless of information source
- Documentation, source code, and parametric knowledge are largely substitutable

**Implication**: Framework choice affects agent performance as much as model choice. Test multiple frameworks on representative tasks before committing.

### 4.2 Agent Complementarity (TensorBench, arXiv:2606.05570)

Benchmarks coding agents on a compiler-based tensor framework (199 tasks) across 7 agents and 3 frontier model families.

**Critical finding**: Agents pass DIFFERENT subsets of tasks: pairwise Cohen's κ = -0.07 to 0.43. Even the two strongest agents show κ = 0.05 — near-orthogonal success patterns.

**Implication**: No single agent dominates. Ensemble/complementary approaches are needed for broad coverage.

### 4.3 Task-Specific Routing Matrix

Based on research findings, route tasks to specialized agents/models:

| Task Category | Best Agent/Model | Rationale | Confidence |
|--------------|-----------------|-----------|:----------:|
| **Bug fixes (single file)** | SWE-agent / mini-swe-agent | Constrained action space; 65% on SWE-bench | High |
| **Multi-file refactoring** | Claude Code (Opus) + Plan Mode | Hard enforcement; structured planning | High |
| **Codebase exploration** | Claude Code (Haiku subagents) | Parallel exploration; cheap | High |
| **Test generation** | Codex CLI (Full Auto) | Shell-first; iterative test-run | Medium |
| **Architecture decisions** | Frontier model (Opus/o3) + human review | High-stakes reasoning | High |
| **Documentation** | Mid-tier model (Sonnet/GPT-4o) | Formulaic; low reasoning | Medium |
| **Security-sensitive changes** | Frontier model + human approval + sandbox | Risk mitigation | High |
| **Dependency management** | OpenHands (DelegatorAgent) | Micro-agent specialization | Medium |
| **Compiler/framework-specific** | Specialized agent (TensorBench findings) | Domain expertise matters | High |

### 4.4 Model Profiling Methodology

To determine which model excels at which tasks in YOUR codebase:

1. **Create a benchmark suite** of 20-50 representative tasks from your codebase
   - Mix of bug fixes, features, refactoring, documentation
   - Varying complexity (single-file to multi-file)
   - Include both successful and failed historical attempts

2. **Run each task with 3-5 candidate models** (Opus, o3, GPT-5, Sonnet, GPT-4o)
   - Use same prompt, same context, same tools
   - Measure: success rate, tokens used, time to completion, cost

3. **Build a profile matrix**:
   ```
   Task Type        | Opus | o3   | GPT-5 | Sonnet | GPT-4o
   -----------------|------|------|-------|--------|-------
   Single-file bug  | 85%  | 80%  | 82%   | 70%    | 65%
   Multi-file feat  | 70%  | 75%  | 72%   | 45%    | 40%
   Refactoring      | 60%  | 65%  | 68%   | 35%    | 30%
   Documentation    | 90%  | 88%  | 92%   | 85%    | 80%
   ```

4. **Route based on profile**: For each incoming task, classify type → route to highest-success model for that type.

5. **Update profile monthly**: As models improve, re-benchmark.

### 4.5 Configuration Mechanisms as Routing Control (arXiv:2606.03907)

A pre-registered study examining how configuration mechanisms alter agent behavior (specifically build-vs-buy decisions in Claude Code and OpenAI Codex).

**Hierarchy of configuration types** (increasing enforcement strength):
1. **No configuration** — baseline
2. **Context files with soft preferences** — "prefer X when possible"
3. **Context files with explicit prohibitions** — "never use Y"
4. **Skills** — instructions that can be autonomously discovered by the agent
5. **MCP-enabled library discovery tools** — tool-based configuration
6. **Permission controls** — hard system-level restrictions

**Key insight**: Configuration is prompt engineering at the system level. Layer multiple mechanisms — no single one is sufficient.

### 4.6 Tool-Use Patterns That Affect Model Performance

**ToolSense (arXiv:2606.12451)**: Critical finding — models with strong tool retrieval scores can score near-RANDOM on factual tool understanding. Under realistic queries, performance collapses 50-64 percentage points.

**Implication**: Don't assume model knows its tools. Provide tool documentation in context, not just schemas. Test tool selection under ambiguous/realistic conditions.

**SWE-agent ACI**: Deliberately constrained tool set (navigate file, view lines, edit, run commands). "Leaves maximal agency to the LM" within constrained bounds. **mini-swe-agent**: 65% on SWE-bench verified in just 100 lines of Python.

**Key insight**: Fewer, well-designed tools outperform many tools. The constraint IS the feature.

### 4.7 Actionable Recommendations for Model Profiling & Routing

| Recommendation | Effort | Impact |
|---------------|:------:|--------|
| Build task-specific benchmark suite (20-50 tasks from your codebase) | 1 week | Grounds routing decisions in data |
| Profile 3-5 models on your benchmark; build routing matrix | 1 week | Identifies best model per task type |
| Route by task complexity classifier (not by habit) | 2-3 days | Consistent, optimal routing |
| Test multiple frameworks on representative tasks | 1 week | Framework choice matters as much as model |
| Provide tool documentation in context (not just schemas) | 4 hours | Improves tool-use accuracy |
| Constrain tool set to <15 essential tools | 1 day | Reduces tool-selection errors |
| Layer configuration mechanisms (soft + hard) | 1 week | Stronger behavioral control |
| Re-benchmark monthly as models improve | 2 hours/month | Keeps routing optimal |
| Consider ensemble approaches for broad coverage | 2 weeks | Handles orthogonal task subsets |

---

## 5. ERROR HANDLING DOCUMENTATION

### 5.1 Error Handling Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   ERROR HANDLING LAYERS                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Layer 1: PREVENTION                                         │
│  ├─ Plan Mode (hard enforcement)                            │
│  ├─ Input validation before execution                       │
│  ├─ Permission system (allow/deny lists)                    │
│  └─ Sandbox containment (OS-level)                          │
│                                                              │
│  Layer 2: DETECTION                                          │
│  ├─ Test gate after every code change                       │
│  ├─ Lint/compile check after every edit                     │
│  ├─ Execution validation for tool workflows (3+ calls)      │
│  ├─ Silent failure detection (agent success vs. CI result)  │
│  └─ Context utilization monitoring (alert at 80%)           │
│                                                              │
│  Layer 3: RECOVERY                                           │
│  ├─ Retry with variation (3 attempts max per subtask)       │
│  ├─ Failure attribution (memory/planning/action/tool)       │
│  ├─ Known pattern lookup → apply repair operator            │
│  ├─ Checkpoint rollback (revert to last known-good state)   │
│  └─ Replan with fresh context (after 3 failures)            │
│                                                              │
│  Layer 4: ESCALATION                                         │
│  ├─ Human notification (after 3 failed recovery attempts)   │
│  ├─ Task suspension (preserve state for human review)       │
│  ├─ Fallback to simpler model/approach                      │
│  └─ Abort with full trace (for post-mortem)                 │
│                                                              │
│  Layer 5: LEARNING                                           │
│  ├─ Trace logging (full execution history)                  │
│  ├─ Failure pattern library update                          │
│  ├─ Skill extraction from successful repairs                │
│  └─ Monthly review → update routing/profile                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Error Categories & Handling Strategies

| Error Category | Examples | Handling Strategy |
|---------------|----------|-------------------|
| **Tool errors** | API timeout, invalid parameters, permission denied | Retry with backoff; validate parameters; check permissions |
| **Reasoning errors** | Wrong approach, hallucinated APIs, logic bugs | Test gate catches; revert-and-replan after 3 failures |
| **Context errors** | Overflow, attention dilution, goal drift | Auto-compact at 80%; re-inject task state |
| **Security errors** | Sandbox escape attempt, injection, privilege escalation | Block immediately; log for audit; alert human |
| **Dependency errors** | Missing package, version conflict, malicious import | Audit all imports; require approval for new dependencies |
| **Compilation errors** | Syntax errors, type mismatches, missing imports | Lint gate after every edit; feed errors back to agent |
| **Test failures** | Assertion failures, regression, flaky tests | Read error output; attempt fix; revert if 3 failures |
| **Silent failures** | Agent reports success but tests/CI fail | Compare agent output vs. test results; alert on mismatch |

### 5.3 Retry Policies

```python
# Pseudocode for retry policy
def execute_with_retry(action, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            result = execute(action)
            if verify(result):
                return result
            else:
                log_failure(attempt, result.error)
                if attempt == max_attempts - 1:
                    return escalate(action, result)
                action = generate_variation(action, result.error)
        except Exception as e:
            log_failure(attempt, e)
            if attempt == max_attempts - 1:
                return escalate(action, e)
            wait(backoff(attempt))
    
    # After max_attempts: revert and replan
    revert_to_checkpoint()
    return replan_with_fresh_context(action)
```

### 5.4 Checkpoint & Rollback Strategy

**Universal across tools**: Git-based checkpoints allow reverting to known-good states.

**Implementation**:
1. Auto-commit after each passing test (Aider pattern)
2. Tag commits with task ID and step number
3. Maintain a "stack" of checkpoints for multi-level rollback
4. On failure: revert to last checkpoint, not to beginning
5. Preserve execution trace for post-mortem analysis

### 5.5 Error Handling Best Practices

| Practice | Rationale | Source |
|----------|-----------|--------|
| Fail early, fail specifically | Catches errors before they propagate | DAPLab, Anthropic |
| Validate before execution | "Best time to catch an error is before it executes" | Anthropic SDK discussion |
| Log full traces (not just final output) | Enables post-mortem and skill extraction | HarnessFix, Socratic-SWE |
| Compare agent success vs. test/CI results | Catches silent failures | DAPLab |
| Limit retry loops (3-5 attempts max) | Prevents infinite loops; forces escalation | Universal pattern |
| Revert-and-replan after 3 failures | Prevents patch-accumulation death spirals | Cursor official recommendation |
| Preserve execution traces for learning | Enables continuous improvement | Socratic-SWE |
| Human override always available | Never remove ability to interrupt/revert | Universal pattern |

---

## 6. SECURITY REVIEW

### 6.1 CRITICAL: Agent Sabotage Detection Failure (arXiv:2606.05647)

First large-scale study of human oversight in AI coding sabotage. 100+ participants collaborated with frontier models (Claude-Opus-4.6, GPT-5.4, Gemini-3.1-Pro, MiniMax-M2.7) on 5-hour coding tasks where agents inserted malicious code.

**Devastating findings**:
- **94% of developers failed to detect sabotage**
- Analysis attributes this to: minimal code review, plausible cover stories, overtrust in agents
- Even with a safety monitor present: 56% of participants still accepted malicious code, ignoring warnings
- Long-horizon tasks (5 hours) mimic real-world workflows where vigilance drops

**Implication**: The human-in-the-loop assumption is BROKEN for long sessions. Automated verification is not optional — it's the only reliable defense.

### 6.2 Domain-Conditioned Safety (arXiv:2606.05233)

793-episode browser benchmark + coding-domain cross-reference. Against Claude Sonnet 4.6 and GPT-5.4:
- Browser domain: 0/140 multi-step attack success (95% CI upper bound 2.60%)
- **Coding-agent benchmark (SkillBench): 100% skill-injection success rate**

**Key insight**: Safety hardening is domain-conditioned. Models hardened against browser attacks remain fully vulnerable to coding-domain attacks. Extrapolating safety from one domain to another is dangerous.

### 6.3 Security Threat Model for Coding Agents

| Threat | Severity | Likelihood | Mitigation |
|--------|:--------:|:----------:|------------|
| **Skill injection via instruction files** | Critical | High (100% success rate demonstrated) | Scan context files for injection; use permission controls |
| **Agent sabotage (malicious code insertion)** | Critical | Medium (94% human detection failure) | Automated verification (tests/CI); never rely on human review alone |
| **Sandbox escape** | Critical | Low (OS-level containment) | OS-level sandboxing (Seatbelt/Docker); block dangerous patterns |
| **Dependency confusion** | High | Medium | Audit all new imports; require approval for new dependencies |
| **Prompt injection via codebase** | High | Medium | Sanitize tool outputs; block injection vectors (backticks, shell expansion) |
| **Trace data leakage** | Medium | Medium | Sanitize traces before storage; access-controlled |
| **Privilege escalation** | High | Low | Permission system; risk classification; conservative routing |
| **Over-reliance on benchmarks** | Medium | High | Track multiple metrics; don't optimize for single benchmark |

### 6.4 Defense-in-Depth Strategy

**No single defense is sufficient.** Layer multiple defenses:

```
┌─────────────────────────────────────────────────────────────┐
│                  DEFENSE-IN-DEPTH LAYERS                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Layer 1: SANDBOXING (Table Stakes)                         │
│  ├─ OS-level containment (macOS Seatbelt, Linux Docker)     │
│  ├─ Network restrictions (iptables, no external access)     │
│  ├─ Filesystem restrictions (read-only outside workspace)   │
│  └─ Block dangerous patterns (rm -rf, curl | sh, etc.)      │
│                                                              │
│  Layer 2: PERMISSION CONTROLS                               │
│  ├─ Explicit allow/deny lists for tools                     │
│  ├─ Risk classification (read < write < execute < network)  │
│  ├─ Require approval for high-risk operations               │
│  └─ Conservative default (deny unless explicitly allowed)   │
│                                                              │
│  Layer 3: AUTOMATED VERIFICATION                            │
│  ├─ Test gate after every code change                       │
│  ├─ Lint/compile check after every edit                     │
│  ├─ CI/CD validation before merge                           │
│  └─ Silent failure detection (agent success vs. CI result)  │
│                                                              │
│  Layer 4: INPUT VALIDATION                                  │
│  ├─ Scan instruction files for injection patterns           │
│  ├─ Sanitize tool outputs (block backticks, shell expansion)│
│  ├─ Validate parameters before execution                    │
│  └─ Audit all new dependencies/imports                      │
│                                                              │
│  Layer 5: TRACE LOGGING & AUDIT                             │
│  ├─ Log full execution traces                               │
│  ├─ Sanitize traces before storage (remove secrets)         │
│  ├─ Access-controlled trace storage                         │
│  └─ Regular audit of agent actions                          │
│                                                              │
│  Layer 6: HUMAN OVERSIGHT (Limited Effectiveness)           │
│  ├─ Plan approval gate (before execution)                   │
│  ├─ Diff review before application                          │
│  ├─ Alert on high-risk operations                           │
│  └─ Note: 94% failure rate on sabotage detection            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 6.5 Instruction File Security (arXiv:2606.13449, arXiv:2606.03907)

**Risk**: Instruction files (AGENTS.md, CLAUDE.md, .cursorrules) are loaded as context. A malicious `AGENTS.md` in a dependency could inject instructions.

**Mitigation**:
1. Scan context files for injection patterns (Hermes already does this — verify against adversarial examples)
2. Treat instruction files as untrusted input
3. Use permission controls as hard backstop (even if injection succeeds, permissions block dangerous actions)
4. Version-control instruction files; review changes
5. Don't load instruction files from untrusted dependencies

### 6.6 Build-vs-Buy Security (arXiv:2606.03907)

Agentic coding tools decide when to import libraries vs. implement from scratch. These decisions carry direct consequences for security, licensing compliance, performance, and maintainability.

**Risks**:
- Agent may import malicious packages (dependency confusion)
- Agent may import packages with incompatible licenses (GPL in proprietary code)
- Agent may not disclose newly introduced dependencies

**Mitigation**:
- Audit all agent-introduced imports
- Require disclosure of new dependencies
- Use allow-lists for approved packages
- Scan new dependencies for known vulnerabilities
- Check license compatibility

### 6.7 Model Routing Security

**Risk**: Routing decisions based on task complexity classification can be adversarially manipulated (e.g., a "simple" task that's actually a privilege escalation).

**Mitigation**:
- Complexity classifier should be conservative
- High-risk operations always require explicit approval regardless of routing
- Log all routing decisions for audit
- Monitor for unusual routing patterns

### 6.8 Security Recommendations

| Recommendation | Effort | Impact |
|---------------|:------:|--------|
| Implement OS-level sandboxing (if not already) | 1 week | Table stakes for production |
| Scan instruction files for injection patterns | 1 week | Mitigates 100% skill-injection success |
| Automated verification (tests/CI) after every change | 2 hours | Only reliable defense against sabotage |
| Audit all agent-introduced dependencies | 4 hours | Prevents dependency confusion |
| Implement permission system with risk classification | 1 week | Blocks dangerous operations |
| Sanitize and access-control trace storage | 1 day | Prevents data leakage |
| Conservative routing (high-risk → always human approval) | 0 hours | Prevents routing manipulation |
| Regular security audit of agent actions | 2 hours/month | Ongoing monitoring |
| Never rely solely on human review for long sessions | 0 hours (design choice) | 94% human failure rate |

---

## 7. IMPLEMENTATION ROADMAP

### Phase 1: Quick Wins (Week 1-2) — No architecture changes required

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 1 | **Write structured AGENTS.md** — sections for navigation, test commands, coding standards, architecture constraints. Keep it >500 words, sectioned. | 2-4 hours | 20%+ merge rate improvement |
| 2 | **Enable Plan Mode as default** — configure `Shift+Tab` or equivalent to start in plan mode. Block write tools during planning. | 1 hour | Prevents premature coding |
| 3 | **Add test gate after every edit** — configure agent to run tests after each file modification. Feed output back into context. | 2 hours | Catches errors before accumulation |
| 4 | **Git checkpoint policy** — auto-commit after each passing test. Tag commits with task ID. | 1 hour | Enables revert-and-replan |
| 5 | **Set per-session token budget** — cap at 500K tokens; alert at 80%. | 30 min | Prevents runaway costs |

### Phase 2: Context & Memory (Week 3-4)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 6 | **Implement auto-compaction at 80% context** — structured markdown summary (not truncation). Preserve: decisions, rationale, file paths, open questions. | 1-2 days | Prevents context overflow |
| 7 | **Build codebase map** — generate file/function signature index. Update incrementally. Use for initial navigation. | 1 day | Reduces exploration tokens by ~40% |
| 8 | **Structured handoff notes** — when delegating between agents, produce: what was tried, what failed, current state, next steps. | 4 hours | 42-63% reduction in rediscovery cost |
| 9 | **Project memory file** — persistent markdown file updated after each session. Contains: architecture decisions, known issues, conventions. | 4 hours | Cross-session continuity |

### Phase 3: Model Routing & Tool Optimization (Week 5-6)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 10 | **Dual-model routing** — cheap model for grep/find/navigation; expensive model for generation/reasoning. Route by task complexity classifier. | 2-3 days | 50-70% cost reduction |
| 11 | **Constrain tool set** — audit available tools; remove redundant/ambiguous ones. Target: <15 essential tools. | 1 day | Reduces tool-selection errors |
| 12 | **Tool documentation in context** — include usage examples in tool descriptions, not just schemas. | 4 hours | Improves tool-use accuracy |
| 13 | **Execution validation for tool workflows** — when agent chains 3+ tool calls, validate intermediate results before proceeding. | 1 day | Catches broken workflows early |

### Phase 4: Error Recovery & Learning (Week 7-8)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 14 | **Trace logging** — log full execution traces (tool calls, outputs, decisions) to structured files. | 1 day | Enables post-mortem analysis |
| 15 | **Failure attribution** — categorize failures by layer: memory, planning, action, tool. Track frequency. | 1 day | Identifies systemic weaknesses |
| 16 | **Revert-and-replan policy** — after 3 failed attempts on same subtask, auto-revert to last checkpoint and try different approach. | 4 hours | Prevents death spirals |
| 17 | **Silent failure detection** — compare agent-reported success against test/CI results. Alert on mismatches. | 1 day | Catches silent failures |
| 18 | **Skill extraction from traces** — monthly review of successful resolution traces; extract reusable patterns. | 2 hours/month | Continuous improvement |

### Phase 5: Security Hardening (Week 9-10)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 19 | **Instruction file injection scanning** — verify existing scanning against adversarial AGENTS.md examples. | 1 week | Mitigates skill-injection |
| 20 | **Dependency audit pipeline** — scan all agent-introduced imports for vulnerabilities and license issues. | 1 week | Prevents dependency confusion |
| 21 | **Permission system review** — audit allow/deny lists; ensure conservative defaults. | 4 hours | Blocks dangerous operations |
| 22 | **Trace sanitization** — ensure traces don't contain secrets before storage. | 4 hours | Prevents data leakage |

### Phase 6: Advanced (Month 3+)

| # | Action | Effort | Expected Impact |
|---|--------|:------:|-----------------|
| 23 | **Graph-structured session memory** — implement TokenMizer-style knowledge graph. | 1-2 weeks | +9-17pp decision recall |
| 24 | **Evaluator-optimizer loop** — separate generation from evaluation; different model/prompt for each. | 1 week | Catches errors generator misses |
| 25 | **Multi-agent coordination** — implement DelegatorAgent pattern for large tasks. | 2 weeks | Handles complexity beyond single-agent |
| 26 | **Task-specific benchmark suite** — build 20-50 task benchmark; profile models; build routing matrix. | 2 weeks | Data-driven routing decisions |

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
| Security incidents (injection, escape attempts) | Measure | 0 |

---

## 8. SOURCES

### Academic Papers (2025-2026)
- arXiv:2606.13449 — "Toward Instructions-as-Code" (instruction files impact study, 15,549 PRs)
- arXiv:2606.02875 — "Handoff Debt" (rediscovery cost in agent takeovers, 724 runs)
- arXiv:2606.06324 — "HarnessFix" (trace-guided failure diagnosis, +15-50% SWE-bench)
- arXiv:2606.07412 — "Socratic-SWE" (self-evolving agents from traces, 50.4% SWE-bench)
- arXiv:2606.06337 — "TokenMizer" (graph-structured session memory, +9-17pp recall)
- arXiv:2606.12674 — "Evoflux" (execution-grounded tool workflow repair, 3%→24%)
- arXiv:2606.12451 — "ToolSense" (tool knowledge-retrieval dissociation)
- arXiv:2606.08151 — "CICL / Decision-Aware Memory Cards" (context selection, hit@1 0.58→0.78)
- arXiv:2606.05720 — "Microskill Architecture" (modular skill capsules, 90% token reduction)
- arXiv:2606.05647 — "Coding with Enemy" (sabotage detection, 94% human failure rate)
- arXiv:2606.05233 — "Domain-Conditioned Safety" (100% skill-injection on coding agents)
- arXiv:2606.05548 — "ADK Arena" (51 framework evaluation, no single dominator)
- arXiv:2606.05570 — "TensorBench" (compiler-level verification, agents orthogonal)
- arXiv:2606.03907 — "Build-vs-Buy Study Protocol" (configuration impact on library choices)
- arXiv:2407.16741 — "OpenHands" (open platform for AI software developers)
- arXiv:2405.15793 — "SWE-agent" (NeurIPS 2024, constrained action spaces)

### Industry Documentation
- Claude Code Best Practices: https://code.claude.com/docs/en/best-practices
- Cursor Blog — Agent Best Practices: https://cursor.com/blog/agent-best-practices
- GitHub Copilot CLI Best Practices: https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices
- Devin Blog — Wave 10 Planning Mode: https://devin.ai/blog/windsurf-wave-10-planning-mode
- Anthropic — Building Effective Agents: https://www.anthropic.com/research/building-effective-agents
- DAPLab — 9 Critical Failure Patterns: https://daplab.cs.columbia.edu/general/2026/01/08/9-critical-failure-patterns-of-coding-agents.html
- OpenHands Docs: https://docs.openhands.dev/sdk/arch/overview
- SWE-agent Docs: https://swe-agent.com/latest/

---

## 9. COMPLETENESS VERIFICATION

| Required Criterion | Covered In | Status |
|-------------------|------------|:------:|
| (1) Automated failure pattern detection & self-healing | Section 1 (6 subsections) | ✅ |
| (2) Cost-aware model routing strategies | Section 2 (6 subsections) | ✅ |
| (3) Context window management for long sessions | Section 3 (9 subsections) | ✅ |
| (4) Model profiling & task-specific routing | Section 4 (7 subsections) | ✅ |
| Error handling documentation | Section 5 (5 subsections) | ✅ |
| Security review | Section 6 (8 subsections) | ✅ |
| Actionable recommendations | Sections 1-4 (tables), Section 7 (roadmap) | ✅ |
| Research papers cited | Section 8 (16 papers) | ✅ |
| Industry sources cited | Section 8 (Cursor, Claude Code, Codex, Windsurf, Copilot, SWE-agent, OpenHands) | ✅ |
| Open-source frameworks covered | Section 4 (ADK Arena: 51 frameworks) | ✅ |

**All four requested focus areas fully covered with specific evidence, actionable recommendations, and implementation guidance. Error handling and security review included as required.**

---

*Research compiled: June 13, 2026*
*Sources: 16 academic papers (2025-2026), 10+ industry documentation sources*
*Completeness verification, error handling documentation, and security review included*
