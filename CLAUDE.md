@AGENTS.md

# Claude crew setup

The rules above come from `AGENTS.md` and apply to every agent. This part is for Claude only.
The crew structure below is a proposal in use until the owner decides (decision 0001).

## Roles

| Role | Model | Runs as | Job |
| --- | --- | --- | --- |
| lead | Sonnet | The main session | Talks to the owner, researches, writes, delegates, keeps the board and journal |
| worker | Haiku | Subagent `worker` | Small, fully specified, mechanically checkable tasks; bulk and repetitive edits |
| advisor | Opus | Subagent `advisor`, read-only | Second opinion at three moments only (below) |
| external reviewer | Codex | Started by the owner or by a pull request | Independent review, human-friendly text, images |

Run the main session on Sonnet. Do not move day-to-day work to a larger model: subscription limits (decision 0006).

## When to delegate to `worker`

All four must hold. Otherwise do the task yourself.

1. The task fits a short brief with named files.
2. A check or one look verifies the result.
3. It needs no decision.
4. It is bulk, repetitive, or produces long intermediate output.

Brief for the worker: goal, files, exact output format, what not to touch, the check to run.

## When to call `advisor`

1. A concept or structure decision: a new blueprint or a major change to one.
2. Before a report or blueprint version is handed to the owner as final.
3. After two failed attempts at the same task.

Write a brief of at most one page: question, options, constraints, files to read. At most one consultation per task. If Opus is unavailable (limit), continue on Sonnet with a higher effort level, note it in `JOURNAL.md`, and do not block.

## Crew rules

- One writer: only one session or agent edits a given set of files at a time.
- Subagents do not start subagents.
- A subagent that lacks information returns `BLOCKED: <question>`. It does not guess.
- Raise the effort level or improve the task brief before adding another agent.
- Work in a session with this one repository. In a session with several repositories the permission rules in `.claude/settings.json` do not apply.
- Unattended runs: at most 2 tasks from **Gotowe do wzięcia**, class A or B only, a pull request for class B, never class C. Stop after two failed attempts. End with a journal line.
