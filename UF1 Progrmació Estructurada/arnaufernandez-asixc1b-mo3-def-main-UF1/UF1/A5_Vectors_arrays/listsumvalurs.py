# Llegir la llista de valors de l'usuari
valors = [int(x) for x in input("Introdueix una llista de valors separats per espais: ").split()]

# Calcular la suma dels valors
suma_valors = sum(valors)

# Imprimir la suma
print("Suma dels valors:", suma_valors)
