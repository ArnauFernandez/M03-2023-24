"""
posteriorment mostri en pantalla cada nombre de la llista juntament amb el seu quadrat i el seu cub.
"""

from random import randint
import random

# Inicializar la lista con 10 valores aleatorios
lista_valores = [random.randint(1, 10) for _ in range(10)]

# Mostrar en pantalla cada número de la lista con su cuadrado y su cubo
for valor in lista_valores:
    cuadrado = valor ** 2
    cubo = valor ** 3
    print(f"Número: {valor}, Cuadrado: {cuadrado}, Cubo: {cubo}")
