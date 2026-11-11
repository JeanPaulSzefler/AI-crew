#!/usr/bin/env python3
"""Repository check for a content project. No dependencies.

Run: python3 tools/check.py
Exit code 0 = pass. Any other = fail; do not commit.
Changing this file is an owner-only action (see AGENTS.md).
"""
import json
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Settings for this repository -------------------------------------------
# Folders whose Markdown links are not checked: raw sources, records that are
# never edited, and template folders.
SKIP_LINKS_IN = ["resources", "docs/decisions", "docs/out-of-scope"]
# Folders whose README.md must mention every other .md file in the folder.
INDEXED_DIRS = ["outputs", "recommendations"]
# Instruction files and their line limit.
INSTRUCTION_FILES = ["AGENTS.md", "CLAUDE.md"]
MAX_INSTRUCTION_LINES = 200
# -----------------------------------------------------------------------------

IGNORED_DIRS = {".git", "node_modules", ".venv", "__pycache__"}
LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
problems = []


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def markdown_files():
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for name in files:
            if name.lower().endswith(".md"):
                yield os.path.join(folder, name)


def check_links():
    for path in markdown_files():
        r = rel(path)
        if any(r == s or r.startswith(s + "/") for s in SKIP_LINKS_IN):
            continue
        text = open(path, encoding="utf-8").read()
        text = INLINE.sub("", FENCE.sub("", text))
        for target in LINK.findall(text):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue  # web link, mailto, or anchor in the same file
            if "{{" in target:
                continue  # template placeholder
            file_part = unquote(target.split("#", 1)[0])
            base = ROOT if file_part.startswith("/") else os.path.dirname(path)
            if not os.path.exists(os.path.normpath(os.path.join(base, file_part.lstrip("/")))):
                problems.append(f"{r}: broken link -> {target}")


def check_instruction_files():
    for name in INSTRUCTION_FILES:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            problems.append(f"{name}: missing")
            continue
        lines = sum(1 for _ in open(path, encoding="utf-8"))
        if lines > MAX_INSTRUCTION_LINES:
            problems.append(f"{name}: {lines} lines, limit is {MAX_INSTRUCTION_LINES}")


def check_board():
    path = os.path.join(ROOT, "BOARD.md")
    if not os.path.exists(path):
        problems.append("BOARD.md: missing")
        return
    seen = {}
    text = FENCE.sub("", open(path, encoding="utf-8").read())
    for line in text.splitlines():
        m = re.match(r"\s*- \[[ xX]\] (T-\d+)\b", line)
        if m:
            seen[m.group(1)] = seen.get(m.group(1), 0) + 1
    for task, count in sorted(seen.items()):
        if count > 1:
            problems.append(f"BOARD.md: task id {task} appears {count} times")


def check_decisions():
    folder = os.path.join(ROOT, "docs", "decisions")
    if not os.path.isdir(folder):
        problems.append("docs/decisions/: missing")
        return
    numbers = {}
    for name in sorted(os.listdir(folder)):
        m = re.match(r"(\d{4})-.+\.md$", name)
        if not m:
            continue
        numbers.setdefault(m.group(1), []).append(name)
        if m.group(1) != "0000" and "**Status:**" not in open(os.path.join(folder, name), encoding="utf-8").read():
            problems.append(f"docs/decisions/{name}: no Status line")
    for number, names in numbers.items():
        if len(names) > 1:
            problems.append(f"docs/decisions/: number {number} used twice: {', '.join(names)}")


def check_indexes():
    for d in INDEXED_DIRS:
        folder = os.path.join(ROOT, d)
        readme = os.path.join(folder, "README.md")
        if not os.path.exists(readme):
            problems.append(f"{d}/README.md: missing")
            continue
        index = open(readme, encoding="utf-8").read()
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md") and name != "README.md" and name not in index:
                problems.append(f"{d}/README.md: does not list {name}")


def check_settings():
    path = os.path.join(ROOT, ".claude", "settings.json")
    if os.path.exists(path):
        try:
            json.load(open(path, encoding="utf-8"))
        except ValueError as error:
            problems.append(f".claude/settings.json: not valid JSON ({error})")


for check in (check_links, check_instruction_files, check_board, check_decisions, check_indexes, check_settings):
    check()

if problems:
    print(f"CHECK FAILED: {len(problems)} problem(s)")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("CHECK PASSED")
