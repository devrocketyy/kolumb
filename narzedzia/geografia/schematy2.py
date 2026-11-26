# Schematy geografii — porcja 2 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
S = {}
MIES = 'IFMAMJJASOND'


def klimatogram(temp, opady, tmin=-10, tmax=30, pmax=400, x0=45, x1=330, y0=250, y1=40):
    """Klimatogram: słupki opadów (gw2), linia temperatury (hot), dwie osie z podziałką."""
    w = (x1 - x0) / 12
    ty = lambda t: y0 - (y0 - y1) * (t - tmin) / (tmax - tmin)
    out = ''.join(f'<path class="dash" d="M{x0} {ty(t):.1f} H{x1}"/>' for t in range(tmin, tmax + 1, 10))
    for i, p in enumerate(opady):
        h = (y0 - y1) * p / pmax
        out += f'<rect class="gw2" x="{x0 + i * w + 3:.1f}" y="{y0 - h:.1f}" width="{w - 6:.1f}" height="{h:.1f}"/>'
    pts = [(x0 + (i + 0.5) * w, ty(t)) for i, t in enumerate(temp)]
    out += '<polyline class="hot" fill="none" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'
    out += ''.join(f'<circle class="hotf" cx="{x:.1f}" cy="{y:.1f}" r="2.4"/>' for x, y in pts)
    out += f'<path class="s" d="M{x0} {y1} V{y0} H{x1} V{y1}"/>'
    for t in range(tmin, tmax + 1, 10):
        out += f'<path class="s" d="M{x0 - 4} {ty(t):.1f} H{x0}"/><text class="ts" x="{x0 - 6}" y="{ty(t) + 3:.1f}" text-anchor="end">{t}</text>'
    for k in range(0, pmax + 1, pmax // 4):
        yy = y0 - (y0 - y1) * k / pmax
        out += f'<path class="s" d="M{x1} {yy:.1f} H{x1 + 4}"/><text class="ts" x="{x1 + 6}" y="{yy + 3:.1f}">{k}</text>'
    out += ''.join(f'<text class="ts" x="{x0 + (i + 0.5) * w:.1f}" y="{y0 + 13}" text-anchor="middle">{m}</text>' for i, m in enumerate(MIES))
    out += f'<text class="ts" x="{x0 - 6}" y="{y1 - 8}" text-anchor="end">°C</text><text class="ts" x="{x1 + 6}" y="{y1 - 8}">mm</text>'
    tsr = sum(temp) / 12
    tt = f'{tsr:.1f}'.replace('.', ',')
    out += (f'<text class="tb" x="{(x0 + x1) / 2:.0f}" y="{y0 + 32}" text-anchor="middle">'
            f'średnia {tt}°C · amplituda {max(temp) - min(temp)}°C · suma opadów {sum(opady)} mm</text>')
    return out, ty, w


def kx(i, x0=45, x1=330):
    return x0 + (i + 0.5) * (x1 - x0) / 12


# ---------- klimatogramy ----------
_rT, _rP = [27, 27, 27, 27, 27, 26, 26, 26, 27, 27, 27, 27], [250, 230, 260, 280, 240, 180, 170, 180, 200, 240, 260, 270]
_r, _ty, _ = klimatogram(_rT, _rP)
_sT, _sP = [10, 11, 13, 15, 19, 23, 26, 26, 23, 19, 14, 11], [80, 70, 55, 40, 25, 8, 2, 4, 25, 60, 85, 90]
_s, _ty2, _ = klimatogram(_sT, _sP, tmin=0, tmax=30, pmax=120)
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat równikowy wilgotny', svg=_r,
      znaczniki=[(kx(1), _ty(27), 95, 20, 'Temperatura', 'Ok. 26–27°C przez cały rok — amplituda roczna tylko ok. 1°C'),
                 (kx(3), 250 - 210 * 280 / 400, 150, 90, 'Opady', 'Obfite w każdym miesiącu, suma ok. 2800 mm'),
                 (kx(7), 250 - 210 * 170 / 400, 190, 120, 'Najsuchszy', 'Nawet najsuchszy miesiąc ma ponad 150 mm'),
                 (kx(9), _ty(0), 200, 200, 'Brak zimy', 'Temperatura nigdy nie zbliża się do 0°C')],
      opis='Klimatogram autorski stacji w Kotlinie Konga (dane przybliżone).',
      uwaga='Mała amplituda + wysoka temperatura + obfite opady przez cały rok = klimat równikowy wilgotny (las deszczowy).'),
 dict(typ='rysunek', tytul='Klimatogram: klimat śródziemnomorski', svg=_s,
      znaczniki=[(kx(6), _ty2(26), 200, 30, 'Gorące lato', 'Lipiec i sierpień ok. 26°C'),
                 (kx(6), 248, 175, 200, 'Susza letnia', 'Lipiec ok. 2 mm — dominuje wyż zwrotnikowy'),
                 (kx(11), 250 - 210 * 90 / 120, 230, 140, 'Wilgotna zima', 'Najwięcej opadów XI–I — niże z zachodu'),
                 (kx(0), _ty2(10), 70, 60, 'Łagodna zima', 'Brak miesięcy poniżej 0°C')],
      opis='Klimatogram autorski stacji w południowej Europie (dane przybliżone).',
      uwaga='Na półkuli N suche, gorące lato przypada na VI–VIII. Zimą strefa wiatrów zachodnich przesuwa się na południe i przynosi deszcze.'),
]

