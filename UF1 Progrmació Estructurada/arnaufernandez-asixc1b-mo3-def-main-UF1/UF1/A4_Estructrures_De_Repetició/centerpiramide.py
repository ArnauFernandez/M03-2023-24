"""
Arnau Fernandez Pinar
M04 UF1 A4
ASIXc
piramide.py
"""

"""SIMBOLO="🧱"
CONT=0
ESPACIO=" "
cantidad=int(input(""))
for x in range(cantidad):
    ESPACIO=ESPACIO*cantidad
    CONT=CONT+1
    if CONT>=1:
        print (""*(cantidad-x),SIMBOLO*1)
print(" ")
"""
from time import sleep

ARBOL="🧱"
mida = int(input())
for i in range(1, mida+1):
    print(" "*(mida- i),ARBOL*i)
    sleep(0.2)