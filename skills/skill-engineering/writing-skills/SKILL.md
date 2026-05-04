---
name: writing-skills
description: Use when creating, revising, or validating Hermes skills so they are discoverable, reusable, and grounded in real successful workflows.
version: 1.0.0
author: Hermes Agent (adapted from obra/superpowers)
license: MIT
metadata:
  hermes:
    tags: [skills, documentation, workflow, reuse]
    related_skills: [verification-before-completion, writing-plans, systematic-debugging]
---

# Writing Skills

## Overview

A good skill captures a reusable method, not a one-off story. It should help future sessions recognize when to load it and exactly how to use it.

Core principle: write skills from proven workflows, then verify they are clear and reusable.

## Use This When

Use when:
- creating a new Hermes skill
- updating a stale or incomplete skill
- converting a proven workflow into reusable procedural memory
- evaluating whether something should be a skill at all

## What A Skill Is

A skill is:
- a reusable technique
- a repeatable workflow
- a reference guide for a recurring task
- a compact procedure that improves future execution

A skill is not:
- a diary of one session
- raw notes with no trigger conditions
- project-specific temporary state
- something that should instead be enforced mechanically in code or tests

## Before Writing A Skill

Confirm all of these:
1. the workflow actually worked
2. it is likely to recur
3. future-you would benefit from loading it
4. the value comes from judgment/process, not just static data

## Skill Design Rules

### 1. Optimize for discovery

The `description` should primarily answer: when should this skill be used?
Do not stuff the description with the full workflow.
Trigger conditions are more important than implementation summary.

### 2. Optimize for execution

The body should include:
- what the skill is for
- when to use it and when not to use it
- concrete steps in order
- commands or tool patterns when relevant
- pitfalls and verification steps

### 3. Keep the boundary clean

Prefer:
- one clear workflow per skill
- linked references only when they truly reduce clutter
- concise wording over narrative prose

## Recommended Structure

A solid Hermes skill usually includes:
- YAML frontmatter
- Overview
- When to Use
- Steps / Process
- Pitfalls or Common Mistakes
- Verification / Expected Outcome

## Hermes-Specific Guidance

When authoring skills for Hermes:
- use Hermes tool names and workflows, not Claude/Codex-specific ones
- reference `delegate_task`, `todo`, `skill_manage`, `search_files`, `read_file`, `patch`, `terminal`, etc. where appropriate
- avoid assumptions about non-Hermes runtime features unless clearly labeled
- keep instructions compatible with Hermes categories and naming style

## Validation Checklist

Before saving or updating a skill, check:
- is the trigger condition clear?
- does the description describe when to use it?
- are the steps specific enough to follow?
- does it avoid session-specific temporary details?
- does it fit Hermes tools and conventions?
- is there any stale or platform-specific wording to remove?

## Anti-Patterns

Avoid:
- copying a foreign skill verbatim without adapting tool names and assumptions
- writing a description that summarizes the whole process instead of the trigger
- recording one-off progress as a skill
- leaving ambiguous steps that require guessing
- creating a skill when a simple memory note would be enough

## Remember

A skill should save future effort. If it won't reliably help future execution, do not turn it into a skill.