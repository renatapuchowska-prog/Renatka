# -*- coding: utf-8 -*-
"""Sklada pelne 'Instrukcje ochrony obiektu' dla wszystkich obiektow z SITES
(sites.py) na bazie common_blocks.py/opz_duties.py i szablonu
assets/reference_verdana.docx (patrz build_reference_doc.py).

UWAGA (generalizacja dla nowego Zamawiajacego - WAZNE): ten plik jest
DOSLOWNYM przykladem uzytym dla Prokuratury Okregowej w Lodzi. Zawiera
kilka rzeczy specyficznych dla TEGO Zamawiajacego, ktore trzeba
przeparametryzowac/dostosowac dla nowego klienta, zanim sie go uruchomi:

  - SIGN_NUM = znak postepowania SWZ Lodzi - podmienic na znak nowego
    postepowania (albo usunac, jesli nowy Zamawiajacy go nie ujawnia).
  - section_I() -> LEGAL_BASIS z common_blocks.py jest tresc dla Lodzi
    (numer SWZ, nazwa Wzoru Umowy, lista ustaw) - dla nowego Zamawiajacego
    zbudowac analogiczny tekst z jego wlasnymi danymi (patrz playbook.md
    sekcja "generalizacja" przy LEGAL_BASIS).
  - section_IV(site) -> dane Przedstawiciela Zamawiajacego oraz
    Koordynatora/Dowodcy sa NA STALE wpisane dla Lodzi - dla nowego
    Zamawiajacego podmienic na jego dane kontaktowe z SWZ oraz na
    aktualne dane koordynatora/dowodcy Wykonawcy dla tego zlecenia
    (jesli klientka dostarczy stara instrukcje z innym koordynatorem -
    uzyc danych z niej, patrz playbook.md sekcja 10).
  - HEADINGS / struktura 7 rozdzialow jest UNIWERSALNA i nie wymaga zmian.
  - Zalaczniki 5/6 (dla sadow) NIE sa tu zaimplementowane - jesli nowy
    obiekt to sad, dopisac build_zal5_zal6(site) wg playbook.md sekcja 8.
"""
import os, re, subprocess, shutil
from sites import SITES
from common_blocks import (LEGAL_BASIS, ORG_GENERAL_RULES, SERVICE_INSTRUCTIONS,
                            DOCUMENT_TEMPLATES, WYKAZ_OSOB, PAGE_BREAK,
                            add_spacing_after_lists)

DOCUMENT_TEMPLATES = DOCUMENT_TEMPLATES.replace("{{PAGE_BREAK}}", PAGE_BREAK)

REF_DOCX = os.path.abspath("assets/reference_verdana.docx")
LOGO_MAXUS = os.path.abspath("assets/logos_norm/maxus.png")
LOGO_MM_MONITORING = os.path.abspath("assets/logos_norm/mm_monitoring.png")
LOGO_MM_SECURITY = os.path.abspath("assets/logos_norm/mm_security.png")
PHOTOS_DIR = os.path.abspath("assets/photos")

OUT_MD = "md2"
OUT_DOCX = "/mnt/user-data/outputs/Instrukcje_ochrony"
DRAFT_DIR = "draft"
os.makedirs(OUT_MD, exist_ok=True)
os.makedirs(OUT_DOCX, exist_ok=True)
os.makedirs(DRAFT_DIR, exist_ok=True)

# UWAGA: znak postepowania SWZ - PRZYKLAD dla Lodzi. Podmienic dla nowego
# Zamawiajacego (albo wywalic z Rozdzialu IV, jesli tam sie odwoluje).
SIGN_NUM = "3026-7.261.6.2026"

HEADINGS = [
    ("I", "PODSTAWY PRAWNE DZIAŁAŃ OCHRONNYCH"),
    ("II", "LOKALIZACJA I OPIS OBIEKTU PODLEGAJĄCEGO OCHRONIE"),
    ("III", "ORGANIZACJA OCHRONY"),
    ("IV", "PODLEGŁOŚĆ SŁUŻBOWA"),
    ("V", "INSTRUKCJE SŁUŻBOWE"),
    ("VI", "WZORY DOKUMENTÓW SŁUŻBOWYCH"),
    ("VII", "WYKAZ OSÓB ZAPOZNANYCH Z INSTRUKCJĄ"),
]

def heading_text(rn, title):
    return f"{rn}. {title}"

