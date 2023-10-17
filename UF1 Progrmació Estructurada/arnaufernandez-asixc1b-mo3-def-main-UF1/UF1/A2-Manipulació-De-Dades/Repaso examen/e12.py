"""
Exercici 12
Implementa un programa que demani per teclat dos punts del pla i tot seguit calculi i mostri la distància entre ells.
Notes:
Un punt del pla es representa amb un parell de números. Per exemple, el punt A es representarà pels números x1 i y1, i el punt B pels números x2 i y2
La fórmula de la distància entre dos punts A i B és
distància(A,B) = √( (x2 - x1)2 + (y2 - y1)2)
"""
import math
x1=int(input("Dame un valor para la coordenanda: "))
x2=int(input("Dame un valor para la coordenanda: "))
y1=int(input("Dame un valor para la coordenanda: "))
y2=int(input("Dame un valor para la coordenanda: "))
distancia=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("la distancia entre los puntos es ",round(distancia,2))