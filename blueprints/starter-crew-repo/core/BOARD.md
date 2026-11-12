# Task board

The state of work in this repository. Agents start here. Rules: [`AGENTS.md`](AGENTS.md).

Task format:

```text
- [ ] T-001 · title · who: lead | worker | codex | owner · class: A | B | C
      Goal: what must exist. Files: where. Accept: how to tell it is done.
```

A task without goal, files and acceptance is not ready and stays under "Ideas".
Optional tags: `needs-pc` (cannot be done in the cloud), `external` (an idea from another project, with its note id).

## Waiting for owner

Questions and approvals. Oldest first. The owner answers under the entry.

- (empty)

## Ready

- [ ] T-001 · {{title}} · who: lead · class: B
      Goal: {{…}}. Files: {{…}}. Accept: {{…}}.

## In progress

A paused or handed-over task has a state file in [`work/`](work/README.md). The entry gives the state and links the file.

- (empty)

## Ideas

Not prepared yet. Agents may add here; they may not start these.

- (empty)

## For other projects

Ideas noticed while working here that concern another repository. Append only, newest at the bottom. Nobody writes into another repository from here; the target repository's own session picks the note up. Rules: [`AGENTS.md`](AGENTS.md), section "Other repositories".

```text
- N-{{repo}}-001 · for: repo-name · YYYY-MM-DD
      Noticed: … Why it matters: … Where to see it: file or place.
```

- (empty)

## Done

The last 10. Older ones are in the git history and in `JOURNAL.md`.

- (empty)
