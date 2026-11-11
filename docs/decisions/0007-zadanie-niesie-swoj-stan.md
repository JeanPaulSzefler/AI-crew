# 0007: Zadanie niesie swój stan: plik stanu, punkty kontrolne, stała kolejność wznawiania

- **Data:** 2026-11-11
- **Status:** przyjęta
- **Podstawa:** Owner 11.11.2026: zadania i ich przekazywanie między modelami i rolami mają zapewnić ciągłość kontekstu oraz możliwość pauzy, gdy kończy się limit sesji albo trzeba poczekać na decyzję Ownera; „Tak, przyjmij cz. 1”

## Decyzja

- Zadanie wstrzymane, zablokowane albo przekazywane ma plik stanu `work/T-NNN-tytul.md`: stan, kto trzyma, gałąź, co zrobione, następny krok, otwarte pytania, pułapki. Zadanie zrobione w jednym podejściu zostaje linią na tablicy.
- Po każdym kroku jest punkt kontrolny: plik stanu, commit z numerem zadania, push.
- Każda sesja wznawia pracę w tej samej kolejności: tablica, plik stanu, historia gałęzi, test, następny krok.
- Zadanie ma zawsze jednego trzymającego.

Zastępuje regułę „jedno zadanie = jeden commit” z pierwszej wersji `AGENTS.md`: commitów jest tyle, ile punktów kontrolnych, a każdy zaczyna się numerem zadania.

## Powód

Limit przerywa sesję w pół kroku, więc stan zapisany dopiero na końcu nie powstaje. Plik stanu jest też jednym nośnikiem kontekstu dla Haiku, Opusa i Codexa, a wznowienie kosztuje odczyt jednego pliku.

## Kiedy wrócić

Gdy pliki stanu okażą się martwe (nikt ich nie czyta przy wznawianiu) albo gdy narzędzia zaczną same przenosić stan między sesjami i modelami.
