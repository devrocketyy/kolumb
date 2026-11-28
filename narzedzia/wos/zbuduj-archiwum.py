#!/usr/bin/env python3
"""IndexLab — buduje archiwum arkuszy CKE z WOS w starszej formule (2015).

Źródło: narzedzia/wos/arkusze_archiwum.py (lista ARKUSZE, tryb „link + omówienie”).
Wynik: przedmioty/wos/arkusze/<id>.json oraz wpisy w przedmioty/wos.json (na końcu listy arkuszy).
Arkusze dostają archiwum=True — są do ćwiczeń, ale poza planem, prognozą i próbną maturą.
Użycie: python3 narzedzia/wos/zbuduj-archiwum.py
"""
import json, os, runpy

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arkusze_archiwum.py')
OUT = os.path.join(ROOT, 'przedmioty', 'wos', 'arkusze')
SUBJ = os.path.join(ROOT, 'przedmioty', 'wos.json')

arch = runpy.run_path(SRC)['ARKUSZE']
for a in arch:
    a['archiwum'] = True
    with open(os.path.join(OUT, a['id'] + '.json'), 'w', encoding='utf-8') as o:
        json.dump(a, o, ensure_ascii=False, indent=1)
        o.write('\n')
s = json.load(open(SUBJ, encoding='utf-8'))
ids = {a['id'] for a in arch}
s['arkusze'] = [x for x in s['arkusze'] if not x['id'].endswith('-f2015')] + \
               [{'id': a['id'], 'plik': f'wos/arkusze/{a["id"]}.json'} for a in arch]
with open(SUBJ, 'w', encoding='utf-8') as o:
    json.dump(s, o, ensure_ascii=False, indent=2)
    o.write('\n')
for a in arch:
    z = [z for w in a['wiazki'] for z in w['zadania']]
    print(f'{a["id"]}: {len(z)} zadań, {sum(x["punkty"] for x in z)} pkt')