# ---------------------------------------------------------------------------
def table_to_bullets(table_md):
    """Convert a pandoc pipe table (with a trailing bold summary line) into a
    Markdown bullet list, per user's request to avoid tables for staffing."""
    lines = [l for l in table_md.strip().split("\n")]
    # first line = header, second = separator
    header_cells = [c.strip() for c in lines[0].strip("|").split("|")]
    data_lines = []
    trailer_lines = []
    in_table = True
    for l in lines[2:]:
        if l.strip().startswith("|") and in_table:
            data_lines.append(l)
        else:
            in_table = False
            if l.strip():
                trailer_lines.append(l.strip())
    bullets = []
    for l in data_lines:
        cells = [c.strip() for c in l.strip("|").split("|")]
        parts = []
        for h, c in zip(header_cells, cells):
            if c:
                parts.append(f"{h}: {c}")
        bullets.append("- " + "; ".join(parts))
    out = "\n".join(bullets)
    if trailer_lines:
        out += "\n\n" + "\n".join(trailer_lines)
    return out

# ---------------------------------------------------------------------------
def cover_page(site):
    return f"""| ![]({LOGO_MAXUS}){{width=2.86cm}} | ![]({LOGO_MM_MONITORING}){{width=3.41cm}} | ![]({LOGO_MM_SECURITY}){{width=3.2cm}} |
|:---:|:---:|:---:|

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverTitle"}}
INSTRUKCJA OCHRONY OBIEKTU
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSubtitle"}}
{site['nazwa'].upper()}
:::

::: {{custom-style="CoverSubtitle"}}
{site['adres'].upper()}
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

::: {{custom-style="CoverSmall"}}
&nbsp;
:::

```{{=openxml}}
<w:tbl>
<w:tblPr><w:tblW w:w="0" w:type="auto"/><w:jc w:val="center"/>
<w:tblBorders><w:top w:val="none" w:sz="0"/><w:left w:val="none" w:sz="0"/><w:bottom w:val="none" w:sz="0"/><w:right w:val="none" w:sz="0"/><w:insideH w:val="none" w:sz="0"/><w:insideV w:val="none" w:sz="0"/></w:tblBorders>
</w:tblPr>
<w:tblGrid><w:gridCol w:w="4675"/><w:gridCol w:w="4675"/></w:tblGrid>
<w:tr>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:b/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:b/></w:rPr><w:t>Zatwierdził Zamawiający</w:t></w:r></w:p></w:tc>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:b/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:b/></w:rPr><w:t>Zatwierdził Wykonawca</w:t></w:r></w:p></w:tc>
</w:tr>
<w:tr>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="360"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr><w:t>..........................................</w:t></w:r></w:p></w:tc>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="360"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr><w:t>..........................................</w:t></w:r></w:p></w:tc>
</w:tr>
<w:tr>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:sz w:val="16"/><w:i/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:sz w:val="16"/><w:i/></w:rPr><w:t>/ podpis, pieczęć /</w:t></w:r></w:p></w:tc>
<w:tc><w:tcPr><w:tcW w:w="4675" w:type="dxa"/></w:tcPr><w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:sz w:val="16"/><w:i/></w:rPr></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/><w:sz w:val="16"/><w:i/></w:rPr><w:t>/ podpis, pieczęć /</w:t></w:r></w:p></w:tc>
</w:tr>
</w:tbl>
```
"""

def systemy_list(items):
    return "\n".join(f"- {it}." for it in items)

