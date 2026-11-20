# Schematy biologii — porcja 5: rysunki z fizjologii człowieka (autorskie, uproszczone).
S = {}


def rura(d, w=9):
    """Kanalik lub naczynie: podwójny kontur."""
    return (f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="var(--surface-2)" stroke-width="{w - 4}" stroke-linecap="round" stroke-linejoin="round"/>')


def kropki(pts, r=2):
    return ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts)


# ---------- neuron ----------
_neuron = (
    '<path class="s" d="M62 136 l-20 -25 l-12 -14 M42 111 l-20 2 M60 160 l-25 20 l-16 0 M35 180 l-6 22 M80 124 l5 -35 l-10 -22 M85 89 l16 -18 M76 176 l-4 36 l10 22 M72 212 l-14 14"/>'
    '<circle class="f" cx="80" cy="150" r="27"/><circle class="f2" cx="78" cy="150" r="10"/><circle class="d" cx="80" cy="148" r="3"/>'
    '<path class="f" d="M105 141 L126 147 L126 153 L105 159 Z"/>'
    '<line class="s" x1="126" y1="150" x2="332" y2="150"/>'
    + ''.join(f'<rect class="f2" x="{x}" y="142" width="34" height="16" rx="7"/>' for x in (135, 177, 219, 261))
    + '<path class="s" d="M332 150 l24 -30 M332 150 l28 0 M332 150 l24 30"/>'
    + '<circle class="f" cx="358" cy="118" r="7"/><circle class="f" cx="364" cy="150" r="7"/><circle class="f" cx="358" cy="182" r="7"/>'
)

# ---------- synapsa ----------
_syn = (
    '<path class="f" d="M150 0 L150 60 Q118 92 140 140 Q200 170 260 140 Q282 92 250 60 L250 0 Z"/>'
    '<path class="f2" d="M90 186 Q200 164 310 186 L310 300 L90 300 Z"/>'
    '<g transform="translate(200 38)"><ellipse class="f" cx="0" cy="0" rx="24" ry="10"/><path class="s2" d="M-16 -5 l6 10 l6 -10 l6 10 l6 -10 l6 10"/></g>'
    + ''.join(f'<circle class="s" cx="{x}" cy="{y}" r="9"/>' + kropki([(x - 3, y - 2), (x + 3, y + 2), (x, y + 4)], 1.4) for x, y in ((176, 104), (202, 92), (228, 108), (190, 128), (222, 132)))
    + kropki([(190, 162), (204, 166), (216, 161), (198, 158)], 1.6)
    + ''.join(f'<rect class="d" x="{x - 3}" y="171" width="6" height="9" rx="1"/>' for x in (180, 200, 220))
    + ''.join(f'<rect class="s" x="{x}" y="{y}" width="6" height="10" rx="1"/>' for x, y in ((150, 134), (244, 134)))
    + '<text class="t" x="20" y="18">impuls nerwowy ↓</text>'
)

# ---------- serce (widok od przodu) ----------
_serce = (
    '<rect class="f" x="40" y="80" width="110" height="75" rx="18"/>'
    '<rect class="f" x="250" y="80" width="110" height="75" rx="18"/>'
    '<path class="f" d="M40 165 L195 165 L195 225 Q150 288 100 282 Q40 272 40 222 Z"/>'
    '<path class="f" d="M205 165 L360 165 L360 212 Q350 292 262 290 Q205 282 205 232 Z"/>'
    '<rect class="f2" x="195" y="165" width="10" height="78"/>'
    '<path class="f" d="M168 165 L168 40 Q168 26 150 26 L110 26 L110 12 L150 12 Q192 12 192 40 L192 165 Z"/>'
    '<path class="f" d="M208 165 L208 30 Q208 6 240 6 L300 6 Q330 6 330 30 L330 60 L310 60 L310 32 Q310 24 300 24 L245 24 Q232 24 232 34 L232 165 Z"/>'
    '<rect class="f" x="72" y="8" width="28" height="74"/>'
    '<rect class="f" x="358" y="92" width="34" height="14"/><rect class="f" x="358" y="126" width="34" height="14"/>'
    '<path class="s" d="M74 155 l14 16 M126 155 l-14 16 M282 155 l14 16 M332 155 l-14 16"/>'
    '<path class="s" d="M170 170 q5 -7 10 0 q5 -7 10 0 M210 170 q5 -7 10 0 q5 -7 10 0"/>'
    '<text class="t" x="44" y="298">strona prawa</text><text class="t" x="300" y="298">strona lewa</text>'
)

# ---------- nefron ----------
_nefron = (
    '<circle class="f" cx="70" cy="70" r="32"/><circle cx="70" cy="70" r="26" fill="var(--surface)" stroke="currentColor" stroke-width="1.2"/>'
    '<path class="s" d="M8 60 L48 64 c10 -14 26 -10 22 2 c-4 10 14 14 16 2 c2 -12 -18 -16 -22 -4 c-4 12 14 20 18 8 c2 -6 -6 -10 -10 -4 L48 78 L8 84"/>'
    + rura('M96 88 c20 14 2 34 26 38 s22 -30 40 -14 s-4 30 22 32 L200 120 L200 262 Q212 282 224 262 L224 122 c10 -24 30 -6 40 -24 s-6 -24 18 -26 s30 10 46 -6')
    + '<path d="M332 30 L332 292" fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round"/>'
      '<path d="M332 30 L332 292" fill="none" stroke="var(--surface-2)" stroke-width="10" stroke-linecap="round"/>'
    + '<text class="t" x="44" y="118">krew</text><text class="t" x="300" y="296">mocz ↓</text>'
)

