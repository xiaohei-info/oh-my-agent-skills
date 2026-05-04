---
name: obsidian-inbox-to-wiki-ingest
description: Compile one or more raw Obsidian Inbox notes into the `_wiki/` layer using controlled source pages, selective downstream updates, and mandatory index/log maintenance.
version: 1.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, llm-wiki, ingest, inbox, wiki-curation, knowledge-base]
    related_skills: [karpathy-llm-wiki-obsidian, obsidian, obsidian-wiki-lint-triage]
---

# Obsidian Inbox to Wiki Ingest

## Overview

Use this skill when raw material already exists in an Obsidian vault `Inbox/` and Hermes should compile it into the `_wiki/` layer.

This is an **execution skill**, not a methodology skill. It assumes the Karpathy-style boundary is already chosen:
- `Inbox/` = source space
- `_wiki/` = compiled reusable knowledge

Core principle: **compile with judgment, not summary spam**.

## When to Use

Use when:
- the user asks to ingest a note, article clipping, transcript, or source already stored in `Inbox/`
- Hermes should promote a raw note into `_wiki/sources/`
- Hermes should decide whether a source also requires updates to `concepts/`, `entities/`, `questions/`, `syntheses/`, or `comparisons/`
- the user wants a repeatable `Inbox/ -> _wiki/` curation pass

Do not use when:
- the task is only to explain the Karpathy workflow itself; use `karpathy-llm-wiki-obsidian`
- the task is only to maintain/lint `_wiki/`; use `obsidian-wiki-lint-triage`
- the source has not been read yet
- the material is too ambiguous to place and needs user prioritization first

## Preflight

Before writing anything:
1. confirm the vault path
2. if a vault-root `AGENTS.md` exists, read it for local folder mappings and guardrails
3. if `_wiki/hot.md` exists, read it for recent context before deciding ingest scope
4. locate the raw source note under `Inbox/`
5. inspect `_wiki/` structure and existing related pages
6. decide whether this source is worth compiling now

Use Hermes file tools:
- `search_files` for discovery
- `read_file` for source inspection and related page review
- `write_file` for new pages
- `patch` for targeted updates

## Source Identity and Dedup

Treat every note under `Inbox/` as valid source input, including `Inbox/hermes/default/...`.

Treat vault-root workflow/runtime folders such as `.agents/`, `.codex/`, and `.vault-meta/` as carrier infrastructure, not as source notes and not as compiled wiki pages.
They may define how the local wiki workflow runs, but they do not change the fundamental boundary that `Inbox/` is source space and `_wiki/` is the compiled target.

If the vault also contains a populated legacy `Wiki/` tree, inspect it during preflight before creating new compiled pages in `_wiki/`. The goal is not to keep writing into `Wiki/`, but to avoid duplicating already-compiled material while the vault is in a split-root or migration state.

### Manifest-aware dedup contract

In generic Hermes workflows, `source_path` is the primary dedup key.

In vaults that maintain `Inbox/.manifest.json` with source hashes and `address_map`:
- treat `Inbox/.manifest.json` as the primary delta/dedup contract when it exists
- check whether the source path is already present with the same content hash
- reuse an existing page/address mapping when the manifest already records it
- keep `source_path` in the compiled page as provenance metadata even when manifest-based dedup is available

Before creating a new `_wiki/sources/` page:
1. capture the note's current vault-relative path exactly, for example `Inbox/...`
2. if `Inbox/.manifest.json` exists, inspect it first for prior ingest state and any `address_map` reuse opportunity
3. search `_wiki/sources/` for that exact `source_path`
4. if the note contains a canonical external URL, DOI, video URL, paper ID, or similar durable identifier, search for that too
5. if a matching source page already exists, update it instead of creating a second source page
6. if a relevant compiled page exists only under a legacy `Wiki/` tree, treat that as migration context and make the overlap explicit before creating new duplicate compiled material

Minimum frontmatter for each `sources/` page:
- `source_path: Inbox/...`
- `source_title: ...`
- `source_canonical: ...` (optional)
- `ingested_on: YYYY-MM-DD`

