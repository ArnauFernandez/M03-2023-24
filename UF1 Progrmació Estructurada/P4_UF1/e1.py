"""
1. Programa que demana a l'usuari la introducció de 10 nombres sencers i ha de mostrar, 
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
cero=0
positvo=0
negativo=0
for i in range(10):
    numeros=input(int("pide diez numeros"))
if numeros ==0:
    cero=cero+1
elif numeros >0:
    positvo=positvo+1
else:
    negativo=negativo+1
print(negativo,positvo,cero)