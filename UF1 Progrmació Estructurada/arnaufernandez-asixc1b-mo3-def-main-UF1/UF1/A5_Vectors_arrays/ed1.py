# Llegir el número de l'usuari
numero = int(input("Introdueix un número: "))

# Crear el diccionari amb les claus i els quadrats
diccionari_quadrats = {i: i**2 for i in range(1, numero + 1)}

# Mostrar el diccionari generat
print("Diccionari generat:")
print(diccionari_quadrats)
