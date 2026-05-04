---
name: subagent-collaboration-workflow
description: "Use when Hermes should run a complete multi-role subagent workflow: decompose work, assign isolated planner/investigator/implementer/reviewer tasks, integrate results, and verify before claiming success."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [subagents, delegation, workflow, review, verification, parallel]
    related_skills: [subagent-first, subagent-driven-development, dispatching-parallel-agents, verification-before-completion, writing-plans]
---
# Subagent Collaboration Workflow

## Overview

**IMPORTANT:** Use `subagent-first` skill first to determine delegation strategy. This skill provides the full multi-role workflow once you've decided subagents are appropriate.

This skill defines the full controller-side workflow for subagent collaboration.
---

# Subagent Collaboration Workflow

## Overview

This skill defines the full controller-side workflow for subagent collaboration.

Core principle:
- Hermes main session is the controller
- child agents are specialists with narrow scopes
- role separation is intentional
- results are integrated centrally
- completion is claimed only after controller-side verification

Architecture layers:
- Controller/judgment layer: understand the objective, gather context, partition work, resolve conflicts, and decide when the task is actually done.
- Execution agent layer: bounded work is executed either directly by the main session for small obvious tasks, or by isolated subagents when separation or parallelism adds value.
- Verification layer: review and proof are independent from implementation; passing work through a separate verifier role is part of the workflow, not an optional flourish.
- Shared tool layer: Hermes tools are the common atomic substrate used by all upper layers. They are not a separate "executor role"; controller, implementers, and verifiers all call the same tool primitives as needed.
- Asset layer: successful workflows should be stabilized into skills, templates, scripts, or compact memory notes when they will save future effort.

This is the workflow skill.
Backend choice is secondary.
You can run the same workflow with native Hermes children or with a specific ACP backend such as OpenCode, Codex, or Claude Code.
A linked reference file `references/role-prompts.md` contains reusable prompt templates for planner, investigator, implementer, spec reviewer, quality reviewer, and fix-up roles.

## When to Use

Use this skill when:
- the task is complex enough to benefit from role separation
- multiple subtasks or investigations need isolated context
- you want planner -> implementer -> reviewer style execution
- there may be parallel read-only investigation before edits
- you need tighter quality control than a single agent pass

Do not use this skill when:
- the task is trivial and faster to do directly
- subtasks are so coupled that isolation is fake
- there is not enough context yet to partition the work safely
- the task requires ongoing user interaction inside child tasks

## Controller Responsibilities

The controller must always own:
- objective definition
- context gathering
- task partitioning
- deciding sequential vs parallel execution
- conflict resolution across child outputs
- final verification
- user communication

Never delegate all judgment away.

## Standard Roles

### 1. Planner

Use when you need:
- task decomposition
- file or subsystem mapping
- risk identification
- suggested verification commands

Planner output should be structured as:
1. task breakdown
2. likely files or systems touched
3. risks and dependencies
4. recommended verification
5. whether tasks are parallel-safe

### 2. Investigator

Use for read-only diagnosis, audits, or codebase reconnaissance.
Good for:
- tracing logic paths
- finding root causes
- comparing implementations across files
- surfacing hidden dependencies

Investigator should not modify files unless explicitly allowed.

### 3. Implementer

Use for one bounded change at a time.
Give it:
- exact task text
- scope boundaries
- relevant paths
- required tests/checks
- explicit no-scope-creep instruction

### 4. Spec Reviewer

Use after implementation to check:
- requested scope fully covered
- no missing acceptance criteria
- file/function/behavior matches the task
- no extra unrelated work added

### 5. Quality Reviewer

Use after spec review passes to check:
- maintainability
- edge cases
- test sufficiency
- conventions and style
- bug risk and security risk

### 6. Verifier

The verifier is usually the controller session.
Run real checks here:
- tests
- lint
- targeted commands
- diffs
- manual file inspection when needed

Do not rely on a child agent's self-report as the only verification.

## Phase-by-Phase Workflow

### Phase 1: Gather Context First

Before spawning children:
- read the relevant files
- inspect repository structure if needed
- identify constraints from the user
- decide whether a written plan is needed

If the task is underspecified, gather more context before delegation.

### Phase 2: Partition the Work

Split work by independent responsibility, not by arbitrary chunk size.

Good partitions:
- planner for decomposition
- two read-only investigators on separate subsystems
- one implementer for one bounded code change
- one independent reviewer after implementation

Bad partitions:
- two implementers editing the same hot file concurrently
- one child told to both build and approve the same work
- parallel tasks whose outputs depend on unknown shared state

### Phase 3: Create a Todo Backbone

For multi-step work, create a todo list in the controller session.
Example shape:

```python
todo([
  {"id": "gather", "content": "Gather context and determine task split", "status": "in_progress"},
  {"id": "plan", "content": "Run planner subagent if needed", "status": "pending"},
  {"id": "implement", "content": "Run implementer task(s)", "status": "pending"},
  {"id": "review", "content": "Run independent review", "status": "pending"},
  {"id": "verify", "content": "Run controller-side verification", "status": "pending"}
])
```

Use todo state to prevent losing the collaboration thread.

### Phase 4: Choose Execution Mode

#### Mode A: Sequential collaboration

Use when edits depend on earlier results.
Typical flow:
1. planner
2. implementer
3. spec reviewer
4. quality reviewer
5. controller verification

#### Mode B: Parallel investigation

Use when tasks are truly independent and mostly diagnostic.
Typical flow:
1. controller defines independent read-only questions
2. `delegate_task(tasks=[...])` runs them concurrently
3. controller integrates findings
4. controller decides next edit path

