# Specs

The source of truth for what the program must do. A behaviour change starts here, then becomes a task on the board, then code and a test.

- One file per area: `SPEC-NNN-title.md`.
- Requirements are **numbered clauses** (`SPEC-003.4`). Tasks, tests and commits cite the clause number.
- Every clause has an acceptance criterion that a test can check.
- A bug fix that restores specified behaviour needs no spec change. Name the clause it restores.
- The agent drafts a spec; the owner approves it.

## Template

```markdown
# SPEC-NNN: title

Status: draft | approved YYYY-MM-DD

## Goal
One or two sentences.

## Clauses
1. The program … (Accept: …)
2. …

## Out of scope
- …
```
