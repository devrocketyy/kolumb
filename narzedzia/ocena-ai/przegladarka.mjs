// Generuje supabase/do-przegladarki/ocen.ts — jednoplikową wersję funkcji „ocen” do wklejenia w edytorze Supabase.
// Wkleja moduł _shared/ocena-instrukcja.ts w miejsce importu. Uruchom: node narzedzia/ocena-ai/przegladarka.mjs
import { readFileSync, writeFileSync } from 'node:fs';
const k = (p) => new URL(`../../supabase/${p}`, import.meta.url);
const fn = readFileSync(k('functions/ocen/index.ts'), 'utf8');
const mod = readFileSync(k('functions/_shared/ocena-instrukcja.ts'), 'utf8').replace(/^export /gm, '');
const imp = /^import \{[^}]*\} from '\.\.\/_shared\/ocena-instrukcja\.ts';\n/m;
if (!imp.test(fn)) throw new Error('Brak importu ocena-instrukcja.ts w functions/ocen/index.ts');
const naglowek = '// ocen — wersja jednoplikowa do wklejenia w Supabase → Edge Functions → Open Editor (nazwa funkcji: ocen).\n' +
  '// WYGENEROWANA przez narzedzia/ocena-ai/przegladarka.mjs — edytuj functions/ocen/index.ts i _shared/ocena-instrukcja.ts.\n';
writeFileSync(k('do-przegladarki/ocen.ts'), naglowek + fn.replace(imp, `\n// ---- _shared/ocena-instrukcja.ts ----\n${mod}// ---- koniec ----\n\n`));
console.log('Zapisano supabase/do-przegladarki/ocen.ts');
