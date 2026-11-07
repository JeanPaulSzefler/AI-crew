# Orkiestracja agentów (Herdr) i hosting (Hostinger): analiza dla AI-crew i projektów JvP, Exam Drill i Influencer-AI

7 listopada 2026 · **Wersja 1 (robocza)** · Punkt odniesienia: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md)

## W skrócie

1. **Nie kupuj teraz VPS-a.** Żaden z projektów nie potrzebuje dziś serwera. Najbliższe potrzeby to: polityka prywatności dla JvP, strona źródeł i quiz Quilla dla Influencer-AI, ewentualnie wersja webowa Exam Drill. Wszystkie to **strony statyczne**, które można hostować za darmo (Cloudflare Pages, GitHub Pages, itch.io). Do tego dochodzi domena za około 40–80 PLN rocznie.
2. **Hostinger może się przydać później, ale w dwóch rolach, których nie wolno łączyć na jednym serwerze:**
   - **runner agentów** (VPS z Claude Code, Codexem, ewentualnie Hermesem), uzasadniony dopiero wtedy, gdy crew musi działać non stop poza GitHubem i chmurą Claude Code;
   - **sklep lub blog** (hosting WordPress/WooCommerce albo VPS), dopiero na etapie 3 planu monetyzacji Influencer-AI, czyli po około 1000 zaangażowanych obserwujących.
   
   Agent z dostępem do powłoki i dane klientów sklepu na jednej maszynie to niepotrzebne ryzyko.