# ---------- doliny V i U ----------
_vu = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gs2" d="M10 60 L15 60 L80 228 L100 228 L165 60 L190 60 L190 290 L10 290 Z"/>'
       '<path class="gs" d="M10 60 L15 60 L80 228 L100 228 L165 60 L190 60 L190 120 L170 120 L105 250 L75 250 L10 110 Z" opacity="0.85"/>'
       '<path class="gw2" d="M80 228 L100 228 L96 240 L84 240 Z"/>'
       + ''.join(f'<path class="gf2" d="M{x} {y} l-6 0 l6 -13 l6 13 Z"/>' for x, y in ((22, 78), (34, 108), (160, 78), (148, 108)))
       + '<path class="gs2" d="M210 60 L225 60 C232 150 250 225 300 228 C350 225 368 150 375 60 L390 60 L390 290 L210 290 Z"/>'
       '<path class="gs" d="M210 60 L225 60 C232 150 250 225 300 228 C350 225 368 150 375 60 L390 60 L390 115 L380 115 C372 190 350 248 300 250 C250 248 228 190 220 115 L210 115 Z" opacity="0.85"/>'
       '<path class="gw2" d="M272 228 C285 232 315 232 328 228 Z" style="stroke:none"/><ellipse class="gw" cx="300" cy="228" rx="26" ry="3"/>'
       '<path class="gc" d="M238 200 q8 -10 16 0 Z M346 200 q8 -10 16 0 Z"/>'
       '<path class="gi" style="stroke-dasharray:4 3;fill:none" d="M222 75 C230 160 252 222 300 225 C348 222 370 160 378 75"/>'
       '<text class="ts" x="300" y="70" text-anchor="middle">dawna powierzchnia lodowca</text>'
       '<text class="tb" x="90" y="282" text-anchor="middle">dolina rzeczna V</text><text class="tb" x="300" y="282" text-anchor="middle">dolina lodowcowa U (żłób)</text>')
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Dolina rzeczna V i dolina lodowcowa U', svg=_vu,
      znaczniki=[(90, 234, 120, 255, 'Potok', 'Erozja wgłębna pogłębia wąskie dno'),
                 (45, 150, 60, 25, 'Stoki V', 'Strome, proste; spłukiwanie i ruchy masowe'),
                 (300, 228, 312, 262, 'Płaskie dno', 'Wyżłobione przez lodowiec; jeziora polodowcowe'),
                 (228, 140, 245, 30, 'Strome ściany', 'Wygładzone przez lód'),
                 (354, 196, 330, 170, 'Morena', 'Wał materiału pozostawiony przez lodowiec'),
                 (300, 70, 290, 50, 'Zasięg lodu', 'Grubość dawnego lodowca')],
      opis='Porównanie przekrojów doliny rzecznej (V) i lodowcowej (U).',
      uwaga='Kształt U jest dowodem dawnego zlodowacenia gór — w Tatrach np. Dolina Pięciu Stawów Polskich, Dolina Białki.'),
]

