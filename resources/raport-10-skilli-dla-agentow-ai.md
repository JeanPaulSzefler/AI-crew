# Raport i Transkrypcja: 10 Kluczowych Skilli dla Agentów AI

**Oryginalny materiał wideo:** [Install These 10 Skills Before You Run Your AI Agent Again](https://www.youtube.com/watch?v=BWy1PjJoVek)  
**Autor:** Aleks Szach (@aleks_szach)  
**Sponsor/Partner materiału:** Hostinger (Hermes AI Agent on VPS)

---

## Część 1: Struktura i Transkrypcja Filmu (Timestampy)

Film przedstawia 10 zestawów umiejętności (tzw. *Agent Skills* lub *MCP Skills*), które drastycznie podnoszą wydajność, precyzję, estetykę oraz efektywność kosztową podczas pracy z agentami kodującymi i automatyzującymi (np. Claude Code, Codex, Cursor, Gemini CLI).

| Czas (Timestamp) | Moduł / Temat | Opis zawartości |
| :--- | :--- | :--- |
| **00:00** | **Wstęp** | Wprowadzenie do pojęcia *Agent Skills*. Dlaczego samo używanie podpowiedzi (promptów) to za mało i jak dedykowane umiejętności zmieniają zachowanie agentów AI. |
| **01:03** | **1. REA (Reconstruction Architecture)** | Inżynieria wsteczna dla agentów AI. Jak agent analizuje istniejące aplikacje i odtwarza funkcjonalności. |
| **02:56** | **2. Humanizer** | Wykrywanie i usuwanie wzorców stylistyki generowanej przez AI (*AI slop*), przywracanie ludzkiego tonu w tekstach i kodzie. |
| **04:20** | **Hostinger & Hermes Agent** | Segment sponsorowany: Wdrożenie i uruchomienie agenta Hermes na serwerze VPS Hostinger. |
| **06:38** | **3. Agent Skills (Framework)** | Standardy i ekosystem instalacji skilli (Skills CLI / MCP) w środowiskach deweloperskich. |
| **08:21** | **4. Ponytail** | Odwrócenie filozofii kodowania – narzucenie agentowi zasady pisania minimalnej ilości kodu i wykorzystywania istniejących funkcji. |
| **09:40** | **5. Caveman** | Ekstremalna kompresja tokenów. Skracanie wypowiedzi agenta bez utraty danych technicznych i kodu. |
| **11:04** | **6. Animate (Animate.css Skill)** | Wdrażanie responsywnych animacji w HTML/JSX z uwzględnieniem dostępności i ruchu. |
| **12:35** | **7. Diagram Design** | Tworzenie edytorskich schematów architektury (HTML/SVG) bez szumu wizualnego. |
| **13:45** | **8. Awesome Gamedev Agent Skills** | Optymalizacja wydajności gier oraz pętla tworzenia tzw. *game feel* (juice, screen shake, hit-stop). |
| **15:05** | **9. Lemo Opuscar** | Generowanie wideo ze zdefiniowanym stylem w całości za pomocą kodu i Claude Opus. |
| **16:39** | **10. I have ADHD** | Przekształcanie odpowiedzi AI na model "Action First" – brak zbędnych wstępów, numerowane kroki, czysta treść. |
| **17:50** | **Podsumowanie** | Zestawienie korzyści i rekomendowana kolejność instalacji. |

---

## Część 2: Rozszerzona Analiza 10 Skilli dla Agentów AI

Poniższa sekcja rozbudowuje wiedzę zawartą w filmie o oficjalną dokumentację, repozytoria GitHub oraz dane techniczne ze źródeł zewnętrznych.

---

### 1. REA (Reconstruction Architecture)
* **Autor / Repozytorium:** [morluto/rea](https://github.com/morluto/rea)
* **Typ:** Inżynieria wsteczna i dekompilacja oparta na dowodach (Evidence-Based Reverse Engineering)
* **Główne cechy:**
  * Pozwala agentowi przeanalizować plik wykonywalny lub paczkę (Mach-O, ELF, PE, APK, Electron, zbiory ZIP/ASAR) za pomocą silników dekompilacji (Ghidra, Hopper).
  * Agent nie klonuje kodu źródłowego, lecz bada relacje, ciągi znaków (strings), symbole oraz pseudokod, aby wyjaśnić zasady działania danej funkcji i dopasować ją do Twojego stosu technologicznego.
  * Zapewnia protokół serwera MCP (Model Context Protocol), dzięki czemu Claude Code czy Cursor mogą bezpośrednio wydawać polecenia dekompilacji i analizować logi.
* **Komenda instalacyjna:**
  ```bash
  npx --yes rea-agents@latest setup
  ```
* **Źródło:** [REA na Dev.to & GitHub](https://dev.to/arshtechpro/rea-let-your-ai-agent-reverse-engineer-the-app-features-you-wish-you-had-3en7)

---

### 2. Humanizer
* **Autor / Repozytorium:** [blader/humanizer](https://github.com/blader/humanizer)
* **Typ:** Optymalizacja i stylizacja tekstu (Anti-AI Slop)
* **Główne cechy:**
  * Oparty na wytycznych Wikipedii *Signs of AI writing* (znaki rozpoznawcze tekstu generowanego przez LLM).
  * Wykrywa i eliminuje 26 typowych schematów sztucznej inteligencji, m.in.:
    * Kontrasty typu *"Not X, but Y"* (np. *"To nie tylko funkcja, to zmiana paradygmatu"*).
    * Jednolijnikowe podsumowania końcowe (*"Let that sink in"*).
    * Sztuczne triady (wymyślanie 3 elementów w zdaniu na siłę).
    * Nadmierne używanie pauz (em-dash) oraz zbędne wstępy.
  * Dopasowuje rytm, interpunkcję i słownictwo do unikalnego stylu użytkownika na podstawie podanego próbka tekstu.
* **Komenda instalacyjna:**
  ```bash
  npx skills add blader/humanizer --global
  ```
* **Źródło:** [GitHub - blader/humanizer](https://github.com/blader/humanizer)

---

### 3. Agent Skills / Skills CLI (Framework Standard)
* **Autor / Repozytorium:** Ekosystem `skills.sh` / `addie/agent-skills`
* **Typ:** Uniwersalna infrastruktura zarządzania kontekstem agentów
* **Główne cechy:**
  * Zapewnia standaryzowany interfejs ładowania instrukcji (w formacie `SKILL.md`) dla agentów takich jak Claude Code, Codex, Cursor, Gemini CLI czy Windsurf.
  * Umożliwia dynamiczne wczytywanie zestawów wiedzy tylko wtedy, gdy zadanie tego wymaga, zapobiegając przepełnieniu okna kontekstowego (Context Window).
* **Komenda instalacyjna:**
  ```bash
  npx skills@latest add <repo/skill-name>
  ```
* **Źródło:** [Skills.sh Registry](https://skills.sh)

---

### 4. Ponytail
* **Autor / Repozytorium:** [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
* **Typ:** Inżynieria oprogramowania i minimalizm kodu
* **Główne cechy:**
  * Wdraża zasadę *"Najlepszy kod to ten, którego nie napisano"*.
  * Posiada tzw. **Drabinę Decyzyjną (Decision Ladder)**. Zanim agent napisze nową funkcję, sprawdzi w kolejności:
    1. Czy zadanie można pominąć lub uprościć?
    2. Czy w istniejącym kodzie projektu istnieje już pomocnicza funkcja?
    3. Czy funkcja znajduje się w bibliotece standardowej / natywnym API?
    4. Pisanie własnego kodu jest traktowane jako ostateczność.
  * **Osiągi:** Średnio o 54% mniej wygenerowanego kodu, 27% szybsza odpowiedź agenta oraz 20% redukcja zużycia tokenów.
* **Komenda instalacyjna:**
  ```bash
  npx skills add DietrichGebert/ponytail -g
  ```
* **Źródło:** [Ponytail na AgentConn](https://agentconn.com/skills/ponytail/)

---

### 5. Caveman
* **Autor / Repozytorium:** [JuliusBrussee/skills](https://github.com/juliusbrussee/skills) (podkatalog `caveman`)
* **Typ:** Ekstremalna kompresja odpowiedzi (Token Compression)
* **Główne cechy:**
  * Działa w oparciu o zasadę *"Small mouth, big brain"*.
  * Drastycznie redukuje liczbę tokenów wyjściowych generowanych przez agenta poprzez usunięcie zwrotów grzecznościowych, wyrazów łącznikowych i zbędnej gramatyki.
  * Zachowuje w 100% precyzję komend terminala, fragmentów kodu, komunikatów błędów oraz nazewnictwa API.
* **Komenda instalacyjna:**
  ```bash
  curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
  ```
* **Źródło:** [JuliusBrussee GitHub](https://github.com/juliusbrussee/skills)

---

### 6. Animate (Animate-CSS Skill)
* **Autor / Repozytorium:** [msrbuilds/animate-css-skill](https://github.com/msrbuilds/animate-css-skill)
* **Typ:** Frontend & Interfejs użytkownika
* **Główne cechy:**
  * Pozwala agentom automatycznie dodawać płynne animacje `Animate.css` do szablonów HTML, React (JSX) oraz WordPress PHP.
  * Automatycznie dołącza wykrywanie kierunku tekstu (RTL), wyzwalacze podczas przewijania (scroll-trigger) oraz respektuje ustawienia systemowe `prefers-reduced-motion` dla wygody użytkowników wrażliwych na ruch.
  * Wyciąga tylko potrzebne fragmenty CSS, zamiast ładować pełną, ciężką bibliotekę.
* **Instalacja w Claude Code:**
  ```bash
  mkdir -p ~/.claude/skills/animate-css
  cp -r animate-css-skill/* ~/.claude/skills/animate-css/
  ```
* **Źródło:** [GitHub - msrbuilds/animate-css-skill](https://github.com/msrbuilds/animate-css-skill)

---

### 7. Diagram Design
* **Autor / Repozytorium:** [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
* **Typ:** Architektura i Wizualizacja
* **Główne cechy:**
  * Pozwala agentom tworzyć 45 typów profesjonalnych schematów i diagramów w czystym formacie HTML + SVG.
  * Zastępuje bezbarwne i przestarzałe diagramy Mermaid unikalnym, przejrzystym stylem edytorskim.
  * Wspiera import i eksport danych z Mermaid, draw.io oraz Excalidraw.
* **Komenda instalacyjna:**
  ```bash
  npx skills add cathrynlavery/diagram-design -g
  ```
* **Źródło:** [Cathryn Lavery GitHub](https://github.com/cathrynlavery)

---

### 8. Awesome Gamedev Agent Skills
* **Autor / Repozytorium:** [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)
* **Typ:** Game Development & Optymalizacja Silników (Godot, Unity, Unreal)
* **Główne cechy:**
  * Uczy agenta zasad *Game Feel* (efekty "Juice": drgania kamery / screen shake, hit-stop, interpolacja tweening, reakcje wizualne).
  * Systematyczny proces optymalizacji wydajności (Performance Optimization Loop): profilowanie wątków CPU vs GPU, pula obiektów (Object Pooling), redukcja wywołań rysowania (Draw Calls) oraz kontrola alokacji pamięci.
* **Źródło:** [GitHub - gamedev-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)

---

### 9. Lemo Opuscar
* **Autor / Repozytorium:** [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)
* **Typ:** Programistyczna generacja wideo i reżyseria kodu
* **Główne cechy:**
  * Wtyczka przeznaczona dla modelu Claude Opus (np. Opus 5.5).
  * Zawiera ponad 60 gotowych stylów wizualnych wideo. Agent tworzy krótkie materiały wideo **w całości pisząc kod** (Canvas, WebGL, FFmpeg, Node.js, Python oraz syntezę mowy Kokoro).
  * Pozwala na interaktywną reżyserię krok po kroku (tworzenie scenorysu/storyboardu, zmiana palety barw i tempa).
* **Komenda instalacyjna:**
  ```bash
  claude plugin marketplace add lemomo-ai/lemo-opuscar
  claude plugin install lemo-opuscar@lemolab
  ```
* **Źródło:** [GitHub - lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

---

### 10. I have ADHD
* **Autor / Repozytorium:** [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
* **Typ:** Formatowanie odpowiedzi i produktywność (Action-First Communication)
* **Główne cechy:**
  * Opracowany na podstawie zasad Terapii Poznawczo-Behawioralnej z książki *The Adult ADHD Tool Kit*.
  * Narzuca agentowi 10 żelaznych reguł komunikacji:
    1. **Pierwsza linijka to natychmiastowa akcja** (kod, komenda lub konkretny krok – zero wstępów typu *"Chętnie pomogę!"*).
    2. **Numerowane kroki** przy zadaniach wieloetapowych.
    3. **Ograniczenie list do max 5 pozycji**.
    4. **Przypominanie stanu sesji** (np. *"Krok 2 z 4 ukończony"*).
    5. Brak pożegnalnych uprzejmości (*"Mam nadzieję, że to pomogło!"*).
    6. Podawanie konkretnego szacowanego czasu wykonania (np. *"Około 5 minut"*).
* **Komenda aktywacji:**
  ```text
  /i-have-adhd
  ```
* **Źródło:** [GitHub - ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

---

## Tabela Porównawcza Skilli

| Nazwa Skilla | Główna Kategoria | Cel Wdrożenia | Kluczowa Korzyść |
| :--- | :--- | :--- | :--- |
| **REA** | Reverse Engineering | Analiza obcych aplikacji | Inżynieria wsteczna bez utraty kontekstu |
| **Humanizer** | Copywriting / Tekst | Usuwanie stylu AI | Naturalne brzmienie materiałów pisanym przez AI |
| **Ponytail** | Architektura Kodu | Minimalizacja kodu | -54% kodu, -20% kosztów tokenów |
| **Caveman** | Kompresja Promptu | Oszczędność tokenów | Zwięzłe odpowiedzi deweloperskie |
| **Animate** | Frontend UI | Dostępne animacje | Płynny interfejs bez obciążania strony |
| **Diagram Design** | Wizualizacja | Schematy HTML/SVG | Profesjonalny wygląd diagramów architektury |
| **Awesome Gamedev** | GameDev | Game Feel i Profilowanie | Brak zgadywania przy optymalizacji gier |
| **Lemo Opuscar** | Video / Media | Generowanie wideo kodem | Filmy zoptymalizowane pod model Opus |
| **I have ADHD** | UX Odpowiedzi AI | Odpowiedzi "Action First" | Brak szumu informacyjnego, czyste kroki |

---

## Jak Pobrać Ten Raport? / How to Download This Report?

**Wskazówka (PL):**
Raport został wygenerowany jako pełnoprawny plik `.md` w prawej części ekranu w interaktywnym edytorze. 
* Aby go pobrać: Kliknij przycisk **Eksportuj / Pobierz (ikona pobierania)** znajdujący się w prawym górnym rogu panelu edytora po prawej stronie.
* Możesz również bezpośrednio skopiować całą treść kodu Markdown.

**Instructions (EN):**
This report is generated as a standalone `.md` file inside the document editor on the right side of your screen.
* To download: Click the **Download / Export icon** located at the top right of the editor panel.
* Alternatively, you can copy the raw Markdown source code directly from the editor panel.