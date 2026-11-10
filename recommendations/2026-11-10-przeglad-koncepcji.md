# Przegląd koncepcji AI-crew i planów projektów

10 listopada 2026 · Przegląd przekrojowy wszystkiego, co powstało w tej rozmowie od 31 października: raport o crew, rekomendacja skilli, raport o hostingu (v3.1), aktualizacja przeglądu JvP, raport śpiewnika (v1.2). Oceniam też własne wcześniejsze wnioski z tej sesji.

## Werdykt

Koncepcje są w większości trafne. Problemem nie jest już brak wiedzy, tylko **brak wykonania i zbyt szeroki front**:

- w 10 dni powstało około 2200 linii raportów (w tym 440 od Codexa) i **ani jedno zmierzone zadanie crew**;
- na Twoją decyzję czeka około **40 pytań**: około 30 w raportach AI-crew, 8 zadań `awaiting-owner` i 5 pytań z recenzji z 10.11 w `educationInfluencer`;
- cztery repozytoria mają niescaloną pracę (tabela niżej).

Trzy najważniejsze zmiany, które proponuję:

1. **Zawęzić front do dwóch rzeczy na 6 tygodni** i wstrzymać planowanie reszty.
2. **Zmienić miernik** z kosztu tokenów na **minuty Ownera na zaakceptowaną zmianę**. To Twój czas jest najdroższym zasobem, nie modele.
3. **Wdrożyć crew w istniejącym repo**, zamiast projektować kolejną strukturę od zera.

## Co potwierdziły dane z Twoich repozytoriów

| Teza z raportów | Dowód | Wniosek |
| --- | --- | --- |
| Jeden wykonawca zamiast piramidy ról | `educationInfluencer` ma zaprojektowaną piramidę: CEO (Opus) → xdev (Sonnet) → team (Haiku). W praktyce na 38 zadań: 17 dla xdev, 15 dla Ownera, 3 dla team (wszystkie nadal w backlogu). Komentarze w zadaniach: xdev 56, Codex 12, Owner 14, **CEO 0, team 0**. W dzienniku decyzje podjęli: Owner 30, xdev 9, CEO 2 | Piramida sama zwinęła się do jednego agenta i Ownera. Role CEO i team można usunąć bez straty |
| Recenzent innego dostawcy pomaga | Trzy przypadki: Codex znalazł 4 potwierdzone błędy w JvP (30.10); w `educationInfluencer` znalazł niezgodne twierdzenie i 2 defekty narzędzia (journal 039); w raporcie o hostingu wniósł 6 rzeczy, których nie miałem. W drugą stronę też działa: sesja Claude z 10.11 poprawiła moją tezę o GitHub Pages | Recenzja krzyżowa to jedyny element „wieloagentowy”, który ma u nas dowody |
| Reguły trzeba egzekwować konfiguracją | Hook zatrzymał tę sesję, gdy gałąź nie była wypchnięta (7.11). Lista dozwolonych adresów zablokowała strony Hostingera, arXiv i OpenLP | Działa. Skutek uboczny: część raportów opiera się na źródłach wtórnych |
| Wąskim gardłem jest Owner | 8 z 38 zadań czeka na Ownera; 4 decyzje z raportu z 31.10 nadal bez odpowiedzi; niescalone gałęzie | Proces musi oszczędzać Twoją uwagę, nie tokeny |

Niescalona praca na dziś:

| Repo | Gałąź | Commity poza główną | Ostatni |
| --- | --- | --- | --- |
| `education-games` | `jvp-notatki-2026-10-30` (wersja 1.2.0) | 13 | 5.11 |
| `learning_tools` | `ccr-d914ae0e-4gvx4c` (T-56, niezweryfikowane na PC) | 7 | 30.10 |
| `klasa6` | `nauczanie`, `diagnoza-biologii-II7` | 23 i 1 | 18.10 |
| `AI-crew` | `ccr-a0d3714a-raggyx` | 4 | 8.11 |

## Główne problemy

1. **Za szeroki front.** Pięć aktywnych repozytoriów, a w tej rozmowie doszły: JvP online, Nina's Drills, sklep w dwóch markach, śpiewnik i sam AI-crew. Każdy raport osobno mówi „jeszcze nie kupuj”, ale razem tworzą plan na kilka osób.
2. **AI-crew nie wystartował i nie stosuje własnych zasad.**
   - Blueprint startowy ma status „not started”.
   - Repo nie ma `CLAUDE.md` ani rejestru decyzji; Twoje decyzje z 7.11 są zapisane tylko w tabeli zmian jednego raportu.
   - Domyślną gałęzią na GitHubie jest gałąź sesji, a `master` jest 4 commity z tyłu.
   - Raporty mają po 250–665 linii; plik `-v3` zawiera wersję 3.1.
