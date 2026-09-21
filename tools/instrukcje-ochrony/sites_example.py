# -*- coding: utf-8 -*-
#
# PRZYKLAD struktury danych obiektow (14 jednostek Prokuratury Okregowej w
# Lodzi) - patrz playbook.md. Dla NOWEGO Zamawiajacego przygotowac analogiczny
# plik `sites.py` (ta sama struktura kluczy w kazdym slowniku site), ale z
# danymi wyciagnietymi z NOWEGO SWZ/OPZ/Wzoru Umowy - nie kopiowac tresci
# ponizej dla innego klienta.
#
# Znaczenie pol kazdego "site":
#   nr              - numer porzadkowy obiektu w tym zleceniu
#   slug             - unikalny identyfikator pliku (bez polskich znakow/spacji)
#   nazwa            - pelna nazwa jednostki (WERSALIKI na okladce)
#   adres            - adres obiektu
#   charakter        - opis charakteru obiektu (Rozdzial II)
#   systemy_techniczne - lista zainstalowanych systemow (SSWiN/CCTV/SKD/...)
#   dozor_parkingu   - opis dozorowanego parkingu, albo None jesli brak
#   rtg              - True/False: czy obiekt ma skaner RTG (wplywa na OPZ pkt "r"
#                      i na Rozdzial II)
#   alarm_duty       - True/False: czy pracownik ochrony sam uzbraja/rozbraja alarm
#                      (wplywa na OPZ pkt "kk")
#   ppoz_bezposrednie - True/False: czy SSP jest bezposrednio podlaczony do
#                      Strazy Pozarnej (wplywa na Rozdzial II)
#   caladobowa       - True/False: czy na obiekcie jest posterunek calodobowy
#                      (wplywa na OPZ pkt "b"/obchody nocne)
#   dodatkowe_uwagi  - lista zdan (NIGDY z etykieta "Uwaga szczegolowa:") -
#                      dodatkowe informacje przy tabeli obsady
#   tabela_obsady    - gotowa tabela markdown (pipe table) z obsada posterunkow,
#                      konwertowana pozniej na liste punktowana przez
#                      table_to_bullets() w build2.py

