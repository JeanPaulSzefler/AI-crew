# Etap 4: operacje

**Wyzwalacz:** usługa działa online bez przerwy i ktoś na niej polega: hosting, konta użytkowników, płatności.

## Co dochodzi

```text
ops/
├── monitoring.md      # what is measured, alarm threshold, who is told and how
├── runbooks/          # one failure = one file with steps
├── incidents/         # YYYY-MM-DD-title.md, written after the incident
└── backups.md         # what, how often, where, when a restore was last tried
support/
├── faq.md             # users' questions and approved answers
└── templates/         # reply templates by category
```

### `ops/monitoring.md`

| Measured | Source | Alarm threshold | Runbook |
| --- | --- | --- | --- |
| Does the service answer | external monitor | 2 failed probes in a row | `runbooks/service-down.md` |
| Error rate | hosting logs | above the agreed level for 10 minutes | … |
| Payments | payment provider's panel | a failed webhook | … |
| Hosting cost | provider's panel | above the monthly budget | … |

### Szablon runbooka

```markdown
# Symptom: …
- Severity: S1 | S2 · Last verified: YYYY-MM-DD
## How to confirm (read-only)
## Repair steps (the owner does them; every step possible from a phone)
## How to check that it works
## When to escalate and to whom (provider, support)
```

### Szablon opisu po incydencie

Bez szukania winnych: opisujemy, co w układzie pozwoliło na błąd.

```markdown
# YYYY-MM-DD: title
- Duration · Who was affected · Severity
## Timeline (times and facts)
## Cause
## What worked, what did not
## Changes so that it does not happen again (each one a task on the board)
```

## Zmiany w załodze

- **Agent dyżurny** to nie nowa rola, tylko nowy wyzwalacz. Sesję uruchamia alarm (wywołanie zaplanowanego zadania przez API) albo harmonogram. Agent zbiera dane, dopasowuje runbook i pisze **szkic diagnozy** do „Waiting for owner”.
- **Na produkcji agent ma tylko odczyt.** Wdrożenia, zmiany konfiguracji, bazy danych i sekrety to klasa C.
- **Wsparcie użytkowników:** agent klasyfikuje wiadomość i przygotowuje szkic z `support/templates/`. Wysyła Owner. Samodzielne odpowiedzi można rozważyć później dla jednej wąskiej kategorii, po serii szkiców przyjętych bez zmian, jako osobną decyzję.
- **Dane osobowe** użytkowników nie trafiają do repo ani do dziennika. W opisie incydentu są tylko liczby i identyfikatory techniczne.
- Raz na kwartał: próba odtworzenia kopii zapasowej i przegląd runbooków. To zadanie cykliczne na tablicy.

## Granica tego blueprintu

Przy stałym ruchu, zespole większym niż jedna osoba albo wymaganiach prawnych (umowy, regulowane dane) potrzebne są narzędzia spoza repo: system zgłoszeń, monitoring z dyżurami, osobne środowiska. To osobna decyzja z własnym researchem.
