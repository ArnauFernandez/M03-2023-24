"""
Exercici 10
Escriure un programa que:
● Crea una taula (llista amb dues dimensions) de 5x5 nombres enters
● Llegeix per teclat els nombres enters per a cada casella de la taula
● Mostra per pantalla la suma de tots els elements de cada fila i la suma de tots els
elements de cada columna
Pista: una taula es pot veure com una llista de llistes.
"""
taula = []
for i in range(5):
    taula.append([])
    for j in range(5):
        taula[i].append(int(input("Introduce un numero ")))
for i in taula:
    print(i)
for i in range(5):
    print("La suma de la fila ", i, " es ", sum(taula[i]))
for i in range(5):
    suma = 0
    for j in range(5):
        suma += taula[j][i]
    print("La suma de la columna ", i, " es ", suma)