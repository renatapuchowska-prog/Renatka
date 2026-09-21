# -*- coding: utf-8 -*-
#
# UWAGA JEZYKOWA (potwierdzone wprost przez klientke, obowiazuje wszedzie
# w calym dokumencie): poprawny skrot to "tj." (bez kropki po "t"),
# "t.j." jest bledny - rowniez w cytatach aktow prawnych ("tekst
# jednolity"). Nigdy nie uzywac "t.j.".
#
# UWAGA STYLISTYCZNA: nigdy nie uzywac sformulowania "Uwaga szczegolowa"
# (klientka wprost: "ja tak nie pisze bo to jest glupie"). Dodatkowe
# uwagi/adnotacje wstawiac jako zwykle, pelne zdania albo z krotkim,
# rzeczowym pogrubionym leadem opisujacym temat (np. "**Obsluga skanera
# RTG.**"), nigdy z etykieta "Uwaga szczegolowa:".

PAGE_BREAK = """
```{=openxml}
<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr></w:pPr><w:r><w:rPr><w:sz w:val="2"/></w:rPr><w:br w:type="page"/></w:r></w:p>
```
"""

LEGAL_BASIS = """# I. PODSTAWY PRAWNE DZIAŁAŃ OCHRONNYCH

1. Ustawa z dnia 22 sierpnia 1997 r. o ochronie osób i mienia (tj. Dz.U. 2025.532 ze zm.).
2. Ustawa z dnia 11 września 2019 r. – Prawo zamówień publicznych (tj. Dz.U.2026.793 ze zm.).
3. Ustawa z dnia 24 maja 2013 r. o środkach przymusu bezpośredniego i broni palnej (tj. Dz.U.2026.244 ze zm.).
4. Ustawa z dnia 28 stycznia 2016 r. – Prawo o prokuraturze (tj. Dz.U.2026.810), w tym w szczególności art. 40 § 1 dotyczący zakazu wnoszenia broni, amunicji, materiałów wybuchowych i innych środków niebezpiecznych do budynków, w których mieszczą się jednostki organizacyjne prokuratury.
5. Ustawa z dnia 29 listopada 2000 r. – Prawo atomowe (tj. Dz.U.2026.1) – w zakresie dotyczącym obiektów wyposażonych w urządzenia wytwarzające promieniowanie jonizujące.
6. Kodeks pracy – ustawa z dnia 26 czerwca 1974 r. (tj. Dz.U. 2025.277 ze zm.).
7. Specyfikacja Warunków Zamówienia znak 3026-7.261.6.2026 (SWZ) wraz z Opisem Przedmiotu Zamówienia – Załącznik nr 1 do SWZ (dalej: „OPZ”).
8. Wzór Umowy o świadczenie usługi ochrony osób i mienia w obiektach Prokuratury Okręgowej w Łodzi i podległych jej jednostkach organizacyjnych – Załącznik nr 2 do SWZ (dalej: „Wzór Umowy”).
9. Wewnętrzne regulaminy, instrukcje i procedury bezpieczeństwa obowiązujące w Prokuraturze Okręgowej w Łodzi i podległych jej jednostkach organizacyjnych.

UWAGA: dla obiektów typu SĄD dodać tu również pozycję: "Rozporządzenie Ministra
Sprawiedliwości z dnia 27 września 2023 r. w sprawie dokumentowania czynności
przeglądania zawartości bagażu lub odzieży osób wchodzących do budynku sądów
(Dz.U. z 2023 r. poz. 2030)." - patrz Playbook, sekcja o Zał. 5/6 dla sądów.

UWAGA (generalizacja dla nowego Zamawiającego): powyższa treść jest DOSŁOWNYM
przykładem dla Prokuratury Okręgowej w Łodzi (numer SWZ, nazwa jednostki,
konkretne ustawy). Dla nowego Zamawiającego przebudować tę listę tak, żeby
odzwierciedlała jego własny znak postępowania, nazwę Wzoru Umowy oraz akty
prawne faktycznie właściwe dla danego typu obiektu (np. inne przepisy dla
sądu niż dla prokuratury) - nie zostawiać danych Łodzi "przez pomyłkę".
"""

# ---------------------------------------------------------------------------
# SECTION III - wspólne zasady ogólne (przed tabelą obsady konkretnego obiektu)
# ---------------------------------------------------------------------------

