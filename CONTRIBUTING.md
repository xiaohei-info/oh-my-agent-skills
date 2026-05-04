# Contributing

Thanks for contributing to `oh-my-agent-skills`.

## What belongs here

This repository is for:
- reusable `SKILL.md` packages
- bundle-level method documentation
- support files that belong with a skill (`references/`, `templates/`, `scripts/`, `assets/`)
- packaging and portability guidance for public reuse

This repository is not for:
- private transcripts
- temporary task state
- machine-specific secrets
- environment wrappers that only work on one host, unless clearly labeled as examples

## Contribution standards

A good contribution should improve at least one of:
- reuse
- clarity
- discoverability
- verification quality
- portability
- real-world operator value

## Skill design rules

When adding or modifying a skill:
- optimize the description for **when to use it**
- keep one clear workflow per skill
- preserve linked support files with the skill
- avoid session-specific notes
- avoid private host assumptions
- state verification expectations clearly

## Public packaging rules

When changing the public repo surfaces:
- keep `README.md` hybrid: human-readable front, concise agent-facing tail
- keep bundle docs and source-map docs up to date
- do not let repo-level docs drift from the actual tree
- do not claim portability that is not true

## Verification before merge

Before claiming a contribution is ready:
- verify file structure matches the repo model
- check for leftover private strings or machine paths
- confirm support files are still present with the owning skill
- ensure changed docs still describe the actual current package

## Suggested contribution flow

1. Make the smallest useful change.
2. Keep edits scoped to the relevant bundle or doc surface.
3. Verify locally.
4. Update docs if the package shape changed.
5. Open a PR with a short explanation of the value added.
