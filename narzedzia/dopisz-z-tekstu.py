"""Kolumb — dopisywanie fiszek i pytań z prostego formatu tekstowego.

Użycie:  python3 narzedzia/dopisz-z-tekstu.py <przedmiot> plik1.txt [plik2.txt ...]
Przykład: python3 narzedzia/dopisz-z-tekstu.py wos nowe-fiszki.txt

Skrypt DOPISUJE treści do przedmioty/<przedmiot>/<dział>.json — niczego nie usuwa.
Fiszki o identycznym przodzie są aktualizowane (zachowują id i postęp uczniów).
Format pliku tekstowego:

# id | Nazwa działu | opis
## id | Nazwa poddziału | opis
Q pytanie :: odpowiedź :: źródło                → 1 fiszka
T pojęcie :: definicja :: źródło                → 2 fiszki (pojęcie→definicja, definicja→pojęcie)
P osoba :: koncepcja/dzieło :: źródło           → 2 fiszki (osoba→koncepcja, koncepcja→osoba)
? pytanie :: *poprawna :: zła :: zła :: zła :: wyjaśnienie :: źródło   → pytanie ABCD
Istniejące fiszki zachowują swoje id (dopasowanie po treści przodu).
"""
import re, sys, json, os, hashlib, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = None  # ustawiane w main()
SRC = {
    'K': 'Konstytucja RP, art.', 'KC': 'Kodeks cywilny, art.', 'KK': 'Kodeks karny, art.',
    'KRO': 'Kodeks rodzinny i opiekuńczy, art.', 'KP': 'Kodeks pracy, art.', 'KW': 'Kodeks wykroczeń, art.',
    'KPA': 'Kodeks postępowania administracyjnego, art.', 'KPK': 'Kodeks postępowania karnego, art.',
    'KPC': 'Kodeks postępowania cywilnego, art.', 'PPSA': 'Prawo o postępowaniu przed sądami administracyjnymi, art.',
    'KWYB': 'Kodeks wyborczy, art.', 'TUE': 'Traktat o Unii Europejskiej, art.', 'TFUE': 'Traktat o funkcjonowaniu Unii Europejskiej, art.',
    'KNZ': 'Karta Narodów Zjednoczonych, art.', 'EKPC': 'Europejska Konwencja Praw Człowieka, art.',
    'TP': 'Traktat Północnoatlantycki, art.', 'KPP': 'Karta praw podstawowych UE, art.',
    'PDPC': 'Powszechna Deklaracja Praw Człowieka, art.', 'MPPOIP': 'Międzynarodowy Pakt Praw Obywatelskich i Politycznych, art.',
    'KPD': 'Konwencja o prawach dziecka, art.', 'USG': 'Ustawa o samorządzie gminnym, art.',
    'USP': 'Ustawa o samorządzie powiatowym, art.', 'USW': 'Ustawa o samorządzie województwa, art.',
    'UPP': 'Ustawa o partiach politycznych, art.', 'UST': 'Prawo o stowarzyszeniach, art.', 'UF': 'Ustawa o fundacjach, art.',
    'UDPP': 'Ustawa o działalności pożytku publicznego i o wolontariacie, art.', 'URL': 'Ustawa o referendum lokalnym, art.',
    'URO': 'Ustawa o referendum ogólnokrajowym, art.', 'UO': 'Ustawa o obywatelstwie polskim, art.',
    'UMN': 'Ustawa o mniejszościach narodowych i etnicznych oraz o języku regionalnym, art.',
    'PRAS': 'Prawo prasowe, art.', 'URPO': 'Ustawa o Rzeczniku Praw Obywatelskich, art.',
    'KUSA': 'Konstytucja USA,', 'GG': 'Ustawa Zasadnicza RFN, art.', 'K58': 'Konstytucja V Republiki Francuskiej, art.',
    'KSZ': 'Konstytucja Szwajcarii, art.', 'KRF': 'Konstytucja Federacji Rosyjskiej, art.', 'KIT': 'Konstytucja Republiki Włoskiej, art.',
}
PP = {
    'ZP I': 'Człowiek i społeczeństwo', 'ZP II': 'Społeczeństwo obywatelskie', 'ZP III': 'Organy władzy publicznej w RP',
    'ZP IV': 'Prawa człowieka i ich ochrona', 'ZP V': 'Prawo w RP', 'ZP VI': 'Wybrane problemy polityki publicznej w RP',
    'ZP VII': 'Współczesne stosunki międzynarodowe',
    'ZR I': 'Człowiek w społeczeństwie', 'ZR II': 'Różnorodność kulturowa', 'ZR III': 'Struktura społeczna i problemy społeczne',
    'ZR IV': 'Aspekty etniczne życia społecznego', 'ZR V': 'Państwo, myśl polityczna i demokratyzacja',
    'ZR VI': 'Społeczeństwo obywatelskie i kultura polityczna', 'ZR VII': 'Rywalizacja o władzę', 'ZR VIII': 'Modele sprawowania władzy',
    'ZR IX': 'Sprawowanie władzy w RP', 'ZR X': 'Kontrola władzy', 'ZR XI': 'System prawa w RP',
    'ZR XII': 'Prawa człowieka i ich ochrona międzynarodowa', 'ZR XIII': 'Ład międzynarodowy', 'ZR XIV': 'Integracja europejska',
    'ZR XV': 'Polska polityka zagraniczna',
}

