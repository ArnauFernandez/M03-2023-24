FUSTA = "🟫"
ASTERISC = "🟫"

try:
    # Solicita la cantidad de columnas y filas al usuario
    columnes = int(input("Introdueix la quantitat de columnes: "))
    files = int(input("Introdueix la quantitat de files: "))

    # Comprueba si los valores introducidos tienen sentido
    if columnes <= 0 or files <= 0:
        raise ValueError("Els nombres han de ser majors que zero.")

    # Imprime la caja vacía
    for i in range(files):
        if i == 0 or i == files - 1:
            # Imprime la primera y la última fila con asteriscos o madera
            print(f'{ASTERISC} ' * columnes)
        else:
            # Imprime las filas intermedias con asteriscos o madera en los extremos
            print(f'{ASTERISC}{" " * (2 * columnes - 3)} {ASTERISC}' if columnes > 1 else ASTERISC)

except ValueError as e:
    print(f"Error: {e}")
