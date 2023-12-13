"""
Arnau Fernández Pinar
Matteo Vilchez
e4
Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella
Blanca i és de mida 8x8 sempre ;-)
28/11/2023
"""
BLANC ="▯▯"
NEGRE ="██"
num=9
i=1
for x in range(8):
    linia=""
    num = num - 1
    for y in range(8):
        if i==1:
            linia = linia + BLANC
        else:
            linia = linia + NEGRE
        i=i*-1
    i=i*-1
    print(num,linia)