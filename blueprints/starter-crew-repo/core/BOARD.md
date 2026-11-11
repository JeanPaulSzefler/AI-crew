# Tablica zadań

Stan pracy w tym repo. Agent zaczyna od tego pliku. Zasady: [`AGENTS.md`](AGENTS.md).

Format zadania:

```text
- [ ] T-001 · tytuł · kto: lead | worker | codex | owner · klasa: A | B | C
      Cel: co ma powstać. Pliki: gdzie. Odbiór: po czym poznać, że gotowe.
```

Zadanie bez celu, plików i odbioru nie jest gotowe i zostaje w „Pomysłach”.

## Czeka na Ownera

Pytania i akceptacje. Najstarsze na górze. Owner odpowiada pod wpisem.

- (pusto)

## Gotowe do wzięcia

- [ ] T-001 · {{tytuł}} · kto: lead · klasa: B
      Cel: {{…}}. Pliki: {{…}}. Odbiór: {{…}}.

## W toku

Zadanie wstrzymane albo przekazane ma plik stanu w [`work/`](work/README.md). Wpis podaje stan i odnośnik do pliku.

- (pusto)

## Pomysły

Rzeczy jeszcze nieprzygotowane. Agent może tu dopisywać, nie może ich zaczynać. Pomysł z innego projektu ma dopisek „z zewnątrz” i numer notatki.

- (pusto)

## Dla innych projektów

Pomysły zauważone przy pracy tutaj, które dotyczą innego repo. Tylko dopisywanie, najnowsze na dole. Stąd nikt nie pisze do cudzego repo: notatkę zabiera sesja repo docelowego. Zasady: [`AGENTS.md`](AGENTS.md), sekcja „Other repositories”.

```text
- N-{{repo}}-001 · dla: nazwa-repo · RRRR-MM-DD
      Co zauważyłem: … Dlaczego to ważne: … Gdzie to widać: plik albo miejsce.
```

- (pusto)

## Zrobione

Ostatnie 10. Starsze są w historii gita i w `JOURNAL.md`.

- (pusto)
