# 0002: Zadania i decyzje są plikami w repo, nie zgłoszeniami w GitHub Issues

- **Data:** 2026-11-11
- **Status:** założenie robocze. Przedstawione Ownerowi 11.11.2026 jako założenie; Owner go nie odrzucił, ale też wprost nie potwierdził
- **Podstawa:** rozmowa z 11.11.2026; raport z 11.11.2026, rozdział 8

## Decyzja

Tablica zadań to `BOARD.md`, decyzje to `docs/decisions/`, odrzucone pomysły to `docs/out-of-scope/`. GitHub Issues służy dopiero jako skrzynka zgłoszeń od użytkowników (etap 3 blueprintu).

## Powód

Pliki ładują się w każdej sesji i dla każdego dostawcy bez dodatkowych narzędzi. Agent czyta stan jednym odczytem. Owner widzi wszystko w aplikacji mobilnej razem ze zmianami. To zastępuje rekomendację z raportu z 31.10.2026 (sekcja 5: „GitHub Issues + Projects from day one”).

## Kiedy wrócić

Gdy nad repo pracuje więcej niż jedna osoba; gdy pliki tablicy zaczną się regularnie zderzać przy scalaniu; gdy zgłoszenia z zewnątrz staną się głównym źródłem zadań.
