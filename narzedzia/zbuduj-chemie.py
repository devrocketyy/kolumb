#!/usr/bin/env python3
"""IndexLab — buduje kurs chemii (przedmioty/chemia.json + przedmioty/chemia/*.json).

Struktura: wymagania z chemii (podstawa 2024, matura 2027), plan w docs/13-chemia-plan.md.
Treści autorskie: narzedzia/chemia/tresci*.py (fiszki, pytania), bank*.py (zadania), arkusze.py (omówienia arkuszy CKE).
Działy bez treści nie trafiają do aplikacji.

Użycie: python3 narzedzia/zbuduj-chemie.py && node narzedzia/zbuduj-indeks.mjs
"""
import random
import json, os, glob, runpy, hashlib, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'przedmioty', 'chemia')
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chemia')

# (id działu, nazwa, opis, [(id poddziału, wymaganie, nazwa)]) — plan: docs/13-chemia-plan.md
DZIALY = [
 ('umiejetnosci', 'Umiejętności egzaminacyjne', 'Czytanie poleceń, model obliczeń, jednostki i zaokrąglenia, doświadczenia: obserwacje i wnioski.', [
  ('c-polecenia', 'og. I–II', 'Czytanie poleceń, czasowniki operacyjne i warunki zadania'),
  ('c-obliczenia', 'og. II', 'Model obliczeń, jednostki, zaokrąglenia i sens wyniku'),
  ('c-doswiadczenia', 'og. III', 'Doświadczenia: projekt, obserwacje, wnioski i identyfikacja substancji')]),
 ('atom', 'Budowa atomu i układ okresowy', 'Budowa atomu, izotopy, konfiguracja elektronowa, okresowość, promieniotwórczość.', [
  ('c-atom', 'I.1–2, II.1–2', 'Budowa atomu, izotopy i masa atomowa'),
  ('c-konfiguracja', 'II.3–5', 'Konfiguracja elektronowa, liczby kwantowe i orbitale'),
  ('c-okresowosc', 'II.6–8', 'Układ okresowy i prawo okresowości'),
  ('c-promieniotworczosc', 'II.9–10', 'Przemiany promieniotwórcze i okres półtrwania')]),
 ('wiazania', 'Wiązania i oddziaływania', 'Rodzaje wiązań, hybrydyzacja i kształt cząsteczek, oddziaływania międzycząsteczkowe.', [
  ('c-wiazania', 'III.1–4', 'Wiązania jonowe, kowalencyjne, koordynacyjne i metaliczne'),
  ('c-geometria', 'III.5–6', 'Hybrydyzacja, kształt i polarność cząsteczek'),
  ('c-oddzialywania', 'III.7–8', 'Oddziaływania międzycząsteczkowe a właściwości substancji')]),
 ('stechiometria', 'Mol i stechiometria', 'Mol, masa i objętość molowa, wzory, obliczenia z równań: nadmiar, wydajność, mieszaniny.', [
  ('c-mol', 'I.3–5', 'Mol, masa molowa, objętość molowa gazów'),
  ('c-wzory', 'I.6', 'Wzory empiryczne i rzeczywiste, skład procentowy'),
  ('c-stechiometria', 'I.7–8', 'Obliczenia z równań: nadmiar, wydajność, mieszaniny')]),
 ('kinetyka', 'Energetyka, kinetyka i równowaga', 'Efekty energetyczne, prawo Hessa, szybkość reakcji, stan równowagi i reguła przekory.', [
  ('c-energetyka', 'IV.1–4', 'Efekty energetyczne, entalpia i prawo Hessa'),
  ('c-szybkosc', 'IV.5–7', 'Szybkość reakcji i katalizatory'),
  ('c-rownowaga', 'IV.8–11', 'Stan równowagi, stała równowagi i reguła przekory')]),
 ('roztwory', 'Roztwory', 'Stężenia procentowe i molowe, rozpuszczalność, rozcieńczanie i mieszanie roztworów.', [
  ('c-stezenia', 'V.1–4', 'Stężenie procentowe i molowe'),
  ('c-rozpuszczalnosc', 'V.5–6', 'Rozpuszczalność i roztwory nasycone'),
  ('c-mieszanie', 'V.7–8', 'Rozcieńczanie, zatężanie i mieszanie roztworów')]),
 ('roztwory-wodne', 'Reakcje w roztworach wodnych', 'Kwasy i zasady Brønsteda, pH, dysocjacja, hydroliza, bufory, reakcje jonowe.', [
  ('c-kwasy-zasady', 'VI.1–3', 'Teoria Brønsteda i dysocjacja elektrolityczna'),
  ('c-ph', 'VI.4–7', 'pH, stała i stopień dysocjacji'),
  ('c-hydroliza', 'VI.8–9', 'Hydroliza soli i roztwory buforowe'),
  ('c-jonowe', 'VI.10–12', 'Reakcje strąceniowe i zobojętniania, równania jonowe')]),
 ('nieorganiczne', 'Związki nieorganiczne, metale i niemetale', 'Tlenki, wodorotlenki, kwasy, sole, metale i niemetale, zastosowania.', [
  ('c-tlenki', 'VII.1–3', 'Tlenki i wodorki, charakter chemiczny, amfoteryczność'),
  ('c-wodorotlenki-kwasy', 'VII.4–6', 'Wodorotlenki i kwasy'),
  ('c-sole', 'VII.7–9', 'Sole i ich otrzymywanie'),
  ('c-metale', 'X.1–8', 'Metale i ich związki'),
  ('c-niemetale', 'X.9–16, XI', 'Niemetale, ich związki i zastosowania')]),
 ('redoks', 'Redoks i elektrochemia', 'Stopnie utlenienia, bilansowanie redoks, ogniwa, elektroliza i korozja.', [
  ('c-stopnie', 'VIII.1–3', 'Stopnie utlenienia, utleniacz i reduktor'),
  ('c-bilans', 'VIII.4–5', 'Bilansowanie równań redoks'),
  ('c-ogniwa', 'IX.1–5', 'Ogniwa, szereg napięciowy i SEM'),
  ('c-elektroliza', 'IX.6–9', 'Elektroliza i korozja')]),
 ('organiczna', 'Wstęp do chemii organicznej i węglowodory', 'Izomeria, alkany, alkeny, alkiny, areny i mechanizmy reakcji.', [
  ('c-izomeria', 'XII', 'Izomeria i nazewnictwo'),
  ('c-alkany', 'XIII.1–4', 'Alkany i cykloalkany'),
  ('c-alkeny', 'XIII.5–9', 'Alkeny i alkiny'),
  ('c-areny', 'XIII.10–12', 'Węglowodory aromatyczne')]),
 ('tlenowe', 'Tlenowe pochodne węglowodorów', 'Alkohole i fenole, aldehydy i ketony, kwasy karboksylowe, estry i tłuszcze.', [
  ('c-alkohole', 'XIV', 'Alkohole i fenole'),
  ('c-karbonylowe', 'XV', 'Aldehydy i ketony'),
  ('c-karboksylowe', 'XVI', 'Kwasy karboksylowe'),
  ('c-estry', 'XVII', 'Estry i tłuszcze')]),
 ('azotowe-cukry', 'Związki azotu, białka i cukry', 'Aminy i amidy, aminokwasy, peptydy i białka, cukry.', [
  ('c-aminy', 'XVIII', 'Aminy i amidy'),
  ('c-aminokwasy', 'XIX', 'Aminokwasy, peptydy i białka'),
  ('c-cukry', 'XX', 'Cukry')]),
 ('chemia-zycia', 'Chemia wokół nas i środowisko', 'Chemia w życiu codziennym, tworzywa, paliwa, ochrona środowiska.', [
  ('c-chemia-zycia', 'XXI', 'Chemia w życiu codziennym'),
  ('c-srodowisko', 'XXII', 'Elementy ochrony środowiska')]),
]

