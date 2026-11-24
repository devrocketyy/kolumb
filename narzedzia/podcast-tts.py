#!/usr/bin/env python3
"""IndexLab — zamienia scenariusz odcinka na MP3 (Google Cloud Text-to-Speech) i plik z czasami pytań.

  python3 narzedzia/podcast-tts.py podcast/scenariusze/biologia-06-woda.md [--glos pl-PL-Chirp3-HD-Charon]

Wynik: podcast/mp3/<odcinek>.mp3 oraz podcast/mp3/<odcinek>.json (czasy znaczników [pytanie: id],
[odpowiedź] i [koniec odpowiedzi] w sekundach — z nich korzysta tryb aktywny odtwarzacza).

Klucz API nie jest w kodzie: w środowisku Claude dokleja go proxy (nagłówek X-Goog-Api-Key),
a lokalnie można go podać w zmiennej GOOGLE_TTS_KEY.
Wymaga ffmpeg. Chirp 3 HD nie obsługuje SSML, więc pauzy to wstawiona cisza.
"""
import base64, hashlib, json, os, re, subprocess, sys, tempfile, urllib.request

PAUZY = {'pauza': 1.2, 'pauza, dłuższa': 6.0, 'muzyka': 2.0}
TEMPO, TEMPO_WOLNIEJ = 1.0, 0.9  # naturalne tempo; uczeń może zwolnić w odtwarzaczu
KLUCZ = os.environ.get('GOOGLE_TTS_KEY', 'x')  # 'x' — w środowisku Claude prawdziwy klucz wstawia proxy


def mow(tekst, glos, tempo, plik):
    body = {'input': {'text': tekst}, 'voice': {'languageCode': 'pl-PL', 'name': glos},
            'audioConfig': {'audioEncoding': 'LINEAR16', 'sampleRateHertz': 24000, 'speakingRate': tempo}}
    req = urllib.request.Request('https://texttospeech.googleapis.com/v1/text:synthesize', data=json.dumps(body).encode(),
                                 headers={'Content-Type': 'application/json', 'X-Goog-Api-Key': KLUCZ})
    dane = json.load(urllib.request.urlopen(req, timeout=120))
    open(plik, 'wb').write(base64.b64decode(dane['audioContent']))


def cisza(sek, plik):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono',
                    '-t', f'{sek:.2f}', '-c:a', 'pcm_s16le', plik], check=True)


def dlugosc(plik):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', plik],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def segmenty(md):
    """Lista kroków: ('mow', tekst, tempo) | ('cisza', s) | ('znacznik', nazwa, id)."""
    tresc = md.split('\n---\n', 1)[1]
    kroki = []
    for akapit in re.split(r'\n\s*\n', tresc):
        a = akapit.strip()
        if not a or a.startswith('#'):
            continue
        m = re.fullmatch(r'\[(.+?)\]', a)
        if m:
            w = m.group(1).strip()
            if w.startswith('pytanie:'):
                kroki.append(('znacznik', 'pytanie', w.split(':', 1)[1].strip()))
            elif w == 'odpowiedź':
                kroki.append(('znacznik', 'odpowiedz', None))
            elif w == 'koniec odpowiedzi':
                kroki.append(('znacznik', 'koniec', None))
            elif w.startswith('muzyka'):
                kroki.append(('cisza', PAUZY['muzyka']))
            elif w in PAUZY:
                kroki.append(('cisza', PAUZY[w]))
            continue
        tempo = TEMPO
        if a.startswith('[wolniej]'):
            tempo, a = TEMPO_WOLNIEJ, a[len('[wolniej]'):].strip()
        a = re.sub(r'\[[^\]]*\]', '', a).strip()
        if a:
            kroki.append(('mow', a, tempo))
    return kroki


def main():
    zrodlo = sys.argv[1]
    glos = sys.argv[sys.argv.index('--glos') + 1] if '--glos' in sys.argv else 'pl-PL-Chirp3-HD-Charon'
    nazwa = os.path.splitext(os.path.basename(zrodlo))[0]
    os.makedirs('podcast/mp3', exist_ok=True)
    kroki = segmenty(open(zrodlo, encoding='utf-8').read())
    t, czesci, znaczniki, pytanie = 0.0, [], [], None
    tmp = tempfile.mkdtemp()
    for i, k in enumerate(kroki):
        if k[0] == 'znacznik':
            if k[1] == 'pytanie':
                pytanie = {'id': k[2], 'czas': round(t, 2)}
                znaczniki.append(pytanie)
            elif k[1] == 'odpowiedz' and pytanie:
                pytanie['odpowiedz_od'] = round(t, 2)
            elif k[1] == 'koniec' and pytanie:
                pytanie['odpowiedz_do'] = round(t, 2)
            continue
        plik = os.path.join(tmp, f'{i:04d}.wav')
        if k[0] == 'cisza':
            cisza(k[1], plik)
        else:
            surowy = plik + '.raw.wav'
            mow(k[1], glos, k[2], surowy)
            # łagodne wejście i wyjście każdego fragmentu — bez trzasków i „ucięć” na sklejeniach
            d = dlugosc(surowy)
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', surowy, '-af',
                            f'afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.08):.2f}:d=0.08', plik], check=True)
            cisza(0.6, plik + '.c.wav')  # oddech między akapitami
            czesci.append(plik); t += dlugosc(plik)
            plik = plik + '.c.wav'
        czesci.append(plik); t += dlugosc(plik)
        print(f'\r{i + 1}/{len(kroki)}  {t / 60:.1f} min', end='', flush=True)
    lista = os.path.join(tmp, 'lista.txt')
    open(lista, 'w').write(''.join(f"file '{p}'\n" for p in czesci))
    mp3 = f'podcast/mp3/{nazwa}.mp3'
    # wyrównana głośność (standard podcastów: -16 LUFS), łagodne wyciszenie na końcu, lepsza jakość MP3
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
                    '-af', f'loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st={max(0, t - 1.5):.2f}:d=1.5',
                    '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '96k', '-ac', '1', mp3], check=True)
    json.dump({'odcinek': nazwa, 'glos': glos, 'dlugosc': round(t, 1), 'pytania': znaczniki},
              open(f'podcast/mp3/{nazwa}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'\n{mp3}: {t / 60:.1f} min, pytań: {len(znaczniki)}')


if __name__ == '__main__':
    main()