3. **Z raportu Herdr warto przejąć dla AI-crew trzy rzeczy, wszystkie bez VPS-a:**
   - **recenzja innym modelem innego dostawcy** (Codex/GPT ocenia pracę Claude'a, i odwrotnie); robisz to już ręcznie w `education-games` i `educationInfluencer`;
   - **izolacja agenta autonomicznego w kontenerze** z zamontowanym tylko jednym folderem;
   - **kanał powiadomień i zgód z telefonu.**
4. **Największe ryzyko uzależnienia od Hostingera nie leży w samym VPS-ie**, który przenosi się w mniej niż dzień, jeśli konfiguracja jest w gicie. Leży w:
   - przedpłacie na 24–48 miesięcy, warunkującej cenę promocyjną;
   - podwyżce przy odnowieniu, zwykle około 1,5–2,5× ceny startowej;
   - domenie i poczcie kupionych w pakiecie u tego samego dostawcy;
   - stronach budowanych w zamkniętych kreatorach (Website Builder, Horizons).

Wszystkie ceny w tym dokumencie są **orientacyjne**. Pochodzą z serwisów porównawczych, często afiliacyjnych, bo strona hostinger.com nie była dostępna z tej sesji. Przed zakupem sprawdź cenę w koszyku.

## 1. Ocena raportu wejściowego

| Teza raportu | Ocena | Komentarz |
| --- | --- | --- |
| Herdr (w raporcie „Herder”) zarządza kilkoma agentami z jednego okna i trzyma ich na serwerze po zamknięciu aplikacji | **Potwierdzone** | Herdr to otwartoźródłowy multiplekser terminala (Rust, licencja AGPL) śledzący stan agentów: zablokowany, pracuje, gotowy, bezczynny. Obsługuje m.in. Claude Code i Codex. Wsparcie dla Windows jest w wersji beta |
| Skill `herder-core` | **Niepotwierdzone** | Źródła mówią o „instalowalnym skillu”, który pozwala agentowi sterować Herdrem, ale nie podają tej nazwy. Sprawdzić w repo projektu przed instalacją |
| Hermes Agent ma trwałą pamięć i sam pisze skille | **Potwierdzone** | Projekt Nous Research (MIT, luty 2026). Pamięć w `~/.hermes/`, skille w otwartym standardzie Agent Skills, bramka do Telegrama, Discorda, Slacka, WhatsAppa i Signala |
| Weryfikacja kodu przez innego agenta „dramatycznie podnosi jakość” | **Kierunkowo trafne, liczbowo niezmierzone** | Zgodne z wnioskiem z [raportu AI-crew](2026-10-31-efficient-ai-crew-and-repo-setup.md): niezależny recenzent jest lepszy niż „CEO” na tym samym modelu. Raport nie podaje pomiaru |
| Logowanie do VPS jako `root` z hasłem | **Zła praktyka** | Należy używać kluczy SSH, osobnego użytkownika bez roota, wyłączonego logowania hasłem, firewalla i fail2ban. Agent z dostępem do roota może zniszczyć cały serwer |
| Hermes w Dockerze z jednym podmontowanym folderem | **Dobra praktyka** | Warto ją przyjąć dla każdego agenta działającego bez nadzoru |
| NVMe „wyeliminowało wąskie gardła” | **Język marketingowy** | Agenci czekają głównie na odpowiedź API, nie na dysk. Pamięć RAM ma większe znaczenie (raport słusznie o tym pisze) |
| Kredyty AI Hostingera i ponad 200 modeli przez OpenRouter | **Niezweryfikowane** | Nie dało się tego potwierdzić. Nawet jeśli to prawda, Claude Code i Codex korzystają z własnych subskrypcji, a nie z kredytów Hostingera |
| Ceny i transfer planów KVM 1–8 | **Częściowo potwierdzone** | Parametry zgadzają się z innymi źródłami. KVM 2: 2 vCPU, 8 GB RAM, 100 GB NVMe. Ceny w raporcie nie są podane |

## 2. AI-crew: co poprawić i jaki wariant warto zbudować

### Co już mamy, a co wnosi wzorzec Herdr

| Potrzeba | Obecny plan AI-crew (raport z 31.10) | Wzorzec Herdr + VPS | Wniosek |
| --- | --- | --- | --- |
| Agenci pracują, gdy komputer jest wyłączony | Sesje Claude Code w chmurze, zaplanowane zadania, GitHub Actions | Demon Herdr na VPS-ie | **Mamy to bez VPS-a.** Ta sesja też działa w chmurze |
| Niezależna recenzja | Recenzent na innym modelu Claude (Opus vs Sonnet), tylko do odczytu | Codex sprawdza Claude'a | **Do przejęcia:** recenzent innego dostawcy (GPT) jest bardziej niezależny niż inny model tej samej rodziny |
| Kanał do właściciela | Komentarze w PR, powiadomienia GitHuba, aplikacja Claude | Hermes przez Telegram lub Discord | **Opcjonalnie.** Telegram jest wygodny, ale to kolejny kanał, który trzeba zabezpieczyć |
| Pamięć między sesjami | Pliki w repo (ADR, journal, wiki) | Prywatna pamięć Hermesa w `~/.hermes/` | **Pliki w repo lepsze.** Pamięć Hermesa jest poza gitem, poza przeglądem i jest „drugim źródłem prawdy” |
| Nowe skille | Tylko przez PR i audyt (`skill-auditor`) | Hermes sam zapisuje nowe skille | **Konflikt z regułą zatrudniania.** Skille Hermesa muszą trafiać do repo przez PR |
| Izolacja | Uprawnienia Claude Code, reguły deny, piaskownica | Kontener Docker z jednym wolumenem | **Do przejęcia** dla każdego agenta bez nadzoru |
| Wielu dostawców AI | Claude, Codex ręcznie (ChatGPT w `educationInfluencer`, przegląd Codexa w `education-games`) | Claude + Codex + Hermes w jednym panelu | **Formalizacja tego, co już robisz** |

### Proponowany wariant: „crew wielodostawcowy”, w trzech krokach

| Krok | Co | Infrastruktura | Koszt dodatkowy | Kiedy |
| --- | --- | --- | --- | --- |
| **A. Recenzja krzyżowa** | Codex (GPT) jako drugi recenzent bramkowy PR-ów pisanych przez Claude'a. Wynik jako komentarz w PR, decyzja nadal u Ciebie. Szablon promptu recenzji w `AI-crew` | GitHub Actions albo ręcznie, jak dziś | Subskrypcja ChatGPT, którą już masz, albo klucz API | Od razu, na `education-games` i `learning_tools` |
| **B. Powiadomienia i zgody z telefonu** | Powiadomienia o PR-ach wymagających decyzji. Najprościej: aplikacja GitHub i aplikacja Claude. Telegram dopiero, gdy te nie wystarczą | Bez serwera | 0 PLN | Gdy będzie więcej niż kilka PR-ów tygodniowo |
| **C. Runner na VPS-ie (pilotaż)** | Herdr + Claude Code + Codex na VPS-ie, każdy agent w kontenerze z jednym folderem projektu. Hermes tylko, jeśli potrzebny jest Telegram lub Obsidian | VPS z 4–8 GB RAM | Około 15–60 PLN/mies. (sekcja 4) | Tylko przy jednym z wyzwalaczy poniżej |

**Wyzwalacze kroku C**, z których wystarczy jeden:

- zadania trwają godzinami i nie mieszczą się w limitach sesji w chmurze ani GitHub Actions;
- potrzebny jest dostęp do zasobów, których nie ma w chmurze (lokalny Obsidian, duże pliki, emulator Androida do testów);
- chcesz koordynować agentów różnych dostawców w czasie rzeczywistym, a nie przez PR-y.

**Zasady dla kroku C**, jeśli do niego dojdzie:

- osobny serwer tylko dla agentów, nigdy razem ze sklepem lub stroną;
- logowanie kluczem SSH na użytkownika bez roota;
- sekrety w zmiennych środowiskowych, nie w repo;
- kopia zapasowa poza dostawcą;
- konfiguracja serwera (`docker-compose.yml`, skrypt instalacyjny) w `AI-crew/blueprints/`, żeby serwer dało się odtworzyć u innego dostawcy w kilka godzin.

**Uwaga o subskrypcji:** uruchamianie oficjalnego Claude Code na własnym VPS-ie z tokenem subskrypcji (`claude setup-token`) jest według źródeł wtórnych dopuszczalne do pracy na własny użytek. Nie wolno go używać do obsługi innych osób ani w narzędziach firm trzecich. Anthropic zmieniał te zasady w 2026 r. Przed uruchomieniem agentów pracujących dla klientów lub w produkcie przejdź na klucz API.

## 3. Projekty: czy i kiedy serwer na Hostingerze byłby przydatny

Przejrzane repozytoria (7 listopada 2026): `education-games` (gałąź `jvp-notatki-2026-10-30`, wersja 1.2.0), `learning_tools` (`main`), `educationInfluencer` (`master`, journal 037–042, propozycje w `wiki/proposals/`). Historii innych rozmów z Claude nie mam z tej sesji. Uwzględniłem to, co z nich trafiło do repozytoriów: transkrypcje notatek JvP, journale i decyzje.

### 3.1. Junk vs Plants (JvP)

**Stan:** gra w Godot 4.7 na Androida, 60 poziomów, 7 języków. **Celowo bez serwera**:

- zapis tylko w telefonie;
- wydarzenia liczone od pierwszego uruchomienia na koncie;
- gra ze znajomym przez lokalne Wi-Fi (ENet, wykrywanie przez UDP);
- zakupy rubinów tylko jako podgląd.

`PLAN_PUBLIKACJI.md` prowadzi do Google Play i App Store. Gra jest dla dzieci.

| Potrzeba | Kiedy | Czy potrzebny serwer | Lepsze rozwiązanie |
| --- | --- | --- | --- |
| Strona z polityką prywatności (wymagana przez oba sklepy) | Przed wydaniem | Nie | Strona statyczna (Cloudflare Pages, GitHub Pages) albo podstrona na przyszłej domenie projektu |
| Strona gry i wersja webowa (eksport HTML5 z Godota) | Opcjonalnie | Nie | itch.io (darmowy hosting gier HTML5, gotowa publiczność) |
| Kopia zapisu w chmurze | Później (punkt w planie) | Nie własny | Google Play Games Services (zapisy w chmurze), iCloud na iOS |
| Gra ze znajomym przez internet, nie tylko w Wi-Fi | Ewentualnie | Tak (relay lub serwer gry) | Usługi zarządzane (np. Nakama w chmurze, relay od dostawcy) albo mały VPS. **Uwaga:** gra dla dzieci w programie Google Play Families oznacza ostre wymogi co do danych i komunikacji między graczami. Gra przez internet wymaga przeglądu prawnego |
| Wydarzenia w tym samym czasie dla wszystkich, rankingi | Ewentualnie | Tak, lekki backend | Firebase lub Supabase albo zdalna konfiguracja. Mniejsza odpowiedzialność niż własny serwer |
| Prawdziwe zakupy | Przed wydaniem albo wcale | Nie | Google Play Billing i StoreKit, z bramką dla rodzica |

**Ocena przydatności Hostingera dla JvP:** **niska teraz, umiarkowana później.** VPS miałby sens tylko jako serwer gry przez internet. Przy grze dla dzieci usługa zarządzana jest prawie zawsze lepsza od własnego serwera, bo odpowiedzialność za dane i bezpieczeństwo jest mniejsza.

### 3.2. Nowa aplikacja na bazie Exam Drill („Nina's Drills”)

**Stan w `learning_tools`:**

- statyczna aplikacja HTML/JS bez zależności (decyzja 0002);
- klient Godot na Androida, który wczytuje zestawy pytań z plików (decyzja 0007);
- świadomie **bez hostingu** (decyzja 0006);
- **bez backendu i kont** (odrzucone w `out-of-scope/backend-and-account-sync.md`, z warunkiem powrotu: „kilku użytkowników chce wspólnych statystyk” albo „gubienie postępu”).

W `educationInfluencer` (journal 041) Exam Drill to **najmocniejszy kandydat na przychód**: płatne zestawy pytań dla dorosłych, wersja angielska, aplikacja uniwersalna (E06).

| Potrzeba nowej aplikacji | Czy potrzebny serwer | Najprostsze rozwiązanie |
| --- | --- | --- |
| Publiczna wersja webowa (PWA) | Nie | Cloudflare Pages: darmowy, HTTPS, działa też z prywatnego repo. GitHub Pages z repo prywatnego wymaga płatnego planu GitHub (do sprawdzenia) |
| Sprzedaż płatnych zestawów pytań | **Nie** | Aplikacja już importuje zestawy z plików. Zestaw można sprzedawać jako plik do pobrania przez platformę, która rozlicza VAT (Lemon Squeezy, w części Payhip) albo przez Ko-fi. Zero kodu serwerowego |
| Zabezpieczenie płatnych zestawów przed kopiowaniem | Tak, jeśli to ważne | Klucze licencyjne platformy sprzedażowej albo backend (Supabase) z kontami. Dla pierwszej wersji zwykle nie warto |
| Synchronizacja postępu między urządzeniami, konta | Tak | Supabase lub Firebase: logowanie i baza gotowe, darmowy próg. Lepsze niż własny VPS, bo nie trzeba samemu pilnować bezpieczeństwa kont |
| Analityka użycia | Opcjonalnie | Prosta analityka bez ciasteczek (np. Cloudflare Web Analytics) |

**Warunek wstępny niezależny od hostingu:** nowa aplikacja potrzebuje **osobnego repozytorium** bez `ITIL4_sources/`, czyli bez materiałów zewnętrznych w PDF. Musi mieć też jasne zastrzeżenie o znaku ITIL® (PeopleCert). Upublicznienie to Twoja decyzja (reguła w `learning_tools/CLAUDE.md`).

**Ocena przydatności Hostingera:** **niska.** Hosting statyczny i platforma sprzedażowa pokrywają wersję 1. Gdy dojdą konta i synchronizacja, backend jako usługa (Supabase lub Firebase) wygrywa z własnym VPS-em pod względem bezpieczeństwa i pracy własnej.

### 3.3. Influencer-AI: strona, blog, sklep z postaciami

**Stan** (journal 037, 040, 041 i `wiki/proposals/monetisation-and-community.md`). Kolejność jest ustalona:

1. Teraz, za 0 PLN: strona źródeł (TASK-0038, GitHub Pages), lista e-mailowa, Ko-fi.
2. Interakcja.
3. Społeczność od około 500–1000 obserwujących.
4. Produkty od około 1000+ zaangażowanych obserwujących.

Domena, produkty i KDP to decyzja po 8-tygodniowym teście. Reguła twarda nr 3: konta i wydatki zatwierdza tylko Owner.

| Etap | Potrzeba | Najprostsze rozwiązanie | Rola Hostingera |
| --- | --- | --- | --- |
| 0 (teraz) | Strona źródeł, quiz Quilla (statyczny Exam Drill), polityka prywatności | Cloudflare Pages lub GitHub Pages, generowane skryptem z `content/reels/`. Repo jest prywatne, więc Cloudflare Pages albo osobne publiczne repo tylko z wygenerowaną stroną | Brak |
| 0 | Lista e-mailowa | Buttondown lub Substack (już w planie) | Brak. Poczta Hostingera to nie narzędzie do newsletterów |
| 2 | Blog | Strona statyczna (Astro lub Hugo, wpisy w Markdown, które agenci piszą przez PR) albo Ghost(Pro) | Możliwa, jeśli wybierzesz WordPress |
| 3 | Produkty cyfrowe (planery, karty z faktami, e-booki) | Ko-fi Shop, Payhip, Lemon Squeezy (rozlicza VAT za Ciebie), Amazon KDP | Brak |
| 3 | Merch z postaciami (druk na żądanie) | Printful lub Printify z Etsy albo Shopify. Albo WooCommerce na własnym hostingu | **Tu Hostinger ma sens:** plan Business lub Cloud z WooCommerce. Tańszy niż Shopify, ale odpowiedzialność za aktualizacje, bezpieczeństwo, RODO i VAT (OSS) jest po Twojej stronie |
| 3+ | Platforma z kontami, kursami, członkostwem | Ko-fi Membership, Patreon albo platforma kursów. Własna platforma dopiero przy dużej skali | VPS albo hosting w chmurze, raczej nie na tym etapie |

**Ocena przydatności Hostingera:** **niska przez najbliższe 2–3 miesiące, umiarkowana od etapu 3**, jeśli wybierzesz własny sklep WooCommerce zamiast platformy. Na etapie 3 warto porównać koszt łączny:

- Hostinger + WooCommerce + płatności + księgowość VAT;
- Shopify albo Etsy + Printful;
- Lemon Squeezy dla samych produktów cyfrowych.

### 3.4. Pozostałe repozytoria

- **`klasa6` i `FOZ-ZOE`** publikują przez Dysk Google i druk. Nie potrzebują hostingu.
- **`doktorat_git`, `favorites_training`, `git_training_github`** są nieaktywne.
- **`AI-agents`** to standard skilli i nie potrzebuje hostingu.

### Podsumowanie przydatności serwera

| Projekt | Teraz | Za 6–12 miesięcy | Co zamiast VPS-a na start |
| --- | --- | --- | --- |
| AI-crew | Niska | Umiarkowana (runner agentów, krok C) | Chmura Claude Code, GitHub Actions, recenzja Codexem |
| JvP | Niska | Niska do umiarkowanej (gra przez internet) | Strona statyczna, itch.io, Google Play Games Services |
| Exam Drill / Nina's Drills | Niska | Niska do umiarkowanej (konta, synchronizacja) | Cloudflare Pages i sprzedaż plików zestawów przez platformę |
| Influencer-AI | Niska | Umiarkowana (sklep WooCommerce, blog WordPress) | Strona statyczna, Ko-fi, Buttondown, platformy sprzedażowe |

## 4. Porównanie ofert

### Rodzaje rozwiązań

| Rozwiązanie | Do czego | Zalety | Wady | Koszt orientacyjny |
| --- | --- | --- | --- | --- |
| **Hostinger VPS (KVM 1/2/4)** | Runner agentów, serwer gry, własne aplikacje | Szablony jednym kliknięciem (Hermes, Docker Manager), prosty panel hPanel, asystent AI, centra danych w UE | Niska cena tylko przy przedpłacie na 24–48 miesięcy; odnowienie około 1,5–2,5× drożej. Kopie tygodniowe, tylko dwie ostatnie (według recenzji). Administracja i bezpieczeństwo po Twojej stronie | KVM 2: około 7–9 USD/mies. na start (przedpłata), około 15 USD/mies. po odnowieniu |
| **Hostinger hosting Business (WordPress/WooCommerce)** | Blog, sklep | Prosty start, WooCommerce gotowy, kopie zapasowe, poczta | Ograniczenia hostingu współdzielonego; podwyżka przy odnowieniu; kreatory (Website Builder, Horizons) wiążą stronę z Hostingerem | Około 4 USD/mies. na start (48 mies.), około 9–17 USD/mies. po odnowieniu |
| **Hetzner Cloud (CX23 i podobne)** | Runner agentów, serwer gry | Rozliczenie godzinowe lub miesięczne bez przedpłaty, UE (Niemcy, Finlandia), dobra wydajność | Podwyżki w kwietniu i czerwcu 2026 (linia CPX nawet ponad 2×); brak szablonów „Hermes jednym kliknięciem”; panel dla technicznych | Około 4,5–5 EUR/mies. + VAT za mały serwer (po podwyżce z kwietnia) |
| **Cloudflare Pages** | Strony statyczne, PWA | Za darmo, HTTPS, CDN, działa z prywatnym repo, analityka bez ciasteczek | Tylko strony statyczne (plus Workers do lekkiej logiki) | 0 PLN |
| **GitHub Pages** | Strony statyczne | Za darmo dla repo publicznych, zero konfiguracji | Repo prywatne wymaga płatnego planu GitHub (do sprawdzenia) | 0 PLN |
| **itch.io** | Wersja webowa JvP, strona gry | Za darmo, publiczność graczy | Tylko gry | 0 PLN |
| **Supabase lub Firebase** | Konta, synchronizacja, rankingi | Gotowe logowanie i baza, darmowy próg, brak serwera do utrzymania | Uzależnienie od API dostawcy; koszty rosną z użyciem | 0 PLN na start |
| **Ko-fi, Payhip, Lemon Squeezy** | Produkty cyfrowe, napiwki | Bez serwera. Lemon Squeezy rozlicza VAT jako sprzedawca (merchant of record) | Prowizje (około 5% + opłaty) | 0 PLN stałych |
| **Shopify z Printful** | Sklep z merchem | Bez administracji, integracje druku na żądanie | Abonament miesięczny, prowizje | Około 30–40 USD/mies. (niezweryfikowane) |
| **Chmura Claude Code i GitHub Actions** | Crew agentów | Już używane, bez serwera, sesje dostępne z telefonu | Limity czasu sesji i minut Actions; brak stałego procesu | W ramach subskrypcji |

### Koszt łączny dla 24 miesięcy (orientacyjnie)

| Scenariusz | Co obejmuje | Koszt przez 24 miesiące |
| --- | --- | --- |
| **S0 — zalecany teraz** | Cloudflare Pages lub GitHub Pages, domena u niezależnego rejestratora, Ko-fi, Buttondown | Około 80–160 PLN (tylko domena) |
| **S1 — runner agentów na Hostingerze** | KVM 2, przedpłata 24 miesiące | Około 800–900 PLN z góry, potem około 700 PLN rocznie |
| **S1' — runner agentów na Hetznerze** | Mały serwer, płatność miesięczna | Około 550–650 PLN, bez przedpłaty, rezygnacja w każdej chwili |
| **S2 — sklep WooCommerce na Hostingerze** | Business, przedpłata 48 miesięcy | Około 750–800 PLN z góry za 4 lata, potem około 450–800 PLN rocznie, plus płatności, wtyczki i księgowość |
| **S3 — sklep na platformie** | Shopify z Printful albo Etsy | Około 2800–3800 PLN abonamentu, plus prowizje; zero administracji |

Kurs przyjęty orientacyjnie: 1 USD ≈ 3,8–4,0 PLN, 1 EUR ≈ 4,3 PLN. Nie wliczono subskrypcji Claude i ChatGPT, które płacisz niezależnie, ani kredytów Higgsfield (około 295 PLN miesięcznie według `financial-scenarios.md`).

## 5. Uzależnienie od dostawcy: wyzwania i koszt przesiadki

### Co wiąże najbardziej

| Element | Siła powiązania | Koszt przesiadki | Jak go obniżyć od pierwszego dnia |
| --- | --- | --- | --- |
| Przedpłata 24–48 mies. | **Wysoka (finansowa)** | Utrata niewykorzystanej części (zwrot zwykle tylko w ciągu 30 dni) | Kupować na krótszy okres do czasu potwierdzenia potrzeby, nawet drożej miesięcznie |
| Podwyżka przy odnowieniu | Wysoka | Albo płacisz około 2× więcej, albo się przenosisz | Zapisać datę odnowienia; przegląd ofert 2 miesiące wcześniej |
| Domena kupiona u Hostingera | Średnia | Transfer możliwy, ale zwykle blokada 60 dni po rejestracji lub transferze i opłata za rok przy transferze | Domena u niezależnego rejestratora (np. Cloudflare Registrar), DNS osobno od hostingu |
| Poczta e-mail u Hostingera | Średnia | Migracja skrzynek, ryzyko utraty poczty w trakcie | Poczta projektu na koncie Google projektu (już w `owner-guide-accounts.md`) |
| Strony w Website Builderze lub Horizons | **Wysoka** | Zwykle przebudowa od zera (dni pracy) | Nie budować w zamkniętych kreatorach. Strony statyczne w gicie albo WordPress |
| WordPress/WooCommerce | Średnia | Przeniesienie bazy i plików, DNS, ponowna konfiguracja płatności, przerwa w sprzedaży (1–3 dni pracy) | Kopie zapasowe poza dostawcą; zamówienia i klienci w eksportowalnej formie |
| VPS z Dockerem | **Niska**, jeśli konfiguracja jest w gicie | Pół dnia do dnia | `docker-compose.yml`, skrypt instalacyjny i kopie danych w repo lub poza dostawcą |
| Szablon „Managed Hermes” w hPanelu | Średnia | Ręczna instalacja Hermesa gdzie indziej. Pamięć `~/.hermes/` jest w plikach, więc przenośna | Instalować Hermesa z oficjalnego repo w Dockerze, nie przez szablon |
| Pamięć Hermesa | Średnia (narzędziowa) | Wiedza uwięziona w formacie jednego narzędzia | Wszystko istotne zapisywać w repo (decyzje, wiki); Hermes tylko jako pamięć podręczna |
| Herdr (AGPL) | Niska | Zastępowalny przez tmux albo agent view w Claude Code | — |

### Ryzyka do monitorowania

1. **Bezpieczeństwo VPS-a z agentami.** Agent z powłoką plus treści z internetu (Telegram, strony, notatki) to ryzyko wstrzyknięcia poleceń. Odpowiedź: kontenery, minimalne uprawnienia, brak sekretów płatniczych na tym serwerze.
2. **Dane dzieci (JvP).** Każda funkcja online w grze dla dzieci podlega zasadom Google Play Families i RODO. Lepiej nie zbierać danych wcale.
3. **Podatki i forma prawna przy sprzedaży.** Już odnotowane w wiki Influencer-AI jako decyzja Ownera. Platforma rozliczająca VAT (merchant of record) zdejmuje dużą część tego obciążenia.
4. **Zmiany zasad subskrypcji AI.** Uruchamianie Claude Code i Codexa na serwerze z tokenami subskrypcji jest szarą strefą przy zastosowaniach innych niż osobiste.
5. **Zmiany cen dostawców.** Hetzner podniósł ceny dwa razy w 2026 r. Ten sam scenariusz może dotyczyć każdego dostawcy. Przenośna konfiguracja to jedyna trwała ochrona.

## 6. Rekomendacja i kolejne kroki

| Kiedy | Krok | Projekt |
| --- | --- | --- |
| Teraz | Kupić domenę projektu u niezależnego rejestratora (decyzja Ownera po teście 8-tygodniowym albo wcześniej, jeśli potrzebna jest polityka prywatności JvP) | wszystkie |
| Teraz | Postawić stronę statyczną na Cloudflare Pages: strona źródeł (TASK-0038), polityka prywatności JvP, ewentualnie demo Exam Drill | Influencer-AI, JvP, Exam Drill |
| Teraz | Pilotaż recenzji krzyżowej Codexem na 5–10 PR-ach; wynik w journalu AI-crew | AI-crew |
| Przed wydaniem JvP | Wybrać: brak gry przez internet albo usługa zarządzana; bez własnego serwera | JvP |
| Przy wersji angielskiej Exam Drill | Osobne repo aplikacji; sprzedaż zestawów jako plików przez platformę z rozliczaniem VAT | Exam Drill |
| Etap 3 Influencer-AI | Porównanie kosztu: WooCommerce na Hostingerze vs Shopify/Etsy + Printful vs Lemon Squeezy | Influencer-AI |
| Gdy spełni się wyzwalacz kroku C | Pilotaż VPS-a dla agentów (Hostinger KVM 2 lub Hetzner), konfiguracja w `blueprints/`, najpierw krótki okres rozliczeniowy | AI-crew |

### Otwarte pytania do Ciebie

1. Czy JvP ma kiedykolwiek mieć grę przez internet, czy zostaje przy lokalnym Wi-Fi?
2. Czy „Nina's Drills” ma być nową aplikacją (nowe repo, angielski, sprzedaż), czy wariantem `learning_tools`?
3. Jaki rodzaj sklepu przy postaciach: produkty cyfrowe, merch, a może jedno i drugie?
4. Czy masz już konto lub usługi w Hostingerze (domena, poczta, hosting)? To zmienia koszt przesiadki.

## Źródła

- Raport wejściowy: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md)
- Repozytoria JeanPaulSzefler (stan z 7 listopada 2026): `education-games` (`junk-vs-plants/README.md`, `PLAN_PUBLIKACJI.md`, przegląd Codexa z 30.10), `learning_tools` (`CLAUDE.md`, decyzje 0002, 0006, 0007, `out-of-scope/backend-and-account-sync.md`), `educationInfluencer` (journal 021, 037, 040, 041; `wiki/proposals/monetisation-and-community.md`, `own-apps-for-personas.md`, `financial-scenarios.md`; TASK-0037, TASK-0038)
- [Raport AI-crew z 31 października 2026](2026-10-31-efficient-ai-crew-and-repo-setup.md)
- Herdr: [Bitdoze, recenzja](https://www.bitdoze.com/herdr-agent-multiplexer/), [AI Weekly](https://aiweekly.co/alerts/herdr-adds-agent-state-awareness-to-terminal-multiplexing), [knightli](https://knightli.com/en/2026/07/06/herdr-terminal-agent-multiplexer/)
- Hermes Agent: [hermes-agent.org](https://hermes-agent.org/) (możliwie strona nieoficjalna; repo `NousResearch/hermes-agent` jako źródło pierwotne)
- Hostinger VPS i Hermes: [HostAdvice, ceny VPS z odnowieniem](https://hostadvice.com/hosting-company/hostinger-reviews/vps-pricing/), [Findstack, KVM 1 vs 2 vs 4](https://findstack.com/resources/hostinger-vps-for-ai-agents), [Remote OpenClaw](https://www.remoteopenclaw.com/blog/hermes-agent-hostinger-vps), [Claude Market](https://claudemarket.ai/blog/hermes-agent-hostinger-vps), [learnwithhasan, kopie i ograniczenia](https://learnwithhasan.com/self-hosting-hub/vps-providers/hostinger-vps/)
- Hostinger hosting i WooCommerce: [Website Builder Expert, ceny 2026](https://www.websitebuilderexpert.com/web-hosting/hostinger-pricing/), [WebsiteRating, odnowienia](https://www.websiterating.com/hosting/hostinger-review/)
- Hetzner 2026: [Tom's Hardware](https://www.tomshardware.com/tech-industry/hetzner-to-raise-prices-by-up-to-37-percent-from-april-1), [Northflank](https://northflank.com/blog/hetzner-cloud-server-price-increases), [WZ-IT, czerwiec 2026](https://wz-it.com/en/blog/hetzner-price-increase-june-2026-cpx-ccx-alternatives/)
- Cloudflare Pages: [changelog limitów, styczeń 2026](https://developers.cloudflare.com/changelog/post/2026-01-23-pages-file-limit-increase/)
- Platformy sprzedaży: [We Are Founders, Gumroad vs Payhip vs Lemon Squeezy](https://www.wearefounders.uk/best-platforms-for-selling-digital-products-in-2026/), [Getly](https://www.getly.store/blog/gumroad-vs-lemon-squeezy)
- Claude Code na VPS: [Autonomee, uwierzytelnianie na serwerze](https://autonomee.ai/blog/claude-code-server-vps-authentication-guide/), [Virtua Cloud](https://www.virtua.cloud/learn/en/tutorials/run-claude-code-vps). Źródła wtórne; obowiązują aktualne warunki Anthropic

Ograniczenia tej wersji: strona hostinger.com była zablokowana w ustawieniach sieci tej sesji, więc ceny pochodzą z serwisów porównawczych, często afiliacyjnych. Nie sprawdziłem regulaminu zwrotów ani dokładnych zasad kopii zapasowych bezpośrednio u Hostingera. Kwestie prawne (Google Play Families, VAT, znak ITIL®) wymagają potwierdzenia u źródła.
