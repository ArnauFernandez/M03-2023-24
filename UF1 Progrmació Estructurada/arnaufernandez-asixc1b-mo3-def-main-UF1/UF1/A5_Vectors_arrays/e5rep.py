lista = []
import random
from random import randint
for i in range(10):
    aleatorio=random.randint(1, 10)
    lista.append(aleatorio)
    lista.sort()
print(lista)