# 0003: Trzy tryby autonomii i lista „zawsze Owner”; to repo ma poziom 2

- **Data:** 2026-11-11
- **Status:** przyjęta w części ogólnej. Poziom 2 dla tego repo: do potwierdzenia przez Ownera
- **Podstawa:** Owner 11.11.2026: tryby (a) i (c) są potrzebne; tryb (b) „wg twoich rekomendacji”; tryb (c) na początek jako eksperyment. W tej samej rozmowie Owner pozwolił wypychać zmiany w tym repo prosto na `master`

## Decyzja

- **(a)** Owner podaje cel i wraca do gotowej zmiany do akceptacji. Obowiązuje zawsze.
- **(b)** Załoga sama scala zmiany klasy A (dziennik, tablica, indeksy, literówki, testy, drobne zmiany wewnętrzne) po przejściu testu. Nowe repo zaczyna bez tego trybu i przechodzi na niego po kilku czystych zmianach.
- **(c)** Załoga startuje bez Ownera: raz dziennie jedno–dwa gotowe zadania, raz w tygodniu krótki stan. Eksperyment do przeglądu po miesiącu.
- **Zawsze Owner:** wydania i publikacje, pieniądze, konta, sprawy prawne, kasowanie danych, zmiana widoczności repo oraz zmiana zasad samej załogi (instrukcje, uprawnienia, CI, test).

Repo `AI-crew` dostaje poziom 2, bo ma już serię zmian przyjętych przez Ownera. Raporty, rekomendacje i blueprinty pozostają klasą B, chyba że Owner w sesji poleci inaczej.

## Powód

Zmiana zasad załogi jest na liście „zawsze Owner”, żeby załoga nie mogła sama poluzować swoich zabezpieczeń. Klasa A obejmuje rzeczy tanie do cofnięcia.

## Kiedy wrócić

Po miesiącu trybu (c); po pierwszej zmianie klasy A, którą Owner musiał cofnąć; gdy repo dostanie ochronę gałęzi.