# ---------- meander ----------
_rz = 'M-10 190 C40 190 60 70 120 70 C180 70 210 225 275 225 C335 225 360 120 410 120'
_md = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<path class="gp ol" d="M82 105 C100 84 140 84 158 105 C140 96 100 96 82 105 Z"/>'
       '<path class="gp ol" d="M238 192 C256 212 294 212 312 192 C294 203 256 203 238 192 Z" transform="rotate(180 275 200)"/>'
       f'<path d="{_rz}" style="fill:none;stroke:var(--g-woda2);stroke-width:16;stroke-linecap:round"/>'
       f'<path d="{_rz}" style="fill:none;stroke:var(--g-woda);stroke-width:10;stroke-linecap:round"/>'
       '<path class="s" d="M95 52 l-2 -7 M110 50 l0 -7 M125 50 l1 -7 M140 53 l3 -7 M258 243 l-2 7 M273 245 l0 7 M288 244 l2 7"/>'
       '<path class="gw ol" d="M30 250 C10 240 20 215 50 220 C75 224 95 240 120 236 C100 255 60 262 30 250 Z"/>'
       '<path class="dash" d="M18 238 C40 200 90 215 130 232"/>'
       + ''.join(f'<path class="gf2" d="M{x} {y} l-5 0 l5 -11 l5 11 Z"/>' for x, y in ((200, 50), (215, 40), (350, 270), (370, 262), (30, 120), (45, 110), (330, 60)))
       + '<path class="cold" d="M355 118 q10 -6 22 -6"/><path class="coldf" d="M380 112 l-8 -4 l0 8 Z"/>')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Meander i starorzecze', svg=_md,
      znaczniki=[(118, 52, 160, 25, 'Brzeg wklęsły', 'Erozja boczna — nurt podcina brzeg, powstaje skarpa'),
                 (120, 96, 170, 125, 'Łacha', 'Brzeg wypukły — akumulacja piasku przy wolnym nurcie'),
                 (275, 200, 230, 160, 'Brzeg wypukły', 'Wewnątrz zakola — łacha meandrowa'),
                 (273, 246, 320, 280, 'Skarpa', 'Brzeg wklęsły — erozja boczna'),
                 (60, 238, 90, 280, 'Starorzecze', 'Odcięty dawny meander — jezioro w dnie doliny'),
                 (365, 116, 340, 85, 'Nurt', 'Rzeka płynie z zachodu na wschód')],
      opis='Rzeka meandrująca w dnie doliny nizinnej (widok z góry).',
      uwaga='Na brzegu wklęsłym przeważa erozja, na wypukłym — akumulacja. Gdy rzeka przetnie szyję meandra, zakole zostaje odcięte i powstaje starorzecze.'),
]

# ---------- wydmy ----------
_wd = ('<rect class="gp" x="0" y="0" width="400" height="300" opacity="0.45"/>'
       '<path class="s" d="M200 20 V270" style="stroke-dasharray:4 3"/>'
       # wydma paraboliczna: ramiona pod wiatr (na zachód), czoło na wschód
       '<path class="gp ol" d="M40 70 C90 60 140 80 160 140 C140 200 90 220 40 210 L45 196 C85 200 120 185 135 140 C120 100 85 88 45 84 Z"/>'
       '<path class="gc" d="M118 88 C140 100 158 120 160 140 C158 160 140 182 118 194 C135 175 145 160 146 140 C145 120 135 105 118 88 Z" opacity="0.8"/>'
       + ''.join(f'<path class="gt" d="M{x} {y} l-4 0 l4 -8 l4 8 Z"/>' for x, y in ((48, 80), (60, 82), (50, 206), (62, 204)))
       # barchan: ramiona z wiatrem (na wschód)
       + '<path class="gp ol" d="M250 140 C250 95 290 75 360 70 C320 90 300 115 300 140 C300 165 320 190 360 210 C290 205 250 185 250 140 Z"/>'
       '<path class="gc" d="M360 70 C320 90 300 115 300 140 C300 165 320 190 360 210 C330 180 318 160 318 140 C318 120 330 100 360 70 Z" opacity="0.7"/>'
       + ''.join(f'<path class="s" d="M{x} {y} H{x + 30}"/><path class="d" d="M{x + 30} {y} l-7 -4 l0 8 Z"/>' for x, y in ((20, 268), (70, 268), (120, 268), (220, 268), (270, 268), (320, 268)))
       + '<text class="tb" x="100" y="245" text-anchor="middle">wydma paraboliczna</text><text class="tb" x="300" y="245" text-anchor="middle">barchan</text>'
       '<text class="ts" x="200" y="290" text-anchor="middle">wiatr z zachodu na wschód — widok z góry</text>')
S['g-rzezba'].append(
 dict(typ='rysunek', tytul='Wydma paraboliczna i barchan', svg=_wd,
      znaczniki=[(50, 77, 60, 25, 'Ramiona', 'Paraboli: skierowane POD wiatr — utrwalone roślinnością'),
                 (152, 140, 175, 110, 'Czoło', 'Wędruje z wiatrem; stromy stok zawietrzny po stronie wschodniej'),
                 (350, 74, 300, 25, 'Rogi', 'Barchanu: skierowane Z WIATREM — na brzegach piasek przesypuje się szybciej'),
                 (345, 140, 330, 112, 'Zawietrzny', 'Stromy (ok. 30–34°), wklęsły stok barchanu'),
                 (100, 268, 150, 238, 'Wiatr', 'Stały kierunek wiatru — z zachodu'),
                 (265, 140, 225, 180, 'Dowietrzny', 'Łagodny stok, po którym piasek jest wwiewany')],
      opis='Kształt wydmy wskazuje kierunek wiatru (widok z góry).',
      uwaga='Paraboliczna (wybrzeża, np. Mierzeja Łebska): ramiona pod wiatr. Barchan (pustynie bez roślinności): ramiona z wiatrem.'))

