# Składa narzedzia/ocena-ai/zbior.jsonl z plików zbior_<przedmiot>.py. Uruchom: python3 narzedzia/ocena-ai/zbuduj-zbior.py
import json, glob, importlib.util, os
kat = os.path.dirname(os.path.abspath(__file__))
wiersze = []
for f in sorted(glob.glob(os.path.join(kat, 'zbior_*.py'))):
    spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for ref, typ, czesc, odp in m.Z:
        for i, (rodzaj, tekst, pkt, brak, przeglad) in enumerate(odp, 1):
            wiersze.append({'id': f'{m.P}/{ref}#{i}', 'przedmiot': m.P, 'ref': f'{m.P}/{ref}', 'typ': typ, 'czesc': czesc,
                            'rodzaj': rodzaj, 'odpowiedz': tekst, 'wzor_pkt': pkt, 'wzor_brakuje': brak, 'przeglad': przeglad})
with open(os.path.join(kat, 'zbior.jsonl'), 'w') as o:
    for w in wiersze: o.write(json.dumps(w, ensure_ascii=False) + '\n')
from collections import Counter
print(len(wiersze), 'pozycji', dict(Counter(w['przedmiot'] for w in wiersze)), dict(Counter(w['czesc'] for w in wiersze)), 'do przeglądu:', sum(w['przeglad'] for w in wiersze))
