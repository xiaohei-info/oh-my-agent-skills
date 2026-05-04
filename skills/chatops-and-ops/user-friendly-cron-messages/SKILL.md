---
name: user-friendly-cron-messages
description: Use when creating or refining any Hermes cron job whose final delivery goes to humans on Telegram or similar chat platforms. Prioritize user-readable alert design, compact default output, severity gating, and exception-driven expansion over exhaustive internal dumps.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [cron, telegram, alerting, ux, monitoring, reporting, messaging]
    related_skills: [ops-sentry, writing-skills, cron-model-naming-for-custom-providers]
---

# User-Friendly Cron Messages

## Overview

Cron jobs often fail at the last mile: the underlying work may be correct, but the delivered message is too long, too repetitive, and too hard to scan on Telegram. This skill defines a practical default for **human-facing cron output across any recurring task type**:

- default to short messages
- expand only when something materially changed
- lead with user actionability, not internal completeness
- optimize for inbox scanning, not archival verbosity

This is a **general-purpose cron UX skill**. It applies to trading monitors, ops alerts, daily summaries, research digests, reminders, account checks, health checks, task nudges, and any other recurring chat-delivered cron output.

## When To Use

Use when:
- creating a new cron job that delivers to Telegram/chat
- refactoring an existing cron job whose output is too long or repetitive
- converting a report-style cron into a recurring alert/check-in format
- designing threshold-based monitors, summaries, reminders, reports, or health checks
- any cron output is meant to be consumed quickly by a human in chat

Do **not** use when:
- the cron output is machine-consumed only
- the output is stored as a local artifact/file and not delivered as a chat message
- the user explicitly wants full verbose detail every run

## Core Principle

**Cron output for chat should be written for the recipient’s next 5 seconds, not the model’s last 5 minutes.**

That means:
1. surface priority first
2. compress routine cases aggressively
3. only expand when the user’s interpretation or action materially changes
4. remove repeated low-signal boilerplate
5. preserve the minimum core context needed for trust and action

## Universal Message Architecture

For recurring user-facing cron jobs, prefer a 3-layer structure.

### Layer 1: Message-level priority
Always start with a clear status line.

Generic examples:
- `🟢 常规更新｜...`
- `🟡 需要关注｜...`
- `🔴 重要变化｜...`

Domain-specific variants are fine, but the user should understand urgency from the first line.

### Layer 2: One-screen default summary
The default version should usually fit in ~8–20 lines, depending on task type.

Recommended order:
1. priority/status line
2. one-line change statement
3. compact core facts block
4. only the items that matter now (triggered / changed / due / blocked / ready)
5. compact state/context line if relevant
6. up to 3 recommended actions or next steps
7. up to 2 things not to do / deprioritize / ignore
8. single biggest risk, blocker, or caveat
9. next watchpoints / next checkpoint
10. fixed confirmation/disclaimer line if needed

### Layer 3: Exception-driven expansion
Add a second, longer mode only when needed.

Expand when:
- a key threshold is crossed
- a prior assumption is invalidated
- multiple important conditions change together
- a major event materially changes interpretation
- the recommended action changes materially
- a new blocker or risk appears
- a previously pending item becomes actionable

The expanded mode should still be chat-friendly (roughly 15–35 lines), not a full essay.

## Design Rules

### 1. Default short, not default complete
Do not dump every checked condition every time.

Bad:
- listing every unchanged check on every run
- repeating the same background section each cycle
- turning routine cron output into mini reports

Good:
- list only changed, triggered, due, blocked, or nearly actionable items
- summarize all-clear cases in one sentence
- keep unchanged sections terse

### 2. Lead with action state
Every recurring monitor or summary should expose a single top-level takeaway.

Examples:
- no action needed
- ready to act
- review soon
- blocked pending input
- pause new action
- follow up today
- urgent attention needed

The user should know the operational takeaway before reading the rationale.

### 3. Separate routine from exception
Use two modes:
- **routine mode** for no major change
- **expanded mode** for meaningful change

A common mistake is forcing one format to serve both. That creates either overload or under-explanation.

### 4. Show what changed, not the full internal checklist
If the cron evaluates many conditions, the delivered message should usually show:
- changed items
- triggered items
- nearly triggered items
- newly blocked / newly ready items
- one-line summary for everything else

Keep the full internal checklist in prompt logic if needed, but not in every user-facing message.

### 5. Preserve statefulness compactly
If the cron depends on user state, prior execution state, or environmental context, include a short state line.

Examples:
- `状态: 已读[否] | 等待输入[是] | 假设[上次计划未执行]`
- `状态: 服务[正常] | 错误[0] | 上次异常[已恢复]`
- `状态: 账户[已同步] | 提醒[未确认] | 依赖[缺用户回复]`

This anchors the advice without restating the entire framework.

### 6. Chat messages are not reports
Avoid:
- long markdown tables
- long narrative transitions
- repeated caveat paragraphs
- raw dumps of fetched data
- multiple near-duplicate recommendations
- excessive historical recap when the current state is enough

Prefer:
- bullets
- icons or short labels
- 1-line sections
- numeric anchors
- explicit next steps

## Practical Output Template

A good default Telegram cron message often looks like this:

1. Priority line
2. Short change statement
3. Core facts block
4. What matters now
5. State line (if relevant)
6. Recommended next steps
7. Not recommended / can ignore for now
8. Key blocker / risk / caveat
9. Watch next / next check time
10. Reply template / requested user update (if needed)
11. Fixed closing note

## Expansion Triggers

Use expanded mode when any of the following happen:
- threshold crossed
- threshold nearly crossed and user should prepare
- thesis/assumption invalidated or weakened
- important blocker appears or clears
- major event changes decision quality
- multiple signals fire together
- recommended action changes from last run
- status escalates from routine to attention/urgent

