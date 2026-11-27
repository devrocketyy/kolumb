#!/usr/bin/env python3
"""Wybiera zróżnicowane zadania otwarte z przedmioty/*/ do zbioru testowego oceny AI.
Zapis: narzedzia/ocena-ai/zadania.json (szkielet — odpowiedzi uczniów dopisuje się w zbior.jsonl).
Użycie: python3 narzedzia/ocena-ai/wybierz.py [na_przedmiot=40] [ziarno=7]"""
import json, glob, random, re, sys, os
N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
ZAMKNIETE = re.compile(r'(^|\s)[A-F]\.\s.+[;.]\s*[B-F]\.\s|Zaznacz|Podkreśl|Wybierz|Zakreśl|Oceń prawdziwość|Wpisz.*[PF]\b|\bP/F\b|Uzupełnij.*wybier', re.I)
TYPY = [('oblicz', r'\boblicz|\bwyznacz masę|\bpodaj wartość'), ('wyjasnij', r'wyjaśnij|uzasadnij|dlaczego|przedstaw przyczyn|określ.*wpływ'),
        ('porownaj', r'porównaj|wskaż.*różnic|podaj.*różnic'), ('wymien', r'wymień|podaj dwa|podaj trzy|podaj.*przykład'),
        ('material', r'na podstawie|z (tekstu|mapy|ilustracji|wykresu|źródła|schematu|tabeli)|materiał')]
def typ(p):
    for t, r in TYPY:
        if re.search(r, p, re.I): return t
    return 'podaj'
def zbierz(przedmiot):
    out = []
    for f in glob.glob(f'{ROOT}/przedmioty/{przedmiot}/**/*.json', recursive=True):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        def walk(o, ctx):
            if isinstance(o, dict):
                if 'polecenie' in o and 'odpowiedz' in o and o.get('punkty'):
                    out.append(dict(przedmiot=przedmiot, zrodlo=os.path.relpath(f, ROOT), nr=o.get('nr'), punkty=o['punkty'],
                        polecenie=o['polecenie'][:3000], material=(o.get('material') or ctx.get('material') or '')[:4000],
                        klucz=o['odpowiedz'][:3000], zasady=(o.get('zasady') or '')[:2000]))
                    return
                c = dict(ctx)
                if isinstance(o.get('material'), str): c['material'] = o['material']
                for v in o.values(): walk(v, c)
            elif isinstance(o, list):
                for v in o: walk(v, ctx)
        walk(d, {})
    # pomiń zadania zależne od rysunku/źródła, którego nie ma w danych
    ZALEZNE = re.compile(r'(ze|na) (schemacie|rysunku|mapie|wykresie|fotografii|ilustracji|planie)|litery? ze|źródł[aoue]m? \d|z (mapy|schematu|wykresu)', re.I)
    return [z for z in out if not ZAMKNIETE.search(z['polecenie']) and len(z['klucz']) > 25 and not (ZALEZNE.search(z['polecenie']) and len(z['material']) < 80)]
wynik = []
for p in ['biologia', 'chemia', 'geografia', 'historia', 'wos']:
    pula = zbierz(p)
    for z in pula: z['typ'] = typ(z['polecenie'])
    random.shuffle(pula)
    wybor, licz = [], {}
    # kwoty: ok. 55% za 1 pkt, 35% za 2 pkt, reszta 3+; max 1/3 jednego typu
    kw = {1: round(N * .5), 2: round(N * .35)}
    for z in pula:
        k = 1 if z['punkty'] == 1 else 2 if z['punkty'] == 2 else 3
        if k == 3: continue
        if licz.get(('p', k), 0) >= kw.get(k, 0) or licz.get(('t', z['typ']), 0) >= N // 3: continue
        licz[('p', k)] = licz.get(('p', k), 0) + 1; licz[('t', z['typ'])] = licz.get(('t', z['typ']), 0) + 1; wybor.append(z)
    for z in pula:
        if len(wybor) >= N: break
        if z['punkty'] >= 3 and sum(1 for w in wybor if w['punkty'] >= 3) < N - kw[1] - kw[2] and z not in wybor: wybor.append(z)
    for i, z in enumerate(wybor): z['id'] = f"{p[:3]}-{i+1:02d}"; z['czesc'] = 'robocza' if i % 4 else 'kontrolna'
    print(p, len(pula), '->', len(wybor), {t: sum(1 for w in wybor if w['typ'] == t) for t in set(w['typ'] for w in wybor)})
    wynik += wybor
json.dump(wynik, open(os.path.join(os.path.dirname(__file__), 'zadania.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('razem', len(wynik))
