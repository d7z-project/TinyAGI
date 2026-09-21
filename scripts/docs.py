#!/usr/bin/env python3
"""Check public documentation, stage only listed chapters, and build mdBook."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import hashlib
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".mdbook-src"
BOOK = ROOT / "book"
LINK = re.compile(r"(?P<image>!?)\[(?P<label>[^\]\n]+)\]\((?P<url>[^\s)]+)\)")
PRIVATE_ROOTS = ("experiments/", "GPT.md", ".idea/", ".env")
RULES = {
    "API credential": re.compile(
        r"\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}"
        r"|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b"
    ),
    "private key": re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"),
    "bearer credential": re.compile(r"(?i)\bBearer\s+[A-Za-z0-9_.+-]{24,}"),
    "JWT credential": re.compile(r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]{16,}"),
    "personal absolute path": re.compile(r"/(?:home|Users)/[^/\s]+/"),
    "private service URL": re.compile(
        r"https?://(?:localhost|127\.0\.0\.1|10\.(?:\d+\.){2}\d+"
        r"|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b"
    ),
    "URL credential": re.compile(r"https?://[^/\s:@]+:[^/\s@]+@"),
}

# Fingerprint of a redacted historical service hostname; do not store its address.
PRIVATE_HOST_HASHES = {"57bed7a5cab0beb41a0da010946cd48748f6f5f603035b911c7fa183383b33f7"}

def scan(text: str, name: str) -> list[str]:
    """Report only rule names and locations, never matched credential values."""
    findings = [
        f"{name}:{text.count(chr(10), 0, match.start()) + 1}: {rule}"
        for rule, pattern in RULES.items()
        for match in pattern.finditer(text)
    ]
    for match in re.finditer(r"https?://[^\s<>\"'`]+", text):
        try:
            host = urlsplit(match[0]).hostname
        except ValueError:
            continue
        if host and hashlib.sha256(host.lower().encode()).hexdigest() in PRIVATE_HOST_HASHES:
            line = text.count("\n", 0, match.start()) + 1
            findings.append(f"{name}:{line}: historical service URL")
    return findings


def chapters() -> list[Path]:
    summary = ROOT / "SUMMARY.md"
    paths = []
    for match in LINK.finditer(summary.read_text()):
        name = match["url"]
        path = ROOT / name
        if (
            not name.endswith(".md")
            or name not in ("README.md", "DESIGN.md") and not name.startswith("docs/")
            or ".." in PurePosixPath(name).parts
            or path.is_symlink()
            or not path.is_file()
            or not path.resolve().is_relative_to(ROOT)
        ):
            raise ValueError(f"Invalid public chapter: {name}")
        if path in paths:
            raise ValueError(f"Duplicate public chapter: {name}")
        paths.append(path)
    if not paths:
        raise ValueError("SUMMARY.md must list public chapters")
    missing = set((ROOT / "docs").rglob("*.md")) - set(paths)
    if missing:
        raise ValueError("Unlisted documents: " + ", ".join(str(p.relative_to(ROOT)) for p in sorted(missing)))
    return paths


def check() -> list[Path]:
    paths = chapters()
    failures = []
    for path in [*paths, ROOT / "SUMMARY.md", ROOT / "AGENTS.md"]:
        text = path.read_text()
        name = str(path.relative_to(ROOT))
        failures.extend(scan(text, name))
        if re.search(r"<\s*/?\s*(?:details|summary)\b", text, re.I):
            failures.append(f"{name}: collapsed content is not allowed")
        # No include directive can read a file outside the curated chapter set.
        if re.search(r"\{\{\s*#(?:include|rustdoc_include|playground)\b", text):
            failures.append(f"{name}: file inclusion directives are not allowed")
    tracked = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, text=True, capture_output=True, check=True
    ).stdout.split("\0")
    for name in tracked:
        if name and (name.startswith(PRIVATE_ROOTS) or name.endswith(".iml")):
            failures.append(f"{name}: local-only file is still in the Git index")
    if failures:
        raise ValueError("Publication check failed:\n" + "\n".join(failures))
    print(f"Publication check passed: {len(paths)} chapters; no recognized sensitive patterns.")
    return paths


def prepare() -> None:
    paths = check()
    allowed = {str(p.relative_to(ROOT)) for p in paths}
    prepared = {}
    local_references = 0
    upstream_references = 0

    def book_name(name: str) -> str:
        path = PurePosixPath(name)
        return str(path.with_name("index.md")) if path.name == "README.md" else name

    for path in paths:
        name = path.relative_to(ROOT).as_posix()
        parent = posixpath.dirname(name) or "."

        def rewrite(match: re.Match) -> str:
            nonlocal local_references, upstream_references
            raw = match["url"]
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                return match[0]
            target = posixpath.normpath(posixpath.join(parent, unquote(url.path)))
            fragment = "#" + url.fragment if url.fragment else ""
            label = match["label"]
            if target == "GPT.md" or target.startswith("experiments/"):
                if match["image"]:
                    raise ValueError(f"{name}: local-only image cannot be published")
                local_references += 1
                destination = posixpath.relpath("docs/documentation-publishing.md", parent)
                return f"[{label}（本地材料，不发布）]({destination}#local-materials)"
            if target.startswith("../go-mini/"):
                upstream_references += 1
                suffix = target.removeprefix("../go-mini/")
                return f"[{label}](https://github.com/d7z-team/go-mini/blob/main/{suffix}{fragment})"
            if target not in allowed:
                raise ValueError(f"{name}: link target is not a public chapter: {target}")
            destination = posixpath.relpath(book_name(target), parent)
            return f"{match['image']}[{label}]({destination}{fragment})"

        prepared[book_name(name)] = LINK.sub(rewrite, path.read_text())
    # This is the only copied content. Never copy the repository root as book.src.
    if STAGING.is_symlink():
        raise ValueError("Refusing to replace a symlinked staging directory")
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir()
    for name, text in prepared.items():
        destination = STAGING / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text)
    summary = LINK.sub(
        lambda m: f"[{m['label']}]({book_name(m['url'])})",
        (ROOT / "SUMMARY.md").read_text(),
    )
    (STAGING / "SUMMARY.md").write_text(summary)
    print(f"Prepared {len(prepared)} chapters; mapped {local_references} local references and {upstream_references} upstream links.")


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


def verify() -> None:
    if not (BOOK / "index.html").is_file():
        raise ValueError("Build output is missing")
    pages = {}
    failures = []
    for path in BOOK.rglob("*"):
        if path.is_symlink():
            failures.append(f"{path.relative_to(BOOK)}: symlinks cannot be published")
        if path.is_file() and (path.suffix in (".html", ".md", ".json", ".js")):
            # Includes print output and the search index, not only visible pages.
            failures.extend(scan(path.read_text(), str(path.relative_to(BOOK))))
        if path.suffix == ".html" and path.is_file():
            pages[path.resolve()] = Page(path.read_text())
        if path.is_file() and path.suffix in (".md", ".py", ".sqlite", ".log", ".env"):
            failures.append(f"{path.relative_to(BOOK)}: unexpected source/runtime artifact")
    for path, page in pages.items():
        for raw in page.links:
            url = urlsplit(raw)
            if url.scheme or url.netloc or url.path.startswith("/"):
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(BOOK):
                failures.append(f"{path.relative_to(BOOK)}: link escapes output directory")
            elif not target.exists():
                failures.append(f"{path.relative_to(BOOK)}: missing local link {url.path}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                failures.append(f"{path.relative_to(BOOK)}: missing anchor {url.fragment}")
    if not list(BOOK.glob("mermaid*.min.js")) or not list(BOOK.glob("mermaid-init*.js")):
        failures.append("Mermaid assets are missing")
    if failures:
        raise ValueError("Output check failed:\n" + "\n".join(sorted(set(failures))))
    print(f"Output check passed: {len(pages)} HTML pages, local links, assets and sensitive-pattern scan.")


def build() -> None:
    prepare()
    subprocess.run(["mdbook-mermaid", "install", str(ROOT)], check=True)
    env = os.environ.copy()
    if "PAGES_BASE_PATH" in env:
        env["MDBOOK_OUTPUT__HTML__SITE_URL"] = env["PAGES_BASE_PATH"].rstrip("/") + "/"
    subprocess.run(["mdbook", "build", str(ROOT)], env=env, check=True)
    verify()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "prepare", "build", "verify"))
    args = parser.parse_args()
    try:
        {"check": check, "prepare": prepare, "build": build, "verify": verify}[args.command]()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
