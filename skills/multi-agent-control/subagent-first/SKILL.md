---
name: subagent-first
description: "Default to subagents for all non-trivial work. Use this skill to decide when to delegate, how to partition work for parallel execution, and how to package bulletproof context to prevent subagent drift."
version: 2.3.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [subagents, delegation, parallelism, workflow, context-packaging, wisdom-accumulation]
    related_skills: [subagent-driven-development, subagent-collaboration-workflow, dispatching-parallel-agents]
    changelog:
      - "v2.2: Intent Gate now auto-injected via SOUL.md; skill focuses on execution AFTER intent classification. Removed redundant decision framework (now in SOUL.md). Added cross-reference to SOUL.md Intent Gate."
      - "v2.1: Added Wisdom extraction standard format template, extraction checklist, when NOT to extract rules, and query matching rules"
      - "v2.0: Added 6-Section Delegation Prompt (from OMO research), Wisdom Accumulation, Wave parallel with dependency scheduling"
---

# Subagent-First Workflow

## Intent Gate: Already Running

**Intent Gate is now auto-injected via SOUL.md (slot #1 in system prompt).**

You do NOT need to re-run intent classification here — SOUL.md already enforced:
- Step 0: Verbalize Intent
- Step 1: Classify Request Type
- Step 1.5: Turn-Local Intent Reset
- Step 2: Check for Ambiguity
- Step 2.5: Context-Completion Gate
- Step 3: Validate Before Acting (Delegation Check)

**This skill applies AFTER Intent Gate decides: DELEGATE.**

When Intent Gate's Step 3 returns "delegate", use this skill's execution protocols.

---

## Spend Sanity Check Before Dispatch

Even when SOUL.md has already decided a task is non-trivial enough to delegate, do one more short check before spawning children:
- What concrete value does this create for the core customer?
- What is the lightest viable dispatch shape?
- Is a heavier wave plan buying real marginal value, or just process?
- Would the user actually miss any of these steps if they disappeared?

If the answers are weak, reframe or shrink the dispatch instead of sending more children.

## Core Principle

**Default to subagents. Only execute directly when the cost of delegation exceeds the benefit.**

The Intent Gate Delegation Check already made the decision. Now execute it properly.

## Quick Reference: When Direct Execution is Acceptable

Intent Gate already filtered these. Direct execution is acceptable ONLY when Intent Gate classified as:
- **Trivial**: 1-2 tool calls, zero branching, predictable output
- **Explicit**: Specific file/line, clear command, single action

All other classifications → use subagent (per Intent Gate Step 3).

## When Intent Gate Says DELEGATE (Execution Protocols)

Intent Gate's Step 3 (Delegation Check) returns DELEGATE for:
- Exploratory tasks
- Open-ended tasks
- Multi-file changes
- Research/Synthesis
- Investigation/Diagnosis
- Parallelizable work
- Unknown scope tasks

When you receive DELEGATE decision from Intent Gate, follow the phases below.

---

## Dispatch Disclosure (User-Facing, Concise)

For coding tasks delegated to subagents, tell the user **before dispatch** in 1-3 short bullets:
- **Backend**: e.g. `OpenCode ACP (opencode acp, non-pure mode)`
- **Agent choice**: e.g. `Sisyphus - Ultraworker` for general coding, `Hephaestus - Deep Agent` for deeper implementation
- **Dispatch shape**: e.g. `single implementer`, `Wave 1 parallel investigation x2`, `controller verifies after child completes`

Default disclosure pattern:

```text
Subagent plan:
- Backend: OpenCode ACP (opencode acp, non-pure mode)
- Agent: Sisyphus - Ultraworker
- Dispatch: 1 coding subagent + controller verification
```

If using more than one child, disclose wave shape briefly:

```text
Subagent plan:
- Backend: OpenCode ACP (opencode acp, non-pure OMO)
- Agents: Wave 1 Sisyphus x2, Wave 2 Hephaestus x1
- Dispatch: parallel investigation first, then single implementation, then controller verification
```

Do this concisely; do NOT dump the full 6-section prompt to the user unless asked.


---

## Phase 0: Wisdom Retrieval

**Before partitioning tasks, query prior learnings.**

```
1. Identify task type: {domain}-{action-type}
   Examples: auth-test-fixing, api-refactoring, db-debugging

2. Query hindsight_recall:
   prior_wisdom = hindsight_recall(query="{task_type}")

3. If wisdom exists → inject into Phase 2 CONTEXT section
   If no wisdom → proceed without prior context
```

---

## Phase 1: Task Partitioning & Wave Planning

**Map dependencies and plan wave dispatch.**

### Step 1.1: Decompose Task

```
Can this task be decomposed into independent subtasks?
├── YES → What are the dependencies between subtasks?
│         ├── No dependencies → Wave 1 (parallel)
│         ├── Some dependencies → Wave 1 + Wave 2 pattern
│         └── Heavy dependencies → Sequential execution
│
└── NO → Single subagent task, skip wave planning
```

### Step 1.2: Dependency Analysis

| Dependency Type | Action |
|-----------------|--------|
| Sequential data flow (output → input) | Sequential |
| Shared file edits (same file) | Sequential OR explicit file boundaries |
| Decision dependency (approach determines next) | Sequential |
| Validation dependency (must verify before next) | Sequential |
| Independent scope (different dirs) | Parallel Wave 1 |
| Read-only + read-only (no writes) | Parallel Wave 1 |

### Step 1.3: Wave Plan Output

```
Wave Plan:
├── Wave 1: [Task A, Task B] (parallel, max 3)
├── Wave 2: [Task C] (depends on Wave 1)
├── Wave 3: [Task D] (depends on Wave 2)
│
└── Total waves: N
└── Estimated iterations per subagent: 15-50
```

### Step 1.4: User Confirmation Checkpoint ⚠️

**Before dispatching 3+ waves or 5+ subagents, MUST confirm with user:**

```
Wave Plan Summary:
- Wave 1: 3 subagents (auth, api, db investigation)
- Wave 2: 1 subagent (integration design)
- Wave 3: 1 subagent (implementation)
- Total: 5 subagents, ~150 iterations

Proceed with dispatch? [YES/NO]
```

**If user says NO → Adjust plan, reduce scope, or cancel.**

This checkpoint prevents:
- Token cost explosion from runaway parallel dispatch
- User surprise from unexpected agent activity
- Premature execution before plan validation

---

## Phase 2: Subagent Dispatch

**Construct 6-Section context and dispatch.**

### Step 2.1: Build 6-Section Context

Use the template for each subagent:

```python
context = """
TASK:
[One clear sentence]

OUTCOME:
- [Deliverable 1]
- [Deliverable 2]
- [Verification criteria]

TOOLS:
- [Toolset]: [specific instructions]

MUST:
- [Required action]
- [Required verification]

MUST NOT:
- [Prohibition 1] (catch AI slop)
- [Prohibition 2] (prevent scope creep)

CONTEXT:
[Prior wisdom from Phase 0]
[Project conventions]
[Related files/code snippets]
"""
```

### Step 2.2: Dispatch Waves

```python
# Wave 1
wave1_results = delegate_task(
    tasks=[
        {"goal": "...", "context": "...", "toolsets": [...], "max_iterations": 30},
        {"goal": "...", "context": "...", "toolsets": [...], "max_iterations": 30},
    ]
)

# Wave 2 (if exists)
wave2_results = delegate_task(
    tasks=[
        {"goal": "...", "context": f"...{wave1_results[0]['summary']}...", ...},
    ]
)
```

---

## Phase 3: Verification

**Controller checks subagent output, never trust blindly.**

### Step 3.1: Output Validation Checklist

```
□ Does summary match OUTCOME criteria?
□ Were MUST requirements fulfilled?
□ Were MUST NOT prohibitions respected?
□ If tests specified → Did tests pass?
□ If files specified → Check actual changes with read_file/diff
□ Any unexpected changes? → Investigate before accepting
```

### Step 3.2: Failure Handling

```
If verification fails:
├── Minor issue → Fix in controller (patch/terminal)
├── Major issue → Re-dispatch with corrected context
├── Subagent ran off → Add MUST NOT constraints, retry
│
└── DO NOT accept subagent summary without checking
```

---

## Phase 4: Wisdom Capture

**Extract learnings from successful completion.**

### Step 4.1: Wisdom Extraction Checklist

Run after EVERY successful subagent completion:

```
□ Pattern discovered? → Extract to Pattern field
□ Gotcha identified? → Extract to Gotcha field
□ Convention learned? → Extract to Convention field
□ Tool combo worked? → Extract to Tool Combo field
□ Failure overcome? → Extract to Failure Recovery field
□ Key insight? → Extract to Key Insight field

□ Task failed? → DO NOT extract (only from successes)
□ Trivial task? → DO NOT extract (no learning value)
```

### Step 4.2: Store Wisdom

```python
hindsight_retain(
    content="[WISDOM ENTRY]\nTask Type: {type}\nPattern: {...}\n...",
    context="{task_type}"
)
```

### Step 4.3: Completion Notification ⚠️

**After wisdom capture, notify user of completion:**

```
Task Completed:
- Subagent: {role}
- Outcome: {summary of deliverables}
- Verification: {passed checks}
- Wisdom: {key insight captured (if applicable)}

Result: {SUCCESS/PARTIAL/FAILED}
```

**If PARTIAL or FAILED → Offer next steps instead of marking done.**

This checkpoint prevents:
- User not knowing task status
- Premature closure without explicit confirmation
- Lost context for follow-up actions

---

## 6-Section Delegation Prompt (From OMO Research)

**Every subagent context MUST follow this structure.** This is the single most important factor in preventing subagent drift.

### The 6 Sections

```
TASK:
[One-sentence task description]

OUTCOME:
[What success looks like - specific deliverables]

TOOLS:
[Available toolsets and any tool-specific instructions]

MUST:
[Explicit requirements - things that MUST be done]

MUST NOT:
[Explicit prohibitions - things that MUST NOT be done]

CONTEXT:
[Background information, prior findings, project conventions]
```

### Why This Structure Works

1. **TASK** - Clear, singular focus prevents scope creep
2. **OUTCOME** - Defines completion criteria upfront
3. **TOOLS** - Prevents tool hallucination and wrong toolset selection
4. **MUST** - Forces positive constraints that can't be ignored
5. **MUST NOT** - Explicit prohibitions catch AI slop patterns (from OMO's "Anti-AI-Slop" design)
6. **CONTEXT** - Rich background without drowning in noise

### Example: Good vs Bad

**BAD - Vague context causes drift:**
```python
delegate_task(
    goal="Fix the auth tests",
    context="Tests are failing, figure it out"
)
# Result: Subagent explores entire codebase, changes unrelated files, breaks other tests
```

**GOOD - 6-Section keeps subagent on track:**
```python
delegate_task(
    goal="Fix failing auth tests",
    context="""
TASK:
Make test_login_failure in tests/auth/test_login.py pass.

OUTCOME:
- Test passes: pytest tests/auth/test_login.py::test_login_failure succeeds
- Report: exact fix made with line numbers
- No other tests broken

TOOLS:
- terminal (pytest, git)
- file (read, patch)

MUST:
- Fix the password comparison logic in src/auth/login.py
- Run pytest after changes to verify
- Report exact changes made

MUST NOT:
- Change test assertions
- Add new dependencies
- Modify any files outside src/auth/login.py
- Skip running tests before reporting done

CONTEXT:
- test_login_failure fails with AssertionError: "Invalid credentials" expected but got "Login successful"
- Password is hashed with bcrypt, comparison should use checkpw()
- Project uses pytest, run: pytest tests/auth/test_login.py -v
- Related file: src/auth/login.py line 47-52
""",
    toolsets=["terminal", "file"],
    max_iterations=25
)
```

### MUST NOT Anti-Patterns (From OMO)

Common AI slop patterns to explicitly prohibit:

- "Do NOT add unnecessary logging/print statements"
- "Do NOT add comments explaining obvious code"
- "Do NOT refactor unrelated code while fixing the issue"
- "Do NOT add TODOs or placeholders"
- "Do NOT create new abstractions unless explicitly requested"
- "Do NOT change variable names for 'clarity'"
- "Do NOT add defensive null checks that weren't requested"

---

## Wisdom Format Reference

**Standard format for hindsight_retain (details in Phase 4):**

```python
hindsight_retain(
    content="[WISDOM ENTRY]\nTask Type: {domain}-{action}\nPattern: {...}\nGotcha: {...}\nConvention: {...}\nTool Combo: {...}\nFailure Recovery: {...}\nKey Insight: {...}",
    context="{task_type}"
)
```

**Query matching:** Use task type as keyword (e.g., `hindsight_recall(query="auth-test-fixing")`).

---

## Wave Dispatch Reference

**Wave dispatch pattern (details in Phase 1-2):**

```
Wave 1: [Task A, Task B, Task C] → parallel, max 3 concurrent
Wave 2: [Task D] → depends on Wave 1 results
Wave 3: [Task E] → depends on Wave 2 results
```

**Dependency types requiring sequential execution:**
- Same file edits
- Output → input data flow
- Decision/validation dependency

**Max concurrent limit:** Hermes config default = 3.

---

## Partitioning for Parallel Execution

### Decision Logic

```
Can tasks run independently?
├── YES → Can they touch the same files?
│   ├── NO → Dispatch in parallel (Wave 1)
│   └── YES → Can edits be cleanly separated?
│       ├── YES → Parallel with explicit file boundaries in MUST NOT
│       └── NO → Sequential execution
└── NO → Sequential execution required
```

### Good Parallel Partitions

- Multiple independent investigations (different subsystems)
- Separate test files with isolated failures
- Read-only research tasks on different topics
- Independent implementation tasks with non-overlapping files

### Bad Parallel Partitions

- Multiple implementers editing the same file
- Tasks where one's output is another's input
- Investigations that might discover shared root causes
- Any task pair where you can't predict the interaction

---

## Complete Context Packaging Template

**Use this template for every delegate_task call:**

```python
delegate_task(
    goal="[One-sentence task from TASK section]",
    
    context="""
TASK:
[One clear sentence describing what to accomplish]

OUTCOME:
- [Specific deliverable 1]
- [Specific deliverable 2]
- [Verification criteria]

TOOLS:
- [Toolset 1]: [any specific instructions]
- [Toolset 2]: [any specific instructions]

MUST:
- [Required action 1]
- [Required action 2]
- [Required verification step]

MUST NOT:
- [Prohibition 1 - catch AI slop]
- [Prohibition 2 - prevent scope creep]
- [Prohibition 3 - maintain invariants]

CONTEXT:
[Prior findings from controller]
[Project conventions]
[Related files/code snippets]
[Prior wisdom from hindsight_recall if applicable]
""",
    
    toolsets=["terminal", "file"],
    max_iterations=30  # Adjust based on complexity
)
```

---

## Anti-Patterns

### Anti-Pattern 1: Missing MUST NOT

```python
# BAD - No prohibitions, subagent adds "helpful" extras
delegate_task(
    goal="Fix login bug",
    context="TASK: Fix the login validation bug."
)
# Result: Subagent fixes bug AND refactors code AND adds logging AND breaks tests
```

```python
# GOOD - Explicit MUST NOT catches AI slop
delegate_task(
    goal="Fix login bug",
    context="""
TASK: Fix password validation in src/auth/login.py.

MUST NOT:
- Add logging statements
- Refactor surrounding code
- Change function signatures
- Modify tests
"""
)
```

### Anti-Pattern 2: Parallel Editors

```python
# BAD - Two implementers editing the same file
delegate_task(tasks=[
    {"goal": "Add login to app.py", ...},
    {"goal": "Add logout to app.py", ...}  # Race condition!
])
```

```python
# GOOD - Sequential or parallel with file boundaries
# Option 1: Sequential (use Wave pattern)
delegate_task(goal="Add login to app.py", ...)
# Wait, then:
delegate_task(goal="Add logout to app.py", ...)

# Option 2: Parallel with explicit file separation in MUST NOT
delegate_task(tasks=[
    {
        "goal": "Add login to auth/login.py",
        "context": "... MUST NOT: Edit any file outside auth/login.py"
    },
    {
        "goal": "Add logout to auth/logout.py",
        "context": "... MUST NOT: Edit any file outside auth/logout.py"
    }
])
```

### Anti-Pattern 3: No Wisdom Capture

```python
# BAD - Learnings lost after subagent completes
result = delegate_task(...)
# Move on without capturing what worked

# Next similar task → same mistakes, same rediscovery
```

```python
# GOOD - Capture wisdom for reuse
result = delegate_task(...)

# Extract and store
hindsight_retain(
    content=f"Pattern that worked: {result['key_insight']}",
    context="task-category"
)

# Future task benefits from prior learning
```

### Anti-Pattern 4: Skipping Verification

```python
# BAD - Trust subagent summary without checking
result = delegate_task(...)
user.tell("Done!")  # No verification
```

```python
# GOOD - Controller verifies in MUST section
delegate_task(
    context="""
MUST:
- Run pytest tests/auth/ after changes
- Include test output in summary
"""
)
result = delegate_task(...)
# Check summary includes test results, not just "I fixed it"
```

---

## Role Selection Guide

| Task Type | Recommended Toolsets | Typical Iterations |
|-----------|---------------------|-------------------|
| Investigation/Diagnosis | terminal, file | 15-25 |
| Implementation | terminal, file | 30-50 |
| Code Review | file | 15-25 |
| Research | web, search | 20-35 |
| Planning | file, web | 25-40 |
| Parallel Investigation | terminal, file | 15-25 each |
| Deep Refactoring | terminal, file | 50-70 |

---

## Backend Choice

The workflow discipline stays the same regardless of backend:

**Hermes native children** (default):
```python
delegate_task(goal="...", context="...", toolsets=["terminal", "file"])
```

**OpenCode with OMO** (preferred for code-heavy work):
```python
delegate_task(
    goal="...",
    context="...",
    acp_command="opencode",
    acp_args=["acp"],
    toolsets=["terminal", "file"]
)
```

Use the ACP entrypoint that is valid in your own environment. A local wrapper is fine, but keep it outside the reusable skill unless it is part of your public setup instructions.
```

**Model override for specialized tasks**:
```python
delegate_task(
    goal="...",
    context="...",
    model={"model": "anthropic/claude-opus-4"}  # Heavy reasoning
)
```

---

## Integration with Other Skills

- **subagent-driven-development**: Use for executing pre-written implementation plans task-by-task
- **subagent-collaboration-workflow**: Use for complex multi-role workflows with planner/investigator/implementer/reviewer separation
- **verification-before-completion**: Always use before claiming work is done

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│               INTENT GATE → SUBAGENT EXECUTION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SOUL.md INTENT GATE (auto-injected, every message):           │
│  ├── Step 0: Verbalize Intent                                   │
│  ├── Step 1: Classify (Trivial/Explicit/Exploratory/etc.)       │
│  ├── Step 1.5: Turn-Local Reset                                 │
│  ├── Step 2: Ambiguity Check                                    │
│  ├── Step 2.5: Context-Completion Gate                          │
│  └── Step 3: Delegation Check → DELEGATE or DIRECT              │
│                                                                 │
│  IF DELEGATE (this skill applies):                              │
│  ├── 6-Section Prompt: TASK/OUTCOME/TOOLS/MUST/MUST NOT/CONTEXT │
│  ├── Wave Parallel: Map deps → Wave 1 → Wave 2 → ...            │
│  ├── Wisdom: Extract → hindsight_retain                         │
│  └── Verify: Controller checks subagent output                  │
│                                                                 │
│  IF DIRECT (Intent Gate decided trivial/explicit):              │
│  └── Execute in controller session                              │
│                                                                 │
│  CONTEXT: Always use 6-Section structure                        │
│  MUST NOT: Catch AI slop (no extra logging, no refactors, etc.) │
│  WISDOM: hindsight_recall before, hindsight_retain after        │
│  VERIFY: Never trust subagent summaries blindly                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Remember

1. **Intent Gate runs first** - SOUL.md auto-injects, you inherit its decision
2. **DELEGATE → use this skill** - Apply 6-Section, Wave Parallel, Wisdom protocols
3. **DIRECT → skip this skill** - Intent Gate already decided trivial/explicit
4. **Always use 6-Section** - TASK/OUTCOME/TOOLS/MUST/MUST NOT/CONTEXT
5. **MUST NOT catches AI slop** - Explicit prohibitions prevent scope creep
6. **Capture wisdom** - hindsight_retain after success, hindsight_recall before new tasks
7. **Wave parallel** - Map dependencies, dispatch in waves, respect config limits
8. **Verify in controller** - Never trust subagent summaries blindly