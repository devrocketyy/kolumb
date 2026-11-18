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
    15: 'Kryterium A — rzeczowość i argumentacja (0–12 pkt): jasne stanowisko wobec tezy; argumenty dotyczące wszystkich wymaganych aspektów lub postaci; poprawna i szeroka faktografia (daty, nazwy, przykłady); dostrzeżenie kontrargumentów i złożoności zjawiska; wniosek zgodny ze stanowiskiem.\nKryterium B — kompozycja i spójność (0–3 pkt): wstęp, rozwinięcie i zakończenie; logiczne powiązanie argumentów; poprawny język.\nMinimum 300 wyrazów. Praca nie na temat lub bez stanowiska — 0 pkt.',
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
            units.append(build_unit(uid, nr, nazwa, T.get(uid, {})))
        with open(os.path.join(OUT, did + '.json'), 'w') as o:
            json.dump({'id': did, 'nazwa': dn, 'opis': opis, 'poddzialy': units}, o, ensure_ascii=False, indent=1)
            o.write('\n')
    extra = set(T) - {t[0] for d in DZIALY for t in d[3]}
    assert not extra, f'treści dla nieznanych poddziałów: {extra}'

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
            w['id'] = f'b-{did}-{i:02d}'
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
    nf = sum(len(v.get('F', [])) for v in T.values())
    nq = sum(len(v.get('Q', [])) for v in T.values())
    print(f'biologia: {len(aktywne)} działów, {len(known)} poddziałów ({len(T)} z treścią), {nf} fiszek, {nq} pytań, {len(arkusze)} arkuszy')


if __name__ == '__main__':
    main()
