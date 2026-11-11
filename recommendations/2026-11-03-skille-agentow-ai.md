# Rekomendacja: które z 10 skilli dla agentów AI warto wdrożyć

3 listopada 2026 · Na podstawie [`resources/raport-10-skilli-dla-agentow-ai.md`](../resources/raport-10-skilli-dla-agentow-ai.md) i przeglądu projektów Ownera

> Zanonimizowano 11.11.2026: nazwy i szczegóły prywatnych projektów zastąpiono opisem typu projektu.

## W skrócie

| Decyzja | Skill | Gdzie |
| --- | --- | --- |
| **Wdrożyć** | Awesome Gamedev Agent Skills (tylko wybrane skille Godot) | Projekty w Godot |
| **Wdrożyć** | Humanizer | Projekty treściowe i `AI-crew` (teksty dla ludzi) |
| **Wdrożyć po audycie** | Ponytail (sam `SKILL.md`, bez hooków) | Projekty z kodem |
| **Opcjonalnie** | Diagram Design | `AI-crew` (diagramy architektury) |
| **Pilotaż za zgodą Ownera** | Lemo Opuscar | Tylko projekt treściowy z wideo, jako porównanie z obecnym narzędziem |
| **Nie teraz** | REA, Caveman, Animate, I have ADHD, Skills CLI jako instalator | — |

