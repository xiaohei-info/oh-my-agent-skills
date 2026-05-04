# Bundle Map

## engineering-execution
Execution discipline for coding and debugging.

Included skills:
- `verification-before-completion`
- `systematic-debugging`

Core ideas:
- no success claims without fresh evidence
- no fixes without root-cause investigation first

## multi-agent-control
Controller-side patterns for subagent delegation and workflow integration.

Included skills:
- `subagent-first`
- `subagent-collaboration-workflow`

Core ideas:
- controller retains judgment
- child prompts must be bounded
- verification is independent from implementation
- same-file concurrent edits are usually a smell

## skill-engineering
Methods for authoring, improving, and publishing skills as reusable assets.

Included skills:
- `skill-optimizer`
- `writing-skills`
- `external-hermes-skills-lifecycle`

Core ideas:
- optimize for discovery first
- package support files correctly
- use keep/revert loops for skill improvement

## chatops-and-ops
Human-facing cron UX and low-noise operational alerting.

Included skills:
- `user-friendly-cron-messages`
- `ops-sentry`

Core ideas:
- optimize messages for the next 5 seconds of human attention
- suppress duplicate and stale alerts
- distinguish routine output from exception-mode output

## research-and-reading
Research routing and deep-analysis frameworks.

Included skills:
- `web-reading-router`
- `hv-analysis`

Core ideas:
- pick the lightest reliable reading path before escalating to a browser
- combine longitudinal and cross-sectional analysis for deeper judgment

## knowledge-compilation
Compiled-knowledge workflows for Obsidian-style vaults.

Included skills:
- `karpathy-llm-wiki-obsidian`
- `obsidian-inbox-to-wiki-ingest`
- `obsidian-wiki-lint-triage`

Core ideas:
- separate source space from compiled knowledge
- prefer traceable source-grounded updates
- lint for knowledge health, not cosmetic neatness
