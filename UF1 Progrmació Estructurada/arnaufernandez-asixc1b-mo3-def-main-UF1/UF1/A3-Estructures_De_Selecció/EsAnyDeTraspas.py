"""
Arnau Fernandez Pinar
ASIXc M03 UF1 RA1
EsAnyDeTraspas
Com segurament sabràs, a causa d'algunes raons astronòmiques, l'any poden ser de traspàs o comú. Els primers tenen una durada de 366 dies, mentre que els últims tenen una durada de 365 dies.
Des de la introducció del calendari gregorià (en 1582), s'utilitza la següent regla per a determinar el tipus d'any:
Si el número de l'any no és divisible entre quatre, és un any comú.
En cas contrari, si el número de l'any no és divisible entre 100, és un any de traspàs.
En cas contrari, si el número de l'any no és divisible entre 400, és un any comú.
En cas contrari, és un any de traspàs.
El programa ha de mostrar un dels dos missatges possibles, que són Any de traspàs o Any comú, segons el valor ingressat. (Només llegir el número d'any, per facilitar l'algoritme)
Si la data és anterior a "Gregori", ha de mostrar la frase Data anterior a Gregori
"""
año=int(input("Introduce un año"))
if not año % 4== 0:
    print("Año común")
elif not año % 100 == 0:
    print("Año visiesto")
elif not año %400==0:
    print("Año común")
else:
    print("Año Visiesto")

elif año >= 1582:
    print("Anterior a Gregori")