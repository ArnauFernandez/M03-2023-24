"""
Implementar un programa, que:
● Crea una taula bidimensional de longitud 5x15
● Carrega la taula amb únicament zeros i uns, on els uns ocuparan les posicions o
elements que delimiten la taula, és a dir, les més externes, mentre que la resta
dels elements contindran zeros.
● Mostra el contingut de la matriu a la pantalla, és a dir, mostra el següent:
111111111111111
100000000000001
100000000000001
100000000000001
111111111111111

"""
taula = []
for i in range(5):
    taula.append([])
    for j in range(15):
        taula[i].append(0)
for i in range(5):
    taula[i][0] = 1
    taula[i][14] = 1
for i in range(15):
    taula[0][i] = 1
    taula[4][i] = 1
for i in taula:
    print(i)