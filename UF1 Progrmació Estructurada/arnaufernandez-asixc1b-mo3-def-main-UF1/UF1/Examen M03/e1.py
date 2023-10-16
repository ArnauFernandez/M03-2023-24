"""
Arnau Fernandez Pinar
ASIXc Mo3 UF1
Excercici 1
Hem de travessar un camp d'un extrem (superior-esquerre) a un altre (inferior-dret) i volem saber quanta distància haurem de recórrer. Només tenim la informació de l'amplada i l'alçada. 
Ens demanen, crear un programa que mostra la llargada que fa la diagonal, d’un extrem a l’altre. Cal demanar per teclat, a l'usuari l'amplada i l'alçada d'un camp, per poder fer els càlculs.
"""
import math
largo=int(input("Introduce el valor de la distancia "))
ancho=int(input("Introduce el valor de la anchura "))
diagonal=math.sqrt(largo**2+ancho**2)
print("La diagonal tiene un distancia de",diagonal,"metros cuadrados")