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

1. **Struktura załogi** ([decyzja 0001](docs/decisions/0001-struktura-zalogi.md), [raport](outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md) rozdz. 3–4): przyjąć, zmienić czy odrzucić? Do czasu odpowiedzi ma status propozycji.
2. **Poziom autonomii tego repo:** zapisany jako 2 (załoga sama scala dziennik, tablicę, indeksy i literówki). Potwierdzić albo zmienić na 1 ([decyzja 0003](docs/decisions/0003-tryby-autonomii.md)).
3. **Tryb (c):** w którym repo i od kiedy włączyć dwa zaplanowane zadania ([treści poleceń](blueprints/starter-crew-repo/automation/scheduled-tasks.md))? Włącza Owner albo załoga na jego wyraźne polecenie.
4. **Pilotaż:** który nowy projekt postawić z blueprintu jako pierwszy?
5. **Gałąź domyślna na GitHubie** jest nadal gałęzią sesji, a nie `master`. Zmiana: Settings → Branches (tylko Owner).
6. **Sprostowanie:** w raporcie hostingowym v3 i w przeglądzie w publicznym repo z grami polecenie „rozważ” zostało zapisane jako „decyzja Ownera”. Poprawka była zaproponowana, czeka na zgodę.
7. **Historia gita** zawiera starsze wersje raportów ze szczegółami prywatnych projektów. Odłożone przez Ownera 11.11.2026.
8. **Założenia robocze** do potwierdzenia: zadania w plikach ([0002](docs/decisions/0002-zadania-i-decyzje-w-plikach.md)) i podział języków ([0004](docs/decisions/0004-jezyk-plikow.md)).
9. **Utworzyć puste prywatne repo `crew-inbox`** (GitHub: New repository → Private). Integracja Claude nie może zakładać repozytoriów. Po utworzeniu wystarczy napisać w sesji „uruchom skrzynkę”. Do decyzji przy okazji: które repo podłączyć oprócz tego. Stan: [`work/T-005-crew-inbox.md`](work/T-005-crew-inbox.md).

## Gotowe do wzięcia

- [ ] T-002 · Dopasować zadanie startowe śpiewnika do nowego blueprintu · kto: lead · klasa: B
      Cel: `TASK-000` śpiewnika korzysta z `starter-crew-repo` (wariant z kodem) zamiast własnej listy plików. Pliki: `blueprints/spiewnik-live/`. Odbiór: zadanie odsyła do blueprintu, nie powiela jego treści, test przechodzi.
- [ ] T-003 · Dodać do blueprintu słowniczek pojęć dla Ownera · kto: lead · klasa: B
      Cel: jedna strona po polsku: sesja, subagent, klasa ryzyka, poziom autonomii, zaplanowane zadanie, PR. Pliki: `blueprints/starter-crew-repo/`. Odbiór: każde pojęcie z README blueprintu ma objaśnienie w dwóch zdaniach.

## W toku

Zadanie wstrzymane albo przekazane ma plik stanu w [`work/`](work/README.md). Wpis podaje stan i odnośnik do pliku.

- [ ] T-005 · Uruchomić skrzynkę centralną `crew-inbox` · kto: lead · klasa: B · stan: czeka na Ownera · [plik stanu](work/T-005-crew-inbox.md)

## Pomysły

Rzeczy jeszcze nieprzygotowane. Agent może tu dopisywać, nie może ich zaczynać. Pomysł z innego projektu ma dopisek „z zewnątrz” i numer notatki.

- Sprawdzić w praktyce pięć pytań z rozdziału 11 raportu (advisor w chmurze, automatyczne recenzje Codex, `@codex review` od załogi, obrazy z Codex, limit przy trybie c). Wymaga kont Ownera i sesji na Sonnecie.
- Wariant blueprintu dla aplikacji mobilnej albo gry, z krokiem „wymaga komputera” przy budowaniu paczki.
- Po pilotażu: przegląd blueprintu według rozdziału 10 raportu.
- Przejrzeć raport z 31.10 i rekomendację skilli pod kątem zgodności z decyzjami 0001–0006.
- Jedna próba sesji-kuriera (wariant B z decyzji 0008): sesja uruchamia krótką sesję w repo docelowym, która zapisuje notatkę.
- Automatyzacja zbierania w skrzynce (decyzja 0009: „potem na automat”). Warunki w `blueprints/crew-inbox/README.md`: dwa podłączone repo, trzy udane zbierania ręczne, zgoda Ownera na zaplanowane zadanie.

## Dla innych projektów

Pomysły zauważone przy pracy tutaj, które dotyczą innego repo. Tylko dopisywanie, najnowsze na dole. Stąd nikt nie pisze do cudzego repo: notatkę zabiera sesja repo docelowego. Zasady: [`AGENTS.md`](AGENTS.md), sekcja „Other repositories”.

```text
- N-aicrew-001 · dla: nazwa-repo · RRRR-MM-DD
      Co zauważyłem: … Dlaczego to ważne: … Gdzie to widać: plik albo miejsce.
```

- (pusto)

## Zrobione

Ostatnie 10. Starsze są w historii gita i w `JOURNAL.md`.

- [x] T-001 · Raport koncepcyjny, struktura startowa tego repo i blueprint `starter-crew-repo` · kto: lead · klasa: B · 2026-11-11
- [x] T-004 · Blueprint v1.1: pliki stanu zadań, punkty kontrolne, jedno repo na sesję, skrzynka nadawcza (decyzje 0007 i 0008) · kto: lead · klasa: B · 2026-11-11
