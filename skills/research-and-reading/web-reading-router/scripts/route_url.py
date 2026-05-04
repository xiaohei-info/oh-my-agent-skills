#!/usr/bin/env python3
import argparse
import json
from urllib.parse import urlparse

PLATFORM_RULES = [
    ("mp.weixin.qq.com", "wechat-reader", "Use the dedicated WeChat article workflow", "native-first", "high"),
    ("github.com", "github-native", "Prefer GitHub-native repo/issue/PR reading", "native-first", "medium"),
    ("youtube.com", "video-native", "Prefer transcript and metadata workflows", "native-first", "medium"),
    ("youtu.be", "video-native", "Prefer transcript and metadata workflows", "native-first", "medium"),
    ("bilibili.com", "video-native", "Prefer transcript and metadata workflows", "native-first", "medium"),
    ("reddit.com", "reddit-native", "Prefer dedicated Reddit reading", "native-first", "medium"),
]

FILE_SUFFIX_RULES = [
    (".pdf", "pdf", "Treat as PDF", "resource-native", "low"),
    (".jpg", "image", "Treat as image", "resource-native", "low"),
    (".jpeg", "image", "Treat as image", "resource-native", "low"),
    (".png", "image", "Treat as image", "resource-native", "low"),
    (".webp", "image", "Treat as image", "resource-native", "low"),
    (".gif", "image", "Treat as image", "resource-native", "low"),
    (".json", "structured-fetch", "Treat as structured payload", "resource-native", "low"),
    (".xml", "structured-fetch", "Treat as XML or RSS", "resource-native", "low"),
    (".rss", "structured-fetch", "Treat as RSS", "resource-native", "low"),
    (".atom", "structured-fetch", "Treat as Atom feed", "resource-native", "low"),
]


def detect(url: str) -> dict:
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    path = (parsed.path or "").lower()

    for suffix, route, reason, action_level, risk in FILE_SUFFIX_RULES:
        if path.endswith(suffix):
            return {
                "kind": "file-like",
                "route": route,
                "reason": reason,
                "action_level": action_level,
                "risk": risk,
                "next_step": route,
                "fallbacks": [],
            }

    for domain, route, reason, action_level, risk in PLATFORM_RULES:
        if host == domain or host.endswith('.' + domain):
            return {
                "kind": "platform",
                "route": route,
                "reason": reason,
                "action_level": action_level,
                "risk": risk,
                "next_step": route,
                "fallbacks": ["web_extract", "browser", "user-assist"] if route != "wechat-reader" else ["browser", "metadata-fallback", "user-assist"],
            }

    browser_signals = ["app.", "account.", "dashboard."]
    browser_needed = any(sig in host for sig in browser_signals)
    return {
        "kind": "generic-webpage",
        "route": "browser" if browser_needed else "web_extract",
        "reason": "Likely interactive app shell" if browser_needed else "Ordinary public webpage",
        "action_level": "browser-needed" if browser_needed else "lightweight-first",
        "risk": "medium" if browser_needed else "low",
        "next_step": "browser" if browser_needed else "web_extract",
        "fallbacks": ["browser", "jina-reader", "user-assist"] if not browser_needed else ["user-assist"],
    }


def main():
    parser = argparse.ArgumentParser(description="Thin URL router for the web-reading-router skill")
    parser.add_argument("url")
    args = parser.parse_args()
    result = detect(args.url)
    result["url"] = args.url
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