def src(s):
    s = s.strip()
    if not s: return ''
    m = re.match(r'^PP (Z[PR] [IVX]+)\b(.*)$', s)
    if m:
        z = 'zakres rozszerzony' if m.group(1).startswith('ZR') else 'zakres podstawowy'
        return f'Podstawa programowa WOS, {z}, dz. {m.group(1)[3:]} „{PP[m.group(1)]}”{m.group(2)}'
    parts = []
    for piece in s.split(';'):
        piece = piece.strip()
        m = re.match(r'^([A-Z0-9]+) (.+)$', piece)
        parts.append(f'{SRC[m.group(1)]} {m.group(2)}' if m and m.group(1) in SRC else piece)
    return '; '.join(parts)

def parse(path):
    dz = None; cur = None; units = []
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        line = line.strip()
        if not line or line.startswith('//'): continue
        if line.startswith('## '):
            i, n, *o = [x.strip() for x in line[3:].split('|')]
            cur = {'id': i, 'nazwa': n, 'opis': o[0] if o else '', 'items': [], 'qs': []}; units.append(cur); continue
        if line.startswith('# '):
            i, n, *o = [x.strip() for x in line[2:].split('|')]
            dz = {'id': i, 'nazwa': n, 'opis': o[0] if o else ''}; continue
        kind, rest = line[0], line[1:].strip()
        f = [x.strip() for x in rest.split('::')]
        try:
            if kind == 'Q':
                cur['items'].append((f[0], f[1], src(f[2] if len(f) > 2 else '')))
            elif kind == 'T':
                cur['items'].append((f'Wyjaśnij pojęcie: {f[0]}', f[1], src(f[2] if len(f) > 2 else '')))
                cur['items'].append((f'Podaj nazwę pojęcia: {f[1]}', f[0], src(f[2] if len(f) > 2 else '')))
            elif kind == 'P':
                cur['items'].append((f'{f[0]} — z jaką koncepcją lub dziełem kojarzysz tę postać?', f[1], src(f[2] if len(f) > 2 else '')))
                cur['items'].append((f'Kto jest autorem lub przedstawicielem? — {f[1]}', f[0], src(f[2] if len(f) > 2 else '')))
            elif kind == '?':
                q, answers, expl, so = f[0], f[1:5], f[5] if len(f) > 5 else '', src(f[6] if len(f) > 6 else '')
                good = [a for a in answers if a.startswith('*')]
                assert len(answers) == 4 and len(good) == 1, 'ABCD: 4 odpowiedzi, jedna z *'
                good = good[0][1:].strip(); bad = [a for a in answers if not a.startswith('*')]
                pos = int(hashlib.md5(q.encode()).hexdigest(), 16) % 4
                opts = bad[:pos] + [good] + bad[pos:]
                cur['qs'].append({'pytanie': q, 'odpowiedzi': opts, 'poprawna': 'ABCD'[pos], 'wyjasnienie': expl, 'zrodlo': so})
            else:
                raise ValueError('nieznany typ linii')
        except Exception as e:
            sys.exit(f'{path}:{ln}: {e}: {line[:80]}')
    return dz, units

