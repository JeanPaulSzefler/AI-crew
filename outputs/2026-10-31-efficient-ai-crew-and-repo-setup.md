# Efficient AI Crew and Repo Setup for AI Agents: Updated Recommendations

Oct 31, 2026 · Knowledge article · Builds on [`resources/ai-crew-findings-and-starter-repo-blueprint.md`](../resources/ai-crew-findings-and-starter-repo-blueprint.md)

## Executive summary

The original blueprint holds up well against the current evidence. A flat crew, files instead of chat, tests as the judge, hard budgets and cost-per-task tracking are all backed by Anthropic's own guidance and by independent research. Six things need updating:

1. **Rules must be enforced by configuration, not just written down.** Claude Code now makes an explicit split: `CLAUDE.md`, skills and policy files are *guidance* the model may weigh; hooks, deny rules, branch protection and spend limits are *enforcement*. Every rule in the blueprint's always-human list and budgets needs a matching mechanism (table in [Enforcement map](#enforcement-map-from-written-rule-to-mechanism)).
2. **Model tiering is now "model × effort", and prices have shifted.** Haiku 5.5 is about 20× cheaper per token than Sonnet 5.5, and Opus 5.5 costs only 2× Sonnet. Effort (`low` → `max`) is the first cost lever, ahead of switching models. Escalating to Opus is now cheap, and Haiku is very cheap but only for short, checkable work.
3. **"Two levels maximum" is not the default any more.** Subagents can spawn subagents up to three layers deep by default. The blueprint's rule has to be set explicitly (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`).
4. **Keep `CLAUDE.md` tiny and human-written.** A 2026 study found that auto-generated context files *lower* agent success and raise cost by over 20%, while short, developer-written files of non-obvious conventions help a little. Architecture overviews do not help.
5. **There are two ways to trigger agents now, not one.** GitHub Actions (`claude-code-action@v1`) still covers labels and mentions. Claude Code *cloud scheduled tasks* cover schedules, API calls and GitHub events on a subscription without a workflow file.
6. **Start with three agent definitions, not five.** Planner, executor and reviewer, with the lead and the skill auditor as a skill or checklist until metrics justify more.

## 1. What the evidence says about crew efficiency

### Multi-agent costs a lot and pays only for parallel, read-heavy work

| Source | Finding | Implication for the crew |
| --- | --- | --- |
| Anthropic, multi-agent research system | Agents use about 4× the tokens of chat; multi-agent systems about 15×. Token usage alone explained about 80% of performance variance. Multi-agent (Opus lead, Sonnet workers) beat a single agent by 90.2% on *research* | Multi-agent buys breadth by spending tokens. It is worth it for wide, parallel reading, not by default |
| Same source | Coding has "fewer truly parallelizable parts than research"; tasks with shared context or many dependencies are a poor fit | An implementation crew should be mostly single-threaded, with parallelism only across independent stories |
| Same source | Vague delegation caused duplicated work and gaps; a delegation needs an objective, output format, tool guidance and boundaries | This is the Definition of Ready, applied to agent handoffs |
| Same source | About 20 test cases were enough for early evaluation; judge the end state, not each step | A 20-story baseline is enough to compare crew setups |
| Cognition (Walden Yan), "Don't build multi-agents" and the April 2026 follow-up | Agents that split work make conflicting implicit decisions. What now works in practice: several agents *contribute* intelligence (review, research), but *writes* stay single-threaded | One writer per story; reviewers and researchers read and report |
| Claude Code docs, "Know what subagents cost" | A subagent on the same model gives "parallelism or a fresh pair of eyes", "not a smarter answer". A fresh subagent can be *slower* because it must re-gather context | Do not delegate in the hope of better quality; delegate for parallelism, isolation or independent review |
| Claude Code docs, agent teams | Experimental and off by default. About 7× the tokens of a standard session in plan mode. Teams of 3–5 are recommended; no worktree isolation, so each teammate must own different files | Not for the starter crew. Possibly later for research or review sweeps |

**Verdict:** the blueprint's "single agent by default, spawn only for parallel work, a clean context or an independent review" matches the best current evidence word for word. Keep it as rule 1.

### Independent review beats a "CEO" agent

Claude Code's docs recommend a reviewer "that hasn't seen how the code was written", with read-only tools (`tools: Read, Grep, Glob`) and a prompt that ends with **"skip style"**. Their reason: "a reviewer that's asked to find problems will always find *something*", and fixing every finding produces needless abstraction and tests for impossible cases. This supports the blueprint's critique of the same-model CEO and sharpens the reviewer spec. It should:

