# Kontrola: czy poprawna odpowiedź nie jest regularnie najdłuższa (per temat i łącznie).
import json, glob
t = l = 0
for p in sorted(glob.glob('przedmioty/historia/*.json')):
    d = json.load(open(p))
    for u in d.get('poddzialy', []):
        for q in u['pytania']:
            L = [len(x) for x in q['odpowiedzi']]; c = 'ABCD'.index(q['poprawna']); t += 1
            if L[c] == max(L) and L.count(max(L)) == 1:
                l += 1
                if L[c] >= 1.4 * sorted(L)[-2]: print('  zdradza:', u['id'], q['id'], q['pytanie'][:60])
print(f'historia: poprawna najdłuższa w {l}/{t} = {round(100*l/max(t,1))}%')
