# Etap 1: budowa

**Wyzwalacz:** ponad około 10 otwartych zadań albo pierwsza specyfikacja.

## Co dochodzi

| Element | Zasada |
| --- | --- |
| `work/` | Większe zadania i epiki dostają własny plik `T-NNN-tytul.md`. `BOARD.md` zostaje spisem z odnośnikami |
| `docs/specs/` | W projekcie z kodem obowiązkowo. W treściowym: opis formatu albo standardu, jeśli taki powstał |
| `.claude/skills/` | Skill powstaje **po trzecim powtórzeniu** tej samej procedury. Skill, który coś publikuje albo kasuje, ma `disable-model-invocation: true` |
| `.claude/rules/` | Reguły dotyczące tylko części repo (np. jednego folderu) wychodzą z `AGENTS.md` do reguł ścieżkowych |

## Szablon pliku zadania

```markdown
# T-NNN: tytuł

- Kto: lead | worker | codex | owner · Klasa: A | B | C · Stan: gotowe | w toku | zrobione
- Zależy od: T-…

## Cel
## Pliki
## Odbiór
- [ ] …
## Poza zakresem
## Notatki z pracy
(próby, pytania, odpowiedzi; najnowsze na dole)
```

## Zmiany w załodze

- **Poziom autonomii 2** (załoga sama scala klasę A): po pięciu kolejnych zmianach przyjętych przez Ownera bez poprawek. Zmiana poziomu to decyzja Ownera zapisana w `docs/decisions/` i w `AGENTS.md`.
- **Tryb (c):** jedno zaplanowane uruchomienie dziennie i stan tygodniowy. Treści poleceń: [`../automation/scheduled-tasks.md`](../automation/scheduled-tasks.md).
- **Hurt dla Wykonawcy:** dopiero teraz zwykle pojawia się go tyle, że delegowanie się opłaca.

## Sygnały, że etap 1 działa

Agent po „co dalej” bierze zadanie bez dopytywania. Owner czyta tylko sekcję „Czeka na Ownera”. Zwroty po recenzji są rzadsze niż co trzecie zadanie.
