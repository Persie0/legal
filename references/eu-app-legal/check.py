#!/usr/bin/env python3
"""Track changes to curated app-publisher legal URLs without storing their text.

Standard-library only. Respect robots.txt, source opt-outs and rate limits.
The first successful --update establishes the baseline; subsequent runs
report changes and update SHA-256 fingerprints of readable page text.
"""

from __future__ import annotations

import argparse
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import time
import unicodedata
from urllib import error, parse, request, robotparser
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
SOURCES = BASE / "sources.json"
FINGERPRINTS = BASE / "fingerprints.json"
UA = "EUAppLegalReferenceTracker/1.0 (+https://github.com/Persie0/legal)"
BLOCKED = {"script", "style", "noscript", "template", "svg", "head", "footer", "header", "nav"}
MIN_TEXT = 250
MAX_BODY_BYTES = 2_000_000


class ReadableText(HTMLParser):
    """Prefer <main>/<article> text, fallback to non-navigation visible body."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.all_text: list[str] = []
        self.main_text: list[str] = []
        self.article_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag.lower())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        pass

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.stack:
            # Recover from invalid/unbalanced HTML.
            idx = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[idx:]

    def handle_data(self, data: str) -> None:
        if any(t in BLOCKED for t in self.stack):
            return
        chunk = re.sub(r"\s+", " ", data).strip()
        if not chunk:
            return
        self.all_text.append(chunk)
        if "main" in self.stack:
            self.main_text.append(chunk)
        if "article" in self.stack:
            self.article_text.append(chunk)

    def text(self) -> str:
        chunks = self.article_text if sum(map(len, self.article_text)) >= MIN_TEXT else (
            self.main_text if sum(map(len, self.main_text)) >= MIN_TEXT else self.all_text
        )
        return normalize_text(" ".join(chunks))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", unescape(text))).strip()


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return result


def robots_allowed(url: str, cache: dict[str, robotparser.RobotFileParser]) -> bool:
    parsed = parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Only HTTPS policy URLs are permitted")
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin not in cache:
        robots_url = origin + "/robots.txt"
        req = request.Request(robots_url, headers={"User-Agent": UA})
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        try:
            with request.urlopen(req, timeout=12) as response:
                if response.status != 200:
                    raise RuntimeError(f"robots.txt HTTP {response.status}")
                body = response.read(200_000).decode("utf-8", errors="replace")
            rp.parse(body.splitlines())
        except error.HTTPError as exc:
            if exc.code in (404, 410):
                # A missing robots.txt does not restrict access.
                rp.parse([])
            else:
                raise RuntimeError(f"robots.txt unavailable: HTTP {exc.code}") from exc
        cache[origin] = rp
    return cache[origin].can_fetch(UA, url)


def fingerprint(url: str, robots_cache: dict[str, robotparser.RobotFileParser]) -> tuple[str, int]:
    if not robots_allowed(url, robots_cache):
        raise PermissionError("robots.txt disallows this request")
    req = request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en,de;q=0.9",
        },
    )
    with request.urlopen(req, timeout=18) as response:
        final_url = response.geturl()
        old_host = (parse.urlsplit(url).hostname or "").removeprefix("www.")
        new_host = (parse.urlsplit(final_url).hostname or "").removeprefix("www.")
        if parse.urlsplit(final_url).scheme != "https" or old_host != new_host:
            raise RuntimeError("Redirect changed site; requires manual URL review")
        content_type = response.headers.get("Content-Type", "").lower()
        if "html" not in content_type:
            raise RuntimeError(f"Unexpected content type: {content_type[:70]}")
        body = response.read(MAX_BODY_BYTES + 1)
        if len(body) > MAX_BODY_BYTES:
            raise RuntimeError("Page too large; manual review required")
        encoding = response.headers.get_content_charset() or "utf-8"
    parser = ReadableText()
    parser.feed(body.decode(encoding, errors="replace"))
    text = parser.text()
    if len(text) < MIN_TEXT:
        raise RuntimeError("Insufficient readable legal text (possible JS challenge)")
    return hashlib.sha256(text.encode("utf-8")).hexdigest(), len(text)


def main() -> int:
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--update", action="store_true", help="Write changed fingerprints")
    args.add_argument("--strict", action="store_true", help="Fail if any check errors occur")
    args.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    opts = args.parse_args()
    sources = load_json(SOURCES, {})
    state = load_json(FINGERPRINTS, {"schema_version": 1, "documents": {}})
    if state.get("schema_version") != 1 or not isinstance(state.get("documents"), dict):
        raise ValueError("Unknown/invalid fingerprint schema")
    robots_cache: dict[str, robotparser.RobotFileParser] = {}
    changed = []
    errors = []
    checked = 0
    skipped = 0
    seen = set()
    for publisher in sources.get("publishers", []):
        for doc in publisher.get("documents", []):
            doc_id = doc["id"]
            if doc_id in seen:
                raise ValueError(f"Duplicate document ID: {doc_id}")
            seen.add(doc_id)
            if doc["monitor"] != "automatic":
                skipped += 1
                continue
            url = doc["url"]
            try:
                digest, size = fingerprint(url, robots_cache)
                checked += 1
                previous = state["documents"].get(doc_id)
                if previous is None or previous["sha256"] != digest or previous["url"] != url:
                    status = "NEW" if previous is None else "CHANGED"
                    changed.append(f"{status:7} {doc_id} {url}")
                    if opts.update:
                        state["documents"][doc_id] = {
                            "url": url,
                            "sha256": digest,
                            "characters": size,
                            "changed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        }
                else:
                    print(f"OK      {doc_id}")
            except (error.URLError, TimeoutError, OSError, RuntimeError, ValueError, PermissionError) as exc:
                errors.append(f"ERROR   {doc_id}: {exc}")
            time.sleep(max(0.0, opts.delay))
    for item in changed + errors:
        print(item)
    print(f"SUMMARY checked={checked} changed={len(changed)} manual={skipped} errors={len(errors)}")
    if opts.update and changed:
        FINGERPRINTS.write_text(
            json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if checked == 0 or (opts.strict and errors):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
