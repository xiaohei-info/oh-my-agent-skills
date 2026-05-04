# AGENTS.md

## Purpose

This repository is a library of reusable agent methods and Hermes-compatible skills.

Use it as:
- a source of `SKILL.md` packages
- a reference library for agent workflow design
- a portability guide for adapting Hermes-style patterns to other runtimes

## Read order

When working in this repository:
1. `README.md` — human-facing overview
2. `docs/bundles.md` — what each bundle is for
3. `docs/portability-notes.md` — what is Hermes-native vs portable
4. target `skills/<bundle>/<skill-name>/SKILL.md`

## Editing rules

When modifying this repo:
- preserve each skill as a self-contained unit
- keep linked support files beside the skill
- do not hardcode private machine paths
- do not add host-specific wrappers to reusable skills unless clearly labeled as examples
- keep descriptions optimized for discovery: *when to use the skill* matters more than internal narration
- prefer surgical edits over style churn

## Publishing rules

Before release:
- verify that copied support files are present
- remove or generalize environment-specific assumptions
- ensure README and docs explain repo structure clearly
- do not claim a method is fully generic if it still depends on Hermes-native primitives

## Installation model

The primary packaging model is directory-based skill reuse:
- one skill = one folder
- `SKILL.md` is the entrypoint
- `references/`, `templates/`, `scripts/`, and `assets/` are copied with it when present

## Scope boundary

This repo is for:
- skill files
- methodology docs
- reusable support references/templates/scripts

This repo is not for:
- private chat logs
- transient task state
- machine-specific deployment secrets
- host-only wrapper scripts unless intentionally published as examples