Ogólna zasada: skille **kopiujemy do `.claude/skills/` konkretnego repo z przypiętą wersją** (commit SHA) zamiast instalować globalnie przez `npx … --global` czy `curl | bash`. Każdy nowy skill przechodzi przez PR i audyt `skill-auditor` z repo [`AI-agents`](https://github.com/JeanPaulSzefler/AI-agents). To jest reguła „zatrudniania” z blueprintu AI-crew.

## 1. Profil projektów

Rekomendacje odnoszą się do typów projektów, nie do konkretnych repozytoriów:

- **projekty w Godot 4.x** (gra i aplikacja użytkowa na Androida): zapisy, sieć, eksport APK, testy;
- **projekty treściowe**: teksty publiczne i materiały czytane przez ludzi, także po polsku; jeden z nich tworzy krótkie wideo;
- **repozytoria z dokumentami i diagramami**, w tym `AI-crew`;
- **standard audytu skilli** w publicznym `AI-agents`.

Nie ma frontendu webowego z animacjami ani potrzeby dekompilowania aplikacji.

## 2. Ocena każdego skilla

Wszystkie 10 repozytoriów istnieje i jest aktywnie rozwijanych (ostatnie commity od kwietnia do listopada 2026). Licencje: MIT lub Apache-2.0, z wyjątkiem `animate-css-skill`, który nie ma pliku licencji.

### Awesome Gamedev Agent Skills: wdrożyć wybiórczo

- **Dlaczego:** pakiet ma 16 skilli Godot (m.in. `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `godot-ui-control`, `godot-multiplayer`) oraz dyscypliny (`game-feel`, `performance-optimization`, `save-systems`). To pasuje do gier i aplikacji w Godot (zapisy, sieć, Android).
- **Jak:** nie instaluj całego pakietu (251 plików, router). Skopiuj 6–8 potrzebnych skilli do `.claude/skills/` każdego repo Godot.
- **Zestaw dla gry:** `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `save-systems`, `game-feel`, `performance-optimization`, `godot-multiplayer`.
- **Zestaw dla aplikacji użytkowej w Godot:** `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `godot-ui-control`. Reguły projektu mają pierwszeństwo przed skillami.

### Humanizer: wdrożyć do treści dla ludzi

- **Dlaczego:** projekty treściowe tworzą teksty czytane przez ludzi (posty, napisy, materiały do nauki, konspekty). Humanizer (397 linii, MIT, v3.1.0) wyłapuje m.in. kontrasty „nie X, lecz Y”, sztuczne triady, jednozdaniowe puenty, nadmiar myślników.
- **Język polski:** wzorce są opisane po angielsku, ale skill wprost mówi, że te same konstrukcje występują w każdym języku. Przed wdrożeniem w projektach polskojęzycznych przetestuj go na 3–5 istniejących polskich tekstach.
- **Zgodność ze stylem projektu:** jeśli projekt ma własny przewodnik stylu dla plików wewnętrznych, Humanizer go nie zastępuje. Używaj go tylko na etapie przeglądu tekstów publicznych (opisy, napisy, posty), przed akceptacją Ownera.
- **Jak:** jako krok w istniejących skillach przeglądu, nie jako tryb zawsze włączony.

### Ponytail: wdrożyć po audycie, sam skill

- **Dlaczego:** reguła „najmniejsza kompletna zmiana” jest zbieżna z rekomendacjami AI-crew (krótki kod, recenzja bez stylu, koszt na zadanie). Przyda się w projektach z kodem.
- **Uwaga 1:** pełny plugin rejestruje hooki `SessionStart` i `SubagentStart` (Node.js), linię statusu i moduł „band” z opcjonalnym webhookiem. To więcej niż skill. Zacznij od samego `skills/ponytail/SKILL.md`; hooki dopiero po audycie.
- **Uwaga 2:** liczby z raportu (−54% kodu, −20% tokenów) pochodzą z benchmarków autora. Zweryfikuj je własnym logiem kosztu na zadanie (sekcja 7 raportu AI-crew).
- **Uwaga 3:** Ponytail ustawia też styl odpowiedzi („jedna–dwie linie na końcu”). Sprawdź, czy nie koliduje z regułami odpowiedzi w `CLAUDE.md` danego repo.

### Diagram Design: opcjonalnie

- **Dlaczego:** 45 typów diagramów w HTML/SVG, import z draw.io i Mermaid. Przydatne w `AI-crew` (schematy przepływu crew) i w projektach z diagramami draw.io.
- **Dlaczego nie od razu:** diagramów jest na razie mało. Wdrożyć, gdy pojawi się konkretna potrzeba.

### Lemo Opuscar: pilotaż tylko w projekcie treściowym z wideo

- **Dlaczego warto:** projekt i tak testuje narzędzia AI do wideo. Wideo generowane kodem (Canvas, WebGL, FFmpeg, synteza mowy Kokoro) to tańsza, powtarzalna alternatywa do porównania.
- **Dlaczego ostrożnie:** plugin zakłada model Opus, ma 2478 plików i generuje media. Koszty i każda publikacja wymagają zgody Ownera.
- **Jak:** jedno zadanie porównawcze na jednym krótkim filmie, z limitem kosztu i bez publikacji.

### Nie teraz

| Skill | Powód |
| --- | --- |
| **REA** | Dekompilacja binarek (Ghidra, APK, Electron). Żadne repo tego nie potrzebuje. Ryzyko naruszenia licencji i EULA cudzych aplikacji. Duży pakiet (ponad 7000 plików) |
| **Caveman** | Kompresuje *odpowiedzi* agenta, a koszt pracy agentów zależy głównie od kontekstu wejściowego, nie od wyjścia. Gorsza czytelność dla Ciebie (czytasz po polsku) i ryzyko utraty niuansów w przekazaniach między agentami. Instalacja przez `curl \| bash`. Lepsza dźwignia kosztu: poziom `effort` i krótki `CLAUDE.md` |
| **Animate (Animate.css)** | Brak projektu z frontendem webowym, który potrzebuje animacji. Brak pliku licencji w repo |
| **I have ADHD** | To preferencja osobista, nie projektowa, a jej reguły pokrywają się z Ponytailem. Jeśli chcesz „najpierw akcja”, dopisz 3–4 zdania do swojego `~/.claude/CLAUDE.md` zamiast instalować plugin z hookiem `SessionStart` |
| **Skills CLI (`npx skills add`)** | Format `SKILL.md` już stosujesz we wszystkich repo. Globalna instalacja omija PR i audyt. Wolimy ręczne kopiowanie z przypiętym SHA |

## 3. Bezpieczeństwo i koszty

- **Hooki uruchamiają kod przy każdej sesji.** Ponytail i I have ADHD rejestrują hooki `SessionStart` w Node.js. Instaluj je tylko po przeczytaniu kodu, nigdy przez `curl | bash`.
- **Wersjonowanie:** w każdym skopiowanym skillu dopisz w `README` lub w nagłówku źródło i SHA commita, z którego go wzięto. Aktualizacja to nowy PR.
- **Zakres:** instaluj na poziomie projektu (`.claude/skills/` w repo), nie globalnie. Dzięki temu skill działa tylko tam, gdzie ma sens, i nie zwiększa kontekstu w pozostałych repo (opis każdego skilla ładuje się do każdej sesji).
- **Repo publiczne:** skille z licencją MIT/Apache można w nich trzymać, zachowując plik licencji i informację o autorze.
- **Audyt:** przed pierwszym użyciem uruchom `skill-auditor` (repo `AI-agents`) na każdym skopiowanym skillu.

## 4. Plan wdrożenia

| Krok | Repo | Co zrobić | Kryterium sukcesu |
| --- | --- | --- | --- |
| 1 | Gra w Godot | Dodać 7 skilli Godot z pakietu gamedev | Agent uruchamia testy headless i eksport bez dopytywania |
| 2 | Aplikacja użytkowa w Godot | Dodać 4 skille Godot; sprawdzić zgodność z regułami projektu | Brak sprzeczności z regułami projektu |
| 3 | Projekt treściowy | Dodać Humanizer jako krok przeglądu tekstów publicznych | Owner akceptuje teksty z mniejszą liczbą poprawek |
| 4 | Projekty polskojęzyczne | Przetestować Humanizer na 3–5 polskich tekstach; wdrożyć, jeśli wynik jest dobry | Teksty brzmią naturalnie, bez utraty wierności źródłu |
| 5 | Projekty z kodem | Pilotaż Ponytaila (sam `SKILL.md`) na 10 zadaniach; porównać koszt i rozmiar zmian | Mniejszy diff i koszt na zadanie bez nowych błędów |
| 6 | Projekt treściowy z wideo | Zadanie pilotażowe Opuscar, za zgodą Ownera i z limitem kosztu | Zapisana decyzja |

## Źródła

- Raport wejściowy: [`resources/raport-10-skilli-dla-agentow-ai.md`](../resources/raport-10-skilli-dla-agentow-ai.md) (na podstawie filmu Aleksa Szacha)
- Repozytoria skilli, sprawdzone 3 listopada 2026: [morluto/rea](https://github.com/morluto/rea), [blader/humanizer](https://github.com/blader/humanizer), [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), [msrbuilds/animate-css-skill](https://github.com/msrbuilds/animate-css-skill), [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design), [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
- Przegląd projektów Ownera (3 listopada 2026)
- [Raport AI-crew z 31 października 2026](../outputs/2026-10-31-efficient-ai-crew-and-repo-setup.md): zasady kosztów, egzekwowania reguł i zatrudniania skilli
