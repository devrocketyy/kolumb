#!/usr/bin/env python3
"""IndexLab — buduje kurs biologii (przedmioty/biologia.json + przedmioty/biologia/*.json).

Struktura: wymagania egzaminacyjne z biologii obowiązujące od 2025 r. (matura 2027), plan w docs/07-biologia-plan.md.
Treści autorskie: narzedzia/biologia/tresci*.py (fiszki, pytania), bank*.py (zadania), arkusze.py (omówienia arkuszy CKE).
Działy bez treści nie trafiają do aplikacji.

Użycie: python3 narzedzia/zbuduj-biologie.py && node narzedzia/zbuduj-indeks.mjs
"""
import random
import json, os, glob, runpy, hashlib, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'przedmioty', 'biologia')
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'biologia')

# (id działu, nazwa, opis, [(id poddziału, wymaganie, nazwa)]) — plan: docs/07-biologia-plan.md
DZIALY = [
 ('umiejetnosci', 'Umiejętności egzaminacyjne', 'Czasowniki operacyjne, metodologia badań, analiza danych i konstruowanie wykresów.', [
  ('b-czasowniki', 'og. IV', 'Czasowniki operacyjne i budowa odpowiedzi'),
  ('b-metodologia', 'og. II', 'Metodologia badań biologicznych'),
  ('b-dane', 'og. III', 'Analiza danych: wykresy, tabele, statystyka'),
  ('b-wykresy', 'og. III', 'Konstruowanie wykresów, tabel i schematów')]),
 ('biochemia', 'Biochemia', 'Woda, pierwiastki, węglowodany, białka, lipidy i kwasy nukleinowe.', [
  ('b-woda', 'I.1', 'Woda, makro- i mikroelementy'),
  ('b-weglowodany', 'I.2.1', 'Węglowodany'),
  ('b-bialka', 'I.2.2', 'Białka'),
  ('b-lipidy', 'I.2.3', 'Lipidy'),
  ('b-kwasy', 'I.2.4', 'Kwasy nukleinowe')]),
 ('komorka', 'Komórka', 'Budowa komórki, błony i transport, organella, endosymbioza.', [
  ('b-typy-komorek', 'II.1, II.13–14', 'Typy komórek i obserwacje mikroskopowe'),
  ('b-blony', 'II.2–4', 'Błona komórkowa, transport, osmoza i plazmoliza'),
  ('b-jadro', 'II.5–7', 'Jądro, rybosomy i system błon wewnątrzkomórkowych'),
  ('b-mitochondria', 'II.8–9', 'Mitochondria, plastydy i endosymbioza'),
  ('b-sciana', 'II.10–12', 'Ściana komórkowa, wakuola i cytoszkielet')]),
 ('metabolizm', 'Metabolizm', 'ATP i przenośniki, enzymy, fotosynteza, oddychanie komórkowe, fermentacje.', [
  ('b-atp', 'III.1–2', 'Szlaki metaboliczne, ATP i przenośniki elektronów'),
  ('b-enzymy', 'III.3', 'Enzymy'),
  ('b-fotosynteza', 'III.4', 'Fotosynteza'),
  ('b-oddychanie', 'III.5.1–4, 6', 'Oddychanie komórkowe'),
  ('b-fermentacje', 'III.5.5, 7', 'Fermentacje, glukoneogeneza i glikogenoliza')]),
 ('podzialy', 'Podziały komórkowe i genom', 'Organizacja DNA, replikacja, cykl komórkowy, mitoza, mejoza, apoptoza.', [
  ('b-genom', 'IV.1', 'Organizacja materiału genetycznego'),
  ('b-replikacja', 'IV.2', 'Replikacja DNA'),
  ('b-cykl', 'IV.3', 'Cykl komórkowy i ploidalność'),
  ('b-mitoza-mejoza', 'IV.4–7, 9', 'Mitoza, mejoza i cytokineza'),
  ('b-apoptoza', 'IV.8', 'Apoptoza')]),
 ('genetyka-molekularna', 'Genetyka molekularna', 'Budowa genu, transkrypcja, translacja, kod genetyczny i regulacja ekspresji.', [
  ('b-gen', 'XIII.1', 'Budowa genu'),
  ('b-transkrypcja', 'XIII.2–3', 'Transkrypcja i obróbka RNA'),
  ('b-translacja', 'XIII.4–6', 'Kod genetyczny i translacja'),
  ('b-regulacja', 'XIII.7', 'Regulacja ekspresji genów')]),
 ('genetyka', 'Genetyka klasyczna i zmienność', 'Krzyżówki, sprzężenia, płeć, rodowody, mutacje i choroby genetyczne.', [
  ('b-krzyzowki', 'XIV.1.1', 'Krzyżówki jedno- i dwugenowe'),
  ('b-wspoldzialanie', 'XIV.1.2', 'Współdziałanie genów i allele wielokrotne'),
  ('b-sprzezenia', 'XIV.1.3–4', 'Geny sprzężone i mapy genowe'),
  ('b-plec', 'XIV.1.5–7', 'Płeć, cechy sprzężone z płcią i dziedziczenie pozajądrowe'),
  ('b-rodowody', 'XIV.1.8', 'Analiza rodowodów'),
  ('b-mutacje', 'XIV.2.1–6', 'Zmienność, mutacje i aberracje'),
  ('b-choroby-genetyczne', 'XIV.2.7–9', 'Choroby genetyczne, mutageny i nowotwory')]),
 ('biotechnologia', 'Biotechnologia', 'Biotechnologia tradycyjna i molekularna, GMO, klonowanie, medycyna, etyka.', [
  ('b-biotech-tradycyjna', 'XV.1–2', 'Biotechnologia tradycyjna'),
  ('b-techniki', 'XV.3–5', 'Narzędzia i techniki inżynierii genetycznej'),
  ('b-gmo', 'XV.6–9', 'GMO, klonowanie i komórki macierzyste'),
  ('b-biotech-medycyna', 'XV.10–14', 'Terapia genowa, poradnictwo i etyka')]),
 ('mikroorganizmy', 'Mikroorganizmy', 'Wirusy, bakterie i archeowce, protisty, grzyby i porosty.', [
  ('b-wirusy', 'XII', 'Wirusy'),
  ('b-bakterie', 'VI', 'Bakterie i archeowce'),
  ('b-protisty', 'VIII', 'Protisty'),
  ('b-grzyby', 'VII', 'Grzyby i porosty')]),
 ('rosliny', 'Rośliny', 'Różnorodność, tkanki i organy, gospodarka wodna, odżywianie, rozmnażanie, wzrost i rozwój.', [
  ('b-przeglad-roslin', 'IX.1, IX.2.1–2', 'Glony i przegląd roślin lądowych'),
  ('b-tkanki-roslinne', 'IX.2.3–4', 'Tkanki roślinne'),
  ('b-organy', 'IX.2.5–8', 'Organy wegetatywne i ich modyfikacje'),
  ('b-gospodarka-wodna', 'IX.3', 'Gospodarka wodna i mineralna'),
  ('b-odzywianie-roslin', 'IX.4', 'Odżywianie roślin, C4 i CAM'),
  ('b-rozmnazanie-roslin', 'IX.5', 'Przemiana pokoleń i rozmnażanie'),
  ('b-rozwoj-roslin', 'IX.6–7', 'Wzrost, rozwój, hormony i ruchy roślin')]),
 ('zwierzeta', 'Zwierzęta i systematyka', 'Zasady klasyfikacji, kladogramy, bezkręgowce i kręgowce.', [
  ('b-systematyka', 'V', 'Klasyfikacja i kladogramy'),
  ('b-bezkregowce', 'X', 'Bezkręgowce'),
  ('b-kregowce', 'X', 'Kręgowce')]),
 ('fizjologia', 'Fizjologia człowieka i zwierząt', 'Tkanki, odżywianie, odporność, oddychanie, krążenie, wydalanie, hormony, układ nerwowy, ruch, rozmnażanie.', [
  ('b-tkanki-zwierzece', 'XI.1', 'Tkanki, narządy i homeostaza'),
  ('b-odzywianie', 'XI.2.1', 'Odżywianie i trawienie'),
  ('b-odpornosc', 'XI.2.2', 'Odporność'),
  ('b-oddychanie-czl', 'XI.2.3 a–j', 'Wymiana gazowa'),
  ('b-krazenie', 'XI.2.3 k–s', 'Krążenie'),
  ('b-wydalanie', 'XI.2.4', 'Wydalanie i osmoregulacja'),
  ('b-hormony', 'XI.2.5', 'Regulacja hormonalna'),
  ('b-nerwy', 'XI.2.6', 'Układ nerwowy i zmysły'),
  ('b-ruch', 'XI.2.7', 'Ruch'),
  ('b-skora', 'XI.2.8', 'Pokrycie ciała i termoregulacja'),
  ('b-rozmnazanie', 'XI.2.9', 'Rozmnażanie i rozwój')]),
 ('ewolucja-ekologia', 'Ewolucja, ekologia i ochrona przyrody', 'Dobór, genetyka populacji, specjacja, nisza, populacje, ekosystemy, ochrona.', [
  ('b-dobor', 'XVI.1–5', 'Dowody ewolucji i dobór naturalny'),
  ('b-populacje-genetyka', 'XVI.6–9', 'Genetyka populacji'),
  ('b-specjacja', 'XVI.10–18', 'Specjacja i ewolucja człowieka'),
  ('b-nisza', 'XVII.1', 'Ekologia organizmów i nisza'),
  ('b-populacje', 'XVII.2, XVII.3.1–5', 'Populacje i zależności międzygatunkowe'),
  ('b-ekosystem', 'XVII.3.6–9', 'Ekosystem i obiegi materii'),
  ('b-ochrona', 'XVIII', 'Różnorodność biologiczna i jej ochrona')]),
]

