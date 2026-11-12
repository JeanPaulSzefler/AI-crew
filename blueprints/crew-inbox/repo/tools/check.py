#!/usr/bin/env python3
"""Check that the inbox is consistent. No dependencies.

Run: python3 tools/check.py     Exit code 0 = pass. Otherwise do not commit.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = re.compile(r"^- (H-(\d{4})) · from: (\S+) · (N-[\w.-]+-\d+) · ")
ENTRY = re.compile(r"^- (H-\d{4}) · ")
REPO_ROW = re.compile(r"^\|\s*`?[\w.-]+/[\w.-]+`?\s*\|")
problems = []


def lines(*parts):
    path = os.path.join(ROOT, *parts)
    return open(path, encoding="utf-8").read().splitlines() if os.path.exists(path) else None


for name in ("AGENTS.md", "CLAUDE.md", "repos.md", "index.md", "JOURNAL.md"):
    if lines(name) is None:
        problems.append(f"{name}: missing")

if not any(REPO_ROW.match(line) for line in lines("repos.md") or []):
    problems.append("repos.md: no repository listed")

index_ids, sources = [], set()
for line in lines("index.md") or []:
    match = INDEX.match(line)
    if match:
        index_ids.append(match.group(1))
        key = (match.group(3), match.group(4))
        if key in sources:
            problems.append(f"index.md: note collected twice: {key[0]} {key[1]}")
        sources.add(key)
    elif line.startswith("- H-"):
        problems.append(f"index.md: entry not in the expected format: {line[:60]}")
for position, hub_id in enumerate(index_ids, start=1):
    if hub_id != f"H-{position:04d}":
        problems.append(f"index.md: expected H-{position:04d}, found {hub_id}")
        break

delivered = {}
folder = os.path.join(ROOT, "for")
for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
    if not name.endswith(".md") or name == "README.md":
        continue
    for line in lines("for", name):
        match = ENTRY.match(line)
        if match:
            delivered.setdefault(match.group(1), []).append(name)
for hub_id in index_ids:
    files = delivered.get(hub_id, [])
    if len(files) != 1:
        problems.append(f"{hub_id}: must be in exactly one file in for/, found in {len(files)}")
for hub_id in delivered:
    if hub_id not in index_ids:
        problems.append(f"{hub_id}: in for/ but not in index.md")

if problems:
    print(f"CHECK FAILED: {len(problems)} problem(s)")
    for problem in problems:
        print(" -", problem)
    sys.exit(1)
print(f"CHECK PASSED: {len(index_ids)} note(s)")
