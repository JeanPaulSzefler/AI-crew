# 0009: Skrzynka centralna to osobne prywatne repo `crew-inbox`; zbieranie na polecenie, potem automat

- **Data:** 2026-11-11
- **Status:** przyjęta
- **Podstawa:** Owner 11.11.2026: „skrzynka to osobne prywatne repo, uruchomić od razu i nazwać po angielsku. Na razie na polecenie, potem na automat”

## Decyzja

- Notatki między projektami (decyzja 0008) zbiera osobne prywatne repo. Nazwę `crew-inbox` wybrał agent; Owner może ją zmienić.
- Skrzynka rusza od razu, a nie dopiero przy trzecim repo.
- Zbieranie odbywa się na polecenie Ownera w sesji skrzynki. Automatyzacja przyjdzie później, osobną decyzją.
- Zbiera skrypt, nie model. Skrzynka jest spisem: stan pomysłu zostaje w repo docelowym. Sesja projektu czyta tylko swój plik.

Struktura: [`blueprints/crew-inbox/`](../../blueprints/crew-inbox/README.md).

## Powód

Bez skrzynki każde repo musiałoby czytać wszystkie pozostałe. Repo musi być prywatne, bo spis zawiera nazwy projektów. Agent rekomendował start przy trzecim repo; Owner wybrał start od razu.

## Kiedy wrócić

Przy decyzji o automatyzacji (warunki w blueprincie); gdy notatek jest tyle, że jeden plik na repo przestaje wystarczać; po zmianie planu GitHub, która pozwoli ograniczyć prawo zapisu.
