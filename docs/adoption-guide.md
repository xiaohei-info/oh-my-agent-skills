# Adoption Guide

This repository can be adopted in several ways depending on your host runtime.

## Principle

Adopt the **smallest useful bundle set** that preserves the methodology you actually need.

Do not install every skill just because it exists.

## Adoption profiles

### 1. Reference-only
Use this when you mainly want ideas, not direct installation.

Read:
- `README.md`
- `docs/bundles.md`
- `docs/portability-notes.md`
- selected `SKILL.md` files

Best for:
- prompt engineers
- agent runtime designers
- workflow researchers

### 2. Partial Hermes bundle install
Use this when you already run Hermes and want a few targeted improvements.

Recommended starting bundles:
- `engineering-execution`
- `multi-agent-control`
- `skill-engineering`

Best for:
- existing Hermes operators
- people upgrading a local skill library selectively

### 3. Full Hermes bundle adoption
Use this when you want the repo to serve as a curated skill pack.

Install:
- all bundle directories you need
- each skill with its support files intact

Best for:
- a dedicated Hermes profile
- a team-maintained shared Hermes skill library

### 4. Cross-runtime adaptation
Use this when you are not on Hermes but want the methods.

Translate:
- child-agent orchestration
- file-edit tooling
- task-tracking primitives
- user clarification surfaces

Best for:
- custom agent runtimes
- OpenCode/Codex/Claude Code based systems
- orchestration frameworks that can emulate the workflow patterns

## Recommended starting points by need

### Need: stronger completion discipline
Start with:
- `engineering-execution/verification-before-completion`
- `engineering-execution/systematic-debugging`

### Need: better multi-agent delegation
Start with:
- `multi-agent-control/subagent-first`
- `multi-agent-control/subagent-collaboration-workflow`

### Need: better skill packaging
Start with:
- `skill-engineering/writing-skills`
- `skill-engineering/external-hermes-skills-lifecycle`
- `skill-engineering/skill-optimizer`

### Need: chat-native recurring automation
Start with:
- `chatops-and-ops/user-friendly-cron-messages`
- `chatops-and-ops/ops-sentry`

### Need: research and knowledge workflows
Start with:
- `research-and-reading/web-reading-router`
- `research-and-reading/hv-analysis`
- `knowledge-compilation/*`

## Installation notes for Hermes

When installing into Hermes:
- copy the entire skill directory
- do not copy only `SKILL.md`
- preserve any `references/`, `templates/`, `scripts/`, and `assets/`
- place the skill under the category layout your Hermes environment expects

## Verification checklist

After adopting a bundle, ask:
- does the host actually know when to load it?
- are the support files still reachable?
- did we preserve the intended workflow boundaries?
- are local/private assumptions removed or reintroduced?
- did this reduce ambiguity or just add more text?
