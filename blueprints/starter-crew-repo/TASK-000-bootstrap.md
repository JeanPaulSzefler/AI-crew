---
id: TASK-000
title: Set up a new repository from the starter-crew-repo blueprint
who: lead (Sonnet), advisor (Opus) once, owner
class: B
---

# TASK-000: a new repository from the blueprint

## Goal

An empty repository is made ready for the crew: rules, board, check and roles. No project content and no project code.

## Input from the owner

- The project name and one to three sentences: what for and for whom.
- The variant: content or code.
- Repository visibility (public or private) and the name of the main branch.

## Owner's steps

1. Create the empty repository on GitHub and open a Claude session on it. **One repository per session.**
2. After approving the pull request: in a public repository, protect the main branch (required check `check`). In a private repository on the Free plan protection does not work; the rules in `AGENTS.md` and the `ask` rules remain.
3. Optional: connect the repository in Codex and turn on automatic reviews.

## Lead's steps (one pull request)

1. Copy `core/` to the repository root. Rename `dot-claude` to `.claude` and `dot-gitignore` to `.gitignore`.
2. Add the files of the chosen variant (`variant-content/` or `variant-code/`) **without its `README.md`**, which is only a guide. Rename `dot-github` to `.github`. For the code variant also copy `dot-claude/agents/reviewer.md` to `.claude/agents/`.
3. Fill every `{{…}}` field in `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/brief.md`, `BOARD.md`, `JOURNAL.md`. Add to `AGENTS.md` the rows and rules listed in the variant's README.
4. Set the check command in `AGENTS.md` and in `.github/workflows/check.yml`. Run it. It must pass.
5. Record decision `0001`: variant, autonomy level 1, assumptions (subscriptions, where work happens) with their revisit conditions.
6. Put three to five first tasks under "Ready" in `BOARD.md`, each with goal, files, acceptance and class.
7. **One advisor consultation:** a one-page brief built from `docs/brief.md` and the list of first tasks. Question: do scope and order make sense, and what is the biggest risk? Add the verdict to `JOURNAL.md`.
8. Open the pull request for the owner.

## Accept

- [ ] No `{{` is left in the repository outside example blocks.
- [ ] `AGENTS.md` and `CLAUDE.md` together have fewer than 200 lines.
- [ ] The check command passes locally and in CI.
- [ ] `.claude/settings.json` is valid JSON with `deny` rules, `ask` rules and the subagent nesting limit.
- [ ] `advisor.md` has read-only tools.
- [ ] `BOARD.md` has at least three ready tasks, and the note id in "For other projects" contains the repository name.
- [ ] `work/README.md` exists with the state file template.
- [ ] The owner approved the pull request.

## Out of scope

Project content and code, skills, scheduled tasks (stage 1), releases (stage 2), secrets and accounts.
