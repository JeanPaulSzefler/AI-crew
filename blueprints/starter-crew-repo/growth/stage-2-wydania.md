# Etap 2: wydania

**Wyzwalacz:** pierwszy użytkownik poza Ownerem (pierwsza publikacja, pierwsza paczka przekazana komuś).

## Co dochodzi

| Element | Zasada |
| --- | --- |
| `CHANGELOG.md` | Dla ludzi, nie zrzut commitów. Sekcje: Added, Changed, Fixed, Removed. Na górze zawsze „Unreleased” |
| Numer wersji | `GŁÓWNA.POBOCZNA.POPRAWKA`. Poprawka błędu podnosi ostatnią liczbę, nowa funkcja środkową, zmiana niezgodna wstecz pierwszą |
| `docs/release.md` | Lista kontrolna wydania (niżej). Każde wydanie przechodzi ją od góry do dołu |
| Tag w gicie | `vX.Y.Z` na commicie, z którego powstało wydanie |
| `.github/pull_request_template.md` | Zadanie, klauzula specyfikacji, komenda testu z wynikiem, ryzyka |
| Opublikowane paczki | Raz wydanego pliku nie podmienia się. Poprawka to nowa wersja |

## Lista kontrolna wydania (`docs/release.md`)

```markdown
# Release vX.Y.Z

- [ ] All tasks of the release are under "Done"
- [ ] The check passes on the main branch (output pasted below)
- [ ] `CHANGELOG.md`: "Unreleased" moved under the version number with the date
- [ ] Version number changed in every place it appears
- [ ] Advisor (Opus): verdict "go", based on the change list and the check output
- [ ] Codex: review of the changes since the last release; findings handled
- [ ] Package built and tried by hand on a device (if it applies; `needs-pc`)
- [ ] **Owner: approval to publish**
- [ ] Tag `vX.Y.Z`, publication, a line in `JOURNAL.md`
```

## Zmiany w załodze

- Wydanie jest **klasą C**. Załoga przygotowuje wszystko do przedostatniego kroku. Publikuje Owner.
- Doradca i Codex są obowiązkowi **przed każdym wydaniem**. To jeden z trzech momentów użycia Opus.
- Po wydaniu Prowadzący dopisuje do dziennika, co poszło inaczej niż w liście kontrolnej, i poprawia listę.

## Dla projektów treściowych

„Wydaniem” jest publikacja: wpis, materiał, raport przekazany na zewnątrz. Zamiast numeru wersji wystarcza data publikacji i wpis w `CHANGELOG.md`. Lista kontrolna ma wtedy: źródła sprawdzone, redakcja Codex, prawa do obrazów i cytatów, zgoda Ownera.