Do not create two `_wiki/sources/` pages for the same source note unless the user explicitly asks to split treatment.

## Core Decision Gate

Before writing into `_wiki/`, answer these questions:
1. Is this source worth compiling?
2. What theme or topic area does it belong to?
3. Should it update an existing page or create a new one?
4. Is `sources/` only sufficient for now, or does it justify downstream page updates?

If these answers are unclear, do **not** write speculative `_wiki/` content yet.

## What to Extract From Each Source

Read the source itself, not just the title. Extract these six classes:
1. facts
2. claims
3. concepts
4. entities
5. tensions / conflicts / contradictions
6. open questions

If the source contributes little or nothing across these dimensions, it may not deserve full compilation.

## Output Rules

### Language mode configuration

Compiled `_wiki/` output should follow a switchable language mode, not a hardcoded one.

Use these settings:
- `compiled_output_language`: `zh-CN` or `en`
- `compiled_filename_language`: `zh-CN` or `en`
- `preserve_original_source_title`: `true`

Example host policy:
- `compiled_output_language: zh-CN`
- `compiled_filename_language: zh-CN`
- `preserve_original_source_title: true`

Apply this rule consistently:
- page prose, summaries, and section headings follow `compiled_output_language`
- the visible compiled filename should follow `compiled_filename_language`
- keep the original source title in frontmatter when useful
- preserve important original English terms in parentheses when they improve precision in Chinese mode
- do not output an all-English compiled page or filename unless the language mode has been switched to English by the user

### 1. Always start with a `sources/` page

Each ingested source should create or update one page in `_wiki/sources/`.

Recommended filename pattern:
- `YYYY-MM-DD-标题.md`

Minimum structure:
- frontmatter with:
  - `type: source`
  - `source_path: Inbox/...`
  - `source_title: ...`
  - `source_canonical: ...` (optional)
  - `ingested_on: YYYY-MM-DD`
  - `created: YYYY-MM-DD`
  - `updated: YYYY-MM-DD`
  - `status: active`
  - `tags: []`
- `## 摘要`
- `## 核心要点`
- `## 关键事实 / 主张`
- `## 相关概念`
- `## 相关实体`
- `## 张力 / 更新`
- `## 开放问题`

### Provenance discipline

Keep source-grounded content and Hermes synthesis separable:
- `关键事实 / 主张` = statements supported by the current source note
- `张力 / 更新` = corrections, conflicts, or cross-source synthesis
- `开放问题` = unresolved items or follow-up work

Do not slip unattributed inference into `关键事实 / 主张`.
If a statement is not directly supported by the current source note, move it to `张力 / 更新` or `开放问题`.

### 2. Decide whether downstream pages must change

After the `sources/` page, update only the affected downstream pages:
- `_wiki/concepts/`
- `_wiki/entities/`
- `_wiki/questions/`
- `_wiki/syntheses/`
- `_wiki/comparisons/`

For manifest-driven vaults, reusable analytical answers and durable question resolution often prefer `_wiki/questions/` as the first-class landing zone.
Use `_wiki/syntheses/` only when the local schema explicitly treats it as a live compiled page type rather than an optional bucket.

When updating downstream pages, preserve traceability by linking back to the relevant `_wiki/sources/...` page.
Do not make unsupported downstream claims that cannot be traced to a source page or clearly labeled synthesis.

### 3. Source-only ingest is allowed, but must be explicit

Stop at `sources/` only when:
- the source is low-density
- the topic is still unstable
- more sources are needed before abstraction
- the wiki has no stable home for the abstraction yet

Even then, still record:
- candidate concepts
- candidate entities
- open questions
- why source-only was sufficient for now

### 4. Every ingest must update navigation, chronology, and hot cache

A valid ingest also updates:
- `_wiki/index.md`
- `_wiki/log.md`
- `_wiki/hot.md` when that cache file exists in the local workflow

Use stable local-friendly formats:

