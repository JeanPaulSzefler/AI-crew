# Śpiewnik na żywo (nazwa robocza): wymagania wstępne, ocena miejsca w repozytoriach i plan dla AI-crew

8 listopada 2026 · **Wersja 1 (robocza, przed odpowiedziami Ownera)** · Zadanie startowe nowego repo: [`blueprints/spiewnik-live/TASK-000-bootstrap.md`](../blueprints/spiewnik-live/TASK-000-bootstrap.md)

## W skrócie

1. **Pomysł:** wspólny, interaktywny śpiewnik do prowadzenia śpiewu na wydarzeniach.
   - Prowadzący uruchamia wydarzenie, a uczestnicy dołączają z telefonu lub przeglądarki, podając kod, jak w Kahoot.
   - Wszyscy widzą ten sam fragment tekstu, przełączany przez prowadzącego.
   - Każdy może w dowolnej chwili wyjść do samodzielnego przeglądania i jednym przyciskiem wrócić „na żywo”.
2. **Rekomendacja: nowe repozytorium** (robocza nazwa `spiewnik-live`), a nie podprojekt istniejącego.
   - Żadne obecne repo nie pasuje. `learning_tools` ma decyzje „bez backendu i bez hostingu”, a śpiewnik wymaga synchronizacji na żywo.
   - Nadaje się natomiast na **pierwszy realny produkt dla AI-crew** (pilotaż struktury z raportu z 31.10).
3. **Architektura na start: aplikacja webowa (PWA) bez instalacji** i lekki serwer pokojów na żywo w usłudze zarządzanej.
   - Rekomendowane: Cloudflare Workers + Durable Objects. Alternatywa: Supabase Realtime.
   - Bez własnego VPS-a, bo najdroższy jest czas administracji (raport z 7.11, sekcja 5).
   - Aplikacja w sklepach później; Godot nie pasuje do aplikacji tekstowej.
4. **Podejście „najpierw lokalnie i plik” (jak w Exam Drill).**
   - Utwory, biblioteki i wydarzenia żyją w plikach JSON ze schematem, łatwych do edycji przez człowieka i agenta AI.
   - Serwer przechowuje tylko trwające wydarzenie. Konta i chmura bibliotek dopiero w drugim etapie.
5. **Najważniejsze ryzyka:**
   - **prawa autorskie do tekstów** (ZAiKS, wydawcy, CCLI);
   - **słaby internet na miejscu wydarzenia**: treść pobierana przy dołączeniu, przegląd działa offline;
   - bezpieczeństwo kodu wydarzenia.
6. **Pytania do Ownera są w sekcji 8.** Odpowiedzi zmienią zakres MVP, wybór technologii i zadania.

## 1. Pomysł i słownik

| Pojęcie | Znaczenie w tej aplikacji |
| --- | --- |
| **Utwór** (pieśń, piosenka) | Tytuł, metadane i tekst podzielony na **strony** (slajdy), np. zwrotki i refren. Opcjonalnie kolejność wykonania (refren po każdej zwrotce) |
| **Strona** | Jeden fragment tekstu wyświetlany naraz |
| **Biblioteka** | Zbiór utworów (np. „Śpiewnik DK”, „Kolędy”). Utwór może być w wielu bibliotekach |
| **Wydarzenie** | Zamknięta, uporządkowana lista utworów z jednej lub wielu bibliotek, przygotowana na konkretne spotkanie. Kolejność ustala i zmienia tylko prowadzący |
| **Prowadzący** (admin) | Tworzy wydarzenie, uruchamia je i steruje stroną na żywo |
| **Uczestnik** | Dołącza kodem lub kodem QR, bez konta. Widzi tekst na żywo albo przegląda samodzielnie |
| **Tryb na żywo** | Ekran uczestnika podąża za prowadzącym: ten sam utwór, ta sama strona |
| **Tryb przeglądania** | Uczestnik sam przewija strony i utwory. Widzi, gdzie jest „na żywo”, i może jednym przyciskiem wrócić |
| **Widok rzutnika** | Pełnoekranowy, duży tekst na laptopie podłączonym do rzutnika lub telewizora, podążający za trybem na żywo |

Podobieństwa:

- **do Kahoot:** kod wydarzenia, dołączanie bez konta, prowadzący steruje ekranami wszystkich;
- **do Exam Drill:** treść jako dane w plikach, import i eksport, standard pliku z instrukcją dla agenta AI, działanie na telefonie.

## 2. Wymagania funkcjonalne (wstępne)

