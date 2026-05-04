# oh-my-agent-skills

A curated open-source bundle of **agent methodologies** and **Hermes-compatible skills** for building stronger AI workflows.

This repository is not a monolithic framework. It is a **packaged library of reusable operating methods**:
- engineering execution discipline
- multi-agent controller workflows
- skill authoring and optimization
- chat-friendly cron / alert design
- web-reading and deep-research patterns
- compiled knowledge workflows for Obsidian-style vaults

Some assets are directly usable as Hermes `SKILL.md` packages. Others are useful even outside Hermes because the underlying method is portable.

## What is in this repo

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
  bundles.md
  portability-notes.md
  source-map.md
```

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

See `docs/source-map.md` for the current bundle map.

### Option B — Adapt the methods to another agent stack
Even when a skill references Hermes tools, the underlying method is often portable:
- `delegate_task` -> your child-agent or worker abstraction
- `read_file/search_files/patch/write_file` -> your codebase tooling
- `clarify` -> your user-interaction layer
- `todo` -> your task planner / state tracker

## Portability notes

This public repo intentionally keeps many **Hermes-native** concepts because they are part of the original execution model. However, local machine paths and private host assumptions were stripped or generalized before release.

See:
- `docs/portability-notes.md`
- `AGENTS.md`

## Design philosophy

The repo is opinionated about a few things:
- evidence before claims
- root cause before fixes
- explicit delegation contracts
- reusable methods over one-off transcripts
- compact, discoverable skill packaging
- human-readable automation output

## Contributing

Contributions are welcome when they improve:
- clarity
- portability
- verification quality
- discoverability
- real-world reuse

If you add a new skill, keep it grounded in a workflow that actually worked.

## License

MIT
