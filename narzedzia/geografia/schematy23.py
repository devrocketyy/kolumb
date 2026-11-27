# Schematy geografii — porcja 23 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Hydrogram: zlewnia leśna a zurbanizowana ----------
_h = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for i, v in enumerate((0, 6, 14, 10, 4, 0)):
    _h += f'<rect class="gw2 ol" x="{60 + i * 14}" y="40" width="12" height="{v * 4}"/>'
_h += '<text class="ts" x="60" y="32">opad</text>'
_h += '<path class="s" d="M50 260 H380 M50 110 V260"/>'
_h += '<path class="hot" fill="none" d="M50 245 C100 245 120 120 150 120 C180 120 190 230 260 240 C300 245 340 245 380 245" style="stroke-width:2.6"/>'
_h += '<path class="cold" fill="none" d="M50 245 C120 245 150 200 200 190 C250 185 290 225 380 238" style="stroke-width:2.6"/>'
_h += '<path class="dash" d="M95 80 V260"/><path class="dash" d="M150 120 V260"/><path class="dash" d="M200 190 V260"/>'
_h += '<text class="ts" x="215" y="278" text-anchor="middle">czas →</text><text class="ts" x="44" y="120" text-anchor="end">Q</text>'
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Hydrogram: zlewnia zurbanizowana a leśna', svg=_h,
      znaczniki=[(150, 120, 230, 100, 'Zlewnia miejska', 'Wysoka, szybka kulminacja — beton i kanalizacja odprowadzają wodę natychmiast'),
                 (200, 190, 290, 170, 'Zlewnia leśna', 'Niska, późna kulminacja — las i gleba zatrzymują wodę'),
                 (95, 80, 30, 70, 'Maksimum opadu', 'Punkt odniesienia do liczenia czasu opóźnienia'),
                 (122, 255, 120, 285, 'Krótki czas opóźnienia', 'W mieście kulminacja następuje niedługo po deszczu')],
      opis='Porównanie reakcji dwóch zlewni na ten sam opad — wykres autorski IndexLab (wartości względne).',
      uwaga='Uszczelnianie powierzchni (asfalt, dachy) skraca czas opóźnienia i podnosi kulminację — rośnie ryzyko powodzi błyskawicznych. Zieleń, retencja i ogrody deszczowe działają odwrotnie.'),
]

# ---------- 2. Wulkan tarczowy a stratowulkan ----------
_v = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_v += '<path class="gm2 ol" d="M10 240 C60 200 120 170 150 165 C180 170 220 200 260 240 Z" style="opacity:.9"/>'
_v += '<path class="gs ol" d="M250 240 L320 70 L330 70 L395 240 Z"/>'
for k in range(1, 5):
    y = 240 - k * 34
    _v += f'<path class="s" d="M{250 + k * 14} {y} L{395 - k * 13} {y}" style="stroke-width:.8"/>'
_v += '<path class="gm" d="M321 70 L323 240 L327 240 L329 70 Z"/><path class="gm" d="M147 165 L149 240 L152 240 L154 165 Z"/>'
_v += '<path class="gk ol" d="M300 40 C310 20 340 20 350 40 C365 45 355 60 340 58 C330 66 312 62 305 55 C290 55 290 42 300 40 Z"/>'
_v += '<path class="gt ol" d="M0 240 H400 V300 H0 Z"/>'
_v += '<text class="tb" x="135" y="275" text-anchor="middle">wulkan tarczowy</text><text class="tb" x="323" y="275" text-anchor="middle">stratowulkan</text>'
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Wulkan tarczowy a stratowulkan — porównanie', svg=_v,
      znaczniki=[(80, 200, 40, 150, 'Łagodne stoki', 'Rzadka lawa bazaltowa rozlewa się szeroko (Mauna Loa)'),
                 (300, 140, 230, 110, 'Warstwy lawy i popiołów', 'Lepka lawa i materiał piroklastyczny na zmianę'),
                 (325, 45, 260, 30, 'Chmura erupcyjna', 'Wybuchowe erupcje — popioły, lawiny piroklastyczne'),
                 (150, 200, 200, 200, 'Komin', 'Droga magmy z ogniska do krateru')],
      opis='Porównanie dwóch głównych typów wulkanów (bez zachowania skali) — rysunek autorski IndexLab.',
      uwaga='Tarczowe: plamy gorąca i ryfty (Hawaje, Islandia), erupcje wylewne. Stratowulkany: strefy subdukcji (Fudżi, Etna, Andy), erupcje wybuchowe i największe zagrożenie dla ludzi.'),
]

# ---------- 3. Skala Mohsa ----------
_m = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
mins = ['talk', 'gips', 'kalcyt', 'fluoryt', 'apatyt', 'ortoklaz', 'kwarc', 'topaz', 'korund', 'diament']
for i, n in enumerate(mins):
    h = 18 + i * 20
    x = 20 + i * 37
    cls = 'gp' if i < 2 else ('gc' if i < 5 else ('gs2' if i < 8 else 'gi'))
    _m += f'<rect class="{cls} ol" x="{x}" y="{250 - h}" width="30" height="{h}"/>'
    _m += f'<text class="tb" x="{x + 15}" y="{245 - h}" text-anchor="middle">{i + 1}</text>'
    _m += f'<text class="ts" x="{x + 15}" y="{265 + (i % 2) * 14}" text-anchor="middle">{n}</text>'
