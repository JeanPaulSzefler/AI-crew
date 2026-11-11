# Koncepcja AI crew dla nowych projektów i blueprint repo

11 listopada 2026 · wersja 1.2 · status: rekomendacja, czeka na wybór Ownera (rozdział 13 przyjęty)

Raport odpowiada na trzy pytania Ownera:

1. Czy struktura „Opus prowadzi, Sonnet definiuje zadania, Haiku wykonuje, Codex niezależnie” jest efektywna i możliwie autonomiczna?
2. Czy lepiej, żeby to Sonnet prowadził pracę, rozmawiał z Ownerem i uruchamiał subagentów?
3. Jaka struktura repo jest najlepsza dla małego, dopiero zaczynanego projektu i jak ma rosnąć, gdy dojdą wydania, poprawki błędów i wsparcie operacyjne?

Raport dotyczy **nowych** projektów. Nie ocenia istniejących repozytoriów Ownera. Doświadczenia z nich są użyte tylko w formie uogólnionej.

## W skrócie

- **Dobór modeli do rodzaju pracy jest trafny, układ w łańcuch nie.** Łańcuch Opus → Sonnet → Haiku to dwa przekazania, przy których ginie kontekst, a najdroższy model stoi w miejscu o największej liczbie tur (rozmowa z Ownerem).
- **Tak, Sonnet powinien prowadzić.** Nie jako „scrum master”, który tylko rozdaje zadania, ale jako grający trener: rozmawia z Ownerem, planuje i **sam wykonuje większość pracy**.
- **Haiku** dostaje wąską klasę zadań: małe, w pełni opisane, sprawdzalne automatem, hurtowe. **Opus** jest doradcą w trzech momentach, a nie kierownikiem. **Codex** zostaje niezależnym recenzentem, redaktorem tekstów dla ludzi i źródłem obrazów.
- **Autonomię dają mechanizmy, a nie liczba ról:** zadania gotowe do wzięcia zapisane w pliku, automatyczny test, z góry ustawione uprawnienia, lista spraw „zawsze Owner” i kolejka pytań, która nie zatrzymuje pracy.
- **Repo startowe to kilkanaście krótkich plików.** Reszta dochodzi dopiero wtedy, gdy wystąpi konkretny wyzwalacz: pierwsze wydanie, pierwszy zgłoszony błąd, pierwsza usługa działająca online.

## 1. Założenia (punkt odniesienia, nie stała)

| Obszar | Stan na 11.11.2026 | Kiedy wrócić do tematu |
| --- | --- | --- |
| Subskrypcje | Claude Pro i ChatGPT Plus, bez płatnego API | Zmiana planu albo limitów |
| Modele na co dzień | Sonnet 5.5 i Haiku 5.5. Opus 5.5 tylko punktowo. Fable poza codziennym użyciem | Nowy model albo zmiana limitów |
| Miejsce pracy | Sesje chmurowe uruchamiane z aplikacji mobilnej. Komputer tylko do rzeczy lokalnych (np. paczki `.apk`) | Pojawi się praca, której chmura nie obsłuży |
| GitHub | Plan Free | Przejście na plan płatny |
| Autonomia | (a) cel → gotowa zmiana do akceptacji, (b) samodzielne scalanie drobnych zmian, (c) start bez Ownera według harmonogramu | Po miesiącu praktyki |
| Typ projektu | Nieznany z góry: treściowy albo z kodem | — |

Obserwacje Ownera, na których opiera się dobór modeli: Opus przy zadaniach programistycznych często trafiał w limit subskrypcji, Sonnet przy małej liczbie zapytań nie, a Haiku dobrze radził sobie z prostymi zadaniami.

## 2. Co mówią źródła

### 2.1. Zaczynaj od najprostszego układu

Anthropic w „Building effective agents” zaleca: „finding the simplest solution possible, and only increasing complexity when needed”. Ostrzega też, że autonomia agentów oznacza „higher costs, and the potential for compounding errors”.

### 2.2. Wielu agentów pomaga w pracy równoległej, a szkodzi w sekwencyjnej

