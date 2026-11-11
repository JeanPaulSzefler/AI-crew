# Blueprint: starter-crew-repo

Startowa struktura repo dla nowego, małego projektu prowadzonego przez załogę AI pod nadzorem jednego Ownera. Uzasadnienie i źródła: [raport z 11.11.2026](../../outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md).

Wersja 1.0 · 11.11.2026 · status: propozycja do pilotażu

## Załoga w jednym akapicie

Prowadzi **Sonnet** w sesji głównej: rozmawia z Ownerem, planuje i sam wykonuje większość pracy. **Haiku** (subagent `worker`) dostaje małe, w pełni opisane zadania hurtowe. **Opus** (subagent `advisor`) daje drugą opinię w trzech momentach: koncepcja, wydanie, dwie nieudane próby. **Codex** jest niezależnym recenzentem, redaktorem tekstów dla ludzi i źródłem obrazów. Sprawy z listy „zawsze Owner” załatwia tylko Owner.

## Co tu jest

| Folder | Zawartość |
| --- | --- |
| [`core/`](core/) | Pliki wspólne dla każdego projektu: `AGENTS.md`, `CLAUDE.md`, `BOARD.md`, `JOURNAL.md`, `docs/`, ustawienia i agenci |
| [`variant-content/`](variant-content/README.md) | Dodatki dla projektu treściowego: test odnośników i indeksów, CI |
| [`variant-code/`](variant-code/README.md) | Dodatki dla projektu z kodem: specyfikacje, recenzent, CI |
| [`growth/`](growth/README.md) | Co dochodzi na kolejnych etapach: budowa, wydania, utrzymanie, operacje |
| [`automation/`](automation/) | Tryb bez Ownera ([zaplanowane zadania](automation/scheduled-tasks.md)) i [praca z Codex](automation/codex.md) |
| [`TASK-000-bootstrap.md`](TASK-000-bootstrap.md) | Zadanie startowe: jak postawić nowe repo z tego blueprintu |

Foldery `dot-claude` i `dot-github` oraz plik `dot-gitignore` to szablony. W docelowym repo nazywają się `.claude`, `.github` i `.gitignore`. Tu mają inne nazwy, żeby nie działały w tym repo i były widoczne w przeglądarce plików.

## Jak użyć

1. Utwórz puste repo i otwórz w nim sesję Claude (model Sonnet).
2. Napisz: „Wykonaj `TASK-000-bootstrap.md` z blueprintu `starter-crew-repo` w repo AI-crew. Projekt: …, wariant: …”.
3. Zaakceptuj PR. Od tej chwili praca idzie przez `BOARD.md`.

## Zasady, na których stoi blueprint

1. **Krótkie instrukcje, które ładują się wszędzie.** `AGENTS.md` i `CLAUDE.md` mają razem poniżej 200 linii. Tylko ta warstwa działa w każdej sesji, także z telefonu.
2. **Stan w plikach.** Tablica, dziennik, decyzje i odrzucone pomysły zastępują pamięć sesji.
3. **Test jest sędzią.** Jedna komenda, ta sama lokalnie i w CI.
4. **Jeden piszący, jeden poziom subagentów.**
5. **Załoga nie zmienia własnych zasad.** To zawsze Owner.
6. **Nic na zapas.** Każdy dodatkowy element ma wyzwalacz w [`growth/`](growth/README.md).

## Czego tu celowo nie ma

Skilli, osobnych plików zadań, arkusza kosztów, `CODEOWNERS`, formularzy zgłoszeń, folderu polityk, większej liczby agentów. Powody i moment dodania: rozdział 8 raportu oraz `growth/`.

## Kiedy zmienić blueprint

Po każdym pilotażu i po zmianie założeń (plan subskrypcji, limity, nowe modele, nowe funkcje narzędzi). Sygnały i zmiany: rozdział 10 raportu. Zmiana blueprintu to zadanie na tablicy repo `AI-crew`.
