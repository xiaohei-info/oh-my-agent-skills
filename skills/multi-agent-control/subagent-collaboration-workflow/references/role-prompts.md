# Role Prompt Templates

Use these as controller-side starting points and customize per task.

## Planner

Goal:
Produce a task decomposition for the requested work.

Context template:
- Objective: ...
- Repo/workdir: ...
- Constraints: ...
- Relevant files already known: ...
- Output required:
  1. task breakdown
  2. likely files touched
  3. dependencies and risks
  4. suggested verification
  5. which tasks are safe to parallelize
- Do not modify files.

## Investigator

Goal:
Inspect one subsystem and report findings.

Context template:
- Question to answer: ...
- Repo/workdir: ...
- Scope boundaries: inspect only ...
- Files or symbols to inspect: ...
- Output required:
  1. findings
  2. exact files/functions involved
  3. risks or uncertainties
  4. follow-up questions if any
- Read-only. Do not modify files.

## Implementer

Goal:
Implement one bounded change.

Context template:
- Task: ...
- Repo/workdir: ...
- Allowed files: ...
- Non-goals: ...
- Required checks/tests: ...
- Output required:
  1. files changed
  2. summary of changes
  3. commands run and results
  4. remaining risks
- Avoid unrelated edits.

## Spec Reviewer

Goal:
Check whether implementation matches the requested task exactly.

Context template:
- Original request/spec: ...
- Files to inspect: ...
- Check:
  - all required scope implemented
  - no missing acceptance criteria
  - no unrelated extra changes
  - paths/signatures/behavior match request
- Output required:
  - PASS or FAIL
  - exact gaps if FAIL
- Read-only. Do not modify files.

## Quality Reviewer

Goal:
Review implementation quality after spec compliance.

Context template:
- Files to inspect: ...
- Review dimensions:
  - maintainability
  - readability
  - edge cases
  - test sufficiency
  - bug/security risk
- Output required:
  - Critical issues
  - Important issues
  - Minor issues
  - Verdict: APPROVED or REQUEST_CHANGES
- Read-only. Do not modify files.

## Fix-Up Implementer

Goal:
Address only the review findings that were accepted by the controller.

Context template:
- Accepted issues to fix: ...
- Repo/workdir: ...
- Files likely involved: ...
- Non-goals: do not expand scope beyond listed issues
- Required checks/tests: ...
- Output required:
  1. issues addressed
  2. exact changes made
  3. commands run and results
  4. remaining concerns

## Parallel Batch Pattern

Use when tasks are read-only and independent.
For each task include:
- one precise question
- strict subsystem/file boundary
- read-only instruction
- expected output format

Avoid parallel edit tasks unless file overlap is confidently near zero.