ORG_GENERAL_RULES = """## Zasady ogólne organizacji ochrony {.unnumbered}

1. Ochrona osób i mienia realizowana jest w formie bezpośredniej ochrony fizycznej (elementu osobowego), zgodnie z OPZ i Wzorem Umowy (a po zawarciu umowy – jej postanowieniami), przez pracowników ochrony Wykonawcy.
2. Każdy pracownik ochrony skierowany do wykonywania usługi na obiekcie musi nie być skazany za przestępstwo umyślne oraz posiadać stan sprawności psychicznej i fizycznej umożliwiający prawidłowe i bezpieczne wykonywanie czynności.
3. Zamawiającemu przysługuje prawo niedopuszczenia – bez podawania przyczyn – wskazanych przez Wykonawcę pracowników ochrony do wykonywania usługi na obiekcie.

{{OPZ_DUTIES_LIST}}
"""

# ---------------------------------------------------------------------------
# SECTION V - INSTRUKCJE SŁUŻBOWE (wspólne, wzorzec dla nowych obiektów)
#
# POPRAWKI (potwierdzone wprost przez klientke, obowiazuja dla wszystkich
# nowych Instrukcji):
# 1. Listy "Pracownik ochrony:" / "Pracownik ochrony powinien:" (wlamanie,
#    napad) sa NUMEROWANE (1., 2., 3. ...) - NIE punktory (-) i NIE litery
#    (a., b., c. ...). Zweryfikowane na pierwszym/oryginalnym wzorze
#    klientki - musi byc jednolite w calym dokumencie.
# 2. Zestaw grafik pierwszej pomocy to 4 obrazy (nie 3): numery alarmowe +
#    scenariusze (zranienie/zlamanie/krwotok/omdlenie/atak padaczki/
#    zadlawienie), oparzenia + porazenie pradem, pozycja bezpieczna, RKO
#    ilustrowane. Wstawiane BEZ dodatkowych podpisow w tekscie (obrazy maja
#    wlasne, wbudowane tytuly) - patrz Playbook sekcja 7 po szczegoly i
#    wymiary. Zrodlo grafik: NAJNOWSZY realny wzor klientki dostarczony dla
#    danego typu obiektu - NIE skrypty make_safety_graphics.py /
#    make_pozycja_bezpieczna.py (stary, zastapiony standard).
# ---------------------------------------------------------------------------