`_wiki/index.md`
- one curated bullet per page
- format: `- [[path/to/page|Display Title]] — one-line why this page matters`
- place the bullet under the most relevant existing section; do not create many tiny sections during routine ingest

`_wiki/log.md`
- if the local workflow uses newest-first logs, prepend new entries at the **top** of the file
- keep the entry parseable for local tooling such as `wiki-fold`
- preferred format:
  `## YYYY-MM-DD ingest | Source Title`
  `- Source: Inbox/...`
  `- Summary: [[sources/...|Title]]`
  `- Pages created: [[concepts/...]], [[entities/...]]`
  `- Pages updated: [[index]], [[questions/...]]`
  `- Key insight: one sentence`
- if this was source-only ingest, say `Pages updated: none beyond sources/`

`_wiki/hot.md`
- if present, treat it as a cache rather than a journal
- overwrite it wholesale with a concise factual refresh of recent context
- do not append incremental fragments to the bottom

## Page-Type Decision Rules

### Update `concepts/` when
- the source sharpens a recurring idea, method, framework, or distinction
- the concept is likely to reappear across multiple future sources
- an existing concept page needs correction or enrichment

Do not create a concept page for a one-off phrase with no expected reuse.

### Update `entities/` when
- the source materially adds information about a durable person/org/project/product/protocol
- the entity is likely to recur in future notes

### Update `questions/` when
- the source raises or partially resolves a reusable question
- the question is worth revisiting across sources
- the output is effectively a durable answer page in this vault's local workflow

### Update `syntheses/` when
- the source changes an existing multi-source thesis or stage summary
- the local schema explicitly treats `syntheses/` as active compiled output
- the user would likely benefit from a durable merged view rather than isolated source summaries

### Update `comparisons/` when
- the source materially improves a structured A-vs-B or option comparison already underway
- the distinction is clearer in side-by-side form than in standalone pages

## Preferred Editing Behavior

- Prefer updating existing pages over creating duplicates.
- Keep one canonical page per durable object.
- When an existing `sources/` page already matches the same source, update it instead of creating a new page.
- Separate facts from interpretation and unresolved questions.
- Prefer links over dumping repeated prose into many pages.

## Recommended Procedure

1. Find and read the raw `Inbox/` note.
2. Capture the exact `source_path` and inspect any manifest/hash/address_map state when present.
3. Find related `_wiki/` pages by topic, concept, and entity names.
4. Decide the ingest scope:
   - source-only
   - source + specific downstream updates
5. Create or update the `_wiki/sources/` page.
6. Apply only the necessary downstream updates.
7. Update `_wiki/index.md`.
8. Prepend a new `_wiki/log.md` entry.
9. Refresh `_wiki/hot.md` if it exists.
10. Re-read the changed pages to verify coherence.

## Anti-Patterns

Avoid:
- summary-only ingest with no compiled structure
- copying large raw excerpts directly into `_wiki/`
- creating many new pages “for completeness”
- duplicating an existing concept/entity page instead of patching it
- creating a second `sources/` page when dedup or manifest state already shows prior ingest
- treating `.agents/`, `.codex/`, or `.vault-meta/` as source notes
- premature synthesis when one source is not enough
- skipping `index.md`, `log.md`, or active `hot.md`

## Verification

Before claiming ingest is complete, confirm:
- the raw source note was actually read
- the exact `source_path` was captured and checked for duplication
- manifest/hash/address_map state was consulted when present
- the new or updated `sources/` page exists and is traceable to `Inbox/...`
- downstream page updates were selective and justified
- `_wiki/index.md` points to the new or updated material
- `_wiki/log.md` records the ingest in the expected local-friendly format
- `_wiki/hot.md` was refreshed if it is part of the local workflow
- page links and section names are coherent on re-read

## Expected Outcome

A successful run of this skill should leave:
- one traceable `_wiki/sources/` page per ingested source note, created or updated without duplication
- only the necessary downstream wiki updates
- an updated `_wiki/index.md`
- a concise top-prepended `_wiki/log.md` entry
- an updated `_wiki/hot.md` when locally used
- a cleaner and more navigable compiled knowledge layer
