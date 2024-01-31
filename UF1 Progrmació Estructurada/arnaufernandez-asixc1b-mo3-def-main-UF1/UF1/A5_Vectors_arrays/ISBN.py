# Input
codi_isbn = input("Introdueix els 10 dígits del codi ISBN separats per espais: ").split()

# Convertir la llista de dígits a una cadena
codi_isbn_str = ''.join(codi_isbn)

# Verificació del codi ISBN
if len(codi_isbn_str) == 10:
    suma = 0
    for i in range(9):
        suma += int(codi_isbn_str[i]) * (i + 1)

    residu = suma % 11
    control = int(codi_isbn_str[-1])

    if residu == control or (residu == 10 and codi_isbn_str[-1] == 'X'):
        resultat = True
    else:
        resultat = False

    # Output
    print(resultat)
else:
    print("La longitud del codi ISBN ha de ser 10.")