Priorytety: **MVP** (pierwsze użycie na prawdziwym wydarzeniu), **M2** (drugi etap: konta i chmura), **Później**.

### 2.1. Utwory i biblioteki

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-01 | Utworzenie, edycja i usunięcie utworu: tytuł, tekst, podział na strony (pusta linia = nowa strona), etykiety sekcji (Zwrotka 1, Refren, Bridge), kolejność wykonania | MVP |
| F-02 | Metadane utworu: autor słów, autor muzyki, źródło (np. śpiewnik, numer), język, tagi, **pole praw** (domena publiczna, licencja, „do użytku wewnętrznego”) | MVP |
| F-03 | Biblioteka: lista utworów z wyszukiwaniem po tytule, pierwszej linijce, tagu i numerze; sortowanie | MVP |
| F-04 | Uruchomienie dowolnego utworu z biblioteki **od razu na żywo** (wydarzenie ad hoc z jednym utworem) | MVP |
| F-05 | Podgląd stron utworu przed wyświetleniem (prowadzący) | MVP |
| F-06 | Akordy nad tekstem w widoku dla muzyków (format ChordPro); uczestnicy widzą sam tekst | Później (pytanie 3) |
| F-07 | Wersje utworu (np. skrócona) bez duplikowania całości | Później |

### 2.2. Wydarzenia

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-10 | Utworzenie wydarzenia z utworów jednej lub kilku bibliotek; ustalenie kolejności (przeciąganie) | MVP |
| F-11 | **Lista zamknięta:** uczestnicy nie zmieniają listy; prowadzący może dodawać, usuwać i przestawiać utwory także w trakcie | MVP |
| F-12 | Zablokowanie edycji listy (np. po przygotowaniu przez zespół) | M2 |
| F-13 | Kilku prowadzących jednego wydarzenia (współprowadzący przejmuje sterowanie) | M2 (pytanie 7) |
| F-14 | Szablon wydarzenia, np. „Spotkanie kręgu: pieśń na początek, do Ducha Świętego, na zakończenie” | Później |

### 2.3. Tryb na żywo

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-20 | Start wydarzenia generuje **kod** (np. 6 znaków) i **kod QR** z odnośnikiem | MVP |
| F-21 | Dołączenie uczestnika z przeglądarki bez instalacji i bez konta; opcjonalny pseudonim | MVP |
| F-22 | Prowadzący: następna/poprzednia strona, skok do utworu i strony, **wygaszenie** (pusty ekran), zakończenie wydarzenia | MVP |
| F-23 | Uczestnicy w trybie na żywo widzą zmianę strony **w ciągu około 1 s** | MVP |
| F-24 | Spóźniony uczestnik po dołączeniu od razu widzi aktualny utwór i stronę | MVP |
| F-25 | Po zerwaniu połączenia klient sam się łączy ponownie i wyrównuje stan | MVP |
| F-26 | **Widok rzutnika**: pełny ekran, duża czcionka, wysoki kontrast, bez elementów sterujących | MVP (pytanie 2) |
| F-27 | Liczba uczestników online widoczna dla prowadzącego | M2 |
| F-28 | Interakcje jak w Kahoot: głosowanie na następną pieśń, prośby o pieśń, reakcje | Później (pytanie 16) |

### 2.4. Tryb przeglądania (uczestnik)

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-30 | Przełączenie „na żywo” ↔ „przeglądam” w dowolnej chwili | MVP |
| F-31 | W przeglądaniu: następna i poprzednia strona, lista utworów wydarzenia, przejście do dowolnego utworu | MVP |
| F-32 | Stały wskaźnik „na żywo jest teraz: utwór X, strona Y” i przycisk „Wróć na żywo” | MVP |
| F-33 | Przegląd całej biblioteki (nie tylko utworów wydarzenia), jeśli prowadzący na to pozwoli | M2 (pytanie 6) |
| F-34 | Ustawienia czytelności: rozmiar czcionki, tryb ciemny, wysoki kontrast | MVP |

### 2.5. Import, eksport i standard pliku

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-40 | Eksport i import **utworu, biblioteki i wydarzenia** do i z jednego pliku w formacie natywnym (sekcja 4) | MVP |
| F-41 | Walidacja pliku przed importem, z czytelnymi błędami (numer utworu, pole, co jest nie tak) | MVP |
| F-42 | **Standard pliku i instrukcja dla agenta AI** (wzór: `learning_tools/authoring/`): schemat JSON, przykład, zasady dzielenia na strony, lista błędów | MVP |
| F-43 | Import ze zwykłego tekstu (wklejony tekst → strony po pustych liniach) | MVP |
| F-44 | Import i eksport **ChordPro** (`.cho`, `.chordpro`) | M2 |
| F-45 | Import i eksport **OpenLyrics** (XML, używany m.in. przez OpenLP) | Później |
| F-46 | Import przy łączeniu: utwór o tym samym identyfikatorze nie tworzy duplikatu; podgląd różnic i wybór | M2 |

