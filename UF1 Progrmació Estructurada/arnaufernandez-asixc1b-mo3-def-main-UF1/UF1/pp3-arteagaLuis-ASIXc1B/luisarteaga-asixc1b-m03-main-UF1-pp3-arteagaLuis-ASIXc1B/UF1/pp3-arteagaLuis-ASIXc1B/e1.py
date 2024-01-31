"""
            Luis Arteaga
            M03-Programació
            UF1
            24/1/2023
            Vores de la matriu
            Descripció:
            Demanar, a l'ususari, la quantitat de files i columnes d'una matriu 2D.
            Comprovar que la matriu sigui quadrada, és a dir que tingui les mateixes fileres que columnes.
            Omplir la matriu amb 1's ales vores i la resta amb 0's.
            S'enten per vores de la matriu la primera i l'ultima filera i la primera i última columna.
            Guardar la matriu a una variable anomenda "matriu".
            Mostrar la matriu resultant per pantalla.
"""
nom_files = (int(input("Quantes files te el quadrat: ")))
quadrat = nom_files
for x in range(quadrat):
    for y in range(quadrat):
        if x == 0 or x == quadrat - 1 or y == 0 or y == quadrat - 1 :
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
