# Jak repo rośnie

Zasada: **element dochodzi wtedy, gdy wystąpi jego wyzwalacz**. Nie na zapas. Element, którego nikt nie użył przez dwa miesiące, wraca do przeglądu: zostawić czy usunąć.

| Etap | Wyzwalacz | Dokument |
| --- | --- | --- |
| 0. Start | Nowe repo | [`../core/`](../core/) i jeden wariant |
| 1. Budowa | Ponad około 10 otwartych zadań albo pierwsza specyfikacja | [`stage-1-budowa.md`](stage-1-budowa.md) |
| 2. Wydania | Pierwszy użytkownik poza Ownerem | [`stage-2-wydania.md`](stage-2-wydania.md) |
| 3. Utrzymanie | Pierwszy błąd zgłoszony przez użytkownika albo więcej niż jedna wersja w użyciu | [`stage-3-utrzymanie.md`](stage-3-utrzymanie.md) |
| 4. Operacje | Usługa działa online bez przerwy: hosting, konta, płatności | [`stage-4-operacje.md`](stage-4-operacje.md) |

Etapy się sumują. Projekt treściowy zwykle kończy na etapie 1 albo 2. Aplikacja z kontami i płatnościami dochodzi do 4.

Załoga nie rośnie o stałe role. Rosną **wyzwalacze** (harmonogram, zdarzenie z GitHuba, alarm) i **procedury** (skille, runbooki). Prowadzący zostaje jeden.

Przejście na kolejny etap zapisuje się jako decyzję w `docs/decisions/`.
