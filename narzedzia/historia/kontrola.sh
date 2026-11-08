#!/bin/sh
# Pełna kontrola treści historii: budowa, długość odpowiedzi, duplikaty, statystyki.
set -e
python3 narzedzia/zbuduj-historie.py
python3 narzedzia/historia/sprawdz.py
python3 - <<'P'
import json,glob,collections
c=collections.defaultdict(list); r=[]; q=0
for p in glob.glob('przedmioty/historia/*.json'):
    for u in json.load(open(p)).get('poddzialy',[]):
        r.append(len(u['fiszki'])); q+=len(u['pytania'])
        for f in u['fiszki']: c[f['przod'].lower()].append(u['id'])
d={k:v for k,v in c.items() if len(set(v))>1}
print('fiszek do nauki:',sum(r),'| pytań:',q,'| na temat min',min(r),'śr',round(sum(r)/len(r)),'| duplikaty między tematami:',len(d))
for k,v in list(d.items())[:10]: print('  dup:',k[:70],v)
P
