#!/usr/bin/env python3
"""Sprawdza scenariusze podcastu w formacie 2.0: zgodność znaczników [pytanie: id] z plikiem pytań,
kolejność, liczbę słów i parę [odpowiedź]/[koniec odpowiedzi].  python3 narzedzia/sprawdz-podcast.py biologia"""
import glob, json, os, re, sys
prefiks = sys.argv[1] if len(sys.argv) > 1 else ''
for md in sorted(glob.glob(f'podcast/scenariusze/{prefiks}*.md')):
    nazwa = os.path.basename(md)[:-3]
    pj = f'podcast/pytania/{nazwa}.json'
    if not os.path.exists(pj):
        continue
    t = open(md, encoding='utf-8').read()
    body = t.split('\n---\n', 1)[1]
    ids = re.findall(r'\[pytanie: ([\w-]+)\]', body)
    q = [x['id'] for x in json.load(open(pj, encoding='utf-8'))['pytania']]
    slowa = len([w for line in body.splitlines() if line and not line.startswith(('[', '#')) for w in line.split()])
    bledy = []
    if ids != q: bledy.append(f'znaczniki {ids} ≠ pytania {q}')
    if body.count('[odpowiedź]') != body.count('[koniec odpowiedzi]'): bledy.append('niesparowane [odpowiedź]')
    print(f"{'OK ' if not bledy else 'BŁĄD'} {nazwa}: {slowa} słów (~{slowa / 105 + len(ids) * 0.12:.1f} min), pytań {len(q)}", *bledy)
