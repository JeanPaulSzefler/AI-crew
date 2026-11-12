# Project brief: AI-crew

One page. The owner approves changes. Translated to English on 2026-11-12 (decision 0010); the content is unchanged.

## Why

The owner runs several small projects with the help of AI agents. This repository works out **the concept of an AI crew and ready repository structures** that can be copied into a new project, so that the crew works effectively and as independently as possible on a small budget.

## What success is

- A new project can be set up from the blueprint in one session and run from the task board at once.
- The owner works mainly from the phone: states a goal, comes back to a finished change, answers questions in one place.
- The blueprint changes after pilots and when assumptions change, and every change has a recorded reason.

## Scope

- **In:** research, reports, recommendations, repository blueprints, lessons from pilots in generalised form.
- **Out:** diagnoses or plans of the owner's existing projects; application code; anything that reveals details of private projects. Details: `docs/out-of-scope/`.

## Assumptions

A reference point, not a constant. Each assumption has a condition for revisiting it.

| Assumption | Revisit when |
| --- | --- |
| Subscriptions: Claude Pro and ChatGPT Plus, no paid API (decision 0006) | The plan or the limits change |
| Day-to-day models: Sonnet and Haiku; Opus only at set moments | A new model appears or the limits change |
| Where work happens: cloud sessions started from the mobile app; a computer only for local work | Work appears that the cloud cannot do |
| GitHub on the Free plan | A move to a paid plan |
| Target projects differ: content and code | One type becomes dominant |

## Always the owner

The list is in [`AGENTS.md`](../AGENTS.md#always-the-owner-class-c). Addition for this repository: everything that concerns the owner's other repositories.
