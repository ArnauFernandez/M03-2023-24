# Llegir la paraula i la posició de l'usuari
paraula = input("Introdueix una paraula: ")
posicio = int(input("Introdueix la posició: "))

# Comprovar si la posició és vàlida
if 0 <= posicio < len(paraula):
    # Accedir a la lletra a la posició indicada
    lletra = paraula[posicio]
    print(f"Lletra a la posició {posicio}: {lletra}")
else:
    print("Posició no vàlida. Si us plau, introdueix una posició vàlida.")
