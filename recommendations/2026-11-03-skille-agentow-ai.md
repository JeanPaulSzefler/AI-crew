# Rekomendacja: które z 10 skilli dla agentów AI warto wdrożyć

3 listopada 2026 · Na podstawie [`resources/raport-10-skilli-dla-agentow-ai.md`](../resources/raport-10-skilli-dla-agentow-ai.md) i przeglądu wszystkich 10 repozytoriów JeanPaulSzefler

## W skrócie

| Decyzja | Skill | Gdzie |
| --- | --- | --- |
| **Wdrożyć** | Awesome Gamedev Agent Skills (tylko wybrane skille Godot) | `education-games`, `learning_tools/godot` |
| **Wdrożyć** | Humanizer | `educationInfluencer`, `foz-zoe`, `klasa6`, `AI-crew` (treści dla ludzi) |
| **Wdrożyć po audycie** | Ponytail (sam `SKILL.md`, bez hooków) | `learning_tools`, `education-games`, przyszły kod `AI-crew` |
| **Opcjonalnie** | Diagram Design | `AI-crew` (diagramy architektury), ewentualnie `doktorat_git` |
| **Pilotaż za zgodą Ownera** | Lemo Opuscar | tylko `educationInfluencer`, jako porównanie z Higgsfield |
| **Nie teraz** | REA, Caveman, Animate, I have ADHD, Skills CLI jako instalator | — |

