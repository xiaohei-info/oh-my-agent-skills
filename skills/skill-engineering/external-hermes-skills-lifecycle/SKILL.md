---
name: external-hermes-skills-lifecycle
description: Use when importing, installing, packaging, or publishing third-party Hermes skills so category placement, support files, discoverability, and open-source release surfaces stay correct.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, skills, installation, packaging, publishing, documentation]
    related_skills: [writing-skills, hermes-agent, verification-before-completion]
---

# External Hermes Skills Lifecycle

## Overview

Use this umbrella skill when the task is about the lifecycle of a skill outside Hermes core:
- adopting a third-party skill into `~/.hermes/skills`
- preserving linked support files and category layout
- making the installed skill discoverable and verifiable
- packaging a reusable skill or methodology repo for public release so other agents can adopt it correctly

A human maintainer would not keep separate micro-skills for "install" and "package" when they are two halves of the same lifecycle. This umbrella keeps both directions together:
- **inbound adoption** -> install into a local Hermes environment
- **outbound release** -> package a local skill/methodology repo for open-source reuse

## When to Use

Use when:
- a user wants a third-party skill from GitHub or another repo installed into Hermes
- a skill repo must be copied into `~/.hermes/skills` with correct category placement
- you need to verify that support files (`references/`, `templates/`, `scripts/`, `assets/`) came across intact
- a reusable skill/methodology repo is being prepared for public release
- README, AGENTS, runtime guidance, and deployment docs need clearer separation

Do not use when:
- the task is authoring one local skill from scratch with no import/release dimension
- the task is only a tiny wording tweak inside an already-installed local skill
- the repo is not intended to be reused outside the current workspace

## Lifecycle Split

### Inbound: adopt an external skill locally
Goal: install a third-party skill into `~/.hermes/skills` without modifying Hermes core.

### Outbound: package a reusable skill repo for others
Goal: ship a repo that another human or agent can adopt systematically without guessing structure, rollout order, or memory boundaries.

## Part A — Installing External Skills Into Hermes

### 1. Inspect the live local skill layout first

Before copying anything:
- inspect `~/.hermes/skills`
- determine category conventions
- confirm whether the destination should be `category/skill-name/`

Do not guess taxonomy from the upstream repo alone.

### 2. Fetch or update the upstream source

- clone or update the source repo in the requested workspace
- record the exact commit or revision used

### 3. Inspect the upstream skill directory before copying

Read:
- `SKILL.md`
- linked files under `references/`, `scripts/`, `templates/`, `assets/`

Decide install category from:
- live local taxonomy
- the skill's actual purpose

### 4. Install only the requested skill directory

- copy just the requested skill directory
- preserve upstream files exactly unless a minimal compatibility fix is required
- do not drag in unrelated siblings from the repo

### 5. Verify exact-copy integrity and discovery

Verification should include:
- destination path under `~/.hermes/skills`
- file existence and integrity
- `skills_list` visibility
- `skill_view(name)` load success
- support-file access when relevant

### 6. Separate discoverability from runtime readiness

A skill can be installed and discoverable even if optional scripts or dependencies are not yet usable.
Report missing runtime dependencies separately instead of calling the install a failure.

## Part B — Packaging Skills or Methodology Repos for Open Source

### 1. De-privateize first

Before publishing:
- remove machine-specific paths, usernames, vault names, and private defaults
- move environment-specific assumptions into documented config or integration docs
- make clear what the package is not if it could be mistaken for a plugin, product, or daemon

### 2. Separate package surfaces by role

Common surfaces include:
- README -> human-facing overview and adoption hook
- multi-language README entry links when more than one language is shipped
- optional agent loader docs such as `AGENTS.md`
- optional compressed runtime guidance such as `SOUL.md`
- memory-boundary guidance when relevant
- reusable assets under `skills/`, `templates/`, `scripts/`
- deployment or implementation docs that explain rollout order

Not every repo needs every surface, but every shipped surface must have a clear purpose.

When packaging a **unified public repository from an existing local skill library**:
- organize skills into a small number of class-level bundles rather than dumping a flat directory tree
- copy the **public package from the source skill directories**, not the other way around; keep the local/private originals untouched
- preserve support files with each skill (`references/`, `templates/`, `scripts/`, `assets/`)
- normalize private examples in the copied public version: machine paths, wrapper binaries, private vault names, host-specific policy wording
- add repo-level surfaces that explain the collection, not just the individual skills; a strong default is `README.md`, `AGENTS.md`, a bundle map, portability notes, and a source map

For a compact packaging checklist and recommended bundle/doc layout, see `references/public-skill-bundle-packaging.md`.

After the first public push succeeds, do a **public-repo polish pass** before calling the package truly handoff-ready:
- add community-health surfaces such as `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/*`, and `.github/pull_request_template.md`
- add governance surfaces such as `SECURITY.md` and `CODE_OF_CONDUCT.md` when the repo is meant for outside collaboration
- add a `CHANGELOG.md` and cut an explicit initial release tag instead of leaving the repo in an unversioned “just pushed” state
- add bundle-level `README.md` entrypoints when the repo groups many skills into thematic directories
- add a social-preview asset to the repo itself (for example `assets/social-preview.png`) plus a short doc explaining intended usage
- remember that GitHub's repository social preview card may still require a manual upload in repository settings even when the image asset is committed in-repo; do not assume the README image automatically becomes the repo card
- update repo metadata after structure stabilizes: description, topics, and release notes

### 3. Make README hybrid, not overloaded

README should:
- explain what the package is
- surface the distinctive value proposition early
- cite upstream conceptual lineage when relevant
- keep detailed rollout procedures in deeper docs
- optionally include a concise `For Agents` tail
- when multiple languages exist, put neutral language-switch links near the top of the README instead of special-casing one language as an afterthought

README should not:
- become one giant system prompt
- duplicate the full implementation guide
- hide the real package value behind only structure/install text

### 4. Separate package layers from rollout order

Implementation/deployment guidance should clearly distinguish:
- **what artifacts exist**
- **in what order to land them into a host system**

Also provide:
- capability-based landing guidance
- minimum / standard / full adoption profiles when helpful
- smoke tests or post-install verification

## Shared Pitfalls Across the Lifecycle

- guessing category placement instead of checking the live local taxonomy
- copying whole repos when the request is only for one skill
- losing support files because only `SKILL.md` was copied
- calling a discoverable install broken just because an optional script dependency is missing
- publishing a repo with local-only assumptions still embedded
- letting README, AGENTS, runtime docs, and deployment docs duplicate each other

## Verification Checklist

Before claiming success, confirm the relevant half of the lifecycle:

### For installs
- correct destination path under `~/.hermes/skills`
- requested skill copied without unrelated extras
- support files preserved
- skill discoverable via `skills_list`
- skill loadable via `skill_view`
- runtime caveats reported separately

### For packaging
- README is human-readable first and not overloaded
- deployment docs separate structure from rollout order
- reusable assets are actually portable
- local/private assumptions were removed or documented
- there is at least one concrete adoption/verification path

## Expected Outcome

A good run of this skill should leave the user with either:
- a correctly installed external skill that Hermes can discover and load
or
- a reusable skill/methodology repo that another agent can adopt without structural guesswork.