SITES = [

# 1 ------------------------------------------------------------------------
{
"nr": 1,
"slug": "01_Prokuratura_Okregowa_w_Lodzi",
"nazwa": "PROKURATURA OKRĘGOWA W ŁODZI",
"adres": "ul. Kilińskiego 152, 90-322 Łódź",
"charakter": (
"Siedziba główna Prokuratury Okręgowej w Łodzi – Zamawiającego. Budynek administracji "
"publicznej / wymiaru sprawiedliwości o podwyższonym priorytecie bezpieczeństwa, w którym "
"na co dzień przebywają prokuratorzy, pracownicy administracyjni oraz interesanci. "
"Obiekt sąsiaduje z parkingiem zlokalizowanym przy zbiegu ulic Kilińskiego i Wigury, "
"podlegającym dozorowi w ramach niniejszej Instrukcji."
),
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": "Parking przy zbiegu ulic Kilińskiego i Wigury – dozorowany całodobowo przez pracownika monitoringu oraz kontrolowany w ramach obchodów.",
"rtg": False,
"alarm_duty": False,
"ppoz_bezposrednie": False,
"caladobowa": True,
"dodatkowe_uwagi": [
 "Obiekt wyposażony w bramkę do wykrywania metali oraz skaner bagażu – obsługiwane przez pracownika ochrony na wejściu głównym.",
 "Pracownik monitoringu pełni jednocześnie funkcję koordynującą pozostałe posterunki w godzinach nocnych oraz w dni wolne od pracy.",
],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy | Wymiar tygodniowy |
|---|---|---|---|---|
| Pracownik kwalifikowany nr 1 – wejście główne | pon.–pt. | 7:00–16:00 | 9 h | 45 h |
| Pracownik kwalifikowany nr 2 – wejście | pon.–pt. | 8:00–20:00 | 12 h | 60 h |
| Pracownik niekwalifikowany – wejście | pon.–pt. | 9:00–15:00 | 6 h | – |
| Pracownik niekwalifikowany – dozór parkingu (ten sam pracownik) | pon.–pt. | 7:30–9:00 i 15:00–16:30 | 3 h | 45 h (łącznie z wejściem) |
| Pracownik monitoringu | pon.–niedz. | całodobowo (24 h) | 24 h | 168 h |

**Łączna liczba pracowników ochrony na obiekcie: 4 osoby.**""",
},

# 2 ------------------------------------------------------------------------
{
"nr": 2,
"slug": "02_Archiwum_Zakladowe_Lodz",
"nazwa": "ARCHIWUM ZAKŁADOWE PROKURATURY OKRĘGOWEJ W ŁODZI",
"adres": "ul. Wydawnicza 10, Łódź",
"charakter": (
"Obiekt archiwum zakładowego Prokuratury Okręgowej w Łodzi, w którym przechowywana jest "
"dokumentacja aktowa jednostki. Ochrona pełniona jest w sposób ciągły, całodobowy, "
"z uwagi na brak stałej obsady administracyjnej obiektu w porze pozaurzędowej."
),
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": False,
"ppoz_bezposrednie": False,
"caladobowa": True,
"dodatkowe_uwagi": [
 "Pracownik ochrony wykonuje systematyczne obchody pomieszczeń archiwum, ze szczególnym uwzględnieniem kontroli zabezpieczeń przeciwpożarowych oraz stanu zamknięć pomieszczeń archiwalnych.",
 "W jednostce, w której ochrona pełniona jest całodobowo, obchody wykonywane są nie rzadziej niż 3 razy w porze poza urzędowaniem, tj. ok. godz. 20:00, 24:00 i 04:00, potwierdzone wpisem w Książce Służby.",
],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy | Wymiar tygodniowy |
|---|---|---|---|---|
| Pracownik ochrony | pon.–niedz. | całodobowo (24 h) | 24 h | 168 h |

**Łączna liczba pracowników ochrony na obiekcie: 1 osoba (obsada rotacyjna, zapewniająca ciągłość służby 24/7).**""",
},

# 3 ------------------------------------------------------------------------
{
"nr": 3,
"slug": "03_Prokuratura_Rejonowa_Lodz_Srodmiescie",
"nazwa": "PROKURATURA REJONOWA ŁÓDŹ-ŚRÓDMIEŚCIE",
"adres": "ul. Kilińskiego 152, Łódź (budynek Prokuratury Okręgowej w Łodzi)",
"charakter": (
"Jednostka organizacyjna mieszcząca się w budynku Prokuratury Okręgowej w Łodzi. Ochrona "
"obiektu (wejście, ruch osobowy interesantów) prowadzona jest we współpracy i koordynacji "
"z posterunkami ochrony Prokuratury Okręgowej w Łodzi znajdującymi się w tym samym budynku "
"(vide odrębna Instrukcja ochrony dla Prokuratury Okręgowej w Łodzi)."
),
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": False,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [
 "Z uwagi na wspólną lokalizację z Prokuraturą Okręgową w Łodzi, pracownik ochrony przypisany do niniejszej jednostki współdziała z pozostałymi posterunkami budynku przy ul. Kilińskiego 152, w szczególności w zakresie kontroli ruchu osobowego oraz obsługi wejścia.",
],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | poniedziałek | 7:30–16:30 | 9 h |
| Pracownik ochrony | wtorek | 7:30–17:00 | 9,5 h |
| Pracownik ochrony | środa | 7:30–16:30 | 9 h |
| Pracownik ochrony | czwartek | 7:30–16:30 | 9 h |
| Pracownik ochrony | piątek | 7:30–16:30 | 9 h |

**Wymiar tygodniowy: 45,5 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 4 ------------------------------------------------------------------------
{
"nr": 4,
"slug": "04_Prokuratura_Rejonowa_Lodz_Gorna",
"nazwa": "PROKURATURA REJONOWA ŁÓDŹ-GÓRNA",
"adres": "ul. Sieradzka 11A, Łódź",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości, w którym urzędują prokuratorzy oraz pracownicy administracyjni, przyjmowani są interesanci.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon.–pt. | 8:00–19:00 | 11 h |

**Wymiar tygodniowy: 55 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 5 ------------------------------------------------------------------------
{
"nr": 5,
"slug": "05_Prokuratura_Rejonowa_Lodz_Widzew_Polesie",
"nazwa": "PROKURATURA REJONOWA ŁÓDŹ-WIDZEW ORAZ PROKURATURA REJONOWA ŁÓDŹ-POLESIE",
"adres": "ul. Dąbrowskiego 40a, Łódź",
"charakter": (
"Wspólny kompleks budynkowy, w którym mieszczą się dwie jednostki organizacyjne: Prokuratura "
"Rejonowa Łódź-Widzew oraz Prokuratura Rejonowa Łódź-Polesie. Obiekt posiada dwa odrębne "
"wejścia obsługiwane przez oddzielnych pracowników ochrony oraz jest objęty ochroną "
"całodobową za pośrednictwem posterunku monitoringu."
),
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": "Parking przy ul. Dąbrowskiego 40a – dozorowany, ze sprawdzaniem zezwoleń na parkowanie w miejscach odpowiednio oznakowanych.",
"rtg": False,
"alarm_duty": False,
"ppoz_bezposrednie": False,
"caladobowa": True,
"dodatkowe_uwagi": [
 "Posterunek wejściowy Prokuratury Rejonowej Łódź-Polesie oraz posterunek wejściowy Prokuratury Rejonowej Łódź-Widzew (obsadzony przez pracownika kwalifikowanego) współdziałają z posterunkiem monitoringu w zakresie obserwacji terenu i parkingu.",
 "W jednostce, w której ochrona pełniona jest całodobowo (posterunek monitoringu), obchody terenu wykonywane są nie rzadziej niż 3 razy w porze poza urzędowaniem, tj. ok. godz. 20:00, 24:00 i 04:00.",
],
"tabela_obsady": """| Stanowisko | Dni | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik – wejście Polesie | pon. | 7:00–16:00 | 9 h |
| Pracownik – wejście Polesie | wt. | 7:00–17:00 | 10 h |
| Pracownik – wejście Polesie | śr.–pt. | 7:00–16:00 | 9 h (śr., czw.), 9 h (pt.) |
| Pracownik kwalifikowany – wejście Widzew | pon.–pt. | 8:00–14:00 | 6 h |
| Pracownik monitoringu | pon.–niedz. | całodobowo (24 h) | 24 h |

**Wymiar tygodniowy: wejście Polesie – 46 h, wejście Widzew – 30 h, monitoring – 168 h. Łączna liczba pracowników ochrony na obiekcie: 3 osoby.**""",
},

# 6 ------------------------------------------------------------------------
{
"nr": 6,
"slug": "06_Prokuratura_Rejonowa_w_Pabianicach",
"nazwa": "PROKURATURA REJONOWA W PABIANICACH",
"adres": "ul. Warszawska 39, Pabianice",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system p.poż. podłączony bezpośrednio do Straży Pożarnej",
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": True,
"alarm_duty": True,
"ppoz_bezposrednie": True,
"caladobowa": False,
"dodatkowe_uwagi": [
 "Wykonawca zobowiązany jest przedstawić Zamawiającemu, w terminie 60 dni od dnia podpisania umowy, zezwolenie Prezesa Państwowej Agencji Atomistyki na prowadzenie działalności związanej ze stosowaniem urządzenia wytwarzającego promieniowanie jonizujące w niniejszym obiekcie.",
 "System sygnalizacji pożarowej obiektu podłączony jest bezpośrednio do Straży Pożarnej – w przypadku aktywacji systemu pracownik ochrony niezwłocznie weryfikuje przyczynę alarmu na miejscu zdarzenia.",
],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony nr 1 | pon.–pt. | 9:00–14:00 | 5 h |
| Pracownik ochrony nr 2 | pon.–pt. | 7:30–19:00 | 11,5 h |

**Wymiar tygodniowy: 82,5 h. Łączna liczba pracowników ochrony na obiekcie: 2 osoby.**""",
},

# 7 ------------------------------------------------------------------------
{
"nr": 7,
"slug": "07_Prokuratura_Rejonowa_w_Zgierzu",
"nazwa": "PROKURATURA REJONOWA W ZGIERZU",
"adres": "ul. Łódzka 20, Zgierz",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon.–pt. | 7:00–19:00 | 12 h |

**Wymiar tygodniowy: 60 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 8 ------------------------------------------------------------------------
{
"nr": 8,
"slug": "08_Prokuratura_Rejonowa_Lodz_Baluty",
"nazwa": "PROKURATURA REJONOWA ŁÓDŹ-BAŁUTY",
"adres": "ul. Ciesielska 7, Łódź",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony nr 1 | pon.–pt. | 7:00–15:00 | 8 h |
| Pracownik ochrony nr 2 | pon.–pt. | 10:00–18:00 | 8 h |

**Wymiar tygodniowy: 80 h. Łączna liczba pracowników ochrony na obiekcie: 2 osoby.**""",
},

# 9 ------------------------------------------------------------------------
{
"nr": 9,
"slug": "09_Prokuratura_Rejonowa_w_Kutnie",
"nazwa": "PROKURATURA REJONOWA W KUTNIE",
"adres": "ul. Staszica 3, Kutno",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": False,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon., śr., czw., pt. | 8:00–16:00 | 8 h |
| Pracownik ochrony | wtorek | 8:00–17:00 | 9 h |

**Wymiar tygodniowy: 41 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 10 -----------------------------------------------------------------------
{
"nr": 10,
"slug": "10_Prokuratura_Rejonowa_w_Skierniewicach",
"nazwa": "PROKURATURA REJONOWA W SKIERNIEWICACH",
"adres": "ul. Gałeckiego 4, Skierniewice",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon.–pt. | 7:00–18:00 | 11 h |

**Wymiar tygodniowy: 55 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 11 -----------------------------------------------------------------------
{
"nr": 11,
"slug": "11_Prokuratura_Rejonowa_w_Lowiczu",
"nazwa": "PROKURATURA REJONOWA W ŁOWICZU",
"adres": "ul. Kaliska 1/3, Łowicz",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon., śr., czw., pt. | 8:00–16:00 | 8 h |
| Pracownik ochrony | wtorek | 8:00–17:00 | 9 h |

**Wymiar tygodniowy: 41 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 12 -----------------------------------------------------------------------
{
"nr": 12,
"slug": "12_Prokuratura_Rejonowa_w_Leczycy",
"nazwa": "PROKURATURA REJONOWA W ŁĘCZYCY",
"adres": "ul. Lotnicza 9, Łęczyca",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": "Parking przy ul. Lotniczej 4 w Łęczycy – dozorowany, ze sprawdzaniem zezwoleń na parkowanie w miejscach odpowiednio oznakowanych.",
"rtg": True,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [
 "Wykonawca zobowiązany jest przedstawić Zamawiającemu, w terminie 60 dni od dnia podpisania umowy, zezwolenie Prezesa Państwowej Agencji Atomistyki na prowadzenie działalności związanej ze stosowaniem urządzenia wytwarzającego promieniowanie jonizujące w niniejszym obiekcie.",
],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon.–pt. | 8:00–16:00 | 8 h |

**Wymiar tygodniowy: 40 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 13 -----------------------------------------------------------------------
{
"nr": 13,
"slug": "13_Prokuratura_Rejonowa_w_Brzezinach",
"nazwa": "PROKURATURA REJONOWA W BRZEZINACH",
"adres": "ul. Sienkiewicza 9, Brzeziny",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon., śr., czw., pt. | 8:00–16:00 | 8 h |
| Pracownik ochrony | wtorek | 8:00–17:00 | 9 h |

**Wymiar tygodniowy: 41 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

# 14 -----------------------------------------------------------------------
{
"nr": 14,
"slug": "14_Prokuratura_Rejonowa_w_Rawie_Mazowieckiej",
"nazwa": "PROKURATURA REJONOWA W RAWIE MAZOWIECKIEJ",
"adres": "ul. Zamkowa Wola 31, Rawa Mazowiecka",
"charakter": "Budynek jednostki organizacyjnej prokuratury o charakterze administracji publicznej / wymiaru sprawiedliwości.",
"systemy_techniczne": [
 "system sygnalizacji włamania (SSWiN)",
 "system telewizji przemysłowej (CCTV)",
 "system kontroli dostępu (SKD)",
],
"dozor_parkingu": None,
"rtg": False,
"alarm_duty": True,
"ppoz_bezposrednie": False,
"caladobowa": False,
"dodatkowe_uwagi": [],
"tabela_obsady": """| Stanowisko | Dni świadczenia usługi | Godziny służby | Wymiar dobowy |
|---|---|---|---|
| Pracownik ochrony | pon., śr., czw., pt. | 8:00–16:00 | 8 h |
| Pracownik ochrony | wtorek | 8:00–17:00 | 9 h |

**Wymiar tygodniowy: 41 h. Łączna liczba pracowników ochrony na obiekcie: 1 osoba.**""",
},

]