def section_II(site):
    rn, title = HEADINGS[1]
    parts = [f"# {heading_text(rn, title)}\n"]
    if site["nr"] == 1:
        photo_path = os.path.join(PHOTOS_DIR, f"photo_{site['slug']}.png")
        parts.append(f'::: {{custom-style="ImgCenter"}}\n![]({photo_path}){{width=16cm}}\n:::\n')
    parts.append(f"**Adres obiektu:** {site['adres']}\n")
    parts.append(f"**Charakter obiektu:**\n\n{site['charakter']}\n")
    parts.append(
        "**Zakaz wnoszenia broni i materiałów niebezpiecznych:**\n\n"
        "Zgodnie z art. 40 § 1 ustawy z dnia "
        "28 stycznia 2016 r. – Prawo o prokuraturze, do budynku, w którym mieści się jednostka organizacyjna "
        "prokuratury, nie wolno wnosić broni ani amunicji, a także materiałów wybuchowych i innych środków "
        "niebezpiecznych. Zakaz ten nie dotyczy prokuratorów oraz osób wykonujących obowiązki służbowe "
        "wymagające posiadania broni. Pracownik ochrony zobowiązany jest do egzekwowania powyższego zakazu "
        "zgodnie z zasadami określonymi w Rozdziale III niniejszej Instrukcji.\n"
    )
    parts.append("**Zainstalowane systemy ochrony technicznej:**\n")
    parts.append(systemy_list(site["systemy_techniczne"]) + "\n")
    if site.get("dozor_parkingu"):
        parts.append(f"**Dozorowanie terenu / parkingu:**\n\n{site['dozor_parkingu']}\n")
    if site.get("rtg"):
        parts.append(
            "**Urządzenie wytwarzające promieniowanie jonizujące (RTG):**\n\n"
            "W obiekcie zainstalowany jest "
            "skaner rentgenowski do kontroli bagażu osób wchodzących. Zasady jego obsługi oraz wymogi "
            "formalne związane z posiadaniem zezwolenia Prezesa Państwowej Agencji Atomistyki opisano "
            "w Rozdziale III niniejszej Instrukcji.\n"
        )
    if site.get("ppoz_bezposrednie"):
        parts.append(
            "**Połączenie z systemem powiadamiania Straży Pożarnej:**\n\n"
            "System sygnalizacji pożarowej obiektu "
            "jest bezpośrednio połączony z jednostką Państwowej Straży Pożarnej.\n"
        )
    parts.append(
        "**Godziny urzędowania jednostki:**\n\n"
        "od poniedziałku do piątku w godzinach 8:00–16:00 "
        "(pięciodniowy tydzień pracy Zamawiającego), z zastrzeżeniem godzin pełnienia służby ochrony "
        "określonych w Rozdziale III, które mogą wykraczać poza godziny urzędowania jednostki.\n"
    )
    return "\n".join(parts)

def section_III(site):
    rn, title = HEADINGS[2]
    from common_blocks import build_opz_duties_section
    parts = [f"# {heading_text(rn, title)}\n"]
    parts.append(ORG_GENERAL_RULES.replace("{{OPZ_DUTIES_LIST}}", build_opz_duties_section(site)))
    parts.append("## Obsada posterunków ochrony na obiekcie {.unnumbered}\n")
    parts.append(table_to_bullets(site["tabela_obsady"]) + "\n")
    # UWAGA: nigdy nie uzywac etykiety "Uwaga szczegolowa:" (klientka: "ja tak
    # nie pisze bo to jest glupie") - dodatkowe uwagi wstawiamy jako zwykle,
    # pelne zdania, bez sztucznej etykiety z przodu.
    for uwaga in site.get("dodatkowe_uwagi", []):
        parts.append(f"{uwaga}\n")
    return "\n".join(parts)

def section_IV(site):
    rn, title = HEADINGS[3]
    return f"""# {heading_text(rn, title)}

**Przedstawiciel Zamawiającego** – osoba wyznaczona do kontaktu w postępowaniu o udzielenie zamówienia publicznego, znak: {SIGN_NUM}:

- [PRZYKŁAD, PODMIENIĆ DLA NOWEGO ZAMAWIAJĄCEGO] – dane kontaktowe osoby wskazanej w SWZ (dział, telefon, e-mail).

**Przedstawiciel Wykonawcy:**

Koordynator ochrony Wykonawcy (imię i nazwisko):

- [PRZYKŁAD] – tel., e-mail.

Dowódca obiektu (imię i nazwisko):

- [PRZYKŁAD] – tel., e-mail.

Telefony alarmowe do dyżurnego całodobowej stacji monitorowania alarmów Wykonawcy:

- [tel. kom.]
- [tel. stacjonarny]

Przedstawiciel Wykonawcy (Koordynator ochrony) będzie zobowiązany do pozostawania w stałym kontakcie telefonicznym z Zamawiającym oraz do natychmiastowego przyjazdu na każde jego wezwanie. Zmiana osób lub danych kontaktowych wskazanych powyżej będzie wymagać pisemnego powiadomienia Zamawiającego.

UWAGA (Playbook, sekcja 10): jeżeli dla danego Zamawiającego/obiektu klientka
dostarczy STARĄ, realnie używaną instrukcję zawierającą już wskazanego
koordynatora ochrony/dowódcę obiektu - dane kontaktowe w tym rozdziale
MUSZĄ być zgodne z tą starą instrukcją, a nie z placeholderami powyżej.
"""

