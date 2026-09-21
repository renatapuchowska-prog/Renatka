# -*- coding: utf-8 -*-
# Literalna lista obowiazkow Wykonawcy z OPZ (Zalacznik nr 1 do SWZ), pkt 26
# lit. a) - kk). Zachowane oryginalne litery i brzmienie; niektore pozycje
# sa warunkowe (dotycza tylko okreslonych obiektow) - oznaczone w polu "gdy".
#
# UWAGA (generalizacja dla nowego Zamawiajacego): OPZ_PKT26 ponizej to
# DOSLOWNA tresc z OPZ Prokuratury Okregowej w Lodzi - jest to PRZYKLAD
# poprawnie odfiltrowanej listy (test: "co robi pracownik ochrony na
# posterunku" vs "co zapewnia Wykonawca jako podmiot", patrz playbook.md
# sekcja 3). Dla NOWEGO Zamawiajacego trzeba zbudowac ANALOGICZNA liste na
# podstawie JEGO wlasnego OPZ - nie kopiowac tej listy 1:1, tylko uzyc jej
# jako wzorca metody: przejsc przez kazdy punkt nowego OPZ (zwykle pkt 26
# lub odpowiednik), zastosowac test z playbooka, zachowac oryginalne
# oznaczenia literowe/numeryczne tych punktow, ktore zostaja.
#
# UWAGA JEZYKOWA (potwierdzone wprost przez klientke): skrot "tj." (bez
# kropki po "t") jest poprawny, "t.j." jest bledny - rowniez w cytatach
# aktow prawnych ("tekst jednolity"). Dotyczy to CALEGO dokumentu, bez
# wyjatku dla cytatow Dz.U. Nie uzywac "t.j." nigdzie.

