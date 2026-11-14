#!/usr/bin/env python3
"""IndexLab — buduje kurs historii (przedmioty/historia.json + przedmioty/historia/*.json).

Struktura działów i tematów = wymagania szczegółowe z podstawy programowej 2024
(Dz.U. 2024 poz. 1019, załącznik nr 1 — historia, zakres rozszerzony), które według
informatora CKE sprawdza matura z historii od 2026 r.
Treści (fiszki, pytania) są autorskie i leżą w narzedzia/historia/tresci*.py.

Użycie: python3 narzedzia/zbuduj-historie.py && node narzedzia/zbuduj-indeks.mjs
"""
import random
import json, os, glob, runpy, hashlib, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'przedmioty', 'historia')
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historia')

# (id działu, nazwa, opis, [(id tematu, nr wymagania, nazwa)])
DZIALY = [
 ('umiejetnosci', 'Wprowadzenie i umiejętności egzaminacyjne', 'Historia jako nauka, chronologia, praca ze źródłem i wypowiedź argumentacyjna.', [
  ('h-nauka', 'I', 'Historia jako nauka'),
  ('h-chronologia', 'og. I', 'Chronologia historyczna'),
  ('h-zrodla', 'og. II', 'Analiza i interpretacja źródeł'),
  ('h-narracja', 'og. III', 'Wypowiedź argumentacyjna')]),
 ('starozytnosc', 'Starożytność', 'Pradzieje, starożytny Wschód, Grecja i Rzym.', [
  ('h-wschod', 'II', 'Pradzieje i historia starożytnego Wschodu'),
  ('h-grecja', 'III', 'Świat starożytnych Greków'),
  ('h-rzym', 'IV', 'Społeczeństwo, życie polityczne i kultura starożytnego Rzymu')]),
 ('sredniowiecze', 'Średniowiecze', 'Europa i Polska od upadku Rzymu do końca XV w.', [
  ('h-bizancjum', 'V', 'Bizancjum i świat islamu'),
  ('h-wczesne-sredniowiecze', 'VI', 'Europa wczesnego średniowiecza'),
  ('h-krucjaty', 'VII', 'Europa w okresie krucjat'),
  ('h-realia-sredniowiecza', 'VIII', 'Gospodarcze i społeczne realia średniowiecznej Europy'),
  ('h-piastowie', 'IX', 'Polska w okresie wczesnopiastowskim'),
  ('h-rozbicie', 'X', 'Polska w okresie rozbicia dzielnicowego'),
  ('h-pozne-sredniowiecze', 'XI', 'Europa późnego średniowiecza'),
  ('h-polska-xiv-xv', 'XII', 'Polska w XIV i XV w.'),
  ('h-kultura-sredniowiecza', 'XIII', 'Kultura średniowiecza')]),
 ('nowozytnosc', 'Nowożytność (XVI–XVII w.)', 'Odkrycia, renesans, reformacja i Rzeczpospolita Obojga Narodów.', [
  ('h-odkrycia', 'XIV', 'Odkrycia geograficzne i europejski kolonializm doby nowożytnej'),
  ('h-renesans', 'XV', 'Czasy renesansu'),
  ('h-reformacja', 'XVI', 'Reformacja i jej skutki'),
  ('h-europa-xvi-xvii', 'XVII', 'Europa w XVI i XVII w.'),
  ('h-ostatni-jagiellonowie', 'XVIII', 'Państwo polsko-litewskie w czasach ostatnich Jagiellonów'),
  ('h-unia-lubelska', 'XIX', 'Powstanie Rzeczypospolitej Obojga Narodów'),
  ('h-wolne-elekcje', 'XX', 'Pierwsze wolne elekcje i ich następstwa'),
  ('h-renesans-polska', 'XXI', 'Renesans w Polsce'),
  ('h-ron-xvii-polityka', 'XXII', 'Polityka wewnętrzna i zagraniczna Rzeczypospolitej w XVII w.'),
  ('h-ron-xvii-ustroj', 'XXIII', 'Ustrój, społeczeństwo i kultura Rzeczypospolitej w XVII w.')]),
 ('xviii-wiek', 'Wiek XVIII i epoka napoleońska', 'Oświecenie, rewolucje, upadek Rzeczypospolitej i Napoleon.', [
  ('h-oswiecenie', 'XXIV', 'Europa w dobie oświecenia'),
  ('h-rewolucje-xviii', 'XXV', 'Rewolucje XVIII w.'),
  ('h-rp-xviii', 'XXVI', 'Rzeczpospolita w XVIII w. (od czasów saskich do Konstytucji 3 maja)'),
  ('h-upadek-rp', 'XXVII', 'Upadek Rzeczypospolitej'),
  ('h-kultura-oswiecenia', 'XXVIII', 'Kultura doby oświecenia w Rzeczypospolitej'),
  ('h-napoleon', 'XXIX', 'Epoka napoleońska')]),
 ('xix-wiek', 'Wiek XIX', 'Europa po kongresie wiedeńskim i ziemie polskie pod zaborami.', [
  ('h-po-kongresie', 'XXX', 'Europa i świat po kongresie wiedeńskim'),
  ('h-ziemie-1815-1848', 'XXXI', 'Ziemie polskie i ich mieszkańcy w latach 1815–1848'),
  ('h-powstanie-styczniowe', 'XXXII', 'Powstanie styczniowe i jego następstwa'),
  ('h-swiat-xix-xx', 'XXXIII', 'Europa i świat w II połowie XIX i na początku XX w.'),
  ('h-przemiany-xix', 'XXXIV', 'Przemiany gospodarcze i społeczne. Nowe prądy ideowe'),
  ('h-zabory-xix-xx', 'XXXV', 'Ziemie polskie pod zaborami w II połowie XIX i na początku XX w.'),
  ('h-kultura-xix', 'XXXVI', 'Kultura i nauka polska w II połowie XIX i na początku XX w.')]),
 ('lata-1914-1939', 'I wojna światowa i dwudziestolecie', 'Wielka Wojna, odrodzenie Polski, totalitaryzmy i II Rzeczpospolita.', [
  ('h-i-wojna', 'XXXVII', 'I wojna światowa'),
  ('h-sprawa-polska-iws', 'XXXVIII', 'Sprawa polska w przededniu i podczas I wojny światowej'),
  ('h-europa-po-iws', 'XXXIX', 'Europa i świat po I wojnie światowej'),
  ('h-totalitaryzmy', 'XL', 'Narodziny i rozwój totalitaryzmów w okresie międzywojennym'),
  ('h-odrodzenie', 'XLI', 'Walka o odrodzenie państwa polskiego po I wojnie światowej'),
  ('h-ii-rp-polityka', 'XLII', 'Dzieje polityczne II Rzeczypospolitej'),
  ('h-ii-rp-spoleczenstwo', 'XLIII', 'Społeczeństwo i gospodarka II Rzeczypospolitej'),
  ('h-ii-rp-kultura', 'XLIV', 'Kultura i nauka w okresie II Rzeczypospolitej')]),
 ('ii-wojna', 'II wojna światowa', 'Droga do wojny, wrzesień 1939, okupacja, Holokaust i Polskie Państwo Podziemne.', [
  ('h-droga-do-wojny', 'XLV', 'Świat na drodze do II wojny światowej'),
  ('h-wrzesien-1939', 'XLVI', 'Wojna obronna Polski w 1939 r.'),
  ('h-ii-wojna', 'XLVII', 'II wojna światowa i jej etapy'),
  ('h-okupacja', 'XLVIII', 'Polska pod okupacją niemiecką i sowiecką'),
  ('h-eksterminacja', 'XLIX', 'Niemiecka polityka eksterminacji'),
  ('h-panstwo-podziemne', 'L', 'Władze RP na uchodźstwie i w okupowanym kraju')]),
 ('swiat-po-1945', 'Świat po 1945 r.', 'Zimna wojna, dekolonizacja, integracja i przemiany cywilizacyjne.', [
  ('h-zimna-wojna', 'LI', 'Świat po II wojnie światowej. Początek zimnej wojny'),
  ('h-dekolonizacja', 'LII', 'Dekolonizacja, integracja i nowe konflikty'),
  ('h-przemiany-cywilizacyjne', 'LIII', 'Przemiany cywilizacyjne na świecie'),
  ('h-przelom-tysiacleci', 'LIV', 'Świat na przełomie tysiącleci')]),
 ('polska-po-1945', 'Polska po 1945 r.', 'Od przejęcia władzy przez komunistów do III Rzeczypospolitej.', [
  ('h-przejecie-wladzy', 'LV', 'Przejmowanie władzy przez komunistów w Polsce (1944–1948)'),
  ('h-stalinizm', 'LVI', 'Stalinizm w Polsce i jego erozja'),
  ('h-prl-1957-1981', 'LVII', 'Polska w latach 1957–1981'),
  ('h-dekada-80', 'LVIII', 'Dekada 1981–1989'),
  ('h-iii-rp', 'LIX', 'Narodziny III Rzeczypospolitej i jej miejsce w świecie')]),
]

