# Zestaw Zenka — Plany/Instrukcje/Regulaminy ochrony

Ten katalog to zestaw materiałów referencyjnych i kodu, na podstawie których agent
**Zenek** (`.claude/agents/zenek.md`) tworzy **Instrukcje ochrony obiektu**, **Plany
ochrony obiektów** i **Regulaminy dla pracowników ochrony** dla firmy ochroniarskiej
(Maxus / MM Service Monitoring / MM Service Security), na podstawie dokumentacji
przetargowej (SWZ + OPZ + Wzór Umowy) lub podpisanej umowy dla danego Zamawiającego.

## Dlaczego to w ogóle działa tutaj, a nie w oryginalnym Projekcie na claude.ai

Pierwsza wersja tego zestawu była wgrywana jako "Wiedza projektu" (Project knowledge)
w zwykłym Projekcie na claude.ai. Okazało się to zawodne z dwóch powodów:

1. **Sekcja "Context" w Projektach Claude wyciąga z wgranych plików tylko czysty
   tekst (RAG), nie zachowuje ich jako prawdziwe pliki binarne.** Efekt: plik
   `reference_verdana.docx` wgrywał się jako niemal pusty (~475 bajtów) — cała
   warstwa wizualna (czcionka, kolory, marginesy) przepadała. Obrazki (.png) w
   ogóle się nie wgrywały jako użyteczna treść.
2. **Zwykły Projekt na claude.ai (bez włączonego uruchamiania kodu) nie potrafi
   sam wygenerować pliku .docx** — może tylko przygotować treść (tekst).

**Claude Code (to środowisko) rozwiązuje oba te problemy**: ma dostęp do
narzędzia Bash, czyli może faktycznie uruchamiać Python, pandoc i LibreOffice,
czytać i zapisywać prawdziwe pliki binarne (w tym obrazy i .docx), i oddać
gotowy, sformatowany plik do pobrania. To jest dokładnie to środowisko, o
którym mówi stare README.txt klientki: *"w rozmowie z Claude, która ma tę
funkcję — tak jak ta, w której to wszystko powstało"*.

## Zawartość katalogu

- `playbook.md` — pełna, **aktualna** wersja standardu (wrzesień 2026). Zawiera
  zarówno finalne zasady, jak i historię konkretnych błędów/poprawek klientki —
  czytać całość przed pierwszym zleceniem, wracać do niej przy każdej wątpliwości.
- `common_blocks.py` — gotowe bloki treści (podstawy prawne, zasady ogólne,
  instrukcje służbowe Rozdziału V, wzory dokumentów Rozdziału VI, wykaz osób) i
  funkcje OOXML (`p_label`, `p_dotline`, `p_center`, `p_section_bar`,
  `add_spacing_after_lists`, ...).
- `opz_duties.py` — literalna lista obowiązków z OPZ Prokuratury Okręgowej w
  Łodzi (pkt 26 lit. a–kk) jako **przykład poprawnie odfiltrowanej listy** — nie
  kopiować 1:1 dla innego Zamawiającego, tylko zastosować tę samą metodę
  filtrowania do jego własnego OPZ.
- `build_reference_doc.py` — buduje `assets/reference_verdana.docx` **od zera
  kodem** (Verdana 10pt, marginesy A4, kolory, stopka z numeracją stron) —
  uruchomić raz na początku pracy nad nowym katalogiem roboczym.
- `build2.py` — składa markdown → `.docx` przez pandoc, w dwóch przebiegach
  (żeby spis treści miał prawdziwe numery stron), z pełnym post-processingiem
  (wyśrodkowanie nagłówków, odstępy po listach). **To jest przykład dla
  Prokuratury Okręgowej w Łodzi** — zawiera dane specyficzne dla tego
  Zamawiającego (`SIGN_NUM`, treść Rozdziału I i IV) oznaczone komentarzami
  "UWAGA (generalizacja)" — przed użyciem dla nowego klienta podmienić te
  fragmenty.
- `sites_example.py` — przykładowa struktura danych 14 obiektów (do wzorowania
  się przy budowie analogicznego pliku dla nowego Zamawiającego).
- `assets/logos_norm/` — prawdziwe logotypy firmowe (Maxus, MM Service
  Monitoring; MM Service Security do uzupełnienia, gdy klientka je dostarczy).
- `make_pozycja_bezpieczna.py`, `make_safety_graphics.py` — **NIE UŻYWAĆ**.
  Stary, zastąpiony standard (własne, generowane skryptem grafiki pierwszej
  pomocy, zestaw 3-elementowy). Celowo nieprzeniesione do tego katalogu —
  aktualny standard (playbook.md, sekcja 7) wymaga 4 grafik wyekstrahowanych z
  najnowszego realnego wzoru klientki, nie własnych rysunków.

## Jak zacząć nowe zlecenie (skrót — pełne zasady w playbook.md)

1. Przeczytać `playbook.md` w całości.
2. Zebrać od Renaty: SWZ + OPZ + Wzór Umowy nowego Zamawiającego (i, jeśli
   istnieje, starą/realnie używaną instrukcję dla tego samego obiektu — dane
   koordynatora, zdjęcie budynku, grafiki pierwszej pomocy trzeba wtedy wziąć
   z niej, nie z placeholderów).
3. Ustalić z Renatą etap sprawy (przetarg w toku / firma wygrała / umowa
   podpisana) — od tego zależy, czy dokument sygnalizuje niepewność, czy nie
   (playbook.md, sekcja 10).
4. Odfiltrować obowiązki z OPZ testem z playbook.md sekcja 3 (posterunek vs.
   administracja Wykonawcy) i zbudować `site`-podobną strukturę danych dla
   nowego obiektu (wzorem `sites_example.py`).
5. Jeśli `assets/reference_verdana.docx` jeszcze nie istnieje w bieżącym
   katalogu roboczym — uruchomić `build_reference_doc.py`.
6. Skopiować/dostosować `build2.py` dla nowego Zamawiającego (podmienić
   `SIGN_NUM`, treść Rozdziału I i IV — patrz komentarze "UWAGA
   (generalizacja)" w kodzie) i uruchomić.
7. **Zweryfikować wynik, nie tylko kod**: rozpakować wygenerowany `.docx`
   (`unzip`), sprawdzić `word/styles.xml`/`word/document.xml`, wyrenderować do
   PDF (`soffice --headless --convert-to pdf`), przejrzeć `pdftotext -layout`
   i przejść przez checklistę z playbook.md sekcja 11.
8. Oddać gotowy plik `.docx` (i PDF do podglądu) Renacie.