S['b-nerwy'] = [
    dict(typ='rysunek', tytul='Budowa neuronu', svg=_neuron,
         znaczniki=[
             (42, 111, 22, 40, 'Dendryt', 'przewodzi impulsy do ciała komórki'),
             (94, 168, 120, 250, 'Ciało komórki (perykarion)', 'zawiera jądro i większość organelli'),
             (78, 150, 40, 250, 'Jądro komórkowe', ''),
             (116, 150, 140, 70, 'Wzgórek aksonu', 'tu powstaje potencjał czynnościowy'),
             (236, 142, 236, 70, 'Osłonka mielinowa', 'izoluje akson, przyspiesza przewodzenie'),
             (173, 150, 200, 250, 'Przewężenie Ranviera', 'przewodzenie skokowe'),
             (318, 150, 318, 70, 'Akson (neuryt)', 'przewodzi impulsy od ciała komórki'),
             (364, 150, 380, 240, 'Zakończenie aksonu (kolbka synaptyczna)', 'uwalnianie neuroprzekaźnika'),
         ],
         opis='Neuron ruchowy z aksonem otoczonym osłonką mielinową.',
         uwaga='Impuls biegnie zawsze w kierunku: dendryty → ciało komórki → akson → zakończenia aksonu. W aksonach z mieliną przeskakuje między przewężeniami Ranviera.'),
    dict(typ='rysunek', tytul='Synapsa chemiczna', svg=_syn,
         znaczniki=[
             (152, 40, 60, 40, 'Kolbka presynaptyczna', 'zakończenie aksonu'),
             (176, 104, 60, 100, 'Pęcherzyk synaptyczny', 'zawiera neuroprzekaźnik'),
             (200, 38, 340, 30, 'Mitochondrium', 'dostarcza ATP do uwalniania przekaźnika'),
             (153, 139, 60, 160, 'Kanał wapniowy', 'napływ Ca²⁺ uruchamia egzocytozę'),
             (204, 166, 350, 110, 'Neuroprzekaźnik', 'np. acetylocholina'),
             (232, 165, 350, 160, 'Szczelina synaptyczna', ''),
             (200, 176, 250, 250, 'Receptor błony postsynaptycznej', 'wiąże neuroprzekaźnik, otwiera kanały jonowe'),
             (120, 182, 60, 230, 'Błona postsynaptyczna', ''),
         ],
         opis='Przekazywanie impulsu z neuronu na kolejną komórkę.',
         uwaga='Synapsa przewodzi jednokierunkowo: receptory są tylko na błonie postsynaptycznej, a pęcherzyki — tylko w kolbce presynaptycznej.'),
]

S['b-krazenie'] = [
    dict(typ='rysunek', tytul='Budowa serca człowieka', svg=_serce,
         znaczniki=[
             (95, 117, 18, 145, 'Prawy przedsionek', 'przyjmuje krew odtlenowaną z żył głównych'),
             (110, 225, 18, 250, 'Prawa komora', 'tłoczy krew do pnia płucnego'),
             (305, 117, 385, 175, 'Lewy przedsionek', 'przyjmuje krew natlenioną z żył płucnych'),
             (285, 230, 385, 250, 'Lewa komora', 'najgrubsza ściana, tłoczy krew do aorty'),
             (300, 15, 380, 40, 'Aorta', 'krwiobieg duży'),
             (180, 100, 150, 50, 'Pień płucny', 'krwiobieg mały'),
             (86, 40, 30, 30, 'Żyła główna górna', ''),
             (380, 133, 385, 70, 'Żyły płucne', 'krew natleniona z płuc'),
             (100, 163, 18, 190, 'Zastawka trójdzielna', ''),
             (307, 163, 385, 205, 'Zastawka dwudzielna (mitralna)', ''),
             (200, 225, 200, 290, 'Przegroda międzykomorowa', 'oddziela krew natlenioną od odtlenowanej'),
         ],
         opis='Schemat serca w widoku od przodu (jak u osoby stojącej naprzeciw).',
         uwaga='Na rysunkach serca prawa strona serca leży po lewej stronie obrazka. Ściana lewej komory jest najgrubsza, bo tłoczy krew do całego ciała.'),
]

S['b-wydalanie'] = [
    dict(typ='rysunek', tytul='Budowa nefronu', svg=_nefron,
         znaczniki=[
             (68, 70, 20, 130, 'Kłębuszek nerkowy', 'sieć naczyń włosowatych — filtracja'),
             (70, 39, 130, 20, 'Torebka Bowmana', 'zbiera przesącz (mocz pierwotny)'),
             (20, 61, 20, 20, 'Tętniczka doprowadzająca', ''),
             (20, 83, 20, 190, 'Tętniczka odprowadzająca', 'węższa — utrzymuje wysokie ciśnienie w kłębuszku'),
             (150, 116, 120, 200, 'Kanalik kręty I rzędu', 'resorpcja glukozy, aminokwasów, jonów i wody'),
             (212, 272, 140, 280, 'Pętla Henlego', 'zagęszczanie moczu'),
             (282, 72, 270, 20, 'Kanalik kręty II rzędu', 'sekrecja i resorpcja jonów (aldosteron)'),
             (332, 200, 385, 200, 'Kanalik zbiorczy', 'resorpcja wody pod wpływem ADH'),
         ],
         opis='Nefron — podstawowa jednostka czynnościowa nerki.',
         uwaga='Ciałko nerkowe (kłębuszek z torebką) leży w korze nerki, pętla Henlego sięga do rdzenia.'),
]