SERVICE_INSTRUCTIONS = """# V. INSTRUKCJE SŁUŻBOWE


## 1. Instrukcja postępowania pracowników ochrony w przypadku awarii i podtopienia {.unnumbered}

**Postanowienia ogólne**

1. Awarie dotyczą urządzeń technicznych i są spowodowane przez niewłaściwe postępowanie człowieka (obsługę, konserwację i eksploatację) albo wynikają z naturalnego zużycia materiałów, ukrytych wad, niespodziewanie pojawiających się zmian w środowisku (drgania sejsmiczne lub wyładowania atmosferyczne zmniejszające lub gwałtownie zwiększające dopływ prądu elektrycznego).
2. Podtopienie to częściowe zalanie przez wody zewnętrzne obiektu.

**Codzienne środki ostrożności**

1. Pracownicy ochrony w ramach wykonywanych czynności mają obowiązek zewnętrznego sprawdzenia stanu instalacji wodno-kanalizacyjnej i elektrycznej, informując przedstawiciela Zamawiającego o dostrzeżonych nieprawidłowościach grożących awarią.
2. Pracownicy ochrony mają obowiązek sprawdzenia wszelkich informacji o nieprawidłowościach grożących awarią.

**Zasady postępowania pracowników ochrony w przypadku awarii**

1. Powiadomić osoby przebywające w obiekcie o powstałym zagrożeniu przy pomocy dostępnych środków łączności lub bezpośrednio głosem.
2. Dokonać lokalizacji awarii.
3. Ocenić stopień zagrożenia.
4. Podjąć, przed przybyciem właściwych ekip technicznych i służb ratowniczych, działania niedopuszczające do rozszerzenia awarii, w miarę posiadanych umiejętności oraz sił i środków.
5. Ograniczyć ewentualne szkody.
6. W sytuacji, gdy wszelka zwłoka w działaniu groziłaby powstaniem szkód w ochranianym mieniu oraz zagrażałaby życiu lub zdrowiu osób przebywających w obiekcie, zorganizować ewakuację osób z zagrożonych stref oraz chronionego mienia.
7. Po przybyciu służb ratowniczych (Państwowej Straży Pożarnej, Policji, Pogotowia Ratunkowego) współdziałać z nimi, podporządkowując się poleceniom kierującego akcją.
8. Podjąć działania zabezpieczające akcję ratunkową, wskazać i ewentualnie udostępnić posiadane: źródła zasilania w energię elektryczną (główne wyłączniki), hydranty oraz inne środki.
9. Udzielić ewentualnej pomocy przedlekarskiej osobom poszkodowanym.
10. Podjąć działania przeciwdziałające panice.
11. Po zakończeniu akcji ratowniczej sporządzić notatkę służbową.

**Zasady postępowania pracowników ochrony w przypadku podtopienia**

1. W pierwszej fazie uczestniczyć w zabezpieczeniu pomieszczeń przed zalaniem.
2. W drugiej fazie zabezpieczyć ewakuowane mienie.

## 2. Instrukcja postępowania pracowników ochrony w przypadku włamania {.unnumbered}

**Obowiązki pracowników ochrony po opuszczeniu obiektu przez pracowników i interesantów**

1. Sprawdzenie, czy wszyscy pracownicy i interesanci opuścili obiekt.
2. Zamknięcie obiektu od wewnątrz.
3. Sprawdzenie, czy w obiekcie nie pozostały osoby postronne, niemające uprawnień do przebywania po godzinach urzędowania.
4. Sprawdzenie wykazu osób zgłoszonych do przebywania w obiekcie po godzinach urzędowania.
5. Sprawdzenie, czy zostały zwrócone wszystkie wydane w danym dniu klucze do pomieszczeń.
6. W przypadku niezdania kluczy – wdrożenie procedury określonej w instrukcji przechowywania kluczy.
7. Sprawdzenie, czy wszystkie pomieszczenia zostały prawidłowo zamknięte (ewentualnie zaplombowane).
8. Włączenie systemu alarmu antywłamaniowego – jeśli istnieje – oraz ewentualne poinformowanie o tym fakcie operatora alarmu.
9. Patrolowanie obiektu po wyznaczonej trasie z określoną częstotliwością.

**Sposób postępowania pracownika ochrony po ujawnieniu włamania**

Pracownik ochrony:

1. zachowując środki ostrożności, ustala, czy włamywacz pozostaje w obiekcie, czy też opuścił teren,
2. niezwłocznie powiadamia dyżurnego stacji monitorowania Wykonawcy w celu przybycia Grupy Interwencyjnej oraz Policję,
3. zabezpiecza miejsce włamania, powstrzymując osoby trzecie przed zatarciem śladów,
4. zabezpiecza porzucone przez włamywacza mienie,
5. przekazuje miejsce popełnienia przestępstwa przybyłemu patrolowi Policji i udziela wszelkich informacji,
6. powiadamia o zdarzeniu przedstawiciela Zamawiającego oraz Koordynatora ochrony Wykonawcy,
7. dokumentuje zdarzenie oraz podjęte działania w Książce Służby oraz w notatce służbowej.

## 3. Instrukcja postępowania pracowników ochrony w przypadku napadu {.unnumbered}

**Sposób postępowania pracowników ochrony w trakcie napadu**

Pracownik ochrony powinien:

1. dążyć, w miarę możliwości, do powiadomienia Policji,
2. środkami łączności bezprzewodowej powiadomić dyżurnego całodobowej stacji monitorowania alarmów Wykonawcy,
3. nie stawiać oporu napastnikom i nie komentować ich zachowania – jeżeli sprawcy nie są uzbrojeni, dopuszcza się próbę podjęcia działań zmierzających do ich ujęcia,
4. na żądanie napastników wydać żądane przedmioty, opóźniając się w miarę możliwości,
5. dyskretnie obserwować napastników w celu zapamiętania jak największej liczby szczegółów o ich wyglądzie, sposobie zachowania i wymowie.

**Sposób postępowania bezpośrednio po napadzie**

Pracownik ochrony powinien:

1. środkami łączności bezprzewodowej powiadomić dyżurnego całodobowej stacji monitorowania alarmów,
2. nawiązać i utrzymywać kontakt z Policją,
3. powiadomić o zdarzeniu przedstawiciela Zamawiającego i Koordynatora ochrony Wykonawcy,
4. obserwować kierunek ucieczki napastników,
5. zabezpieczyć miejsce zdarzenia,
6. zamknąć obiekt,
7. ustalić świadków,
8. udzielić ewentualnej pomocy poszkodowanym i wezwać Pogotowie Ratunkowe,
9. przekazać miejsce popełnienia przestępstwa przybyłemu patrolowi Policji i udzielać wszelkich informacji.

## 4. Instrukcja postępowania pracowników ochrony w przypadku katastrofy budowlanej {.unnumbered}

**Zasady postępowania w przypadku niezamierzonego, gwałtownego zniszczenia obiektu budowlanego lub jego części**

1. Opuszczając miejsce pracy (budynek), należy:
   a. wyłączyć instalację cieplną, klimatyzacyjną, elektryczną, wodną,
   b. zabrać ze sobą dokumenty tożsamości i inne ważne dokumenty, odzież, pieniądze,
   c. zwracać uwagę, czy wszyscy opuścili budynek,
   d. zachować szczególną ostrożność (uwaga na stropy, klatki schodowe itp.),
   e. o ile nie można opuścić budynku (pomieszczenia) drzwiami wyjściowymi przez klatkę schodową z powodu zagrożenia lub innych przeszkód – uciekać przez okno, jeżeli jest to możliwe,
   f. w przypadku braku możliwości opuszczenia uszkodzonego budynku wywiesić w oknie biały materiał (np. obrus, ręcznik, koszulę) jako znak dla ratowników, że potrzebna jest pomoc,
   g. w przypadku unieruchomienia (przysypania) nawoływać pomoc, stukać w lekkie elementy metalowe w celu ułatwienia ratownikom lokalizacji,
   h. po opuszczeniu budynku: powiadomić kierującego akcją ratowniczą o osobach, które mogły pozostać w pomieszczeniach, przekazać służbie ratowniczej informacje pomocne w prowadzeniu akcji, udać się w rejon ewakuacji, nie wracać na miejsce katastrofy bez zezwolenia przełożonych i służb, w przypadku doznania obrażeń zgłosić się do punktu pomocy medycznej, stosować się do poleceń przełożonych i służb biorących udział w akcji ratowniczej.
2. W sytuacjach wystąpienia na terenie obiektu wypadku lub innego zdarzenia grożącego bezpośrednim niebezpieczeństwem utraty życia albo ciężkim uszczerbkiem na zdrowiu osób tam przebywających, należy natychmiast powiadomić o tym fakcie przedstawiciela Zamawiającego oraz Koordynatora ochrony Wykonawcy i postępować zgodnie z obowiązującą instrukcją bezpieczeństwa i higieny pracy. We wszystkich przypadkach zaistnienia sytuacji kryzysowych w godzinach pracy i konieczności przeprowadzenia ewakuacji osób z budynku, osoby przebywające w obiekcie zobowiązane są do bezwzględnego podporządkowania się zaleceniom osób kierujących ewakuacją.

## 5. Instrukcja postępowania pracowników ochrony w przypadku groźby zdetonowania ładunku wybuchowego {.unnumbered}

**Działania prewencyjne – zwracanie uwagi na:**

1. rzucające się w oczy nietypowe zachowania osób,
2. pozostawione bez opieki przedmioty: teczki, paczki, torby, pakunki itp., szczególnie w miejscach pozwalających na ukrycie niewielkich pakunków (np. w toaletach, windach, piwnicach, korytarzach, poczekalniach),
3. osoby ubrane nietypowo do występującej pory roku,
4. samochody, w szczególności furgonetki, parkujące w nietypowych miejscach, tj. w pobliżu wejść do obiektu; wszystkie wejścia do obiektu po godzinach urzędowania powinny być zamknięte,
5. fakt, że sprawca zagrożenia nie musi wyróżniać się z tłumu szczególnym wyglądem.

**Działania po ujawnieniu ładunku lub przesyłki niebezpiecznej**

1. Zakaz dotykania podejrzanego przedmiotu.
2. Podjęcie działań izolacyjnych pomieszczenia, w którym znajduje się przedmiot.
3. Powiadomienie przedstawiciela Zamawiającego i Koordynatora ochrony Wykonawcy.
4. Powiadomienie Policji, Straży Pożarnej, Pogotowia Ratunkowego.
5. Przekazanie obiektu dowódcy sił Policji.
6. Udzielenie wszelkiej pomocy służbom ratowniczym.

**Działania w przypadku telefonicznej informacji o podłożeniu niebezpiecznego ładunku**

1. Rozmowę należy prowadzić spokojnie i uprzejmie.
2. Osoba odbierająca informację powinna podtrzymywać rozmowę jak najdłużej.
3. W jej trakcie dążyć do uzyskania możliwie największej liczby informacji o zgłaszającym oraz o podłożonym niebezpiecznym ładunku:
   a. dlaczego został podłożony niebezpieczny ładunek?
   b. jak on wygląda?
   c. jakie stanowi zagrożenie?
   d. gdzie jest podłożony?
   e. kiedy eksploduje / rozszczelni się?

## 6. Instrukcja na wypadek powstania pożaru {.unnumbered}

Zadania pracownika ochrony w ramach stałej ochrony w zakresie ochrony przeciwpożarowej i ewakuacji określa wdrożona dla obiektu instrukcja bezpieczeństwa pożarowego. Pracownicy ochrony zobowiązani są do:

1. sprawdzenia, przed przystąpieniem do pracy, czy wszystkie komplety kluczy (bieżącego użycia, zapasowe, plombowane itp.) do poszczególnych pomieszczeń znajdują się w miejscu do tego celu wyznaczonym,
2. dopilnowania przestrzegania przez osoby przebywające na terenie obiektu przepisów przeciwpożarowych, w szczególności dotyczących zakazu palenia tytoniu i używania otwartego ognia,
3. przeciwdziałania używaniu sprzętu przeciwpożarowego niezgodnie z przeznaczeniem,
4. dopilnowania, aby drogi i wyjścia ewakuacyjne nie były zastawione,
5. codziennego sprawdzania, po zakończeniu pracy, czy urządzenia elektroenergetyczne i gazowe zostały wyłączone, czy nie występują oznaki tlenia lub palenia materiałów albo zapachu gazu,
6. sprawdzania stanu bezpieczeństwa przeciwpożarowego rejonów i miejsc pracy podczas prowadzenia remontów pomieszczeń i instalacji,
7. w przypadku powstania pożaru: ogłoszenia alarmu pożarowego i powiadomienia Straży Pożarnej, powiadomienia przedstawiciela Zamawiającego i Koordynatora ochrony Wykonawcy, udzielenia wszelkiej informacji o obiekcie dowódcy akcji straży pożarnej.

## 7. Instrukcja postępowania pracowników ochrony patrolu (Grupy) interwencyjnej {.unnumbered}

1. Doraźnie, na wezwanie pracownika ochrony, przyjeżdża Grupa Interwencyjna Wykonawcy, będąca wsparciem w całodobowej dyspozycji. Wsparcie Grupy Interwencyjnej jest dostępne w szczególności w przypadku bezpośredniego zagrożenia życia i zdrowia, np. napadu, włamania czy rabunku.
2. Grupa Interwencyjna składa się z co najmniej dwóch pracowników ochrony wpisanych na listę kwalifikowanych pracowników ochrony fizycznej (wliczając kierowcę), nieposiadających statusu osób niepełnosprawnych.
3. Pracownicy Grupy Interwencyjnej wyposażeni są w środki gwarantujące szybką i niezawodną łączność.
4. Czas przybycia Grupy Interwencyjnej na miejsce zgłoszenia nie może przekroczyć 15 minut, a w przypadku zaoferowania w Formularzu ofertowym krótszego czasu reakcji – czasu zadeklarowanego przez Wykonawcę.
5. Po zakończeniu interwencji Grupa Interwencyjna sporządza notatkę służbową z przebiegu interwencji i przekazuje ją Zamawiającemu.
6. Tryb powiadamiania osób funkcyjnych w zależności od sytuacji określa Zamawiający, a telefony alarmowe do dyżurnego całodobowej stacji monitorowania alarmów Wykonawcy wskazane są w Rozdziale IV niniejszej Instrukcji.

## 8. Instrukcja udzielenia pierwszej pomocy przedmedycznej {.unnumbered}

1. Każdy pracownik ochrony posiada aktualne przeszkolenie z zakresu udzielania pierwszej pomocy przedmedycznej, potwierdzone stosownym zaświadczeniem.
2. W przypadku zdarzenia zagrażającego życiu lub zdrowiu osoby przebywającej na terenie obiektu, pracownik ochrony postępuje według poniższego schematu:
   a. ocenia sytuację i zapewnia bezpieczeństwo sobie oraz poszkodowanemu,
   b. sprawdza przytomność i oddech poszkodowanego,
   c. wzywa pomoc (Pogotowie Ratunkowe – tel. 999 lub 112) oraz informuje przedstawiciela Zamawiającego i Koordynatora ochrony Wykonawcy,
   d. w razie braku oddechu – rozpoczyna resuscytację krążeniowo-oddechową zgodnie z posiadanym przeszkoleniem, a w przypadku dostępności – wykorzystuje automatyczny defibrylator zewnętrzny (AED),
   e. w przypadku krwawień – stosuje ucisk bezpośredni oraz opatrunek uciskowy,
   f. do czasu przybycia zespołu ratownictwa medycznego nie pozostawia poszkodowanego bez opieki oraz nie podaje mu żadnych leków ani płynów,
   g. po przybyciu zespołu ratownictwa medycznego przekazuje mu wszystkie posiadane informacje o zdarzeniu i podjętych czynnościach,
   h. sporządza notatkę służbową z przebiegu zdarzenia i udzielonej pomocy.

{{GRAPHIC_NUMERY}}

{{GRAPHIC_OPARZENIA}}

{{GRAPHIC_POZYCJA}}

{{GRAPHIC_RKO}}
"""

