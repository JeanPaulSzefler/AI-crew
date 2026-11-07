# Raport: Poradnik Orkiestracji Agentów AI (Herder + Claude Code + Codex + Hermes) oraz Analiza Oferty Hostinger

---

## 1. Raport i Analiza Filmu: „Jak Ustawić Herdr dla Kilku Agentów AI. Pełny Poradnik”

**Kanał:** Aleks Szach  
**Link do filmu:** [YouTube - Jak Ustawić Herdr dla Kilku Agentów AI](http://www.youtube.com/watch?v=PlLK_EEjjcA)

---

### A. Opis i Zestawienie Wszystkich Instrukcji z Filmu

Film instruktażowy prezentuje sposób konfiguracji i orkiestracji zespołu wieloagentowego AI (złożonego z agentów: **Claude Code**, **Codex** oraz **Hermes Agent**) zarządzanego przez system **Herder** uruchomiony na zdalnym serwerze VPS (Hostinger).

#### KROK 1: Przygotowanie Środowiska Serwerowego (Hostinger VPS)
1. **Wybór serwera:** Zaloguj się na Hostinger i wybierz plan **VPS KVM 2** (lub KVM 4 dla większej liczby agentów).
2. **Instalacja szablonu:** Podczas wstępnej konfiguracji serwera wybierz gotowy szablon systemowy **Hermes Agent** (zamiast ręcznej instalacji czystej dystrybucji Linuxa).
3. **Zabezpieczenie:** Ustaw i zapisz w bezpiecznym miejscu (np. managerze haseł) hasło administratora (`root`).

#### KROK 2: Instalacja i Konfiguracja Aplikacji Herder
1. Pobierz ze strony Herdera dedykowaną aplikację desktopową (dostępną dla Windows, macOS, Linux).
2. Po pierwszym uruchomieniu i przejściu wstępnego samouczka (wybór motywu), dodaj nową maszynę w zakładce podając:
   * **Username:** `root`
   * **Host/IP:** Adres IP VPS uzyskany z panelu hPanel
3. Połącz się podając zapisane wcześniej hasło root (opcjonalnie skonfiguruj klucze SSH do logowania bezhasłowego).
4. **Tworzenie struktury katalogów:** Na serwerze utwórz dedykowany folder roboczy dla projektu, w którym będą operować wszyscy agenci.

#### KROK 3: Instalacja Agentów CLI (Claude Code & Codex)
1. **Instalacja Claude Code:**
   * Przejdź do głównej przestrzeni (`root`), wklej komendę instalacyjną i uruchom polecenie `claude` (w przypadku komunikatu *command not found*, użyj komendy przeładowującej ścieżki środowiskowe PATH).
   * Przeprowadź autoryzację: otwórz wygenerowany w terminalu link w przeglądarce, zaloguj się do konta Anthropic i wklej kod autoryzacyjny z powrotem do Herdera.
2. **Instalacja Codex:**
   * Wklej komendę instalacyjną i uruchom polecenie `codex`.
   * Wybierz logowanie kodem (browser code login), co pozwoli powiązać instancję z już posiadaną subskrypcją zamiast podawania klucza API.

#### KROK 4: Izolacja i Podłączenie Hermesa (Docker)
1. Hermes Agent działa domyślnie w odizolowanym kontenerze Docker.
2. W panelu Hostinger przejdź do **Docker Manager -> Projects -> Hermes Agent -> Edit YAML**.
3. W sekcji `volumes` dopisz montowanie ścieżki folderu projektu (np. `- /root/moj-projekt:/workspace`), a następnie kliknij **Wdróż** (Deploy).
4. **Uprawnienia i skróty:** Nadaj kontenerowi prawa do zapisu w folderze projektu za pomocą komendy z dedykowanego przewodnika.
5. Dodaj skrót wywołania kontenera Hermesa na serwerze, aby pojawił się w Herderze pod skrótem numerycznym (np. przycisk `3`).

#### KROK 5: Instalacja Skilla `herder-core` i Wieloagentowa Orkiestracja
1. W przestrzeni `root` zainstaluj oficjalny skill `herder-core` przypisany do głównego agenta (np. Claude Code).
2. Uruchom Claude Code w folderze projektu i wywołaj go poleceniem:
   > *"Użyj skilla herder-core, aby uruchomić Codexa i Hermesa w tym projekcie i razem stwórzcie [nazwa zadania]..."*
3. **Podział ról w przykładzie z filmu:**
   * **Hermes Agent:** Odczytuje prywatne notatki (np. z aplikacji Obsidian) i wyciąga wskaźniki wydajności filmów YouTube.
   * **Codex:** Przetwarza surowe dane wyciągnięte przez Hermesa i tworzy z nich ranking.
   * **Claude Code (Szef/Lider):** Nadzoruje pracę pod-agentów, zbiera ich raporty i buduje stronę internetową prezentującą wyniki.

---

### B. Komentarz i Ocena Techniczna

1. **Przejście z CLI na Herder Core (Daemon Architecture):**  
   Kluczowym konceptem przedstawionym w filmie jest architektura rozdzielenia interfejsu GUI od procesu wykonawczego (`Herder Core`). Odcięcie połączenia lokalnego komputera lub zamknięcie okna aplikacji nie przerywa wykonywania zadań przez agentów na VPS. Jest to zasadnicza przewaga nad standardowym uruchamianiem agentów w zwykłych sesjach SSH terminala.

2. **Zasada "Cross-Checking" (Agent-Weryfikator):**  
   Praca w pętli jednoliniowej (gdzie ten sam model ocenia swój kod) często prowadzi do "halucynacyjnej ślepoty" na własne błędy. Użycie Codexa do weryfikacji i układania logiki obok piszącego kod Claude'a dramatycznie podnosi jakość wyjściowych skryptów i aplikacji.

3. **Bezpieczeństwo Kontenera Docker:**  
   Decyzja o trzymaniu Hermesa w kontenerze z ograniczonym podmontowanym wolumenem (`volumes`) stanowi istotny zabieg bezpieczeństwa. Ponieważ autonomiczny agent potrafi sam pobierać biblioteki i uruchamiać skrypty z sieci, ograniczenie jego dostępu do wyłącznie jednego folderu roboczego zapobiega przypadkowemu uszkodzeniu całego systemu VPS.

---

## 2. Dopełnienie Raportu: Powiązane Wzorce i Dodatkowe Konfiguracje

Aby dopełnić raport o wartościowe techniki i alternatywne konfiguracje zespołów AI agentów, warto uwzględnić materiały dotyczące pełnej autonomii oraz zarządzania pamięcią agenta Hermes.

### Sekcja A: Budowanie Architektury "Hermes Agent" od Podstaw
* **Zakres tematyczny:** Konfiguracja Hermesa od stanu czystego serwera do podłączenia zewnętrznych baz wiedzy.
* **Kluczowy dodatek do raportu:** Hermes wyposażony jest w moduł **Persistent Memory & Skills Hub**. O ile Claude i Codex po zamknięciu sesji gubią kontekst i muszą odczytywać pliki na nowo, o tyle Hermes zapisuje nowo wyuczone umiejętności i nawyki w trwałym magazynie wiedzy, rozwijając się wraz z kolejnymi zadaniami.

### Sekcja B: Alternatywny Wzorzec "Cross-Validation Pipeline" (Pętla Recenzji)
* **Praktyka programistyczna:** Zamiast równoległego podziału zadań, agenci pracują w trybie sekwencyjnym:
  1. **Agent 1 (Claude Code):** Pisze pierwotny kod i testy jednostkowe.
  2. **Agent 2 (Codex):** Wykonuje Code Review, szukając podatności bezpieczeństwa i wąskich gardeł.
  3. **Agent 3 (Hermes):** Automatyzuje wdrożenie (CI/CD) i powiadamia użytkownika przez Telegram lub Discord.

---

## 3. Oferta Hostinger – Możliwości i Ograniczenia w Kontekście Agentów AI (Hermes, Claude, Codex)

Hostinger oferuje dedykowane plany **VPS KVM z wbudowanymi szablonami AI (np. Managed Hermes Agent)**.

---

### A. Przegląd Planów i Parametrów VPS

| Plan VPS | vCPU | RAM | Dysk (NVMe) | Bandwidth | Zastosowanie w AI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **KVM 1** | 1 rdzeń | 4 GB | 50 GB | 4 TB | 1 agent (np. samodzielny Hermes) |
| **KVM 2** *(Rekomendowany)* | 2 rdzenie | 8 GB | 100 GB | 8 TB | Zespół 2–3 agentów (Hermes + Claude CLI + Codex) |
| **KVM 4** | 4 rdzenie | 16 GB | 200 GB | 16 TB | Wieloagentowa orkiestracja, operacje na dużych zbiorach danych |
| **KVM 8** | 8 rdzeni | 32 GB | 400 GB | 32 TB | Środowiska produkcyjne / zaawansowane kontenery |

---

### B. Możliwości Oferty Hostinger dla Agentów AI

1. **Wdrożenie jednym kliknięciem (One-Click AI Templates):**  
   Dedykowany obraz systemowy instaluje środowisko Docker, agenta Hermes oraz niezbędne biblioteki w kilka minut bez potrzeby znajomości administracji serwerem Linux.

2. **Wydajność pamięci masowej (NVMe SSD):**  
   Agenci tacy jak Hermes i Claude nieustannie odczytują i zapisują pliki lokalne (notatki, kod, bazę wektorową). Zastosowanie dysków NVMe wyeliminowało wąskie gardła operacji I/O.

3. **Multi-platform Messaging Integrations:**  
   Dzięki infrastrukturze serwerowej Hermes uruchomiony na Hostingerze potrafi równolegle utrzymywać połączenie z komunikatorami Telegram, Discord, Slack, WhatsApp czy e-mail.

4. **Kredyty AI & Integracja OpenRouter / direct LLM:**  
   Hostinger oferuje wbudowane pakiety kredytów AI oraz obsługę ponad 200 modeli LLM (poprzez OpenRouter lub bezpośrednie klucze API od OpenAI / Anthropic).

---

### C. Ograniczenia i Wyzwania (W tym Kontekst Hermesa i Agentów)

1. **Brak sprzętowego wspomagania GPU:**  
   Plany VPS Hostinger oparte są na procesorach CPU (AMD EPYC). Nie nadają się do lokalnego uruchamiania dużych modeli otwartych (np. Llama 3 70B czy Mistral w całości na VPS). Agenci **muszą polegać na zewnętrznych API** (OpenAI, Anthropic, OpenRouter).

2. **Zarządzanie Pamięcią RAM przy Wielu Agentach:**  
   Mimo że agenci wykonują wywołania API, lokalne środowiska (Node.js dla Claude Code, pythonowe środowiska Hermesa, procesy budowania w Dockerze) potrafią szybko zużyć pamięć. Plan KVM 1 (4 GB RAM) może zapychać się przy jednoczesnej pracy 3 agentów w Herderze, stąd zalecenie minimum KVM 2 lub KVM 4.

3. **Limit I-węzłów i Przepustowości:**  
   Choć transfer jest wysoki (od 4 TB do 32 TB), intensywne automatyczne przeglądanie stron (web scraping) oraz ciągłe pobieranie pakietów przez agentów może w skrajnych przypadkach natrafić na wycieki pamięci lub obostrzenia sieciowe.

4. **Model Zarządzany vs VPS (Managed vs Root VPS):**  
   W wersji *Managed Hermes* użytkownik otrzymuje wygodny interfejs webowy, ale ma ograniczony dostęp do pełnych modyfikacji OS. Z kolei na pełnym VPS z rootem trzeba samodzielnie dbać o podstawowe konfiguracje bezpieczeństwa sieciowego (mimo obecności ochrony DDoS w cenie).