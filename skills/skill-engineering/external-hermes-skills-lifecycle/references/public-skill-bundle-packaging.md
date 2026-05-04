# Public Skill Bundle Packaging

Use this note when turning a private/local skill library into one public repository.

## Goal

Publish a **curated bundle of reusable skills and methods**, not a raw filesystem dump.

## Recommended repo surfaces

At minimum:
- `README.md` — what the repo is, who it is for, what bundles exist
- multi-language README entry links near the top when more than one translation is shipped
- `AGENTS.md` — editing and packaging rules for agents/collaborators
- `skills/` — bundled public skill folders
- `docs/bundles.md` — what each bundle is for
- `docs/portability-notes.md` — what is runtime-specific vs portable
- `docs/source-map.md` — where each public skill came from
- `LICENSE`
- `.gitignore`

## Recommended packaging flow

1. Choose only the class-level skills worth publishing.
2. Group them into a few thematic bundles.
3. Copy each skill directory intact, including support files.
4. Scan the copied public package for:
   - machine paths
   - local wrapper binaries
   - private hostnames / vault names
   - wording tied to one user's environment
5. Patch only the public copy to generalize those assumptions.
6. Add repo-level docs so the collection is understandable as a project.
7. Verify the public repo tree and search for remaining private strings before push.
8. After the first successful push, run a public-polish pass:
   - add `CONTRIBUTING.md`
   - add `.github/ISSUE_TEMPLATE/*` and `pull_request_template.md`
   - add `SECURITY.md` and `CODE_OF_CONDUCT.md` if outside collaboration is expected
   - add `CHANGELOG.md`
   - create an initial version tag/release (for example `v0.1.0`)
   - add bundle-level `README.md` entrypoints when users will browse themed directories
   - if multiple languages exist, replace one-off phrasing like `For Chinese readers` with a neutral language-link block near the top of every README (for example `Languages: [English](README.md) | [简体中文](README.zh-CN.md)`)
   - add an in-repo social-preview asset plus a short note on how to use it
   - update GitHub metadata such as description and topics

## Good bundle examples

- engineering execution
- multi-agent control
- skill engineering
- chatops / ops
- research / reading
- knowledge compilation

## Anti-patterns

- publishing local skill folders unchanged when they still contain private machine paths
- copying only `SKILL.md` and losing `references/`, `templates/`, or `scripts/`
- shipping a huge flat list of narrow skills with no bundle explanation
- rewriting the local source skills when only the public copy needed normalization
- creating a repo that explains nothing above the individual skill level
