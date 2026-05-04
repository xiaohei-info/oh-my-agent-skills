# Bundle Guide

This document helps you choose the right bundle based on the workflow problem you want to fix.

The bundle folders are a **modular browsing surface**. You can adopt one skill, one bundle, or mix individual skills across bundles.

## engineering-execution

**Use this bundle when:**
- agents claim completion too early
- debugging turns into guess-and-check
- you want a stricter evidence standard before saying work is done

**Included skills:**
- `verification-before-completion`
- `systematic-debugging`

**What it gives you:**
- no success claims without fresh verification
- no bug fixes without root-cause investigation first
- better regression discipline before declaring something fixed

**Typical Hermes install target:**
- `software-development/*`

## multi-agent-control

**Use this bundle when:**
- child agents drift or overlap
- delegation prompts are too vague
- same-file parallel work keeps causing collisions
- you want controller-side discipline instead of just more agents

**Included skills:**
- `subagent-first`
- `subagent-collaboration-workflow`

**What it gives you:**
- bounded delegation contracts
- clearer controller vs child responsibilities
- better wave-based parallelism decisions
- stronger verification separation after delegated work

**Typical Hermes install targets:**
- `autonomous-ai-agents/subagent-first`
- `software-development/subagent-collaboration-workflow`

## skill-engineering

**Use this bundle when:**
- good workflows keep getting lost between runs
- your skills are hard to discover or maintain
- you want to package or publish skills for reuse

**Included skills:**
- `skill-optimizer`
- `writing-skills`
- `external-hermes-skills-lifecycle`

**What it gives you:**
- better skill authoring structure
- stronger packaging hygiene
- repeatable improvement loops for existing skills

**Typical Hermes install targets:**
- `meta/skill-optimizer`
- `software-development/writing-skills`
- `software-development/external-hermes-skills-lifecycle`

## chatops-and-ops

**Use this bundle when:**
- cron outputs read like internal dumps
- alerts are noisy, stale, or repetitive
- automation is technically correct but not actually useful to the human reader

**Included skills:**
- `user-friendly-cron-messages`
- `ops-sentry`

**What it gives you:**
- short, actionable, human-readable recurring messages
- lower alert fatigue
- clearer distinction between routine output and exception-mode output

**Typical Hermes install target:**
- `devops/*`

## research-and-reading

**Use this bundle when:**
- URL reading is inconsistent or too heavy
- browser use is overkill for simple pages
- you want deeper judgment than one-pass summarization

**Included skills:**
- `web-reading-router`
- `hv-analysis`

**What it gives you:**
- a lighter and more reliable reading-tool routing habit
- stronger horizontal + vertical analysis workflows
- better research structure for reports and synthesis

**Typical Hermes install target:**
- `research/*`

## knowledge-compilation

**Use this bundle when:**
- notes accumulate but do not compile into durable knowledge
- source material and stable knowledge are mixed together
- your vault needs ingestion, lint, and triage discipline

**Included skills:**
- `karpathy-llm-wiki-obsidian`
- `obsidian-inbox-to-wiki-ingest`
- `obsidian-wiki-lint-triage`

**What it gives you:**
- clearer source-space vs compiled-knowledge boundaries
- better inbox-to-wiki workflows
- healthier long-lived knowledge maintenance

**Typical Hermes install target:**
- `note-taking/*`

## How to choose between bundles

Pick the smallest set that solves the problem you actually have:
- choose **engineering-execution** if reliability and proof are the issue
- choose **multi-agent-control** if delegation quality is the issue
- choose **chatops-and-ops** if human-facing automation UX is the issue
- choose **research-and-reading** if information intake and synthesis are the issue
- choose **knowledge-compilation** if durable knowledge maintenance is the issue
- choose **skill-engineering** if your main goal is turning methods into reusable assets

## Installation reminder

Public bundle names are for repo browsing.

When installing into Hermes, place each skill under its original category path and preserve the whole skill directory. Use [`docs/source-map.md`](source-map.md) whenever the destination is not obvious.
