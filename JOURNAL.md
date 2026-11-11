# Dziennik

Co się wydarzyło, co zostało ustalone i czego się nauczyliśmy. Najnowsze wpisy na dole. Wpisów się nie poprawia; sprostowanie to nowy wpis.

Gdzie co zapisać:

| Notatka | Miejsce |
| --- | --- |
| Co zrobić i czy zrobione | `BOARD.md` |
| Wybór, który jest rozstrzygnięty | `docs/decisions/` |
| Pomysł odrzucony, z powodem | `docs/out-of-scope/` |
| Co się wydarzyło, wniosek, niespodzianka, sprawa otwarta | tutaj |

Stan tygodniowy ma pięć liczb: zadania zakończone, zwroty po recenzji, konsultacje z doradcą, pytania do Ownera, trafienia w limit.

## 2026-10-31 do 2026-11-10 (wpis zbiorczy, odtworzony z historii gita)

- 31.10: repo założone; pierwszy raport o skutecznej załodze i układzie repo.
- 3.11: rekomendacja dotycząca skilli dla agentów.
- 7–8.11: raport o orkiestracji i hostingu (v1–v3.1) oraz analiza Codex.
- 8.11: raport z wymaganiami śpiewnika na żywo i zadanie startowe jego repo.
- 10.11: przegląd przekrojowy koncepcji; usunięty 11.11 na prośbę Ownera.

## 2026-11-11

- Owner doprecyzował cel: koncepcja startowa dla **nowych** projektów, a nie diagnoza istniejących. Raporty zanonimizowano (decyzja 0005).
- Powstał [raport koncepcyjny](outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md), struktura startowa tego repo i blueprint [`starter-crew-repo`](blueprints/starter-crew-repo/README.md).
- Wniosek 1: uprawnienia i hooki z `.claude/settings.json` działają tylko w sesji z jednym repo i lokalnie. W sesji z kilkoma repo i w wątkach „Projects” nie działają. Dlatego zasady krytyczne są w `AGENTS.md`, a praca załogi ma iść w sesji z jednym repo.
- Wniosek 2: status decyzji musi mówić prawdę. Wcześniej polecenie „rozważ” trafiło do raportu jako „decyzja Ownera”. Stąd statusy `propozycja` i `założenie robocze` w `docs/decisions/`.
- Wniosek 3: raport z 31.10 i zadanie startowe śpiewnika zakładały więcej plików na starcie. Nowy blueprint zaczyna od rdzenia i dokłada elementy według wyzwalaczy.
- Ta sesja pracowała z kilkoma repo naraz i na większym modelu (krótka promocja). To wyjątek, nie wzór: zwykła praca ma iść na Sonnecie w sesji z jednym repo.
- Niesprawdzone z tej sesji: strony OpenAI i wpis Anthropic o strategii doradcy były niedostępne; dane pochodzą z wyników wyszukiwania i omówień (oznaczone w raporcie).
- Owner zgłosił dwa wymagania do koncepcji: zadanie ma nieść kontekst przy przekazaniu i przy pauzie (limit, decyzja Ownera), a praca ma iść zawsze na jednym repo, z innymi tylko do odczytu i z możliwością zostawienia notatki z pomysłem. Ustalenie z dokumentacji: repo dołączone do sesji do odczytu nie pozwala na zapis, więc notatka w cudzym repo wymaga albo dostępu do zapisu, albo doręczenia przez sesję tamtego repo. Decyzja czeka na Ownera (tablica, punkt 9).
- Owner przyjął ciągłość zadań (decyzja 0007) i wariant A notatek między projektami (decyzja 0008). Blueprint ma wersję 1.1; te same zasady weszły do `AGENTS.md` i `CLAUDE.md` tego repo za zgodą Ownera.
- Pomysł Ownera: skrzynka centralna zbierająca notatki ze wszystkich repo. Ocena: naprawia doręczanie w wariancie A, ale musi być w prywatnym repo, bo spis notatek zawiera nazwy projektów. Ustalenie z dokumentacji: zaplanowane zadanie z kilkoma repo ma prawo zapisu do każdego z nich, więc zbieranie na start lepiej uruchamiać ręcznie, z repo dołączonymi do odczytu. Czeka na decyzję (tablica, punkt 9).
- Owner zdecydował o skrzynce centralnej (decyzja 0009): osobne prywatne repo, start od razu, zbieranie na polecenie, potem automat. Powstał blueprint `crew-inbox` ze skryptem zbierającym i testem. Utworzenie repo przez integrację nie powiodło się (GitHub: brak uprawnienia), więc T-005 czeka na Ownera z plikiem stanu. Pierwsze użycie pliku stanu w praktyce.
- Wniosek: zbieranie notatek jest czynnością mechaniczną, więc robi je skrypt, a model tylko go uruchamia. To tańsze i nie pozwala przerabiać treści notatek.