### 2.6. Konta, udostępnianie i dane

| Id | Wymaganie | Priorytet |
| --- | --- | --- |
| F-50 | MVP bez kont: biblioteki na urządzeniu prowadzącego, kopia przez eksport pliku; wydarzenie z tajnym odnośnikiem prowadzącego | MVP |
| F-51 | Konta prowadzących (logowanie Google); biblioteki w chmurze, synchronizacja między telefonem a komputerem | M2 |
| F-52 | Udostępnianie biblioteki innym prowadzącym (odczyt lub edycja) | M2 (pytanie 5) |
| F-53 | Usuwanie konta i danych w aplikacji i przez stronę WWW (wymóg sklepów, sekcja 3 raportu z 7.11) | M2 |
| F-54 | Uczestnicy zawsze bez kont; serwer nie przechowuje danych uczestników po zakończeniu wydarzenia | MVP |

## 3. Wymagania niefunkcjonalne

| Id | Wymaganie | Wartość wstępna (do potwierdzenia) |
| --- | --- | --- |
| N-01 | Opóźnienie zmiany strony | ≤ 1 s dla 95% uczestników przy normalnym internecie |
| N-02 | Skala wydarzenia | Do 300 uczestników (pytanie 1) |
| N-03 | Działanie przy słabym internecie | Cała treść wydarzenia pobierana przy dołączeniu (kilkadziesiąt KB). Przeglądanie działa offline; tryb na żywo wraca po odzyskaniu połączenia |
| N-04 | Urządzenia | Telefony od 360 px szerokości, tablety, laptop i rzutnik. Bieżące Chrome, Safari (iOS), Firefox, Edge. Macierz rozmiarów ekranów jak w `learning_tools` (T-56) |
| N-05 | Instalacja | Brak wymaganej instalacji (PWA z opcją „dodaj do ekranu głównego”) |
| N-06 | Prywatność | Uczestnicy bez kont i bez danych osobowych; brak analityki firm trzecich; dane wydarzenia usuwane po zakończeniu (np. po 24 h) |
| N-07 | Bezpieczeństwo | Sterowanie tylko z tokenem prowadzącego (nie samym kodem); ograniczenie prób zgadywania kodów; kody wygasają |
| N-08 | Koszt | Darmowy próg usług zarządzanych przy małej skali; do około 25 zł/mies. przy regularnym użyciu |
| N-09 | Utrzymanie | Brak własnego serwera do administrowania; infrastruktura opisana w repo (konfiguracja w gicie) |
| N-10 | Dostępność | Czytniki ekranu (role ARIA), sterowanie klawiaturą u prowadzącego (strzałki, spacja, pilot do prezentacji) |
| N-11 | Testy | Testy automatyczne wielu klientów (prowadzący + kilku uczestników) w przeglądarce w CI |

## 4. Format pliku (propozycja do decyzji)

Na wzór Exam Drill: **jeden typ pliku JSON ze schematem**. Może zawierać utwory, biblioteki i wydarzenia, więc ten sam plik służy do eksportu jednego utworu i całego śpiewnika. Tekst utworu jest zapisany **jako zwykły tekst**, a nie tablica znaków. Dzięki temu człowiek i agent AI edytują go naturalnie.

```json
{
  "format": "spiewnik-live",
  "formatVersion": 1,
  "songs": [
    {
      "id": "przykladowa-piesn",
      "title": "Przykładowa pieśń",
      "authors": { "lyrics": "Autor testowy", "music": "Kompozytor testowy" },
      "source": "Śpiewnik testowy, nr 1",
      "rights": "domena-publiczna",
      "language": "pl",
      "tags": ["przyklad", "zakonczenie"],
      "sections": [
        { "id": "z1", "label": "Zwrotka 1", "text": "Pierwsza linia pierwszej zwrotki,\ndruga linia pierwszej zwrotki.\n\nTrzecia linia (nowa strona po pustej linii)." },
        { "id": "r", "label": "Refren", "text": "Linia refrenu,\ndruga linia refrenu." },
        { "id": "z2", "label": "Zwrotka 2", "text": "Pierwsza linia drugiej zwrotki,\ndruga linia drugiej zwrotki." }
      ],
      "order": ["z1", "r", "z2", "r"]
    }
  ],
  "libraries": [
    { "id": "spiewnik-testowy", "title": "Śpiewnik testowy", "songIds": ["przykladowa-piesn"] }
  ],
  "events": [
    { "id": "spotkanie-2026-11", "title": "Spotkanie, listopad", "items": [ { "songId": "przykladowa-piesn" } ], "locked": false }
  ]
}
```

