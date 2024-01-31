# Llegir la quantitat de valors
n = int(input("Introdueix la quantitat de valors: "))

# Llegir la llista de valors de l'usuari
valors = [int(x) for x in input("Introdueix la llista de valors separats per espais: ").split()]

# Comprovar si la llista és cap i cua
if valors == valors[::-1]:
    print("cap i cua")
else:
    print("No és cap i cua")
