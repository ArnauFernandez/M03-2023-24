"""
Arnau Fernández Pinar
Matteo Vilchez
e2. Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9.
(ambdós inclosos)
28/11/2023
"""
num = int(input("Introduce un número entre 2 y 9: "))
if num >= 2 and num <= 9:
    print(1)
    for i in range(2, num):
        print(i,end=" ")
        print(" "*(i-2),end="")
        print(i)
    else: print(str(i+1)*(1+i))
else:
    print("El número debe estar entre 2 y 9")