Przykład używa tekstu zastępczego. Przykłady i testy w repo też nie powinny zawierać tekstów chronionych (sekcja 7).

Zasady wstępne:

- `id` stabilne i czytelne (kebab-case). Ten sam `id` przy imporcie oznacza ten sam utwór (F-46).
- **Strona = sekcja**, a długa sekcja dzieli się na strony po pustej linii. Kolejność wykonania w `order`; refren można powtarzać.
- Pole `rights` jest obowiązkowe (sekcja 7).
- Schemat w repo (`format/spiewnik.schema.json`), walidator w CI, instrukcja dla agenta AI i przykłady. Wzorem jest `learning_tools/authoring/`: `AGENT-INSTRUCTIONS.md`, `QUESTION-STANDARD.md`, schemat i walidator.
- Import ChordPro, OpenLyrics i czystego tekstu **konwertuje do tego formatu**. Eksport w drugą stronę.

## 5. Architektura i technologie

### Rekomendacja

| Warstwa | Wybór | Dlaczego |
| --- | --- | --- |
| Klient | **PWA**: TypeScript z lekkim zestawem do budowania (Vite), bez ciężkiego frameworka albo z małym (np. Svelte lub Preact). Decyzja zespołu w ADR | Dołączanie bez instalacji to sedno modelu „jak Kahoot”. Jedna aplikacja dla prowadzącego, uczestnika i rzutnika. W Exam Drill świadomie wybrano „bez budowania” (decyzja 0002), ale tu dochodzą WebSocket, synchronizacja i stan, więc lekkie budowanie jest uzasadnione |
| Pokój na żywo | **Cloudflare Workers + Durable Objects** (jeden obiekt na wydarzenie, połączenia WebSocket z hibernacją, stan w SQLite obiektu) | Gotowy model „pokoju”; brak serwera do utrzymania; darmowy próg na start; wpisuje się w rekomendację Cloudflare z raportu z 7.11 (domena, Pages) |
| Hosting klienta | **Cloudflare Pages** | Darmowy, HTTPS, CDN |
| Biblioteki w MVP | **Na urządzeniu** (IndexedDB) + eksport i import pliku | Jak Exam Drill: prywatnie, bez kont; serwer zna tylko trwające wydarzenie |
| Konta i chmura (M2) | Do wyboru w ADR: **Cloudflare D1 + logowanie Google** albo **Supabase** (Auth + Postgres) | Supabase daje gotowe logowanie; trzymanie wszystkiego w Cloudflare to jeden dostawca. Decyzja przy M2 |
| Aplikacja w sklepach | **Później**: opakowanie PWA (Trusted Web Activity na Androida, Capacitor dla iOS) | Najpierw sprawdzić, czy PWA wystarcza |

### Protokół na żywo (szkic)

1. Prowadzący tworzy pokój i wysyła treść wydarzenia (JSON). Serwer zwraca kod uczestnika i **osobny token prowadzącego**.
2. Uczestnik łączy się kodem i od razu dostaje treść oraz aktualny stan `{songIndex, pageIndex, blank, rev}`.
3. Każda zmiana prowadzącego to nowy stan z rosnącym `rev`. Serwer rozsyła go wszystkim. Klient ignoruje stany starsze niż już widziany.
4. Zmiana listy utworów w trakcie (F-11) to nowa wersja treści (`contentRev`); klient pobiera ją w tle.
5. Tryb przeglądania jest **wyłącznie po stronie klienta**: uczestnik dalej odbiera stan, ale go nie wyświetla, tylko pokazuje wskaźnik „na żywo jest…”.
6. Koniec wydarzenia: serwer zamyka pokój i po czasie przechowywania usuwa treść.

Protokół zostanie opisany w specyfikacji (SPEC-002) niezależnie od dostawcy. Przesiadka z Durable Objects na inną usługę (Supabase Realtime, własny serwer WebSocket, Nakama) wymaga wtedy tylko zmiany warstwy transportu.

### Alternatywy

