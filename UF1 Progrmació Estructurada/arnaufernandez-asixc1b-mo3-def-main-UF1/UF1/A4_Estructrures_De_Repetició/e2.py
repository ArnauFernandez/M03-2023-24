"""Crea una aplicació que permet endevinar un número. L'aplicació genera un nombre “aleatori” de l'1 al 100. A continuació, l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o més petit que el que ha introduït, a més dels intents que et queden (tens 10 intents per encertar-lo). El programa acaba quan s'encerta el número (a més et diu quants intents has necessitat per encertar-lo), si s'arriba al límit d'intents, l’aplicació et mostra el número que havia generat."""
import random
randomNum=random.randrange(1,101)
vidas=10
i=0
for i in range(10):
    intento=int(input("dime un número"))
    if intento==randomNum:
        print("Acertaste")
        break
    else:
        vidas=vidas-1
        if intento<randomNum:
            print("el valor es mas grande")
            print("tienes ",vidas, " vidas")
        else:
            print("es mas pequeño")
            print("tienes ",vidas, " vidas")
    if i==9:
        print("fallaste")