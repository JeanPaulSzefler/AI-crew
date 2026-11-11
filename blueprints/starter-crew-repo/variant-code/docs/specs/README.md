# Specyfikacje

Źródło prawdy o tym, co program ma robić. Zmiana zachowania zaczyna się tutaj, potem zadanie na tablicy, potem kod i test.

- Jeden plik na obszar: `SPEC-NNN-tytul.md`.
- Wymagania są **numerowanymi klauzulami** (`SPEC-003.4`). Zadania, testy i commity przywołują numer klauzuli.
- Każda klauzula ma kryterium odbioru, które da się sprawdzić testem.
- Poprawka błędu, która przywraca opisane zachowanie, nie wymaga zmiany specyfikacji. Wystarczy wskazać klauzulę, którą przywraca.
- Specyfikację pisze agent, zatwierdza Owner.

## Szablon

```markdown
# SPEC-NNN: tytuł

Status: szkic | zatwierdzona RRRR-MM-DD

## Cel
Jedno–dwa zdania.

## Klauzule
1. Program … (Odbiór: …)
2. …

## Poza zakresem
- …
```