| Opcja | Za | Przeciw |
| --- | --- | --- |
| Supabase Realtime (Broadcast) + Supabase Auth | Konta i baza w jednym; dobra dokumentacja | Darmowy projekt jest wstrzymywany po około tygodniu bez aktywności, więc regularne wydarzenia wymagają planu Pro (około 25 USD/mies.). Według źródeł wtórnych darmowy plan ma limit około 200 jednoczesnych połączeń |
| Nakama (wspólna z JvP, raport z 7.11) | Jeden backend dla wszystkich aplikacji | Serwer gier na VPS-ie: administracja; za ciężka na prosty pokój tekstowy |
| Własny serwer WebSocket na VPS (no1.pl, Hetzner, Hostinger) | Pełna kontrola | Czas administracji i ryzyko awarii w trakcie wydarzenia |
| Tryb sieci lokalnej (laptop prowadzącego jako serwer w Wi-Fi sali) | Działa bez internetu | Telefony muszą być w tej samej sieci; przeglądarki nie mają UDP; więcej pracy. Dopiero jeśli internet na miejscu jest problemem (pytanie 14) |
| Godot (jak JvP i klient Exam Drill) | Znany zespołowi | Aplikacja tekstowa; eksport webowy tylko z rendererem Compatibility i dużym plikiem. Dołączanie z przeglądarki bez instalacji byłoby słabe |

### Podobne rozwiązania (punkt odniesienia, nie do kopiowania)

- **OpenLP**: otwartoźródłowy program do wyświetlania pieśni w kościołach. Format **OpenLyrics** (XML) i zdalny podgląd w przeglądarce.
- **ChordPro**: tekstowy format pieśni z akordami.
- Komercyjne: ProPresenter, Holyrics, OnSong.

Warto sprawdzić, czy OpenLP nie pokrywa już potrzeb, zanim zespół zbuduje własną aplikację. Pytanie 18.

## 6. Czy to pasuje do istniejącego repo?

| Repo | Dopasowanie | Uzasadnienie |
| --- | --- | --- |
| `learning_tools` (Exam Drill) | **Niskie** | Wspólna idea „treść jako plik + telefon”, ale decyzje 0002 (bez budowania, bez backendu) i 0006 (bez hostingu) wprost wykluczają tryb na żywo. Repo prywatne z surowymi materiałami ITIL. Mieszanie domen utrudniłoby pracę obu projektów |
| `education-games` (JvP) | Brak | Gry w Godot dla dzieci |
| `educationInfluencer` | Brak | Laboratorium treści, nie oprogramowania |
| `FOZ-ZOE` | **Treściowo tak, technicznie nie** | Konspekty spotkań kręgów DK przewidują śpiew (np. do Ducha Świętego); śpiewnik może im służyć. To jednak repozytorium dokumentów (md, docx, pdf), a nie aplikacji. Później konspekt może wskazywać pieśni z biblioteki |
| `klasa6` | Brak | Edukacja domowa |
| `AI-crew` | Nie jako kod | To repo zasad i blueprintów; aplikacja nie powinna tu żyć |

**Rekomendacja: nowe repozytorium**, zbudowane według struktury AI-crew (raport z 31.10, sekcja 8; wersja 3 raportu z 7.11). Śpiewnik dobrze nadaje się na **pierwszy produkt pilotażowy AI-crew**, bo jest mały, ma jasne kryteria odbioru i daje się testować automatycznie.

**Co przenieść z innych repo (wzorce, nie kod):**

- z `learning_tools`:
  - `authoring/` (standard pliku, schemat, instrukcja dla agenta, walidator);
  - zasada „najpierw specyfikacja” (`spec-change`);
  - decyzje i odrzucone pomysły jako pliki;
  - macierz rozmiarów ekranów (T-56);
- z `education-games`: doświadczenia z wykrywaniem w sieci lokalnej, gdyby potrzebny był tryb bez internetu;
- z raportu z 7.11:
  - Cloudflare jako hosting i domena;
  - konta projektu (Google Cloud, Apple) przy Ownerze;
  - zasady odtwarzania i przenośności.

Kodu nie współdzielić między repozytoriami. Każde ma własny cykl życia.

## 7. Ryzyka

