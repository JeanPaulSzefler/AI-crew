# Blueprints

Starting structures for the AI crew, developed here before they are copied into a real project repo.

## Conventions

- One folder per blueprint, named in kebab-case, e.g. `starter-crew-repo/`.
- Inside each folder, lay out the files as they would appear in the target repo. Hidden folders are stored as `dot-claude/` and `dot-github/` so that they are inert here and visible in file browsers; the bootstrap task renames them.
- Each blueprint has its own `README.md` stating its purpose, status (`draft`, `review`, `approved`), source documents and open decisions.
- Files that are copied into a repository are in English, with English tags and field names. The guide that explains a blueprint may be in Polish (decision 0010).
- Changes to a blueprint go through a pull request, as the crew's "hiring" rule requires.

## Blueprints

| Blueprint | Status | Based on |
| --- | --- | --- |
| [`starter-crew-repo/`](starter-crew-repo/README.md) | v1.2, proposal for a pilot | [Concept report of 11 Nov](../outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md). Core files, content and code variants, growth stages, automation, bootstrap task. v1.1 adds task state files with checkpoints and cross-project notes |
| [`crew-inbox/`](crew-inbox/README.md) | v1.1, accepted (decision 0009); the private repository itself waits for the owner to create it | Central inbox for notes between projects: rules, collector script, check. Complements `starter-crew-repo/automation/cross-repo-notes.md` |
| [`spiewnik-live/`](spiewnik-live/) | draft (waiting for owner answers). Predates `starter-crew-repo`; to be aligned with it (task T-002) | [Requirements report v1](../outputs/2026-11-08-spiewnik-live-wymagania-v1.md) |
