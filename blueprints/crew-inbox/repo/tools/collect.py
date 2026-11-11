#!/usr/bin/env python3
"""Collect notes for other projects into this inbox. No dependencies.

Run:  python3 tools/collect.py
      python3 tools/collect.py --local owner/name=/path/to/clone   (repeatable)
      python3 tools/collect.py --dry-run

Reads repos.md, fetches the outbox file of every listed repository and appends
each note that is not in index.md yet to index.md and to for/<target>.md.
It never changes a note's text and never writes outside this repository.
Exit code: 0 = all repositories read; 2 = at least one could not be read.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTION = "## Dla innych projektów"
REPO = re.compile(r"^[\w.-]+/[\w.-]+$")
PATH = re.compile(r"^[\w][\w./ -]*$")
NOTE = re.compile(r"^- (N-[\w.-]+-\d+)\s*·\s*dla:\s*([\w./-]+)\s*·\s*(\d{4}-\d{2}-\d{2})\s*$")
INDEX = re.compile(r"^- H-(\d{4}) · z: (\S+) · (N-[\w.-]+-\d+) · ")


def registry():
    rows = []
    for line in open(os.path.join(ROOT, "repos.md"), encoding="utf-8"):
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and REPO.match(cells[0]) and PATH.match(cells[2]):
            rows.append({"repo": cells[0], "name": cells[0].split("/")[1].lower(),
                         "public": cells[1].lower().startswith("publ"), "path": cells[2]})
    return rows


def git(args, cwd=None):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")  # never wait for a password prompt
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, timeout=180, env=env)


def fetch(repo, path, local):
    """Return the outbox file's text, or None if it cannot be read."""
    if repo in local:
        try:
            return open(os.path.join(local[repo], path), encoding="utf-8").read()
        except OSError:
            return None
    with tempfile.TemporaryDirectory() as tmp:
        url = f"https://github.com/{repo}.git"
        for extra in (["--filter=blob:none"], []):
            target = os.path.join(tmp, "partial" if extra else "full")
            if git(["clone", "--quiet", "--depth", "1", "--no-checkout"] + extra + [url, target]).returncode == 0:
                shown = git(["show", f"HEAD:{path}"], cwd=target)
                if shown.returncode == 0:
                    return shown.stdout
        return None


def parse_outbox(text):
    """Return (notes, malformed). A note is (source_id, target, date, body_lines)."""
    notes, malformed, inside, fenced, current = [], [], False, False, None
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced, current = not fenced, None
            continue
        if fenced:
            continue
        if line.startswith("## "):
            inside, current = line.strip() == SECTION, None
            continue
        if not inside:
            continue
        match = NOTE.match(line)
        if match:
            current = (match.group(1), match.group(2), match.group(3), [])
            notes.append(current)
        elif line.startswith("- N-"):
            malformed.append(line.strip())
            current = None
        elif current and line[:1] in (" ", "\t") and line.strip():
            current[3].append(line.strip())
        else:
            current = None
    return notes, malformed


def known():
    seen, last = set(), 0
    path = os.path.join(ROOT, "index.md")
    for line in open(path, encoding="utf-8") if os.path.exists(path) else []:
        match = INDEX.match(line)
        if match:
            last = max(last, int(match.group(1)))
            seen.add((match.group(2), match.group(3)))
    return seen, last


def append(path, text, header=""):
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as handle:
        handle.write((header if new else "") + text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="append", default=[], metavar="owner/name=/path")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    local = dict(item.split("=", 1) for item in args.local)
    repos = registry()
    targets = {row["name"]: row for row in repos}
    seen, last = known()
    today = datetime.date.today().isoformat()
    added, unread, malformed_all = {}, [], []

    for row in repos:
        text = fetch(row["repo"], row["path"], local)
        if text is None:
            unread.append(row["repo"])
            continue
        notes, malformed = parse_outbox(text)
        malformed_all += [f'{row["repo"]}: {m}' for m in malformed]
        for source_id, target, date, body in notes:
            if (row["repo"], source_id) in seen:
                continue
            seen.add((row["repo"], source_id))
            last += 1
            hub_id = f"H-{last:04d}"
            name = target.split("/")[-1].lower()
            known_target = targets.get(name)
            file_name = name if known_target else "_unknown"
            body_text = "".join(f"      {line}\n" for line in body) or "      (brak treści)\n"
            added.setdefault(file_name, []).append(hub_id)
            if args.dry_run:
                continue
            append(os.path.join(ROOT, "index.md"),
                   f'- {hub_id} · z: {row["repo"]} · {source_id} · dla: {target} · notatka: {date} · zebrano: {today}\n{body_text}')
            origin = "" if known_target and known_target["public"] else f' · z: {row["repo"].split("/")[1]} ({source_id})'
            append(os.path.join(ROOT, "for", file_name + ".md"), f"- {hub_id} · {date}{origin}\n{body_text}",
                   header=f"# Notatki dla: {file_name}\n\nTylko dopisywanie. Najnowsze na dole.\n\n")

    total = sum(len(ids) for ids in added.values())
    parts = ", ".join(f"{name}: {len(ids)}" for name, ids in sorted(added.items())) or "brak nowych"
    summary = f"zebrano {total} ({parts}); nieodczytane repo: {len(unread)}; błędne wpisy: {len(malformed_all)}"
    print(("DRY RUN: " if args.dry_run else "") + summary)
    for repo in unread:
        print(" - nie udało się odczytać:", repo)
    for entry in malformed_all:
        print(" - błędny wpis:", entry)
    if not args.dry_run:
        append(os.path.join(ROOT, "JOURNAL.md"), f"- {today}: {summary}\n")
    sys.exit(2 if unread else 0)


main()
