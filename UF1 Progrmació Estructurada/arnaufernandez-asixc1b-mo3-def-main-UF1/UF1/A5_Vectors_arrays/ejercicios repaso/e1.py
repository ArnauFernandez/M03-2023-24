"""
Exercici 1
Realitzar un programa que inicialitza una llista
amb 10 valors aleatoris (de l'1 al 10) i posteriorment
mostri en pantalla cada nombre de la llista
juntament amb el seu quadrat i el seu cub.
"""

import random

llista = []
for i in range(10):
    llista.append(random.randint(1, 10))

for i in llista:
    print(i, i**2, i**3)