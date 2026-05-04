---
name: karpathy-llm-wiki-obsidian
description: Set up or document a Karpathy-style LLM Wiki workflow in Obsidian, especially when raw material should live in Inbox and compiled knowledge should live in _wiki.
version: 1.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, llm-wiki, karpathy, knowledge-base, methodology]
    related_skills: [obsidian, obsidian-inbox-to-wiki-ingest, obsidian-wiki-lint-triage, web-reading-router]
---

# Karpathy LLM Wiki in Obsidian

## Overview

Use this skill when the user wants to apply Andrej Karpathy's LLM Wiki methodology inside an Obsidian vault.

Core pattern:
- `Inbox/` = full source space (clippings, rough notes, research memos, and Hermes-authored design/workflow notes)
- `_wiki/` = compiled / structured / maintained knowledge layer

The goal is not to build a generic RAG system. The goal is to define a persistent wiki maintenance workflow: ingest raw material, compile it into structured pages, answer from the wiki first, and periodically lint the wiki for health.

## When to Use

Use when:
- the user shares Karpathy's LLM Wiki gist and wants it operationalized
- the user wants an Obsidian-based knowledge workflow with clear raw vs compiled layers
- the user wants design docs, templates, and workflows before implementation
- the user wants Hermes to maintain a persistent wiki instead of producing one-off answers
- the user wants to decide what belongs in `Inbox/`, `_wiki/`, or workflow/schema notes

Do not use when:
- the user only wants a one-off summary of an article
- the user wants a general Obsidian note unrelated to LLM Wiki methodology
- the user has not yet decided where raw and compiled knowledge should live
- the task is specifically to ingest one note or lint `_wiki/`; use the execution skills for that

## Required Mental Model

Always keep the three layers distinct:
1. **Source space**: valid source notes live anywhere under `Inbox/`. They may be clipped material, human notes, or Hermes-authored design/workflow notes. Do not exclude subfolders such as `Inbox/hermes/default/` from source consideration unless the user explicitly creates a non-source area.
2. **Wiki**: LLM-maintained compiled knowledge, usually in `_wiki/`
3. **Schema/workflow**: the rules that tell Hermes how to ingest, query, and lint

Do not collapse source material and compiled knowledge into the same folder or page type.
Do not treat `_wiki/` as an archive dump.

## Responsibilities Split

### Human responsibilities
- choose research direction
- decide which sources matter
- decide which questions are important
- make final calls on key conclusions
- set maintenance priorities

### Hermes responsibilities
- read sources fully
- summarize and extract facts/claims/concepts/entities/questions
- link related pages
- update multiple `_wiki/` pages coherently
- maintain `_wiki/index.md` and `_wiki/log.md`
- surface conflicts, gaps, and next questions
- turn durable answers into reusable wiki pages

## Process

### 1. Read the source methodology first

If the user points to Karpathy's gist or another methodology source:
- read the original source, not a third-party summary
- use `web_extract` first
- if extraction fails, escalate with browser tools
- separate explicit claims from your own interpretation

### 2. Confirm the vault boundary

Before writing docs or scaffolding, determine:
- what counts as the source space
- what folder is the compiled wiki output
- where Hermes should place design notes

For this user's current convention:
- `Inbox/` is the source space
- `_wiki/` is the compiled output layer
- default-profile Hermes design/research notes go in `Inbox/hermes/default/`

### Source-space rule

Treat all of `Inbox/` as source-eligible by default. `Inbox/hermes/default/` is allowed in source scanning when notes there contain durable design, research, or workflow content.

Do not hard-code folder exclusions inside `Inbox/` unless the user explicitly defines a non-source scratch area.

### 3. Inspect the current vault before designing

Use Hermes file tools to verify:
- the vault exists
- the target Inbox path exists or can be created
- whether `_wiki/` already exists
- whether there are existing notes you should match for naming/style
- whether a vault-root `AGENTS.md` exists and defines carrier-specific mappings or guardrails

If the vault path is not already explicit, use the `obsidian` skill's vault-resolution conventions before writing.

Prefer:
- `search_files` for discovery
- `read_file` for note inspection
- `write_file`/`patch` for note creation and edits

If `AGENTS.md` exists at the vault root, read it before assuming the local meaning of folders such as `Inbox/`, `_wiki/`, `Wiki/`, `.raw/`, or `wiki/`.

### 3.1 Indirect-evidence fallback when the live vault is not directly readable

If you cannot directly read the active Obsidian vault files, do not stop at a generic caveat. Look for grounded indirect evidence that still reveals the vault's real operating state, especially:
- plugin backup/state files such as `data.json`, `data.pre-autodetect-backup.json`, or `manifest.json`
- Obsidian `workspace.json` captures
- local verification docs that record real GUI runs against the target vault

