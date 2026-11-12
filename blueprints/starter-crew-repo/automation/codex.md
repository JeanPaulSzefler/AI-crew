# Codex w załodze

Codex (ChatGPT) jest niezależnym uczestnikiem: nie podlega Prowadzącemu i ma inne „ślepe plamy” niż modele Claude. Zasady czyta z tego samego pliku co wszyscy: `AGENTS.md`.

## Do czego

| Zadanie | Kiedy obowiązkowo | Wynik |
| --- | --- | --- |
| Recenzja zmian | Przed wydaniem i przed publikacją tekstu. Zalecana przy klasie B | Recenzja w PR |
| Redakcja tekstów dla ludzi | Każdy tekst, który wychodzi na zewnątrz | PR z poprawionym tekstem |
| Obrazy | Na zamówienie z tablicy | Pliki w repo przez PR |

## Jak przekazać pracę

**Recenzja:** komentarz w PR:

```text
@codex review
```

Po `review` można dopisać, na czym się skupić. Codex stosuje sekcję „Review guidelines” z `AGENTS.md`. W ustawieniach Codex można włączyć automatyczne recenzje każdego nowego PR.

**Paczka zadań:** na tablicy zadania mają `who: codex`. Owner wysyła w Codex jedną wiadomość:

```text
Read AGENTS.md. Do the tasks marked "who: codex" under "Ready"
in BOARD.md. One commit per task, one pull request for the batch. Do not
change AGENTS.md, CLAUDE.md, .claude/, .github/ or the check script.
Update BOARD.md and add one line per task to JOURNAL.md in the last commit.
```

**Opis zadania redakcyjnego** (w tablicy albo w pliku zadania): plik, odbiorca tekstu, ton, czego nie zmieniać (fakty, liczby, cytaty, nazwy), maksymalna długość.

**Opis obrazu:** co ma przedstawiać, styl, proporcje i rozmiar, ścieżka docelowa, zakazy (prawdziwe osoby, cudze znaki i postacie).

## Co wraca i kto poprawia

- Uwagi z recenzji poprawia **autor zmiany**, nie recenzent. Prowadzący rozpatruje każdą uwagę: poprawia albo odpisuje, dlaczego nie.
- Uwag o stylu nie trzeba wdrażać. Recenzent pytany o problemy zawsze coś znajdzie.
- Zmiany od Codex przechodzą ten sam test i tę samą akceptację Ownera co zmiany załogi Claude.

## Niepotwierdzone, do sprawdzenia w praktyce

1. Limity recenzji i zadań chmurowych w planie Plus oraz działanie w repo prywatnych.
2. Czy komentarz `@codex review` dodany przez załogę Claude (z konta GitHub Ownera) uruchamia recenzję. Jeśli tak, przekazanie do recenzji nie wymaga Ownera.
3. Czy Codex w chmurze sam generuje obrazy i dodaje je do repo, czy trzeba je przenieść z aplikacji ChatGPT.

Wynik każdej próby zapisz w `JOURNAL.md` projektu i zgłoś do repo `AI-crew`, żeby poprawić ten plik.