# ---------------------------------------------------------------------------
# SECTION VI - WZORY DOKUMENTÓW SŁUŻBOWYCH (wspólne, wg ustalonego wzoru firmowego)
# ---------------------------------------------------------------------------

def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _rpr(bold=False, italic=False, size=None):
    parts = ['<w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/>']
    if bold:
        parts.append("<w:b/>")
    if italic:
        parts.append("<w:i/>")
    if size:
        parts.append(f'<w:sz w:val="{size}"/>')
    return "<w:rPr>" + "".join(parts) + "</w:rPr>"

def p_center(text, bold=True, space_before=120, space_after=200):
    return (
        f'<w:p><w:pPr><w:spacing w:before="{space_before}" w:after="{space_after}"/>'
        f'<w:jc w:val="center"/>{_rpr(bold=bold, size=26)}</w:pPr>'
        f'<w:r>{_rpr(bold=bold, size=26)}<w:t xml:space="preserve">{_esc(text)}</w:t></w:r></w:p>'
    )

def p_ref(text):
    return (
        f'<w:p><w:pPr><w:jc w:val="right"/><w:spacing w:after="200"/>'
        f'{_rpr(italic=True, size=18)}</w:pPr>'
        f'<w:r>{_rpr(italic=True, size=18)}<w:t xml:space="preserve">{_esc(text)}</w:t></w:r></w:p>'
    )