PP = 'Wymagania egzaminacyjne 2027, biologia (zakres rozszerzony)'
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
        'id': 'biologia', 'nazwa': 'Biologia', 'skrot': 'BIO',
        'opis': 'Matura rozszerzona z biologii — wymagania egzaminacyjne 2027, zadania w stylu CKE.',
        'dzialy': [{'id': d, 'plik': f'biologia/{d}.json'} for d in aktywne],
        'arkusze': [{'id': a['id'], 'plik': f'biologia/arkusze/{a["id"]}.json'} for a in arkusze],
        'bank': [{'plik': f'biologia/bank/{d}.json'} for d in sorted(bank)],
    }
    with open(os.path.join(ROOT, 'przedmioty', 'biologia.json'), 'w') as o:
        json.dump(subj, o, ensure_ascii=False, indent=1)
        o.write('\n')
    nf = sum(1 for k, v in T.items() for p, _ in v.get('F', []) if (k, p) not in USUN)
    nq = sum(1 for k, v in T.items() for q in v.get('Q', []) if (k, q[0]) not in USUN_Q)
    print(f'biologia: {len(aktywne)} działów, {len(known)} poddziałów ({len(T)} z treścią), {nf} fiszek, {nq} pytań, {len(arkusze)} arkuszy, {sum(len(v) for v in S.values())} schematów')


if __name__ == '__main__':
    main()
