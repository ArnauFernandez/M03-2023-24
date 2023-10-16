WHITE = "   "
BLACK = "███"
MARK = "***"

TABLE_SIZE = int(input("Tablero tamaño"))
PUNTOX = int(input("Punto X"))
PUNTOY = int(input("Punto Y"))

for x in range(TABLE_SIZE):
    for y in range(TABLE_SIZE):
        if x == PUNTOX and y == PUNTOY:
            print(MARK, end="")
        else:
            print(WHITE if y % 2 == x % 2 else BLACK, end="")
    print()