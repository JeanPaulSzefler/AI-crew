# Orkiestracja agentów (Herdr) i hosting (Hostinger): analiza dla AI-crew i projektów JvP, Nina's Drills i Influencer-AI

7 listopada 2026 · **Wersja 3 (robocza)** · Punkty odniesienia: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md) oraz [analiza Codexa z 7.11](2026-11-07-codex-ai-crew-hosting-i-migracja.md)

## Co się zmieniło

### Wersja 3: po weryfikacji raportu Codexa

Codex przygotował równoległą analizę (commit `48d8031`, scalona z tą gałęzią w `00b7842`). Napisał ją **przed** odpowiedziami Ownera, więc zakłada JvP tylko z lokalną grą przez Wi-Fi. Jej twierdzenia sprawdziłem w kodzie i w dokumentacji pod przypiętymi wersjami (sekcja 8). Wersja 3 przejmuje z niej to, czego brakowało w wersji 2:

1. **GitHub Pages nie nadaje się do stron komercyjnych.** Regulamin wyklucza biznes, sklep i SaaS. Polityka prywatności płatnej gry, sklep i Nina's Drills idą na Cloudflare Pages (sekcje 3.3 i 7).
2. **Pliki APK nie zmieszczą się na Cloudflare Pages.** Limit to 25 MiB na plik, a Exam Drill 1.6 ma 26,6 MB, JvP 1.2.0 ma 57,7 MB. APK dystrybuować przez Google Play, wydania na GitHubie albo magazyn obiektowy.
3. **Wersja webowa JvP to nie tylko eksport.** Godot Web obsługuje tylko renderer Compatibility (JvP używa Mobile), a przeglądarka nie ma UDP ani ENet. Nakama działa przez WebSocket, więc ten sam backend obsłuży przyszły klient webowy.
4. **Herdr i `herdr-core` nie izolują agentów.**
   - Po restarcie maszyny procesy nie przetrwają.
   - `herdr-core` (CLI `hc`) działa z uprawnieniami konta i nie jest piaskownicą.
   - Docker z jednym wolumenem to nie pełna izolacja: nie montować `docker.sock` i nie uruchamiać kontenerów uprzywilejowanych.
5. **Koszt czasu Ownera.** Model Codexa wycenia godzinę pracy, przyjmując 100 zł. Przy backendzie gier czas administracji jest większą pozycją niż sam serwer (sekcja 5).
6. **Szacunki nakładu przy przesiadce** w godzinach, ryzyko przedpłaty, przypisanie postępu w przeglądarce do domeny, Mac do budowania wersji iOS, bezpieczeństwo GitHub Actions (sekcje 2, 5, 6).

### Wersja 2: odpowiedzi Ownera

Wersja 1 jest w historii repo (commit `6e83de0`), wersja 2 w `9a61bea`. Wersja 2 uwzględniła odpowiedzi Ownera z 7 listopada:

| Pytanie | Odpowiedź | Wpływ na wnioski |
| --- | --- | --- |
| JvP: gra przez internet? | **Tak**: gra przez internet, konta na serwerze, zakupy po zalogowaniu kontem Google | JvP **potrzebuje backendu**. Serwer staje się uzasadniony (sekcja 3.1) |
| Exam Drill jako nowa aplikacja? | **Tak**: osobna aplikacja, nazwa robocza „Nina's Drills” | Osobne repo; sprzedaż zestawów w dwóch kanałach (web i Google Play) wymaga wspólnych kont i uprawnień (sekcja 3.2) |
| Sklep: cyfrowy czy merch? | **Jedno i drugie** | Dwa tory sprzedaży i dwie marki: postacie Influencer-AI (dorośli) i JvP (rodzice) (sekcja 3.3) |
| Usługi u Hostingera? | **Brak** | Brak kosztów utopionych; wybór dostawcy jest w pełni otwarty |

## W skrócie

1. **Serwer jest teraz uzasadniony, ale dla gry, nie dla agentów.** Gra przez internet, konta i zakupy w JvP wymagają backendu. Rekomenduję **Nakamę**: otwartoźródłowy serwer gier z oficjalnym SDK dla Godota, logowaniem przez Google i Apple, grą w czasie rzeczywistym i weryfikacją zakupów z Google Play i App Store. Nakama działa w Dockerze z bazą Postgres **na małym VPS-ie**.
   - Hostinger KVM 2 dobrze się do tego nadaje. Hetzner jest równorzędną alternatywą z płatnością miesięczną.
   - Uzależnienie jest niskie, bo kod jest otwarty, a dane to zwykły Postgres.
2. **Jeden backend kont dla JvP i Nina's Drills.** Nina's Drills będzie sprzedawać zestawy pytań na stronie i w Google Play. Wspólny mechanizm kont i uprawnień (co kto kupił) oszczędza pracę. Nakama to obsługuje; Supabase jest alternatywą bardziej „aplikacyjną”.
3. **Największe wyzwania JvP online nie są techniczne, tylko regulacyjne.** Gra jest dla dzieci, więc obowiązuje:
   - program Google Play Families;
   - zgoda rodzica według RODO (w Polsce najpewniej poniżej 16 lat; do potwierdzenia);
   - obowiązek usuwania konta w aplikacji i przez stronę WWW;
   - zakaz otwartego czatu z nieznajomymi;
   - na iOS: obowiązek „Sign in with Apple” obok logowania Google.
4. **Sklep: na start bez własnego serwera.**
   - Produkty cyfrowe przez platformę rozliczającą VAT (Lemon Squeezy, w części Payhip) albo Ko-fi.
   - Merch przez druk na żądanie (Printful lub Printify) z Etsy albo Shopify.
   - Własny WooCommerce (np. na Hostingerze) dopiero przy skali, która uzasadnia administrację i rozliczenia VAT po Twojej stronie.
5. **Agentów AI-crew na VPS nadal nie trzeba.** Jeśli kiedyś trafią na serwer, to na **osobny**, nie na ten z kontami i płatnościami graczy.
6. **Strony na Cloudflare Pages, APK poza nim.**
   - Strony komercyjne nie na GitHub Pages (regulamin).
   - APK przez Google Play, wydania na GitHubie albo magazyn obiektowy (limit 25 MiB na plik).
7. **Największy koszt to czas, nie serwer.** Administracja backendu gier to około 2–4 h miesięcznie. Przy wycenie 100 zł/h daje to więcej niż sam VPS (sekcja 5).

Codex i ja doszliśmy niezależnie do tych samych głównych wniosków:

- nie kupować dziś dużego VPS-a ani wieloletniego pakietu;
- statyczne strony teraz;
- produkcja oddzielona od agentów;
- przenośny stos (Docker, Postgres);
- domena na koncie Ownera.

Różnica wynika z decyzji Ownera o grze online. Dla JvP serwer przestał być „potencjalny” i stał się planowany.