Use these artifacts to infer, but clearly label as inferred-from-artifacts rather than directly-read:
- whether settings point to `Inbox/` and `_wiki/`
- whether `_wiki/index.md` and `_wiki/log.md` are part of the active scaffold
- whether `Inbox/hermes/default/` is actively used as source/design space
- whether both `_wiki/` and legacy `Wiki/` are in active coexistence (for example via `lastOpenFiles` in `workspace.json`)
- whether real ingest/query/lint runs have already succeeded in the target system

This fallback is especially valuable for methodology assessment, split-root detection, and deciding whether a source should be ingested now.
Do not overclaim direct vault state when using this method; distinguish direct file reads from evidence reconstructed through plugin artifacts.

### 4. Write the design note before scaffolding

Before creating `_wiki/` structure, write a design note in the source layer that explains:
- why this is compilation-first rather than retrieval-first
- what `Inbox/` is for
- what `_wiki/` is for
- what the core workflows are: ingest, query, lint
- what the human vs Hermes role split is

For this user, placing this note in `Inbox/hermes/default/` is correct.

### 5. Produce the companion workflow docs

After the main design note, create companion docs in the source/design layer:
1. **Page type templates**
2. **Ingest workflow checklist**
3. **Lint checklist**

These docs should define the future operating rules, not just explain the idea.

### 6. Only scaffold `_wiki/` after the method is documented

If the user approves, then create the minimum wiki structure, typically:

```text
_wiki/
  index.md
  log.md
  overview.md
  sources/
  concepts/
  entities/
  questions/
  syntheses/
  comparisons/
```

This is a **minimum scaffold**, not an exclusivity rule. Carrier-specific extensions are compatible when they preserve `_wiki/` as the compiled layer, for example:
- `hot.md` for short-lived hot-cache restoration
- `domains/` for top-level curated entry pages
- `meta/` for dashboards, lint reports, manifests, or maintenance artifacts
- optional `canvases/` or `folds/` when the local workflow explicitly uses them

Do not jump straight to heavy automation, embeddings, or vector search.

## Operational Rules This Methodology Implies

### Page-type gates
Use one page for one main object.

- `sources/`: compiled single-source pages; first landing point from `Inbox/`
- `concepts/`: stable recurring concepts, methods, frameworks
- `entities/`: people, companies, products, projects, protocols, orgs
- `questions/`: durable, reusable, likely-to-recur questions
- `syntheses/`: multi-source summaries, theses, stage views
- `comparisons/`: structured side-by-side comparisons

Do not create concept pages for one-off terms with no reuse value.
Prefer updating an existing page over creating a new one.

### Query posture
Use **wiki-first** behavior:
1. if `_wiki/hot.md` exists, read it first for short-lived recent context
2. then read `_wiki/index.md` to locate the most relevant pages
3. answer from relevant `_wiki/` pages first
4. revisit raw `Inbox/` material only when the wiki lacks evidence or detail
5. in this vault's current local workflow, durable query answers normally write back into `_wiki/questions/`; use `_wiki/syntheses/` only when the local schema explicitly treats it as a live compiled page type

### Write-back gate
A chat answer is worth writing back when it:
- resolves a recurring question
- combines multiple sources into a durable synthesis
- materially updates an existing concept/entity page
- would likely save future repeated work

Do not write back one-off or low-signal answers just to make the wiki larger.

### Ingest and lint routing
Once the methodology is approved:
- if installed, use `obsidian-inbox-to-wiki-ingest` for Inbox -> `_wiki/` compilation work
- if installed, use `obsidian-wiki-lint-triage` for `_wiki/` health review, prioritization, and repair planning
- if those execution skills are unavailable in the active environment, follow the vault's local operator contracts instead; this often means reading a vault-root `AGENTS.md` and honoring any project-local wiki ingest/lint workflow rules

### Execution surfaces consolidated here

This umbrella keeps the full class together instead of splitting methodology, ingest, and lint into narrow siblings.

#### Inbox -> `_wiki/` ingest
Use the same operating model whenever raw `Inbox/` notes should be promoted into compiled knowledge:
- always start with a traceable `_wiki/sources/` page
- in generic Hermes workflows, `source_path` is the primary dedup key
- in vaults that maintain `Inbox/.manifest.json` with source hashes and `address_map`, treat that manifest as the primary delta/dedup contract and keep `source_path` as page-level provenance metadata
- apply downstream updates selectively to `concepts/`, `entities/`, `questions/`, `syntheses/`, or `comparisons/`
- every ingest updates `_wiki/index.md` and `_wiki/log.md`
- source-only ingest is allowed when abstraction would be premature, but it must be explicit