| Ryzyko | Opis | Odpowiedź |
| --- | --- | --- |
| **Prawa autorskie do tekstów** | Wiele pieśni religijnych i piosenek jest chronionych (polskie organizacje zbiorowego zarządzania jak ZAiKS, wydawcy; za granicą licencje CCLI dla kościołów). Wyświetlanie i powielanie tekstów, zwłaszcza na publicznych lub transmitowanych wydarzeniach, może wymagać zgody. Platforma przechowująca teksty od użytkowników odpowiada za reakcję na zgłoszenia | Brak publicznego katalogu w MVP; treści tylko w wydarzeniach i prywatnych bibliotekach; obowiązkowe pole `rights`; adres do zgłoszeń naruszeń; **konsultacja prawna przed publicznym udostępnieniem** |
| Słaby internet na miejscu | Kościoły i sale często mają słaby zasięg | Treść pobierana przy dołączeniu; przegląd offline; wyraźny stan „brak połączenia”; tryb sieci lokalnej później |
| Przejęcie sterowania | Ktoś odgaduje kod i przełącza strony | Osobny token prowadzącego; limit prób; kody wygasają |
| Awaria w trakcie wydarzenia | Serwer niedostępny | Uczestnicy mają treść lokalnie; prowadzący może dalej wyświetlać na rzutniku z lokalnej kopii |
| Dzieci wśród uczestników (wydarzenia rodzinne) | Dane dzieci | Uczestnicy bez kont i danych; brak czatu; brak analityki |
| Uzależnienie od dostawcy | API Durable Objects jest specyficzne dla Cloudflare | Protokół w specyfikacji; warstwa transportu wymienna (sekcja 5) |
| Rozrost zakresu | Pokusa „jak ProPresenter” | Twarde MVP z sekcji 2; reszta w backlogu |

## 8. Pytania do Ownera

**Kontekst użycia**

1. Gdzie i z kim będzie używany śpiewnik (krąg DK, parafia, rekolekcje, koncert, szkoła, rodzina)? Ilu uczestników maksymalnie na jednym wydarzeniu?
2. Czy potrzebny jest **widok na rzutnik lub telewizor** obok telefonów? Czy telefony mają go zastąpić?
3. Czy muzycy potrzebują **akordów** (osobny widok), czy tylko tekst?
4. Jaki jest internet w typowym miejscu wydarzenia? Czy tryb bez internetu (sieć lokalna) jest konieczny?

**Role i treści**

5. Kto tworzy biblioteki: tylko Ty i zaufani prowadzący, czy każdy użytkownik? Czy biblioteki mają być współdzielone w grupie (np. wszystkie kręgi), czy prywatne?
6. Czy uczestnik w trybie przeglądania ma widzieć **tylko utwory wydarzenia**, czy całą bibliotekę?
7. Czy w jednym wydarzeniu może być **kilku prowadzących**? Czy prowadzący zmienia listę w trakcie?
8. Skąd pochodzą teksty: własne opracowania, istniejące śpiewniki (papierowe, PDF, Word), OpenLP? Jakie formaty importu są ważne?
9. Czy treści to głównie pieśni w domenie publicznej lub własne, czy także współczesne pieśni chronione? Czy wydarzenia bywają publiczne lub transmitowane?

**Produkt**

10. Czy na start wystarczy **aplikacja webowa** (PWA, „dodaj do ekranu głównego”), czy aplikacja w Google Play lub App Store jest potrzebna od razu?
11. Język interfejsu: tylko polski, czy też angielski?
12. Czy uczestnicy mają mieć jakieś interakcje (głosowanie na pieśń, prośby, reakcje), czy tylko czytanie?
13. Model: darmowe dla wspólnoty, płatne dla organizacji, inne?
14. Robocza nazwa (np. „Śpiewnik Live”, „Wspólny Śpiewnik”) i domena: osobna czy pod domeną projektu?

**Organizacja**

15. Repo publiczne czy prywatne? Rekomenduję prywatne do czasu wyjaśnienia praw do przykładowych tekstów.
16. Czy jest termin pierwszego prawdziwego użycia (pilotaż na wydarzeniu)?
17. Czy pilotaż AI-crew ma ruszyć właśnie na tym projekcie (planista, wykonawca, recenzent; pomiar kosztu na zadanie)?
18. Czy sprawdzałeś **OpenLP** lub podobne narzędzia? Czego w nich brakuje? Warto to wiedzieć przed budową własnej aplikacji.

## 9. Plan realizacji przez AI-crew

Zasady z raportu AI-crew z 31.10:

- jedno zadanie to jeden PR, z kryteriami odbioru i komendą testów (Definition of Ready);
- testy i CI są sędzią;
- dwie nieudane próby oznaczają eskalację;
- recenzent tylko do odczytu, na innym modelu niż wykonawca.

Role: **P** planista (Sonnet), **W** wykonawca (Sonnet; Haiku dla zadań mechanicznych po pomiarze), **R** recenzent (Opus lub Codex jako recenzja krzyżowa), **O** Owner.

