# Tryb (c): załoga startuje bez Ownera

Dwa zaplanowane zadania w chmurze Claude Code. Każde uruchomienie to zwykła sesja chmurowa: zużywa ten sam limit subskrypcji co praca ręczna.

## Jak włączyć (z telefonu)

1. Otwórz sesję Claude w tym repo i napisz: „Utwórz zaplanowane zadanie według `automation/scheduled-tasks.md`”. Albo wejdź na `claude.ai/code/routines` i wybierz „New task”.
2. Ustaw: **model Sonnet**, to jedno repo, środowisko chmurowe, harmonogram.
3. W konektorach zostaw tylko potrzebne (zwykle GitHub). Uruchomienie może używać każdego dołączonego konektora, także do zapisu.
4. Włącz powiadomienie push o zakończeniu.

Włączenie, zmiana i wyłączenie zaplanowanego zadania to decyzja Ownera.

## Zadanie 1: codzienna praca

Harmonogram: raz dziennie, poza godzinami, w których Owner sam pracuje z Claude.

```text
You are the lead of this repository's crew in an unattended run.
Read AGENTS.md and CLAUDE.md first and follow them.

0. If a crew pull request from an earlier run is still open: do not start new
   tasks. Act only on the owner's comments in it, then end.
1. Open BOARD.md. If the owner answered something under "Czeka na Ownera",
   act on the answer first.
2. Resume first: a task under "W toku" that you hold and that is paused
   ("wstrzymane: limit") or now has the owner's answer continues from its
   state file in work/.
3. Then take new tasks from "Gotowe do wzięcia" assigned to lead or worker,
   top first, so that this run handles at most 2 tasks in total. Skip
   class C and tasks marked "wymaga komputera".
4. Work on one branch for this run. After every step: update the task's
   state file if it has one, commit with the task id, push. Run the check.
5. Two failed attempts at a task: stop it, write what you tried in its state
   file, go on to the next.
6. Missing information: write the question under "Czeka na Ownera" and go on.
   Do not guess.
7. Last commit: update BOARD.md and add one line per task to JOURNAL.md.
8. Class A only, at autonomy level 2: merge. Otherwise open one pull request
   for the owner with a short summary in Polish.
If there is nothing to resume and no ready task, end without changes.
```

## Zadanie 2: stan tygodniowy

Harmonogram: raz w tygodniu.

```text
Unattended weekly status for this repository. Read AGENTS.md first.
Do not start any task.

Add an entry at the bottom of JOURNAL.md under today's date, in Polish,
at most 15 lines:
- five numbers for the last 7 days: tasks finished, changes returned after
  review, advisor consultations, questions to the owner, limit hits. Use
  JOURNAL.md, BOARD.md and the git log. Write "brak danych" where you cannot tell.
- what is waiting for the owner, oldest first.
- one thing that went wrong or was slow, with a proposed fix.
- notes added to "Dla innych projektów" in the last 7 days, and ideas marked
  "z zewnątrz" that still have no decision.
Add up to three proposed next tasks to "Pomysły" in BOARD.md.
Commit according to the repository's autonomy level.
```

## Bezpieczniki

| Ryzyko | Zabezpieczenie |
| --- | --- |
| Uruchomienie zużywa limit potrzebny Ownerowi | Jedno uruchomienie dziennie, najwyżej dwa zadania, pora poza pracą Ownera |
| Zmiany piętrzą się bez przeglądu | Krok 0: otwarty PR załogi wstrzymuje nowe zadania |
| Agent robi coś z listy „zawsze Owner” | Klasa C wykluczona w poleceniu i w `AGENTS.md`; reguły `ask` zatrzymują sesję do decyzji |
| Agent utknie | Stop po dwóch nieudanych próbach, pytanie do kolejki, następne zadanie |
| Limit przerwie uruchomienie w połowie | Punkt kontrolny po każdym kroku; następne uruchomienie zaczyna od wznowienia |
| Brak gotowych zadań | Uruchomienie kończy się bez zmian |

Po przekroczeniu limitu subskrypcji kolejne uruchomienia są odrzucane do odnowienia okna. Bez włączonych dodatkowych kredytów nie powstaje dodatkowy koszt.

## Przegląd po miesiącu

Zostawić, zmienić częstotliwość albo wyłączyć. Podstawa: pięć liczb ze stanów tygodniowych i odpowiedź na pytanie, czy Owner częściej przyjmował zmiany, czy je poprawiał.