3. **Zły miernik.** Plan z 31.10 mierzy koszt w dolarach na zadanie i testuje, czy Haiku jest tańsze od Sonneta. Przy subskrypcji tokeny w ramach limitów nie kosztują nic dodatkowo, a raport z 7.11 sam pokazał, że największym kosztem jest Twój czas (100 zł/h). Optymalizujemy nie tę zmienną.
4. **„Rozważ” zapisałem jako „decyzję”.** Napisałeś: „Rozważ dla 1 grę przez internet, hostowane konta i zakupy”. W raporcie v2/v3 i w przeglądzie JvP (scalonym do `master` w `education-games`) figuruje to jako „decyzja Ownera”. Na tej podstawie plan przeszedł od razu do Nakamy na VPS-ie, zanim gra trafiła do sklepu.
5. **Trzy różne backendy dla jednej osoby.** Nakama na VPS-ie (JvP), Cloudflare (śpiewnik), Supabase jako opcja (Nina's Drills). Każdy to osobna administracja i osobna wiedza.
6. **Niedoszacowane ryzyka prawne.**
   - **ITIL:** PeopleCert prowadzi program licencji dla produktów firm trzecich i ogranicza komercyjne użycie swoich znaków i materiałów do licencjobiorców. „Najmocniejszy kandydat na przychód” ma więc nierozstrzygnięty warunek wstępny. W raporcie było to tylko „zastrzeżenie o znaku”.
   - **JvP:** starsza wersja zasad Google mówi, że aplikacje kierowane głównie do dzieci nie powinny używać logowania Google. Aktualnego brzmienia nie potwierdziłem. To może podważyć „zakupy po zalogowaniu kontem Google”.
   - **Śpiewnik:** prawa do tekstów pieśni (już opisane w raporcie).
7. **Planowanie wyprzedza dane.** Śpiewnik ma 40 wymagań i 30 zadań, zanim wiadomo, gdzie i dla ilu osób ma działać. Sklep jest rozpisany przed pierwszym opublikowanym postem.
8. **Cztery konwencje pracy.** `learning_tools`, `klasa6` i `educationInfluencer` mają każde własny układ zadań, decyzji i dziennika. Blueprint AI-crew proponuje piąty.

## Proponowane zmiany w koncepcjach

| Obszar | Było | Proponuję |
| --- | --- | --- |
| **Skład crew** | Planista, wykonawca, recenzent, opcjonalnie lead; w `educationInfluencer` CEO → xdev → team | **Jeden wykonawca + recenzent tylko do odczytu + Codex przy bramkach.** Planowanie jako skill, nie osobny agent. Bez CEO i bez „team”. Zgodne z propozycją P6 z recenzji `educationInfluencer` z 10.11 |
| **Modele** | Sonnet jako wykonawca, potem test Haiku; Opus do eskalacji | **Domyślny model sesji (Opus 5.5) jako wykonawca; regulacja poziomem `effort`, nie zmianą modelu.** Sonnet, gdy limity subskrypcji zaczną przeszkadzać. Haiku tylko do masowego czytania przez podagentów. Fable 5.2 do przeglądów przekrojowych i trudnych specyfikacji, raz na etap. Test „Haiku kontra Sonnet” zdejmuję jako przedwczesny |
| **Miernik** | Koszt w USD na zadanie | **Minuty Ownera na zaakceptowaną zmianę**, „przyjęte za pierwszym razem” (tak/nie), liczba pytań do Ownera. Tokeny tylko pomocniczo |
| **Standard repo** | Nowy blueprint z teorii | **„Standard domowy” wyciągnięty z `learning_tools`**, które działa najlepiej: najpierw specyfikacja, jedno zadanie = jeden commit, numerowane decyzje, odrzucone pomysły z warunkiem powrotu, tablica, dziennik. Dodać trzy brakujące rzeczy: reguły w `settings.json`, CI, recenzenta |
| **Decyzje Ownera** | Pytania rozsiane po raportach | **Jedna kolejka, najwyżej 5 otwartych pytań.** Każde z rekomendacją domyślną i terminem. Sprawy odwracalne agent wykonuje domyślnie po terminie. Pieniądze, konta, publikacje i prawo zawsze czekają na Ciebie |
| **Dokumenty** | Rosnące raporty z wersjami | Limit około 150 linii. Decyzje do osobnych plików. Poprawki jako errata (wzór: tabela zmian w recenzji `educationInfluencer` z 10.11) |
| **Hosting** | Cloudflare na strony; Nakama na VPS-ie dla gier | **Najpierw bez serwera, jedna platforma.** Cloudflare na strony, pokoje na żywo i małe API. VPS dopiero po bramce „JvP online”. Przed wyborem Nakamy porównać ją z zarządzanym backendem gier (np. LootLocker ma wtyczkę do Godota i logowanie Google; weryfikacji zakupów i limitów nie sprawdziłem) |
| **JvP online** | „Decyzja”, od razu konta + zakupy + gra online | **Kierunek do rozważenia, w trzech etapach z bramkami:** (1) wydanie offline w Google Play; (2) zakupy przez sklep Google bez własnych kont; (3) konta i gra online dopiero po sprawdzeniu zasad dla aplikacji dziecięcych i po danych z wydania |
| **Nina's Drills** | Wspólna Nakama z JvP | **Osobno i bez backendu na start.** Wycofuję wspólny backend: dane dorosłych klientów nie powinny dzielić serwera z grą dla dzieci. Przed sprzedażą zestawów ITIL sprawdzić licencję PeopleCert. Alternatywa bez tego ryzyka: produktem jest silnik i standard pliku, a zestawy użytkownik tworzy z własnych materiałów z pomocą AI |
| **Śpiewnik** | 30 zadań i dwie ścieżki | **Nic nie budować do trzech odpowiedzi** (niżej). Małe grupy bez rzutnika: pominąć OpenLP, zrobić minimalną aplikację webową. Sala z rzutnikiem: OpenLP i własny widok uczestnika. Pokój na żywo zbudować raz; ten sam wzorzec przyda się potem w JvP |
| **Influencer-AI** | Sklep w dwóch markach, hosting | **Wstrzymać planowanie sklepu do decyzji w 8. tygodniu testu.** Teraz tylko P1–P3 z recenzji z 10.11 (blokady w konfiguracji, limit prób, koszt na przyjęty reel) |
| **Praca z Codexem** | Ustalenia w czacie | Przekazanie tylko przez wypchniętą gałąź albo PR. Commit `48d8031` istniał najpierw tylko lokalnie u Codexa i nie dało się go znaleźć |
| **Sesje** | Jedna sesja: 10 dni, 5 repozytoriów, 3 modele | Jedna sesja na jeden rezultat; stan przekazywany plikami w repo. Dla sesji badawczych osobne środowisko z szerszą listą dozwolonych stron |

## Kolejność na 6 tygodni

| Kiedy | Co | Kto |
| --- | --- | --- |
| Tydzień 1 | Domknąć pracę w toku: scalić JvP 1.2.0; zdecydować o gałęziach `klasa6`; PR w `learning_tools` po sprawdzeniu na PC; `master` jako domyślna gałąź w AI-crew | Owner, agent |
| Tydzień 1 | Uruchomić dwa „zegary”, które tylko Ty możesz włączyć: konta i pierwszy post Influencer-AI (start 8-tygodniowego testu) oraz test zamknięty JvP w Google Play (12 testerów przez 14 dni) | Owner |
| Tygodnie 1–3 | **Pilotaż crew w `education-games`:** `CLAUDE.md`, testy regresji dla błędów R1–R4 i migracji zapisu, CI. Wykonawca Claude, recenzent Codex. Mierzyć minuty Ownera | agent, Codex |
| Tygodnie 3–6 | Śpiewnik: jedno spotkanie z OpenLP albo od razu mini-aplikacja, zależnie od odpowiedzi. Drugi projekt crew | Owner, agent |
| Tygodnie 3–6 | Nina's Drills: tylko sprawdzenie licencji i demo webowe bez sprzedaży | agent |
| Po 6 tygodniach | Przegląd z liczbami. Bramki: JvP online, sklep (po 8 tygodniach testu), VPS | Owner |

Dlaczego pilotaż w `education-games`: testy i CI zalecił przegląd Codexa z 30.10, chronią najbardziej zaawansowany produkt przed wydaniem, dają się sprawdzić automatycznie i nie wymagają żadnej Twojej decyzji produktowej.

## Kolejka decyzji: pięć pytań na teraz

| # | Pytanie | Domyślnie |
| --- | --- | --- |
| 1 | Czy akceptujesz zawężenie na 6 tygodni (wydanie JvP z testami, start Influencer-AI, reszta wstrzymana)? | Tak |
| 2 | Czy JvP online ma być „kierunkiem do rozważenia po wydaniu offline”, a nie decyzją? | Tak; poprawię zapisy w obu repozytoriach |
| 3 | Czy w AI-crew agent może wypychać dokumenty prosto na `master`? Zmiana domyślnej gałęzi na `master` jest w ustawieniach GitHuba (Settings → Branches) | Tak |
| 4 | Czy pilotaż crew ma ruszyć w `education-games` z Codexem jako recenzentem? | Tak |
| 5 | Śpiewnik: gdzie i dla ilu osób? Czy jest komputer z rzutnikiem i Wi-Fi? Czy prowadzący ma prowadzić z samego telefonu? | Brak; bez odpowiedzi nic nie buduję |

Pozostałe pytania z wcześniejszych raportów proponuję uznać za zawieszone do przeglądu po 6 tygodniach.

## Errata do wcześniejszych dokumentów tej sesji

| Dokument | Było | Powinno być |
| --- | --- | --- |
| Raport o hostingu v3 (W skrócie, sekcja 3.1) i przegląd JvP §7 w `education-games` | „Decyzja Ownera z 7.11: gra przez internet, konta, zakupy” | „Kierunek do rozważenia”; Owner napisał „rozważ” |
| Raport o hostingu v3, zmiana nr 1 i sekcja 3.3 | „GitHub Pages nie nadaje się do stron komercyjnych” | Regulamin wyklucza strony służące **głównie** transakcjom lub SaaS; strona źródeł z linkiem do Ko-fi najpewniej jest dozwolona. Faktyczna przeszkoda: Pages nie działa z prywatnego repo na darmowym planie (ustalenie sesji `educationInfluencer` z 10.11) |
| Raport o hostingu v3, sekcja 3.2 | Wspólna Nakama dla JvP i Nina's Drills jako wariant rekomendowany | Wycofane (tabela zmian wyżej) |
| Raport o crew z 31.10, sekcje 2 i 9 | Test „Haiku kontra Sonnet”; Fable 5.1 za 10/50 USD | Test zdjęty. Aktualnie Fable 5.2 kosztuje 8/40 USD za milion tokenów; Opus 5.5 4/20; Sonnet 5.5 2/10; Haiku 5.5 0,10/0,50 |
| Raport śpiewnika, sekcje 2 i 9 | 40 wymagań i 30 zadań jako plan | Katalog możliwości; planem stanie się po odpowiedziach z pytania 5 |

Poprawek w tych plikach jeszcze nie wprowadziłem.

Bez zmian pozostaje rekomendacja skilli z 3.11. Nadal otwarte: repo `AI-agents` nie zawiera plików standardu, których wymaga `skill-auditor`.

## Czego nie sprawdziłem

- **Licencja PeopleCert:** znam tylko opis programu z wyników wyszukiwania; nie czytałem przewodnika licencyjnego (wersja 4.0 z 3.12.2025).
- **Zasady Google dla aplikacji dziecięcych:** źródło o logowaniu Google pochodzi z archiwalnej wersji zasad z 2020 r.
- **LootLocker:** potwierdziłem tylko wtyczkę do Godota i logowanie Google.
- **Statystyki `educationInfluencer`:** policzone z nagłówków komentarzy w `tasks/` i pól „Decided by” w `journal/` na `master` z 10.11 (`3f4dfe4`).
- To przegląd jednego recenzenta, który ocenia też własną pracę. Zgodnie z własną zasadą proponuję dać ten plik Codexowi do kontrrecenzji.

## Źródła

- Repozytoria (stan z 10.11.2026): `AI-crew` @ `ade7800`; `educationInfluencer` @ `3f4dfe4` (`tasks/`, `journal/`, `.claude/agents/`, `docs/workflow.md`, `docs/reviews/2026-11-09-ai-video-from-scratch-review.md`); `education-games` @ `2680682`; `learning_tools` @ `db28321`; `klasa6` @ `583c427`.
- Wcześniejsze dokumenty: [raport o crew](../outputs/2026-10-31-efficient-ai-crew-and-repo-setup.md), [rekomendacja skilli](2026-11-03-skille-agentow-ai.md), [raport o hostingu v3.1](../outputs/2026-11-07-orkiestracja-agentow-i-hosting-v3.md), [analiza Codexa](../outputs/2026-11-07-codex-ai-crew-hosting-i-migracja.md), [raport śpiewnika v1.2](../outputs/2026-11-08-spiewnik-live-wymagania-v1.md).
- Ceny i dobór modeli: dokumentacja Claude API (stan z 3.11.2026), w tym zalecenie, by przed kaskadą modeli zmierzyć mocniejszy model na niższym `effort` i oceniać koszt ukończonego zadania.
- [PeopleCert: Third Party Product Licensing](https://peoplecert.org/Organizations/Services/third-party-product-licensing-service) i [przewodnik TPPL](https://peoplecert.org/-/media/folders-reorganized/legal-documents/peoplecert-tppl-guide.pdf).
- [LootLocker: logowanie Google](https://docs.lootlocker.com/players/authentication/how-to/sign-in-with-google), [konfiguracja SDK Godota](https://docs.lootlocker.com/the-basics/godot-quick-start/configure-the-sdk).
- [Google Play Games Services: logowanie](https://developer.google.com/games/services/common/concepts/sign-in), [archiwalne zasady danych użytkownika API Google (2020)](https://webcf.waybackmachine.org/web/20220411212138/https://developers.google.com/terms/api-services-user-data-policy), [Family Link i profile dzieci](https://support.google.com/families/answer/7106960).
