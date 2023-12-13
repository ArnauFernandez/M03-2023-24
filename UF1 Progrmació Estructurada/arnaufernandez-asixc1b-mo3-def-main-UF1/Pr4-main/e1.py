"""
Arnau Fernández Pinar
Matteo Vilchez
e1. Programa que demana a l'usuari la introducció de 10 nombres sencers (que també podrien ser 10000000 😱😳😈) i ha de mostrar,
al final i per pantalla, quants són positius,
quants negatius i quants zero.
28/11/2023
"""
ceros=0
positivo=0
negativo=0
for i in range(10):
    num=int(input())
    if num >0:
        positivo=positivo+1
    elif num ==0:
        ceros=ceros+1
    else:
        negativo=negativo+1
print("tienes",positivo,"positivos","tienes",negativo,"negativos","tienes",ceros,"ceros")