#### Mode C: Repair loop

Use when review finds problems.
Flow:
1. reviewer reports concrete gaps
2. controller validates the criticism
3. fresh implementer or fix-up child addresses only those gaps
4. reviewer re-checks
5. controller verifies again

### Phase 5: Integrate Results Centrally

After child tasks finish, the controller must:
- compare outputs for contradiction or overlap
- inspect changed files or diffs when edits happened
- decide whether more work is needed
- never treat child summaries as final truth

### Phase 6: Verify Before Claiming Success

Controller verification should include the smallest sufficient real checks, such as:
- targeted tests
- full test suite when risk justifies it
- lint/typecheck/build
- diff inspection
- runtime smoke test

Only after verification should the user be told the work is complete.

## Prompt Construction Rules

Every child prompt should contain:
- the exact objective
- repository or working path if relevant
- whether edits are allowed
- specific files/subsystems involved
- explicit constraints and non-goals
- expected output format
- verification expectations
- enough prior findings and local context so the child does not have to rediscover the problem from scratch
- a clear statement of what success looks like and what would count as going out of scope

## Delegation Alignment Contract

Before spawning a child, the controller should package a compact but sufficient handoff that includes:
- objective: what exact result is wanted now
- current state: what is already known, already tried, and already fixed
- boundaries: what must not be touched, expanded, or re-litigated
- acceptance target: what specific change or proof is required for this run
- output contract: what the child must report back (for example changed edges, changed files, reasons, verification)

If a child could plausibly solve the wrong problem, the handoff is still under-specified.
Do not delegate broad exploratory work when the controller can first narrow the search space.
Do not make children re-read large areas of context that the controller can summarize into a tighter task package.

## Efficiency Rules For Delegation

To improve speed without sacrificing alignment:
- pre-filter likely targets in the controller session before delegating, so children start from candidate objects instead of open-ended exploration
- carry forward confirmed facts, existing edges, prior failures, and forbidden actions into the next child task instead of forcing re-discovery
- prefer one clearly scoped batch with an explicit acceptance target over a vague multi-goal mission
- when a prior child establishes that a concept pair is already correctly normalized, record that in the next handoff as settled and avoid re-checking it unless new evidence appears
- if a child run is interrupted or rate-limited, restart with a narrower, continuation-style brief rather than the full original exploration packet

Good prompt:
- "Inspect `run_agent.py` retry handling around the non-streaming loop, identify where retries are decided, do not edit files, and summarize exact function names plus risk points."

Bad prompt:
- "Look into retries."

## Backend-Agnostic Delegation Pattern

Default Hermes-native child:

```python
delegate_task(
  goal="...",
  context="...",
  toolsets=["terminal", "file"]
)
```

Optional ACP backend specialization:

```python
delegate_task(
  goal="...",
  context="...",
  acp_command="opencode",
  acp_args=["acp"],
  toolsets=["terminal", "file"]
)
```

Important:
- if your environment uses a local wrapper for ACP launches, document that wrapper separately and keep this reusable workflow backend-agnostic
- backend choice does not change the workflow discipline
- keep the collaboration pattern stable even if the child engine changes
- choose backend only after deciding the role and scope

## Default Controller Routing Heuristic

Use this quick routing order before acting:
1. Clarify only if missing information materially changes the tool or delegation path.
2. If the task is small, obvious, and the proof path is short, execute directly in the controller session with shared tools.
3. If uncertainty is high but the work is still read-only, run planner and/or investigator roles first.
4. If the task splits into truly independent domains, dispatch parallel investigators or implementers with non-overlapping scopes.
5. If one bounded change needs coherence, use a single implementer instead of parallel editors.
6. If you make or accept any non-trivial result, run an independent verification step before claiming completion.
7. If the workflow proves reusable, stabilize it into a skill, script, template, or compact memory note.

A compact rule of thumb:
- Small + obvious -> controller executes directly
- Unclear + read-heavy -> planner/investigator first
- Independent + parallel-safe -> parallel child tasks
- One coherent change -> single implementer
- Anything important -> independent verification

## Recommended Decision Rules

Use a planner first when:
- task scope is broad
- file touch points are unclear
- there are multiple possible implementation paths

Use parallel investigators when:
- questions are independent
- read-only exploration will reduce uncertainty
- child tasks will not step on each other

Use a single implementer when:
- one bounded change must be made coherently
- edits touch the same file set
- consistency matters more than concurrency

Use direct controller execution when:
- the task is trivial or only a couple of steps
- the tool path is obvious and isolated
- delegation overhead would exceed the work itself
- no meaningful role separation is gained by spawning a child

Use reviewers every time when:
- the task is non-trivial
- correctness matters
- the user asked to solidify a reusable collaboration process

## Anti-Patterns

Avoid:
- delegating before gathering enough context
- vague child prompts
- overlapping concurrent editors
- letting the implementer self-approve
- skipping the spec review because tests pass
- skipping controller verification because reviewer sounded confident
- telling the user work is done based only on subagent summaries

## Relationship to Other Skills

- use `writing-plans` when you need a formal implementation plan first
- use `subagent-driven-development` when executing a plan task-by-task with review loops
- use `dispatching-parallel-agents` when concurrency is the main benefit
- use `verification-before-completion` before any final success claim

## Remember

Subagents are specialists, not owners.
Hermes is the controller.
Partition carefully.
Review independently.
Verify centrally.
Then report completion.
