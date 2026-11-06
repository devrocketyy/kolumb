#!/usr/bin/env python3
"""IndexLab — bank zadań autorskich z prostego formatu tekstowego do JSON.

Użycie:  python3 narzedzia/zbuduj-bank.py <przedmiot> plik1.txt [plik2.txt ...]
Wynik:   przedmioty/<przedmiot>/bank/<dział>.json (wiązki o tym samym id są nadpisywane, inne zostają).

Format:
@W id | dział | tytuł wiązki
@M                      ← materiał źródłowy (kolejne linie, opcjonalnie)
@R źródło materiału     ← np. „Na podstawie: Konstytucja RP, art. 144” (opcjonalnie)
@Z typ | punkty         ← typ: pf, abcd, przyporzadkuj, rozstrzygnij, argument, podaj, wyjasnij, porownaj, pismo, wypracowanie
@P                      ← polecenie (kolejne linie)
@O                      ← odpowiedź / klucz (kolejne linie)
@S                      ← zasady oceniania (opcjonalnie; domyślne zależą od typu)
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

DOMYSLNE = {
    'pf': '1 pkt – poprawna ocena wszystkich stwierdzeń.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'abcd': '1 pkt – wskazanie poprawnej odpowiedzi.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'przyporzadkuj': '1 pkt – poprawne przyporządkowanie wszystkich elementów.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'podaj': '1 pkt – podanie poprawnej odpowiedzi.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'rozstrzygnij': '1 pkt – poprawne rozstrzygnięcie i poprawne uzasadnienie.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'argument': '1 pkt – sformułowanie poprawnego argumentu i poprawnego kontrargumentu.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'wyjasnij': '1 pkt – poprawne wyjaśnienie z odwołaniem do materiału lub wiedzy.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
    'porownaj': '1 pkt – poprawne wskazanie podobieństwa lub różnicy.\n0 pkt – inna odpowiedź lub brak odpowiedzi.',
}

def zasady_dla(typ, pkt):
    if typ in DOMYSLNE and pkt == 1:
        return DOMYSLNE[typ]
    if pkt == 2:
        return '2 pkt – poprawna i pełna odpowiedź na obie części polecenia.\n1 pkt – poprawna odpowiedź na jedną część polecenia.\n0 pkt – inna odpowiedź lub brak odpowiedzi.'
    if pkt == 3:
        return '3 pkt – trzy poprawne elementy odpowiedzi.\n2 pkt – dwa poprawne elementy.\n1 pkt – jeden poprawny element.\n0 pkt – inna odpowiedź lub brak odpowiedzi.'
    return ''

def parse(path):
    wiazki, w, z, field = [], None, None, None
    for ln, raw in enumerate(open(path, encoding='utf-8'), 1):
        line = raw.rstrip('\n')
        if line.startswith('//'):
            continue
        m = re.match(r'^@(\w)\s*(.*)$', line)
        if m:
            tag, rest = m.group(1), m.group(2).strip()
            if tag == 'W':
                i, d, t = [x.strip() for x in rest.split('|', 2)]
                w = {'id': i, 'dzial': d, 'tytul': t, 'material': '', 'zrodlo': 'Zadanie autorskie IndexLab', 'zadania': []}
                wiazki.append(w); z = None; field = None
            elif tag == 'M':
                field = ('w', 'material')
            elif tag == 'R':
                w['zrodlo'] = 'Zadanie autorskie IndexLab. ' + rest
                field = None
            elif tag == 'Z':
                typ, pkt = [x.strip() for x in rest.split('|')]
                z = {'nr': str(len(w['zadania']) + 1), 'typ': typ, 'punkty': int(pkt), 'polecenie': '', 'odpowiedz': '', 'zasady': ''}
                w['zadania'].append(z); field = None
            elif tag in 'POS':
                field = ('z', {'P': 'polecenie', 'O': 'odpowiedz', 'S': 'zasady'}[tag])
            else:
                sys.exit(f'{path}:{ln}: nieznany znacznik @{tag}')
            continue
        if field is None:
            if line.strip():
                sys.exit(f'{path}:{ln}: tekst poza polem: {line[:60]}')
            continue
        obj = w if field[0] == 'w' else z
        obj[field[1]] = (obj[field[1]] + '\n' + line) if obj[field[1]] else line
    for w in wiazki:
        w['material'] = w['material'].strip()
        assert w['zadania'], f'wiązka {w["id"]} nie ma zadań'
        for z in w['zadania']:
            for k in ('polecenie', 'odpowiedz', 'zasady'):
                z[k] = z[k].strip()
            assert z['polecenie'] and z['odpowiedz'], f'{w["id"]}/{z["nr"]}: brak polecenia lub odpowiedzi'
            if not z['zasady']:
                z['zasady'] = zasady_dla(z['typ'], z['punkty'])
    return wiazki

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sid = sys.argv[1]
    out = os.path.join(ROOT, 'przedmioty', sid, 'bank')
    os.makedirs(out, exist_ok=True)
    nowe = [w for p in sys.argv[2:] for w in parse(p)]
    for d in sorted({w['dzial'] for w in nowe}):
        path = os.path.join(out, f'{d}.json')
        old = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {'dzial': d, 'wiazki': []}
        idx = {w['id']: i for i, w in enumerate(old['wiazki'])}
        for w in (x for x in nowe if x['dzial'] == d):
            if w['id'] in idx: old['wiazki'][idx[w['id']]] = w
            else: idx[w['id']] = len(old['wiazki']); old['wiazki'].append(w)
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(old, fh, ensure_ascii=False, indent=1); fh.write('\n')
        n = sum(len(w['zadania']) for w in old['wiazki']); p = sum(z['punkty'] for w in old['wiazki'] for z in w['zadania'])
        print(f'{d}: {len(old["wiazki"])} wiązek, {n} zadań, {p} pkt')
    # dopisz banki do pliku przedmiotu
    sp = os.path.join(ROOT, 'przedmioty', f'{sid}.json')
    subj = json.load(open(sp, encoding='utf-8'))
    have = {b['plik'] for b in subj.get('bank', [])}
    for f in sorted(os.listdir(out)):
        if f.endswith('.json') and f'{sid}/bank/{f}' not in have:
            subj.setdefault('bank', []).append({'plik': f'{sid}/bank/{f}'})
    with open(sp, 'w', encoding='utf-8') as fh:
        json.dump(subj, fh, ensure_ascii=False, indent=2); fh.write('\n')
