# Śpiewnik na żywo (nazwa robocza): wymagania wstępne, ocena miejsca w repozytoriach i plan dla AI-crew

8 listopada 2026 · **Wersja 1.2 (robocza)** · Zadanie startowe nowego repo: [`blueprints/spiewnik-live/TASK-000-bootstrap.md`](../blueprints/spiewnik-live/TASK-000-bootstrap.md)

> **Wersja 1.1:** dodany [rozdział 11 o OpenLP](#11-openlp-co-już-jest-i-co-można-rozwinąć-jako-wkład). Owner nie znał OpenLP (odpowiedź na pytanie 18).
>
> **Wniosek:** OpenLP pokrywa około połowy wymagań MVP: bibliotekę, listę wydarzenia, rzutnik, akordy, import i podgląd na żywo w sieci lokalnej. Brakuje tego, co w pomyśle najważniejsze dla uczestnika:
>
> - samodzielnego przeglądania z powrotem „na żywo”;
> - dołączania kodem przez internet;
> - tworzenia treści z telefonu.
>
> Dwie pierwsze luki da się w dużej części rozwinąć jako wkład w OpenLP na własnej gałęzi. Trzecia wymaga własnej aplikacji.
>
> **Wersja 1.2:** analiza stron OpenLP (strona, blog, podręcznik) ze źródeł na GitLabie, rozdział 11.6.
>
> - Najważniejsze odkrycie: **własne widoki sceniczne** pozwalają zbudować tryb uczestnika dla bieżącej pieśni (K0) **bez zmian w kodzie OpenLP**.
> - Druga darmowa alternatywa, **Quelea**, ma wbudowaną funkcję „mobile lyrics”. Warto ją porównać w pilotażu.

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
18. ~~Czy sprawdzałeś **OpenLP**?~~ **Odpowiedź Ownera: nie.** Analiza w rozdziale 11. Nowe pytania z niej wynikające to 19–21.
19. Czy na typowym wydarzeniu jest **komputer (Windows, macOS, Linux) podłączony do rzutnika lub telewizora** i **sieć Wi-Fi**, do której mogą dołączyć uczestnicy? OpenLP tego wymaga.
20. Czy prowadzący ma móc prowadzić wydarzenie **wyłącznie z telefonu**, bez komputera?
21. Czy akceptujesz licencję **GPLv3** dla kodu rozwijanego jako wkład w OpenLP (kod pozostaje otwarty, także na własnej gałęzi)?

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

0. **Przed budową czegokolwiek:** pilotaż czystego OpenLP na jednym spotkaniu (rozdział 11.5, krok 1). To zero programowania i szybko pokaże, które luki naprawdę bolą.
1. Odpowiedzi na pytania z sekcji 8. Szczególnie ważne: 1, 2, 4, 5, 9, 10, 14, 15, 17, 19, 20, 21.
2. Owner tworzy puste repozytorium (nazwa i widoczność z pytań 14 i 15) albo zleca to Claude'owi.
3. Wykonanie [TASK-000](../blueprints/spiewnik-live/TASK-000-bootstrap.md) w nowym repo.
4. Wersja 2 tego raportu po odpowiedziach, jako SPEC-000 w nowym repo.

## 11. OpenLP: co już jest i co można rozwinąć jako wkład

Stan na 8 listopada 2026. Źródło: kod pobrany z GitLaba:

- `openlp/openlp` @ `19743f9` (22.10.2026);
- `openlp/web-remote` @ `715abba` (3.10.2026);
- `openlp/web-sync`;
- lista otwartych merge requestów przez API GitLaba.

Strony openlp.org i manual.openlp.org były zablokowane w tej sesji, więc ocena opiera się na kodzie, a nie na podręczniku.

### 11.1. Czym jest OpenLP

- **Darmowy program do wyświetlania pieśni i tekstów** w kościołach. Działa jako aplikacja na komputerze: Windows, macOS, Linux; Python i Qt (PySide6 w wersji 4).
- **Licencja GPLv3 lub nowsza.** Kod i wkłady pozostają otwarte.
- **Projekt jest aktywny.** Wydanie 3.1.2; commity i merge requesty z października i listopada 2026; nowa wersja 4 w przygotowaniu. Część merge requestów czeka jednak latami, np. „remote-sync” od 2019 r.
- **Wtyczki:** pieśni, biblia, slajdy własne, obrazy, multimedia, prezentacje, ogłoszenia, statystyki użycia pieśni, Planning Center, OBS Studio.
- **Zdalny panel webowy** (`openlp/web-remote`, Angular, GPLv3). Serwuje go sam OpenLP w sieci lokalnej: port 4316 (HTTP) i 4317 (WebSocket). Widoki:
  - główny: kopia ekranu na żywo;
  - **sceniczny**: bieżący i następny slajd, dla śpiewaków;
  - **akordy**;
  - slajdy, lista wydarzenia, wyszukiwanie, ogłoszenia, motywy, ustawienia.
- **Polskie tłumaczenie** interfejsu jest (`resources/i18n/pl.ts`).

### 11.2. Pokrycie wymagań z sekcji 2

Oznaczenia: ✓ jest, ◐ częściowo, ✗ brak.

| Id | Wymaganie | OpenLP | Uwagi |
| --- | --- | --- | --- |
| F-01 | Utwór, strony, sekcje, kolejność | ✓ | Etykiety zwrotek i refrenu, kolejność wykonania. Edycja tylko w programie na komputerze |
| F-02 | Metadane, prawa | ✓ | Autorzy, śpiewnik z numerem, tematy, prawa autorskie, numer CCLI |
| F-03 | Biblioteka, wyszukiwanie | ◐ | Jedna baza pieśni na instalację; podział przez „śpiewniki” i tematy zamiast wielu bibliotek |
| F-04 | Utwór od razu na żywo | ✓ | „Wyślij na żywo” z biblioteki, także z panelu webowego |
| F-05 | Podgląd | ✓ | Panel podglądu obok panelu na żywo |
| F-06 | Akordy dla muzyków | ✓ | Akordy w tekście, widok akordów w panelu webowym, transpozycja przez API |
| F-10 | Wydarzenie z kolejnością | ✓ | „Service” (plik `.osz`), dowolna kolejność |
| F-11 | Lista zamknięta, zmiany przez prowadzącego w trakcie | ✓ | Zmienia tylko operator, w programie albo z panelu po zalogowaniu |
| F-13 | Kilku prowadzących | ◐ | Kilka osób może sterować z panelu webowego po zalogowaniu |
| F-20 | Kod i QR dla uczestników | ◐ | Adres i kod QR panelu są **w ustawieniach** programu; brak kodu wydarzenia i QR na ekranie dla sali |
| F-21 | Dołączenie bez instalacji i konta | ◐ | **Tylko w tej samej sieci Wi-Fi**: przeglądarka → adres komputera. Przez internet brak (wymaga przekierowania portów lub tunelu) |
| F-22 | Sterowanie, wygaszenie, koniec | ✓ | Mocna strona programu, także pilotem do prezentacji |
| F-23, F-24 | Zmiana w około 1 s, spóźniony widzi stan | ✓ | WebSocket w sieci lokalnej |
| F-25 | Ponowne łączenie | ◐ | Do sprawdzenia w praktyce |
| F-26 | Rzutnik | ✓ | **Najmocniejsza strona:** motywy, tła, wiele ekranów |
| F-27, F-28 | Liczba uczestników, interakcje | ✗ | Ogłoszenia działają tylko od operatora na ekran |
| **F-30–F-32** | **Przeglądanie z powrotem „na żywo”** | ✗ | **Główna luka.** Widoki panelu tylko podążają za ekranem. Kliknięcie pozycji listy **zmienia ekran na żywo** (to sterowanie). API zwraca treść tylko bieżącej pozycji na żywo, nie innych pozycji listy |
| F-33 | Przegląd całej biblioteki przez uczestnika | ✗ | Wyszukiwanie zwraca tytuły do wysłania na żywo, nie tekst do czytania |
| F-34 | Czytelność (czcionka, ciemny tryb) | ◐ | Ustawienia widoku scenicznego; brak ustawień „uczestnika” |
| F-40 | Eksport i import natywny | ◐ | Pieśni: OpenLyrics (XML, eksport i import). Wydarzenie: plik `.osz` |
| F-42 | Standard pliku i instrukcja dla AI | ◐ | **OpenLyrics to udokumentowany standard XML**, który agent AI może edytować. Brak instrukcji dla agenta (możemy ją napisać) |
| F-43 | Import czystego tekstu | ◐ | Wklejenie do edytora ze znacznikami zwrotek; import dokumentów (OpenOffice, Word) |
| F-44 | ChordPro | ◐ | **Import jest, eksportu brak** |
| F-45 | OpenLyrics | ✓ | Import i eksport; około 30 importerów innych programów (ProPresenter, EasyWorship, OpenSong, SongBeamer, CCLI i inne) |
| F-46 | Łączenie przy imporcie | ◐ | Narzędzie do wyszukiwania duplikatów pieśni |
| F-50 | Bez kont | ✓ | Wszystko lokalnie |
| F-51, F-52 | Konta, chmura, udostępnianie bibliotek | ✗ | MR „remote-sync” (synchronizacja pieśni przez folder lub serwer `web-sync`, MIT) **otwarty od 2019 r.**; import z Planning Center (usługa komercyjna); nowy MR integracji z chmurą ConcertAmi (7.11.2026) |
| F-54 | Uczestnicy bez kont i danych | ✓ | — |
| — | Tworzenie i edycja treści z telefonu lub przeglądarki | ✗ | Panel webowy steruje, ale nie edytuje pieśni |
| — | Prowadzenie wyłącznie z telefonu | ✗ | Program musi działać na komputerze; telefon może być tylko pilotem |
| N-03 | Słaby internet | **✓ w innym sensie** | Model sieci lokalnej **w ogóle nie potrzebuje internetu**, wystarczy router Wi-Fi w sali. Brak pamięci podręcznej treści u uczestnika |
| N-07 | Bezpieczeństwo sterowania | ◐ | Logowanie do sterowania jest **domyślnie wyłączone** (wszyscy w Wi-Fi mogą sterować); domyślny login i hasło to `openlp` / `password`. Trzeba włączyć i zmienić |

**Bilans dla 32 pozycji powyżej:** ✓ 14, ◐ 12, ✗ 6. Jest albo częściowo jest **około 80%** (w pełni około 45%), ale braki dotyczą akurat **wyróżnika pomysłu**: samodzielnego przeglądania uczestnika z powrotem „na żywo”, dołączania przez internet i tworzenia treści z telefonu.

### 11.3. Co można rozwinąć jako wkład w OpenLP (własna gałąź)

| Id | Wkład | Repo OpenLP | Rozmiar | Szansa przyjęcia | Zamyka |
| --- | --- | --- | --- | --- | --- |
| **K0** | **Własny widok sceniczny „uczestnik”** (HTML, CSS, JS w folderze danych `stages/uczestnik`, adres `http://<ip>:4316/stage/uczestnik`). Podąża za bieżącą pozycją na żywo; pozwala przewijać jej strony samodzielnie, z przyciskiem „Wróć na żywo”; czcionka i tryb ciemny. **Bez zmian w OpenLP** (mechanizm z podręcznika, rozdział 11.6) | Brak: osobna paczka zip, np. dodatek społeczności lub wpis w wiki | **S** | Nie wymaga przyjęcia; można udostępnić społeczności | F-30, F-32, F-34 (w obrębie **bieżącego** utworu) |
| K1 | **Tryb uczestnika** w panelu webowym: widok tylko do odczytu, który podąża za ekranem; uczestnik przewija strony samodzielnie, widzi wskaźnik „na żywo jest…” i przycisk „Wróć na żywo”; czcionka i tryb ciemny; ukryte sterowanie | `web-remote` (Angular, TypeScript) | S–M | Wysoka: częsta potrzeba w kościołach, bez zmian w rdzeniu | F-30, F-32, F-34 |
| K2 | **Punkt API tylko do odczytu**: treść dowolnej pozycji listy wydarzenia bez wysyłania jej na żywo, z ustawieniem „pozwól uczestnikom przeglądać listę” | `openlp` (Python, Flask, testy pytest) | S | Średnio-wysoka; trzeba uzgodnić prywatność (notatki operatora) | F-31; warunek pełnego K1 |
| K3 | **Kod QR i adres dla sali na ekranie** (nakładka na początku wydarzenia) | `openlp` (Qt) | S–M | Wysoka | F-20 |
| K4 | **Pamięć podręczna treści u uczestnika** (PWA): przegląd działa przy chwilowym zerwaniu Wi-Fi | `web-remote` | M | Średnia | N-03 |
| K5 | **Eksport ChordPro** (import już jest); ewentualnie instrukcja dla agenta AI do OpenLyrics w dokumentacji | `openlp` (songs) i `documentation` | S–M | Średnia | F-44, F-42 |
| K6 | **Dostęp przez internet:** dodatek OpenLP, który wysyła stan na żywo i treść wydarzenia do zewnętrznego pośrednika, oraz pośrednik z kodem wydarzenia | Dodatek (addon) OpenLP + **własna usługa** (np. pokój Durable Object z sekcji 5) | L | Jako dodatek społeczności: tak (tak dystrybuowany jest np. ConcertAmi); w rdzeniu raczej nie | F-20, F-21 przez internet |
| K7 | **Ożywienie MR „remote-sync”** (biblioteki współdzielone przez serwer `web-sync`) | `openlp` + `web-sync` | L | Niepewna: MR od 2019 r., trzeba uzgodnić z autorem (tgc-dk) | F-51, F-52 |

**Jak pracować na własnej gałęzi:**

- **Gdzie:** fork na GitLabie (wymaga konta GitLab Ownera), gałąź np. `participant-mode`.
  - AI-crew pracuje na GitHubie, więc wygodniej trzymać **prywatne lustro na GitHubie** do pracy agentów i CI, a merge request zgłaszać na GitLabie.
  - GitHub Actions (`claude-code-action`) nie działa bezpośrednio na GitLabie.
- **Używanie przed przyjęciem do OpenLP:**
  - Panel webowy instaluje się jako paczka zip w folderze danych `remotes`. Własną wersję K1 można więc wgrać ręcznie na swój komputer **bez czekania na przyjęcie**. Do sprawdzenia: wyłączenie automatycznej aktualizacji panelu, żeby nie nadpisała własnej wersji.
  - Zmiany w rdzeniu (K2, K3) wymagają uruchomienia OpenLP z własnego kodu źródłowego albo przyjęcia do OpenLP.
- **Przed pierwszym merge requestem:** zgłoszenie (issue) lub rozmowa z opiekunami projektu (forum, czat), żeby ustalić kierunek. Wymogu podpisania umowy CLA w repo nie znalazłem; do potwierdzenia w wiki.
- **Licencja:** wkłady w OpenLP i panel webowy na GPLv3. Własna usługa pośrednicząca (K6), która rozmawia z OpenLP przez sieć, może mieć osobną licencję (np. MIT). Do potwierdzenia, jeśli miałaby zawierać kod OpenLP.

### 11.4. Co zostaje poza OpenLP

| Potrzeba | Dlaczego nie OpenLP |
| --- | --- |
| Prowadzenie wydarzenia **wyłącznie z telefonu** | OpenLP to program na komputer |
| **Tworzenie i edycja** śpiewników na telefonie lub w przeglądarce przez wielu użytkowników | Edycja tylko w programie na komputerze; brak kont |
| **Dołączanie przez internet bez wspólnej sieci Wi-Fi** | Tylko przez K6 (dodatek + własny pośrednik) albo własną aplikację |
| Interakcje jak w Kahoot (głosowania, prośby) | Poza modelem programu |
| Plik JSON „wszystko w jednym” (utwory + biblioteki + wydarzenia) | OpenLP ma OpenLyrics (pieśni) i `.osz` (wydarzenia). Można zostać przy nich i dopisać instrukcję dla AI |

### 11.5. Rekomendacja: najpierw OpenLP, własna aplikacja tylko na brakujące elementy

1. **Pilotaż bez programowania** (1 spotkanie):
   - OpenLP na laptopie z rzutnikiem albo telewizorem;
   - router Wi-Fi w sali;
   - uczestnicy otwierają widok sceniczny lub główny w przeglądarce telefonu;
   - **koniecznie włączyć logowanie do sterowania** i zmienić domyślne hasło;
   - import kilku pieśni z OpenLyrics lub ChordPro.
   
   Wynik: lista luk, które naprawdę przeszkadzają.
2. **Jeśli brakuje głównie przeglądania przez uczestnika:** najpierw **K0** (własny widok sceniczny, bez zmian w OpenLP, kilka dni pracy). Potem, jeśli uczestnicy chcą przeglądać także inne pieśni z listy, **K1 + K2** jako wkład w OpenLP na własnej gałęzi. Mały zakres, prawdziwi użytkownicy i niezależna recenzja opiekunów OpenLP. To dobry **pilotaż AI-crew**, z kosztem na zadanie mierzonym jak w sekcji 9.
3. **Jeśli potrzebne jest dołączanie przez internet:** K6. Pośrednik to w praktyce serwer pokoju z sekcji 5 (T-030, T-031). Można go zbudować raz i użyć zarówno jako dodatku do OpenLP, jak i w ewentualnej własnej aplikacji.
4. **Własna aplikacja `spiewnik-live`** (sekcje 2–9) tylko wtedy, gdy kluczowe jest prowadzenie z samego telefonu, tworzenie treści na telefonie albo konta i chmura dla wielu wspólnot (pytania 5, 19, 20).

**Zmiana w planie zadań przy ścieżce OpenLP** (zastępuje etapy 1–3 sekcji 9, jeśli Owner ją wybierze):

| Id | Zadanie | Rola | Kryterium odbioru |
| --- | --- | --- | --- |
| O-001 | Pilotaż czystego OpenLP na jednym spotkaniu; lista luk | O | Notatka w `docs/` z lukami w kolejności ważności |
| O-005 | **K0: własny widok sceniczny „uczestnik”** (HTML, CSS, JS; WebSocket 4317 i `/api/v2/controller/live-items`), testy e2e z atrapą API, instrukcja instalacji w folderze `stages` | W, R | Na niezmienionym OpenLP 3.1.x uczestnik przewija strony bieżącej pieśni bez wpływu na ekran i wraca „na żywo”; macierz ekranów 360–1920 px |
| O-002 | Fork `openlp` i `web-remote` na GitLabie; prywatne lustro na GitHubie z CI; uruchomienie OpenLP z kodu i panelu w trybie deweloperskim | O (konta), W | Zbudowany panel webowy; testy (`pytest`, `vitest`) zielone na forku |
| O-003 | Zgłoszenie (issue) u opiekunów OpenLP z propozycją K1 + K2 | P, O | Odpowiedź opiekunów albo decyzja o pracy tylko na własnej gałęzi |
| O-010 | K2: punkt API tylko do odczytu + testy | W, R | Testy pytest; brak zmiany zachowania dla istniejących klientów |
| O-011 | K1: tryb uczestnika w `web-remote` + testy e2e (Playwright) | W, R | Uczestnik przegląda strony bez zmiany ekranu; „Wróć na żywo” działa; macierz ekranów |
| O-012 | Ręczne wdrożenie własnego panelu w folderze `remotes` i drugi pilotaż | O, W | Notatka z pilotażu |
| O-013 | Merge requesty do OpenLP (K2, potem K1) | W, O | MR zgłoszone; uwagi opiekunów jako zadania |
| O-020 | K3: kod QR na ekranie | W, R | Test i pilotaż |
| O-030 | Decyzja: K6 (pośrednik) czy własna aplikacja | P, O | ADR z uzasadnieniem po pilotażach |

### 11.6. Co mówią strony OpenLP (strona, blog, podręcznik)

Stan na 8 listopada 2026.

Pierwsza prośba o dostęp do openlp.org, podręcznika, wiki i forum została odrzucona; za drugim razem Owner dostęp przyznał. Najpierw przeanalizowałem strony **ze źródeł na GitLabie**, a potem uzupełniłem je o strony na żywo:

- `openlp/website` @ `c3551bd` (15.09.2026): źródło openlp.org, strony i 324 wpisy bloga;
- `openlp/documentation` @ `87986e9` (6.01.2026): źródło podręcznika manual.openlp.org;
- wyszukiwarka dla forum.

Repozytorium `openlp/wiki` wymaga logowania przy klonowaniu, ale jego strony są publiczne przez API GitLaba (dalej).

**Uzupełnienie po przyznaniu dostępu do stron OpenLP (8.11.2026):**

- **Panel webowy jest nowszy niż w blogu:** serwer aktualizacji `get.openlp.org` podaje **wersję 1.3.1** (paczka `remote-1.3.1.zip`, 2,2 MB).
- **Strona główna** (openlp.org): „sterowanie OpenLP z przeglądarki telefonu”, „import pieśni z innych popularnych programów”, Windows, Linux, macOS i FreeBSD, bez abonamentu. Funkcji dla uczestników na telefonach nie wymienia.
- **Wiki** (wiki.openlp.org przekierowuje do wiki projektu na GitLabie; 115 stron, czytane przez API):
  - **Custom Stage Views** potwierdza mechanizm K0: folder `stages/<nazwa>/stage.html`, adres `/stage/<nazwa>/`. Stan pobiera się przez WebSocket, a dane przez HTTP API v2.
  - **WebSockets** (port 4317): stan zawiera licznik zmian ekranu (`counter`), licznik zmian listy (`service`), identyfikator bieżącej pozycji (`item`), wygaszenie, motyw i notację akordów. Wystarcza do trybu „podążaj za ekranem” i wskaźnika „na żywo jest…”.
  - **Ważne ograniczenie** (HTTP API i WebSockets): „serwer OpenLP jest dostępny tylko w sieci lokalnej, nie wykonuje przekierowania portów i **nie jest przystosowany do dużego obciążenia**; nie zaleca się wystawiania go do internetu”. Konsekwencje:
    - dla dużych wydarzeń (pytanie 1, N-02) OpenLP w sieci lokalnej może być wąskim gardłem; potrzebny test obciążenia;
    - pośrednik K6 powinien **kopiować stan raz i rozsyłać go sam**, a nie przekazywać ruchu uczestników do OpenLP.
  - **Zasady wkładu** (Development/Workflow):
    - fork na GitLabie i merge request;
    - **każdy merge musi zawierać co najmniej jeden test**;
    - pokrycie testami około 65%;
    - nacisk na TDD.
    
    Pasuje to do zasady AI-crew „testy są sędzią”. Wymogu umowy CLA nie znalazłem.
  - **Releases/v4-Beta:** lista otwartych spraw przed wersją 4.0. Zaplanowane wydanie testowe 4.0a1; do zrobienia m.in. „Test Web Remote” i przeniesienie plików do pobrania. Wkład w panel webowy warto zgrać z wersją 4.
- **Forum** (discuss.openlp.org): wątek [„Is there a way to connect/cast to people's tablet or phone?”](https://discuss.openlp.org/d/2869-is-there-a-way-to-connectcast-to-peoples-tablet-or-phone). Użytkownicy pokazują tekst na telefonach uczestników przez widok główny w sieci lokalnej, a zgłaszane problemy dotyczyły opóźnień przy słabym Wi-Fi (wersja 2.x, odświeżanie co 0,5 s). Potrzeba istnieje, ale jest obsługiwana „przy okazji” widoku dla operatora. Kilka wątków o własnych widokach scenicznych (akordy, OBS, wygaszanie) potwierdza, że ta droga jest w społeczności znana.

**Stan projektu (blog i strony):**

- Ostatnie wydanie stabilne to **3.1.7 „Pondering Perez”** (16.02.2025). Wpis mówi: „prace nad OpenLP 4.0 trwają”. Gałąź `master` z października 2026 to już 4.0 (PySide6).
- **Web Remote 1.2.3** (24.03.2025): ustawienie blokujące wygaszanie ekranu telefonu (wake lock) na Androidzie i iOS. Przydaje się uczestnikom czytającym tekst z telefonu.
- **3.1.0** (29.02.2024):
  - **dodatki społeczności** („community plugins”), czyli własne wtyczki bez wchodzenia do rdzenia OpenLP;
  - blokada przed jednoczesnym użyciem z kilku miejsc. Według bloga to rozwiązanie tymczasowe „do czasu lepszego mechanizmu współdzielenia danych”. Współdzielenie bibliotek jest więc znaną, otwartą potrzebą (por. K7).
- **Mały zespół, ograniczone zasoby:**
  - strona „Contribute” wprost prosi o programistów Pythona (rdzeń), Angulara (panel webowy), Swifta (aplikacja na iOS) i Javy (Android);
  - około 5 zgłoszeń wsparcia dziennie i mało osób, które na nie odpowiadają;
  - strona „Donate”: projekt nie ma przychodów i jest finansowany z prywatnych środków programistów.
  
  Wniosek: wkład jest mile widziany, ale przegląd merge requestów może trwać długo.
- Wiki dla współtwórców jest na GitLabie (`gitlab.com/openlp/wiki`).

**Podręcznik (manual):**

- **Panel webowy** steruje listą i slajdami, wygaszaniem, motywem i pulpitem; wyszukuje i dodaje pozycje; wysyła ogłoszenia. „Kliknięcie dowolnej pozycji listy natychmiast przenosi do sterowania slajdami”. Potwierdza to brak przeglądania bez wpływu na ekran.
- **Widok sceniczny** (`/stage`): czytelny tekst na czarnym tle, zegar, notatki do pieśni, numery zwrotek z podświetleniem bieżącej, następna pozycja. Wymaga tej samej sieci. **Notatki operatora są widoczne w widoku scenicznym**, więc udostępniając go uczestnikom, trzeba pilnować treści notatek.
- **Własne widoki sceniczne**: folder `stages/<nazwa>` w folderze danych OpenLP, własne `stage.html`, `stage.css`, `stages.js` (szablon z wiki), adres `http://<ip>:4316/stage/<nazwa>`. **To umożliwia K0**: tryb uczestnika bez zmiany kodu OpenLP. Forum potwierdza, że użytkownicy tworzą własne, responsywne widoki sceniczne.
- **Widok główny** (`/main`) pokazuje zrzuty ekranu rzutnika (bez wideo). **Widok akordów** (`/chords`) ma transpozycję.
- **Aplikacja OpenLP Remote na iOS** (App Store) to pilot dla operatora, w tej samej sieci; nie służy uczestnikom.
- **Sieć:** podręcznik wielokrotnie podkreśla, że urządzenia muszą być **w tej samej sieci**. O dostępie przez internet nie ma ani słowa. Potwierdza to lukę F-21 i sens K6.
- **Eksport pieśni:** tylko **OpenLyrics**, jeden plik na pieśń (100 pieśni to 100 plików). Eksport ChordPro nie jest opisany. Potwierdza to K5 i potrzebę konwertera „wiele pieśni ↔ jeden plik” dla pracy z agentem AI.
- Logowanie do sterowania jest opisane jako opcja (`user_auth`), a nie domyślne zabezpieczenie.

**Inna darmowa alternatywa: Quelea** (Java, GPLv3, Windows, macOS, Linux). Według opisów projektu ma funkcję **„mobile lyrics”**: wysyłanie tekstu na żywo do telefonów uczestników przez przeglądarkę, z własnymi kolorami. Ma też widok sceniczny z akordami dla zespołu i aplikację pilota. Nie sprawdzałem jej kodu ani dokumentacji (źródła wtórne). Warto ją porównać z OpenLP w pilotażu (O-001), bo „mobile lyrics” to dokładnie widok uczestnika. Nie wiadomo jednak, czy ma przeglądanie z powrotem „na żywo”.

**Wpływ na rekomendację:** mechanizm własnych widoków scenicznych **obniża koszt pierwszego kroku**. Tryb uczestnika dla bieżącej pieśni (K0) można zbudować i używać na niezmienionym OpenLP 3.1.x, bez forka i bez czekania na opiekunów. Fork i merge requesty (K1, K2) są potrzebne dopiero do przeglądania innych pieśni z listy.

## Źródła

- Repozytoria JeanPaulSzefler (stan z 8.11.2026):
  - `learning_tools`: `authoring/README.md`, decyzje 0002, 0006, 0007;
  - `FOZ-ZOE`: `instrukcja-tworzenia-konspektow.md` (śpiew w strukturze spotkania);
  - `education-games` (sieć lokalna w JvP).
- [Raport AI-crew z 31.10.2026](2026-10-31-efficient-ai-crew-and-repo-setup.md) (struktura repo, role, zasady) i [raport z 7.11.2026, wersja 3.1](2026-11-07-orkiestracja-agentow-i-hosting-v3.md) (Cloudflare, koszty czasu, Godot Web, konta projektu).
- OpenLyrics i OpenLP: [OpenLP: OpenLyrics XML (Launchpad)](https://bugs.launchpad.net/openlp/+bug/745636), [forum OpenLP](https://discuss.openlp.org/d/5240-adding-authors-using-xml). ChordPro: chordpro.org (nie sprawdzałem w tej sesji).
- Kod OpenLP (rozdział 11), sprawdzony 8.11.2026:
  - [openlp/openlp](https://gitlab.com/openlp/openlp) @ `19743f9`: `LICENSE` (GPLv3), `CHANGELOG.rst` (3.1.2), `openlp/core/api/versions/v2/` (punkty API, `login_required`), `openlp/core/api/tab.py` (adres i QR w ustawieniach), `openlp/core/api/deploy.py` (instalacja panelu jako zip), `openlp/core/common/settings.py` (porty 4316 i 4317, logowanie domyślnie wyłączone), `openlp/plugins/songs/lib/importers/` (około 30 importerów, m.in. ChordPro i OpenLyrics);
  - [openlp/web-remote](https://gitlab.com/openlp/web-remote) @ `715abba`: widoki main, stage, chords, slides, service, search;
  - [openlp/web-sync](https://gitlab.com/openlp/web-sync) (MIT);
  - [MR !9 remote-sync](https://gitlab.com/openlp/openlp/-/merge_requests/9), [MR !944 ConcertAmi](https://gitlab.com/openlp/openlp/-/merge_requests/944).
- Strony OpenLP ze źródeł (rozdział 11.6):
  - [openlp/website](https://gitlab.com/openlp/website) @ `c3551bd`: `pages/contribute.rst`, `pages/donate.rst`, blog (3.1.0, 3.1.7, Web Remote 1.2.3);
  - [openlp/documentation](https://gitlab.com/openlp/documentation) @ `87986e9`: `manual/source/web_remote.rst`, `stage_view.rst` (własne widoki sceniczne), `ios-remote.rst`, `configure.rst` (ta sama sieć), `export_songs.rst`.
- Forum i Quelea (źródła wtórne):
  - [OpenLP: własny widok sceniczny](https://discuss.openlp.org/d/3266-custom-stage-view-layout-i-made), [notatki w widoku scenicznym](https://discuss.openlp.org/d/3450-notes-stage-view);
  - [Quelea, SourceForge](https://sourceforge.net/p/quelea/), [Quelea w ToolRadar](https://toolradar.com/tools/quelea), [Quelea vs OpenLP](https://toolradar.com/compare/quelea-vs-openlp).
- Prawa autorskie (źródła wtórne, bez rozstrzygnięcia dla Polski):
  - [ZAiKS, umowa licencyjna na wykonania](https://app.zaiks.org.pl/media/v4anjzq3/umowa-licencyjna-na-publiczne-wykonywanie-utworow-podczas-wystepow-estradowych-umowa-stala.pdf);
  - [CCLI: wyświetlanie tekstów](https://support-ccli-us.helpscoutdocs.com/article/945-can-we-display-lyrics-on-screen-or-in-the-background-when-we-stream-or-post-recordings-of-our-services-online);
  - [OpenLP: numery CCLI](https://discuss.openlp.org/d/274-ccli-numbers-should-not-appear-on-non-ccli-licensed-songs).
- Pokoje na żywo:
  - [Cloudflare Durable Objects, cennik](https://developers.cloudflare.com/durable-objects/platform/pricing);
  - [Ably: Durable Objects vs Supabase](https://ably.com/compare/cloudflare-durable-objects-vs-supabase);
  - [Supabase: wstrzymywanie darmowych projektów](https://supabase.com/docs/guides/platform/free-project-pausing).

Ograniczenia: limity darmowych planów (Durable Objects, Supabase Realtime) pochodzą częściowo ze źródeł wtórnych. Kwestie prawne wymagają konsultacji. Szacunki opóźnień i skali to cele projektowe, nie wyniki testów.
