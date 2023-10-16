"""

Exercici 2
Crea una llista i inicialitza-la amb 5 cadenes
de caràcters llegides per teclat. Copia els
elements de la llista a una altra llista però
en ordre invers, i mostra els elements d'aquesta
 segona llista per pantalla.
"""

llista = []
llista2 = []
for i in range(5):
    llista.append(input("Introduce un texto "))
for i in range(5):
    llista2.append(llista[4-i])
for i in llista2:
    print(i)