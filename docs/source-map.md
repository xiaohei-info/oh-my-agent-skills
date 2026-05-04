# Source Map

This document maps the current public repository layout to the source skill families used during packaging.

## Public bundle -> original source family

### `skills/engineering-execution/`
- `verification-before-completion` <- `software-development/verification-before-completion`
- `systematic-debugging` <- `software-development/systematic-debugging`

### `skills/multi-agent-control/`
- `subagent-first` <- `autonomous-ai-agents/subagent-first`
- `subagent-collaboration-workflow` <- `software-development/subagent-collaboration-workflow`

### `skills/skill-engineering/`
- `skill-optimizer` <- `meta/skill-optimizer`
- `writing-skills` <- `software-development/writing-skills`
- `external-hermes-skills-lifecycle` <- `software-development/external-hermes-skills-lifecycle`

### `skills/chatops-and-ops/`
- `user-friendly-cron-messages` <- `devops/user-friendly-cron-messages`
- `ops-sentry` <- `devops/ops-sentry`

### `skills/research-and-reading/`
- `web-reading-router` <- `research/web-reading-router`
- `hv-analysis` <- `research/hv-analysis`

### `skills/knowledge-compilation/`
- `karpathy-llm-wiki-obsidian` <- `note-taking/karpathy-llm-wiki-obsidian`
- `obsidian-inbox-to-wiki-ingest` <- `note-taking/obsidian-inbox-to-wiki-ingest`
- `obsidian-wiki-lint-triage` <- `note-taking/obsidian-wiki-lint-triage`

## Support-file policy

When reusing a skill from this repository, copy the entire skill directory, not only `SKILL.md`.

That means carrying along any of:
- `references/`
- `templates/`
- `scripts/`
- `assets/`

present inside the skill folder.