def merge(dz, units):
    path = f'{OUT}/{dz["id"]}.json'
    old = json.load(open(path)) if os.path.exists(path) else {'poddzialy': []}
    oldu = {u['id']: u for u in old.get('poddzialy', [])}
    out_units = []
    new_ids = {u['id'] for u in units}
    for u in units:
        o = oldu.get(u['id'], {'fiszki': [], 'pytania': []})
        by_front = {f['przod']: f for f in o['fiszki']}
        by_q = {q['pytanie']: q for q in o['pytania']}
        n = max([int(re.sub(r'\D', '', f['id']) or 0) for f in o['fiszki']] + [0])
        nq = max([int(re.sub(r'\D', '', q['id']) or 0) for q in o['pytania']] + [0])
        fiszki = [dict(f) for f in o['fiszki']]
        idx = {f['przod']: i for i, f in enumerate(fiszki)}
        for przod, tyl, so in u['items']:
            if przod in idx:
                fiszki[idx[przod]].update({'tyl': tyl, 'zrodlo': so})
            else:
                n += 1
                idx[przod] = len(fiszki)
                fiszki.append({'id': f'f{n:03d}', 'przod': przod, 'tyl': tyl, 'zrodlo': so})
        pytania = [dict(q) for q in o['pytania']]
        qidx = {q['pytanie']: i for i, q in enumerate(pytania)}
        for q in u['qs']:
            if q['pytanie'] in qidx:
                pytania[qidx[q['pytanie']]].update(q)
            else:
                nq += 1
                qidx[q['pytanie']] = len(pytania)
                pytania.append({'id': f'p{nq:02d}', **q})
        out_units.append({'id': u['id'], 'nazwa': u['nazwa'], 'opis': u['opis'], 'fiszki': fiszki, 'pytania': pytania})
    merged = {u['id']: u for u in out_units}
    order = [u['id'] for u in old.get('poddzialy', [])] + [u['id'] for u in out_units if u['id'] not in oldu]
    out_units = [merged.get(i) or oldu[i] for i in order]  # kolejność zachowana, nowe poddziały na końcu
    data = {'id': dz['id'], 'nazwa': dz['nazwa'] or old.get('nazwa', ''), 'opis': dz['opis'] or old.get('opis', ''), 'poddzialy': out_units}
    os.makedirs(OUT, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    nf = sum(len(u['fiszki']) for u in out_units); nq = sum(len(u['pytania']) for u in out_units)
    print(f'{dz["id"]}: {len(out_units)} poddziałów, {nf} fiszek, {nq} pytań ABCD')
    for u in out_units:
        print(f'   {u["id"]:32} {len(u["fiszki"]):4} f  {len(u["pytania"]):3} p')
    return nf, nq

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    OUT = os.path.join(ROOT, 'przedmioty', sys.argv[1])
    tf = tq = 0
    for p in sys.argv[2:]:
        a, b = merge(*parse(p)); tf += a; tq += b
    print(f'RAZEM w zmienionych działach: {tf} fiszek, {tq} pytań')
    print('Teraz uruchom: node narzedzia/zbuduj-indeks.mjs')
