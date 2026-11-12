# crew-inbox

A private inbox for ideas between projects. A crew working in one repository writes a note for another project in its own board. The inbox collects those notes in one place, and each project reads only its own file.

This is a list, not a task board. Whether an idea becomes a task is the owner's decision in the target repository.

## How to use it from the phone

| I want to… | What to do |
| --- | --- |
| collect new notes | A session in this repository (model Haiku): "collect notes" |
| pick up notes in a project | A session in the project's repository: "pick up notes from the inbox" |
| connect another repository | A session in this repository: "connect owner/name, private" (or "public") |
| see everything | [`index.md`](index.md) |
| read the analyses of new project ideas | [`project-ideas/`](project-ideas/README.md) |

The phrases can be in any language.

## Connecting a repository

1. The project's repository needs an outbox: the section "For other projects" in `BOARD.md`. A repository without a board can have a file `OUTBOX.md` with the same section heading. That repository's own session adds it.
2. A row is added to [`repos.md`](repos.md): repository, visibility, file.

Note format in the outbox:

```text
## For other projects

- N-reponame-001 · for: repo-name · YYYY-MM-DD
      Noticed: … Why it matters: … Where to see it: file or place.
```

## Files

| File | Holds |
| --- | --- |
| [`repos.md`](repos.md) | Connected repositories |
| [`index.md`](index.md) | Every collected note with its source |
| [`for/`](for/README.md) | One file per target repository |
| [`JOURNAL.md`](JOURNAL.md) | One line per collection |
| [`project-ideas/`](project-ideas/README.md) | Preliminary analyses of ideas for new projects |
| `tools/collect.py`, `tools/check.py` | The collector and the check |

## Privacy

This repository is private and names private projects. The file `for/<repo>.md` of a public repository does not say where a note came from. The source crew writes the note; for a public repository the text must be generalised.
