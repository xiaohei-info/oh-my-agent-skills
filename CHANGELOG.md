# Changelog

All notable changes to this repository will be documented in this file.

The format is inspired by Keep a Changelog.

## [0.1.2] - 2026-05-04

### Changed
- Updated the public `external-hermes-skills-lifecycle` skill to codify the multilingual README pattern: use neutral language-switch links near the top of every README instead of one-off phrasing like `For Chinese readers`
- Synced the linked packaging reference file into the public repo copy of that skill so the support-file contract matches the source skill

## [0.1.0] - 2026-05-03

### Added
- Initial public packaging of the `oh-my-agent-skills` repository
- Curated bundle structure across engineering execution, multi-agent control, skill engineering, ChatOps/Ops, research/reading, and knowledge compilation
- Repo-level surfaces: `README.md`, `README.zh-CN.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/bundles.md`, `docs/adoption-guide.md`, `docs/portability-notes.md`, `docs/source-map.md`
- Bundle-level `README.md` entrypoints under each `skills/<bundle>/` directory
- Community health files under `.github/` for issues and pull requests

### Changed
- Public copies of selected skills were normalized to remove host-specific wrapper paths and private environment wording while preserving the underlying methods

### Notes
- This release is intentionally methodology-first: the repository is useful both as a Hermes-compatible skill bundle and as a portable agent-workflow reference library
