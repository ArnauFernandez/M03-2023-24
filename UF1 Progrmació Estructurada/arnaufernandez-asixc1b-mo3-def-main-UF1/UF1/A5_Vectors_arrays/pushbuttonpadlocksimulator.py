# Inicialitzar l'estat inicial del "candau"
estat_candau = [False] * 8

# Llegir les entrades de l'usuari fins que introdueixi -1
while True:
    entrada = int(input("Introdueix el número del botó (o -1 per finalitzar): "))

    # Comprovar si s'ha introduït -1 per finalitzar
    if entrada == -1:
        break

    # Comprovar si el número del botó està dins del rang vàlid (0-7)
    if 0 <= entrada <= 7:
        # Invertir l'estat del botó (de True a False o viceversa)
        estat_candau[entrada] = not estat_candau[entrada]
    else:
        print("Número de botó no vàlid. Si us plau, introdueix un número de botó entre 0 i 7.")

# Mostrar l'estat final del "candau"
print("Estat final del candau:", estat_candau)