OPZ_PKT26 = [
    ("a", "ochrona zewnętrzna i wewnętrzna obiektów (wyposażenia, sprzętu i urządzeń oraz osób)", "always"),
    ("b", "kontrola terenów włączonych do obiektów, dozorowanie parkingów{parking_clause}, sprawdzanie zezwoleń na parkowanie, o ile dany parking jest odpowiednio oznaczony", "parking"),
    ("c", "bieżąca obserwacja obiektów za pomocą urządzeń telewizji dozorowej", "always"),
    ("d", "prowadzenie książki dyżurów i innych dokumentów w ochranianych obiektach", "always"),
    ("e", "wydawanie kluczy do pomieszczeń osobom uprawnionym, po wcześniejszym sprawdzeniu tożsamości pobierającego i odnotowaniu tego w wykazie ewidencji pobranych kluczy", "always"),
    ("f", "prowadzenie kontroli ruchu osobowego interesantów Prokuratury Okręgowej w Łodzi i podległych jej jednostek organizacyjnych, połączone z obsługą bramki wykrywania metali, skanera bagażu (w jednostkach w których występują te urządzenia) oraz rejestracją osób wchodzących i wychodzących w książce wejść i wyjść, a także pojazdów wjeżdżających na teren", "always"),
    ("g", "natychmiastowe interweniowanie w przypadku stwierdzenia naruszenia przepisów porządkowych oraz przepisów ochrony przeciwpożarowej", "always"),
    ("h", "w przypadku pożaru lub innego miejscowego zagrożenia natychmiastowe wyprowadzenie osób znajdujących się w strefach ich zasięgu, wezwanie Straży Pożarnej lub innych służb ratowniczych, po czym do czasu ich przybycia przystąpienie do likwidacji zagrożenia", "always"),
    ("i", "zapewnienie bezpieczeństwa osób i mienia na terenie obiektów Zamawiającego", "always"),
    ("j", "z chwilą zaistnienia wykroczenia, przestępstwa, napadu lub uzyskania informacji o podłożeniu niebezpiecznego ładunku bądź podejrzeniu podłożenia niebezpiecznego ładunku, podjęcie działań zgodnych z obowiązującymi instrukcjami", "always"),
    ("k", "zapewnienie reakcji grup interwencyjnych (co najmniej 2 osoby w jednej załodze wliczając kierowcę, które nie posiadają statusu osób niepełnosprawnych i są wpisane na listę kwalifikowanych pracowników ochrony) w czasie do 15 minut od momentu zgłoszenia", "always"),
    ("l", "wykonywanie systematycznych obchodów w chronionych obiektach, a w jednostkach w których ochrona pełni służbę całodobowo, min. 3 razy w godzinach poza urzędowaniem jednostek, tj. ok. 20:00, ok. 24:00, ok. 04:00", "always"),
    ("m", "podejmowanie ścisłej współpracy i udzielanie pomocy pracownikom Zamawiającego w stanach zagrożenia bądź wystąpienia zdarzeń zagrażających ich życiu i zdrowiu", "always"),
    ("n", "korzystanie z technicznych środków ochrony mienia (telewizja przemysłowa, systemy kontroli dostępu, system alarmowy, skaner bagażu, bramki wykrywania metali) zainstalowanych w budynkach", "always"),
    ("o", "stałe informowanie kierownictwa jednostek organizacyjnych oraz Wykonawcy o zaistniałych i potencjalnych zagrożeniach, np.: o zaistnieniu przestępstwa, napadu bądź uzyskaniu informacji o podłożeniu niebezpiecznego ładunku lub podejrzenia jego podłożenia, wystąpieniu awarii lub zdarzeń losowych", "always"),
    ("p", "stosowanie dozwolonych środków przymusu bezpośredniego, w granicach określonych w art. 36 ustawy z dnia 22 sierpnia 1997 r. o ochronie osób i mienia (tj. Dz.U.2025.532 ze zm.) i w art. 11 i 12 ustawy z 24 maja 2013 r. o środkach przymusu bezpośredniego i broni palnej (tj. Dz.U.2026.244 ze zm.)", "always"),
    ("s", "egzekwowanie przestrzegania przez osoby wchodzące do obiektów chronionych obowiązujących w nich zasad bezpieczeństwa", "always"),
    ("r", "obsługa skanera RTG do kontroli bagażu wyłącznie przez pracownika posiadającego aktualne przeszkolenie oraz badania lekarskie w tym zakresie", "rtg"),
    ("dd", "podejmowanie interwencji w sytuacjach bezpośredniego zagrożenia", "always"),
    ("ee", "zwracanie się do osób, co do których zachodzi uzasadnione podejrzenie, że wnoszą lub posiadają przedmioty objęte zakazem z art. 40 § 1 ustawy – Prawo o prokuraturze, o okazanie wnoszonych przedmiotów, w tym zawartości bagaży, a w razie odmowy – odmowa wpuszczenia takiej osoby do obiektu", "always"),
    ("ff", "wydawanie poleceń porządkowych osobom zakłócającym porządek", "always"),
    ("gg", "ujęcie, w celu niezwłocznego przekazania Policji, osób stwarzających bezpośrednie zagrożenie dla życia lub zdrowia ludzkiego, a także chronionego mienia", "always"),
    ("hh", "podejmowanie innych działań w trybie i na zasadach określonych prawem oraz instrukcjami przewidzianymi dla pracowników ochrony", "always"),
    ("ii", "podejmowanie innych czynności niezbędnych do prawidłowej realizacji usługi ochrony, wynikających z wewnętrznych regulacji Prokuratury Okręgowej w Łodzi", "always"),
    ("kk", "otwieranie jednostki we wszystkie dni urzędowania, a także po uprzednim telefonicznym zgłoszeniu w dni wolne od pracy, oraz rozbrajanie systemu alarmowego na co najmniej 30 minut przed rozpoczęciem urzędowania; po zakończeniu urzędowania – zamykanie obiektu i uzbrajanie systemu alarmowego", "alarm"),
]


def format_parking_clause(site):
    addr = site.get("dozor_parkingu")
    if not addr:
        return ""
    # site["dozor_parkingu"] zaczyna sie od "Parking przy ..." - wyciagamy fraze lokalizacyjna
    loc = addr.split("–")[0].strip()
    if loc.lower().startswith("parking "):
        loc = loc[len("parking "):]
    return f" (zlokalizowanego {loc})"


def build_opz_duties_list(site):
    """Zwraca liste (litera, tekst) obowiazujacych dla danego obiektu,
    z zachowaniem oryginalnych liter OPZ pkt 26 (niektore litery moga
    zostac pominiete, jesli dana pozycja nie dotyczy tego obiektu)."""
    has_parking = bool(site.get("dozor_parkingu"))
    has_rtg = bool(site.get("rtg"))
    has_alarm = bool(site.get("alarm_duty"))
    has_monitoring = bool(site.get("caladobowa"))

    out = []
    for letter, text, cond in OPZ_PKT26:
        if cond == "parking" and not has_parking:
            continue
        if cond == "rtg" and not has_rtg:
            continue
        if cond == "alarm" and not has_alarm:
            continue
        if cond == "monitoring" and not has_monitoring:
            continue
        if cond == "parking":
            text = text.format(parking_clause=format_parking_clause(site))
        out.append((letter, text))
    return out
