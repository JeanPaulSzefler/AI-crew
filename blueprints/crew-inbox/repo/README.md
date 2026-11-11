# crew-inbox

Prywatna skrzynka na pomysły między projektami. Załoga pracująca w jednym repo zapisuje u siebie notatkę dla innego projektu. Skrzynka zbiera te notatki w jedno miejsce, a każdy projekt czyta tylko swój plik.

To jest spis, nie tablica zadań. O tym, czy pomysł zostaje zadaniem, decyduje Owner w repo docelowym.

## Jak używać z telefonu

| Chcę… | Co zrobić |
| --- | --- |
| zebrać nowe notatki | Sesja w tym repo (model Haiku), wiadomość: „zbierz notatki” |
| odebrać notatki w projekcie | Sesja w repo projektu, wiadomość: „zabierz notatki ze skrzynki” |
| podłączyć kolejne repo | Sesja w tym repo, wiadomość: „podłącz repo właściciel/nazwa, prywatne” (albo „publiczne”) |
| zobaczyć wszystko | [`index.md`](index.md) |

## Podłączenie repo

1. W repo projektu musi istnieć skrzynka nadawcza: sekcja „Dla innych projektów” w `BOARD.md`. Repo bez tablicy może mieć plik `OUTBOX.md` z tym samym nagłówkiem sekcji. Dodaje ją sesja tamtego repo.
2. W [`repos.md`](repos.md) dochodzi wiersz: repo, widoczność, plik.

Format notatki w skrzynce nadawczej:

```text
## Dla innych projektów

- N-nazwarepo-001 · dla: nazwa-repo · RRRR-MM-DD
      Co zauważyłem: … Dlaczego to ważne: … Gdzie to widać: plik albo miejsce.
```

## Pliki

| Plik | Co zawiera |
| --- | --- |
| [`repos.md`](repos.md) | Podłączone repo |
| [`index.md`](index.md) | Wszystkie zebrane notatki ze źródłem |
| [`for/`](for/README.md) | Jeden plik na repo docelowe |
| [`JOURNAL.md`](JOURNAL.md) | Jedna linia na każde zbieranie |
| `tools/collect.py`, `tools/check.py` | Zbieranie i test |

## Prywatność

To repo jest prywatne i zawiera nazwy prywatnych projektów. Plik `for/<repo>.md` repo publicznego nie podaje, skąd pochodzi notatka. Treść notatki pisze załoga źródłowa; dla repo publicznego ma być uogólniona.
