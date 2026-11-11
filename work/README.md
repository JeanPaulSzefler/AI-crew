# Pliki stanu zadań

Zadanie niesie swój stan. Dzięki temu pracę może podjąć inna sesja, inny model albo inny dostawca, także po nagłym przerwaniu.

## Kiedy powstaje plik

Plik `T-NNN-tytul.md` powstaje, gdy zadanie:

- nie skończy się w jednym podejściu,
- czeka na decyzję Ownera,
- przechodzi do kogoś innego (worker, advisor, Codex).

Zadanie zrobione w jednym podejściu zostaje linią na tablicy.

## Zasady

1. **Punkt kontrolny po każdym kroku:** najpierw aktualizacja pliku stanu, potem commit i push. Sesję może przerwać limit w dowolnej chwili, więc stan zapisuje się w trakcie, nie na końcu.
2. **„Następny krok” to jedno konkretne działanie**, które da się wykonać bez pytania o cokolwiek.
3. **Jeden trzymający.** Pole „Trzyma” zmienia ten, kto przekazuje zadanie.
4. **Wznowienie:** tablica → plik stanu → `git log` gałęzi zadania → test → następny krok.
5. Po zakończeniu plik zostaje ze stanem „zrobione”. Wpis na tablicy przechodzi do „Zrobione”.

## Rodzaje pauzy

| Pauza | Co zapisać | Kto wznawia |
| --- | --- | --- |
| Limit sesji | Nic dodatkowego: wystarcza ostatni punkt kontrolny | Ta sama sesja po odnowieniu limitu albo następne uruchomienie |
| Decyzja Ownera | Pytanie z opcjami w pliku stanu i wpis w „Czeka na Ownera” | Dowolna sesja po odpowiedzi |
| Przekazanie | Kto trzyma i co ma wrócić | Odbiorca, potem prowadzący |

## Szablon

```markdown
# T-NNN: tytuł

- **Stan:** w toku | wstrzymane: limit | czeka na Ownera | przekazane: worker / advisor / codex | zrobione
- **Trzyma:** lead | worker | codex | owner
- **Klasa:** A | B | C · **Gałąź:** `nazwa-gałęzi`
- **Ostatni punkt kontrolny:** RRRR-MM-DD, commit `abc1234`

## Cel i odbiór
Przepisane z tablicy. Nie zmieniać w trakcie pracy.

## Zrobione
- …

## Następny krok
Jedno konkretne działanie.

## Otwarte pytania
- Pytanie · opcje · co zrobię bez odpowiedzi (albo: „czekam”)

## Pułapki i ustalenia
Czego nie ruszać, co już próbowano bez skutku, wybory podjęte po drodze.
```