PP = 'Wymagania egzaminacyjne 2027, chemia (zakres rozszerzony)'
CKE = 'https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne'


def load_tresci():
    T = {}
    for f in sorted(glob.glob(os.path.join(SRC, 'tresci*.py'))):
        for k, v in runpy.run_path(f)['T'].items():
            if k in T:  # kolejne porcje dopisują fiszki i pytania do istniejących tematów
                T[k]['F'] = T[k].get('F', []) + v.get('F', [])
                T[k]['Q'] = T[k].get('Q', []) + v.get('Q', [])
            else:
                T[k] = dict(v)
    return T


_usun = os.path.join(SRC, 'usuniete.py')
_u = runpy.run_path(_usun) if os.path.exists(_usun) else {}
USUN, USUN_Q = _u.get('USUN', set()), _u.get('USUN_Q', set())
USUN_W, TYTULY_W = _u.get('USUN_W', set()), _u.get('TYTULY_W', {})
_w = os.path.join(SRC, 'wyrownania.py')
ODP = runpy.run_path(_w)['ODP'] if os.path.exists(_w) else {}  # wyrównane długości odpowiedzi ABCD
UZYTE_ODP = set()


def load_schematy():
    """schematy*.py: S['uid'] = [dict(typ='rysunek'|'proces'|'cykl', tytul, opis, ...)]"""
    S, tytuly = {}, set()
    for f in sorted(glob.glob(os.path.join(SRC, 'schematy*.py'))):
        for k, lst in runpy.run_path(f)['S'].items():
            for x in lst:
                assert x['typ'] in ('rysunek', 'proces', 'cykl'), (k, x['tytul'])
                assert x['tytul'] not in tytuly, ('powtórzony schemat', x['tytul'])
                tytuly.add(x['tytul'])
                y = {'id': _id('s', x['tytul']), 'typ': x['typ'], 'tytul': x['tytul'], 'opis': x.get('opis', '')}
                if x.get('uwaga'):
                    y['uwaga'] = x['uwaga']
                if x['typ'] == 'rysunek':
                    vb = [float(v) for v in x.get('viewBox', '0 0 400 300').split()]
                    zn = []
                    for m in x['znaczniki']:
                        px, py, lx, ly, n = m[:5]
                        for xx, yy in ((px, py), (lx, ly)):
                            assert vb[0] <= xx <= vb[0] + vb[2] and vb[1] <= yy <= vb[1] + vb[3], ('znacznik poza rysunkiem', x['tytul'], n)
                        zn.append({'x': px, 'y': py, 'lx': lx, 'ly': ly, 'n': n, 'd': m[5] if len(m) > 5 else ''})
                    assert 3 <= len(zn) <= 12, ('rysunek: 3–12 znaczników', x['tytul'])
                    assert len({z['n'] for z in zn}) == len(zn), ('powtórzona nazwa znacznika', x['tytul'])
                    y.update(svg=' '.join(x['svg'].split()), viewBox=x.get('viewBox', '0 0 400 300'), znaczniki=zn)
                else:
                    kroki = [{'t': a, 'd': b} if b else {'t': a} for a, b in ((k2 if isinstance(k2, tuple) else (k2, '')) for k2 in x['kroki'])]
                    assert 3 <= len(kroki) <= 12, ('proces: 3–12 etapów', x['tytul'])
                    assert len({z['t'] for z in kroki}) == len(kroki), ('powtórzony etap', x['tytul'])
                    y['kroki'] = kroki
                S.setdefault(k, []).append(y)
    return S