Ceny są **orientacyjne**. Strona hostinger.com była zablokowana w tej sesji; dane pochodzą z serwisów porównawczych, często afiliacyjnych. Przed zakupem sprawdź w koszyku.

## 1. Ocena raportu wejściowego

| Teza raportu | Ocena | Komentarz |
| --- | --- | --- |
| Herdr (w raporcie „Herder”) zarządza kilkoma agentami i trzyma ich na serwerze po zamknięciu aplikacji | **Potwierdzone, z zastrzeżeniem** | Otwartoźródłowy multiplekser terminala (Rust, AGPL). Śledzi stan agentów; obsługuje Claude Code i Codex. Windows w becie. **Po restarcie maszyny procesy nie przetrwają**; Herdr przywraca układ i może wznowić wspierane sesje agentów (README, potwierdzone przez Codexa i przeze mnie). Podobną podstawową trwałość daje tmux |
| Skill `herder-core` | **Częściowo potwierdzone** | Istnieje osobne narzędzie **`herdr-core` z CLI `hc`**: terminale działające po wyjściu, API przez gniazdo. Według jego dokumentacji bezpieczeństwa działa z uprawnieniami konta i **nie jest piaskownicą ani brokerem uprawnień**. Nazwy „skill herder-core” nie potwierdzono |
| Hermes Agent: trwała pamięć, sam pisze skille | **Potwierdzone** | Nous Research, MIT, luty 2026. Pamięć w `~/.hermes/`, skille w standardzie Agent Skills, bramka do komunikatorów |
| Weryfikacja przez innego agenta podnosi jakość | **Kierunkowo trafne, niezmierzone** | Zgodne z raportem AI-crew z 31.10 (niezależny recenzent) |
| Logowanie `root` z hasłem | **Zła praktyka** | Klucze SSH, użytkownik bez roota, firewall, fail2ban |
| Hermes w Dockerze z jednym wolumenem | **Dobra praktyka, ale nie pełna izolacja** | Przyjąć dla agentów bez nadzoru. Wolumen nadal może zostać usunięty lub zaszyfrowany. Zamontowany `docker.sock` albo kontener uprzywilejowany niweczą izolację. Dokumentacja bezpieczeństwa Hermesa też wskazuje izolację na poziomie systemu, a nie reguły wewnątrz procesu |
| NVMe „wyeliminowało wąskie gardła” | **Marketing** | Agenci czekają głównie na API; ważniejsza jest pamięć RAM |
| Kredyty AI Hostingera, 200+ modeli przez OpenRouter | **Niezweryfikowane** | Claude Code i Codex i tak korzystają z własnych subskrypcji |

## 2. AI-crew: wariant „crew wielodostawcowy”

Zgodny z wariantami A–C Codexa (na żądanie → laboratorium zdalne → automatyzacja przez repo i CI). Kroki poniżej:

| Krok | Co | Infrastruktura | Kiedy |
| --- | --- | --- | --- |
| **A. Recenzja krzyżowa** | Codex (GPT) jako drugi recenzent PR-ów pisanych przez Claude'a. Formalizuje to, co już robisz ręcznie w `education-games` i `educationInfluencer` | GitHub Actions albo ręcznie | Od razu |
| **B. Powiadomienia i zgody z telefonu** | Aplikacja GitHub i aplikacja Claude; Telegram dopiero, gdy te nie wystarczą | Bez serwera | Przy większej liczbie PR-ów |
| **C. Runner na VPS-ie (pilotaż)** | Herdr + Claude Code + Codex. Każdy agent pod zwykłym użytkownikiem, w kontenerze z jednym folderem, z limitami RAM/CPU, bez `docker.sock` i bez trybu uprzywilejowanego. Najwyżej dwa aktywne zadania na start | **Osobny** VPS, nigdy ten z backendem gry. Krótki okres rozliczeniowy | Tylko przy konkretnym wyzwalaczu: długie zadania, zasoby spoza chmury, koordynacja agentów w czasie rzeczywistym |

**Pomiar pilotażu (za Codexem).** Około 20 porównywalnych, małych zadań z aktywnych projektów. Porównać jednego agenta z parą wykonawca + recenzent. Zapisywać:

- zaakceptowany wynik;
- regresje;
- koszt modeli;
- czas człowieka;
- liczbę ponowień.

Więcej ról tylko wtedy, gdy obniżają koszt zaakceptowanej zmiany lub czas człowieka bez utraty jakości.

**Bezpieczeństwo automatyzacji w GitHub Actions (za Codexem i dokumentacją `claude-code-action`):**

- niezaufany PR nie może uruchamiać kodu z sekretami repo (ostrożnie z `pull_request_target` i `workflow_run`);
- jednorazowe runnery zamiast trwałych runnerów na własnym serwerze;
- alert rozliczeniowy to nie twardy limit, więc potrzebny jest własny mechanizm przerwania pracy.

**Nowy wątek z wersji 2:** agenci mogą **budować i testować** backend JvP. Nakama działa w Dockerze, więc da się ją uruchomić w sesji Claude Code w chmurze i w GitHub Actions do testów integracyjnych. Nie potrzeba do tego produkcyjnego serwera. Dostęp agentów do **produkcyjnego** serwera z danymi graczy powinien być zablokowany. Wdrożenie wykonuje człowiek albo potok CI zatwierdzony przez Ownera.

**Subskrypcja na serwerze:** oficjalny Claude Code z tokenem subskrypcji na własnym VPS-ie jest według źródeł wtórnych dopuszczalny do pracy na własny użytek. Do obsługi innych osób lub w produkcie potrzebny jest klucz API. Anthropic zmieniał te zasady w 2026 r.

## 3. Projekty

Przejrzane repozytoria (7 listopada 2026):

- `education-games`: gałąź `jvp-notatki-2026-10-30`, wersja 1.2.0;
- `learning_tools`: `main`;
- `educationInfluencer`: `master`, journal 021 i 037–042, `wiki/proposals/`.

Historii innych rozmów z Claude nie widzę z tej sesji. Uwzględniłem to, co z nich trafiło do repozytoriów.

### 3.1. Junk vs Plants: gra przez internet, konta i zakupy

**Dziś:** wszystko lokalnie.

- Zapis tylko w telefonie.
- Do 6 lokalnych kont bez hasła.
- Gra ze znajomym przez Wi-Fi: ENet i wykrywanie przez UDP, jeden telefon jest gospodarzem.
- Wydarzenia liczone od pierwszego uruchomienia.
- Zakupy rubinów tylko jako podgląd.
- Gra jest dla dzieci; plan obejmuje Google Play i App Store.

**Cel (decyzja Ownera z 7.11):** gra przez internet, konta na serwerze, zakupy po zalogowaniu kontem Google.

#### Co jest potrzebne

