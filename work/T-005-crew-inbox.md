# T-005: Uruchomić skrzynkę centralną `crew-inbox`

- **Stan:** czeka na Ownera
- **Trzyma:** owner
- **Klasa:** B · **Gałąź:** `master` (blueprint); nowe repo: gałąź główna
- **Ostatni punkt kontrolny:** 2026-11-11, commit z blueprintem `crew-inbox`

## Cel i odbiór

Prywatne repo `crew-inbox` istnieje, ma pliki z `blueprints/crew-inbox/repo/`, a pierwsze zbieranie i test przechodzą. Decyzja 0009.

## Zrobione

- Blueprint `blueprints/crew-inbox/`: zasady, instrukcja, skrypt zbierający, test, CI.
- Skrypt i test sprawdzone na danych próbnych i na odczycie publicznego repo.
- Próba utworzenia repo przez integrację: odmowa GitHuba (brak uprawnienia do tworzenia repozytoriów).

## Następny krok

Po utworzeniu repo przez Ownera: dołączyć `crew-inbox` do sesji z prawem zapisu, wykonać krok 2 z `blueprints/crew-inbox/README.md` („Założenie skrzynki”), wpisać do `repos.md` repo `AI-crew` (publiczne, `BOARD.md`), uruchomić zbieranie i test, wypchnąć.

## Otwarte pytania

- Owner: utworzyć puste prywatne repo `crew-inbox` · bez tego brak dalszych kroków · czekam.
- Owner: które repo podłączyć oprócz `AI-crew`? · bez odpowiedzi podłączam tylko `AI-crew`.

## Pułapki i ustalenia

- Jeśli aplikacja Claude na GitHubie ma dostęp tylko do wybranych repo, nowe repo trzeba do nich dodać.
- Nazwy innych repo Ownera wpisuje się tylko w prywatnej skrzynce, nigdy tutaj.
- Zbieranie na polecenie; zaplanowanego zadania nie tworzyć bez osobnej decyzji.
