# Wariant z kodem

Dla projektów, których wynikiem jest działający program: aplikacja, gra, narzędzie, strona z logiką. Dokłada się do [`core/`](../core/).

## Co dochodzi

| Element | Po co |
| --- | --- |
| `src/`, `tests/` | Kod i testy. Nazwy według zwyczaju danej technologii |
| [`docs/specs/`](docs/specs/README.md) | Najpierw specyfikacja z numerowanymi klauzulami, potem kod i test, który przywołuje klauzulę |
| [`dot-claude/agents/reviewer.md`](dot-claude/agents/reviewer.md) | Recenzent ze świeżym kontekstem (Sonnet, tylko odczyt) przed oddaniem PR Ownerowi |
| [`dot-github/workflows/check.yml`](dot-github/workflows/check.yml) | Testy przy każdym PR i każdej zmianie na gałęzi głównej |

Jeśli projekt ma własny format plików z danymi (np. pytania, poziomy, utwory), od razu dodaj trójkę: **schemat, instrukcję dla agenta i walidator**. Walidator wchodzi do komendy sprawdzającej.

## Co dopisać do `AGENTS.md`

W „Commands” prawdziwe komendy: instalacja, test, lint, uruchomienie. W „How work is done”:

```markdown
- Spec first: a behaviour change starts as a change in `docs/specs/`, approved by the owner.
- Every bug fix adds a test that fails without the fix.
- Tests and commits cite the spec clause (for example `SPEC-003.4`).
```

W `.claude/settings.json` warto dodać listę `allow` z komendami testów (np. `"Bash(npm test *)"`), żeby agent nie pytał o zgodę przy każdym uruchomieniu.

## Typowy podział pracy

| Praca | Kto |
| --- | --- |
| Specyfikacja, plan, implementacja, testy | Prowadzący (Sonnet) |
| Hurt: zmiana nazw, konwersje danych, uzupełnianie prostych testów według wzoru | Wykonawca (Haiku) |
| Architektura na starcie, ocena przed wydaniem, odblokowanie po dwóch porażkach | Doradca (Opus) |
| Recenzja przed PR | `reviewer` (Sonnet), a przed wydaniem także Codex |
| Scalanie klasy B, wydanie | Owner |

## Praca wymagająca komputera

Zadania, których nie da się wykonać w chmurze (np. podpisana paczka `.apk`), dostają na tablicy dopisek „wymaga komputera”. Załoga przygotowuje wszystko do tego kroku i opisuje go w zadaniu tak, żeby Owner wykonał go jedną komendą.
