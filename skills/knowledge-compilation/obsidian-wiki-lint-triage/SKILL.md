---
name: obsidian-wiki-lint-triage
description: Review the health of an existing `_wiki/` compiled knowledge layer, surface priority fixes, and triage backlog candidates. Use after initial wiki scaffolding or periodically during maintenance.
version: 1.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, llm-wiki, lint, maintenance, triage, wiki-curation, knowledge-base]
    related_skills: [karpathy-llm-wiki-obsidian, obsidian, obsidian-inbox-to-wiki-ingest]
---

# Obsidian Wiki Lint Triage

## Overview

Use this skill when `_wiki/` exists and Hermes should review its structural health, surface problems, and propose fixes in priority order.

This is an **execution skill**, not a methodology skill. It assumes a Karpathy-style wiki is already in place:
- `Inbox/` = source space
- `_wiki/` = compiled knowledge

Core principle: **lint for knowledge health, not typo/formatting**.

## Default Mode: Audit-Only

Default lint behavior is audit-only.

Read scope:
- all of `_wiki/`
- relevant source candidates anywhere under `Inbox/`, including `Inbox/hermes/default/`

Default write scope:
- none

Unless the user explicitly asks for repairs or persistent audit logging, do not modify `_wiki/` pages, do not rewrite `_wiki/index.md`, and do not append/prepend to `_wiki/log.md`.

Lint should surface findings and recommended repairs first. Repair is a separate follow-up step.

## When to Use

Use when:
- the user asks to lint or check `_wiki/`
- `_wiki/` has grown and may have duplicates, orphans, stale pages, or navigation gaps
- Hermes should surface backlog items stuck in `Inbox/` that now deserve compilation
- the user wants a structured triage report rather than a laundry list

Do not use when:
- the task is to explain the Karpathy workflow itself; use `karpathy-llm-wiki-obsidian`
- the task is to ingest one specific note; use `obsidian-inbox-to-wiki-ingest`
- `_wiki/` has not yet been scaffolded

## Preflight

Before judging health:
1. confirm the vault path
2. if a vault-root `AGENTS.md` exists, read it for local mappings and writeback conventions
3. if `_wiki/hot.md` exists, read it first for recent context
4. inspect the live `_wiki/` structure and key pages
5. determine whether a legacy `Wiki/` tree is also present

## What Lint Checks

Lint should answer seven structural questions:
1. Is `_wiki/` still navigable?
2. Are there duplicate or synonym pages?
3. Are there orphan or weakly linked pages?
4. Are any pages outdated or contradicted by newer sources?
5. Are there missing high-value pages that should exist?
6. Is important `Inbox/` content still stuck uncompiled?
7. Is the vault in a split-root state where both `_wiki/` and a populated legacy `Wiki/` tree coexist?

## Valid Extensions and Carrier Artifacts

Do not mistake a richer carrier-specific layout for structural drift.
By default, treat these as valid `_wiki/` extensions when they are actively used by the local workflow:
- `hot.md` for short-lived recent-context cache
- `domains/` for top-level topic entry pages
- `meta/` for dashboards, manifests, lint reports, or other maintenance artifacts
- optional `canvases/` or `folds/` when the local workflow explicitly creates them

Also distinguish compiled wiki content from vault-root workflow/runtime folders such as `.agents/`, `.codex/`, and `.vault-meta/`.
Those folders may define local carrier behavior, but they are not themselves `_wiki/` health targets unless their conventions directly affect navigation, provenance, or writeback inside `_wiki/`.

## Navigation Checks

Inspect:
- `_wiki/index.md` reflects the real current structure
- important pages have clear entries in the index
- `overview.md` still matches the intended scope
- recent high-value pages are findable via index or nearby links
- when present as first-class local conventions, `hot.md`, `domains/`, and key `meta/` pages are consistent with the compiled layer's real current state

If navigation is broken, report it as a P1 issue. Only fix `_wiki/index.md` during lint when the user explicitly requests writeback.

## Duplicate and Synonym Handling

Detect:
- pages with the same object under different filenames
- naming variants that represent the same concept/entity
- repeated summaries across `sources/` that could be merged

Actions:
- recommend one canonical page
- recommend merge targets instead of proliferating pages
- do not merge synonym pages during audit-only lint unless the user explicitly requests repairs

## Orphan and Link Health

Detect:
- pages in `_wiki/` with no incoming links
- pages referenced only from obscure corners
- concepts/entities that should appear in `sources/` pages but do not

Actions:
- recommend link additions before any deletion
- recommend downgrade or merge only if the page truly lacks future value
- do not delete, merge, or downgrade pages during audit-only lint unless the user explicitly requests repairs

## Outdated or Contradicted Content

Detect:
- core topic pages contradicted by newer `sources/`
- stale thesis pages in `syntheses/` that no longer reflect current understanding
- unanswered or stale `questions/` that newer sources may resolve

