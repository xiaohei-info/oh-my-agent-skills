# Platform Routing

Use this reference when the domain itself suggests the best reading path.

## Domain-first routing

| Domain / pattern | Preferred route | Why |
|---|---|---|
| `mp.weixin.qq.com` | `wechat-reader` | WeChat articles are often JS-rendered and anti-bot protected |
| `github.com` | GitHub-native path | Repos, issues, and PRs are usually better via `gh` or Hermes GitHub skills |
| `youtube.com`, `youtu.be` | transcript / metadata path | Video pages are better read via transcript and metadata workflows |
| `bilibili.com` | transcript / metadata path | Video-native workflow is usually better than page scraping |
| `reddit.com` | Agent Reach / Reddit-native read | Post body and comments are easier via dedicated readers |
| file-like URL (`.pdf`, image, `.json`, `.xml`, `.rss`) | file-specific path | Avoid treating a file like a normal article |

## Generic rules

- Prefer platform-native reading over raw HTML scraping.
- Prefer `web_extract` for ordinary public articles and documentation.
- Prefer browser tools only when rendering or interaction is truly needed.
- If a page is public but extraction is weak, try a lightweight external reader before escalating to browser.

## File-like routing

- PDF: `web_extract`
- Images: `vision_analyze`
- JSON/XML/RSS: fetch then inspect structured content
- Subtitle / transcript files: fetch and read as text rather than rendering in browser
