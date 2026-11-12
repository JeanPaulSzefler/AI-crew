# Decisions

One decision per file. Numbers go up: `NNNN-short-title.md`.

- A decision is **never edited**. A change is a new decision; the old one gets a note at the top with the date and the number of the new one.
- The highest-numbered decision on a matter is the one in force.
- The status tells the truth: `accepted` only when the owner confirmed it. An agent's recommendation is a `proposal`. An assumption the owner neither rejected nor confirmed is a `working assumption`.
- Decisions 0001 to 0009 are in Polish, as written. From 0010 on, decisions are in English.

Template: [`0000-template.md`](0000-template.md).

| No. | Decision | Status |
| --- | --- | --- |
| [0001](0001-struktura-zalogi.md) | Sonnet leads, Haiku does small tasks, Opus advises at set moments, Codex works independently | proposal |
| [0002](0002-zadania-i-decyzje-w-plikach.md) | Tasks and decisions are files in the repository, not GitHub Issues | working assumption |
| [0003](0003-tryby-autonomii.md) | Three autonomy modes and the "always the owner" list; this repository is at level 2 | accepted; the level of this repository waits for confirmation |
| [0004](0004-jezyk-plikow.md) | Agent files in English, owner files in Polish | superseded by 0010 |
| [0005](0005-prywatne-projekty-tylko-w-formie-uogolnionej.md) | No names or diagnoses of the owner's other projects in this repository | accepted |
| [0006](0006-subskrypcje-jako-punkt-odniesienia.md) | Claude Pro and ChatGPT Plus without a paid API as the reference point | accepted |
| [0007](0007-zadanie-niesie-swoj-stan.md) | A task carries its state: state file, checkpoints, fixed resume order | accepted |
| [0008](0008-jedno-repo-na-sesje-i-skrzynka-nadawcza.md) | One repository per session, others read-only; ideas for other projects go to an outbox | accepted |
| [0009](0009-skrzynka-centralna-crew-inbox.md) | The central inbox is a separate private repository `crew-inbox`; collected on command, automated later | accepted |
| [0010](0010-language.md) | English for agents, tags and file structure; Polish only for long texts the owner analyses | accepted |
