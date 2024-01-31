TORRE = "♖"

# Llegir la posició de la torre
posicio = input("Introdueix la posició de la torre (per exemple, d4): ")
columna = ord(posicio[0].lower()) - ord('a')
fila = int(posicio[1]) - 1

# Inicialitzar el tauler amb valors 0
tauler_escacs = [[0 for _ in range(8)] for _ in range(8)]

# Marcar la posició actual de la torre
tauler_escacs[fila][columna] = TORRE

# Marcar les files i columnes
for i in range(len(tauler_escacs)):
    if i != fila:
        tauler_escacs[i][columna] = 1
    if i != columna:
        tauler_escacs[fila][i] = 1

# Imprimir el tauler resultat
for fila in tauler_escacs:
    print(" ".join(map(str, fila)))