def section_I():
    rn, title = HEADINGS[0]
    return LEGAL_BASIS.replace("# I. PODSTAWY PRAWNE DZIAŁAŃ OCHRONNYCH", f"# {heading_text(rn, title)}")

# Sciezki do 4 realnych grafik pierwszej pomocy (wyekstrahowanych z
# najnowszego wzoru klientki, patrz playbook.md sekcja 7) - podmieniac na
# aktualne pliki dla kazdego nowego zlecenia, NIE uzywac skryptow
# make_safety_graphics.py / make_pozycja_bezpieczna.py (stary standard).
GFX_NUMERY = os.path.abspath("assets/graphics_v2/numery_scenariusze.jpeg")
GFX_OPARZENIA = os.path.abspath("assets/graphics_v2/oparzenia_porazenie.jpeg")
GFX_POZYCJA = os.path.abspath("assets/graphics_v2/pozycja_bezpieczna.jpeg")
GFX_RKO = os.path.abspath("assets/graphics_v2/rko_ilustrowane.jpeg")

def section_V():
    rn, title = HEADINGS[4]
    from common_blocks import _convert_section_v_headings
    txt = SERVICE_INSTRUCTIONS.replace("# V. INSTRUKCJE SŁUŻBOWE", f"# {heading_text(rn, title)}")
    txt = _convert_section_v_headings(txt)
    txt = txt.replace("{{GRAPHIC_NUMERY}}", f'::: {{custom-style="ImgCenter"}}\n![]({GFX_NUMERY}){{width=13.73cm}}\n:::')
    txt = txt.replace("{{GRAPHIC_OPARZENIA}}", f'::: {{custom-style="ImgCenter"}}\n![]({GFX_OPARZENIA}){{width=14.23cm}}\n:::')
    txt = txt.replace("{{GRAPHIC_POZYCJA}}", f'::: {{custom-style="ImgCenter"}}\n![]({GFX_POZYCJA}){{width=14.23cm}}\n:::')
    txt = txt.replace("{{GRAPHIC_RKO}}", f'::: {{custom-style="ImgCenter"}}\n![]({GFX_RKO}){{width=14.23cm}}\n:::')
    return txt

def section_VI():
    rn, title = HEADINGS[5]
    return DOCUMENT_TEMPLATES.replace("# VI. WZORY DOKUMENTÓW SŁUŻBOWYCH", f"# {heading_text(rn, title)}")

def section_VII():
    rn, title = HEADINGS[6]
    return WYKAZ_OSOB.replace("# VII. WYKAZ OSÓB ZAPOZNANYCH Z INSTRUKCJĄ", f"# {heading_text(rn, title)}")

def build_body_sections(site):
    """Returns list of (heading_id, markdown_block) for sections I..VII."""
    return [
        ("I", section_I()),
        ("II", section_II(site)),
        ("III", section_III(site)),
        ("IV", section_IV(site)),
        ("V", section_V()),
        ("VI", section_VI()),
        ("VII", section_VII()),
    ]

def assemble(site, toc_block=None):
    """Assemble full markdown. If toc_block is None -> pass 1 (no ToC page).
    If toc_block is provided -> pass 2 (final), inserted right after cover."""
    md = [cover_page(site)]
    md.append(PAGE_BREAK)
    if toc_block is not None:
        md.append(toc_block)
        md.append(PAGE_BREAK)
    sections = build_body_sections(site)
    justify_ids = {"I", "II", "III", "IV", "V"}
    for i, (hid, block) in enumerate(sections):
        if hid in justify_ids:
            block = f'::: {{custom-style="Justify"}}\n{block}\n:::\n'
        md.append(block)
        if i < len(sections) - 1:
            md.append(PAGE_BREAK)
    return "\n\n".join(md)

def run_pandoc(md_path, docx_path):
    cmd = [
        "pandoc", md_path, "-f", "markdown", "-t", "docx",
        "-o", docx_path,
        f"--reference-doc={REF_DOCX}",
    ]
    subprocess.run(cmd, check=True)
    center_chapter_headings(docx_path)
    # Wymog klientki: odstep (pusta linia) po KAZDEJ liscie (numerowanej,
    # literowanej lub wypunktowanej), przed kolejnym akapitem spoza listy.
    add_spacing_after_lists(docx_path)