- review against a written spec (`SPEC.md` or the story's acceptance criteria),
- report only gaps that affect correctness,
- be unable to edit.

## 2. Model tiering, updated with current prices

Current list prices per million tokens (Anthropic API, Oct 2026):

| Model | Input | Output | Relative to Sonnet 5.5 | Notes |
| --- | --- | --- | --- | --- |
| Haiku 5.5 | $0.10 | $0.50 | ~1/20 | Prompts over 100K tokens cost 5× ($0.50 / $2.50) |
| Sonnet 5.5 | $2.00 | $10.00 | 1× | Default effort `high`, recalibrated levels |
| Opus 5.5 | $4.00 | $20.00 | 2× | Claude Code's default model, at `medium` effort |
| Fable 5.1 | $10.00 | $50.00 | 5× | Most capable; opt-in only |

Batch processing is 50% off, but it is single-shot (no tool loop), so it fits offline grooming jobs, not agent sessions. Prompt caching is the largest single cost lever. Subagents get a 5-minute cache by default, so short, focused subagent runs cache better than long idle ones.

### What changed versus the blueprint

- **Opus is no longer the expensive outlier.** At 2× Sonnet, using Opus for short, high-value moments (gate reviews, unblocking) is cheap. The blueprint's "keep Opus rare" still holds on a *subscription*, where model-specific usage limits apply, but less so on the API.
- **Haiku is now nearly free per token but still not a default executor.** Anthropic's cost guidance says the smallest model "fits high-volume work with checkable outputs, not long agentic loops". Also, a Haiku session whose context grows past 100K tokens pays 5× the base rate. Atomic, short stories with tests suit Haiku; anything that sprawls does not.
- **Effort comes first.** Anthropic's guidance is to sweep effort on the current model before changing models, and to "measure the simpler alternative first — the most capable model at lower effort". Caches are model-scoped, so a cascade that hops between models within one task loses cache reuse.
- **Judge cost per completed task, not per token.** "A cheaper request that needs more turns or retries to finish the job isn't cheaper." Price the hardest tenth of tasks, because that tail is where the money goes.

### Recommended starting assignments

| Role | Model | Effort | Tools | When it runs |
| --- | --- | --- | --- | --- |
| Owner (human) | n/a | n/a | n/a | Goals, spend, publishing, licences, new roles, merges to `main` |
| Planner / refiner | Sonnet 5.5 | `medium` | Read, Grep, Glob, issue/backlog tools | Rough idea → ready story; rewrites failed stories |
| Executor | Sonnet 5.5 to start; Haiku 5.5 for stories labelled `mechanical` once measured | `medium` | Edit, Write, Bash (allow-listed), no Agent tool | One ready story → one PR |
| Reviewer | Opus 5.5 (a different model from the executor) | `medium` | Read, Grep, Glob only | At gates: PR ready, publish, spend |
| Lead (optional) | Opus 5.5 | `high` / `xhigh` | Full, short sessions | After two failed attempts or a grey-zone call |
| Explorer / search | Haiku 5.5 | `low` | Read, Grep, Glob | Codebase sweeps, link checks, log summaries |

**Routing experiment (Phase 3):** run the first ~20 stories on Sonnet to set a baseline. Then route stories that meet a strict "mechanical" definition to Haiku. Keep Haiku only if cost per *merged* story, including retries and review rework, is lower.

## 3. Enforcement map: from written rule to mechanism

Claude Code's own best-practice page puts it plainly: "If something has to happen every time, make it a hook, a deny rule, or a managed setting. `CLAUDE.md` is for guidelines, and Claude is allowed to decide a guideline doesn't apply." It also warns that auto mode is a classifier, so "your 'never' rules belong in deny rules or hooks".

| Blueprint rule | Human-readable source | Enforced by |
| --- | --- | --- |
| Always-human: publishing, releases, irreversible actions | `docs/policies/always-human.md` | Skills for these flows set `disable-model-invocation: true`; `ask` rules on `git push`, deploy and publish commands; branch protection on `main` requiring the owner's approval |
| Always-human: money and ad spend | same | No payment or ads credentials in any agent environment; spend caps at the provider; agents only *propose* spend in a PR or issue |
| Always-human: licences | same | A PR checklist item plus CODEOWNERS on asset folders, so licence-bearing files need the owner's review |
| Secrets never read | `CLAUDE.md` note | `deny` rules: `Read(./.env)`, `Read(./secrets/**)`; they hold in every permission mode |
| Hard budgets | `docs/policies/budgets.md` | API: a dedicated Console workspace with a spend limit. Headless: `--max-turns`, `--max-budget-usd`. Actions: `timeout-minutes`, `concurrency` with `cancel-in-progress`. Subagents: `maxTurns` in frontmatter |
| Two levels maximum | `CLAUDE.md` | `"env": {"CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "1"}` in `.claude/settings.json`; omit `Agent` from subagent `tools` |
| Tests and CI are the judge | `CLAUDE.md` (the test command) | A `Stop` hook that runs the fast test suite (exit 2 blocks "done"); CI as a required status check on `main` |
| Reviewer never edits | `reviewer.md` | `tools: Read, Grep, Glob` in the reviewer's frontmatter |
| Definition of Ready | `docs/policies/definition-of-ready.md` | A GitHub issue *form* with required fields (files, acceptance criteria, test command, size); the executor workflow runs only on the `ready` label, which only the planner or owner applies |
| Capped retries, then escalate | `CLAUDE.md` | Workflow convention: each failed run adds an `attempt-n` label; at `attempt-2` the workflow swaps `ready` for `escalate` instead of running again |
| No agent without an approved PR | `CLAUDE.md` | CODEOWNERS on `.claude/**` and `.github/workflows/**`, so the owner must approve changes to agents, skills, hooks and workflows |

Keep the enforced set small. The docs note that every hook fires wrongly now and then, and "if you ever find yourself at forty of them, most are probably preferences."

## 4. Context files, skills and memory

### `CLAUDE.md` / `AGENTS.md`

- **Size:** under 200 lines (official target). Each line costs attention on every task.
- **Content test:** "Could it find this by reading the code? Would it actually go and look? If both are yes, leave it out." Include exact test, lint and typecheck commands; misleading spots in the code; decisions not visible in the repo; anything corrected twice.
- **Exclude:** architecture overviews and file layouts. Claude reads the repo itself, and the ETH Zürich / LogicStar study (Gloaguen et al., ICLR 2026) found that repository overviews did not help. It also found that LLM-generated context files slightly *reduced* success and raised cost by more than 20%. Developer-written files gave modest gains, mainly for non-standard conventions.
- **No shouting:** `IMPORTANT` and all-caps are now counter-productive. A rule that must hold becomes a hook.
- **AGENTS.md:** Claude Code reads `AGENTS.md` natively when there is no `CLAUDE.md`. If other agents (Codex, Cursor, Gemini CLI) will also work in the repo, keep the shared rules in `AGENTS.md` and make `CLAUDE.md` a one-line `@AGENTS.md` import plus any Claude-only notes. Otherwise, one `CLAUDE.md` is enough.
- **Path-scoped rules:** `.claude/rules/*.md` with a `paths:` filter load only when Claude touches matching files. Use them instead of growing `CLAUDE.md`.
- **Personal notes:** `CLAUDE.local.md`, git-ignored.

### Skills

- A skill's `description` is always in context; the body loads only when used. That makes skills the right home for procedures such as refinement, release and conventions.
- Keep `SKILL.md` under 500 lines; move reference material into sibling files.
- `disable-model-invocation: true` for anything with side effects (release, publish, spend). The owner then has to start it with `/name`.
- Skills follow the open Agent Skills standard (agentskills.io), so they carry over to other tools.
- The blueprint's "a role as a skill, not an agent" (for example marketing) is exactly the recommended pattern.

### Memory

Start with ADRs in `docs/decisions/`, as the blueprint says. Claude Code also has *auto memory* (notes Claude writes itself, first 200 lines loaded) and subagent `memory: project` (version-controlled). Use the latter for the reviewer's recurring findings before considering an external memory system like the one in the source video.

## 5. Coordination: tracker and triggers

### Task board: recommend GitHub Issues + Projects from day one

The blueprint leaned towards Backlog.md. After checking both, I recommend **GitHub Issues + Projects for tasks**, with specs and decisions as Markdown files in the repo:

- `claude-code-action` and cloud scheduled tasks are built around issues, labels and PRs, so triggers need no glue.
- Issues close automatically on merge, and issue forms enforce the Definition of Ready fields.
- It avoids a later migration and a second source of truth.

Backlog.md (MIT, about 7k stars, active) is still a good choice if the crew stays local or offline. Its own guidance matches the blueprint: one task per agent session, one PR per task. It also recommends its CLI instructions over MCP, which matches Claude Code's note that CLIs are more context-efficient than MCP servers. Jira stays out for the reasons the blueprint gives.

### Triggers: two options

| Need | Recommended mechanism | Why |
| --- | --- | --- |
| `@claude` in an issue or PR | `claude-code-action@v1`, interactive mode | Only users with write access can trigger it; bots are rejected unless allow-listed |
| Label `refine` / `ready` | `claude-code-action@v1`, automation mode (`prompt` set), `if:` on the label | Runs on your runner; `claude_args: --model … --max-turns …` |
| Daily backlog triage | Claude Code **cloud scheduled task** (`/schedule`) or an Actions `cron` | Scheduled tasks need no workflow file and run on the subscription; they push only to `claude/` branches |
| Event outside GitHub | Scheduled task **API trigger**, or n8n → `workflow_dispatch` | A scheduled task's API trigger replaces most of what n8n did in the blueprint |
| PR review | The reviewer subagent via a workflow, or Anthropic's managed Code Review (Team/Enterprise) | Managed Code Review needs no workflow file |

Practical notes from the official docs:

- **Authentication:** `ANTHROPIC_API_KEY` (billed per token, hard cap through a Console workspace spend limit) or `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token` (uses the subscription). For automation, I recommend an API key in a dedicated workspace: you get a hard spend limit and exact cost per run.
- **CI on Claude's commits:** commits made with the default `GITHUB_TOKEN` do not trigger other workflows. Let the action authenticate as the Claude GitHub App so `ci.yml` runs on its PRs.
- **Every workflow** gets `timeout-minutes`, a `concurrency` group with `cancel-in-progress: true`, and `--max-turns` in `claude_args`.
- **Public repos:** GitHub withholds secrets from fork PRs and disables `cron` schedules after 60 days without activity.
- **Scheduled tasks** are in research preview, capped at 100 runs per hour per account, and act as *your* GitHub identity. Protect `main` with a rule the task cannot bypass.
- The blueprint cites third-party pages and forks for `claude-code-action`. Replace them with the official repo and docs (see Sources).

## 6. Parallel work without collisions

- **Worktrees:** `claude -w <name>` or `isolation: worktree` in a subagent's frontmatter gives each parallel worker its own checkout. List the small git-ignored files workers need (such as `.env.example`) in `.worktreeinclude`.
- **`/batch`** splits one large mechanical change into 5–30 worktree-isolated units, each with its own PR. This is the right tool for migrations, rather than a crew.
- **Dynamic workflows** run many subagents from a script and cross-check their results. They suit codebase audits and cross-checked research, not day-to-day stories.
- **Agent teams** stay off (experimental, about 7× tokens, no file isolation).

## 7. Measuring whether the crew pays off

The blueprint's rule 12 (measure and prune) is the most important one. Here is how to do it with current tooling:

- **Per session:** `/usage` shows cost and attributes usage by subagent, skill, plugin and MCP server. Its recommendations flag patterns above 10% of usage.
- **Per headless or Action run:** `--output-format json` returns a result object with cost and usage. Append one row per story to `metrics/cost-per-task.csv` with: story id, model, effort, attempts, tokens, USD, merged (y/n), review rework (y/n).
- **Organisation level:** the Console's Claude Code analytics, or OpenTelemetry export.
- **Reference point:** Anthropic reports about $13 per developer per active day as the enterprise average. A crew that costs much more than a single developer seat per finished story needs a reason.
- **Eval set:** freeze about 20 representative stories (Anthropic's early-eval size) and re-run them when you change models, effort or crew shape.

## 8. Updated starter repo structure

Changes from the blueprint are marked with `*`.

```text
ai-crew/
├── CLAUDE.md                      # <200 lines: commands, gotchas, where things live
├── AGENTS.md                    * # only if other agent tools join; CLAUDE.md then imports it
├── README.md                      # for humans
├── .gitignore                   * # CLAUDE.local.md, .env, worktree leftovers
├── .worktreeinclude             * # small git-ignored files copied into worktrees
├── .claude/
│   ├── settings.json              # deny/ask rules, Stop hook (tests), env: spawn depth 1
│   ├── agents/
│   │   ├── planner.md             # Sonnet, read + tracker tools
│   │   ├── executor.md            # Sonnet → Haiku for mechanical stories, no Agent tool
│   │   └── reviewer.md            # Opus, Read/Grep/Glob only, "skip style"
│   │                            * # lead.md and skill-auditor.md added only when metrics justify
│   ├── skills/
│   │   ├── story-refinement/SKILL.md
│   │   ├── dev-conventions/SKILL.md
│   │   ├── skill-audit/SKILL.md * # checklist the reviewer applies to PRs touching .claude/
│   │   └── release/SKILL.md     * # disable-model-invocation: true
│   └── rules/                   * # path-scoped rules instead of a growing CLAUDE.md
├── docs/
│   ├── specs/                   * # one SPEC.md per feature: the definition of done
│   ├── decisions/                 # ADRs (moved from backlog/decisions)
│   └── policies/                * # always-human.md, budgets.md, definition-of-ready.md
├── metrics/
│   └── cost-per-task.csv        * # one row per story
├── src/
├── tests/
└── .github/
    ├── CODEOWNERS               * # owner must approve .claude/**, workflows, assets
    ├── workflows/
    │   ├── ci.yml                 # required status check
    │   ├── claude.yml           * # @claude mentions
    │   ├── refine.yml             # label refine → planner
    │   └── execute.yml            # label ready → executor; attempt-n labels
    │                            * # triage.yml optional: a cloud scheduled task can replace it
    ├── ISSUE_TEMPLATE/story.yml * # issue form with required Definition of Ready fields
    └── pull_request_template.md
```

The blueprint's `backlog/` folder gives way to GitHub Issues plus `docs/`. If you choose Backlog.md instead, `backlog/tasks/` replaces the issue form and `docs/` stays as it is.

## 9. Rollout plan

| Phase | Add | Exit criterion |
| --- | --- | --- |
| 0. Foundations (this repo now) | Research, blueprints, spend limits at the provider, a decision on billing mode | Blueprint for the starter repo approved |
| 1. Single agent baseline | `CLAUDE.md`, `settings.json` (deny rules, Stop hook, spawn depth 1), CI, branch protection, `metrics/cost-per-task.csv` | ~20 stories done by one general agent, with cost per story logged |
| 2. Independent review | `reviewer.md`, `story-refinement` skill, `claude.yml` with timeouts and concurrency | Reviewer catches real defects without style noise |
| 3. Label automation and routing | `refine.yml`, `execute.yml`, issue form, `attempt-n` escalation; Haiku-vs-Sonnet routing test | Cost per merged story at or below the Phase 1 baseline |
| 4. Optional roles | `lead.md`, scheduled triage, `/batch` or dynamic workflows for large changes | Each addition shows a lower cost per task or a measurable quality gain; otherwise remove it |

## 10. Decisions for the owner

1. **Task board:** GitHub Issues + Projects (recommended) or Backlog.md?
2. **Billing for automation:** an API key in a dedicated Console workspace with a spend limit (recommended), or the subscription OAuth token?
3. **First real product:** the language and test framework decide `ci.yml`, the Stop hook and `dev-conventions`.
4. **Repo visibility:** private is recommended while agents have write access and secrets.

## Sources

Primary (official):

- [Claude Code: Best practices](https://code.claude.com/docs/en/best-practices): deterministic vs non-deterministic instructions, CLAUDE.md content test, Stop hook, deny rules, unattended runs, "what you can stop doing"
- [Claude Code: Create custom subagents](https://code.claude.com/docs/en/sub-agents): frontmatter fields, model resolution, spawn depth, best practices
- [Claude Code: Run agents in parallel](https://code.claude.com/docs/en/agents) and [Agent teams](https://code.claude.com/docs/en/agent-teams)
- [Claude Code: How Claude remembers your project](https://code.claude.com/docs/en/memory): CLAUDE.md size, AGENTS.md handling, path-scoped rules, auto memory
- [Claude Code: Skills](https://code.claude.com/docs/en/skills): frontmatter, content lifecycle, size guidance, Agent Skills standard
- [Claude Code: GitHub Actions](https://code.claude.com/docs/en/github-actions) and [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action), including [configuration](https://github.com/anthropics/claude-code-action/blob/main/docs/configuration.md)
- [Claude Code: Scheduled tasks](https://code.claude.com/docs/en/routines)
- [Claude Code: Manage costs](https://code.claude.com/docs/en/costs)
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Anthropic model pricing and cost-optimisation guidance (Claude API reference, cached Oct 2026)

Independent:

- Gloaguen, Mündler, Müller, Raychev, Vechev, [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) (ICLR 2026). Read via abstract and summaries; the full text was not reachable from this environment
- Cognition, [Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents) and [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working). Read via search excerpts; the pages were not reachable from this environment
- LangChain, [How and when to build multi-agent systems](https://blog.langchain.com/how-and-when-to-build-multi-agent-systems)
- [Backlog.md (MrLesk)](https://github.com/MrLesk/Backlog.md)

Caveat: prices and Claude Code features change quickly. The scheduled tasks, agent view and agent teams features cited here are in research preview or experimental. Re-check the linked docs before relying on a specific limit.
