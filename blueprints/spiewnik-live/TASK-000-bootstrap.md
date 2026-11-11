---
id: TASK-000
title: Utworzenie repozytorium śpiewnika na żywo ze strukturą AI-crew
status: draft (czeka na odpowiedzi Ownera: nazwa, widoczność, pilotaż AI-crew)
role: executor (Sonnet), reviewer (Opus albo Codex), owner
created: 2026-11-08
depends_on: [odpowiedzi na pytania 14, 15, 17 z raportu]
source: ../../outputs/2026-11-08-spiewnik-live-wymagania-v1.md
---

# TASK-000: utworzenie repo i struktury AI-crew

## Cel

Puste repozytorium aplikacji „śpiewnik na żywo” (nazwa robocza `spiewnik-live`) zostaje przygotowane do pracy zespołu AI-crew. Zadanie tworzy **tylko strukturę, zasady i CI**, bez kodu aplikacji. Pierwsze zadania merytoryczne (T-001, T-002, T-010) mogą ruszyć zaraz po nim.

## Kontekst

- Wymagania wstępne i plan zadań: [`outputs/2026-11-08-spiewnik-live-wymagania-v1.md`](../../outputs/2026-11-08-spiewnik-live-wymagania-v1.md).
- Struktura i zasady crew:
  - [raport AI-crew z 31.10, sekcja 8](../../outputs/2026-10-31-efficient-ai-crew-and-repo-setup.md#8-updated-starter-repo-structure);
  - [raport z 7.11, wersja 3.1](../../outputs/2026-11-07-orkiestracja-agentow-i-hosting-v3.md): bezpieczeństwo agentów, GitHub Actions, koszty.
- Wzorzec standardu pliku dla agentów: standard z aplikacji Exam Drill (schemat, instrukcja dla agenta, walidator).

## Kroki Ownera (przed i po)

1. Utworzyć puste repo na GitHubie (nazwa i widoczność według odpowiedzi; rekomendacja: prywatne) albo zlecić to Claude'owi.
2. Podłączyć repo do sesji Claude Code.
3. Po scaleniu PR tego zadania:
   - włączyć ochronę gałęzi `main` (wymagany zielony CI i akceptacja Ownera);
   - ustawić `CODEOWNERS`, jeśli GitHub wymaga potwierdzenia.
4. Nie dodawać jeszcze żadnych sekretów (Cloudflare, Google). Przyjdą w T-040.

## Kroki wykonawcy (jeden PR)

Utworzyć poniższe pliki. Treści zwięzłe; `CLAUDE.md` poniżej 200 linii; bez architektury, którą agent sam wyczyta z repo.

```text
spiewnik-live/
├── CLAUDE.md                     # komendy (install, test, lint, validate), zasady pracy, gdzie co leży
├── README.md                     # dla ludzi: czym jest projekt, status, jak uruchomić
├── .gitignore                    # node_modules, dist, .env*, CLAUDE.local.md, .wrangler
├── .claude/
│   ├── settings.json             # deny: Read(.env*), Read(secrets/**); ask: git push, wrangler deploy;
│   │                             # env: CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1; Stop hook: npm test (gdy istnieje)
│   ├── agents/
│   │   ├── planner.md            # Sonnet: specyfikacje, zadania gotowe do pracy, odpowiedzi na pytania
│   │   ├── executor.md           # Sonnet: jedno gotowe zadanie = jeden PR, z testami; bez narzędzia Agent
│   │   └── reviewer.md           # tylko Read/Grep/Glob; ocena względem specyfikacji; „pomiń styl”
│   └── skills/
│       ├── spec-change/SKILL.md  # zmiana zachowania zaczyna się od specyfikacji (wzór: Exam Drill)
│       ├── song-format/SKILL.md  # jak tworzyć i walidować pliki śpiewnika (odsyła do format/)
│       └── journal/SKILL.md      # gdzie zapisać decyzję, odrzucony pomysł, wniosek
├── docs/
│   ├── specs/SPEC-000-wizja.md   # na start: kopia sekcji 1–3 raportu jako szkic; Owner zatwierdza w T-001
│   ├── decisions/README.md       # format ADR: numer, data, decyzja, powód, warunek powrotu; bez edycji po przyjęciu
│   ├── out-of-scope/README.md    # odrzucone pomysły z powodem (wzór: Exam Drill)
│   └── policies/
│       ├── always-human.md       # publikacja, wydatki, konta, prawa do tekstów, upublicznienie repo: tylko Owner
│       ├── budgets.md            # limity: tury i czas zadań, budżet API, minuty Actions
│       └── definition-of-ready.md# pliki do zmiany, kryteria odbioru, komenda testów, mały rozmiar
├── format/
│   ├── README.md                 # miejsce na schemat i instrukcje (wypełnia T-010 i T-012)
│   └── examples/README.md        # zasada: tylko teksty zastępcze lub z domeny publicznej
├── metrics/cost-per-task.csv     # nagłówek: task,model,effort,attempts,tokens,usd,merged,rework
├── JOURNAL.md                    # dziennik: co zrobiono, czego się nauczono (najnowsze na dole)
├── BOARD.md                      # tablica: etapy 0–5 i zadania T-001…T-055 z raportu, statusy
└── .github/
    ├── CODEOWNERS                # Owner dla .claude/**, .github/**, docs/policies/**
    ├── pull_request_template.md  # zadanie, specyfikacja (klauzula), testy (komenda + wynik), ryzyka
    ├── ISSUE_TEMPLATE/story.yml  # formularz z polami Definition of Ready (wymagane)
    └── workflows/
        └── ci.yml                # na push i PR: sprawdzenie Markdown i JSON; timeout-minutes; concurrency
```

Zasady do zapisania w `CLAUDE.md`:

- najpierw specyfikacja; jedno zadanie = jeden PR = jeden commit tematyczny;
- testy i CI są sędzią; dwie nieudane próby oznaczają eskalację do planisty, potem do Ownera;
- treści utworów w repo tylko zastępcze lub z domeny publicznej;
- agenci nie wdrażają na produkcję i nie dodają sekretów;
- odpowiedzi i dokumenty po polsku; kod, identyfikatory i komunikaty commitów po angielsku (do potwierdzenia przez Ownera).

## Kryteria odbioru

- [ ] Wszystkie pliki z listy istnieją i mają treść (bez „TODO” w `CLAUDE.md`, `policies/` i definicjach agentów).
- [ ] `CLAUDE.md` ma poniżej 200 linii.
- [ ] `.claude/settings.json` jest poprawnym JSON-em i zawiera reguły deny, ask i limit zagnieżdżenia subagentów.
- [ ] `reviewer.md` ma `tools: Read, Grep, Glob`.
- [ ] CI uruchamia się na PR i przechodzi; job ma `timeout-minutes` i grupę `concurrency`.
- [ ] `BOARD.md` zawiera zadania T-001…T-055 z raportu, wszystkie w stanie „do zrobienia”.
- [ ] Recenzent (inny model niż wykonawca) zaakceptował PR; Owner scalił.

## Poza zakresem

Kod aplikacji, wybór frameworka (T-002), konfiguracja Cloudflare (T-040), sekrety, domena.
