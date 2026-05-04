# oh-my-agent-skills

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/xiaohei-info/oh-my-agent-skills?display_name=tag)](https://github.com/xiaohei-info/oh-my-agent-skills/releases)
[![License](https://img.shields.io/github/license/xiaohei-info/oh-my-agent-skills)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/xiaohei-info/oh-my-agent-skills)](https://github.com/xiaohei-info/oh-my-agent-skills/commits/main)

A curated open-source bundle of **agent methodologies** and **Hermes-compatible skills** for building stronger AI workflows.

This repository is not a monolithic framework and not a raw export of one local skill directory. It is a **curated public package of reusable operating methods** for people building agent runtimes, skill libraries, research workflows, chat-native automations, and compiled-knowledge systems.

![oh-my-agent-skills social preview](assets/social-preview.png)

## Why this repo exists

Most agent stacks do not fail because they cannot call a model or run tools. They fail because they lack:
- a stable definition of completion
- a disciplined debugging method
- bounded delegation contracts for child agents
- a way to turn repeated workflows into reusable assets
- human-readable automation outputs instead of internal dumps
- a maintainable structure for knowledge compilation

This repository packages methods that address those gaps.

## Signature operating ideas

What makes this repo distinctive is not just the file tree. It is the operating model behind the skills.

- **Skills are operational assets, not prompt scraps** — a good skill is reusable procedural memory with trigger conditions, execution steps, pitfalls, and verification expectations.
- **Execution quality comes from discipline, not just capability** — strong model/tool access is not enough; you need explicit completion standards, debugging discipline, and verification gates.
- **Multi-agent systems need controllers, not just more agents** — delegation only compounds value when task shape, scope boundaries, and verification roles are explicit.
- **Automation output should be optimized for human consumption** — recurring cron jobs, alerts, and checks should default to short, actionable, chat-readable output.
- **Knowledge bases should be compiled, not merely accumulated** — raw source space and compiled durable knowledge should be separated, with ingest and lint as first-class workflows.
- **Public packaging matters** — a useful local skill library becomes far more valuable when it is structured, de-privatized, and published as a reusable bundle.

## Operating model in one page

### Existential purpose
Package a small set of agent methods that materially improve how agent systems execute, delegate, verify, package skills, and maintain knowledge.

### Economic model
The repo creates value when a team can reuse one of these skills or methods instead of re-deriving the workflow from scratch each time.

### North star
**Verified leverage per unit of spend** — more real output, less rework, less ambiguity, less coordination waste.

### Compounding mechanism
Every good workflow can become a reusable asset:
- a skill
- a support reference
- a template
- a repeatable controller pattern
- a packaging doctrine others can adopt

### Completion standard
A method in this repo is only “good” if it is:
- understandable by another human or agent
- structured for reuse
- explicit about when to use it
- explicit about how to verify outcomes

### Drift-correction frame
The collection stays healthy by:
- bundling skills by class, not as a flat dump
- preserving support files with each skill
- normalizing private/local assumptions in the public copy
- documenting portability limits instead of pretending universal compatibility

### Strongest worldview shift
Treat the agent workflow itself as a product surface worth designing, packaging, reviewing, and publishing.

## Quickstart

If you only have this repo link and want a correct first pass:

1. Read this `README.md` for the high-level model.
2. Read [`docs/adoption-guide.md`](docs/adoption-guide.md) to choose an adoption path.
3. Read [`docs/bundles.md`](docs/bundles.md) to understand the thematic bundles.
4. Read [`docs/portability-notes.md`](docs/portability-notes.md) before copying anything into another runtime.
5. Install or adapt only the bundles you can actually support.

## Distinctive capabilities

This repo is especially useful if you need one or more of these capabilities:

- **evidence-first completion** — `verification-before-completion`
- **root-cause debugging discipline** — `systematic-debugging`
- **controller-style subagent orchestration** — `subagent-first`, `subagent-collaboration-workflow`
- **skill packaging and optimization** — `skill-optimizer`, `writing-skills`, `external-hermes-skills-lifecycle`
- **chat-native cron and alert design** — `user-friendly-cron-messages`, `ops-sentry`
- **web-reading tool routing and deep research** — `web-reading-router`, `hv-analysis`
- **compiled knowledge maintenance for Obsidian-style vaults** — `karpathy-llm-wiki-obsidian`, `obsidian-inbox-to-wiki-ingest`, `obsidian-wiki-lint-triage`

## Repository layout

```text
skills/
  engineering-execution/
  multi-agent-control/
  skill-engineering/
  chatops-and-ops/
  research-and-reading/
  knowledge-compilation/

docs/
  adoption-guide.md
  bundles.md
  portability-notes.md
  social-preview.md
  source-map.md
```

assets/
  social-preview.png
```

## Bundles

### 1. Engineering execution
Skills that enforce evidence-driven execution rather than guesswork.
- `verification-before-completion`
- `systematic-debugging`

### 2. Multi-agent control
Controller-side workflows for delegation, bounded subagent handoffs, verification, and wave parallelism.
- `subagent-first`
- `subagent-collaboration-workflow`

### 3. Skill engineering
Methods for authoring, packaging, improving, and publishing reusable agent skills.
- `skill-optimizer`
- `writing-skills`
- `external-hermes-skills-lifecycle`

### 4. ChatOps and Ops
Human-readable recurring alerts, cron outputs, and low-noise monitoring methods.
- `user-friendly-cron-messages`
- `ops-sentry`

### 5. Research and reading
Structured URL reading, deep research, and report-generation workflows.
- `web-reading-router`
- `hv-analysis`

### 6. Knowledge compilation
Inbox-to-wiki and lint/triage methods for maintaining compiled knowledge layers.
- `karpathy-llm-wiki-obsidian`
- `obsidian-inbox-to-wiki-ingest`
- `obsidian-wiki-lint-triage`

## Who this is for

This repo is useful if you are:
- building an AI agent runtime
- curating a reusable skill library
- trying to make multi-agent workflows less sloppy
- packaging prompt/method assets for public reuse
- designing chat-native cron or alerting systems
- maintaining an Obsidian-style compiled knowledge base

## How to use it

### Option A — Use as a Hermes skill bundle
Copy one or more skill directories into your Hermes skills directory, preserving each skill's support files (`references/`, `scripts/`, `templates/`, `assets/`).

Typical install target:
- `~/.hermes/skills/<category>/<skill-name>/`

See [`docs/source-map.md`](docs/source-map.md) for the current bundle map.

### Option B — Adapt the methods to another agent stack
Even when a skill references Hermes tools, the underlying method is often portable:
- `delegate_task` -> your child-agent or worker abstraction
- `read_file/search_files/patch/write_file` -> your codebase tooling
- `clarify` -> your user-interaction layer
- `todo` -> your task planner / state tracker

### Option C — Read it as an agent-methods library
You do not have to install anything immediately. Many users will get value first by reading:
- bundle overviews
- portability notes
- the individual `SKILL.md` files as design references

## What good adoption looks like

A good adoption of this repo should make your system:
- more verification-driven
- less sloppy in delegation
- better at skill packaging and reuse
- more readable in human-facing automation outputs
- more explicit about source-space vs compiled-knowledge boundaries

If adoption mainly adds ceremony, duplicates stronger local workflows, or turns into a giant prompt dump, it has gone wrong.

## Related docs

- [`AGENTS.md`](AGENTS.md) — repository working rules for agent collaborators
- [`docs/adoption-guide.md`](docs/adoption-guide.md) — how to adopt the bundles
- [`docs/bundles.md`](docs/bundles.md) — bundle-by-bundle overview
- [`docs/portability-notes.md`](docs/portability-notes.md) — what is Hermes-native vs portable
- [`docs/social-preview.md`](docs/social-preview.md) — social preview asset notes
- [`docs/source-map.md`](docs/source-map.md) — source-to-public bundle mapping
- [`SECURITY.md`](SECURITY.md) — how to report security-sensitive issues
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — participation expectations

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## For Agents

If you are an adopting agent:
1. read `README.md`
2. read `docs/adoption-guide.md`
3. read `docs/portability-notes.md`
4. then install or emulate only the smallest useful bundle set

Do not blindly copy every surface just because it exists.

## License

MIT
