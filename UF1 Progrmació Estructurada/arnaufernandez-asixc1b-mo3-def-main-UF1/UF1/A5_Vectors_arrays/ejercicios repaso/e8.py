"""
Exercici 8
Volem desar els noms i les edats dels alumnes de curs. Feu un programa que introdueixi
el nom i l'edat de cada alumne. El procés de lectura de dades acabarà quan s'introdueix
com a nom un asterisc (*)
En finalitzar es mostrarà les dades següents:
● Els alumnes majors d’edat
● Els alumnes més vells: per fer això caldrà primer que obtingueu quina és l’edat
més gran que us han entrat i aleshores mostrar els alumnes que tinguin aquesta
edat (pot haver-hi més d’un)
Pistes:
- Per calcular el màxim d’una llista podeu implementar vosaltres mateixos el codi
o podeu fer servir la funció max.
- Els noms i les edats que aneu llegint els haureu de desar en llistes separades.
Exemple:
noms = [‘Rosa’, ‘Joan’, ‘Emma’]
edats = [18, 21, 19]
On Rosa té 18 anys, Joan 21 i Emma 19.
- Si un cop llegits els noms i les edats podeu consultar les dues llistes per separat,
tenint en compte que al primer nom de la llista de noms li correspon la primera
edat de la llista d’edats, al segon nom li correspon la segona edat, i així
successivament, o bé, podeu fe servir la funció zip de Python que us permet
consultar les dues llistes per “parelles”.

"""
noms = []
edats = []

while True:
    nom = input("Introdueix el nom de l'alumne (o * per acabar): ")
    if nom == "*":
        break
    edat = int(input("Introdueix l'edat de l'alumne: "))
    noms.append(nom)
    edats.append(edat)

# Alumnes majors d'edat
majors_d_edat = []
for nom, edat in zip(noms, edats):
    if edat >= 18:
        majors_d_edat.append(nom)
print("Alumnes majors d'edat:", majors_d_edat)

# Alumnes més vells
edat_maxima = max(edats)
alumnes_mes_vells = []
for nom, edat in zip(noms, edats):
    if edat == edat_maxima:
        alumnes_mes_vells.append(nom)
print("Alumnes més vells:", alumnes_mes_vells)
