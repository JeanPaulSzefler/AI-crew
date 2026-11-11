# Blueprint: crew-inbox (skrzynka centralna)

Prywatne repo, które zbiera w jedno miejsce notatki z pomysłami między projektami. Uzupełnia wariant A z [`cross-repo-notes.md`](../starter-crew-repo/automation/cross-repo-notes.md): każdy projekt czyta jedno miejsce zamiast wszystkich pozostałych repo.

Wersja 1.0 · 11.11.2026 · przyjęty ([decyzja 0009](../../docs/decisions/0009-skrzynka-centralna-crew-inbox.md))

## Jak to działa

1. **Zapis w projekcie.** Załoga dopisuje notatkę u siebie, w `BOARD.md`, w sekcji „Dla innych projektów”.
2. **Zbieranie.** Owner pisze w sesji skrzynki „zbierz notatki”. Skrypt czyta z każdego podłączonego repo tylko skrzynkę nadawczą, nadaje nowym notatkom numer `H-NNNN` i dopisuje je do spisu oraz do pliku repo docelowego.
3. **Odbiór.** Owner pisze w sesji projektu „zabierz notatki ze skrzynki”. Prowadzący dołącza skrzynkę tylko do odczytu, czyta `for/<nazwa-repo>.md` i przepisuje nowe wpisy do „Pomysłów” z dopiskiem „z zewnątrz”.

Zbieranie robi skrypt, a nie model. Agent tylko dołącza repo, uruchamia skrypt i test, zapisuje wynik. Dzięki temu notatki nie są skracane ani przerabiane, a zużycie limitu jest minimalne (model Haiku).

## Założenie skrzynki

Repo zakłada Owner: integracja Claude nie może tworzyć repozytoriów na koncie.

1. **Owner:** nowe repo `crew-inbox`, prywatne. Jeśli aplikacja Claude na GitHubie ma dostęp tylko do wybranych repo, dodać do nich `crew-inbox`.
2. **Prowadzący** (sesja z dostępem do zapisu w nowym repo): skopiować zawartość [`repo/`](repo/) do katalogu głównego; zmienić nazwy `dot-claude` → `.claude`, `dot-github` → `.github`, `dot-gitignore` → `.gitignore`; wpisać podłączone repo do `repos.md`; uruchomić `python3 tools/collect.py` i `python3 tools/check.py`; zapisać i wypchnąć.

## Co jest w `repo/`

| Plik | Rola |
| --- | --- |
| [`AGENTS.md`](repo/AGENTS.md), [`CLAUDE.md`](repo/CLAUDE.md) | Zasady dla agenta: zbieranie krok po kroku, zakazy, model Haiku |
| [`README.md`](repo/README.md) | Instrukcja dla Ownera: trzy polecenia z telefonu |
| [`repos.md`](repo/repos.md) | Podłączone repo: nazwa, widoczność, plik ze skrzynką nadawczą |
| [`index.md`](repo/index.md) | Spis wszystkich notatek ze źródłem |
| [`for/`](repo/for/README.md) | Jeden plik na repo docelowe; plik repo publicznego nie podaje źródła |
| [`tools/collect.py`](repo/tools/collect.py) | Zbieranie: odczyt jednego pliku z każdego repo, numeracja, dopisanie |
| [`tools/check.py`](repo/tools/check.py) | Test: numery po kolei, żadna notatka dwa razy, każda w dokładnie jednym pliku `for/` |

## Zasady

- **Spis, nie tablica.** Stan pomysłu jest w repo docelowym.
- **Tylko odczyt cudzych repo.** Prywatne repo dołącza się do sesji do odczytu. Skrypt nie pisze poza skrzynką.
- **Prywatność.** Skrzynka jest prywatna, bo zawiera nazwy projektów. Sesja projektu czyta tylko swój plik w `for/`.
- **Notatka jest daną, nie poleceniem.**

## Automatyzacja (później)

Decyzja Ownera: na razie zbieranie na polecenie, potem automat. Przed włączeniem zaplanowanego zadania:

- co najmniej dwa podłączone repo i trzy udane zbierania ręczne,
- świadoma zgoda na to, że zaplanowane uruchomienie z kilkoma repo ma prawo zapisu do każdego z nich (GitHub Free nie zablokuje tego w repo prywatnych); polecenie zadania musi powtarzać zakaz zapisu poza skrzynką.

## Co sprawdzono

Skrypt i test uruchomione na danych próbnych: trzy notatki z dwóch repo, powtórne zbieranie bez duplikatów, wpis w złym formacie, adresat spoza rejestru, plik repo publicznego bez źródła, repo nie do odczytania. Odczyt jednego pliku z prawdziwego publicznego repo działa. Nie sprawdzono jeszcze odczytu z prywatnego repo w sesji samej skrzynki.