Actions:
- identify pages contradicted by newer evidence
- recommend exact updates for materially wrong core pages
- do not silently rewrite pages during audit-only lint unless the user explicitly requests repairs

## Missing High-Value Pages

Detect:
- concepts/entities that recur across multiple `sources/` but have no dedicated page
- questions that are repeatedly asked across sources but not yet compiled into `questions/`
- comparison opportunities that would clarify a decision

Gate: do not create pages merely for neatness. Create only when the missing page is:
- recurring
- reusable
- likely to save future work

## Inbox Backlog Candidates

Detect:
- raw notes in `Inbox/` that now justify compilation because they:
  - relate to an established wiki topic
  - add evidence to an existing question or synthesis
  - introduce a stable recurring concept/entity
  - would clarify an important distinction

Actions:
- list backlog candidates in the lint report
- recommend which items to ingest next using `obsidian-inbox-to-wiki-ingest`

## Split-root / Migration State

Detect:
- whether both `_wiki/` and a populated legacy `Wiki/` tree exist in the same vault
- whether audits aimed at `_wiki/` would therefore under-report the health of the currently active compiled corpus
- whether new ingest into `_wiki/` is at risk of duplicating already-compiled material that only exists under `Wiki/`

Actions:
- report split-root state explicitly when present
- recommend whether the next step is migration, dual-read caution, or target-root clarification
- do not silently treat a scaffold-only `_wiki/` as a fully healthy compiled system when `Wiki/` still holds the substantive corpus

## Priority Levels

Use a three-tier priority system:
- **P1** — broken index, stale core topic pages, duplicate sprawl harming retrieval, high-value pages not navigable
- **P2** — orphan pages, missing key links, stale question or synthesis pages
- **P3** — naming cleanup, possible new pages, cosmetic structure improvements

Focus on P1 first. P3 should not dominate a lint pass.

## Shared File-Format Expectations

When judging navigation and chronology, treat these as the expected minimums:
- `_wiki/index.md`: `- [[path/to/page|Display Title]] — one-line why this page matters`
- if the local workflow keeps `_wiki/log.md` **newest-first** and structured for parseability, do not flag top-prepended entries as a defect
- `_wiki/hot.md`, when present, is a cache file that may be overwritten wholesale rather than appended

## Recommended Lint Procedure

1. Inspect `_wiki/` structure: subfolders, page counts, key pages.
2. Read `_wiki/hot.md` first if it exists.
3. Read `_wiki/index.md` to understand intended navigation.
4. Check for duplicates: similar titles, overlapping concepts, repeated summaries.
5. Check for orphans: pages with no wikilinks pointing to them.
6. Check outdated content: compare `sources/` dates to core pages.
7. Check missing pages: concepts/entities that recur in sources but lack dedicated pages.
8. Check `Inbox/` backlog: candidates now worth compiling.
9. Write a structured lint report, not a raw dump.
10. Prioritize fixes into P1/P2/P3.
11. If and only if the user asked for writeback or persistent audit logging, prepend a concise entry to `_wiki/log.md` using the local convention; otherwise leave vault files unchanged.

## Output Structure

For this user's current vault, lint output should default to **Chinese** unless the user explicitly asks for English.

A lint pass should produce a short report in this form:
1. **Healthy**: one-line status for what is working well
2. **Findings**: grouped by category (duplicates, orphans, outdated, missing, backlog)
3. **Priority Fixes**: P1 items with specific pages and recommended actions, marked as not yet applied unless repair mode was explicitly requested
4. **Backlog Candidates**: `Inbox/` items recommended for next ingest
5. **Suggested Next Ingest / Synthesis**: optional recommendation for next major wiki work

Keep the report concise. Do not dump full page lists.

## Anti-Patterns

Avoid:
- large refactors during lint
- creating pages just for neatness
- moving raw content directly into `_wiki/`
- treating `hot.md`, `domains/`, or `meta/` as structural bugs merely because they are optional in another carrier
- over-prioritizing minor formatting issues
- focusing on format over knowledge validity
- leaving outdated core pages unchanged because they are “stable”
- silently repairing pages during an audit-only run

## Verification

Before claiming lint is complete, confirm:
- `AGENTS.md` was consulted when present
- `_wiki/hot.md` and `_wiki/index.md` were actually inspected
- duplicates and orphans were detected by reading page content, not filenames alone
- outdated pages were identified against newer `sources/`
- backlog candidates are grounded in `Inbox/` inspection
- the lint report is structured and concise
- no vault files were modified unless the user explicitly requested writeback

## Expected Outcome

A successful run of this skill should leave:
- a structured triage report delivered to the user
- a clear list of P1 fixes if any
- a short backlog candidate list if any
- an optional `_wiki/log.md` update only if writeback was explicitly requested
- a recommendation for next ingest or synthesis work
- no speculative page creation or silent repairs during audit-only lint
