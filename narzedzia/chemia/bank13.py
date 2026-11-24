# Bank zadań autorskich — chemia, część 13.
BANK = {'umiejetnosci': [
 B('Błędy w odpowiedzi ucznia — równanie jonowe',
   'Tekst autorski. Uczeń zapisał reakcję CaCO₃ z kwasem solnym: CO₃²⁻ + 2H⁺ → CO₂ + H₂O.',
   T('wyjasnij', 1, 'Wskaż błąd i podaj poprawny zapis.', 'CaCO₃ jest trudno rozpuszczalny — nie rozpisuje się go na jony: CaCO₃ + 2H⁺ → Ca²⁺ + CO₂ + H₂O.', 'Typowy błąd z raportów CKE.')),
 B('Błędy w odpowiedzi ucznia — obliczenia',
   'Tekst autorski. Uczeń obliczył pH 0,01 M Ba(OH)₂ jako 12.',
   T('wyjasnij', 1, 'Wskaż błąd i podaj poprawny wynik.', 'Pominął dwie grupy OH⁻: [OH⁻] = 0,02 → pOH = 1,7 → pH = 12,3.', '—')),
 B('Plan doświadczenia — elektroliza',
   'Tekst autorski. Należy wykazać, że podczas elektrolizy roztworu KI przy anodzie powstaje jod.',
   T('podaj', 1, 'Zaproponuj odczynnik do wykrycia jodu i obserwację.', 'Kleik skrobiowy — granatowe zabarwienie przy anodzie.', '—'),
   T('podaj', 1, 'Zaproponuj wskaźnik pokazujący zmianę odczynu przy katodzie i obserwację.', 'Fenoloftaleina — malinowe zabarwienie (powstają jony OH⁻).', '—')),
], 'stechiometria': [
 B('Analiza miareczkowa — Cl⁻ metodą Mohra',
   'Tekst autorski. 20,0 cm³ wody mineralnej zmiareczkowano 0,0100 M AgNO₃ wobec K₂CrO₄ — zużyto 12,0 cm³.',
   T('oblicz', 2, 'Oblicz stężenie jonów Cl⁻ w mg/dm³ (M(Cl) = 35,5).', 'ok. 213 mg/dm³', 'n = 1,2·10⁻⁴ mol w 20 cm³ → 6,0·10⁻³ mol/dm³ · 35,5 g = 0,213 g/dm³.'),
   T('podaj', 1, 'Podaj, jak rozpoznać punkt końcowy.', 'Pojawia się ceglastoczerwony osad Ag₂CrO₄.', 'Wytrąca się po całkowitym strąceniu AgCl.')),
], 'roztwory': [
 B('Stężenie po rozpuszczeniu gazu',
   'Tekst autorski. W 100 cm³ wody rozpuszczono 2,24 dm³ NH₃ (w. n.). Objętość roztworu przyjmij 100 cm³.',
   T('oblicz', 1, 'Oblicz stężenie molowe amoniaku.', '1,0 mol·dm⁻³', '0,1 mol / 0,1 dm³.')),
], 'roztwory-wodne': [
 B('Hydroliza — ilościowo',
   'Tekst autorski. Roztwór NH₄Cl ma stężenie 0,10 mol·dm⁻³; Kb(NH₃) = 1,8·10⁻⁵.',
   T('oblicz', 2, 'Oblicz pH roztworu.', 'pH ≈ 5,1', 'Ka = 5,6·10⁻¹⁰; [H⁺] = √(5,6·10⁻¹¹) = 7,5·10⁻⁶; pH = 5,13.')),
], 'kinetyka': [
 B('Energia wiązań — spalanie metanu',
   'Tekst autorski. Energie wiązań (kJ/mol): C–H 413, O=O 498, C=O (w CO₂) 799, O–H 463.',
   T('oblicz', 2, 'Oblicz ΔH reakcji CH₄ + 2O₂ → CO₂ + 2H₂O(g).', '−802 kJ', 'Zerwane: 4·413 + 2·498 = 2648; utworzone: 2·799 + 4·463 = 3450; ΔH = −802 kJ.')),
], 'redoks': [
 B('Dysproporcjonowanie',
   'Tekst autorski. Chlor wprowadzony do gorącego roztworu KOH tworzy KCl i KClO₃.',
   T('podaj', 2, 'Napisz równanie reakcji (cząsteczkowo) i dobierz współczynniki.', '3Cl₂ + 6KOH → 5KCl + KClO₃ + 3H₂O', 'Cl 0 → −I (×5), 0 → +V (×1).')),
 B('Szereg aktywności — doświadczenie',
   'Tekst autorski. Płytki: Zn, Cu, Ag zanurzono w roztworach: CuSO₄, AgNO₃, ZnSO₄ (każda płytka w każdym roztworze).',
   T('podaj', 2, 'Podaj, w ilu przypadkach zaszła reakcja, i wymień je.', '3: Zn + CuSO₄, Zn + AgNO₃, Cu + AgNO₃', 'Metal aktywniejszy wypiera mniej aktywny.')),
], 'nieorganiczne': [
 B('Otrzymywanie tlenu',
   'Tekst autorski. Tlen otrzymano przez ogrzewanie KMnO₄: 2KMnO₄ → K₂MnO₄ + MnO₂ + O₂.',
   T('oblicz', 1, 'Oblicz objętość tlenu (w. n.) z 31,6 g KMnO₄ (M = 158 g/mol).', '2,24 dm³', '0,2 mol KMnO₄ → 0,1 mol O₂.'),
   T('podaj', 1, 'Podaj, jak sprawdzić, że gaz to tlen.', 'Tlące się łuczywko rozżarza się.', '—')),
], 'organiczna': [
 B('Węglowodory — odróżnianie',
   'Tekst autorski. Trzy gazy: metan, eten, etyn.',
   T('podaj', 2, 'Zaproponuj sposób odróżnienia etynu od etenu.', 'Np. amoniakalny roztwór AgNO₃ (lub CuCl) — etyn tworzy osad acetylenku; eten nie.', 'Woda bromowa odbarwia się z oboma.')),
], 'tlenowe': [
 B('Utlenianie alkoholi dichromianem',
   'Tekst autorski. Trzy alkohole C₄H₁₀O: butan-1-ol, butan-2-ol, 2-metylopropan-2-ol ogrzewano z zakwaszonym K₂Cr₂O₇.',
   T('podaj', 1, 'Podaj, w których probówkach barwa zmieniła się na zieloną.', 'Butan-1-ol i butan-2-ol', 'III-rzędowy nie utlenia się.')),
], 'azotowe-cukry': [
 B('Glukoza — masa srebra',
   'Tekst autorski. 9,0 g glukozy (M = 180 g/mol) poddano próbie Tollensa.',
   T('oblicz', 1, 'Oblicz masę wydzielonego srebra.', '10,8 g', '0,05 mol glukozy → 0,1 mol Ag.')),
], 'chemia-zycia': [
 B('Spalanie paliw — CO₂',
   'Tekst autorski. Samochód spala 5 kg benzyny (przyjmij C₈H₁₈, M = 114 g/mol) na 100 km.',
   T('oblicz', 2, 'Oblicz masę CO₂ emitowaną na 100 km.', 'ok. 15,4 kg', 'n = 43,86 mol · 8 = 350,9 mol CO₂ · 44 g = 15,4 kg.')),
]}