- Badanie Google Research i MIT (180 konfiguracji): w zadaniach sekwencyjnych **wszystkie** układy wieloagentowe pogorszyły wynik o 39–70%. Niezależni agenci wzmacniali błędy 17,2 raza, a układ z centralnym koordynatorem 4,4 raza.
- Anthropic o własnym systemie badawczym: wielu agentów zużywa około 15 razy więcej tokenów niż zwykła rozmowa i opłaca się przy szerokich zadaniach równoległych. Programowanie ma takich części mniej.
- Cognition („Don't build multi-agents” i wpis z 2026 r.): zapis zmian powinien zostać w jednym wątku. Dodatkowi agenci sprawdzają się przy czytaniu i przeglądzie.

Wniosek: tworzenie jednej zmiany w repo to praca sekwencyjna. Łańcuch trzech ról na jednej zmianie działa przeciw wynikowi.

### 2.3. Systemy wieloagentowe psują się na specyfikacji i przekazaniach

Badanie „Why Do Multi-Agent LLM Systems Fail?” (ponad 1600 przebiegów, 7 frameworków) dzieli błędy na trzy grupy: problemy ze specyfikacją i projektem układu (około 42%), rozjechanie się agentów między sobą (około 37%) oraz słaba weryfikacja wyniku (około 21%). Autorzy podkreślają, że to głównie błędy projektu układu, a nie słabość modeli. Udziały pochodzą z omówienia pracy, nie z pełnego tekstu.

Wniosek: każde przekazanie między agentami potrzebuje pisemnego opisu, a każdy wynik automatycznego sprawdzenia.

### 2.4. Mocny model jako doradca, nie jako kierownik

- Anthropic opisał „advisor strategy”: tańszy model wykonuje zadanie od początku do końca i w kluczowych momentach pyta mocniejszego. Według omówień wpisu Sonnet z doradcą Opus miał wynik wyższy o 2,7 punktu procentowego przy koszcie zadania niższym o 11,9% niż sam Sonnet. Haiku z doradcą Opus wyraźnie zyskiwał, ale zostawał poniżej samego Sonneta. Liczby dotyczą modeli z wiosny 2026 r.
- Dokumentacja Claude Code wymienia parę „Sonnet main + Opus advisor” jako typową: „Sonnet handles routine work and escalates planning, ambiguous failures, and completion checks to Opus”.
- Aider od 2024 r. stosuje podobny podział (architekt + edytor) i uzyskał nim najlepsze wyniki w swoim benchmarku. Zastrzega jednak, że dwa wywołania na zadanie są wolniejsze.
- Przewodnik Anthropic po kosztach: układ „mocny planuje, tani wykonują” opłaca się tylko przy dużej pracy równoległej. Przy jednym łańcuchu zależnych kroków lepiej wypada jeden model.

Wniosek: źródła popierają odwrócenie proponowanej piramidy. Tańszy model prowadzi, droższy doradza.

### 2.5. Długą pracę bez nadzoru trzyma w ryzach stan zapisany w plikach

- Anthropic („Effective harnesses for long-running agents”): lista funkcji w pliku, plik postępu, commity, **jedna funkcja naraz** i testy wykonywane „as a human user would”. Każda nowa sesja zaczyna od przeczytania logu gita i pliku postępu. Najczęstsze błędy bez tego: robienie wszystkiego naraz, przedwczesne „gotowe”, zostawianie repo w nieznanym stanie.
- OpenAI („Harness engineering”): `docs/` jest źródłem prawdy, a `AGENTS.md` ma około 100 linii i służy jako mapa, nie encyklopedia.
- Badanie ETH (ICLR 2026): generowane, rozbudowane pliki kontekstowe obniżają skuteczność agentów i podnoszą koszt o około 20%. Plik instrukcji ma być krótki i zawierać tylko to, czego agent nie znajdzie w repo.

### 2.6. Niezależny recenzent ma mieć świeży kontekst

Dokumentacja Claude Code zaleca recenzenta, który nie widział, jak powstawała zmiana, i ma tylko prawo odczytu. Zaleca też prośbę „pomiń styl”, bo recenzent pytany o problemy zawsze coś znajdzie. Model z innej firmy daje dodatkowo inne „ślepe plamy”.

### 2.7. Lekcje z wcześniejszych projektów Ownera (uogólnione)

- Zaprojektowana piramida trzech ról (strateg, kierownik zadań, wykonawca) w praktyce sprowadziła się do jednego agenta i Ownera. Role na górze i na dole prawie nie były wywoływane.
- Recenzja wykonana przez model innego dostawcy kilka razy znalazła realne błędy, których autor zmiany nie widział.
- Najlepiej działał zestaw: najpierw specyfikacja, jedno zadanie = jeden commit, numerowane decyzje bez edycji wstecz, lista odrzuconych pomysłów z warunkiem powrotu, tablica zadań, dziennik oraz automatyczny walidator.

## 3. Ocena proponowanej struktury

| Element propozycji | Ocena | Dlaczego |
| --- | --- | --- |
| Opus jako lead: koncepcja, rozmowa z Ownerem, odpowiedzi dla xdev | **Zmienić** | Rozmowa i koordynacja to najwięcej tur. Stawia to model o najciaśniejszym limicie tam, gdzie zużycie jest największe. Opus jest wart swojej ceny w kilku decyzjach, nie w każdej wymianie zdań |
| Sonnet jako xdev: definiuje zadania | **Zostawić i rozszerzyć** | Sonnet ma też wykonywać. Rozdzielenie „definiuje” i „wykonuje” na jednej zmianie to przekazanie, które kosztuje i gubi kontekst (2.2, 2.3) |
| Haiku jako dev: wykonuje wszystkie zadania | **Zawęzić** | Haiku dobrze robi małe, jasne zadania. Słabiej wypada w długich pętlach z wieloma decyzjami. Jako jedyny wykonawca generowałby wiele pytań i zwrotów |
| Pytania Haiku → Sonnet → Opus | **Uprościć** | Subagent nie rozmawia w trakcie pracy. Zwraca wynik tylko do tego, kto go uruchomił. Każde pytanie to przerwane zadanie i ponowne uruchomienie |
| Codex niezależnie: review, obrazy, teksty dla ludzi | **Zostawić** | Zgodne z 2.6 i z doświadczeniem. Wymaga tylko prostego sposobu przekazania zadań |
| Trzy szczeble nad jedną zmianą | **Odrzucić jako układ domyślny** | Praca sekwencyjna traci na wielu agentach (2.2). W praktyce piramidy i tak się spłaszczają (2.7) |

Co w propozycji jest dobre i zostaje: różne modele do różnych rodzajów pracy, pytania zamiast zgadywania, niezależna recenzja oraz Opus w roli tego, kto ocenia koncepcję.

## 4. Rekomendowana struktura załogi

```text
Owner  ⇄  Prowadzący (Sonnet, sesja główna)
              ├─ sam wykonuje większość zadań
              ├─→ Wykonawca (Haiku, subagent): małe zadania hurtowe
              └─→ Doradca (Opus, subagent): trzy momenty

Owner  →  Codex: recenzja, teksty dla ludzi, obrazy  →  wynik w repo
```

| Rola | Model | Jak działa | Zakres |
| --- | --- | --- | --- |
| **Owner** | człowiek | Aplikacja mobilna | Cel, wybory, akceptacje, sprawy „zawsze Owner” |
| **Prowadzący** | Sonnet 5.5 | Sesja główna | Rozmowa z Ownerem, plan, wykonanie, delegowanie, tablica i dziennik |
| **Wykonawca** | Haiku 5.5 | Subagent `worker` | Małe, w pełni opisane zadania sprawdzalne automatem; praca hurtowa i powtarzalna; długie wyszukiwania |
| **Doradca** | Opus 5.5 | Subagent `advisor`, tylko odczyt | Druga opinia w trzech momentach (niżej) |
| **Recenzent zewnętrzny** | Codex | Uruchamia Owner albo automat na PR | Niezależna recenzja, redakcja tekstów dla ludzi, obrazy |

### Kiedy Prowadzący deleguje do Wykonawcy

Wszystkie cztery warunki muszą być spełnione. Inaczej Prowadzący robi zadanie sam.

1. Zadanie mieści się w krótkim opisie z nazwanymi plikami.
2. Wynik sprawdzi automat albo jedno spojrzenie.
3. Zadanie nie wymaga żadnej decyzji.
4. Zadanie jest hurtowe, powtarzalne albo produkuje dużo tekstu pośredniego.

Opis dla Wykonawcy ma zawsze pięć części: cel, pliki, format wyniku, czego nie ruszać, jaki test uruchomić. Wykonawca, któremu brakuje informacji, kończy z wynikiem `BLOCKED: pytanie`. Nie zgaduje.

### Kiedy Prowadzący woła Doradcę

1. Decyzja o koncepcji albo strukturze: na starcie projektu i przy dużej zmianie.
2. Przed wydaniem albo ważnym scaleniem.
3. Po dwóch nieudanych próbach tego samego zadania.

Doradca dostaje brief najwyżej na jedną stronę (pytanie, opcje, ograniczenia, pliki do przeczytania) i zwraca werdykt do 300 słów. Najwyżej jedna konsultacja na zadanie. Gdy Opus jest niedostępny z powodu limitu, Prowadzący pracuje dalej na wyższym poziomie `effort`, zapisuje to w dzienniku i nie blokuje pracy.

Dwie techniki doradcy:

| Technika | Zaleta | Wada | Rekomendacja |
| --- | --- | --- | --- |
| Subagent `advisor` z briefem | Koszt pod kontrolą: Opus czyta jedną stronę i wskazane pliki. Działa wszędzie, gdzie ładują się agenty z repo | Opus nie widzi całej rozmowy | **Domyślna** |
| Narzędzie `/advisor opus` | Claude sam decyduje, kiedy pytać. Doradca widzi całą rozmowę | Eksperymentalne. Każde wywołanie czyta cały zapis od nowa i liczy się do limitu | Do przetestowania na jednym zadaniu |

### Trzy zasady techniczne

- **Jeden piszący.** Dany zestaw plików zmienia naraz tylko jedna sesja albo jeden agent.
- **Jeden poziom subagentów.** Subagent nie uruchamia kolejnych (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`).
- **Najpierw `effort`, potem agenci.** Gdy wynik jest za słaby, pierwszym ruchem jest wyższy poziom `effort` albo lepszy opis zadania. Dodatkowa rola jest ostatnim ruchem.

### Limity subskrypcji w tym układzie

Limit sesji i limit tygodniowy są wspólne dla wszystkich modeli. Osobno istnieją limity rodziny modeli (komunikat „You've hit your Opus limit”). Po takim komunikacie przejście na model z innej rodziny pozwala pracować dalej. Dlatego Opus używany punktowo nie zatrzyma pracy Sonneta, a Opus jako prowadzący zatrzymywałby ją regularnie, co zgadza się z obserwacją Ownera. Subagenci liczą się do tych samych limitów co sesja główna.

## 5. Pytania i eskalacje

| Od → do | Kiedy | Jak |
| --- | --- | --- |
| Wykonawca → Prowadzący | Brak informacji | Wynik `BLOCKED: pytanie`. Prowadzący odpowiada i wznawia albo robi sam |
| Prowadzący → Doradca | Trzy momenty z rozdziału 4 | Brief w pliku, werdykt wraca do sesji |
| Prowadzący → Owner | Sprawa z listy „zawsze Owner” albo brak danych, których nie ma w repo | Wpis w sekcji „Czeka na Ownera” w `BOARD.md`. Praca nad pozostałymi zadaniami trwa |
| Owner → Codex | Paczka zadań oznaczonych `codex` | Jedna wiadomość. Wynik jako PR albo plik w repo |
| Codex → Prowadzący | Uwagi z recenzji | Komentarze w PR albo plik z uwagami. Poprawia autor zmiany, nie recenzent |

Zasada wspólna: pytanie nie zatrzymuje całej pracy. Zatrzymuje jedno zadanie.

## 6. Autonomia

### 6.1. Co ją daje

| Przeszkoda | Mechanizm |
| --- | --- |
| Agent nie wie, co robić dalej | `BOARD.md` z sekcją „Gotowe do wzięcia”. Zadanie jest gotowe, gdy ma cel, pliki, test odbioru i klasę ryzyka |
| Agent nie wie, czy skończył | Jedna komenda sprawdzająca, ta sama lokalnie i w CI |
| Agent czeka na zgodę przy każdym kroku | Uprawnienia ustawione z góry. Pytanie tylko przy działaniach z krótkiej listy |
| Agent potrzebuje odpowiedzi Ownera | Kolejka „Czeka na Ownera”, następne zadanie w tym czasie |
| Sesja nie pamięta poprzedniej | Stan w plikach: tablica, dziennik, decyzje |
| Nikt nie uruchomił pracy | Zaplanowane zadania w chmurze |
| Limit subskrypcji | Sonnet i Haiku na co dzień, Opus punktowo |

### 6.2. Klasy ryzyka i tryby

| Klasa | Przykłady | Kto scala |
| --- | --- | --- |
| **A, niska** | Notatki, dziennik, tablica, literówki, testy, dokumenty wewnętrzne | Załoga po przejściu testu (tryb b) |
| **B, zwykła** | Funkcje, specyfikacje, treści dla ludzi | Owner akceptuje PR (tryb a) |
| **C, tylko Owner** | Wydania i publikacje, pieniądze, konta, sprawy prawne, kasowanie danych, zmiana widoczności repo, **zmiana zasad załogi** (instrukcje, uprawnienia, CI, test) | Owner wykonuje albo zatwierdza każdy krok |

- **Tryb (a):** Owner podaje cel i wraca do gotowego PR. Obowiązuje w każdym repo od początku.
- **Tryb (b):** załoga sama scala klasę A. Nowe repo zaczyna bez niego i przechodzi na (b) po kilku czystych zmianach.
- **Tryb (c):** załoga startuje bez Ownera. Eksperyment na początek: raz dziennie bierze jedno–dwa gotowe zadania klasy A lub B, raz w tygodniu pisze krótki stan.

Zmiana zasad załogi jest w klasie C celowo. Dzięki temu załoga nie może sama poluzować swoich zabezpieczeń.

### 6.3. Gdzie które zabezpieczenie naprawdę działa

To ustalenie z dokumentacji ma duże znaczenie przy pracy z telefonu:

| Warstwa | Sesja chmurowa z jednym repo | Sesja z kilkoma repo | Wątek w „Projects” (beta) | Lokalnie |
| --- | --- | --- | --- | --- |
| `CLAUDE.md` i `.claude/rules/` | tak | tak | tak | tak |
| Uprawnienia i hooki z `.claude/settings.json` | tak | **nie** | **nie** | tak |
| Agenci i skille z `.claude/` | tak | tak (zaobserwowane) | **nie** | tak |
| Test w GitHub Actions | tak | tak | tak | tak |

Wnioski dla blueprintu:

1. **Zasady krytyczne muszą być w `CLAUDE.md`/`AGENTS.md`**, bo tylko ta warstwa ładuje się wszędzie. `settings.json` jest drugim pasem bezpieczeństwa, nie jedynym.
2. **Praca załogi: jedno repo na sesję.** Wtedy działają uprawnienia, hooki, agenci i skille z repo.
3. **Test w CI jest sędzią niezależnym od miejsca pracy.**
4. **GitHub Free:** ochrona gałęzi działa w repo publicznych, w prywatnych nie. W prywatnym repo regułę „nie scalaj klasy B i C bez Ownera” trzymają instrukcje, reguły `ask` i nawyk pracy przez PR.
5. Funkcja „Projects” jest wygodna z telefonu, ale jej wątki nie ładują agentów, skilli ani uprawnień z repo. Na razie lepiej używać zwykłych sesji z jednym repo.

### 6.4. Tryb (c) w praktyce

Zaplanowane zadania są dostępne w planie Pro. Każde uruchomienie to pełna sesja chmurowa, która zużywa ten sam limit co zwykła praca. Sesja startuje w trybie automatycznym, a reguły `ask` nadal zatrzymują ją do decyzji Ownera. Zmiany trafiają domyślnie na gałęzie `claude/…`. Model wybiera się przy tworzeniu zadania: Sonnet.

Bezpieczniki codziennego uruchomienia: najwyżej dwa zadania, tylko z sekcji „Gotowe do wzięcia”, nigdy klasa C, PR dla klasy B, stop po dwóch nieudanych próbach, wpis do dziennika na końcu. Gotowe treści poleceń są w blueprincie (`automation/scheduled-tasks.md`).

## 7. Codex w załodze

| Zadanie | Jak przekazać | Wynik |
| --- | --- | --- |
| Recenzja zmian | Komentarz `@codex review` w PR albo automatyczne recenzje włączone w ustawieniach Codex | Recenzja w PR |
| Redakcja tekstów dla ludzi | Zadanie na tablicy z oznaczeniem `codex`. Owner wysyła jedną wiadomość: „wykonaj zadania oznaczone codex z BOARD.md” | PR z poprawionym tekstem |
| Obrazy | Zadanie z opisem obrazu i ścieżką docelową | Pliki w repo, PR |

- **Wspólne zasady w `AGENTS.md`.** Codex czyta ten plik sam. `CLAUDE.md` importuje go pierwszą linią (`@AGENTS.md`) i dodaje tylko część dla Claude'a. Jedno źródło zasad dla obu dostawców.
- **Sekcja „Review guidelines” w `AGENTS.md`** mówi recenzentowi, co zgłaszać: błędny wynik, złamanie zasad, brak testu, bezpieczeństwo i prywatność. Styl pomija.
- **Automatyzacja do rozważenia:** automatyczne recenzje Codex na każdym PR. Według cennika Codex jest w planie Plus razem z integracją recenzji. Limity i działanie w repo prywatnych trzeba potwierdzić w ustawieniach konta.
- **Do sprawdzenia w praktyce:** czy komentarz `@codex review` wysłany przez załogę (z konta GitHub Ownera) uruchamia recenzję. Jeśli tak, Owner nie musi niczego wysyłać ręcznie.

Recenzja Codex jest obowiązkowa przed wydaniem i przed publikacją tekstu. Przy zwykłych zmianach klasy B jest zalecana, przy klasie A zbędna.

## 8. Blueprint startowy (etap 0)

```text
repo/
├── AGENTS.md              # wspólne zasady dla wszystkich agentów (≤ 100 linii)
├── CLAUDE.md              # @AGENTS.md + role i modele załogi Claude
├── README.md              # dla ludzi: co to jest, stan, jak zacząć
├── BOARD.md               # zadania i „Czeka na Ownera”
├── JOURNAL.md             # co się wydarzyło i czego się nauczyliśmy
├── work/                  # pliki stanu zadań wstrzymanych i przekazywanych (rozdz. 13)
├── docs/
│   ├── brief.md           # cel, odbiorca, zakres, założenia, miara sukcesu
│   ├── decisions/         # decyzje: numerowane, bez edycji wstecz
│   └── out-of-scope/      # odrzucone pomysły z powodem i warunkiem powrotu
├── .claude/
│   ├── settings.json      # deny/ask, limit zagnieżdżenia subagentów
│   └── agents/
│       ├── worker.md      # Haiku
│       └── advisor.md     # Opus, tylko odczyt
├── tools/check.*          # jedna komenda sprawdzająca
└── .github/workflows/check.yml   # ta sama komenda w CI
```

| Plik | Po co | Skąd zasada |
| --- | --- | --- |
| `AGENTS.md` + `CLAUDE.md` | Krótka mapa i zasady, które ładują się wszędzie | 2.5, 6.3 |
| `BOARD.md` | Agent wie, co robić dalej. Owner widzi, co na niego czeka | 2.5 |
| `JOURNAL.md` | Nowa sesja szybko łapie stan | 2.5 |
| `docs/brief.md` | Specyfikacja celu, pierwsze źródło błędów układu | 2.3 |
| `docs/decisions/`, `docs/out-of-scope/` | Agent nie proponuje drugi raz rzeczy już rozstrzygniętych | 2.7 |
| `tools/check.*` + CI | Sędzia zamiast opinii | 2.3, 2.5 |
| `.claude/settings.json`, agenci | Drugi pas bezpieczeństwa i role | 4, 6.3 |

### Dwa warianty

| | Wariant treściowy | Wariant z kodem |
| --- | --- | --- |
| Dodatkowe foldery | `sources/` (surowe materiały, tylko odczyt), foldery na gotowe treści | `src/`, `tests/`, `docs/specs/` |
| Co sprawdza test | Odnośniki, obecność źródeł, indeksy, długość plików instrukcji | Testy, lint, walidator formatów |
| Dodatkowa rola | — | `reviewer` (Sonnet, tylko odczyt, świeży kontekst) |
| Główna zasada | Każde twierdzenie ma źródło albo oznaczenie `UNVERIFIED` | Najpierw specyfikacja, potem kod i test |

### Czego celowo nie ma na starcie

| Element | Dlaczego nie teraz | Kiedy dodać |
| --- | --- | --- |
| Skille | Bez powtarzalnej czynności skill jest zgadywaniem | Po trzecim powtórzeniu tej samej procedury |
| Plik dla każdego zadania | Na starcie plik stanu mają tylko zadania wstrzymane i przekazywane (rozdział 13) | Etap 1 |
| Arkusz kosztów na zadanie | Przy subskrypcji bez API nie ma kosztu w dolarach | Gdy pojawi się API. Wcześniej wystarcza pięć liczb w tygodniowym stanie |
| `CODEOWNERS`, formularze zgłoszeń | Jeden Owner, brak zewnętrznych zgłoszeń | Etap 3 |
| Folder polityk | Lista „zawsze Owner” mieści się w `AGENTS.md` | Gdy lista przestanie się mieścić |
| Więcej agentów | Każda rola to przekazanie | Gdy konkretna, powtarzalna praca jej wymaga |

To odchudza wcześniejszą propozycję z raportu z 31.10 (sekcja 8) i z zadania startowego śpiewnika. Tamte elementy nie są błędne. Przychodzą później.

## 9. Jak struktura rośnie

Zasada: **element dochodzi wtedy, gdy wystąpi jego wyzwalacz**, a nie na zapas.

| Etap | Wyzwalacz | Co dochodzi w repo | Co zmienia się w załodze |
| --- | --- | --- | --- |
| **0. Start** | Nowe repo | Rdzeń z rozdziału 8 | Tryb (a) |
| **1. Budowa** | Ponad około 10 otwartych zadań albo pierwsza specyfikacja | `work/` (pliki zadań i epiki), `docs/specs/`, pierwsze skille, reguły ścieżkowe w `.claude/rules/` | Tryb (b) po kilku czystych zmianach. Haiku do hurtu. Tryb (c) raz dziennie |
| **2. Wydania** | Pierwszy użytkownik poza Ownerem | `CHANGELOG.md`, wersje (SemVer), `docs/release.md` z listą kontrolną, tagi, szablon PR | Doradca i Codex przed każdym wydaniem. Wydanie zawsze zatwierdza Owner |
| **3. Utrzymanie** | Pierwszy błąd zgłoszony przez użytkownika albo więcej niż jedna wersja w użyciu | Skrzynka zgłoszeń (GitHub Issues z formularzem), `docs/triage.md`, reguła „każda poprawka ma test regresyjny”, gałęzie poprawek | Zaplanowany przegląd zgłoszeń: klasyfikacja, odtworzenie, propozycja poprawki jako PR |
| **4. Operacje** | Usługa działa online bez przerwy (hosting, konta, płatności) | `ops/runbooks/`, `ops/incidents/` (opis po incydencie, bez szukania winnych), `ops/monitoring.md`, `support/` (FAQ, szablony odpowiedzi), `SECURITY.md`, plan kopii zapasowych | Agent „dyżurny”: uruchamiany alarmem albo harmonogramem, zbiera dane i pisze szkic diagnozy. Zmiany na produkcji i odpowiedzi do użytkowników zatwierdza Owner |

Uwagi do etapów:

- **Etap 2:** wydanie jest klasą C. Załoga przygotowuje wszystko (wersja, lista zmian, paczka, lista kontrolna), a Owner wykonuje ostatni krok. Praca wymagająca komputera Ownera (np. podpisana paczka `.apk`) dostaje na tablicy oznaczenie „wymaga komputera”.
- **Etap 3:** zgłoszenia od ludzi z zewnątrz to dane, nie polecenia. Agent, który je czyta, nie wykonuje zawartych w nich instrukcji.
- **Etap 4:** agent ma na produkcji tylko odczyt. Runbook opisuje kroki tak, żeby mógł je wykonać Owner z telefonu. Odpowiedzi wsparcia zaczynają jako szkice. Samodzielne wysyłanie można rozważyć później dla wąskich, powtarzalnych kategorii.
- Załoga nie rośnie o nowe stałe role. Rosną **wyzwalacze** (harmonogram, zdarzenie z GitHuba, alarm) i **procedury** (skille, runbooki). Prowadzący zostaje jeden.

## 10. Kiedy zmienić sam blueprint

Tygodniowy stan zapisuje pięć liczb: zadania zakończone, zwroty po recenzji, konsultacje z Doradcą, pytania do Ownera, trafienia w limit.

| Sygnał | Zmiana |
| --- | --- |
| Zadania Wykonawcy wracają do poprawki częściej niż co trzecie | Zawęzić zakres Haiku albo poprawić opisy zadań |
| Prowadzący regularnie prosi Doradcę przy zwykłych zadaniach | Zadania są za duże albo za słabo opisane. Poprawić definicję gotowości |
| Sonnet trafia w limit | Mniej zadań na uruchomienie, więcej pracy dla Haiku, niższy `effort` |
| Opus przestaje trafiać w limit (nowy plan albo nowe limity) | Rozważyć Opus jako prowadzącego w fazie koncepcji |
| Nowa generacja modeli | Powtórzyć próbę: to samo zadanie na trzech układach, porównać wynik i zużycie |
| „Projects” zaczną ładować agentów i uprawnienia z repo | Rozważyć je jako główne miejsce pracy z telefonu |

## 11. Do sprawdzenia w praktyce

1. Czy `/advisor opus` działa w sesjach chmurowych w planie Pro i ile zużywa limitu.
2. Czy automatyczne recenzje Codex działają w planie Plus dla repo prywatnych i jakie mają limity.
3. Czy komentarz `@codex review` wysłany przez załogę uruchamia Codex.
4. Czy Codex w chmurze potrafi sam wygenerować obraz i dodać go do repo, czy obrazy trzeba przenosić z aplikacji ChatGPT.
5. Jak często tryb (c) trafia w limit przy jednym uruchomieniu dziennie.

## 12. Co dalej

1. **Zrobione razem z tym raportem:** struktura startowa repo `AI-crew` oraz blueprint w `blueprints/starter-crew-repo/` (rdzeń, dwa warianty, etapy wzrostu, automatyzacja, zadanie startowe).
2. **Wybór Ownera:** przyjąć, zmienić albo odrzucić strukturę z rozdziału 4. Do tego czasu ma status propozycji ([decyzja 0001](../docs/decisions/0001-struktura-zalogi.md)).
3. **Pierwszy pilotaż:** jeden nowy mały projekt postawiony z blueprintu, miesiąc pracy, potem przegląd według rozdziału 10.
4. **Włączenie trybu (c)** w wybranym repo: dwa zaplanowane zadania z gotowymi treściami poleceń.

## 13. Uzupełnienie z 11.11.2026 (wersja 1.1)

Po lekturze raportu Owner dodał dwa wymagania. Oba zostały przyjęte ([decyzja 0007](../docs/decisions/0007-zadanie-niesie-swoj-stan.md) i [0008](../docs/decisions/0008-jedno-repo-na-sesje-i-skrzynka-nadawcza.md)) i weszły do blueprintu.

### 13.1. Zadanie niesie swój stan

Cel: ciągłość kontekstu przy przekazaniu między modelami i rolami oraz możliwość pauzy, gdy kończy się limit albo trzeba czekać na decyzję Ownera.

- **Stan zapisuje się w trakcie, nie na końcu.** Limit przerywa sesję w pół kroku. Po każdym kroku jest punkt kontrolny: plik stanu, commit z numerem zadania, push. Niewypchnięta praca może przepaść, gdy maszyna sesji wygaśnie.
- **Plik stanu** (`work/T-NNN-tytul.md`) ma zadanie wstrzymane, zablokowane albo przekazywane: stan, kto trzyma, gałąź, co zrobione, **następny krok**, otwarte pytania z opcjami, pułapki.
- **Stała kolejność wznawiania:** tablica → plik stanu → historia gałęzi → test → następny krok.

Ten sam plik jest opisem dla Haiku, briefem dla Opusa i zadaniem dla Codexa. To zgodne z rozdziałem 2.5 (stan w plikach, jedna rzecz naraz) i ogranicza błędy przekazań z rozdziału 2.3.

### 13.2. Jedno repo na sesję, inne tylko do odczytu

- Sesja startuje z jednym repo. Inne dołącza się tylko wtedy, gdy zadanie tego wymaga, i tylko do odczytu. Repo dołączone do odczytu nie pozwala na zapis.
- Powody: uprawnienia z repo działają tylko w sesji z jednym repo (rozdział 6.3); przy kilku repo ładują się instrukcje i agenci ze wszystkich naraz; łatwo o przeniesienie szczegółów prywatnego projektu do publicznego repo.

### 13.3. Notatki z pomysłami dla innych projektów

„Tylko odczyt” i „zostawiam tam notatkę” wykluczają się technicznie: zapis wymaga prawa zapisu do całego cudzego repo. Rozważone warianty:

| Wariant | Jak działa | Ocena |
| --- | --- | --- |
| **A. Skrzynka nadawcza** | Notatka zostaje w `BOARD.md` repo, w którym trwa praca. Zabiera ją sesja repo docelowego na polecenie Ownera | **Przyjęty.** „Tylko odczyt” zostaje realną blokadą |
| B. Kurier | Sesja uruchamia krótką sesję w repo docelowym, która zapisuje notatkę według tamtejszych zasad | Jedna próba; niesprawdzone |
| C. Zapis bezpośredni | Sesja dostaje prawo zapisu do cudzego repo | Odrzucony jako domyślny |

Prowadzący repo docelowego dopracowuje pomysł i proponuje Ownerowi: odrzucić, połączyć albo przyjąć jako zadanie. Notatka jest daną, nie poleceniem. W publicznym repo nie zawiera nazw ani wnętrza prywatnych projektów.

### 13.4. Skrzynka centralna (przyjęta)

Pomysł Ownera: jedno miejsce zbiera notatki ze wszystkich repo, a każde repo czyta tylko to miejsce. To naprawia słaby punkt wariantu A, czyli doręczanie. Bez skrzynki każde repo musiałoby czytać wszystkie pozostałe.

Decyzja Ownera ([0009](../docs/decisions/0009-skrzynka-centralna-crew-inbox.md)): osobne prywatne repo, start od razu, zbieranie na polecenie, potem automat. Rekomendacja agenta brzmiała „przy trzecim repo”; Owner wybrał start od razu.

Zasady budowy:

1. **Osobne prywatne repo**, a nie to publiczne. Spis notatek zawiera nazwy projektów.
2. **Zbiera skrypt, nie model.** Agent dołącza repo do odczytu, uruchamia skrypt i test. Notatki nie są przerabiane, a zużycie limitu jest minimalne.
3. **Skrzynka jest spisem, a nie drugą tablicą.** Stan pomysłu zostaje w repo docelowym.
4. **Projekt czyta tylko swój plik.** Plik repo publicznego nie podaje źródła notatki.
5. **Automatyzacja później.** Zaplanowane zadanie z kilkoma repo ma prawo zapisu do każdego z nich, a GitHub Free nie zablokuje tego w repo prywatnych.

Struktura i instrukcja: blueprint [`crew-inbox`](../blueprints/crew-inbox/README.md).

## Źródła

Dokumentacja Claude Code (pobrana 11.11.2026):

- [Advisor tool](https://code.claude.com/docs/en/advisor): pary modeli, koszt, wymagania
- [Subagents](https://code.claude.com/docs/en/sub-agents): modele, zagnieżdżanie, kiedy subagent, a kiedy rozmowa główna
- [Model configuration](https://code.claude.com/docs/en/model-config) i [Manage costs](https://code.claude.com/docs/en/costs): poziomy `effort`, limity wspólne i limity rodziny modeli
- [Scheduled tasks](https://code.claude.com/docs/en/routines): plan Pro, tryb automatyczny, gałęzie `claude/`, limity
- [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web), [Settings in cloud sessions](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions), [Projects](https://code.claude.com/docs/en/claude-projects): co ładuje się w której sesji
- [Permission modes: protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths) i [Permissions](https://code.claude.com/docs/en/permissions)
- [Memory: AGENTS.md](https://code.claude.com/docs/en/memory#agents-md) i [Best practices](https://code.claude.com/docs/en/best-practices): recenzent ze świeżym kontekstem, „skip style”

Anthropic i OpenAI:

- Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Anthropic, [The advisor strategy](https://claude.com/blog/the-advisor-strategy). Strona niedostępna z tej sesji. Liczby według omówień, m.in. [Gigazine](https://www.gigazine.net/gsc_news/en/20260410-anthropic-advisor-tool) i [MindStudio](https://www.mindstudio.ai/blog/anthropic-advisor-strategy-opus-sonnet-haiku)
- Anthropic, przewodnik doboru modeli i kosztów w dokumentacji Claude API (wzorce „advisor” i „orchestrator”; kopia z 3.11.2026)
- OpenAI, [Harness engineering](https://openai.com/index/harness-engineering/). Przez wyniki wyszukiwania
- OpenAI, [Codex code review in GitHub](https://developers.openai.com/codex/integrations/github) i [cennik Codex](https://chatgpt.com/codex/pricing/). Przez wyniki wyszukiwania; strony niedostępne z tej sesji

Badania i praktycy:

- Kim i in., [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) oraz [omówienie Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- Cemri i in., [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)
- Gloaguen i in., [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) (ICLR 2026)
- Cognition, [Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents) i [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working). Przez wyniki wyszukiwania
- Aider, [Separating code reasoning and editing](https://aider.chat/2024/09/26/architect.html)
- HumanLayer, [12-factor agents](https://github.com/humanlayer/12-factor-agents)
- [DORA 2025: State of AI-assisted Software Development](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report): AI wzmacnia istniejące praktyki, dobre i złe

Praktyki użyte w rozdziale 9, z wiedzy ogólnej (nie pobierano w tej sesji): [Keep a Changelog](https://keepachangelog.com), [Semantic Versioning](https://semver.org), [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/), [Architecture Decision Records](https://adr.github.io).

Zastrzeżenie: funkcje Claude Code i Codex oraz limity planów zmieniają się szybko. Narzędzie advisor i „Projects” są eksperymentalne albo w wersji beta. Przed oparciem się na konkretnym limicie trzeba sprawdzić aktualną dokumentację.
