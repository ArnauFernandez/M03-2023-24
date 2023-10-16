"Exercici 1 Realitzar un programa que inicialitza una llista amb 10 valors aleatoris (de l'1 al 10) i posteriorment mostri en pantalla cada nombre de la llista juntament amb el seu quadrat i el seu cub."
import random
listanum=[]
listasqr=[]
listacub=[]
aleatori=0
for i in range(10):
        aleatori=random.randint(1, 10)
        listanum.append(aleatori)
        cuadrado=aleatori**2
        listasqr.append(cuadrado)
        cubo=aleatori**3
        listacub.append(cubo)
print(listanum)
print(listasqr)
print(listacub)