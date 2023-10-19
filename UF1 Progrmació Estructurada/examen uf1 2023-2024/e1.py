"""
Arnau Fernandez Pinar
ASIXc M03 UF1 PP1
19/10/2023
Exercici 1: e1.py
S'ha creat un nou embàs, esfèric, per emmagatzemar líquids, com ara aigua, llet, o qualsevol refresc.
Ens demanen, crear un programa que mostri per pantalla, l’àrea i el volum, d’una esfera on el radi es llegeix del teclat.
Les fórmules són V=4/3π*r3 i A=4*π*r2  on el valor de π és 3.141592.
"""
import math
radi=float(input("Dame un valor para el radio: "))
diametreArea=radi**2
diametreVolum=radi**3
area=4*math.pi*diametreArea
volum=4/3*math.pi*diametreVolum
print("L'Àrea del cercle es de ",area," i el volum de: ",volum)