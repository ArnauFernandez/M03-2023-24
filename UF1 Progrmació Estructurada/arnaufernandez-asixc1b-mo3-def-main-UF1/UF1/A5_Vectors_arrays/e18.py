# Funció per comptar quantes vegades apareix una cadena a la llista
def comptar(cadena, llista):
    return llista.count(cadena)

# Funció per substituir una cadena per una altra a la llista
def modificar(cadena_antiga, cadena_nova, llista):
    return [cadena_nova if x == cadena_antiga else x for x in llista]

# Funció per eliminar una cadena de la llista
def suprimir(cadena, llista):
    return [x for x in llista if x != cadena]

# Funció per mostrar les cadenes de la llista
def mostrar(llista):
    print("Llista de cadenes:")
    for cadena in llista:
        print(cadena)

# Crear una llista de cadenes
llista_cadenes = []

# Menú d'opcions
while True:
    print("\nMenú d'opcions:")
    print("1. Comptar una cadena")
    print("2. Modificar cadenes")
    print("3. Suprimir una cadena")
    print("4. Mostrar les cadenes")
    print("5. Sortir")

    opcio = input("Selecciona una opció (1-5): ")

    if opcio == "1":
        cadena_comptar = input("Introdueix la cadena a comptar: ")
        vegades = comptar(cadena_comptar, llista_cadenes)
        print(f"Aquesta cadena apareix {vegades} vegades a la llista.")

    elif opcio == "2":
        cadena_antiga = input("Introdueix la cadena a substituir: ")
        cadena_nova = input("Introdueix la nova cadena: ")
        llista_cadenes = modificar(cadena_antiga, cadena_nova, llista_cadenes)
        print("Cadenes modificades amb èxit.")

    elif opcio == "3":
        cadena_suprimir = input("Introdueix la cadena a suprimir: ")
        llista_cadenes = suprimir(cadena_suprimir, llista_cadenes)
        print("Cadena suprimida amb èxit.")

    elif opcio == "4":
        mostrar(llista_cadenes)

    elif opcio == "5":
        print("Programa finalitzat.")
        break

    else:
        print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")