def _id(prefix, text):
    # stały identyfikator z treści — dopisywanie nowych fiszek nie zmienia postępów w istniejących
    return prefix + hashlib.sha1(text.strip().lower().encode()).hexdigest()[:8]


def _stem_leak(term, text):
    # czy odpowiedź (opis) zdradza nazwę — wtedy nie robimy fiszki odwrotnej
    low = text.lower()
    words = [w for w in re.findall(r'[\wąćęłńóśźż]+', term.lower()) if len(w) >= 4]
    return any(w[:5] in low for w in words)


# fiszki o ogólnych tematach („Skutki…”, „Przyczyny…”) nie nadają się do odwrócenia
OGOLNE = set('''Wyjaśnij Podaj Porównaj Oceń Synchronizacja Jak Konflikty Przykłady Skutki Przyczyny Cechy Reformy Etapy
Najważniejsze Walka Wynalazki Zmiany Sytuacja Postawy Ocena Rola Polityka Organizacja Struktura Kultura Twórcy Osiągnięcia
Wkład Początki Geneza Przebieg Znaczenie Bilans Ofiary Opór Zasięg Problem Formy Uniwersytety Zabytki Pisarze Ludzie Nurty
Kryzys Ewolucja Przemiany Rozwój Wpływ Upadek Powstanie Najczęstszy Typowe Wojny Ruchy Procesy Projekty Problemy Migracje
Emancypacja Represje Udział Okoliczności Uwarunkowania Ustrój Organy Plusy Minusy Działalność Dorobek Literatura Sztuka Nauka
Oświata Sport Film Kolektywizacja Podział Granica Granice Społeczeństwo Twórcy Zakony Formy Polacy Pierwsze Inni Wizja Prezydenci
Ostatni Pięć Święta Trzy Dwie Siedem Wewnętrzne Zewnętrzne Charakter Kształtowanie'''.split())


