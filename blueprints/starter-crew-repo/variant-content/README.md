# Wariant treściowy

Dla projektów, których wynikiem są teksty, raporty, materiały do nauki, wpisy, grafiki. Dokłada się do [`core/`](../core/).

## Co dochodzi

| Element | Po co |
| --- | --- |
| `sources/` | Surowe materiały w oryginalnej postaci. **Tylko odczyt**: agent ich nie zmienia. Poprawki trafiają do treści pochodnych z notatką, co w źródle było błędne |
| Foldery na gotowe treści (np. `outputs/`, `wiki/`, `posts/`) | Każdy ma `README.md` z indeksem plików. Nazwy plików zaczynają się od daty, jeśli kolejność ma znaczenie |
| [`tools/check.py`](tools/check.py) | Jedna komenda sprawdzająca: odnośniki, indeksy folderów, unikalne numery zadań i decyzji, długość plików instrukcji, poprawność `settings.json` |
| [`dot-github/workflows/check.yml`](dot-github/workflows/check.yml) | Ta sama komenda przy każdym PR i każdej zmianie na gałęzi głównej |

## Co dopisać do `AGENTS.md`

W tabeli „Map” wiersze dla `sources/` i folderów z treścią. W sekcji „Safety”:

```markdown
- Every claim in a deliverable cites its source, or is marked `UNVERIFIED`.
- Never edit files in `sources/`.
- Text for people: plain words, short sentences, no filler. Owner approves before anything is published.
```

W `.claude/settings.json` do listy `ask` warto dodać `"Edit(/sources/**)"`. Wtedy dodanie albo zmiana surowego pliku wymaga zgody Ownera.

## Ustawienia `check.py`

Na górze pliku są trzy listy: foldery pomijane przy sprawdzaniu odnośników, foldery z obowiązkowym indeksem i pliki instrukcji z limitem linii. Zmiana tego pliku należy do Ownera (klasa C).

## Typowy podział pracy

| Praca | Kto |
| --- | --- |
| Research, szkic, układ treści | Prowadzący (Sonnet) |
| Hurtowe poprawki formatu, indeksy, odnośniki, konwersje | Wykonawca (Haiku) |
| Ocena koncepcji albo struktury całości | Doradca (Opus) |
| Redakcja tekstu dla ludzi, obrazy, niezależna recenzja | Codex |
| Publikacja | Owner |
