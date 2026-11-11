# Orkiestracja agentów (Herdr) i hosting (Hostinger): analiza dla AI-crew, gry JvP, aplikacji quizowej i projektu treściowego

7 listopada 2026, uzupełnione 8 listopada · **Wersja 3.1 (robocza)** · Punkty odniesienia: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md) oraz [analiza Codexa z 7.11](2026-11-07-codex-ai-crew-hosting-i-migracja.md)

> Zanonimizowano 11.11.2026: nazwy i szczegóły prywatnych projektów zastąpiono opisem typu projektu.

## Co się zmieniło

### Wersja 3.1 (8 listopada): rozdział o no1.pl

Nowy [rozdział 9](#9-oferta-no1pl-analiza-etapy-i-alternatywy) zawiera:

- analizę oferty no1.pl na podstawie strony, publicznego cennika (API panelu) i regulaminu;
- które usługi i na jakim etapie projektów mają sens;
- co przydaje się na start;
- porównanie z alternatywami.

Pozostałe rozdziały bez zmian. Nazwa pliku pozostaje `-v3`, żeby nie zepsuć odnośników z innych repozytoriów.

### Wersja 3: po weryfikacji raportu Codexa

Codex przygotował równoległą analizę (commit `48d8031`, scalona z tą gałęzią w `00b7842`). Napisał ją **przed** odpowiedziami Ownera, więc zakłada JvP tylko z lokalną grą przez Wi-Fi. Jej twierdzenia sprawdziłem w kodzie i w dokumentacji pod przypiętymi wersjami (sekcja 8). Wersja 3 przejmuje z niej to, czego brakowało w wersji 2:

1. **GitHub Pages nie nadaje się do stron komercyjnych.** Regulamin wyklucza biznes, sklep i SaaS. Polityka prywatności płatnej gry, sklep i aplikacja quizowa idą na Cloudflare Pages (sekcje 3.3 i 7).
2. **Pliki APK nie zmieszczą się na Cloudflare Pages.** Limit to 25 MiB na plik, a aplikacja quizowa ma 26,6 MB, JvP 1.2.0 ma 57,7 MB. APK dystrybuować przez Google Play, wydania na GitHubie albo magazyn obiektowy.
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
| Nowa aplikacja quizowa na bazie istniejącej? | **Tak**: osobna aplikacja | Osobne repo; sprzedaż zestawów w dwóch kanałach (web i Google Play) wymaga wspólnych kont i uprawnień (sekcja 3.2) |
| Sklep: cyfrowy czy merch? | **Jedno i drugie** | Dwa tory sprzedaży i dwie marki: postacie projektu treściowego (dorośli) i JvP (rodzice) (sekcja 3.3) |
| Usługi u Hostingera? | **Brak** | Brak kosztów utopionych; wybór dostawcy jest w pełni otwarty |

## W skrócie

1. **Serwer jest teraz uzasadniony, ale dla gry, nie dla agentów.** Gra przez internet, konta i zakupy w JvP wymagają backendu. Rekomenduję **Nakamę**: otwartoźródłowy serwer gier z oficjalnym SDK dla Godota, logowaniem przez Google i Apple, grą w czasie rzeczywistym i weryfikacją zakupów z Google Play i App Store. Nakama działa w Dockerze z bazą Postgres **na małym VPS-ie**.
   - Hostinger KVM 2 dobrze się do tego nadaje. Hetzner jest równorzędną alternatywą z płatnością miesięczną.
   - Uzależnienie jest niskie, bo kod jest otwarty, a dane to zwykły Postgres.
2. **Jeden backend kont dla JvP i aplikacji quizowej.** Aplikacja quizowa będzie sprzedawać zestawy pytań na stronie i w Google Play. Wspólny mechanizm kont i uprawnień (co kto kupił) oszczędza pracę. Nakama to obsługuje; Supabase jest alternatywą bardziej „aplikacyjną”.
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
8. **no1.pl: nie na start; kandydat na etap sprzedaży w projekcie treściowym i ewentualnie na zarządzany serwer gry** (rozdział 9).
   - To polski operator z opieką człowieka, pocztą firmową i umową powierzenia.
   - Za moc obliczeniową jest 3–6× droższy od Hetznera lub Hostingera i nie rejestruje `.com`.
   - Ma sens dla WordPressa lub WooCommerce z pocztą i opieką (około 1570 zł/rok). Dla serwera Nakamy tylko w wariancie zarządzanym, jeśli wycena obejmie Dockera i kopie.

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
| **A. Recenzja krzyżowa** | Codex (GPT) jako drugi recenzent PR-ów pisanych przez Claude'a. Formalizuje to, co już robisz ręcznie w innych projektach | GitHub Actions albo ręcznie | Od razu |
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

- publiczne `education-games`: gałąź `jvp-notatki-2026-10-30`, wersja 1.2.0;
- dwa prywatne projekty: istniejąca aplikacja quizowa i projekt treściowy. Ich szczegóły pominięto.

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

**Ekonomia na serwerze, rozgrywka u gospodarza:**

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

### 3.2. Nowa aplikacja quizowa (osobna aplikacja na bazie istniejącej)

**Punkt wyjścia (istniejąca aplikacja, projekt prywatny):**

- statyczna aplikacja HTML/JS bez zależności;
- klient Godot, który importuje zestawy pytań z plików;
- świadomie bez hostingu i bez kont.

Konta stają się potrzebne dopiero przy produkcie na sprzedaż dla wielu użytkowników. W planach to najmocniejszy kandydat na przychód: angielski, dorośli, płatne zestawy.

**Wymogi startowe niezależne od hostingu:**

- osobne repo **bez** surowych materiałów zewnętrznych;
- sprawdzenie praw do cudzych znaków towarowych i treści, zanim zestawy trafią do sprzedaży;
- pytania wyłącznie autorskie;
- przed publikacją sprawdzić, czy nazwa nie koliduje z istniejącymi aplikacjami lub znakami (nie sprawdzałem).

| Kanał sprzedaży | Jak | Backend |
| --- | --- | --- |
| **Web (PWA)** | Strona statyczna (Cloudflare Pages). Zakup zestawu przez Lemon Squeezy (rozlicza VAT) albo Payhip | Bez backendu: zestaw jako plik do pobrania + klucz licencyjny platformy. **Z kontami:** uprawnienie zapisane na koncie |
| **Google Play** | Zestawy jako zakupy w aplikacji przez **Google Play Billing**. Zasady Play wymagają tego dla treści cyfrowych w aplikacji; wyjątki i programy alternatywnych płatności w EOG do sprawdzenia | **Potrzebny:** weryfikacja zakupu i przypisanie zestawu do konta |
| Oba kanały naraz | Kupione w jednym kanale działa w drugim | **Potrzebne wspólne konta i uprawnienia** |

**Wniosek:** jeśli aplikacja quizowa ma sprzedawać w obu kanałach, potrzebuje tych samych klocków co JvP: konta Google, weryfikacji zakupów, uprawnień, synchronizacji postępu.

Uwagi z raportu Codexa, które przyjmuję:

- **Postęp w przeglądarce jest przypisany do domeny** (origin `localStorage`). Ostateczną domenę wersji webowej trzeba wybrać przed publicznym startem. Zmiana domeny wymaga eksportu i importu postępu, chyba że są już konta z synchronizacją.
- **Pobranego pliku nie da się chronić ukrytym adresem.** Płatne zestawy wymagają autoryzowanego pobrania (klucz licencyjny platformy albo konto).
- **Dodanie hostingu nie dodaje klienta API.** Obecna aplikacja mobilna nie ma dostępu do internetu. Konta i synchronizacja to nowa praca: uprawnienia, model danych, obsługa błędów i trybu offline.
- **Nie publikować całego repo istniejącej aplikacji jako strony.** Publiczny artefakt wybiera się osobno.

| Wariant | Opis | Za | Przeciw |
| --- | --- | --- | --- |
| **Wspólna Nakama dla obu aplikacji (rekomendowany na start)** | Jedna instancja, osobne „projekty” danych; zestawy jako produkty z weryfikacją zakupów | Jeden serwer, jedna administracja, ten sam kod kont i zakupów; klient Godot aplikacji quizowej dzieli SDK z JvP | Nakama jest „growa”; dla wersji webowej trzeba klienta JavaScript (Nakama go ma) |
| Supabase dla aplikacji quizowej, Nakama dla JvP | Dwa backendy | Supabase wygodniejszy dla zwykłej aplikacji webowej | Dwa systemy do utrzymania |
| Na start bez kont | Web: plik + licencja. Play: zakupy w aplikacji bez synchronizacji | Najszybciej na rynek | Kupione na stronie nie działa w aplikacji z Play i odwrotnie; ręczne przenoszenie postępu |

**Ocena przydatności serwera:** **umiarkowana.** Wersja 1 może działać bez backendu. Wspólne konta pojawią się razem z backendem JvP prawie bez kosztu dodatkowego.

### 3.3. Projekt treściowy i JvP: strona, blog, sklep cyfrowy i merch

**Stan** (plan prywatnego projektu treściowego, bez szczegółów):

- najpierw bezpłatne kanały własne: strona statyczna, lista e-mailowa, napiwki;
- produkty dopiero przy większej, zaangażowanej publiczności;
- domena i produkty to decyzja po okresie próbnym;
- konta i wydatki zatwierdza Owner.

**Dwie marki, dwa sklepy.** Projekt treściowy kieruje treści do dorosłych i nastolatków, a JvP jest dla dzieci. Merch JvP sprzedaje się **rodzicom**. Nie łączyć tego w jednym sklepie ani w treściach dla dzieci.

| Tor | Na start (bez serwera) | Później (przy skali) | Rola Hostingera |
| --- | --- | --- | --- |
| **Produkty cyfrowe** (planery, karty z faktami, e-booki, zestawy pytań) | Lemon Squeezy (rozlicza VAT za sprzedawcę, około 5% + 0,50 USD) albo Payhip lub Ko-fi Shop (VAT po Twojej stronie). E-booki: Amazon KDP | Ta sama platforma; ewentualnie własny sklep | Brak |
| **Merch** (koszulki, kubki, naklejki z postaciami i z JvP) | Printful lub Printify zintegrowane z **Etsy** (ruch z marketplace, bez abonamentu) albo z **Shopify** (około 30–40 USD/mies., niezweryfikowane) | Własny sklep na Shopify albo **WooCommerce** z wtyczką Printful | **Opcja:** WooCommerce na hostingu Business lub Cloud. Taniej w abonamencie, ale aktualizacje, bezpieczeństwo, RODO i VAT (procedura OSS) są po Twojej stronie |
| **Strona marki i blog** | Strona statyczna (Astro lub Hugo; agenci piszą wpisy przez PR) na Cloudflare Pages | Ghost(Pro) albo WordPress | **Opcja:** WordPress na hostingu, jeśli wybierzesz WordPress |
| **Polityka prywatności i usuwanie konta JvP** | Podstrony statyczne na domenie projektu (Cloudflare Pages) | — | Brak |
| **Pliki APK do pobrania** | Google Play; testowe wersje przez wydania na GitHubie albo magazyn obiektowy (np. Cloudflare R2) | — | Opcja: VPS z HTTPS i sumami kontrolnymi |

**Gdzie hostować strony.** Pierwotny plan zakładał GitHub Pages. Regulamin GitHub Pages wyklucza jednak strony służące głównie biznesowi, sprzedaży albo SaaS. Strona projektu będzie linkować napiwki, produkty i aplikacje, więc bezpieczniej od razu użyć **Cloudflare Pages** dla wszystkich stron projektów. Ograniczenie Cloudflare Pages to 25 MiB na plik, dlatego APK (26,6 MB i 57,7 MB) trzymać osobno. Publikować tylko wygenerowane, zatwierdzone treści, nigdy prywatnej wiki ani roboczych materiałów.

**Rekomendacja dla sklepu:** zacząć od platform, czyli Lemon Squeezy dla cyfrowych oraz Etsy + Printful dla merchu.

- Zero administracji i płatności tylko od sprzedaży.
- Rozliczanie VAT w dużej mierze po stronie platformy.

Własny sklep (Shopify albo WooCommerce na Hostingerze) ma sens dopiero, gdy prowizje zaczną przewyższać koszt i pracę własnego sklepu. Sprzedaż oznacza też wybór formy działalności i rozliczeń podatkowych w Polsce; to decyzja Ownera z księgową (już odnotowane w wiki).

**Ocena przydatności Hostingera dla sklepu i bloga:** **niska na start, umiarkowana przy skali** (WooCommerce, WordPress).

### 3.4. Pozostałe repozytoria

Pozostałe repozytoria nie potrzebują hostingu.

### Podsumowanie przydatności serwera

| Projekt | Teraz | Za 6–12 miesięcy | Co zamiast VPS-a na start |
| --- | --- | --- | --- |
| **JvP** | Niska (projekt i wymogi) | **Wysoka** (Nakama: konta, zakupy, gra przez internet) | Nakama lokalnie w Dockerze do rozwoju |
| **Aplikacja quizowa** | Niska | Umiarkowana (wspólne konta z JvP) | Strona statyczna + Lemon Squeezy; Play Billing |
| **Projekt treściowy: sklep i blog** | Niska | Umiarkowana (WooCommerce przy skali) | Lemon Squeezy, Etsy + Printful, strona statyczna |
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

Nie wliczono subskrypcji Claude i ChatGPT, kosztów narzędzi do generowania treści ani księgowości. Kurs orientacyjny: 1 USD ≈ 3,8–4,0 PLN, 1 EUR ≈ 4,3 PLN.

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
| Postęp w przeglądarce (aplikacja quizowa, wersja webowa) | Średnie | Zmiana domeny gubi postęp zapisany lokalnie | Ostateczna domena przed startem; eksport i import postępu albo konta |
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
| Teraz | Strona statyczna na Cloudflare Pages: polityka prywatności JvP, strona usuwania konta, strona projektu treściowego | JvP, projekt treściowy |
| Teraz | Specyfikacja „JvP online”: zakres (znajomi przez kod, bez czatu), bramka rodzica, dane minimalne, usuwanie konta; wymogi prawne do potwierdzenia | JvP |
| Teraz | Pilotaż recenzji krzyżowej Codexem na 5–10 PR-ach; potem pomiar na około 20 zadaniach (sekcja 2) | AI-crew |
| Przed zakupem serwera | Konkretna wycena: brutto za cały okres, odnowienie, kopie, zwroty, region, umowa powierzenia (sekcja 4) | JvP |
| Następnie | Nakama w Dockerze lokalnie i w CI; SDK Godota; konta, portfel, zakupy testowe Play Billing; gra przez relay obok lokalnego Wi-Fi | JvP |
| Następnie | Osobne repo nowej aplikacji quizowej; wersja webowa i sprzedaż zestawów przez Lemon Squeezy | Aplikacja quizowa |
| Przed testem zamkniętym JvP | VPS produkcyjny w UE (Hostinger KVM 2 albo Hetzner), kopie poza dostawcą, monitoring | JvP |
| Po okresie próbnym projektu treściowego | Lemon Squeezy dla produktów cyfrowych; Etsy + Printful dla merchu (osobno marka JvP dla rodziców) | Projekt treściowy, JvP |
| Później | Wspólne konta i uprawnienia aplikacji quizowej w Nakamie | Aplikacja quizowa |
| Przy skali sklepu | Porównanie: Shopify vs WooCommerce na Hostingerze | Projekt treściowy |

### Otwarte pytania do Ownera

1. **JvP online:** dobieranie tylko znajomych przez kod (zalecane dla dzieci) czy także obcych graczy?
2. **Konto w JvP:** wymagane czy opcjonalne? Rekomendacja: opcjonalne, zakładane przez rodzica; bez konta gra działa offline jak dziś.
3. **Wersja iOS:** w tym samym czasie co online, czy później? Od tego zależy Sign in with Apple i koszt konta Apple.
4. **Aplikacja quizowa:** od razu oba kanały (web i Google Play), czy najpierw tylko web?
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
| Rozmiary APK: aplikacja quizowa 26 613 508 B, JvP 1.2.0 57 705 396 B | `git ls-tree -l` w obu repozytoriach | **Potwierdzone** |
| Godot Web: tylko Compatibility; brak UDP i ENet, dostępne WebSocket i WebRTC | `godot-docs` @ `0709b93`, `exporting_for_web.rst` | **Potwierdzone** |
| JvP: renderer Mobile, protokół sieci 7, ENet i UDP | `project.godot`, `net_session.gd` @ `87655b7` | **Potwierdzone** |
| Aplikacja quizowa (APK) bez dostępu do internetu | Konfiguracja eksportu | **Potwierdzone** |
| Ceny Cloudflare Workers Paid (5 USD/mies.) i R2 (0,015 USD/GB) | Nie sprawdzałem ponownie | Przyjęte za Codexem |
| JvP: lokalna gra przez Wi-Fi jako punkt startu; online „potencjalnie” | — | **Nieaktualne:** Codex pisał przed decyzją Ownera o grze online |
| Ceny Hostinger i Hetzner niepotwierdzone handlowo | — | Zgodne z moim stanem: strony ofert były zablokowane w obu sesjach |

**Ocena:** raport Codexa jest rzetelny, ostrożny w twierdzeniach i dobrze udokumentowany przypiętymi źródłami. Nie znalazłem w nim błędu merytorycznego. Jego wkład przejąłem w tej wersji (lista na początku). Nie zmieniałem treści raportu Codexa.

## 9. Oferta no1.pl: analiza, etapy i alternatywy

Stan na 8 listopada 2026. Źródła:

- strony no1.pl (główna, hosting, VPS, VPS zarządzany, domeny, SSL, SLA, płatności, formularz zamówienia VPS, regulamin);
- **publiczne API cennika** `panel.no1.pl/api/pub/pakiety/`, z którego strona pobiera ceny. Kwoty poniżej pochodzą z tego API.

Ceny konkurencji pochodzą ze źródeł wtórnych i są orientacyjne.

### 9.1. Czym jest no1.pl

**no1.pl Sp. z o.o.** (Sitno, woj. pomorskie; KRS 0001211352, kapitał zakładowy 5000 zł). Firma pozycjonuje się jako **operator i opiekun infrastruktury dla małych firm**, a nie masowy hosting: „Jesteśmy operatorem, nie sklepem z kontami”.

Co deklaruje:

- własna infrastruktura w Polsce;
- jeden opiekun konta i numer telefonu;
- monitoring 24/7;
- bezpłatne migracje;
- poczta firmowa z antyspamem, konfiguracja SPF, DKIM i DMARC;
- VPN i logowanie SSO dla zespołu;
- umowa SLA z czasem reakcji.

Wysoki numer KRS sugeruje **niedawną rejestrację spółki**. Datę warto sprawdzić w KRS.

### 9.2. Cennik (brutto, z VAT 23%; z API, 8.11.2026)

**Hosting zarządzany** (rozliczenie roczne z góry; w każdym pakiecie poczta bez limitu skrzynek, SSL, monitoring, ochrona antymalware, kopie z odtwarzaniem, darmowa migracja, opiekun):

| Pakiet | Cena/rok | Miejsce | Strony / bazy | Domena .pl w cenie | Kolejna domena |
| --- | --- | --- | --- | --- | --- |
| Start (bez domeny) | **782,28 zł** | 20 GB w API (na stronie głównej 10 GB) | 1 / 1 | Nie | 242,31 zł/rok |
| Firma | **908,97 zł** | 20 GB | 1 / 1 | Tak (przez okres pakietu) | 242,31 zł/rok |
| Bez limitu | **1077,48 zł** | 50 GB | bez limitu / bez limitu | Tak | 189,42 zł/rok |

**Dodatki do hostingu (rocznie):**

- monitoring dostępności z alarmem i raportem miesięcznym: 244,77 zł;
- roczny przegląd bezpieczeństwa: 367,77 zł;
- pakiet „Opieka+” (oba razem): **490,77 zł**.

**SLA:** Basic 99,5% w cenie; Optymalny 99,8% (+20%); Premium 99,9% (+40%).

**Serwery VPS** (transfer bez limitu, IPv4 i IPv6, panel no1.panel, SLA 99,5%; rozliczenie miesięczne albo roczne, przy czym rok kosztuje tyle co 10 miesięcy):

| Rozmiar | Parametry | Self (bez administracji) /mies. | Self /rok | Zarządzany /mies. | Zarządzany /rok |
| --- | --- | --- | --- | --- | --- |
| S | 2 vCore, 4 GB RAM, 40 GB NVMe | **166,05 zł** | 1660,50 zł | **350,55 zł** | 3505,50 zł |
| M | 4 vCore, 8 GB RAM, 80 GB NVMe | 332,10 zł | 3321,00 zł | 516,60 zł | 5166,00 zł |
| L | 8 vCore, 16 GB RAM, 160 GB NVMe | 664,20 zł | 6642,00 zł | 848,70 zł | 8487,00 zł |
| XL | 12 vCore, 24 GB RAM, 320 GB NVMe | 959,40 zł | 9594,00 zł | 1143,90 zł | 11 439,00 zł |

Wariant zarządzany zawiera **CloudLinux OS Shared Pro i Imunify360** (narzędzia typowe dla hostingu PHP i WordPress); konfigurację i aktualizacje prowadzi no1.

**Domeny .pl:** rejestracja 60,27 zł, **przedłużenie 183,27 zł/rok**, wyjęcie z kwarantanny 244,77 zł. Strona domen rejestruje tylko końcówkę `.pl`. Certyfikaty: Let's Encrypt w cenie hostingu i VPS zarządzanego; certyfikaty płatne (DV, OV, EV, wildcard) wyceniane indywidualnie.

### 9.3. Warunki umowy (regulamin): co ważne dla projektów

| Zapis | Znaczenie |
| --- | --- |
| Przedpłata online za cały okres (Autopay: karta, BLIK, przelew); faktura VAT po wpłacie | Brak płatności z odroczonym terminem. Rozliczenie miesięczne VPS **nie wymaga wieloletniej przedpłaty**, w przeciwieństwie do cen promocyjnych Hostingera |
| Automatyczne odnowienie; powiadomienie 21 dni przed końcem; rezygnacja do 14 dni przed końcem | Uczciwe i przewidywalne; trzeba pilnować terminu rezygnacji |
| Płatność cykliczna kartą: kwota równa cenie z cennika w dniu odnowienia | Cena może się zmienić przy odnowieniu (z powiadomieniem) |
| **VPS Self: operator nie robi kopii danych** (chyba że zamówiona osobna usługa kopii) | Dla Nakamy trzeba mieć własne kopie, najlepiej u innej firmy |
| VPS zarządzany: kopie w zakresie z potwierdzenia zamówienia | Zakres, częstotliwość i czas odtworzenia trzeba **zapisać w zamówieniu** |
| Po końcu umowy dane VPS dostępne 14 dni, usunięcie w 30 dni | Okno na migrację jest krótkie; planować przesiadkę przed końcem okresu |
| **Umowa powierzenia przetwarzania danych** na wniosek | Plus dla RODO (gra dla dzieci, sklep) |
| Odpowiedzialność wobec firm ograniczona do opłaty za bieżący okres | Standard rynkowy; nie zastępuje własnych kopii |
| Dla konsumentów 14 dni na odstąpienie | Dotyczy zakupu jako osoba prywatna |

### 9.4. Mocne i słabe strony w kontekście naszych projektów

**Mocne:**

- polska spółka, umowa i faktura po polsku, dane w Polsce, umowa powierzenia;
- **opieka człowieka**: jeden opiekun, monitoring, darmowa migracja, przeglądy bezpieczeństwa;
- **poczta firmowa bez limitu skrzynek** w każdym pakiecie hostingu, z konfiguracją SPF, DKIM i DMARC (ważne dla dostarczalności newslettera i maili transakcyjnych sklepu);
- VPS **bez długiej przedpłaty** (miesięcznie), rok za cenę 10 miesięcy;
- jawne poziomy SLA do wyboru.

**Słabe:**

- **cena mocy obliczeniowej.** VPS S (2 vCore, 4 GB) za 166 zł/mies. to kilka razy więcej niż porównywalny serwer u Hetznera (około 25–55 zł/mies.) czy Hostingera po odnowieniu (około 60 zł/mies.);
- **drogie przedłużenie domeny .pl** (183,27 zł/rok wobec około 60–75 zł brutto u części rejestratorów, np. OVH 58,99 zł netto); brak rejestracji `.com`, a projekt treściowy i aplikacja quizowa są anglojęzyczne;
- **brak oferty typowo deweloperskiej:** nic o Dockerze, API do automatyzacji, migawkach na żądanie ani magazynie obiektowym. Agentom trudniej zarządzać infrastrukturą jako kodem;
- **CloudLinux i Imunify360** w wariancie zarządzanym służą hostingowi PHP, nie kontenerom. Czy no1 zarządzi serwerem z Dockerem i Nakamą, trzeba **potwierdzić**;
- **mała, młoda firma** (kapitał 5000 zł): większe ryzyko ciągłości niż u dużych dostawców. Liczba i redundancja centrów danych nie są opisane;
- **niespójności na stronie** sugerują bardzo świeżą ofertę:
  - pakiet Start: 10 GB na stronie głównej, 20 GB w API;
  - formularz VPS: „płatność po uruchomieniu, na podstawie faktury”, a regulamin: „jedyną formą zapłaty jest przedpłata online”;
  - na stronie zamówienia VPS widać fragment komentarza programisty;
  - w publicznym API widać wewnętrzną notatkę („HOST-602, decyzja właściciela”).
  
  Warunki warto potwierdzić **na piśmie** przed zamówieniem.

### 9.5. Z czego korzystać i na jakim etapie

| Etap | Potrzeba | Czy no1.pl? | Uzasadnienie |
| --- | --- | --- | --- |
| **Teraz (start)** | Domena projektów, strony statyczne (polityka prywatności JvP, strona projektu treściowego, quiz) | **Nie** | Cloudflare Pages za darmo wystarcza. Domena `.com` u niezależnego rejestratora; no1 nie rejestruje `.com`, a przedłużenie `.pl` jest drogie |
| Teraz (start) | Adres e-mail w domenie projektu | **Raczej nie** | Na 1–2 osoby wystarczy przekierowanie (Cloudflare Email Routing) do Gmaila albo darmowy Zoho Mail (do 5 osób, bez IMAP). no1 opłaca się, gdy poczta idzie w pakiecie z hostingiem strony |
| Rozwój JvP online (Nakama lokalnie i w CI) | Środowisko testowe | **Nie** | Docker lokalnie i w CI; serwer nie jest potrzebny |
| **Test zamknięty i wydanie JvP online** | Produkcyjny serwer z Nakamą i Postgresem w UE, kopie, monitoring | **Warunkowo: tylko wariant zarządzany po wycenie indywidualnej** | VPS Self (166 zł/mies.) nie daje kopii ani administracji, więc przegrywa z Hetznerem lub Hostingerem 3–6×. **VPS zarządzany S (350,55 zł/mies.)** ma sens, jeśli no1 przejmie Dockera, Nakamę, codzienne kopie, monitoring i aktualizacje. Zastąpi wtedy 2–4 h/mies. Twojej pracy (200–400 zł przy 100 zł/h), więc koszt łączny jest porównywalny. Dochodzą polski kontakt i umowa powierzenia (dane dzieci) |
| **Etap sprzedaży w projekcie treściowym**: blog lub sklep na WordPress/WooCommerce, poczta firmowa | Hosting PHP z opieką, kopiami i pocztą | **Tak, dobry kandydat** | Pakiet „Bez limitu” (1077,48 zł/rok) z „Opieka+” (490,77 zł/rok) = około **1570 zł/rok**: kilka serwisów, poczta, monitoring, przeglądy, migracja. To dokładnie profil no1. Porównać z polskimi hostingami (nazwa.pl, cyber_Folks, home.pl) i Hostingerem |
| Działalność gospodarcza z zespołem | Poczta firmowa, VPN, SSO, SLA, opiekun | **Tak** | To główna specjalizacja no1 |
| Runner agentów AI-crew | Tani, elastyczny Linux na pilotaż | **Nie** | Za drogo za zasoby; brak automatyzacji przez API. Lepszy Hetzner lub Hostinger na krótki okres |
| Dystrybucja APK | Hosting dużych plików | **Nie** | Google Play, wydania na GitHubie, Cloudflare R2 |

**Co może być potrzebne lub korzystne na start (przed jakimkolwiek zakupem):**

1. **Bezpłatna rozmowa z no1** (oferują ją) i prośba o:
   - wzór umowy SLA (Załącznik nr 1);
   - wycenę **VPS zarządzanego z Dockerem i Nakamą**: codzienne kopie poza serwerem, retencja, czas odtworzenia, monitoring, SLA 99,8%;
   - informację o centrach danych i redundancji;
   - potwierdzenie na piśmie rozbieżności ze strony (10/20 GB, forma płatności).
2. Jeśli rozmowa wypadnie dobrze: **mały, niekrytyczny pierwszy krok**. Na przykład pakiet hostingu dla przyszłej strony marki z pocztą albo miesięczny VPS testowy. Nie od razu produkcja gry.
3. **Domeny niezależnie od no1** (nawet jeśli hosting będzie u nich). Przenosiny hostingu nie wymagają wtedy przenoszenia domen, a przedłużenie jest tańsze.

### 9.6. Porównanie z alternatywami

| Potrzeba | no1.pl | Najlepsza alternatywa | Za alternatywą | Za no1.pl |
| --- | --- | --- | --- | --- |
| Domena `.com` | Brak | **Cloudflare Registrar** (bez marży, około 10–11 USD/rok; niezweryfikowane) | Cena, DNS i Pages w jednym miejscu | — |
| Domena `.pl` | 60,27 zł, potem **183,27 zł/rok** | Rejestrator z niskim przedłużeniem, np. OVHcloud (58,99 zł netto/rok). Cloudflare **nie obsługuje `.pl`** (według forum Cloudflare, marzec 2026) | Około 2,5× taniej co roku | Domena w cenie pakietu hostingu „Firma” lub „Bez limitu” przez okres pakietu |
| Strony statyczne | Hosting od 782 zł/rok | **Cloudflare Pages** (0 zł) | Darmowe, globalny CDN, deploy z gita | Opieka i monitoring, ale zbędne dla stron statycznych |
| Poczta w domenie (1–5 osób) | W pakiecie hostingu (skrzynki bez limitu) | **Cloudflare Email Routing + Gmail** (0 zł, tylko przekierowanie) albo **Zoho Mail Free** (do 5 osób, bez IMAP); **Google Workspace** od około 31,50 zł/os./mies. | Darmowe lub w pełni zarządzane przez Google | Pełne skrzynki bez limitu i konfiguracja SPF, DKIM, DMARC w cenie hostingu |
| WordPress/WooCommerce z opieką | **Około 1570 zł/rok** (Bez limitu + Opieka+) | **Hostinger Business** (taniej na start; odnowienie około 9–17 USD/mies.) albo polskie: nazwa.pl, cyber_Folks, home.pl (ceny do porównania) | Niższa cena i więcej narzędzi | Człowiek, który pilnuje i reaguje; migracja i przeglądy w cenie; brak wieloletniej przedpłaty |
| Backend gry (Nakama, Docker) | VPS Self S 166 zł/mies.; zarządzany S 350,55 zł/mies. | **Hetzner** (około 25–55 zł/mies., miesięcznie) albo **Hostinger KVM 2** (około 30–60 zł/mies.) | 3–6× taniej, standardowe migawki, większa skala | Tylko wariant zarządzany z wyceną obejmującą Dockera i kopie: oszczędność Twojego czasu, polski kontakt, umowa powierzenia |
| Pilotaż agentów | VPS Self S 166 zł/mies. | **Hetzner** (krótki okres, rozliczenie godzinowe) | Cena, API, szybkie tworzenie i usuwanie | — |
| Sklep bez administracji | — | **Lemon Squeezy** (cyfrowe), **Etsy + Printful** (merch), Shopify | Brak serwera i VAT po stronie platformy | — |

**Najlepsza alternatywa dla no1.pl, ogólnie:** stos **Cloudflare + Hetzner (lub Hostinger) + platformy sprzedażowe**.

- Cloudflare: domena `.com`, DNS, Pages, Email Routing, R2.
- Hetzner albo Hostinger: jeden przenośny VPS z Nakamą.
- Platformy sprzedażowe: Lemon Squeezy, Etsy z Printful.

To najtańsze i najbardziej elastyczne rozwiązanie. Wymaga jednak Twojego czasu (sekcja 5) i obsługi w języku angielskim.

**no1.pl wygrywa tam, gdzie liczy się przejęcie odpowiedzialności, a nie cena zasobów:**

- WordPress lub WooCommerce z pocztą firmową i opieką (etap sprzedaży w projekcie treściowym);
- ewentualnie zarządzany serwer gry z polską umową powierzenia, jeśli wycena pokaże, że no1 faktycznie przejmie administrację Dockera i Nakamy;
- później: VPN, SSO i SLA dla zespołu.

### 9.7. Rekomendacja

1. **Teraz:** nie kupować nic w no1.pl. Domena `.com` w Cloudflare (`.pl` u rejestratora z niskim przedłużeniem, jeśli potrzebna), strony na Cloudflare Pages, poczta przez przekierowanie albo Zoho.
2. **Przed wyborem serwera dla JvP online:** zapytać no1 o wycenę VPS zarządzanego z Dockerem i Nakamą (kopie, monitoring, SLA 99,8%). Porównać z Hetznerem lub Hostingerem plus Twoje 2–4 h/mies. Wybrać tańszą opcję **łącznie z czasem**.
3. **Etap sprzedaży w projekcie treściowym (sklep lub blog na WordPressie):** no1 „Bez limitu” z „Opieka+” to mocny kandydat. Zacząć od rocznego pakietu, domeny trzymać osobno, kopie także poza no1.
4. **Zawsze:** warunki z rozmowy (kopie, retencja, czas odtworzenia, SLA, forma płatności) potwierdzić w zamówieniu lub umowie, bo strona zawiera rozbieżności.

## Źródła

- Raport wejściowy: [`resources/raport-orkiestracja-agentow-herdr-hostinger.md`](../resources/raport-orkiestracja-agentow-herdr-hostinger.md)
- no1.pl (stan z 8.11.2026):
  - [strona główna](https://no1.pl/), [hosting](https://no1.pl/hosting/), [VPS](https://no1.pl/vps/), [VPS zarządzany](https://no1.pl/vps-zarzadzany/), [domeny](https://no1.pl/domeny/), [SSL](https://no1.pl/ssl/), [SLA](https://no1.pl/sla/), [płatności](https://no1.pl/platnosci/), [regulamin](https://no1.pl/regulamin/), [formularz zamówienia VPS](https://no1.pl/wniosek-vps/);
  - publiczne API cennika: `https://panel.no1.pl/api/pub/pakiety/` (pakiety, ceny domen, dodatki, poziomy SLA).
- Porównania do rozdziału 9 (źródła wtórne, ceny orientacyjne):
  - [OVHcloud .pl](https://www.ovhcloud.com/pl/domains/tld/pl/);
  - [domainoffer.net, .pl](https://domainoffer.net/tld/pl/ovh);
  - [Cloudflare TLD policies](https://www.cloudflare.com/tld-policies) i [forum: prośba o .pl](https://community.cloudflare.com/c/application-performance/registrar-feature-request/100);
  - [Google Workspace, cennik PL](https://workspace.google.com/intl/pl/pricing);
  - [Zoho Mail, plan darmowy (przegląd 2026)](https://aiproductivity.ai/blog/zoho-mail-free-plan-review/);
  - [Cybernews, ranking hostingów PL 2026](https://cybernews.com/pl/najlepsze-hostingi/);
  - [WebsitePlanet: nazwa.pl](https://www.websiteplanet.com/pl/web-hosting/nazwa-pl/), [cyber_Folks](https://www.websiteplanet.com/pl/web-hosting/cyber_folks/).
- [Analiza Codexa z 7.11.2026](2026-11-07-codex-ai-crew-hosting-i-migracja.md) (commit `48d8031`) i jej źródła pierwotne sprawdzone w tej sesji:
  - [Herdr README](https://github.com/herdrdev/herdr/blob/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde/README.md);
  - [herdr-core security](https://github.com/herdrdev/herdr-core/blob/9ce385d9c8abb041dd4437476d770365b3fb5282/docs/security.md);
  - [Hermes SECURITY](https://github.com/NousResearch/hermes-agent/blob/9ffa7dff23726d8daa8b3e167b20a5fabc2e04ef/SECURITY.md);
  - [GitHub Pages limits](https://github.com/github/docs/blob/8cd1075179df75319912891d6620c9cb78eefb4d/content/pages/getting-started-with-github-pages/github-pages-limits.md);
  - [Cloudflare Pages limits](https://github.com/cloudflare/cloudflare-docs/blob/53ce9b502646fdc019b8184b29b9f1054939e1b6/src/content/docs/pages/platform/limits.mdx);
  - [Godot: eksport na Web](https://github.com/godotengine/godot-docs/blob/0709b93758c40d26c91e1d9e4f3afd262c4ed386/tutorials/export/exporting_for_web.rst).
- Repozytoria Ownera (stan z 7.11.2026): publiczne `education-games` (`junk-vs-plants/README.md`, `PLAN_PUBLIKACJI.md`) oraz dwa prywatne projekty (szczegóły pominięto).
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