# tytuły zestawień, porównań i instrukcji („X — przykłady”, „A a B”, „Krok po kroku…”) nie są pojęciami —
# zgadywanie ich z opisu nic nie uczy, więc z takich fiszek nie robimy odwrotek
SLABA_ODWROTKA = re.compile(r' — | – | a | jako |\bkrok|zestawienie|porównanie|przykład|wzór|schemat|typowy błąd|\d|^(funkcj|budow|polecenie|czynnik|sposob|właściwości|główne|szybkość|rodzaj|hormony|zasady|objawy|znaczenie|rola|wpływ|metody|przystosowania)', re.I)


def reverse_cards(F):
    """Fiszki odwrotne (jak w WOS): pojęcie ← definicja, wydarzenie/postać ← opis."""
    out = []
    for p, ty in F:
        if p.startswith('Wyjaśnij pojęcie: '):
            term = p[len('Wyjaśnij pojęcie: '):].strip()
            if not _stem_leak(term, ty):
                out.append((f'Podaj nazwę pojęcia: {ty}', term))
        elif (not p.endswith('?') and not p.endswith(':') and len(p) <= 60 and p.split()[0] not in OGOLNE
              and not SLABA_ODWROTKA.search(p)):
            if not _stem_leak(p, ty):
                out.append((f'Rozpoznaj: {ty}', p))
    return out


def build_unit(uid, nr, nazwa, t):
    ref = f'{PP}, {"wymagania ogólne " + nr[4:] if nr.startswith("og.") else "dz. " + nr}'
    u = {'id': uid, 'nazwa': t.get('nazwa', nazwa), 'opis': f'Wymaganie {nr} podstawy programowej.', 'wymaganie': nr, 'fiszki': [], 'pytania': []}
    F = [(p, ty) for p, ty in t.get('F', []) if (uid, p) not in USUN]
    seen = set()
    for p, ty in F + reverse_cards(F):
        fid = _id('f', p)
        if fid in seen:
            continue
        seen.add(fid)
        u['fiszki'].append({'id': fid, 'przod': p, 'tyl': ty, 'zrodlo': f'Opracowanie IndexLab · {ref}'})
    for q, odp, wyj in t.get('Q', []):
        if (uid, q) in USUN_Q:
            continue
        if q in ODP:
            odp = ODP[q]
            UZYTE_ODP.add(q)
        star = [k for k, a in enumerate(odp) if a.startswith('*')]
        assert len(star) == 1, (uid, q)
        # stała, ale „losowa” kolejność odpowiedzi (zależna od treści pytania), żeby poprawna nie stała zawsze na tym samym miejscu
        los = random.Random(hashlib.sha1(q.encode()).hexdigest())
        kolej = list(range(len(odp)))
        los.shuffle(kolej)
        odp2 = [odp[k] for k in kolej]
        u['pytania'].append({'id': _id('p', q), 'pytanie': q, 'odpowiedzi': [a.lstrip('*') for a in odp2],
                             'poprawna': 'ABCD'[kolej.index(star[0])], 'wyjasnienie': wyj, 'zrodlo': 'Zadanie autorskie IndexLab'})
    return u