### Etap 0: fundamenty

| Id | Zadanie | Rola | Zależy od | Kryterium odbioru |
| --- | --- | --- | --- | --- |
| T-000 | Utworzenie repo i struktury AI-crew ([zadanie startowe](../blueprints/spiewnik-live/TASK-000-bootstrap.md)) | O (repo, sekrety, ochrona gałęzi), W, R | Odpowiedzi na pytania 14, 15, 17 | Struktura z listy w TASK-000; CI zielone na pustym projekcie |
| T-001 | SPEC-000 Wizja i zakres MVP na podstawie odpowiedzi Ownera | P, O | T-000 | Owner akceptuje zakres MVP |
| T-002 | ADR-0001 stos klienta; ADR-0002 dostawca pokoju na żywo; ADR-0003 MVP bez kont | P, R, O | T-001 | Decyzje zapisane z uzasadnieniem i warunkiem powrotu |

### Etap 1: format i dane (bez sieci)

| Id | Zadanie | Rola | Zależy od | Kryterium odbioru |
| --- | --- | --- | --- | --- |
| T-010 | SPEC-001 Format pliku + `format/spiewnik.schema.json` + przykłady | P, W, R | T-002 | Schemat waliduje przykłady; błędne przykłady są odrzucane z czytelnym komunikatem |
| T-011 | Walidator w CI i jako funkcja w aplikacji | W | T-010 | Testy jednostkowe dla każdej klasy błędu |
| T-012 | `format/AGENT-INSTRUCTIONS.md` i `INSTRUKCJA-PL.md` (jak przygotować śpiewnik z AI) | W, R | T-010 | Agent zewnętrzny (np. ChatGPT) z samą instrukcją tworzy plik, który przechodzi walidację (test ręczny Ownera) |
| T-013 | Import z czystego tekstu (podział na strony po pustych liniach) | W | T-010 | Testy na 5 przykładowych tekstach |

### Etap 2: aplikacja lokalna (prowadzący, bez sieci)

| Id | Zadanie | Rola | Zależy od | Kryterium odbioru |
| --- | --- | --- | --- | --- |
| T-020 | Szkielet PWA, przechowywanie w IndexedDB, eksport i import pliku | W | T-011 | Utwór, biblioteka i wydarzenie przetrwają eksport → import bez zmian (test) |
| T-021 | Biblioteka: lista, wyszukiwanie, edytor utworu z podglądem stron | W | T-020 | Testy e2e w przeglądarce; macierz ekranów 360–1920 px |
| T-022 | Edytor wydarzenia: wybór z bibliotek, kolejność, blokada | W | T-021 | Testy e2e |
| T-023 | Widok prezentacji lokalnej (rzutnik bez sieci): pełny ekran, sterowanie klawiaturą i pilotem | W | T-022 | Test e2e; ręczny test na rzutniku (O) |

### Etap 3: tryb na żywo

| Id | Zadanie | Rola | Zależy od | Kryterium odbioru |
| --- | --- | --- | --- | --- |
| T-030 | SPEC-002 Protokół na żywo (stany, `rev`, tokeny, wygasanie, limity) | P, R | T-002 | Specyfikacja z przypadkami brzegowymi (spóźniony uczestnik, zerwanie, zmiana listy) |
| T-031 | Serwer pokoju (Durable Object): tworzenie, dołączanie, rozsyłanie stanu, koniec, czyszczenie | W | T-030 | Testy integracyjne lokalnie (Wrangler) |
| T-032 | Klient prowadzącego: start, kod i QR, sterowanie, wygaszenie, koniec | W | T-031, T-023 | Test e2e z prowadzącym i 3 uczestnikami |
| T-033 | Klient uczestnika: dołączenie, na żywo ↔ przeglądanie, wskaźnik „na żywo”, ponowne łączenie | W | T-031 | Test e2e: zerwanie i powrót; spóźnione dołączenie |
| T-034 | Widok rzutnika podążający za trybem na żywo | W | T-032 | Test e2e |
| T-035 | Bezpieczeństwo: token prowadzącego, limit prób kodu, wygasanie, usuwanie danych | W, R | T-031 | Testy negatywne (próba sterowania bez tokenu, zgadywanie kodów) |
| T-036 | Test obciążeniowy: 300 symulowanych uczestników | W | T-033 | Opóźnienie ≤ 1 s dla 95% (N-01); koszt testu zapisany |

### Etap 4: wydanie pilotażowe