_m += '<path class="s" d="M15 250 H390"/>'
S['g-skaly'] = [
 dict(typ='rysunek', tytul='Skala twardości Mohsa', svg=_m,
      znaczniki=[(35, 225, 60, 150, 'Paznokieć (ok. 2,5)', 'Zarysuje talk i gips'),
                 (220, 120, 150, 95, 'Nóż stalowy (ok. 5,5)', 'Zarysuje minerały do apatytu'),
                 (257, 115, 300, 60, 'Kwarc (7)', 'Rysuje szkło; główny składnik piasku'),
                 (368, 52, 330, 25, 'Diament (10)', 'Najtwardszy minerał naturalny')],
      opis='Dziesięć minerałów wzorcowych skali Mohsa (skala porządkowa, nie liniowa) — rysunek autorski IndexLab.',
      uwaga='Skala Mohsa jest względna: każdy minerał rysuje te o niższym numerze. Różnica twardości między korundem (9) a diamentem (10) jest wielokrotnie większa niż między talkiem a gipsem.'),
]

# ---------- 4. Pustynnienie Sahelu — sprzężenie ----------
_p = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
kroki = ['susza', 'mniej roślin', 'nadmierny wypas i wycinka', 'odsłonięta gleba', 'erozja i wyższe albedo', 'jeszcze mniej opadów']
cx, cy, r = 200, 150, 105
pts = []
for i, k in enumerate(kroki):
    a = math.radians(-90 + i * 60)
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    pts.append((x, y))
    w = len(k) * 6.2 + 16
    _p += f'<rect class="{"gp" if i % 2 else "gc"} ol" x="{x - w / 2:.0f}" y="{y - 13:.0f}" width="{w:.0f}" height="26" rx="8"/><text class="tb" x="{x:.0f}" y="{y + 5:.0f}" text-anchor="middle">{k}</text>'
for i in range(6):
    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 6]
    mx1, my1 = x1 + (x2 - x1) * 0.3, y1 + (y2 - y1) * 0.3
    mx2, my2 = x1 + (x2 - x1) * 0.7, y1 + (y2 - y1) * 0.7
    _p += strz(mx1, my1, mx2, my2, 'hot')
S['g-rolnictwo'] = [
 dict(typ='rysunek', tytul='Pustynnienie Sahelu — błędne koło', svg=_p,
      znaczniki=[(200, 45, 270, 20, 'Susza', 'Słabsze deszcze monsunu zachodnioafrykańskiego'),
                 (291, 202, 330, 280, 'Nadmierny wypas', 'Rosnąca liczba ludzi i stad, wycinka drzew na opał'),
                 (109, 202, 30, 125, 'Wyższe albedo', 'Jasna, naga ziemia odbija więcej promieniowania — mniej konwekcji'),
                 (200, 150, 200, 150, 'Sprzężenie zwrotne', 'Każdy etap nasila kolejny — proces sam się napędza')],
      opis='Model przyczyn i skutków pustynnienia na obszarach suchych — rysunek autorski IndexLab.',
      uwaga='Przerwanie koła: zalesianie (Wielki Zielony Mur), ograniczenie wypasu, kamienne wały zatrzymujące wodę, rolnictwo przystosowane do suszy.'),
]

# ---------- 5. Model stacji na mapie synoptycznej ----------
_s = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_s += '<circle class="s" cx="200" cy="150" r="22" style="fill:none;stroke-width:2"/>'
_s += '<path class="d" d="M200 150 L200 128 A22 22 0 0 1 222 150 Z"/>'   # zachmurzenie 2/8 (ćwiartka)
_s += '<path class="s" d="M215 135 L275 75" style="stroke-width:2"/>'      # trzon wiatru — wieje z NE
_s += '<path class="s" d="M275 75 L295 85 M265 85 L282 93" style="stroke-width:2"/>'
_s += '<text class="tb" x="150" y="130" text-anchor="end">18</text>'
_s += '<text class="tb" x="150" y="182" text-anchor="end">12</text>'
_s += '<text class="tb" x="245" y="182">1012</text>'
_s += '<text class="tb" x="140" y="157" text-anchor="end">≡</text>'
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Model stacji na mapie synoptycznej', svg=_s,
      znaczniki=[(150, 125, 70, 90, 'Temperatura', 'Lewy górny róg — temperatura powietrza w °C'),
                 (150, 177, 70, 220, 'Punkt rosy', 'Lewy dolny róg — temperatura punktu rosy'),
                 (245, 177, 320, 220, 'Ciśnienie', 'Prawy dolny róg — ciśnienie w hPa'),
                 (210, 140, 300, 120, 'Zachmurzenie', 'Wypełnienie kółka w oktantach (tu ok. 2/8)'),
                 (270, 80, 330, 40, 'Wiatr', 'Trzon wskazuje, skąd wieje (tu z NE); kreski — prędkość'),
                 (138, 153, 60, 160, 'Zjawisko', 'Symbol pogody, np. ≡ — mgła')],
      opis='Uproszczony model zapisu danych stacji meteorologicznej na mapie synoptycznej — rysunek autorski IndexLab.',
      uwaga='Różnica temperatury i punktu rosy mówi o wilgotności: im mniejsza, tym powietrze bliższe nasycenia (mgła, opady). Kierunek wiatru odczytujesz od końca trzonu do kółka.'),
]


def _dopasuj(z):
    out = []
    for (x, y, lx, ly, n, d) in z:
        w = len(n) * 6.4 + 16
        if lx > x and lx + w > 400:
            lx = max(x - 25, w)
        elif lx <= x and lx - w < 0:
            lx = min(x + 25, 400 - w)
        if lx <= x and lx > x - 5:
            lx = x - 5
        out.append((x, y, round(lx), ly, n, d))
    return out


for _v in S.values():
    for _s in _v:
        _s['znaczniki'] = _dopasuj(_s['znaczniki'])
