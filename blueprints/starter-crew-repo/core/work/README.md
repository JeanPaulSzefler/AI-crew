# Task state files

A task carries its own state, so that another session, another model or another vendor can continue it, also after a sudden stop.

## When a task gets a file

A file `T-NNN-title.md` is created when the task:

- will not be finished in one sitting,
- waits for the owner's decision,
- goes to someone else (worker, advisor, Codex).

A task finished in one sitting stays a line on the board.

## Rules

1. **Checkpoint after every step:** update the state file first, then commit and push. A usage limit can stop the session at any moment, so state is written during the work, not at the end.
2. **"Next step" is one concrete action** that can be done without asking anything.
3. **One holder.** Whoever hands the task over changes the `Holder` field.
4. **To resume:** board → state file → `git log` of the task branch → check → next step.
5. When the task is finished the file stays, with state `done`. The board entry moves to "Done".

## Kinds of pause

| Pause | What to write | Who resumes |
| --- | --- | --- |
| Usage limit | Nothing extra: the last checkpoint is enough | The same session after the limit resets, or the next run |
| Owner's decision | The question with options in the state file, and an entry under "Waiting for owner" | Any session, after the answer |
| Handover | Who holds the task and what must come back | The receiver, then the lead |

## Template

```markdown
# T-NNN: title

- **State:** in progress | paused: limit | waiting for owner | handed over: worker / advisor / codex | done
- **Holder:** lead | worker | codex | owner
- **Class:** A | B | C · **Branch:** `branch-name`
- **Last checkpoint:** YYYY-MM-DD, commit `abc1234`

## Goal and acceptance
Copied from the board. Do not change it during the work.

## Done
- …

## Next step
One concrete action.

## Open questions
- Question · options · what I do without an answer (or: "waiting")

## Pitfalls and findings
What not to touch, what was already tried without success, choices made along the way.
```
