# Część chemiczna zbioru testowego. Odpowiedzi AUTORSKIE (IndexLab). Format jak w zbior_biologia.py.
P = 'chemia'
Z = [
 ('2026-maj/24', 'uzasadnij', 'robocza', [
  ('pelna', 'Projekt 2, bo najpierw wprowadzamy grupę nitrową, a ona kieruje następny podstawnik (chlor) w położenie meta.', 1, [], False),
  ('bledna', 'Projekt 1, bo chlor kieruje w położenie meta.', 0, ['projekt 2: –NO₂ kieruje w meta, –Cl w orto/para'], False),
  ('czesciowa', 'Projekt 2.', 0, ['uzasadnienie (kierujący wpływ grupy –NO₂)'], False),
 ]),
 ('2015-maj-f2015/5.1', 'podaj', 'robocza', [
  ('pelna', 'sp², cząsteczka płaska (trójkątna).', 1, [], False),
  ('czesciowa', 'sp³, płaska.', 0, ['hybrydyzacja sp²'], False),
 ]),
 ('2026-styczen/22.2', 'uzasadnij', 'kontrolna', [
  ('pelna', 'CH₃CH₂COOK — kwas propanowy jest najsłabszy, więc jego anion jest najmocniejszą zasadą (największa Kb) i najsilniej hydrolizuje.', 1, [], False),
  ('bledna', 'C₆H₅COOK, bo pierścień benzenowy zwiększa zasadowość.', 0, ['CH₃CH₂COOK – największa Kb anionu'], False),
  ('inne_slowa', 'Roztwór propanianu potasu, bo jon propanianowy ma największą stałą zasadowości.', 1, [], False),
 ]),
 ('2016-maj-f2015/24.2', 'podaj', 'robocza', [
  ('pelna', 'A – kwas propanowy, B – propanon (aceton).', 1, [], False),
  ('popr_plus_blad', 'A – propanal, B – propanon.', 0, ['A – kwas propanowy'], False),
 ]),
 ('2016-maj-f2015/30', 'opisz', 'kontrolna', [
  ('pelna', 'Woda bromowa (Br₂ w CCl₄) się odbarwia, a z Cu(OH)₂ po ogrzaniu wytrąca się ceglastoczerwony osad.', 1, [], False),
  ('czesciowa', 'Brom się odbarwia.', 0, ['ceglasty osad z Cu(OH)₂'], False),
  ('bledna', 'Brom się nie odbarwia, a powstaje szafirowy roztwór.', 0, ['odbarwienie bromu', 'ceglasty osad'], False),
 ]),
 ('2017-maj-f2015/1.3', 'podaj', 'robocza', [
  ('pelna', 'X: H₂Se, Z: CrO₃', 1, [], False),
  ('czesciowa', 'X: H₂Se, Z: Cr₂O₃', 0, ['tlenek na maksymalnym stopniu utlenienia: CrO₃'], False),
 ]),
 ('2022-grudzien/1.2', 'podaj', 'kontrolna', [
  ('pelna', 'X1 (tlen): n = 2, l = 1; X3 (mangan): n = 3, l = 2.', 1, [], False),
  ('bledna', 'X1: n = 2, l = 0; X3: n = 4, l = 0.', 0, ['O: n=2, l=1; Mn: n=3, l=2'], False),
 ]),
 ('2026-czerwiec/11.2', 'oblicz', 'robocza', [
  ('pelna', 'W 150 g wody rozpuści się 1,5 · 20 g = 30 g soli, a dodano 70 g, więc roztwór jest nasycony z osadem. Cp = 30 / (30 + 150) · 100% ≈ 16,7%.', 2, [], False),
  ('czesciowa', 'Roztwór nasycony. Cp = 70 / 220 · 100% = 31,8%.', 1, ['Cp liczone tylko z rozpuszczonej soli (30 g) – ok. 16,7%'], False),
  ('bledna', 'Roztwór nienasycony, Cp = 70/150 = 46,7%.', 0, ['roztwór nasycony', 'Cp ≈ 16,7%'], False),
 ]),
 ('2025-maj/13', 'oblicz', 'robocza', [
  ('pelna', 'N₂ + 3H₂ ⇌ 2NH₃; przereagowało x N₂. Suma: 0,8 − 2x = 0,75 · 0,8 = 0,6 → x = 0,1. [N₂] = 0,1; [H₂] = 0,3; [NH₃] = 0,2. Kc = 0,2² / (0,1 · 0,3³) = 0,04 / 0,0027 ≈ 14,8.', 2, [], False),
  ('czesciowa', 'x = 0,1, więc [N₂] = 0,1, [H₂] = 0,3, [NH₃] = 0,2. Kc = 0,2 / (0,1 · 0,3) = 6,67.', 0, ['błędne wyrażenie na Kc (brak potęg) – błąd metody, wynik ok. 14,8'], False),
  ('bledna', 'Kc = 0,75', 0, ['metoda: bilans stężeń z warunku spadku ciśnienia', 'Kc ≈ 14,8'], False),
 ]),
 ('2019-maj-f2015/35', 'oblicz', 'kontrolna', [
  ('pelna', 'n(I₂) = 0,0108 · 0,052 = 5,616 · 10⁻⁴ mol = n(wit. C) w 10 cm³. W 100 cm³: 5,616 · 10⁻³ mol. m = 5,616 · 10⁻³ · 176 ≈ 0,99 g.', 2, [], False),
  ('czesciowa', 'n(I₂) = 0,0108 · 0,052 = 5,616 · 10⁻⁴ mol; m = 5,616 · 10⁻⁴ · 176 = 0,099 g.', 1, ['przeliczenie z 10 cm³ na całą próbkę (100 cm³)'], False),
 ]),
 ('2026-czerwiec/6', 'wyjasnij', 'robocza', [
  ('pelna', 'To glin. W AlCl₃ glin ma tylko 6 elektronów walencyjnych (luka elektronowa), więc przyjmuje wolną parę elektronową od atomu chloru sąsiedniej cząsteczki i tworzy wiązanie koordynacyjne – powstaje dimer Al₂Cl₆. [wzór elektronowy: Al z trzema wiązaniami do Cl, każdy Cl z trzema wolnymi parami]', 2, [], False),
 ]),
 ('2024-maj/27', 'uzasadnij', 'kontrolna', [
  ('pelna', 'Produkt: BrCH₂–C₆H₄–NH₂ (brom podstawia wodór w grupie metylowej). Tak, to reakcja redoks – zmieniają się stopnie utlenienia węgla i bromu.', 1, [], False),
  ('popr_plus_blad', 'Brom podstawia wodór w pierścieniu benzenowym; reakcja redoks.', 0, ['podstawienie w grupie CH₃ (warunki: światło)'], False),
 ]),
 ('2022-grudzien/8', 'oblicz', 'robocza', [
  ('ogolnik', 'Około 38% glinu, bo tyle wychodzi z proporcji.', 0, ['obliczenia (metoda)'], False),
 ]),
]
