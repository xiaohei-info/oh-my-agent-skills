---
name: verification-before-completion
description: Use before claiming work is complete, fixed, or passing. Requires fresh verification evidence before any success claim.
version: 1.0.0
author: Hermes Agent (adapted from obra/superpowers)
license: MIT
metadata:
  hermes:
    tags: [verification, testing, workflow, quality]
    related_skills: [systematic-debugging, requesting-code-review, test-driven-development]
---

# Verification Before Completion

## Overview

Do not claim success without fresh evidence. "Should pass", "looks fixed", and "probably done" are not verification.

Core principle: evidence before claims.

## Use This When

Always use before:
- saying a bug is fixed
- saying tests pass
- saying a build succeeds
- saying a task is complete
- committing or opening a PR after code changes
- reporting subagent work as done

## The Rule

No completion claims without fresh verification evidence from this session.

That means:
1. Identify the exact command that proves the claim.
2. Run it now.
3. Read the full output and exit status.
4. Only make the claim the output actually supports.

## Required Process

### 1. Match claim to proof

Examples:
- "Tests pass" -> run the relevant test command
- "Build succeeds" -> run the build command
- "Bug is fixed" -> reproduce the original failure path or run the regression test
- "Requirements are done" -> compare results against the requirement list, not just tests

### 2. Run the full verification

Use the real command, not a weaker proxy.

Bad:
- running lint and claiming build works
- running one test and claiming the whole suite passes
- trusting an old run
- trusting another agent's summary

Good:
- run the exact test target or suite
- run the actual build
- run the exact reproduction steps for the bug

### 3. Report evidence, not vibes

Good:
- "Ran `pytest tests/foo_test.py -q`: 12 passed."
- "Ran `npm run build`: exit 0."
- "Reproduced the old failing case and it now passes."

Bad:
- "Looks good"
- "Should be fixed now"
- "Done"

## Red Flags

Stop and verify if you catch yourself thinking:
- "probably"
- "should"
- "seems fine"
- "I only changed a small thing"
- "the subagent said it passed"
- "I'm sure it works"

## Common Failure Modes

- Partial verification presented as full verification
- Old output reused as if fresh
- Wrong command for the claim
- No exit code checked
- No regression path tested
- Requirements assumed from passing tests

## Special Cases

### Subagent work

Never trust a delegated task's success report by itself.
Check the actual diff, files, or verification command yourself before reporting success.
The verifier must be independent from the implementer role: ideally the controller session verifies directly, or a fresh reviewer checks the result before the controller makes any completion claim.

### Bug fixes

Prefer proving both:
1. the old failure is covered
2. the fixed behavior now passes

### Requirement completion

Re-read the requirement list and explicitly note anything unverified or out of scope.

## Value-for-Spend Closeout Gate

When the task was non-trivial or consumed meaningful token / tool / coordination budget, also ask:
- What actual customer value came out of this spend?
- Was the spend proportionate to that value?
- What part of the work was high leverage, and what part was avoidable overhead?
- If this had to be done again next week, what would be the cheaper path?

This does **not** replace verification. It adds an ROI lens after evidence is already established.

## Output Pattern

Use this structure when wrapping up:
- What I ran
- What the result was
- What claim that result supports
- What is still unverified, if anything
- For non-trivial work: why this spend was worth it, or how the next run should be cheaper

## Remember

Verification is not ceremony. It is the difference between reporting facts and guessing.
For meaningful work, the closeout should also help improve future value per token/spend.