| Id | Zadanie | Rola | Zależy od | Kryterium odbioru |
| --- | --- | --- | --- | --- |
| T-040 | Wdrożenie: Cloudflare Pages + Workers, domena, środowisko testowe i produkcyjne, wdrożenie z CI po zatwierdzeniu Ownera | W, O | T-035 | Działa na domenie; wdrożenie odtwarzalne z repo |
| T-041 | Polityka prywatności i informacja o prawach do tekstów; adres do zgłoszeń | P, O | T-040 | Strony opublikowane po akceptacji Ownera |
| T-042 | Pilotaż na prawdziwym wydarzeniu; ankieta po wydarzeniu; zgłoszone problemy jako zadania | O | T-040, T-041 | Raport z pilotażu w `docs/` |
| T-043 | Pomiar kosztu na zadanie dla etapów 0–4 (AI-crew) | P | T-042 | Wpis w `metrics/cost-per-task.csv` i podsumowanie |

### Etap 5 (M2, po pilotażu)

| Id | Zadanie |
| --- | --- |
| T-050 | Konta prowadzących (Google), biblioteki w chmurze, synchronizacja; usuwanie konta (ADR o dostawcy) |
| T-051 | Udostępnianie bibliotek, współprowadzący |
| T-052 | Import i eksport ChordPro; łączenie przy imporcie (F-46) |
| T-053 | Akordy dla muzyków (jeśli potrzebne) |
| T-054 | Opakowanie PWA dla Google Play (TWA); ocena iOS |
| T-055 | OpenLyrics (import z OpenLP) |

## 10. Następny krok

1. Odpowiedzi na pytania z sekcji 8. Szczególnie ważne: 1, 2, 4, 5, 9, 10, 14, 15, 17, 18.
2. Owner tworzy puste repozytorium (nazwa i widoczność z pytań 14 i 15) albo zleca to Claude'owi.
3. Wykonanie [TASK-000](../blueprints/spiewnik-live/TASK-000-bootstrap.md) w nowym repo.
4. Wersja 2 tego raportu po odpowiedziach, jako SPEC-000 w nowym repo.

## Źródła

- Repozytoria JeanPaulSzefler (stan z 8.11.2026):
  - `learning_tools`: `authoring/README.md`, decyzje 0002, 0006, 0007;
  - `FOZ-ZOE`: `instrukcja-tworzenia-konspektow.md` (śpiew w strukturze spotkania);
  - `education-games` (sieć lokalna w JvP).
- [Raport AI-crew z 31.10.2026](2026-10-31-efficient-ai-crew-and-repo-setup.md) (struktura repo, role, zasady) i [raport z 7.11.2026, wersja 3.1](2026-11-07-orkiestracja-agentow-i-hosting-v3.md) (Cloudflare, koszty czasu, Godot Web, konta projektu).
- OpenLyrics i OpenLP: [OpenLP: OpenLyrics XML (Launchpad)](https://bugs.launchpad.net/openlp/+bug/745636), [forum OpenLP](https://discuss.openlp.org/d/5240-adding-authors-using-xml). ChordPro: chordpro.org (nie sprawdzałem w tej sesji).
- Prawa autorskie (źródła wtórne, bez rozstrzygnięcia dla Polski):
  - [ZAiKS, umowa licencyjna na wykonania](https://app.zaiks.org.pl/media/v4anjzq3/umowa-licencyjna-na-publiczne-wykonywanie-utworow-podczas-wystepow-estradowych-umowa-stala.pdf);
  - [CCLI: wyświetlanie tekstów](https://support-ccli-us.helpscoutdocs.com/article/945-can-we-display-lyrics-on-screen-or-in-the-background-when-we-stream-or-post-recordings-of-our-services-online);
  - [OpenLP: numery CCLI](https://discuss.openlp.org/d/274-ccli-numbers-should-not-appear-on-non-ccli-licensed-songs).
- Pokoje na żywo:
  - [Cloudflare Durable Objects, cennik](https://developers.cloudflare.com/durable-objects/platform/pricing);
  - [Ably: Durable Objects vs Supabase](https://ably.com/compare/cloudflare-durable-objects-vs-supabase);
  - [Supabase: wstrzymywanie darmowych projektów](https://supabase.com/docs/guides/platform/free-project-pausing).

Ograniczenia: limity darmowych planów (Durable Objects, Supabase Realtime) pochodzą częściowo ze źródeł wtórnych. Kwestie prawne wymagają konsultacji. Szacunki opóźnień i skali to cele projektowe, nie wyniki testów.
