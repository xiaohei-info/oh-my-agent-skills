# Adoption Guide

This repository is designed for **modular adoption**.

You can use it in three progressively heavier ways:
- install **one skill** to fix one failure mode
- install **one bundle** to improve one class of workflows
- adopt a **larger pack** if you want a broader Hermes-compatible skill library

If you are not on Hermes, you can still adapt the methods without copying the runtime-specific syntax verbatim.

## Core principle

Adopt the **smallest useful unit** that preserves the method you actually need.

Do not install every skill just because it exists.

## Step 1: choose the problem you want to fix

### Need: stronger completion discipline
Start with:
- `engineering-execution/verification-before-completion`
- `engineering-execution/systematic-debugging`

### Need: better multi-agent delegation
Start with:
- `multi-agent-control/subagent-first`
- `multi-agent-control/subagent-collaboration-workflow`

### Need: better skill authoring or packaging
Start with:
- `skill-engineering/writing-skills`
- `skill-engineering/external-hermes-skills-lifecycle`
- `skill-engineering/skill-optimizer`

### Need: chat-native recurring automation
Start with:
- `chatops-and-ops/user-friendly-cron-messages`
- `chatops-and-ops/ops-sentry`

### Need: research or compiled-knowledge workflows
Start with:
- `research-and-reading/web-reading-router`
- `research-and-reading/hv-analysis`
- `knowledge-compilation/*`

## Step 2: pick an adoption profile

### 1. Reference-only
Use this when you mainly want ideas, patterns, or review criteria.

Read:
- `README.md`
- `docs/bundles.md`
- `docs/portability-notes.md`
- selected `SKILL.md` files

Best for:
- prompt engineers
- agent runtime designers
- workflow researchers

### 2. One-skill install
Use this when one failure mode matters more than everything else.

Example: install `verification-before-completion` only.

```bash
git clone https://github.com/xiaohei-info/oh-my-agent-skills.git
cd oh-my-agent-skills
mkdir -p ~/.hermes/skills/software-development
cp -R skills/engineering-execution/verification-before-completion \
  ~/.hermes/skills/software-development/
```

Best for:
- quick behavior upgrades
- highly targeted Hermes improvements
- teams testing the repo with minimal risk

### 3. One-bundle install
Use this when you want a coherent set of related skills.

Example: install the full `engineering-execution` bundle.

```bash
mkdir -p ~/.hermes/skills/software-development
cp -R skills/engineering-execution/verification-before-completion \
  ~/.hermes/skills/software-development/
cp -R skills/engineering-execution/systematic-debugging \
  ~/.hermes/skills/software-development/
```

Best for:
- one class of workflow problems
- a team rollout with shared standards
- stronger consistency than one-off skill adoption

### 4. Larger Hermes bundle adoption
Use this when you want the repo to serve as a curated skill pack.

Install:
- the bundles you actually need
- each skill with its support files intact
- each skill into the original Hermes category shown in [`docs/source-map.md`](source-map.md)

Best for:
- a dedicated Hermes profile
- a team-maintained shared Hermes skill library
- environments that already rely on Hermes-native workflows

### 5. Cross-runtime adaptation
Use this when you are not on Hermes but want the methods.

Translate:
- child-agent orchestration
- file-edit tooling
- task-tracking primitives
- user clarification surfaces
- install/verification expectations

Best for:
- custom agent runtimes
- OpenCode / Codex / Claude Code based systems
- orchestration frameworks that can emulate the workflow patterns

## Step 3: install correctly

### Preserve the whole skill directory

When installing into Hermes:
- copy the entire skill directory
- do not copy only `SKILL.md`
- preserve any `references/`, `templates/`, `scripts/`, and `assets/`

### Use the source map for install destinations

Public bundle folders are organized for discoverability.

Hermes install targets should follow the skill's original category, for example:
- `skills/engineering-execution/verification-before-completion`
  -> `~/.hermes/skills/software-development/verification-before-completion`
- `skills/chatops-and-ops/user-friendly-cron-messages`
  -> `~/.hermes/skills/devops/user-friendly-cron-messages`
- `skills/research-and-reading/web-reading-router`
  -> `~/.hermes/skills/research/web-reading-router`

For mixed-category bundles, use [`docs/source-map.md`](source-map.md).

## Step 4: use the skill on purpose

Installing a skill is only the first step. After install, explicitly invoke it in the task prompt.

Examples:
- “Use `verification-before-completion` before telling me this task is done.”
- “Use `systematic-debugging` to investigate this failure before you change code.”
- “Use `subagent-first` to plan and delegate this feature.”
- “Use `user-friendly-cron-messages` to rewrite this cron output for a Telegram user.”

## Verification checklist for Hermes installs

After adopting a skill or bundle, check:
- is the folder in the correct `~/.hermes/skills/<category>/<skill-name>/` path?
- were the support files preserved?
- does your Hermes environment discover the skill?
- does the skill still make sense in your runtime, or does it need portability adaptation?
- did this reduce ambiguity or just add more text?

## Common mistakes

Avoid these:
- installing the whole repo when you only need one behavior change
- copying only `SKILL.md` and dropping support files
- treating public bundle names as the Hermes destination categories
- copying methods into a non-Hermes runtime without translating the tool layer
- adopting too many skills at once and losing the ability to tell which one helped

## Recommended rollout order

A good default sequence is:
1. install one skill
2. use it in real work
3. verify the behavior change
4. add a second skill or bundle only when the first one proves useful

This repository compounds best when you grow it deliberately rather than dumping the whole tree into a runtime all at once.
