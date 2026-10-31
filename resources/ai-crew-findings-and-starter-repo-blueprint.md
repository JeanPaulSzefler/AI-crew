# AI Crew: Findings and Starter Repo Blueprint

Oct 31, 2026 · @JP

## Executive summary

An AI Crew pays off as supervised fast prototyping, not as an autonomous business. Start flat and small, route models by task difficulty, and let tests and the owner judge the output.

- **Structure:** a flat, two-level crew. A planner, one general executor with role skills, a mechanical worker and a gate reviewer. No middle-management layer of "directors".
- **Model tiering:** Sonnet refines and supervises, Haiku executes only atomic ready stories, Opus is an escalation and consultation tier. Choose the model per task, not per rank.
- **Hiring:** the planner may propose new agents or skills as pull requests. A skill auditor and the owner approve them; reuse comes before creation.
- **Coordination:** keep tasks in the repo (Backlog.md) or GitHub Issues + Projects. Jira adds cost and a second source of truth for a small team.
- **Triggers:** GitHub Actions with the official Claude Code action covers labels, mentions, assignment and schedules. n8n bridges events from outside GitHub.
- **Guardrails:** hard spend limits, capped retries with escalation, file-based handoffs, tests and CI as the judge, and a fixed list of decisions that always go to a human.

## Source case: an AI Crew running a 3D-print shop

The GeekWork video by Michał Barczak ran a print-on-demand fishing-accessories shop with an AI Crew for three months. Its value is in the guardrails it exposed, not in the corporate role structure. Details come from a Gemini summary of the video, not a verbatim transcript, so figures should be checked against the video.

**Setup:** four role agents (CEO, CTO, CMO, Researcher) orchestrated by Paperclip, with long-term memory in Hindsight. Stack: Hostinger VPS, WordPress/WooCommerce, Claude Code, Google Ads API, MCP. Ad budget about 3,000 PLN.

| Lesson | What happened | Takeaway |
| --- | --- | --- |
| Runaway cost | A code-fix loop burned over 200 USD of tokens in under two days | Hard spend caps at the API provider and on ad accounts |
| Licensing blind spot | Agents picked free 3D models without checking Creative Commons NC terms | A human verifies the licence of every product |
| Proxy metrics | The marketing agent optimised CTR and CPC, not profit | KPIs on gross margin, with unit economics computed first |
| Persistent memory | Chat sessions lose context | Decisions stored with their reasons and reused |
| Speed | Idea to working shop in days rather than weeks | The real benefit: supervised fast prototyping |

**Critique:** a CEO agent on the same model as the team shares its blind spots, so it adds tokens rather than independent judgement. A reviewer with a different prompt or model and explicit criteria does that job better.

## Team structure and model tiering

A flat crew with escalation beats a corporate pyramid: every extra management layer is another handoff that costs tokens and loses nuance. The model is chosen by task difficulty, so the same worker may run on Haiku or Sonnet.

&#91;embedded content: AI Crew task flow · 3 model tiers, CI as judge, 2 escalation paths\]

Haiku carries most tokens on atomic stories; failures climb to Sonnet, then Opus, while money, licences and publishing always reach the owner.

| Role | Model | Does | Never does |
| --- | --- | --- | --- |
| Owner (human) | n/a | Approves goals, spend, publishing, licences, new roles | Reviews every story |
| Lead | Opus, short sessions | Unblocks what Sonnet cannot; decides grey-zone escalations | Runs continuously as a "CEO" |
| Planner / refiner | Sonnet | Breaks goals into ready stories; answers worker questions; rewrites failed stories | Implements large tasks itself by default |
| Executor | Haiku (Sonnet for hard code) | Implements one ready story with its tests | Takes vague or oversized tasks |
| Reviewer | Sonnet or Opus, different prompt | Checks gates against explicit criteria | Reviews every step |

**Why not "directors" on Sonnet and developers on Haiku:** a pass-through management layer pays tokens for relaying. Haiku on non-trivial code fails more often, and fix loops cost more than getting it right on Sonnet the first time.

**Agent "hiring":** the planner proposes a new agent or skill as a file in a pull request. The skill auditor checks cost and safety, and the owner approves. An existing skill is always reused first.

## Coordination: tracker and triggers

