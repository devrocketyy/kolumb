#!/usr/bin/env python3
"""IndexLab — wpisuje autorskie omówienia zadań do arkuszy CKE z WOS.

Omówienia leżą w narzedzia/wos/omowienia/<id-arkusza>.py jako słownik OM = {nr zadania: tekst}.
Użycie: python3 narzedzia/wos/wpisz-omowienia.py   (wszystkie arkusze, dla których jest plik)
Na końcu wypisuje, ilu zadaniom wciąż brakuje omówienia.
"""
import json, os, runpy, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ARK = os.path.join(ROOT, 'przedmioty', 'wos', 'arkusze')
OMD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'omowienia')

razem = brak = 0
for path in sorted(glob.glob(os.path.join(ARK, '*.json'))):
    aid = os.path.basename(path)[:-5]
    a = json.load(open(path, encoding='utf-8'))
    src = os.path.join(OMD, aid.replace('-', '_') + '.py')
    om = runpy.run_path(src)['OM'] if os.path.exists(src) else {}
    nry = {z['nr'] for w in a['wiazki'] for z in w['zadania']}
    nadmiar = set(om) - nry
    assert not nadmiar, f'{aid}: omówienia dla nieistniejących zadań {sorted(nadmiar)}'
    for w in a['wiazki']:
        for z in w['zadania']:
            razem += 1
            if z['nr'] in om:
                z['omowienie'] = om[z['nr']].strip()
            if not z.get('omowienie'):
                brak += 1
                print(f'  brak: {aid} {z["nr"]}')
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(a, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
print(f'Omówienia: {razem - brak}/{razem} zadań.')
