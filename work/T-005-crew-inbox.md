# T-005: Start the central inbox `crew-inbox`

- **State:** waiting for owner
- **Holder:** owner
- **Class:** B · **Branch:** `master` (blueprint); new repository: its main branch
- **Last checkpoint:** 2026-11-12, blueprint `crew-inbox` switched to English names (decision 0010)

## Goal and acceptance

The private repository `crew-inbox` exists, holds the files from `blueprints/crew-inbox/repo/`, and the first collection and the check pass. Decision 0009.

## Done

- Blueprint `blueprints/crew-inbox/`: rules, owner guide, collector script, check, CI.
- Script and check tested on sample data and on reading a public repository.
- Creating the repository through the integration was refused by GitHub (no permission to create repositories).

## Next step

After the owner creates the repository: attach `crew-inbox` to the session with write access, do step 2 of "Założenie skrzynki" in `blueprints/crew-inbox/README.md`, list `AI-crew` (public, `BOARD.md`) in `repos.md`, run the collector and the check, push.

## Open questions

- Owner: create the empty private repository `crew-inbox` · nothing can continue without it · waiting.
- Owner: which repositories to connect besides `AI-crew`? · without an answer only `AI-crew` is connected.

## Pitfalls and findings

- If the Claude app on GitHub has access to selected repositories only, the new repository must be added to them.
- Names of the owner's other repositories are written only in the private inbox, never here.
- Collecting is on command. Do not create a scheduled task without a separate decision.