def p_label(text, bold=False, space_before=120, space_after=60):
    return (
        f'<w:p><w:pPr><w:jc w:val="both"/><w:spacing w:before="{space_before}" w:after="{space_after}"/>'
        f'{_rpr(bold=bold)}</w:pPr>'
        f'<w:r>{_rpr(bold=bold)}<w:t xml:space="preserve">{_esc(text)}</w:t></w:r></w:p>'
    )

def p_dotline(label=None, space_after=180):
    """Jedna, pojedyncza linia: opcjonalna etykieta + kropkowana linia
    (prawdziwy tab-leader Worda) siegajaca dokladnie do prawego marginesu.
    Nigdy sie nie zawija - to jedna linia, jedna paragraf."""
    lbl_run = f'<w:r>{_rpr()}<w:t xml:space="preserve">{_esc(label)} </w:t></w:r>' if label else ""
    return (
        f'<w:p><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>'
        f'<w:spacing w:after="{space_after}"/>{_rpr()}</w:pPr>'
        f'{lbl_run}<w:r><w:tab/></w:r></w:p>'
    )

def p_two_col_dotlines(left="", right=""):
    """Dwie linie kropkowane obok siebie (np. dwa podpisy)."""
    return (
        '<w:p><w:pPr><w:tabs>'
        '<w:tab w:val="right" w:leader="dot" w:pos="3600"/>'
        '<w:tab w:val="left" w:pos="3900"/>'
        '<w:tab w:val="right" w:leader="dot" w:pos="9350"/>'
        f'</w:tabs>{_rpr()}</w:pPr>'
        f'<w:r><w:tab/></w:r><w:r><w:tab/></w:r><w:r><w:tab/></w:r></w:p>'
    )