ZASADY = {
    1: '1 pkt – odpowiedź poprawna, zgodna z poleceniem, z właściwą terminologią (przy rozstrzygnięciu — z trafnym uzasadnieniem).\n0 pkt – odpowiedź niepełna, niezgodna z poleceniem, z błędem merytorycznym lub brak odpowiedzi.',
    2: '2 pkt – odpowiedź pełna i poprawna (oba wymagane elementy).\n1 pkt – poprawny jeden z dwóch elementów.\n0 pkt – odpowiedź niepoprawna lub brak odpowiedzi.',
    3: '3 pkt – odpowiedź pełna (wszystkie trzy elementy).\n2 pkt – poprawne dwa elementy.\n1 pkt – poprawny jeden element.\n0 pkt – odpowiedź niepoprawna lub brak odpowiedzi.',
}


def bank_zadanie(typ, pkt, polecenie, odpowiedz, omowienie=None):
    z = {'typ': typ, 'punkty': pkt, 'polecenie': polecenie, 'odpowiedz': odpowiedz, 'zasady': ZASADY.get(pkt, '')}
    if omowienie:
        z['omowienie'] = omowienie
    return z


def bank_wiazka(tytul, material, *zadania, zrodlo='Zadanie autorskie IndexLab. Tekst autorski.'):
    return {'tytul': tytul, 'material': material, 'zrodlo': zrodlo, 'zadania': list(zadania)}


