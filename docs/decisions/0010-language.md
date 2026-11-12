# 0010: English for agents, tags and file structure; Polish only for long texts the owner analyses

- **Date:** 2026-11-12
- **Status:** accepted
- **Basis:** Owner, 2026-11-12: communication for agents in English; task tags and the internal structure of files in English too; only long texts for the owner's analysis in Polish; English is also fine there, so writing those in English is not an error

## Decision

- English: everything agents read to do the work (instruction files, prompts, briefs, board, state files, journal, decisions, project brief, READMEs, commit messages) and every tag, field name, section name, status value and file name.
- Polish, or English: long texts written for the owner to analyse, such as reports, recommendations and the guides that explain a blueprint.
- Records written in Polish before this decision stay as written: decisions 0001 to 0009, out-of-scope entries and journal entries.

Renamed with this decision. Board sections: "Czeka na Ownera" is now "Waiting for owner", "Gotowe do wzięcia" is "Ready", "W toku" is "In progress", "Pomysły" is "Ideas", "Dla innych projektów" is "For other projects", "Zrobione" is "Done". Task tags: `kto` is `who`, `klasa` is `class`, `Cel / Pliki / Odbiór` is `Goal / Files / Accept`, "wymaga komputera" is `needs-pc`, "z zewnątrz" is `external`. State file fields: `Stan`, `Trzyma`, `Klasa`, `Gałąź` are `State`, `Holder`, `Class`, `Branch`. Notes between projects use `for:` instead of `dla:`.

Supersedes decision 0004.

## Reason

Instruction and state files are read by agents from more than one vendor, and one language for names removes a class of mismatches between files, prompts and scripts. The owner reads both languages; Polish is kept where reading is long and the owner has to judge the content.

## Revisit when

A person who does not read English joins a project, or mixed-language guides start to cause agent errors.