def p_two_col_labels(left, right):
    return (
        '<w:p><w:pPr><w:tabs><w:tab w:val="left" w:pos="3900"/></w:tabs>'
        f'{_rpr(bold=True, size=18)}</w:pPr>'
        f'<w:r>{_rpr(bold=True, size=18)}<w:t xml:space="preserve">{_esc(left)}</w:t></w:r>'
        f'<w:r><w:tab/></w:r>'
        f'<w:r>{_rpr(bold=True, size=18)}<w:t xml:space="preserve">{_esc(right)}</w:t></w:r></w:p>'
    )

def ooxml_block(*paragraphs):
    return "\n```{=openxml}\n" + "\n".join(paragraphs) + "\n```\n"


def p_section_bar(text):
    """Pasek tytulowy pojedynczej instrukcji w Rozdziale V: CZARNE, pogrubione
    WERSALIKI na turkusowym tle (4BACC6 - accent5 motywu), wyjustowane,
    z odstepem pod spodem. Kolor tekstu MUSI byc jawnie czarny (000000),
    nigdy "auto" i nigdy bialy - potwierdzone wprost przez klientke."""
    return ooxml_block(
        f'<w:p><w:pPr><w:pStyle w:val="SectionBar"/></w:pPr>'
        f'<w:r><w:t xml:space="preserve">{_esc(text)}</w:t></w:r></w:p>'
    )

import re as _re

def _convert_section_v_headings(text):
    pattern = _re.compile(r'^## (.+?) \{\.unnumbered\}$', _re.MULTILINE)
    return pattern.sub(lambda m: p_section_bar(m.group(1)).strip(), text)