PP = 'Podstawa programowa 2024, historia (zakres rozszerzony)'
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


def reverse_cards(F):
    """Fiszki odwrotne (jak w WOS): pojęcie ← definicja, wydarzenie/postać ← opis."""
    out = []
    for p, ty in F:
        if p.startswith('Wyjaśnij pojęcie: '):
            term = p[len('Wyjaśnij pojęcie: '):].strip()
            if not _stem_leak(term, ty):
                out.append((f'Podaj nazwę pojęcia: {ty}', term))
        elif not p.endswith('?') and not p.endswith(':') and len(p) <= 60 and p.split()[0] not in OGOLNE:
            if not _stem_leak(p, ty):
                out.append((f'Rozpoznaj: {ty}', p))
    return out


def build_unit(uid, nr, nazwa, t):
    ref = f'{PP}, {"wymagania ogólne " + nr[4:] if nr.startswith("og.") else "dz. " + nr}'
    u = {'id': uid, 'nazwa': t.get('nazwa', nazwa), 'opis': f'Wymaganie {nr} podstawy programowej.', 'wymaganie': nr, 'fiszki': [], 'pytania': []}
    F = list(t.get('F', []))
    seen = set()
    for p, ty in F + reverse_cards(F):
        fid = _id('f', p)
        if fid in seen:
            continue
        seen.add(fid)
        u['fiszki'].append({'id': fid, 'przod': p, 'tyl': ty, 'zrodlo': f'Opracowanie IndexLab · {ref}'})
    for q, odp, wyj in t.get('Q', []):
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
    1: '1 pkt – odpowiedź poprawna (przy rozstrzygnięciu — z uzasadnieniem odwołującym się do materiału).\n0 pkt – odpowiedź niepoprawna, niepełna lub brak odpowiedzi.',
    2: '2 pkt – odpowiedź pełna i poprawna.\n1 pkt – odpowiedź częściowo poprawna (np. jeden z dwóch elementów).\n0 pkt – odpowiedź niepoprawna lub brak odpowiedzi.',
    3: '3 pkt – odpowiedź pełna z interpretacją i kontekstem.\n2 pkt – brak jednego elementu.\n1 pkt – odpowiedź częściowa.\n0 pkt – odpowiedź niepoprawna lub brak odpowiedzi.',
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
    os.makedirs(OUT, exist_ok=True)
    known = set()
    for did, dn, opis, tematy in DZIALY:
        units = []
        for uid, nr, nazwa in tematy:
            known.add(uid)
            units.append(build_unit(uid, nr, nazwa, T.get(uid, {})))
        with open(os.path.join(OUT, did + '.json'), 'w') as o:
            json.dump({'id': did, 'nazwa': dn, 'opis': opis, 'poddzialy': units}, o, ensure_ascii=False, indent=1)
            o.write('\n')
    extra = set(T) - known
    assert not extra, f'treści dla nieznanych tematów: {extra}'

    chrono = runpy.run_path(os.path.join(SRC, 'chronologia.py'))['CHRONO']
    with open(os.path.join(OUT, 'chronologia.json'), 'w') as o:
        json.dump(chrono, o, ensure_ascii=False, indent=1)
        o.write('\n')

    # bank zadań autorskich: pliki bank*.py definiują słownik BANK {id działu: [wiązki]}
    bank = {}
    for f in sorted(glob.glob(os.path.join(SRC, 'bank*.py'))):
        for did, ws in runpy.run_path(f, init_globals={'B': bank_wiazka, 'T': bank_zadanie})['BANK'].items():
            bank.setdefault(did, []).extend(ws)
    os.makedirs(os.path.join(OUT, 'bank'), exist_ok=True)
    nb = 0
    for did, ws in bank.items():
        assert did in {d[0] for d in DZIALY}, did
        for i, w in enumerate(ws, 1):
            w['id'] = f'h-{did}-{i:02d}'
            w['dzial'] = did
            for j, z in enumerate(w['zadania'], 1):
                z['nr'] = str(j)
            nb += len(w['zadania'])
        with open(os.path.join(OUT, 'bank', did + '.json'), 'w') as o:
            json.dump({'dzial': did, 'wiazki': ws}, o, ensure_ascii=False, indent=1)
            o.write('\n')
    print(f'bank zadań autorskich: {sum(len(v) for v in bank.values())} wiązek, {nb} zadań')

    arkusze = runpy.run_path(os.path.join(SRC, 'arkusze.py'))['ARKUSZE']
    os.makedirs(os.path.join(OUT, 'arkusze'), exist_ok=True)
    for a in arkusze:
        with open(os.path.join(OUT, 'arkusze', a['id'] + '.json'), 'w') as o:
            json.dump(a, o, ensure_ascii=False, indent=1)
            o.write('\n')

    subj = {
        'id': 'historia', 'nazwa': 'Historia', 'skrot': 'HIS',
        'egzamin': '2027-05-18',  # harmonogram CKE 2027: historia (pr) — 18 maja
        'opis': 'Matura rozszerzona z historii — wszystkie wymagania podstawy programowej 2024.',
        'dzialy': [{'id': d[0], 'plik': f'historia/{d[0]}.json'} for d in DZIALY],
        'arkusze': [{'id': a['id'], 'plik': f'historia/arkusze/{a["id"]}.json'} for a in arkusze],
        'bank': [{'plik': f'historia/bank/{d}.json'} for d in sorted(bank)],
        'aktualnosci': {'plik': 'historia/chronologia.json'},
    }
    with open(os.path.join(ROOT, 'przedmioty', 'historia.json'), 'w') as o:
        json.dump(subj, o, ensure_ascii=False, indent=1)
        o.write('\n')
    nf = sum(len(v.get('F', [])) for v in T.values())
    nq = sum(len(v.get('Q', [])) for v in T.values())
    print(f'historia: {len(DZIALY)} działów, {len(known)} tematów ({len(T)} z treścią), {nf} fiszek, {nq} pytań, {len(arkusze)} arkuszy')


if __name__ == '__main__':
    main()
