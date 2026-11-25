# Schematy chemii — porcja 8: domknięcie do 100 schematów.
S = {}
P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-geometria'] = [
    P('Ocena polarności cząsteczki', [
        ('Czy wiązania są spolaryzowane?', 'różnica elektroujemności atomów'),
        ('Ustal kształt', 'VSEPR — z liczby przestrzennej i wolnych par'),
        ('Czy kształt jest symetryczny?', 'liniowy, trójkątny płaski, tetraedr z jednakowymi podstawnikami'),
        ('Symetryczny', 'cząsteczka niepolarna (CO₂, BF₃, CCl₄)'),
        ('Niesymetryczny', 'cząsteczka polarna (H₂O, NH₃, CHCl₃)'),
    ]),
]
S['c-stezenia'] = [
    P('Sporządzanie roztworu o określonym stężeniu molowym', [
        ('Oblicz masę substancji', 'm = c · V · M'),
        ('Odważ substancję', 'na wadze analitycznej'),
        ('Rozpuść w zlewce', 'w niewielkiej ilości wody'),
        ('Przenieś do kolby miarowej', 'przepłucz zlewkę i lejek'),
        ('Uzupełnij do kreski', 'menisk dolny na wysokości kreski, wymieszaj'),
    ]),
]