def build_document_templates():
    parts = []
    parts.append("# VI. WZORY DOKUMENTÓW SŁUŻBOWYCH\n")

    # --- Zalacznik nr 1 --------------------------------------------------
    parts.append(ooxml_block(
        p_ref("Zał. nr 1 – Wzór książki służby"),
        p_center("KSIĄŻKA PRZEBIEGU SŁUŻBY PRACOWNIKA OCHRONY"),
        p_dotline("Data pełnienia służby"),
        p_dotline("Godziny pełnienia służby"),
        p_label("Imię i nazwisko pełniącego służbę"),
        p_dotline(),
    ))
    parts.append(ooxml_block(
        p_center("OPIS PRZEBIEGU SŁUŻBY"),
        *[p_dotline() for _ in range(11)],
    ))
    parts.append(ooxml_block(
        p_center("UWAGI OSÓB KONTROLUJĄCYCH SŁUŻBĘ"),
        *[p_dotline() for _ in range(3)],
        p_two_col_dotlines(),
        p_two_col_labels("PODPIS ZDAJĄCEGO SŁUŻBĘ", "PODPIS PRZYJMUJĄCEGO SŁUŻBĘ"),
    ))
    parts.append("{{PAGE_BREAK}}\n")

    # --- Zalacznik nr 2 --------------------------------------------------
    parts.append(ooxml_block(
        p_ref("Zał. nr 2 – Wzór notatki służbowej z czynności legitymowania"),
        p_center("NOTATKA SŁUŻBOWA Z CZYNNOŚCI LEGITYMOWANIA"),
        p_dotline("W dniu"),
        p_dotline("o godzinie"),
        p_label("Imię i nazwisko osoby"),
        p_dotline(),
        p_label("Nazwa, numer i seria dokumentu potwierdzającego tożsamość"),
        p_dotline(),
    ))
    parts.append(ooxml_block(
        p_label("Przyczyna dokonania czynności legitymowania:"),
        *[p_dotline() for _ in range(4)],
    ))
    parts.append(ooxml_block(
        p_label("Imię i nazwisko osoby dokonującej legitymowania:"),
        p_dotline(),
        p_label("Numer legitymacji służbowej lub identyfikatora osoby dokonującej legitymowania:"),
        p_dotline(),
        p_label("Uwagi:"),
        p_dotline(),
        p_ref("IMIĘ, NAZWISKO I PODPIS SPORZĄDZAJĄCEGO:"),
        p_dotline(),
    ))
    parts.append("{{PAGE_BREAK}}\n")

    # --- Zalacznik nr 3 --------------------------------------------------
    parts.append(ooxml_block(
        p_ref("Zał. nr 3 – Wzór notatki służbowej"),
        p_center("NOTATKA SŁUŻBOWA"),
        p_dotline("Data"),
        p_label("W sprawie:"),
        *[p_dotline() for _ in range(2)],
    ))
    parts.append(ooxml_block(
        p_label("Opis:"),
        *[p_dotline() for _ in range(15)],
        p_ref("IMIĘ, NAZWISKO I PODPIS SPORZĄDZAJĄCEGO:"),
        p_dotline(),
    ))
    parts.append("{{PAGE_BREAK}}\n")

    # --- Zalacznik nr 4 --------------------------------------------------
    parts.append(ooxml_block(
        p_ref("Zał. nr 4 – Wzór protokołu użycia ŚPB"),
        p_center("PROTOKÓŁ Z UŻYCIA LUB WYKORZYSTANIA ŚRODKÓW PRZYMUSU BEZPOŚREDNIEGO"),
        p_label("Imię i nazwisko pracownika ochrony fizycznej, który użył lub wykorzystał środki przymusu bezpośredniego oraz numer jego legitymacji służbowej lub identyfikatora:"),
        p_dotline(),
        p_label("Data, godzina i miejsce użycia lub wykorzystania środków przymusu bezpośredniego:"),
        p_dotline(),
        p_label("Przyczyna, rodzaj i skutek użycia lub wykorzystania środków przymusu bezpośredniego:"),
        *[p_dotline() for _ in range(2)],
    ))
    parts.append(ooxml_block(
        p_label("Dane identyfikujące osobę, w stosunku do której użyto lub wykorzystano środki przymusu bezpośredniego:"),
        *[p_dotline() for _ in range(2)],
        p_label("Informacja dotycząca udzielenia pierwszej pomocy przedmedycznej:"),
        p_dotline(),
        p_label("Uwagi:"),
        p_dotline(),
        p_ref("IMIĘ, NAZWISKO I PODPIS SPORZĄDZAJĄCEGO:"),
        p_dotline(),
    ))

    return "\n".join(parts)


DOCUMENT_TEMPLATES = build_document_templates()