| Funkcja | Element backendu |
| --- | --- |
| Konto gracza z logowaniem Google (i Apple na iOS) | Uwierzytelnianie, profil, usuwanie konta |
| Postęp, ogród, rubiny na serwerze | Magazyn danych gracza, **portfel po stronie serwera** (inaczej rubiny łatwo podrobić) |
| Zakupy | Google Play Billing w aplikacji, **weryfikacja zakupu na serwerze** (Google Play Developer API), ochrona przed ponownym użyciem paragonu, przywracanie zakupów |
| Gra ze znajomym przez internet | Dobieranie przez kod znajomego, przekazywanie wiadomości między telefonami (relay) albo logika na serwerze |
| Wydarzenia wspólne dla wszystkich | Czas serwera, zdalna konfiguracja wydarzeń |
| Rankingi (opcjonalnie) | Tabele wyników |
| Wersja przeglądarkowa (opcjonalnie) | Godot Web obsługuje tylko renderer **Compatibility**, a JvP używa **Mobile**: trzeba przełączyć renderer i przetestować grafikę. Przeglądarka nie ma UDP ani ENet; transport przez WebSocket lub WebRTC. Plik eksportu i strona gry osobno od APK |
| Budowy Androida i testy w trybie headless | Linux z przypiętą wersją Godota, szablonami eksportu, JDK i Android SDK. Ograniczony dostęp do klucza wydania. Może to być CI albo laboratorium VPS, nie serwer produkcyjny |

Codex zwraca uwagę na rzeczy, których nie da się po prostu „przenieść” na VPS:

- wykrywanie przez rozgłoszenia w sieci lokalnej nie działa przez internet;
- obecny kod JvP nie jest gotowym serwerem dedykowanym, bo jest powiązany z UI;
- dodanie backendu unieważnia deklarację „Data Not Collected” z planu publikacji. Trzeba ją przeanalizować na nowo, a nie zostawić „na zapas”.

#### Opcje techniczne

| Opcja | Co daje | Zalety | Wady | Koszt na start |
| --- | --- | --- | --- | --- |
| **Nakama na własnym VPS-ie (rekomendowana)** | Konta (Google, Apple, urządzenie), dane gracza, portfel, weryfikacja zakupów Google i Apple, mecze w czasie rzeczywistym, rankingi, czas serwera | **Oficjalne SDK dla Godota.** Jedna usługa na wszystkie potrzeby. Otwarty kod (Apache 2.0), dane w Postgresie. Łatwa przesiadka między dostawcami VPS | Administracja po Twojej stronie: aktualizacje, kopie, monitoring, bezpieczeństwo. Wymaga Dockera, TLS i kopii poza serwerem | VPS 4–8 GB RAM: około 20–60 PLN/mies. |
| Nakama w Heroic Cloud (zarządzana) | To samo bez administracji | Brak pracy przy serwerze | Ceny na zapytanie; źródła sugerują poziom setek USD miesięcznie. Za drogo na start | Wysoki |
| Firebase (Auth, Firestore, Functions) | Konta, dane, funkcje do weryfikacji zakupów | Bez serwera, darmowy próg na start | Brak gotowej gry w czasie rzeczywistym dla Godota. Wtyczki Godota tylko od społeczności. **Wysokie uzależnienie** (zamknięte API). Koszty rosną z użyciem | 0 PLN, potem płatność za użycie |
| Supabase (Postgres, Auth, Realtime, Edge Functions) | Konta, dane, kanały w czasie rzeczywistym, funkcje do weryfikacji | Otwarty kod, standardowy Postgres, możliwy własny hosting | Darmowe projekty są wstrzymywane po około tygodniu bez aktywności, więc produkcja wymaga planu Pro (około 25 USD/mies.). Gra i weryfikacja zakupów do napisania samemu | 0 PLN do testów, około 100 PLN/mies. na produkcję |
| W4 Cloud (od twórców Godota) | Backend projektowany dla Godota | Natywna integracja z Godot Multiplayer API | Beta (AGPL); stan i ceny w 2026 niepotwierdzone | Nieznany. Obserwować, nie wybierać |
| Własny serwer Godot (tryb headless) + Supabase | Pełna kontrola | Ten sam kod gry na serwerze | Najwięcej pracy | VPS + ewentualnie Supabase |

**Dlaczego Nakama.** Pokrywa wszystkie cztery wymagania Ownera jedną usługą: konta Google, zakupy z weryfikacją, gra przez internet, dane na serwerze. Ma tryb **„relayed”**, w którym serwer tylko przekazuje wiadomości między telefonami. Pasuje to do obecnej architektury JvP, gdzie jeden telefon jest gospodarzem, więc logiki gry nie trzeba przepisywać na serwer. Lokalną grę przez Wi-Fi warto zostawić jako tryb zapasowy. Nakama komunikuje się w czasie rzeczywistym przez **WebSocket**, więc ten sam backend obsłuży przyszłą wersję przeglądarkową, w której nie ma UDP ani ENet.

