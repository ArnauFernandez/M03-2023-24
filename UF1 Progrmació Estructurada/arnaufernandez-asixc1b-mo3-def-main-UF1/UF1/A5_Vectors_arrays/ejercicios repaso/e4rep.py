"""
Programa que declara una llista i la va omplint de números fins que introduïm un
nombre negatiu (el qual no afegirem) Un cop fet això, cal mostrar en pantalla tots els
nombres de la llista.
"""
llista = []
num = 0
while num >= 0:
    num = int(input("Introdueix un número: "))
    if num >= 0:
        llista.append(num)
print("Els números introduïts són: ", llista)
