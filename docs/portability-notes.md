# Portability Notes

This repository contains a mix of:
1. **Hermes-native skills**
2. **portable methods expressed in Hermes terms**

## What was normalized for public release

Before publishing this repo, the copied public versions were adjusted to remove or generalize:
- host-specific ACP wrapper paths such as local `/home/...` binaries
- private vault naming assumptions tied to one user
- wording that implied one specific machine or one private host policy

## What remains Hermes-native on purpose

Many skills still reference Hermes concepts such as:
- `delegate_task`
- `search_files`
- `read_file`
- `patch`
- `write_file`
- `todo`
- `clarify`

Those references are intentional because they document the original runtime contract.

## How to adapt these skills to another stack

### Child agents
- Hermes `delegate_task` -> your child-worker / subagent orchestration primitive

### File operations
- Hermes `read_file/search_files/patch/write_file` -> your repo inspection / edit tooling

### User interaction
- Hermes `clarify` -> your chat approval / UI decision prompt

### Task tracking
- Hermes `todo` -> your planner / work-item state system

## What is portable even if the syntax changes

These ideas survive tool translation:
- evidence before completion claims
- root cause before fix
- explicit delegation contracts
- wave-based parallel planning
- support-file aware skill packaging
- compiled-knowledge maintenance as a first-class workflow
- chat-friendly routine vs exception output design

## Suggested adoption strategy

### If you already use Hermes
Use the skill folders directly.

### If you use another agent runtime
Start by porting the bundle principles, not every line literally.

Recommended order:
1. engineering execution
2. multi-agent control
3. skill engineering
4. chatops / ops
5. knowledge compilation or research bundles as needed
