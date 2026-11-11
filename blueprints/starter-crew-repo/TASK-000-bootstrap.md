---
id: TASK-000
title: Postawienie nowego repo z blueprintu starter-crew-repo
role: lead (Sonnet), advisor (Opus) raz, owner
class: B
---

# TASK-000: nowe repo z blueprintu

## Cel

Puste repozytorium zostaje przygotowane do pracy załogi: zasady, tablica, test i role. Bez treści i bez kodu projektu.

## Wejście od Ownera

- Nazwa projektu i jedno–trzy zdania: po co i dla kogo.
- Wariant: treściowy albo z kodem.
- Widoczność repo (publiczne albo prywatne) i nazwa gałęzi głównej.

## Kroki Ownera

1. Utworzyć puste repo na GitHubie i podłączyć je do sesji Claude. **Jedno repo na sesję.**
2. Po akceptacji PR: w repo publicznym włączyć ochronę gałęzi głównej (wymagany test `check`). W prywatnym na planie Free ochrona nie działa; zostają zasady z `AGENTS.md` i reguły `ask`.
3. Opcjonalnie: podłączyć repo w Codex i włączyć automatyczne recenzje.

## Kroki Prowadzącego (jeden PR)

1. Skopiować `core/` do katalogu głównego repo. Zmienić nazwy: `dot-claude` → `.claude`, `dot-gitignore` → `.gitignore`.
2. Dołożyć pliki wybranego wariantu (`variant-content/` albo `variant-code/`) **bez jego `README.md`**, który jest tylko instrukcją. Zmienić `dot-github` → `.github`, a w wariancie z kodem dołożyć `dot-claude/agents/reviewer.md` do `.claude/agents/`.
3. Wypełnić wszystkie pola `{{…}}` w `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/brief.md`, `BOARD.md`, `JOURNAL.md`. Dopisać do `AGENTS.md` wiersze i zasady z README wariantu.
4. Ustawić komendę testu w `AGENTS.md` i w `.github/workflows/check.yml`. Uruchomić ją. Musi przejść.
5. Zapisać decyzję `0001`: wariant, poziom autonomii 1, założenia (subskrypcje, miejsce pracy) z warunkami powrotu.
6. Wpisać do `BOARD.md` trzy–pięć pierwszych zadań w „Gotowe do wzięcia”, każde z celem, plikami, odbiorem i klasą.
7. **Jedna konsultacja z Doradcą:** brief na jedną stronę z `docs/brief.md` i listą pierwszych zadań. Pytanie: czy zakres i kolejność mają sens, co jest największym ryzykiem. Werdykt dopisać do `JOURNAL.md`.
8. Otworzyć PR dla Ownera.

## Odbiór

- [ ] W repo nie ma żadnego `{{` poza blokami przykładów.
- [ ] `AGENTS.md` i `CLAUDE.md` mają razem mniej niż 200 linii.
- [ ] Komenda testu przechodzi lokalnie i w CI.
- [ ] `.claude/settings.json` jest poprawnym JSON-em z regułami `deny`, `ask` i limitem zagnieżdżenia subagentów.
- [ ] `advisor.md` ma tylko narzędzia odczytu.
- [ ] `BOARD.md` ma co najmniej trzy gotowe zadania.
- [ ] Owner zaakceptował PR.

## Poza zakresem

Treść i kod projektu, skille, zaplanowane zadania (etap 1), wydania (etap 2), sekrety i konta.
