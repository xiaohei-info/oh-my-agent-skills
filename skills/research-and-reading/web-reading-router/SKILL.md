---
name: web-reading-router
description: >
  Route URL reading requests across Hermes tools and platform-specific skills.
  Use when a user shares a URL or asks to read, summarize, extract, inspect,
  or diagnose content from a webpage, article, post, document link, or similar
  web resource, especially when a simple fetch may fail or the best tool path is
  unclear.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [web, routing, browser, extraction, reading]
---

# Web Reading Router

Use this skill to decide how to read a URL before trying tools at random.

## When to Use

Use this skill when:
- the user shares a URL and wants content read or summarized
- the page might need JavaScript rendering
- a lightweight fetch returned partial content
- the URL might belong to a platform that deserves a specialized workflow
- the content may actually be a file resource rather than a normal webpage

Do not load this skill for ordinary search-only tasks where no URL needs to be read.
Exception: if lightweight search/extract tooling is failing upstream but you can identify likely target URLs, use this skill to route a manual browser-based verification pass on those targets.

## Core Rule

Prefer the narrowest reliable path:
1. platform-specific skill or workflow
2. lightweight generic extraction
3. lightweight external reader fallback
4. browser rendering and interaction
5. user assist after diagnosing the blocker

Do not jump to the heaviest option first unless the URL clearly requires it.

## Fast Checklist

Before picking a tool path, classify the URL:
1. Is it a known platform domain?
2. Is it file-like (`.pdf`, image, JSON, XML, RSS)?
3. Is the task one-off reading or repeated extraction?
4. Did a lighter path already fail, and how?

If the helper script exists, run:

```bash
python3 SKILL_DIR/scripts/route_url.py "URL"
```

Use the result as a starting point, not as an absolute rule.

## Baseline Routes

### 1. Platform URLs

Prefer dedicated workflows when possible:
- `mp.weixin.qq.com` → load `wechat-reader`
- `github.com` → use Hermes GitHub skill or `gh` for repo-native reads
  - For repository evaluation tasks, do not stop at the repo landing page or README if the user is asking about doctrine, architecture, overlap, adoption value, or whether the repo is actually useful. Identify and read the canonical files that define the repo's real model before making substantive judgments. Typical paths include `docs/`, `AGENTS.md`, `SOUL.md`, `MEMORY.md`, implementation/integration guides, and the specific `skills/` or template files that operationalize the model.
  - If you only read the README, explicitly label the result as a first-pass impression. Do not present overlap/adoption conclusions as if the full repository charter or operating model has already been reviewed.
- `raw.githubusercontent.com` → if the page snapshot is empty or unhelpful, read the raw body with browser DOM inspection (`document.body.innerText`) instead of assuming the file is unreadable
- `x.com`, `twitter.com` → first try lightweight extraction if available, but expect it to fail or return partial content; if so, use browser rendering because the logged-out post page often exposes the post text directly in the accessibility tree. If media matters, recover rendered image URLs via DOM inspection (`document.querySelectorAll('img')`) and analyze the attachment separately.
- `youtube.com`, `youtu.be`, `bilibili.com` → prefer transcript / metadata paths or Agent Reach
- `reddit.com` → prefer Agent Reach or Reddit-native reading

### 1a. Agent Reach as a platform bridge

If Agent Reach is installed and healthy, use it as a specialized backend for supported channels rather than treating it as a separate top-level micro-skill.

Best fit:
- Reddit, V2EX, GitHub, RSS, WeChat-article search/read, YouTube, Bilibili, and related supported channels
- cases where Hermes native `web_extract` is weak or partial but a platform-aware bridge may succeed
- workflows where `agent-reach doctor` can quickly tell you whether the channel is currently available

Rules:
- resolve the real Agent Reach binary first instead of assuming it is on `PATH`
- run a fresh `doctor` before trusting a channel
- still prefer the narrowest path: if the URL is a direct `mp.weixin.qq.com` article and browser rendering is clearly required, go straight to the WeChat/browser workflow rather than forcing Agent Reach first

### 2. File-like URLs

Switch early when the URL is obviously a file:
- PDF → `web_extract` usually works well
- image → use `vision_analyze`
- JSON / XML / RSS → use `web_extract` or terminal fetch, then inspect structured content

### 3. Generic Public Pages

Start with `web_extract`.
Escalate only if the result is clearly incomplete, heavily templated, empty, or JS-walled.

## Search / Extraction Outage Fallback

If `web_search` or `web_extract` fails with an upstream/provider error on a public-web research task, do not stop at the error if the target sites are already known.

Use this fallback sequence:
1. identify the 3-5 highest-value target URLs or boards
2. open them with `browser_navigate`
3. verify live activity signals such as recent timestamps, visible listings, result counts, salary/rate snippets, or open application flows
4. clearly distinguish browser-verified findings from unverified assumptions
5. if one target is blocked, continue verifying the next best targets instead of abandoning the whole research pass

This is especially useful for marketplace/board reconnaissance where lightweight search fails but direct site access still works.

## Escalation Ladder

### Step A — `web_extract`

Use first for public articles, docs, help pages, and other normal webpages.
Escalate when the result is title-only, empty, clearly truncated, or missing the body.

### Step B — Lightweight external reader fallback

If a public page still looks readable but `web_extract` is incomplete, try a lightweight external path such as:

```bash
curl -s "https://r.jina.ai/https://example.com/article"
```

Use this only for public pages. Do not expect it to bypass strong anti-bot or login walls.

### Step C — Browser rendering

Use browser tools when the page likely needs JavaScript rendering, scrolling, clicking, or inspection of the rendered state.
If the browser hits CAPTCHA, slider verification, login walls, or permission gates, report the exact blocker instead of pretending the content was read.

### Step D — User assist

Ask for help only after diagnosing the blocker. Typical asks:
- paste the relevant text
- send screenshots
- share a mirror link
- provide login state or cookies if the user wants that path used

## Output Pattern

When readable, prefer:
- Type: page/resource type
- Path: route used
- Summary: answer first
- Confidence: full / partial / low
- Notes: any missing pieces or blind spots

When blocked, prefer:
- Type: page/resource type
- Path tried: route used
- Blocker: exact reason
- Next step: best fallback or minimum user assist needed

## Pitfalls

- Do not hallucinate content when extraction failed.
- Do not use browser first for every normal public article.
- Do not treat metadata-only extraction as a full read.
- Do not ignore platform-native paths for GitHub, WeChat, YouTube, Bilibili, or Reddit.

## References

- `references/platform-routing.md`
- `references/failure-diagnosis.md`

## Verification

Before replying, confirm:
- the selected path matched the URL type
- any extracted body is non-empty
- any blocker is stated precisely
- the answer distinguishes full read vs partial recovery
