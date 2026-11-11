# Etap 4: operacje

**Wyzwalacz:** usługa działa online bez przerwy i ktoś na niej polega: hosting, konta użytkowników, płatności.

## Co dochodzi

```text
ops/
├── monitoring.md      # co mierzymy, próg alarmu, kto i jak dostaje alarm
├── runbooks/          # jedna awaria = jeden plik z krokami
├── incidents/         # RRRR-MM-DD-tytul.md, opis po incydencie
└── backups.md         # co, jak często, gdzie, kiedy ostatnio próbowano odtworzyć
support/
├── faq.md             # pytania użytkowników i zatwierdzone odpowiedzi
└── templates/         # szablony odpowiedzi według kategorii
```

### `ops/monitoring.md`

| Co mierzymy | Skąd | Próg alarmu | Runbook |
| --- | --- | --- | --- |
| Czy usługa odpowiada | zewnętrzny monitor | 2 nieudane próby z rzędu | `runbooks/usluga-nie-odpowiada.md` |
| Odsetek błędów | logi hostingu | powyżej ustalonego progu przez 10 minut | … |
| Płatności | panel operatora płatności | nieudany webhook | … |
| Koszt hostingu | panel dostawcy | powyżej budżetu miesięcznego | … |

### Szablon runbooka

```markdown
# Objaw: …
- Waga: S1 | S2 · Ostatnio sprawdzony: RRRR-MM-DD
## Jak potwierdzić (tylko odczyt)
## Kroki naprawy (wykonuje Owner; każdy krok możliwy z telefonu)
## Jak sprawdzić, że działa
## Kiedy eskalować i do kogo (dostawca, wsparcie)
```

### Szablon opisu po incydencie

Bez szukania winnych: opisujemy, co w układzie pozwoliło na błąd.

```markdown
# RRRR-MM-DD: tytuł
- Czas trwania · Kogo dotknęło · Waga
## Przebieg (godziny i fakty)
## Przyczyna
## Co zadziałało, co nie
## Zmiany, żeby się nie powtórzyło (każda jako zadanie na tablicy)
```

## Zmiany w załodze

- **Agent dyżurny** to nie nowa rola, tylko nowy wyzwalacz. Sesję uruchamia alarm (wywołanie zaplanowanego zadania przez API) albo harmonogram. Agent zbiera dane, dopasowuje runbook i pisze **szkic diagnozy** do „Czeka na Ownera”.
- **Na produkcji agent ma tylko odczyt.** Wdrożenia, zmiany konfiguracji, bazy danych i sekrety to klasa C.
- **Wsparcie użytkowników:** agent klasyfikuje wiadomość i przygotowuje szkic z `support/templates/`. Wysyła Owner. Samodzielne odpowiedzi można rozważyć później dla jednej wąskiej kategorii, po serii szkiców przyjętych bez zmian, jako osobną decyzję.
- **Dane osobowe** użytkowników nie trafiają do repo ani do dziennika. W opisie incydentu są tylko liczby i identyfikatory techniczne.
- Raz na kwartał: próba odtworzenia kopii zapasowej i przegląd runbooków. To zadanie cykliczne na tablicy.

## Granica tego blueprintu

Przy stałym ruchu, zespole większym niż jedna osoba albo wymaganiach prawnych (umowy, regulowane dane) potrzebne są narzędzia spoza repo: system zgłoszeń, monitoring z dyżurami, osobne środowiska. To osobna decyzja z własnym researchem.
