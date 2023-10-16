"""
Fer un programa que inicialitza una llista que haurà de contenir 10 números de l'1 al 10
(generats de manera aleatòria), després els ordena de menor a major, i finalment
mostri la llista ordenada de números per pantalla.

"""
import random
llista = []
for i in range(10):
    llista.append(random.randint(1, 10))
llista.sort()
print(llista)