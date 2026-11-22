#!/usr/bin/env python3
"""Validate local relative links in public Markdown files; no dependencies or network."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?(?:\[[^\]\n]*\])\(([^)\n]+)\)")
SCHEMES = ("http:", "https:", "mailto:", "tel:", "data:", "javascript:")
errors = []
scanned = 0

for md in sorted(ROOT.rglob("*.md")):
    if any(part in {".git", "node_modules", ".venv"} for part in md.relative_to(ROOT).parts):
        continue
    scanned += 1
    in_fence = False
    for number, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK.finditer(line):
            raw = match.group(1).strip().split(" ", 1)[0].strip("<>")
            if not raw or raw.startswith(("#", "/")) or raw.lower().startswith(SCHEMES):
                continue
            parts = urlsplit(raw)
            if parts.scheme:
                continue
            relative = unquote(parts.path)
            if not relative:
                continue
            candidate = md.parent / relative
            if not candidate.exists():
                errors.append(f"{md.relative_to(ROOT)}:{number}: missing link target: {raw}")

print(f"Checked local links in {scanned} Markdown files.")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("All checked relative links resolve.")
