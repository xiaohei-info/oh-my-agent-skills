# Security Policy

## Scope

This repository contains:
- reusable skills
- public support files
- packaging and methodology documentation

It does **not** ship production services or hosted infrastructure by itself. Most security concerns here are therefore about:
- unsafe workflow guidance
- accidental inclusion of private machine assumptions or secrets
- misleading portability claims that could cause unsafe adoption

## Reporting a vulnerability

If you believe this repository contains a security-sensitive issue, please **do not** open a public issue first.

Instead, report it privately to the repository owner through GitHub security reporting or a private contact path if one is available.

A good report should include:
- the affected file(s)
- why the issue matters
- what an adopter could do wrong because of it
- any proof of concept or concrete reproduction path
- whether the issue is documentation-only or affects an executable support file

## Examples of issues worth reporting

- a support script that encourages unsafe defaults
- accidental inclusion of secrets, tokens, or private internal paths
- instructions that could cause destructive behavior without warning
- misleading claims that a skill is portable when it actually depends on hidden assumptions
- a public asset that contains private or sensitive data

## What to expect

The maintainer should aim to:
1. acknowledge the report
2. assess scope and severity
3. patch or document the issue
4. publish a fix note when appropriate

## Safe reuse guidance

If you adopt content from this repository:
- verify local paths before running scripts
- review support scripts before execution
- do not assume a workflow is safe in your environment just because it is public here
- prefer the smallest useful adoption surface first