**Ekonomia na serwerze, rozgrywka u gospodarza.** Uzupełnienie przeglądu Codexa z 30.10 (w `education-games` sekcja 7, scalona w PR #4):

- rubiny, roślimonety, nagrody i zakupy w portfelu na serwerze;
- czas wydarzeń, ogrodu i limitów dziennych z serwera, bo zegar telefonu łatwo przestawić;
- sama rozgrywka może dalej być prowadzona przez telefon gospodarza.

#### Wymogi regulacyjne (gra dla dzieci)

Te punkty są ważniejsze niż wybór technologii i wymagają potwierdzenia u źródła lub u prawnika.

| Wymóg | Skąd | Konsekwencja projektowa |
| --- | --- | --- |
| **Zgoda rodzica** na przetwarzanie danych dziecka | RODO art. 8. Granica w Polsce to najpewniej 16 lat (rozbieżne źródła; sprawdzić w ustawie lub u UODO). W USA COPPA poniżej 13 lat | Logowanie kontem Google robi **rodzic** (bramka dla rodzica). Dziecko gra na koncie powiązanym przez rodzica. Minimum danych: bez imienia, wieku ani lokalizacji |
| **Usuwanie konta** w aplikacji **i** przez stronę WWW | Zasady danych użytkownika Google Play (od 2024) | Funkcja w grze + strona WWW (statyczna, z formularzem lub adresem e-mail) + wpis w formularzu „Bezpieczeństwo danych” |
| **Brak otwartego czatu z nieznajomymi** | Google Play Families | Tylko gra ze **znajomymi przez kod**, gotowe emotki zamiast czatu tekstowego, bez publicznego dobierania obcych graczy |
| Zakupy z bramką rodzica, bez nakłaniania dzieci | Google Play Families, wytyczne Apple dla kategorii Kids | Ekran zakupu za bramką rodzica (jest już w planie publikacji) |
| **Sign in with Apple** obok Google na iOS | App Store, wytyczna 4.8 | Nakama obsługuje logowanie Apple; trzeba je dodać przed wydaniem na iOS |
| Budowa wersji iOS | Apple (Xcode) | Wymaga macOS: własnego Maca albo Maca w chmurze. Linuksowy VPS go nie zastąpi |
| Zakupy cyfrowe w aplikacji przez Google Play Billing | Zasady płatności Google Play | Opłata Google: według doniesień z czerwca 2026 około 10% opłaty serwisowej + 5% za rozliczenie przez Play Billing na pierwszy 1 mln USD rocznie (do potwierdzenia w Play Console) |
| Polityka prywatności, rejestr przetwarzania danych | RODO, sklepy | Strona statyczna, dokument w repo, umowa powierzenia z dostawcą serwera |
| Dane w UE | RODO (zalecane) | Serwer w centrum danych w UE (Hostinger i Hetzner mają takie lokalizacje) |

#### Ocena przydatności serwera dla JvP

**Wysoka, gdy ruszą prace nad funkcjami online.** Kolejność:

1. Wymogi i projekt bez czatu.
2. Nakama lokalnie w Dockerze (rozwój i testy, także w sesjach agentów).
3. Integracja SDK Godota: konta, portfel, zakupy testowe Play Billing.
4. VPS produkcyjny w UE przed testem zamkniętym w Google Play (12 testerów przez 14 dni).
5. Wydanie.

VPS nie jest potrzebny przed punktem 4.

### 3.2. Nina's Drills (osobna aplikacja na bazie Exam Drill)

**Punkt wyjścia w `learning_tools`:**

- statyczna aplikacja HTML/JS bez zależności (decyzja 0002);
- klient Godot, który importuje zestawy pytań z plików (decyzja 0007);
- bez hostingu i bez kont (decyzja 0006, `out-of-scope/backend-and-account-sync.md`).

Warunek powrotu do kont, „kilku użytkowników”, spełnia się przy produkcie na sprzedaż. W `educationInfluencer` (journal 041) to najmocniejszy kandydat na przychód: angielski, dorośli, płatne zestawy.

**Wymogi startowe niezależne od hostingu:**

- osobne repo (nazwa robocza `nina-drills`) **bez** `ITIL4_sources/` i innych materiałów zewnętrznych;
- zastrzeżenie o znaku ITIL® (PeopleCert);
- pytania wyłącznie autorskie (decyzja 0004);
- przed publikacją sprawdzić, czy nazwa nie koliduje z istniejącymi aplikacjami lub znakami (nie sprawdzałem).

| Kanał sprzedaży | Jak | Backend |
| --- | --- | --- |
| **Web (PWA)** | Strona statyczna (Cloudflare Pages). Zakup zestawu przez Lemon Squeezy (rozlicza VAT) albo Payhip | Bez backendu: zestaw jako plik do pobrania + klucz licencyjny platformy. **Z kontami:** uprawnienie zapisane na koncie |
| **Google Play** | Zestawy jako zakupy w aplikacji przez **Google Play Billing**. Zasady Play wymagają tego dla treści cyfrowych w aplikacji; wyjątki i programy alternatywnych płatności w EOG do sprawdzenia | **Potrzebny:** weryfikacja zakupu i przypisanie zestawu do konta |
| Oba kanały naraz | Kupione w jednym kanale działa w drugim | **Potrzebne wspólne konta i uprawnienia** |

**Wniosek:** jeśli Nina's Drills ma sprzedawać w obu kanałach, potrzebuje tych samych klocków co JvP: konta Google, weryfikacji zakupów, uprawnień, synchronizacji postępu.

Uwagi z raportu Codexa, które przyjmuję:

- **Postęp w przeglądarce jest przypisany do domeny** (origin `localStorage`). Ostateczną domenę wersji webowej trzeba wybrać przed publicznym startem. Zmiana domeny wymaga eksportu i importu postępu, chyba że są już konta z synchronizacją.
- **Pobranego pliku nie da się chronić ukrytym adresem.** Płatne zestawy wymagają autoryzowanego pobrania (klucz licencyjny platformy albo konto).
- **Dodanie hostingu nie dodaje klienta API.** Obecna aplikacja Godot ma `permissions/internet=false`. Konta i synchronizacja to nowa praca: uprawnienia, model danych, obsługa błędów i trybu offline.
- **Nie publikować całego repo `learning_tools` jako strony.** Zawiera surowe materiały. Publiczny artefakt wybiera się osobno.

| Wariant | Opis | Za | Przeciw |
| --- | --- | --- | --- |
| **Wspólna Nakama dla obu aplikacji (rekomendowany na start)** | Jedna instancja, osobne „projekty” danych; zestawy jako produkty z weryfikacją zakupów | Jeden serwer, jedna administracja, ten sam kod kont i zakupów; klient Godot Nina's Drills dzieli SDK z JvP | Nakama jest „growa”; dla wersji webowej trzeba klienta JavaScript (Nakama go ma) |
| Supabase dla Nina's Drills, Nakama dla JvP | Dwa backendy | Supabase wygodniejszy dla zwykłej aplikacji webowej | Dwa systemy do utrzymania |
| Na start bez kont | Web: plik + licencja. Play: zakupy w aplikacji bez synchronizacji | Najszybciej na rynek | Kupione na stronie nie działa w aplikacji z Play i odwrotnie; ręczne przenoszenie postępu |

**Ocena przydatności serwera:** **umiarkowana.** Wersja 1 może działać bez backendu. Wspólne konta pojawią się razem z backendem JvP prawie bez kosztu dodatkowego.

### 3.3. Influencer-AI i JvP: strona, blog, sklep cyfrowy i merch

**Stan** (journal 037, 040, 041; `wiki/proposals/monetisation-and-community.md`):

- teraz, za 0 PLN: strona źródeł, quiz Quilla, e-mail, Ko-fi;
- produkty od około 1000+ zaangażowanych obserwujących;
- domena, produkty i KDP to decyzja po 8-tygodniowym teście;
- konta i wydatki zatwierdza Owner.

**Dwie marki, dwa sklepy.** Postacie Influencer-AI kierują treści do dorosłych i nastolatków, a JvP jest dla dzieci. Merch JvP sprzedaje się **rodzicom**. Nie łączyć tego w jednym sklepie ani w treściach dla dzieci (journal 040, punkt 8).

| Tor | Na start (bez serwera) | Później (przy skali) | Rola Hostingera |
| --- | --- | --- | --- |
| **Produkty cyfrowe** (planery Niny, karty z faktami, e-booki, zestawy pytań) | Lemon Squeezy (rozlicza VAT za sprzedawcę, około 5% + 0,50 USD) albo Payhip lub Ko-fi Shop (VAT po Twojej stronie). E-booki: Amazon KDP | Ta sama platforma; ewentualnie własny sklep | Brak |
| **Merch** (koszulki, kubki, naklejki z postaciami i z JvP) | Printful lub Printify zintegrowane z **Etsy** (ruch z marketplace, bez abonamentu) albo z **Shopify** (około 30–40 USD/mies., niezweryfikowane) | Własny sklep na Shopify albo **WooCommerce** z wtyczką Printful | **Opcja:** WooCommerce na hostingu Business lub Cloud. Taniej w abonamencie, ale aktualizacje, bezpieczeństwo, RODO i VAT (procedura OSS) są po Twojej stronie |
| **Strona marki i blog** | Strona statyczna (Astro lub Hugo; agenci piszą wpisy przez PR) na Cloudflare Pages | Ghost(Pro) albo WordPress | **Opcja:** WordPress na hostingu, jeśli wybierzesz WordPress |
| **Polityka prywatności i usuwanie konta JvP** | Podstrony statyczne na domenie projektu (Cloudflare Pages) | — | Brak |
| **Pliki APK do pobrania** | Google Play; testowe wersje przez wydania na GitHubie albo magazyn obiektowy (np. Cloudflare R2) | — | Opcja: VPS z HTTPS i sumami kontrolnymi |

**Gdzie hostować strony.** TASK-0038 zakłada GitHub Pages. Regulamin GitHub Pages wyklucza jednak strony służące głównie biznesowi, sprzedaży albo SaaS. Strona źródeł będzie linkować Ko-fi, produkty i aplikacje, więc bezpieczniej od razu użyć **Cloudflare Pages** dla wszystkich stron projektów. Ograniczenie Cloudflare Pages to 25 MiB na plik, dlatego APK (26,6 MB i 57,7 MB) trzymać osobno. Publikować tylko wygenerowane, zatwierdzone treści, nigdy prywatnej wiki ani roboczych materiałów.

**Rekomendacja dla sklepu:** zacząć od platform, czyli Lemon Squeezy dla cyfrowych oraz Etsy + Printful dla merchu.

- Zero administracji i płatności tylko od sprzedaży.
- Rozliczanie VAT w dużej mierze po stronie platformy.

Własny sklep (Shopify albo WooCommerce na Hostingerze) ma sens dopiero, gdy prowizje zaczną przewyższać koszt i pracę własnego sklepu. Sprzedaż oznacza też wybór formy działalności i rozliczeń podatkowych w Polsce; to decyzja Ownera z księgową (już odnotowane w wiki).

**Ocena przydatności Hostingera dla sklepu i bloga:** **niska na start, umiarkowana przy skali** (WooCommerce, WordPress).

### 3.4. Pozostałe repozytoria

- `klasa6` i `FOZ-ZOE`: Dysk Google i druk, bez hostingu.
- `doktorat_git` i repozytoria szkoleniowe: nieaktywne.
- `AI-agents`: standard skilli.

### Podsumowanie przydatności serwera

| Projekt | Teraz | Za 6–12 miesięcy | Co zamiast VPS-a na start |
| --- | --- | --- | --- |
| **JvP** | Niska (projekt i wymogi) | **Wysoka** (Nakama: konta, zakupy, gra przez internet) | Nakama lokalnie w Dockerze do rozwoju |
| **Nina's Drills** | Niska | Umiarkowana (wspólne konta z JvP) | Strona statyczna + Lemon Squeezy; Play Billing |
| **Influencer-AI: sklep i blog** | Niska | Umiarkowana (WooCommerce przy skali) | Lemon Squeezy, Etsy + Printful, strona statyczna |
| **AI-crew** | Niska | Niska do umiarkowanej (osobny runner) | Chmura Claude Code, GitHub Actions, recenzja Codexem |

## 4. Wybór dostawcy serwera dla backendu gier

Backend gier z danymi i płatnościami graczy powinien mieć **własny serwer**. Na nim tylko Nakama i baza, bez agentów AI i bez sklepu.

| Kryterium | Hostinger VPS KVM 2 | Hetzner Cloud (mały serwer) |
| --- | --- | --- |
| Parametry | 2 vCPU, 8 GB RAM, 100 GB NVMe | Około 2 vCPU, 4–8 GB RAM, zależnie od planu |
| Cena | Około 7–9 USD/mies. przy przedpłacie 24 mies., **około 15 USD/mies. po odnowieniu** | Około 4,5–10 EUR/mies. + VAT, rozliczenie miesięczne (po podwyżkach z 2026; linie CPX zdrożały ponad 2×) |
| Zobowiązanie | Niska cena tylko przy długiej przedpłacie | Brak; rezygnacja w każdej chwili |
| Lokalizacja w UE | Tak | Tak (Niemcy, Finlandia) |
| Łatwość | Panel hPanel, Docker Manager, asystent AI | Panel bardziej techniczny |
| Kopie zapasowe | Tygodniowe, według recenzji tylko 2 ostatnie; częstsze płatne | Kopie i migawki płatne jako dodatek |
| Wsparcie | Czat 24/7 | Zgłoszenia |
| Przesiadka | Niski koszt techniczny (Docker + zrzut Postgresa); wysoki finansowy, jeśli przedpłacono lata | Niski |

**Rekomendacja:** oba się nadają.

- **Hostinger KVM 2:** jeśli cenisz prostszy panel i wsparcie na czacie, a decyzja o grze online jest już pewna. Wtedy przedpłata 24 miesięcy się opłaca.
- **Hetzner:** jeśli chcesz zachować swobodę przez pierwsze miesiące testów.

Przy obu: konfiguracja w gicie (`docker-compose.yml` z Nakamą i Postgresem, proxy TLS, skrypt kopii) i kopie bazy codziennie **poza** dostawcą (np. tani magazyn obiektowy w innej firmie).

**Przed zakupem** (lista z raportu Codexa) zebrać konkretną wycenę:

- cena brutto za cały okres, płatność z góry, cena odnowienia;
- kopie zapasowe i ich retencja, migawki, dodatkowe IP i dyski, transfer;
- zasady rezygnacji i zwrotu;
- region danych i umowa powierzenia;
- zakres wsparcia.

Ochrona DDoS i migawka u dostawcy nie zastępują kopii u innej firmy.

**Adres API pod własną domeną** (np. `api.<domena projektu>`). Zmiana dostawcy nie wymaga wtedy aktualizacji aplikacji w sklepach.

**Cel odtwarzania danych** (propozycja Codexa, do przyjęcia):

- utrata najwyżej 24 h zwykłych danych;
- odtworzenie w ciągu 4 h;
- dla zakupów dziennik zdarzeń i ostrzejsze zasady.

## 5. Koszt łączny dla 24 miesięcy (orientacyjnie)

| Pozycja | Scenariusz „platformy + Nakama” (rekomendowany) | Scenariusz „wszystko na swoim” |
| --- | --- | --- |
| Domena (niezależny rejestrator) | Około 80–160 PLN | Około 80–160 PLN |
| Strony statyczne (Cloudflare Pages) | 0 PLN | — |
| Backend gier: Nakama na VPS (Hostinger KVM 2 lub Hetzner) | Około 550–900 PLN za 2 lata, zależnie od dostawcy i przedpłaty | Ten sam |
| Kopie poza dostawcą | Około 50–150 PLN | Około 50–150 PLN |
| Sklep cyfrowy | 0 PLN stałych + około 5% + 0,50 USD od sprzedaży (Lemon Squeezy) | — |
| Merch | 0 PLN stałych (Etsy + Printful: opłaty od wystawienia i sprzedaży) | — |
| Sklep WooCommerce na Hostingerze (Business) | — | Około 750–800 PLN z góry za 4 lata, potem około 450–800 PLN rocznie, plus wtyczki, płatności i księgowość VAT |
| Google Play (konto dewelopera) | Jednorazowo około 100 PLN (25 USD) | To samo |
| Apple Developer (przy wersji iOS) | Około 400 PLN rocznie (99 USD) | To samo |
| Opłaty sklepów od zakupów w aplikacjach | Około 15% przy Play Billing (według doniesień z 2026) | To samo |
| **Razem stałe koszty infrastruktury przez 24 mies.** | **Około 700–1300 PLN** (bez Apple) | **Około 1500–2500 PLN** (bez Apple) + więcej administracji |

Nie wliczono subskrypcji Claude i ChatGPT, kredytów Higgsfield (około 295 PLN/mies.) ani księgowości. Kurs orientacyjny: 1 USD ≈ 3,8–4,0 PLN, 1 EUR ≈ 4,3 PLN.

### Czas Ownera: największa pozycja (metoda Codexa)

Codex liczy koszt całkowity razem z wycenionym czasem (100 zł/h, założenie porównawcze). W tej wersji przyjmuję jego metodę:

| Pozycja | Godziny | Wycena przez 24 mies. |
| --- | --- | --- |
| Administracja backendu gier: aktualizacje, kopie, monitoring, test odtworzenia | 2–4 h/mies. | **4800–9600 zł** |
| Pierwsze uruchomienie serwera produkcyjnego (bez programowania funkcji online) | 8–16 h jednorazowo | 800–1600 zł |
| Strony statyczne i domena | 2–4 h jednorazowo, potem około 0,5 h/mies. | 1400–1600 zł |

**Wniosek:** gotówka za infrastrukturę to około 700–1300 PLN, a czas administracji jest kilkukrotnie droższy. Dlatego:

- przy JvP online liczy się **mało ruchomych części** (jedna usługa Nakama zamiast kilku);
- zautomatyzowane kopie i aktualizacje;
- zarządzana usługa może się opłacić, jeśli zaoszczędzi więcej godzin, niż kosztuje.

Dla porównania, scenariusze Codexa (z jego budżetami AI i czasem) dają przez 24 miesiące:

- około 1900–2100 zł: same strony statyczne;
- około 14 600 zł: laboratorium crew na VPS-ie;
- około 29 200 zł: crew oddzielony od produkcji z API, bazą i mediami.

Są to budżety, nie cenniki, i nie obejmują budowy funkcji aplikacji.

**Przedpłata (przykład Codexa):** 48 miesięcy × 30 zł = 1440 zł z góry. Rezygnacja po 12 miesiącach zostawia 1080 zł niewykorzystanej przedpłaty, jeśli umowa nie przewiduje zwrotu. Oszczędność 40 zł/mies. na serwerze znika, jeśli przesiadka zajmie 8 h (zwrot po 20 miesiącach).

## 6. Uzależnienie i koszt przesiadki

| Element | Powiązanie | Koszt przesiadki | Jak go obniżyć |
| --- | --- | --- | --- |
| **Konta graczy (identyfikatory Google i Apple)** | **Wysokie, jeśli projekt Google Cloud lub klucze Apple należą do dostawcy albo do prywatnego konta** | Utrata możliwości logowania istniejących graczy | Projekt Google Cloud (OAuth, Play Developer API) i konto Apple Developer na **koncie projektu**, niezależnie od hostingu |
| Nakama na VPS | Niskie | Pół dnia do dnia: nowy serwer, odtworzenie z gita, przywrócenie Postgresa, zmiana DNS | Konfiguracja w gicie, codzienne kopie poza dostawcą, test odtworzenia co kwartał |
| Firebase, gdyby go wybrać | **Wysokie** | Przepisanie warstwy danych i kont (tygodnie) | Dlatego nie jest rekomendowany dla JvP |
| Supabase | Średnie | Dni (Postgres przenośny, ale Auth i Edge Functions trzeba odtworzyć) | — |
| Przedpłata w Hostingerze | Wysokie (finansowe) | Niewykorzystana część zwykle przepada po 30 dniach | Przedpłata dopiero, gdy gra online jest pewna; wcześniej krótszy okres lub Hetzner |
| Podwyżka przy odnowieniu | Wysokie | Około 2× wyższa cena albo przenosiny | Zapisać datę odnowienia, przegląd ofert 2 miesiące wcześniej |
| Domena kupiona u dostawcy hostingu | Średnie | Blokada transferu zwykle 60 dni, opłata za rok | Domena u niezależnego rejestratora, DNS osobno |
| Sklep na Etsy lub Shopify | Średnie | Eksport produktów i klientów; recenzje i ruch z Etsy nie przechodzą | Lista klientów (e-mail) na własnej liście mailingowej |
| WooCommerce na Hostingerze | Średnie | 1–3 dni, przerwa w sprzedaży | Kopie poza dostawcą |
| Kreatory Website Builder i Horizons | **Wysokie** | Przebudowa od zera | Nie używać |
| Zakupy w Google Play i App Store | Wysokie (z natury sklepów) | Brak przeniesienia zakupów między sklepami | Uprawnienia zapisane na koncie gracza w Nakamie, nie tylko w sklepie |
| Postęp w przeglądarce (Nina's Drills, wersja webowa) | Średnie | Zmiana domeny gubi postęp zapisany lokalnie | Ostateczna domena przed startem; eksport i import postępu albo konta |
| Subskrypcje płatne | Wysokie | Tokeny kart i zgody na płatności cykliczne zwykle nie przechodzą przez eksport CSV | Na start bez własnych subskrypcji; korzystać z platform |

### Nakład pracy przy przesiadce (szacunki Codexa, przy 100 zł/h)

| Co przenosimy | Nakład | Łącznie z gotówką na okres przejściowy |
| --- | --- | --- |
| Strona statyczna z własną domeną | 2–6 h | 200–650 zł |
| VPS z kontenerami i PostgreSQL (np. Nakama) | 8–20 h | 900–2300 zł |
| WordPress lub WooCommerce między hostami | 12–40 h | 1400–4600 zł |
| Backend na funkcjach platformy (Auth, Storage, funkcje) | 20–60 h | 2200–6800 zł |
| Sklep lub kreator silnie związany z platformą | 60–160 h | 6500–18 000 zł |
| Herdr zastąpiony przez tmux, usługi systemd lub CI | 4–12 h | 400–1300 zł |
| Pamięć Hermesa przeniesiona do innego narzędzia | 8–24 h | 800–2600 zł |

Wiersze to różne zakresy; nie należy ich sumować. Dla JvP z Nakamą dochodzi jedna pozycja spoza tabeli: projekt Google Cloud i konto Apple muszą zostać przy Ownerze (pierwszy wiersz tabeli wyżej). Bez tego przesiadka oznacza utratę logowania graczy.

### Ryzyka do monitorowania

1. **Dane dzieci i zgoda rodzica.** Najwyższe ryzyko prawne. Potrzebny przegląd prawny przed wydaniem funkcji online.
2. **Bezpieczeństwo serwera z płatnościami.** Klucz konta usługi Google musi być dostępny tylko dla Nakamy. Potrzebne aktualizacje, firewall i monitoring.
3. **Jedna osoba jako administrator.** Awaria serwera wyłącza logowanie i zakupy. Potrzebny prosty plan awaryjny: gra działa offline, a zakupy synchronizują się później.
4. **Zmiany opłat i zasad sklepów.** Google zmieniało opłaty w czerwcu 2026.
5. **Zmiany cen dostawców.** Przenośna konfiguracja chroni przed tym najlepiej.
6. **Tokeny subskrypcji AI na serwerze.** Agenci nie powinni mieć dostępu do produkcji gry.

## 7. Plan działania

| Kiedy | Krok | Projekt |
| --- | --- | --- |
| Teraz | Kupić domenę projektu u niezależnego rejestratora; założyć projekt Google Cloud i konto Play Console na koncie projektu | wszystkie |
| Teraz | Strona statyczna na Cloudflare Pages: polityka prywatności JvP, strona usuwania konta, strona źródeł (TASK-0038) | JvP, Influencer-AI |
| Teraz | Specyfikacja „JvP online”: zakres (znajomi przez kod, bez czatu), bramka rodzica, dane minimalne, usuwanie konta; wymogi prawne do potwierdzenia | JvP |
| Teraz | Pilotaż recenzji krzyżowej Codexem na 5–10 PR-ach; potem pomiar na około 20 zadaniach (sekcja 2) | AI-crew |
| Teraz | Scalić `jvp-notatki-2026-10-30` (wersja 1.2.0) z `master`; dodać testy regresji i CI (przegląd JvP, sekcja 7.4) | JvP |
| Przed zakupem serwera | Konkretna wycena: brutto za cały okres, odnowienie, kopie, zwroty, region, umowa powierzenia (sekcja 4) | JvP |
| Następnie | Nakama w Dockerze lokalnie i w CI; SDK Godota; konta, portfel, zakupy testowe Play Billing; gra przez relay obok lokalnego Wi-Fi | JvP |
| Następnie | Osobne repo `nina-drills`; wersja webowa i sprzedaż zestawów przez Lemon Squeezy | Nina's Drills |
| Przed testem zamkniętym JvP | VPS produkcyjny w UE (Hostinger KVM 2 albo Hetzner), kopie poza dostawcą, monitoring | JvP |
| Po teście 8-tygodniowym Influencer-AI | Lemon Squeezy dla produktów cyfrowych; Etsy + Printful dla merchu (osobno marka JvP dla rodziców) | Influencer-AI, JvP |
| Później | Wspólne konta i uprawnienia Nina's Drills w Nakamie | Nina's Drills |
| Przy skali sklepu | Porównanie: Shopify vs WooCommerce na Hostingerze | Influencer-AI |

### Otwarte pytania do Ownera

1. **JvP online:** dobieranie tylko znajomych przez kod (zalecane dla dzieci) czy także obcych graczy?
2. **Konto w JvP:** wymagane czy opcjonalne? Rekomendacja: opcjonalne, zakładane przez rodzica; bez konta gra działa offline jak dziś.
3. **Wersja iOS:** w tym samym czasie co online, czy później? Od tego zależy Sign in with Apple i koszt konta Apple.
4. **Nina's Drills:** od razu oba kanały (web i Google Play), czy najpierw tylko web?
5. **Forma sprzedaży:** czy istnieje już działalność gospodarcza, czy sprzedaż ruszy w innej formie? To wpływa na wybór platform (VAT, faktury).
6. **Wersja przeglądarkowa JvP:** czy jest w planach? Wymaga zmiany renderera na Compatibility i testów grafiki.

## 8. Weryfikacja raportu Codexa

**Zakres:**

- commit `48d8031` (raport `outputs/2026-11-07-codex-ai-crew-hosting-i-migracja.md` i jeden wiersz w `outputs/README.md`);
- scalenie `00b7842` (gałąź robocza Codexa `work` z moją gałęzią).

**Integralność:** scalenie jest poprawne. Konflikt wystąpił tylko w `outputs/README.md` i zachowano oba wpisy. Raport Codexa nie zmienia żadnego innego pliku.

| Twierdzenie Codexa | Sprawdzenie | Wynik |
| --- | --- | --- |
| Herdr: po restarcie maszyny procesy nie przetrwają | README `herdrdev/herdr` @ `ee5bfb5` | **Potwierdzone** („the original processes do not survive”) |
| `herdr-core` ma CLI `hc`, działa z prawami konta, nie jest piaskownicą | README i `docs/security.md` `herdrdev/herdr-core` @ `9ce385d` | **Potwierdzone** |
| Hermes: reguły wewnątrz procesu nie zastępują izolacji systemowej | `SECURITY.md` `NousResearch/hermes-agent` @ `9ffa7df` | **Potwierdzone** (sekcja „OS-Level Isolation”) |
| GitHub Pages nie służy do biznesu, sprzedaży ani SaaS | `github/docs` @ `8cd1075`, `github-pages-limits.md` | **Potwierdzone** |
| Cloudflare Pages: limit 25 MiB na plik | `cloudflare-docs` @ `53ce9b5`, `pages/platform/limits.mdx` | **Potwierdzone** |
| Rozmiary APK: Exam Drill 1.6 = 26 613 508 B, JvP 1.2.0 = 57 705 396 B | `git ls-tree -l` w obu repozytoriach | **Potwierdzone** |
| Godot Web: tylko Compatibility; brak UDP i ENet, dostępne WebSocket i WebRTC | `godot-docs` @ `0709b93`, `exporting_for_web.rst` | **Potwierdzone** |
| JvP: renderer Mobile, protokół sieci 7, ENet i UDP | `project.godot`, `net_session.gd` @ `87655b7` | **Potwierdzone** |
| Exam Drill APK bez dostępu do internetu | `godot/export_presets.cfg`: `permissions/internet=false` | **Potwierdzone** |
| `work/NEXT-PC-SESSION.md` na gałęzi `ccr-d914ae0e-4gvx4c` | `git ls-tree` | **Potwierdzone** |
| Ceny Cloudflare Workers Paid (5 USD/mies.) i R2 (0,015 USD/GB) | Nie sprawdzałem ponownie | Przyjęte za Codexem |
| JvP: lokalna gra przez Wi-Fi jako punkt startu; online „potencjalnie” | — | **Nieaktualne:** Codex pisał przed decyzją Ownera o grze online |
| Ceny Hostinger i Hetzner niepotwierdzone handlowo | — | Zgodne z moim stanem: strony ofert były zablokowane w obu sesjach |

**Ocena:** raport Codexa jest rzetelny, ostrożny w twierdzeniach i dobrze udokumentowany przypiętymi źródłami. Nie znalazłem w nim błędu merytorycznego. Jego wkład przejąłem w tej wersji (lista na początku). Nie zmieniałem treści raportu Codexa.

## Źródła

- Raport wejściowy: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md)
- [Analiza Codexa z 7.11.2026](2026-11-07-codex-ai-crew-hosting-i-migracja.md) (commit `48d8031`) i jej źródła pierwotne sprawdzone w tej sesji:
  - [Herdr README](https://github.com/herdrdev/herdr/blob/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde/README.md);
  - [herdr-core security](https://github.com/herdrdev/herdr-core/blob/9ce385d9c8abb041dd4437476d770365b3fb5282/docs/security.md);
  - [Hermes SECURITY](https://github.com/NousResearch/hermes-agent/blob/9ffa7dff23726d8daa8b3e167b20a5fabc2e04ef/SECURITY.md);
  - [GitHub Pages limits](https://github.com/github/docs/blob/8cd1075179df75319912891d6620c9cb78eefb4d/content/pages/getting-started-with-github-pages/github-pages-limits.md);
  - [Cloudflare Pages limits](https://github.com/cloudflare/cloudflare-docs/blob/53ce9b502646fdc019b8184b29b9f1054939e1b6/src/content/docs/pages/platform/limits.mdx);
  - [Godot: eksport na Web](https://github.com/godotengine/godot-docs/blob/0709b93758c40d26c91e1d9e4f3afd262c4ed386/tutorials/export/exporting_for_web.rst).
- Przegląd JvP z 30.10 z aktualizacją z 7.11: `education-games/review/2026-10-30_przeglad-repo_ChatGPT-Codex.md` (PR #4)
- Repozytoria JeanPaulSzefler (stan z 7.11.2026): `education-games` (`junk-vs-plants/README.md`, `PLAN_PUBLIKACJI.md`, przegląd Codexa z 30.10), `learning_tools` (`CLAUDE.md`, decyzje 0002, 0004, 0006, 0007, `out-of-scope/backend-and-account-sync.md`), `educationInfluencer` (journal 021, 037, 040, 041; `wiki/proposals/monetisation-and-community.md`, `own-apps-for-personas.md`, `financial-scenarios.md`; TASK-0037, TASK-0038)
- [Raport AI-crew z 31.10.2026](2026-10-31-efficient-ai-crew-and-repo-setup.md)
- Herdr: [Bitdoze](https://www.bitdoze.com/herdr-agent-multiplexer/), [AI Weekly](https://aiweekly.co/alerts/herdr-adds-agent-state-awareness-to-terminal-multiplexing), [knightli](https://knightli.com/en/2026/07/06/herdr-terminal-agent-multiplexer/)
- Hermes Agent: [hermes-agent.org](https://hermes-agent.org/) (możliwie nieoficjalna; źródło pierwotne: repo `NousResearch/hermes-agent`)
- Nakama: [weryfikacja zakupów Google](https://heroiclabs.com/docs/nakama/concepts/iap-validation/google/), [Heroic Cloud](https://heroiclabs.com/heroic-cloud/), [porównanie Nakama self-host vs managed](https://gsb.supercraft.host/blog/nakama-open-source-vs-managed-backend/)
- W4 Cloud: [ogłoszenie 2024](https://w4games.com/2024/03/05/w4-cloud-is-here-the-new-multiplayer-infrastructure-for-godot-games), [porównanie backendów Godot 2026](https://crux.supercraft.host/blog/best-godot-backend-2026/)
- Supabase: [wstrzymywanie darmowych projektów](https://supabase.com/docs/guides/platform/free-project-pausing), [przegląd cen 2026](https://www.jetadmin.io/blog/supabase-pricing-2026-guide-to-plans-limits-and-real-world-costs/)
- Google Play: [usuwanie konta](https://support.google.com/googleplay/android-developer/answer/13327111), [zasady Families](https://support.google.com/googleplay/android-developer/answer/9893335), [opłaty od 30.06.2026 (9to5Google)](https://9to5google.com/2026/06/24/google-play-store-external-billing-june-30/), [RevenueCat, alternatywne płatności](https://www.revenuecat.com/guides/google-play-billing/alternative-billing-and-external-offers)
- Apple 4.8: [forum Apple Developer](https://developer.apple.com/forums/thread/765145), [ptkd.com, odrzucenia 4.8](https://ptkd.com/journal/app-store-rejection-4-8-sign-in-with-apple)
- RODO art. 8: [tekst artykułu](https://gdpr-text.com/pl/read/article-8/), [Infor](https://www.infor.pl/prawo/dziecko-i-prawo/nieletni-i-prawo/782695,Zgoda-dziecka-na-przetwarzanie-danych-osobowych-RODO-2018.html)
- Hostinger: [HostAdvice, ceny VPS z odnowieniem](https://hostadvice.com/hosting-company/hostinger-reviews/vps-pricing/), [Findstack, KVM 1 vs 2 vs 4](https://findstack.com/resources/hostinger-vps-for-ai-agents), [learnwithhasan, kopie](https://learnwithhasan.com/self-hosting-hub/vps-providers/hostinger-vps/), [Website Builder Expert, hosting 2026](https://www.websitebuilderexpert.com/web-hosting/hostinger-pricing/)
- Hetzner 2026: [Tom's Hardware](https://www.tomshardware.com/tech-industry/hetzner-to-raise-prices-by-up-to-37-percent-from-april-1), [Northflank](https://northflank.com/blog/hetzner-cloud-server-price-increases)
- Platformy sprzedaży: [We Are Founders](https://www.wearefounders.uk/best-platforms-for-selling-digital-products-in-2026/)
- Claude Code na VPS: [Autonomee](https://autonomee.ai/blog/claude-code-server-vps-authentication-guide/) (źródło wtórne; obowiązują aktualne warunki Anthropic)

Ograniczenia: strona hostinger.com była zablokowana w tej sesji (u Codexa strony ofert Hostinger, Hetzner i Render również); ceny pochodzą ze źródeł wtórnych. Dokumentację Herdr, Hermesa, GitHub Pages, Cloudflare i Godota sprawdziłem pod przypiętymi wersjami przez raw.githubusercontent.com. Wymogi prawne (wiek zgody w Polsce, Families, opłaty Google, wytyczna 4.8, VAT) są streszczone ze źródeł wtórnych i wymagają potwierdzenia u źródła lub u prawnika przed wydaniem.
