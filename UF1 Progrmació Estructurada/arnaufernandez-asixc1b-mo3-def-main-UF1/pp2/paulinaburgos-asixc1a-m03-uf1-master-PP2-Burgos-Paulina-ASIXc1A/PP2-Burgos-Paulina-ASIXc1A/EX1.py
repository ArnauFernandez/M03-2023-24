MIDA = 8
VAR1 = " 1 "
VAR2 = " 2 "
VAR3 = " 0 "

for fila in range(MIDA):
    for columna in range(MIDA):
        if fila == columna:
            print(VAR1, end="")
        elif fila + columna == MIDA-1:
            print(VAR2, end="")
        else:
            print(VAR3, end="")
    #Siguente fila print para ir en vertical
    print()