def main():
    T = load_tresci()
    S = load_schematy()
    os.makedirs(OUT, exist_ok=True)
    known = set()
    aktywne = []
    for did, dn, opis, tematy in DZIALY:
        if not any(t[0] in T for t in tematy):
            continue  # dział jeszcze bez treści — nie pokazujemy go w aplikacji
        aktywne.append(did)
        units = []
        for uid, nr, nazwa in tematy:
            known.add(uid)
            if uid not in T:
                continue
            u = build_unit(uid, nr, nazwa, T.get(uid, {}))
            if S.get(uid):
                u['schematy'] = S[uid]
            units.append(u)
        with open(os.path.join(OUT, did + '.json'), 'w') as o:
            json.dump({'id': did, 'nazwa': dn, 'opis': opis, 'poddzialy': units}, o, ensure_ascii=False, indent=1)
            o.write('\n')
    assert UZYTE_ODP == set(ODP), ('wyrownania.py: pytania, których nie ma w treściach', set(ODP) - UZYTE_ODP)
    extra = set(T) - {t[0] for d in DZIALY for t in d[3]}
    assert not extra, f'treści dla nieznanych poddziałów: {extra}'
    assert not set(S) - known, f'schematy dla nieznanych poddziałów: {set(S) - known}'

    # bank zadań autorskich: pliki bank*.py definiują słownik BANK {id działu: [wiązki]}
    bank = {}
    for f in sorted(glob.glob(os.path.join(SRC, 'bank*.py'))):
        for did, ws in runpy.run_path(f, init_globals={'B': bank_wiazka, 'T': bank_zadanie})['BANK'].items():
            bank.setdefault(did, []).extend(ws)
    os.makedirs(os.path.join(OUT, 'bank'), exist_ok=True)
    nb = 0
    uzyte = set()
    for did in bank:
        for i, w in enumerate(bank[did], 1):
            w['id'] = f'b-{did}-{i:02d}'  # numer nadany przed usunięciami — postępy uczniów się nie przesuwają
        zostaw = []
        for w in bank[did]:
            k = next((k for k in USUN_W if k[0] == did and w['material'].startswith(k[1])), None)
            if k:
                uzyte.add(k)
                continue
            for (d2, pocz), nowy in TYTULY_W.items():
                if d2 == did and w['material'].startswith(pocz):
                    w['tytul'] = nowy
                    uzyte.add((d2, pocz))
            zostaw.append(w)
        bank[did] = zostaw
    assert uzyte == set(USUN_W) | set(TYTULY_W), ('nieużyte wpisy w usuniete.py', set(USUN_W) | set(TYTULY_W) - uzyte)
    for did, ws in bank.items():
        assert did in {d[0] for d in DZIALY}, did
        for w in ws:
            w['dzial'] = did
            for j, z in enumerate(w['zadania'], 1):
                z['nr'] = str(j)
            nb += len(w['zadania'])
        with open(os.path.join(OUT, 'bank', did + '.json'), 'w') as o:
            json.dump({'dzial': did, 'wiazki': ws}, o, ensure_ascii=False, indent=1)
            o.write('\n')
    print(f'bank zadań autorskich: {sum(len(v) for v in bank.values())} wiązek, {nb} zadań')

    ap = os.path.join(SRC, 'arkusze.py')
    arkusze = runpy.run_path(ap)['ARKUSZE'] if os.path.exists(ap) else []
    op = os.path.join(SRC, 'omowienia_ark.py')
    OM = runpy.run_path(op)['OM'] if os.path.exists(op) else {}
    uzyte_om = set()
    for a in arkusze:
        for w in a['wiazki']:
            for z in w['zadania']:
                k = (a['id'], z['nr'])
                if k in OM:
                    assert not z.get('omowienie'), ('omówienie już jest', k)
                    z['omowienie'] = OM[k]
                    uzyte_om.add(k)
    assert uzyte_om == set(OM), ('nieużyte omówienia', set(OM) - uzyte_om)
    os.makedirs(os.path.join(OUT, 'arkusze'), exist_ok=True)
    for a in arkusze:
        with open(os.path.join(OUT, 'arkusze', a['id'] + '.json'), 'w') as o:
            json.dump(a, o, ensure_ascii=False, indent=1)
            o.write('\n')

    subj = {
        'id': 'chemia', 'nazwa': 'Chemia', 'skrot': 'CHE',
        'opis': 'Matura rozszerzona z chemii — wymagania egzaminacyjne 2027, obliczenia krok po kroku, zadania w stylu CKE.',
        'dzialy': [{'id': d, 'plik': f'chemia/{d}.json'} for d in aktywne],
        'arkusze': [{'id': a['id'], 'plik': f'chemia/arkusze/{a["id"]}.json'} for a in arkusze],
        'bank': [{'plik': f'chemia/bank/{d}.json'} for d in sorted(bank)],
        # data matury z chemii 2027 — do uzupełnienia z harmonogramu CKE (docs/13-chemia-plan.md)
    }
    with open(os.path.join(ROOT, 'przedmioty', 'chemia.json'), 'w') as o:
        json.dump(subj, o, ensure_ascii=False, indent=1)
        o.write('\n')
    nf = len({(k, _id('f', p)) for k, v in T.items() for p, _ in v.get('F', []) if (k, p) not in USUN})  # bez powtórzeń wewnątrz poddziału
    nq = sum(1 for k, v in T.items() for q in v.get('Q', []) if (k, q[0]) not in USUN_Q)
    print(f'chemia: {len(aktywne)} działów, {len(known)} poddziałów ({len(T)} z treścią), {nf} fiszek, {nq} pytań, {len(arkusze)} arkuszy, {sum(len(v) for v in S.values())} schematów')


if __name__ == '__main__':
    main()
