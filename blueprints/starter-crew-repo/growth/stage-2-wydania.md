# Etap 2: wydania

**Wyzwalacz:** pierwszy użytkownik poza Ownerem (pierwsza publikacja, pierwsza paczka przekazana komuś).

## Co dochodzi

| Element | Zasada |
| --- | --- |
| `CHANGELOG.md` | Dla ludzi, nie zrzut commitów. Sekcje: Dodane, Zmienione, Naprawione, Usunięte. Na górze zawsze „Niewydane” |
| Numer wersji | `GŁÓWNA.POBOCZNA.POPRAWKA`. Poprawka błędu podnosi ostatnią liczbę, nowa funkcja środkową, zmiana niezgodna wstecz pierwszą |
| `docs/release.md` | Lista kontrolna wydania (niżej). Każde wydanie przechodzi ją od góry do dołu |
| Tag w gicie | `vX.Y.Z` na commicie, z którego powstało wydanie |
| `.github/pull_request_template.md` | Zadanie, klauzula specyfikacji, komenda testu z wynikiem, ryzyka |
| Opublikowane paczki | Raz wydanego pliku nie podmienia się. Poprawka to nowa wersja |

## Lista kontrolna wydania (`docs/release.md`)

```markdown
# Wydanie vX.Y.Z

- [ ] Wszystkie zadania wydania są w „Zrobione”
- [ ] Test przechodzi na gałęzi głównej (wynik wklejony niżej)
- [ ] `CHANGELOG.md`: sekcja „Niewydane” przeniesiona pod numer wersji z datą
- [ ] Numer wersji zmieniony we wszystkich miejscach
- [ ] Doradca (Opus): werdykt „go” na podstawie listy zmian i wyników testu
- [ ] Codex: recenzja zmian od poprzedniego wydania, uwagi rozpatrzone
- [ ] Paczka zbudowana i sprawdzona ręcznie na urządzeniu (jeśli dotyczy; „wymaga komputera”)
- [ ] **Owner: zgoda na publikację**
- [ ] Tag `vX.Y.Z`, publikacja, wpis w `JOURNAL.md`
```

## Zmiany w załodze

- Wydanie jest **klasą C**. Załoga przygotowuje wszystko do przedostatniego kroku. Publikuje Owner.
- Doradca i Codex są obowiązkowi **przed każdym wydaniem**. To jeden z trzech momentów użycia Opus.
- Po wydaniu Prowadzący dopisuje do dziennika, co poszło inaczej niż w liście kontrolnej, i poprawia listę.

## Dla projektów treściowych

„Wydaniem” jest publikacja: wpis, materiał, raport przekazany na zewnątrz. Zamiast numeru wersji wystarcza data publikacji i wpis w `CHANGELOG.md`. Lista kontrolna ma wtedy: źródła sprawdzone, redakcja Codex, prawa do obrazów i cytatów, zgoda Ownera.