# ---------------------------------------------------------------------------
# Literalna lista obowiazkow z OPZ pkt 26 lit. a)-kk) dla sekcji III,
# zgodnie z prośbą: zadania pracowników ochrony maja byc wymienione
# literalnie, tak jak w OPZ/Umowie. UWAGA: format listy w Rozdziale III to
# lista NUMEROWANA (patrz Playbook sekcja 3/4) - markdown "1. tresc",
# NIE punktory - pandoc konwertuje to na prawdziwa numeracje Worda.
# ---------------------------------------------------------------------------

def build_opz_duties_section(site):
    from opz_duties import build_opz_duties_list
    items = build_opz_duties_list(site)
    header = (
        '::: {custom-style="Justify"}\n'
        '## Obowiązki pracowników ochrony na obiekcie {.unnumbered}\n\n'
        'Do obowiązków pracownika ochrony na niniejszym obiekcie należy:\n'
        ':::\n'
    )
    numbered = "\n".join(f"{i}. {t}" for i, (_, t) in enumerate(items, start=1))
    return header + "\n" + numbered + "\n"


WYKAZ_OSOB_INTRO = """# VII. WYKAZ OSÓB ZAPOZNANYCH Z INSTRUKCJĄ

::: {custom-style="FormText"}
Z treścią instrukcji zapoznałem się i przyjąłem do wykonania:
:::
"""

WYKAZ_OSOB_TABLE_OOXML = """
```{=openxml}
<w:tbl>
  <w:tblPr>
    <w:tblStyle w:val="TableGrid"/>
    <w:tblW w:w="0" w:type="auto"/>
    <w:tblBorders>
      <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>
      <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
      <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
      <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
      <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>
      <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    </w:tblBorders>
    <w:tblLayout w:type="fixed"/>
    <w:tblLook w:val="04A0"/>
  </w:tblPr>
  <w:tblGrid>
    <w:gridCol w:w="900"/>
    <w:gridCol w:w="3600"/>
    <w:gridCol w:w="2200"/>
    <w:gridCol w:w="2660"/>
  </w:tblGrid>
  __ROWS__
</w:tbl>
```
"""

def _ooxml_row(cells, bold=False, header=False):
    tc = []
    b_open, b_close = ("<w:b/>", "") if bold else ("", "")
    for c in cells:
        tc.append(
            '<w:tc><w:tcPr><w:vAlign w:val="center"/></w:tcPr>'
            '<w:p><w:pPr><w:spacing w:before="120" w:after="120"/>'
            f'<w:rPr>{b_open}<w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr></w:pPr>'
            f'<w:r><w:rPr>{b_open}<w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr><w:t xml:space="preserve">{c}</w:t></w:r></w:p></w:tc>'
        )
    height = ' <w:trPr><w:trHeight w:val="650"/></w:trPr>' if not header else ""
    return f"<w:tr>{height}{''.join(tc)}</w:tr>"

def build_wykaz_table(n_rows=12):
    rows = [_ooxml_row(["Lp.", "Imię i nazwisko", "Data", "Podpis"], bold=True, header=True)]
    for i in range(1, n_rows + 1):
        rows.append(_ooxml_row([str(i), "", "", ""]))
    return WYKAZ_OSOB_TABLE_OOXML.replace("__ROWS__", "\n".join(rows))

WYKAZ_OSOB = WYKAZ_OSOB_INTRO + "\n\n" + build_wykaz_table(12)


# ---------------------------------------------------------------------------
# POST-PROCESSING: odstep (pusty akapit) po KAZDEJ liscie (numerowanej,
# literowanej lub wypunktowanej kropkami/myslnikami) przed kolejnym akapitem
# nie bedacym czescia listy. Wymog klientki: "Jak coś jest wypunktowane
# nawet kropkami to poniżej ma być linijka przerwy pod wszystkimi punktami
# przed kolejną linijką". Dziala uniwersalnie, bo pandoc renderuje kazdy typ
# listy (numer/litera/punktor) przez <w:numPr> w <w:pPr>, tylko z innym
# numFmt - wystarczy wykryc obecnosc/brak w:numPr miedzy sasiednimi akapitami.
# Wywolywac PO center_chapter_headings(), jako ostatni krok post-processingu
# przed zapisaniem finalnego .docx.
# ---------------------------------------------------------------------------

def add_spacing_after_lists(docx_path):
    import docx as _docx
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    def _has_numpr(p):
        pPr = p._p.find(qn('w:pPr'))
        if pPr is None:
            return False
        return pPr.find(qn('w:numPr')) is not None

    d = _docx.Document(docx_path)
    paras = d.paragraphs
    targets = []
    for i in range(len(paras) - 1):
        if _has_numpr(paras[i]) and not _has_numpr(paras[i + 1]):
            targets.append(paras[i + 1]._p)
    for target_p in targets:
        new_p = OxmlElement('w:p')
        target_p.addprevious(new_p)
    d.save(docx_path)