# ---------- mierzeja i zalew ----------
_mz = ('<rect class="gw2" x="0" y="0" width="400" height="300"/>'
       '<path class="gt" d="M0 300 L0 215 C60 205 90 225 140 212 C200 196 260 220 320 205 C360 195 380 205 400 200 L400 300 Z"/>'
       '<path class="gw" d="M0 215 C60 205 90 225 140 212 C200 196 260 220 320 205 C360 195 380 205 400 200 L400 150 C300 145 120 145 0 155 Z"/>'
       '<path class="gp ol" d="M-5 140 C120 128 290 128 405 136 L405 150 C300 142 120 143 -5 156 Z"/>'
       + ''.join(f'<path class="gf2" d="M{x} {y} l-4 0 l4 -8 l4 8 Z"/>' for x in range(30, 390, 30) for y in ((147 if x % 60 else 145),))
       + '<path class="cold" d="M240 290 C235 260 238 240 230 210" style="stroke-width:3"/>'
       '<path class="cold" d="M231 212 C222 205 238 205 229 214" style="stroke-width:1.5"/>'
       '<path class="gp" d="M220 215 l10 -10 l10 10 Z" opacity="0.9"/>'
       '<path class="s2" d="M60 110 C120 100 200 100 260 110"/><path class="d" d="M260 110 l-8 -5 l1 9 Z"/>'
       '<text class="ts" x="160" y="95" text-anchor="middle">prąd przybrzeżny</text>'
       '<text class="tb" x="200" y="50" text-anchor="middle">Morze Bałtyckie</text>'
       '<path class="gw2" d="M392 140 h13 v12 h-13 Z"/>')
S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Mierzeja i zalew', svg=_mz,
      znaczniki=[(160, 138, 160, 70, 'Mierzeja', 'Wał piasku usypany przez prąd przybrzeżny; wydmy porośnięte lasem'),
                 (200, 175, 280, 180, 'Zalew', 'Płytki, wysłodzony przez rzeki; odcięty od morza'),
                 (398, 146, 370, 115, 'Cieśnina', 'Łączy zalew z morzem'),
                 (238, 260, 290, 265, 'Rzeka', 'Wnosi wodę słodką i osady'),
                 (229, 212, 175, 240, 'Delta', 'Rzeka odkłada osady w spokojnym zalewie')],
      opis='Wybrzeże mierzejowo-zalewowe (widok z góry) — np. Mierzeja Wiślana i Zalew Wiślany.',
      uwaga='Mierzeje i zalewy powstają w wyniku akumulacji morskiej (prądy przybrzeżne), a nie abrazji.'),
]

# ---------- piramidy wieku ----------
_mlode = [9.5, 8.6, 7.6, 6.6, 5.7, 4.8, 4.0, 3.3, 2.7, 2.1, 1.6, 1.2, 0.8, 0.5, 0.3, 0.2]
_stare = [2.0, 2.1, 2.2, 2.4, 2.6, 2.8, 3.0, 3.1, 3.3, 3.4, 3.6, 3.8, 3.5, 3.2, 2.6, 2.4]


def piramida(dane, cx, tytul):
    out = f'<path class="s" d="M{cx} 30 V258"/>'
    for i, v in enumerate(dane):
        y = 254 - i * 14
        w = v * 8.5
        out += f'<rect class="gw2" x="{cx - w:.1f}" y="{y - 12}" width="{w:.1f}" height="12"/><rect class="gm2" x="{cx}" y="{y - 12}" width="{w * 0.98 + (0 if i < 12 else (i - 11) * 2.5):.1f}" height="12"/>'
    out += f'<path class="s" d="M{cx - 85} 258 H{cx + 85}"/>'
    out += ''.join(f'<path class="s" d="M{cx + d * 8.5:.0f} 258 v4"/><text class="ts" x="{cx + d * 8.5:.0f}" y="270" text-anchor="middle">{abs(d)}</text>' for d in (-10, -5, 5, 10))
    out += f'<text class="tb" x="{cx}" y="20" text-anchor="middle">{tytul}</text>'
    return out


