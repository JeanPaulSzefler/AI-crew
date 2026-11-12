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

1. **Crew structure** ([decision 0001](docs/decisions/0001-struktura-zalogi.md), [report](outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md) chapters 3 and 4): accept, change or reject? It is a proposal until answered.
2. **Autonomy level of this repository:** recorded as 2 (the crew merges journal, board, index and typo changes itself). Confirm, or change to 1 ([decision 0003](docs/decisions/0003-tryby-autonomii.md)).
3. **Mode (c):** in which repository and from when should the two scheduled tasks run ([prompts](blueprints/starter-crew-repo/automation/scheduled-tasks.md))? The owner turns them on, or the crew does on the owner's explicit instruction.
4. **Pilot:** which new project is set up from the blueprint first?
5. **Default branch on GitHub** is still the session branch, not `master`. Change: Settings → Branches (owner only).
6. **Correction:** the hosting report v3 and a review in the public games repository record "consider" as "the owner's decision". A fix was proposed and waits for approval.
7. **Git history** holds older report versions with details of private projects. Postponed by the owner on 2026-11-11.
8. **Working assumption** to confirm: tasks and decisions live in files ([0002](docs/decisions/0002-zadania-i-decyzje-w-plikach.md)).
9. **Create the empty private repository `crew-inbox`** (GitHub: New repository → Private). The Claude integration cannot create repositories. After that, say "start the inbox" in a session. Also to decide: which repositories to connect besides this one. State: [`work/T-005-crew-inbox.md`](work/T-005-crew-inbox.md).

## Ready

- [ ] T-002 · Align the songbook bootstrap task with the new blueprint · who: lead · class: B
      Goal: the songbook `TASK-000` uses `starter-crew-repo` (code variant) instead of its own file list. Files: `blueprints/spiewnik-live/`. Accept: the task points to the blueprint, does not repeat its content, and the check passes.
- [ ] T-003 · Add a glossary for the owner to the blueprint · who: lead · class: B
      Goal: one page in Polish: session, subagent, risk class, autonomy level, scheduled task, pull request. Files: `blueprints/starter-crew-repo/`. Accept: every term used in the blueprint README is explained in two sentences.

## In progress

A paused or handed-over task has a state file in [`work/`](work/README.md). The entry gives the state and links the file.

- [ ] T-005 · Start the central inbox `crew-inbox` · who: lead · class: B · state: waiting for owner · [state file](work/T-005-crew-inbox.md)

## Ideas

Not prepared yet. Agents may add here; they may not start these.

- Check in practice the five questions from chapter 11 of the report (advisor in cloud sessions, automatic Codex reviews, `@codex review` posted by the crew, images from Codex, limit use in mode c). Needs the owner's accounts and a session on Sonnet.
- A blueprint variant for a mobile app or a game, with a `needs-pc` step for building the package.
- After the pilot: review the blueprint as chapter 10 of the report describes.
- Review the 31 Oct report and the skills recommendation against decisions 0001 to 0010.
- One trial of a courier session (variant B in decision 0008): a session starts a short session in the target repository, which writes the note there.
- Automate collecting in the inbox (decision 0009: "automate later"). Conditions in `blueprints/crew-inbox/README.md`: two connected repositories, three successful manual collections, the owner's approval of a scheduled task.
- Translate the prose of the blueprint guides to English if the owner prefers one language everywhere (decision 0010 allows both).

## For other projects

Ideas noticed while working here that concern another repository. Append only, newest at the bottom. Nobody writes into another repository from here; the target repository's own session picks the note up. Rules: [`AGENTS.md`](AGENTS.md), section "Other repositories".

```text
- N-aicrew-001 · for: repo-name · YYYY-MM-DD
      Noticed: … Why it matters: … Where to see it: file or place.
```

- (empty)

## Done

The last 10. Older ones are in the git history and in `JOURNAL.md`.

- [x] T-001 · Concept report, starter structure of this repository and the `starter-crew-repo` blueprint · who: lead · class: B · 2026-11-11
- [x] T-004 · Blueprint v1.1: task state files, checkpoints, one repository per session, outbox for notes (decisions 0007 and 0008) · who: lead · class: B · 2026-11-11
- [x] T-006 · English for agent-facing files, tags and file structure (decision 0010) · who: lead · class: B · 2026-11-12