In expanded mode, include:
- what changed
- why it matters
- what prior assumption or state changed
- how the recommendation changes
- what to watch next

## Telegram-Specific Guidance

Telegram is skim-first and mobile-first.

Therefore:
- put the most important line first
- avoid walls of text
- keep section count small
- avoid tables
- use lightweight emoji as scan anchors, not decoration overload
- assume the user may read from notification preview or chat list first

Good emoji anchors:
- `📌` summary / topic
- `📍` current context
- `📊` metrics / range / progress
- `🎯` action state
- `🔥` triggered / changed now
- `⚠️` risk / blocker
- `✅` next action
- `👀` watch next
- `📝` reply template / update request

## Template Selection Guide

Use this quick routing guide before writing a cron prompt.

### Choose `alert-template.md` when
- the cron monitors thresholds, failures, health, or state changes
- the main question is: **did something trigger, change, or break?**
- examples: API health, job failures, price alerts, threshold monitors, abnormal condition detection

### Choose `digest-template.md` when
- the cron summarizes a time window into a concise briefing
- the main question is: **what mattered this cycle, and what changed since last time?**
- examples: daily review, market recap, weekly digest, research summary, periodic briefing

### Choose `reminder-template.md` when
- the cron nudges the user to do something or reply
- the main question is: **what is due now, and what is the shortest next action?**
- examples: follow-up reminders, pending confirmations, scheduled nudges, task reminders

### Choose `workflow-check-template.md` when
- the cron checks whether work can proceed, should wait, or is blocked
- the main question is: **is the system/user/process ready to continue?**
- examples: pre-trade checks, deployment readiness, account readiness, execution gates, prerequisite validation

### If multiple templates seem plausible
Use the template matching the user's immediate decision:
- **trigger/change detection** → alert
- **period summary** → digest
- **user nudge** → reminder
- **go/wait/pause/blocked judgment** → workflow-check

### Practical heuristic
Ask: what should the user understand first?
- "Something changed" → alert
- "Here is the summary" → digest
- "Please do this" → reminder
- "You can / cannot proceed" → workflow-check

## Adaptation By Cron Type

This skill is intentionally cross-domain. Adapt the same structure to different cron types:

### 1. Monitoring / Alerting
Examples:
- system health
- price alerts
- API failures
- job health checks

Emphasize:
- severity
- what changed
- action required or not
- blocker / blast radius

### 2. Reminder / Follow-up
Examples:
- reply reminders
- scheduled follow-up nudges
- recurring planning prompts

Emphasize:
- what is due now
- why it matters now
- shortest next action
- whether user input is needed

### 3. Digest / Summary
Examples:
- daily review
- weekly digest
- research summary
- market recap

Emphasize:
- 3–5 most important takeaways
- what changed since last cycle
- what to watch next
- what can safely be ignored

### 4. Workflow / Execution Check
Examples:
- pre-trade checks
- deployment readiness checks
- operations checklists
- account review tasks

Emphasize:
- go / wait / pause / blocked state
- missing prerequisites
- changed constraints
- next safe action

## What To Keep vs Compress

Keep:
- current regime / state / status
- current action label
- changed or newly relevant items
- one key risk or blocker
- next watchpoints / next step
- state relevant to recommendations

Compress or omit:
- unchanged checks
- long justifications for unchanged conclusions
- exhaustive data lists unless they alter action
- multi-paragraph caveats
- duplicated context from previous runs
- internal reasoning that does not improve user action quality

## Prompt-Writing Guidance

When editing cron prompts, explicitly instruct the model to:
- choose one top-level action or status label
- produce one of two output modes
- list only changed / triggered / near-triggered / newly due items in routine mode
- cap recommendations and anti-recommendations
- cap risk/blocker section length
- explain assumption invalidation only in expanded mode
- optimize for Telegram readability, not completeness

Useful prompt clauses:
- "default to short routine output"
- "expand only on material change"
- "do not list untouched checks one by one"
- "first line must indicate priority level"
- "fit routine mode in ~8–20 lines"
- "expanded mode should remain chat-friendly"
- "optimize for fast human scanning on Telegram"

## Anti-Patterns

Avoid these common failures:

1. **Checklist spam**
   - every condition every run
   - every field re-explained in full

2. **Analysis dump disguised as alert**
   - full memo delivered on a frequent cadence

3. **No escalation framing**
   - user cannot tell if a message matters more than the last one

4. **Too many recommendations**
   - user gets 5–8 competing actions and does nothing

5. **Verbose blocker/risk section**
   - the warning becomes wallpaper and stops being read

6. **No distinction between “watch”, “prepare”, and “act”**
   - creates alert fatigue and lower trust

7. **Domain-locking a generic cron UX pattern**
   - writing the guidance as if it only applies to one scenario when it is broadly reusable

## Verification Checklist

Before finalizing a chat-facing cron prompt, verify:
- does the first line signal urgency or priority?
- can the user understand the top-level takeaway in under 5 seconds?
- does the routine version avoid full checklist dumps?
- is there an explicit expanded mode for important changes?
- are recommendations capped and non-redundant?
- is the message readable on mobile without endless scrolling?
- does it preserve core decision information while compressing routine noise?
- is the structure reusable across other cron types, not just the current one?

For a reusable pre-flight checklist, see `references/checklist.md`.

## Expected Outcome

A well-designed human-facing cron should feel like:
- low-noise in normal conditions
- high-signal when something matters
- easy to scan from Telegram notifications and list view
- trustworthy because important changes are clearly escalated
- actionable without forcing the user to decode a mini report every cycle

The goal is not maximum textual completeness. The goal is **maximum user comprehension per notification**.
