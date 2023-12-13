try:
    # Solicita la base y el exponente al usuario
    base = int(input("Introdueix la base: "))
    exponent = int(input("Introdueix l'exponent: "))

    # Calcula la potencia sin usar la biblioteca math
    resultat = 1
    for _ in range(abs(exponent)):
        resultat *= base if exponent > 0 else 1 / base

    # Imprime el resultado
    print(f"Resultat: {resultat}")

except ValueError:
    print("Si us plau, introdueix dos nombres enters.")
