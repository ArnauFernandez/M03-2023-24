"""
Arnau Fernandez Pinar 
ASIXc M03 UF1 Ex2
Javier Amaya
Matrixalfil
13/12/2022
"""
BLANC = "B"
NEGRE = "N"
MESURA_TAULA = int(input("Tablero tamaño"))
BASE = int(input("Punto X"))
ALTURA = int(input("Punto Y"))

for x in range(MESURA_TAULA):
    for y in range(MESURA_TAULA):
        if x == BASE and y == ALTURA:
            print(MARK, end="")
        else:
            print(BLANC if y % 2 == x % 2 else NEGRE, end="")
    print()