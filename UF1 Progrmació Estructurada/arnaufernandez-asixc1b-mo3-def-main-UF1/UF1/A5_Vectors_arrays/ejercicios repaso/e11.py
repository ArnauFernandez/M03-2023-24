"""
Escriu un programa, que:
● Crea una taula o matriu bidimensional de longitud 5x5 i nom diagonal
● Assigna a cada casella de la matriu el valor 0 o 1 de la manera següent: les
caselles pertanyents a les dues diagonals majors de la matriu prenen el valor 1 i
la resta de les caselles el valor 0
● Mostra el contingut de la matriu a la pantalla.
Sortida del programa per pantalla:
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1

"""
diagonal = []
for i in range(5):
    diagonal.append([])
    for j in range(5):
        diagonal[i].append(0)
for i in range(5):
    diagonal[i][i] = 1
    diagonal[i][4-i] = 1
for i in diagonal:
    print(i)