Keep the task board next to the code: Backlog.md for a git-native crew, GitHub Issues + Projects when people collaborate too. Jira is only worth it to learn it or to match an existing team.

| Tool | Fits when | Watch out for |
| --- | --- | --- |
| [Backlog.md](https://github.com/MrLesk/Backlog.md) (MIT) | Everyone works in git; tasks as Markdown files in the repo, CLI, MCP for Claude Code, terminal and web kanban | No notifications; file conflicts with many parallel agents |
| GitHub Issues + Projects | Mixed human and agent team; issues link to PRs and close on merge | Non-technical members may need onboarding |
| [Plane](https://wz-it.com/en/blog/jira-alternatives-openproject-plane-vikunja-comparison/) (AGPL-3.0) | A Jira-like UI for non-developers; cloud or self-hosted | Extra system plus a webhook bridge to GitHub |
| Vikunja | Simple task lists for a small team | Not a full Jira replacement |
| Jira | Learning it, or an existing Jira team | Verbose JSON per call, a second source of truth, licence |

**If Jira is used:** request only needed fields via JQL and the `fields` parameter, and wrap it in a small CLI that returns a few lines of text per command, documented in a skill.

**Starting agents:** the official [anthropics/claude-code-action](https://x-cmd.com/install/claude-code-action) runs a full Claude Code session on GitHub events. It reacts to an @claude mention, issue assignment or a label such as `ready` ([parameters](https://github.com/gmh5225/claude-code-action)). With a fixed prompt it runs in automation mode on any GitHub event, including schedules ([modes](https://jannikreinhard.com/claude-code-github-actions/)).

| Trigger | Mechanism | Example |
| --- | --- | --- |
| Label `refine` | GitHub Action, Sonnet | Turn a rough issue into a ready story |
| Label `ready` | GitHub Action, Haiku | Implement the story and open a PR |
| Daily schedule | Action `schedule`, or a Claude scheduled task | Sonnet triages and grooms the backlog |
| Event outside GitHub | n8n webhook to an Action or a headless agent | Shop order, email or Plane change |

Each run consumes Actions minutes and API tokens ([Steve Kinney](https://stevekinney.com/courses/ai-development/integrating-with-github-actions)), so set `timeout-minutes` and a `concurrency` group that cancels stale runs ([noqta](https://www.noqta.tn/en/blog/claude-code-ci-cd)). Only collaborators' mentions trigger the action by default, which blocks outside prompt injection.

## Operating rules: cheaper than one or two general agents

The baseline is one or two general agents with skills and specs in the repo; the crew must beat its cost per finished task or be cut back.

1. **Single agent by default.** Spawn a separate agent only for parallel work, a clean context, or an independent review.
2. **Two levels maximum.** Subagents never spawn subagents; cap concurrent agents.
3. **Files, not conversations.** Spec, story and result live in the repo in a fixed format; agents do not chat with each other.
4. **Minimal context.** Each agent gets only the files it needs; CLAUDE.md stays short; skills load on demand.
5. **Definition of Ready for Haiku.** Files to change, acceptance criteria, the test command, small size. A story that fails this goes back to refinement.
6. **One question per story.** A second question means Sonnet rewrites or splits the story instead of answering.
7. **Capped retries, then escalate.** Two failed attempts move the story up: Haiku, Sonnet, Opus, owner.
8. **Tests and CI are the judge.** Model review happens at gates (merge, publish, spend), never after every step.
9. **Hard budgets.** Spend caps at the API provider, per-task budgets, ad-account limits, Action timeouts.
10. **Always-human list by rule.** Money, licences, publishing and irreversible actions go to the owner directly; Opus only rules on the grey zone.
11. **Decisions as files.** Record each decision with its reason in the repo (ADRs) before adding an external memory system.
12. **Measure and prune.** Track cost per completed task against the single-agent baseline; remove roles that do not pay off.

On a subscription rather than the API, Opus drains usage limits fastest, which is one more reason to keep it in short, rare sessions.

## Recommended starter repo structure

One repo holds the crew's rules, roles, tasks, decisions and code, so every agent and person reads the same source of truth. Start with four agent definitions and a handful of skills; add more only through the hiring PR flow.

```text
ai-crew/
├── CLAUDE.md                 # short: mission, rules, where things live
├── README.md                 # for humans: how to work with the crew
├── .claude/
│   ├── settings.json         # permissions, allowed tools
│   ├── agents/
│   │   ├── planner.md        # Sonnet: refine, answer, split stories
│   │   ├── executor.md       # Haiku: one ready story at a time
│   │   ├── reviewer.md       # gate checks against criteria
│   │   ├── lead.md           # Opus: escalations only
│   │   └── skill-auditor.md  # vets new agents and skills
│   └── skills/
│       ├── story-refinement/SKILL.md
│       ├── dev-conventions/SKILL.md
│       └── marketing/SKILL.md     # a role as a skill, not an agent
├── backlog/                  # Backlog.md: tasks, docs, decisions
│   ├── tasks/
│   ├── docs/
│   └── decisions/            # ADRs: decision + reason
├── policies/
│   ├── always-human.md       # money, licences, publishing, irreversible
│   ├── budgets.md            # spend caps per task and per month
│   └── definition-of-ready.md
├── src/
├── tests/
└── .github/
    ├── workflows/
    │   ├── ci.yml            # tests on every push and PR
    │   ├── refine.yml        # label refine: planner
    │   ├── execute.yml       # label ready: executor
    │   └── triage.yml        # daily schedule: backlog grooming
    ├── ISSUE_TEMPLATE/story.md
    └── pull_request_template.md
```

| Piece | Why it is there | Rule it enforces |
| --- | --- | --- |
| `CLAUDE.md` | Every session starts here | Kept under a page; details live in skills and policies |
| `.claude/agents/` | Four roles with fixed models and tool lists | No agent without an approved PR |
| `.claude/skills/` | Roles and know-how loaded on demand | Reuse before creating a new agent |
| `backlog/` | Tasks and decisions as Markdown in git | Agents talk through files, not chat |
| `policies/` | Human-written limits agents must read | Always-human list, budgets, Definition of Ready |
| `tests/` + `ci.yml` | Objective judge of Haiku's work | Red build sends the story back |
| Workflows | Labels and schedules start agents | Timeouts and concurrency on every workflow |

**Rollout in three steps:** first run one general agent on this repo with skills and CI. Add the label-triggered planner and executor once stories routinely pass the Definition of Ready. Add the lead and the daily triage only when the cost-per-task numbers show they pay off.

## Next steps

- [ ] Create the repo skeleton above and a short CLAUDE.md
- [ ] Install Backlog.md and connect it to Claude Code over MCP
- [ ] Write the three policy files: always-human list, budgets, Definition of Ready
- [ ] Set spend caps at the API provider before any automation runs
- [ ] Add a first test suite and the `ci.yml` workflow
- [ ] Write the planner and executor agent definitions and run them manually on a few stories
- [ ] Add the `refine` and `ready` label workflows with timeouts and concurrency
- [ ] Log cost per completed task and compare it with the single-agent baseline after two weeks

## Sources

- Michał Barczak (GeekWork), "Oddałem SKLEP agentom AI na 3 miesiące - co się stało?", [YouTube](https://youtu.be/UYwMKxjMyHo), via a Gemini-written summary
- [Backlog.md, GitHub (MrLesk)](https://github.com/MrLesk/Backlog.md)
- [Backlog.md README (fork, saada)](https://github.com/saada/Backlog.md)
- [Backlog.md CLI reference (fork, janbam)](https://github.com/janbam/backlog.md)
- [claude-code-action overview, x-cmd](https://x-cmd.com/install/claude-code-action)
- [claude-code-action trigger parameters (fork, gmh5225)](https://github.com/gmh5225/claude-code-action)
- [Jannik Reinhard, Claude Code in GitHub Actions](https://jannikreinhard.com/claude-code-github-actions/)
- [noqta, Claude Code in CI/CD](https://www.noqta.tn/en/blog/claude-code-ci-cd)
- [Steve Kinney, Integrating with GitHub Actions](https://stevekinney.com/courses/ai-development/integrating-with-github-actions)
- [WZ-IT, OpenProject, Plane and Vikunja compared](https://wz-it.com/en/blog/jira-alternatives-openproject-plane-vikunja-comparison/)
- [computingforgeeks, Plane as a Jira alternative](https://computingforgeeks.com/plane-project-management-tool)
