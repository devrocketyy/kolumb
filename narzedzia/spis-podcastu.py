#!/usr/bin/env python3
"""Buduje js/nagrania.js — spis gotowych nagrań podcastu dla aplikacji — z plików podcast/mp3/*.json.
Numer odcinka → id tematu/działu bierze z planu (docs/10 biologia, docs/11 historia).
  python3 narzedzia/spis-podcastu.py"""
import glob, json, math, os, re
PLANY = {'biologia': 'docs/10-podcast-biologia-plan.md', 'historia': 'docs/11-podcast-historia-plan.md', 'chemia': 'docs/17-podcast-chemia-plan.md'}
ids = {}
for przedmiot, plan in PLANY.items():
    if os.path.exists(plan):
        for nr, ident in re.findall(r'^\*\*(\d+)\..*?`([\w-]+)`', open(plan, encoding='utf-8').read(), re.M):
            ids[(przedmiot, int(nr))] = ident
wpisy = {}
for pj in sorted(glob.glob('podcast/mp3/*.json')):
    d = json.load(open(pj, encoding='utf-8'))
    m = re.match(r'([a-z]+)-(\d+)-', d['odcinek'])
    if not m or (m.group(1), int(m.group(2))) not in ids:
        print('pomijam', d['odcinek']); continue
    przedmiot, ident = m.group(1), ids[(m.group(1), int(m.group(2)))]
    typ = 'p' if ident.startswith(('b-', 'h-', 's-', 'c-')) else 'd'
    wpis = {'plik': f"podcast/mp3/{d['odcinek']}.mp3", 'min': max(1, math.ceil(d['dlugosc'] / 60)), 'czasy': pj}
    if os.path.exists(f"podcast/pytania/{d['odcinek']}.json"):
        wpis['pytania'] = f"podcast/pytania/{d['odcinek']}.json"
    wpisy[f'{przedmiot}/{typ}/{ident}'] = wpis
open('js/nagrania.js', 'w', encoding='utf-8').write(
    '// Wygenerowane przez narzedzia/spis-podcastu.py — nie edytuj ręcznie.\nexport const NAGRANIA_AUTO = '
    + json.dumps(wpisy, ensure_ascii=False, indent=1) + ';\n')
print(len(wpisy), 'nagrań w js/nagrania.js')