#### `_wiki/` lint / triage
Use the same umbrella when reviewing compiled-knowledge health:
- default mode is audit-only unless the user explicitly requests repairs
- inspect navigation, duplicates, orphans, outdated pages, missing high-value pages, and backlog candidates in `Inbox/`
- treat split-root `_wiki/` + legacy `Wiki/` coexistence as a first-class structural finding
- prioritize fixes as P1/P2/P3 instead of dumping raw page lists

### Shared operator conventions

Keep these conventions explicit and aligned across the execution skills:
- all of `Inbox/` is valid source space, including `Inbox/hermes/default/`
- each compiled `_wiki/sources/` page records the source note's vault-relative `source_path`
- `_wiki/index.md` is a curated navigation page, not a full file dump
- treat `_wiki/log.md` as append-only in history semantics, but if the local workflow is newest-first then prepend new entries at the top using a stable parseable structure
- if the local workflow treats `_wiki/hot.md` as a cache file rather than a journal, overwrite it wholesale when refreshed

### Carrier compatibility with project-local Codex workflows

Some Obsidian vaults place workflow instructions and runtime hooks in hidden root folders such as `.agents/` and `.codex/`.
Treat these as **schema/workflow/runtime layer**, not as compiled knowledge pages.

When a vault-root `AGENTS.md` defines local mappings, follow it before applying upstream assumptions. For example, a carrier may map:
- `.raw/` -> `Inbox/`
- `wiki/` -> `_wiki/`

In that pattern:
- `.agents/` may contain project-local wiki skills and templates
- `.codex/` may contain session hooks that read `_wiki/hot.md`, auto-stage wiki changes, or prompt hot-cache refreshes
- these hidden folders are compatible with the LLM-wiki method as long as `_wiki/` remains the compiled knowledge target and `Inbox/` remains source space

### Language mode configuration

Preserve an explicit switchable language mode for the compiled layer.

Use these settings as the local operating policy:
- `compiled_output_language`: `zh-CN` or `en`
- `compiled_filename_language`: `zh-CN` or `en`
- `preserve_original_source_title`: `true`

Example host policy:
- `compiled_output_language: zh-CN`
- `compiled_filename_language: zh-CN`
- `preserve_original_source_title: true`

When `compiled_output_language` is `zh-CN`:
- `_wiki/` page prose defaults to Chinese
- headings and summaries default to Chinese
- important English terms may be preserved in parentheses for precision
- source pages may keep the original `source_title` in metadata, but the visible compiled page title and filename should be Chinese-facing by default

When `compiled_output_language` is `en`:
- `_wiki/` page prose, headings, summaries, and preferred display titles default to English
- Chinese explanatory prose should not be introduced unless the user explicitly requests bilingual output

Do not silently switch the compiled layer language. If the user asks to change the wiki language, update these settings first, then generate or rename pages accordingly.

### Legacy `Wiki/` coexistence rule

If the vault contains both `_wiki/` and `Wiki/`, treat that as an explicit migration/coexistence state, not as a trivial naming variation.

In that state:
- make the target compiled root explicit before major ingest or maintenance work
- do not assume `_wiki/` is already the only live compiled corpus
- inspect `Wiki/` when needed to avoid duplicate compilation or misleading health conclusions
- surface split-root state clearly in audits and weekly structural summaries

## Naming and Placement Conventions

For this user's current workflow:
- design/method docs belong in `Inbox/hermes/default/`
- source notes remain in `Inbox/`
- compiled knowledge belongs in `_wiki/`

Good filename patterns used successfully:
- `YYYY-MM-DD-karpathy-llm-wiki-落地设计方案.md`
- `YYYY-MM-DD-_wiki-page-type-轻量模板.md`
- `YYYY-MM-DD-ingest-工作流清单.md`
- `YYYY-MM-DD-lint-巡检清单.md`

## Pitfalls

- Do not write methodology/design notes directly into `_wiki/`; they belong in the source/design layer until promoted.
- Do not treat `_wiki/` as an archive dump of clipped sources.
- Do not skip reading the user's existing vault structure before writing notes.
- Do not start with complex search infrastructure; explicit structure and `index.md` come first.
- Do not confuse one-off chat answers with reusable wiki pages.
- Do not let execution details blur the boundary between methodology and operator skills.

## Verification

Before claiming success, confirm:
- the notes were written inside the intended Obsidian vault
- the files landed in the intended folder (`Inbox/hermes/default/` for this user's design docs)
- the design explicitly states `Inbox/` as the source space and `_wiki/` as the compiled layer
- the companion docs clearly cover templates, ingest, and lint
- the methodology states a clear human/Hermes split
- the query posture is wiki-first, not raw-first

## Expected Outcome

A successful run of this skill should leave the user with:
- one clear Karpathy-method design note
- one page-type template note
- one ingest checklist
- one lint checklist
- explicit routing to the execution skills for ingest and lint
- a ready-to-approve plan for scaffolding `_wiki/` next