Ogólna zasada: skille **kopiujemy do `.claude/skills/` konkretnego repo z przypiętą wersją** (commit SHA) zamiast instalować globalnie przez `npx … --global` czy `curl | bash`. Każdy nowy skill przechodzi przez PR i audyt `skill-auditor` z repo [`AI-agents`](https://github.com/JeanPaulSzefler/AI-agents). To jest reguła „zatrudniania” z blueprintu AI-crew.

## 1. Co jest w Twoich repozytoriach

| Repo | Co zawiera | Stan agentowy | Potrzeby, w które mogą trafić skille |
| --- | --- | --- | --- |
| `learning_tools` (prywatne) | Aplikacja do drillu egzaminów (JS w przeglądarce + Godot 4.7 na Androida), banki pytań ITIL 4, wiki | `CLAUDE.md`, 6 skilli, decyzje (ADR) | Kod JS i GDScript, testy Godota, eksport APK |
| `education-games` (publiczne) | Gra `junk-vs-plants` w Godot 4.7 (Mobile): profile, zapisy z migracjami, wydarzenia, ogród, ENet, grafiki | — | Game feel, wydajność, zapisy, multiplayer, eksport na Androida |
| `educationInfluencer` (prywatne) | Fikcyjny influencer AI: reels, napisy (SRT), wiki trendów, propozycje | `CLAUDE.md` w STE en-GB, 4 agentów (CEO/xdev/team/translator), 9 skilli | Teksty publiczne bez „AI slop”, wideo |
| `klasa6` (prywatne) | Wymagania i materiały klasy VI wg podstawy programowej, Google Drive | `CLAUDE.md`, 11 skilli po polsku | Materiały dla ucznia i rodzica pisane naturalnie |
| `FOZ-ZOE` (publiczne) | Konspekty spotkań kręgów Domowego Kościoła, druk, Google Drive | Instrukcja dla agenta AI w Markdown | Teksty po polsku dla ludzi |
| `AI-agents` (publiczne) | Agent `skill-auditor` i README pakietu `skill-optimizer` | Standard audytu skilli | Narzędzie do oceny każdego nowego skilla |
| `AI-crew` (publiczne) | Ten repo: research i blueprinty crew | Raporty i blueprinty | Diagramy, raporty, przyszły kod |
| `doktorat_git` (publiczne) | Materiały doktoratu: docx, pdf, 38 plików draw.io, wykresy | Brak; ostatnia zmiana 2025-10 | Diagramy, ale repo jest nieaktywne |
| `favorites_training`, `git_training_github` | Ćwiczenia z gita z 2021 r. (1–3 pliki) | — | Brak |

Wniosek: masz **dwa projekty Godot** (`education-games`, `learning_tools/godot`), **trzy projekty treściowe** z publicznymi tekstami (`educationInfluencer`, `klasa6`, `FOZ-ZOE`) i **już dojrzały standard skilli** (`AI-agents`, oraz 26 skilli w trzech repo). Nie masz frontendu webowego z animacjami, aplikacji do dekompilowania ani produkcji wideo poza `educationInfluencer`.

## 2. Ocena każdego skilla

Wszystkie 10 repozytoriów istnieje i jest aktywnie rozwijanych (ostatnie commity od kwietnia do listopada 2026). Licencje: MIT lub Apache-2.0, z wyjątkiem `animate-css-skill`, który nie ma pliku licencji.

### Awesome Gamedev Agent Skills: wdrożyć wybiórczo

- **Dlaczego:** pakiet ma 16 skilli Godot (m.in. `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `godot-ui-control`, `godot-multiplayer`) oraz dyscypliny (`game-feel`, `performance-optimization`, `save-systems`). To pasuje dokładnie do `junk-vs-plants` (zapisy z migracjami do v5, ENet, Android) i do klienta Godot w `learning_tools`.
- **Jak:** nie instaluj całego pakietu (251 plików, router). Skopiuj 6–8 potrzebnych skilli do `.claude/skills/` każdego repo Godot.
- **Pierwszy zestaw dla `education-games`:** `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `save-systems`, `game-feel`, `performance-optimization`, `godot-multiplayer`.
- **Dla `learning_tools`:** `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-export`, `godot-ui-control`. Tam decyzja 0007 wymaga zgodności z `app/engine.js`, więc skille Godot nie mogą nadpisywać tej reguły.

### Humanizer: wdrożyć do treści dla ludzi

- **Dlaczego:** `educationInfluencer` publikuje reels i napisy, a jego własna wiki zbiera materiał o „AI slop backlash”. `klasa6` i `FOZ-ZOE` tworzą teksty czytane przez uczniów, rodziców i małżeństwa. Humanizer (397 linii, MIT, v3.1.0) wyłapuje m.in. kontrasty „nie X, lecz Y”, sztuczne triady, jednozdaniowe puenty, nadmiar myślników.
- **Język polski:** wzorce są opisane po angielsku, ale skill wprost mówi, że te same konstrukcje występują w każdym języku. Przed wdrożeniem w `klasa6` i `FOZ-ZOE` przetestuj go na 3–5 istniejących polskich tekstach.
- **Zgodność z STE:** w `educationInfluencer` pliki wewnętrzne pisane są w Simplified Technical English. Humanizer nie zastępuje STE. Używaj go tylko na etapie przeglądu tekstów publicznych (opisy, napisy, posty), przed akceptacją Ownera.
- **Jak:** jako krok w istniejących skillach przeglądu (`task-review`, `reel-dossier`, `weryfikacja-wiernosci`), nie jako tryb zawsze włączony.

### Ponytail: wdrożyć po audycie, sam skill

- **Dlaczego:** reguła „najmniejsza kompletna zmiana” jest zbieżna z rekomendacjami AI-crew (krótki kod, recenzja bez stylu, koszt na zadanie). Przyda się przy vibe-codingu w `education-games` i w kodzie `learning_tools`.
- **Uwaga 1:** pełny plugin rejestruje hooki `SessionStart` i `SubagentStart` (Node.js), linię statusu i moduł „band” z opcjonalnym webhookiem. To więcej niż skill. Zacznij od samego `skills/ponytail/SKILL.md`; hooki dopiero po audycie.
- **Uwaga 2:** liczby z raportu (−54% kodu, −20% tokenów) pochodzą z benchmarków autora. Zweryfikuj je własnym logiem kosztu na zadanie (sekcja 7 raportu AI-crew).
- **Uwaga 3:** Ponytail ustawia też styl odpowiedzi („jedna–dwie linie na końcu”). Sprawdź, czy nie koliduje z regułami odpowiedzi w `CLAUDE.md` danego repo.

### Diagram Design: opcjonalnie

- **Dlaczego:** 45 typów diagramów w HTML/SVG, import z draw.io i Mermaid. Przydatne w `AI-crew` (schematy przepływu crew) i potencjalnie w `doktorat_git` (38 plików draw.io).
- **Dlaczego nie od razu:** `doktorat_git` jest nieaktywne od roku. W `AI-crew` diagramów jest na razie mało. Wdrożyć, gdy pojawi się konkretna potrzeba.

### Lemo Opuscar: pilotaż tylko w educationInfluencer

- **Dlaczego warto:** projekt i tak testuje narzędzia AI do wideo (Higgsfield). Wideo generowane kodem (Canvas, WebGL, FFmpeg, synteza mowy Kokoro) to tańsza, powtarzalna alternatywa do porównania.
- **Dlaczego ostrożnie:** plugin zakłada model Opus, ma 2478 plików i generuje media. Reguły `educationInfluencer` wymagają zgody Ownera na koszty i na każdą publikację, a assety muszą mieć status `APPROVED` w `wiki/assets-register.md`.
- **Jak:** jedno zadanie w `tasks/` („porównać Opuscar z Higgsfield na jednym reelu”), z limitem kosztu i bez publikacji.

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
- **Repo publiczne:** `education-games`, `FOZ-ZOE`, `AI-agents`, `AI-crew` są publiczne. Skille z licencją MIT/Apache można w nich trzymać, zachowując plik licencji i informację o autorze.
- **Audyt:** przed pierwszym użyciem uruchom `skill-auditor` (repo `AI-agents`) na każdym skopiowanym skillu.

## 4. Plan wdrożenia

| Krok | Repo | Co zrobić | Kryterium sukcesu |
| --- | --- | --- | --- |
| 1 | `education-games` | Dodać 7 skilli Godot z pakietu gamedev | Agent uruchamia testy headless i eksport bez dopytywania |
| 2 | `learning_tools` | Dodać 4 skille Godot; sprawdzić zgodność z decyzją 0007 | Brak sprzeczności z `app/engine.js` w kolejnej zmianie SPEC-004 |
| 3 | `educationInfluencer` | Dodać Humanizer jako krok w `task-review` dla tekstów publicznych | Owner akceptuje teksty z mniejszą liczbą poprawek |
| 4 | `klasa6`, `FOZ-ZOE` | Przetestować Humanizer na 3–5 polskich tekstach; wdrożyć, jeśli wynik jest dobry | Teksty brzmią naturalnie, bez utraty wierności źródłu |
| 5 | `learning_tools`, `education-games` | Pilotaż Ponytaila (sam `SKILL.md`) na 10 zadaniach; porównać koszt i rozmiar zmian | Mniejszy diff i koszt na zadanie bez nowych błędów |
| 6 | `educationInfluencer` | Zadanie pilotażowe Opuscar vs Higgsfield, za zgodą Ownera i z limitem kosztu | Decyzja w `journal/` |

## Źródła

- Raport wejściowy: [`resources/raport-10-skilli-dla-agentow-ai.md`](../resources/raport-10-skilli-dla-agentow-ai.md) (na podstawie filmu Aleksa Szacha)
- Repozytoria skilli, sprawdzone 3 listopada 2026: [morluto/rea](https://github.com/morluto/rea), [blader/humanizer](https://github.com/blader/humanizer), [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), [msrbuilds/animate-css-skill](https://github.com/msrbuilds/animate-css-skill), [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design), [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
- Przegląd 10 repozytoriów JeanPaulSzefler (płytkie klony gałęzi domyślnych, 3 listopada 2026)
- [Raport AI-crew z 31 października 2026](../outputs/2026-10-31-efficient-ai-crew-and-repo-setup.md): zasady kosztów, egzekwowania reguł i zatrudniania skilli
