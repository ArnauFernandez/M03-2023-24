from collections import Counter

# Llegir la cadena de l'usuari
cadena = input("Introdueix una cadena: ")

# Comptar les ocurrències de cada caràcter amb distinció de majúscules/minúscules i accents/dièresis
contador_caracters = Counter(cadena)

# Mostrar el diccionari generat
print("Diccionari generat:")
for caracter, ocurrències in contador_caracters.items():
    print(f"{{{caracter}:{ocurrències}}}", end=", ")
print()