_pir = (piramida(_mlode, 100, 'kraj A') + piramida(_stare, 285, 'kraj B')
        + ''.join(f'<text class="ts" x="200" y="{254 - i * 14 - 2}" text-anchor="middle">{i * 5}{"+" if i == 15 else ""}</text>' for i in range(0, 16, 3))
        + '<text class="ts" x="180" y="296" text-anchor="middle">% ludności · niebieski — mężczyźni, pomarańczowy — kobiety</text>')
S['g-struktura'] = [
 dict(typ='rysunek', tytul='Piramidy wieku: młode i starzejące się społeczeństwo', svg=_pir,
      znaczniki=[(25, 248, 40, 60, 'Podstawa A', 'Szeroka: dużo dzieci — wysoki przyrost naturalny (np. Niger)'),
                 (104, 40, 150, 50, 'Wierzchołek', 'Wąski: krótkie przeciętne trwanie życia'),
                 (272, 248, 335, 282, 'Podstawa', 'Zwężona: mało urodzeń — niska dzietność'),
                 (255, 110, 225, 105, 'Środek', 'Szeroki: liczne roczniki dawnych wyżów demograficznych'),
                 (305, 44, 335, 22, 'Kobiety', 'Przewaga kobiet wśród najstarszych — dłuższe trwanie życia')],
      opis='Struktura wieku i płci w dwóch krajach (dane umowne, grupy pięcioletnie).',
      uwaga='Kraj A — piramida „progresywna” (np. Niger, Mali), kraj B — „regresywna”, w kształcie urny (np. Japonia, Włochy, coraz bardziej Polska).'),
]

# ---------- piętra roślinności w Tatrach ----------
_hy = lambda h: 285 - (h - 700) * 0.14
_gora = 'M10 285 L10 250 L60 220 L95 160 L130 95 L150 40 L165 28 L180 50 L205 110 L240 175 L270 230 L285 285 Z'
_pt = (f'<defs><clipPath id="g2tat"><path d="{_gora}"/></clipPath></defs>'
       '<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<g clip-path="url(#g2tat)">'
       f'<rect class="gf" x="0" y="{_hy(1250):.0f}" width="300" height="100"/>'
       f'<rect class="gf2" x="0" y="{_hy(1550):.0f}" width="300" height="{_hy(1250) - _hy(1550):.0f}"/>'
       f'<rect class="gt" x="0" y="{_hy(1800):.0f}" width="300" height="{_hy(1550) - _hy(1800):.0f}" style="opacity:0.85"/>'
       f'<rect class="gp" x="0" y="{_hy(2300):.0f}" width="300" height="{_hy(1800) - _hy(2300):.0f}" style="opacity:0.7"/>'
       f'<rect class="gs" x="0" y="0" width="300" height="{_hy(2300):.0f}"/></g>'
       f'<path class="s" d="{_gora}"/>'
       + ''.join(f'<circle class="gf2" cx="{x}" cy="{y}" r="5"/>' for x, y in ((40, 238), (55, 228), (250, 240), (262, 252)))
       + ''.join(f'<path class="gg" d="M{x} {y} l-5 0 l5 -12 l5 12 Z" opacity="0.6"/>' for x, y in ((92, 180), (215, 160), (228, 178)))
       + ''.join(f'<path class="dash" d="M10 {_hy(h):.0f} H290"/><text class="ts" x="12" y="{_hy(h) - 3:.0f}">{h} m</text>' for h in (1250, 1550, 1800, 2300))
       + f'<text class="tb" x="165" y="20" text-anchor="middle">Gerlach / Rysy ok. 2500 m</text>')
S['g-biomy'] = [
 dict(typ='rysunek', tytul='Piętra roślinności w Tatrach', svg=_pt,
      znaczniki=[(70, 255, 300, 268, 'Regiel dolny', 'Do ok. 1250 m — buk, jodła, świerk (dziś głównie świerczyny)'),
                 (225, 190, 300, 205, 'Regiel górny', 'Do ok. 1550 m — bór świerkowy'),
                 (110, 140, 300, 150, 'Kosodrzewina', 'Do ok. 1800 m — zarośla sosny górskiej (kosówki)'),
                 (190, 90, 300, 100, 'Hale', 'Do ok. 2300 m — murawy wysokogórskie'),
                 (160, 40, 300, 50, 'Turnie', 'Powyżej 2300 m — skały, porosty, mchy')],
      opis='Piętrowy układ roślinności w zależności od wysokości (granice orientacyjne, stok północny).',
      uwaga='Granice pięter leżą wyżej na stokach południowych (cieplejszych) i niżej na północnych. Temperatura spada o ok. 0,6°C na każde 100 m.'),
]