def center_chapter_headings(docx_path):
    """Wysrodkowuje tytuly rozdzialow (I., II., III. ... - styl Heading1),
    dokladnie tak jak w prawdziwym, zaakceptowanym wzorze klienta (Prokuratura
    Okregowa w Lodzi), gdzie kazdy naglowek rozdzialu ma bezposrednie
    formatowanie <w:jc w:val="center"/> na poziomie akapitu. Styl "Heading1"
    sam w sobie NIE wymusza wyrownania (dziedziczy z "Normal" - do lewej),
    dlatego wyrownanie trzeba ustawic osobno na kazdym naglowku rozdzialu po
    konwersji pandoc -> docx. Akapit "Spis tresci" (tez styl Heading1) celowo
    NIE jest dotykany - w oryginalnym wzorze zostaje wyrownany do lewej."""
    import docx as _docx
    from docx.enum.text import WD_ALIGN_PARAGRAPH as _ALIGN
    chapter_titles = {heading_text(rn, title) for rn, title in HEADINGS}
    d = _docx.Document(docx_path)
    for p in d.paragraphs:
        if p.style and p.style.name == "Heading 1" and p.text.strip() in chapter_titles:
            p.alignment = _ALIGN.CENTER
    d.save(docx_path)

def render_pdf(docx_path, outdir):
    subprocess.run([
        "soffice", "--headless", "--convert-to", "pdf", docx_path, "--outdir", outdir
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def find_heading_pages(pdf_path, n_pages_hint=20):
    """Return dict heading_id -> 1-based page number, by scanning pdftotext per page."""
    out = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True, check=True)
    pages = out.stdout.split("\x0c")  # form feed separates pages
    result = {}
    for rn, title in HEADINGS:
        needle = re.sub(r"\s+", " ", heading_text(rn, title)).strip()
        for i, ptext in enumerate(pages, start=1):
            norm = re.sub(r"\s+", " ", ptext)
            if needle in norm:
                result[rn] = i
                break
    return result

def xml_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def make_toc_block(page_map):
    paras = ['<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Spis treści</w:t></w:r></w:p>']
    for rn, title in HEADINGS:
        pg = str(page_map.get(rn, "?"))
        entry = xml_escape(f"{rn}. {title}")
        p = (
            '<w:p><w:pPr><w:pStyle w:val="TocEntry"/>'
            '<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>'
            '</w:pPr>'
            f'<w:r><w:t xml:space="preserve">{entry}</w:t></w:r>'
            '<w:r><w:tab/></w:r>'
            f'<w:r><w:t>{pg}</w:t></w:r></w:p>'
        )
        paras.append(p)
    body = "\n".join(paras)
    return "```{=openxml}\n" + body + "\n```\n"

# ---------------------------------------------------------------------------
def main():
    for site in SITES:
        slug = site["slug"]

        # ---- PASS 1: no ToC, to measure page numbers ----
        md1 = assemble(site, toc_block=None)
        md1_path = os.path.join(DRAFT_DIR, f"{slug}_pass1.md")
        with open(md1_path, "w", encoding="utf-8") as f:
            f.write(md1)
        docx1 = os.path.join(DRAFT_DIR, f"{slug}_pass1.docx")
        run_pandoc(md1_path, docx1)
        render_pdf(docx1, DRAFT_DIR)
        pdf1 = os.path.join(DRAFT_DIR, f"{slug}_pass1.pdf")
        page_map = find_heading_pages(pdf1)
        # shift by 1 page because final doc has an extra ToC page inserted after cover
        page_map_shifted = {k: v + 1 for k, v in page_map.items()}

        # ---- PASS 2: final, with computed static ToC ----
        toc_block = make_toc_block(page_map_shifted)
        md2 = assemble(site, toc_block=toc_block)
        md2_path = os.path.join(OUT_MD, f"{slug}.md")
        with open(md2_path, "w", encoding="utf-8") as f:
            f.write(md2)
        final_docx = os.path.join(OUT_DOCX, f"Instrukcja_ochrony_{slug}.docx")
        run_pandoc(md2_path, final_docx)
        print(f"OK {slug}: strony sekcji = {page_map_shifted}")

    print("Zakonczono generowanie wszystkich plikow.")

if __name__ == "__main__":
    main()
