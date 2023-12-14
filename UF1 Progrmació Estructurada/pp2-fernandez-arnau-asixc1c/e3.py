"""
Arnau Fernandez Pinar
14/12/2023
M03 PP2 UF1
e3 MatrixTower
"""
BLANC ="B"
NEGRE ="N"
num=9
i=1
for x in range(8):
    linia=""
    num = num - 1
    for y in range(8):
        if i==1:
            linia = linia + BLANC + "\t"
        else:
            linia = linia + NEGRE +"\t"
        i=i*-1
    i=i*-1
    print(linia)