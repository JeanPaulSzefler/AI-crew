# T-005: Start the central inbox `crew-inbox`

- **State:** done
- **Holder:** lead
- **Class:** B · **Branch:** `master` (blueprint); `crew-inbox`: `master`
- **Last checkpoint:** 2026-11-12, inbox set up and pushed; first collection found no notes; check passes

## Goal and acceptance

The private repository `crew-inbox` exists, holds the files from `blueprints/crew-inbox/repo/`, and the first collection and the check pass. Decision 0009.

## Done

- Blueprint `blueprints/crew-inbox/`: rules, owner guide, collector script, check, CI.
- Script and check tested on sample data and on reading a public repository.
- Creating the repository through the integration was refused by GitHub (no permission to create repositories). The owner created it on 2026-11-12.
- Inbox set up from the blueprint; `AI-crew` connected; first collection and check passed.
- Added `project-ideas/` to the inbox and the blueprint at the owner's request.

## Next step

None. Follow-ups are on the board: which repositories to connect, and automation later.

## Open questions

- Owner: which repositories to connect besides `AI-crew`? Moved to the board, "Waiting for owner", item 9.

## Pitfalls and findings

- If the Claude app on GitHub has access to selected repositories only, the new repository must be added to them.
- Names of the owner's other repositories are written only in the private inbox, never here.
- Collecting is on command. Do not create a scheduled task without a separate decision.
