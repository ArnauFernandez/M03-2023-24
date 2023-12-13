# Define los emojis
TRONC = "🏾"  # o TRONC = "🪵" si prefieres
FULLA = "🍁"
ARBRE = "🎄"
BOLA = "🔴"
ESTEL = "🔸"

# Solicita la altura del árbol al usuario
try:
    mida_arbre = int(input("Introdueix la mida de l'arbre: "))

    # Dibuja las ramas del árbol
    for i in range(1, mida_arbre + 1):
        espais = " " * (mida_arbre - i)
        fullas = FULLA * (2 * i - 1)
        print(espais + fullas)

    # Dibuja el tronco del árbol
    for _ in range(mida_arbre // 2):
        espai_tronc = " " * (mida_arbre - 1)
        print(espai_tronc + TRONC)

    # Dibuja las decoraciones en el tronco (bolas y estrella)
    espai_decoracio = " " * (mida_arbre - 1)
    print(espai_decoracio + BOLA)
    print(espai_decoracio + ESTEL)

except ValueError:
    print("Si us plau, introdueix un nombre enter.")
