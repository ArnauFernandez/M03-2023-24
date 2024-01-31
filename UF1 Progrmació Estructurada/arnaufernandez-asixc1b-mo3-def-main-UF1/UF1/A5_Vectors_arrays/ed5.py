agenda = {}

while True:
    print("\nMenú:")
    print("1. Afegir/Modificar")
    print("2. Buscar")
    print("3. Esborrar")
    print("4. Llistar")
    print("5. Sortir")

    opcio = input("Escull una opció (1-5): ")

    if opcio == '1':
        nom = input("Introdueix el nom: ")
        if nom in agenda:
            print(f"El telèfon de {nom} és: {agenda[nom]}")
            modificar = input("Vols modificar el telèfon? (s/n): ")
            if modificar.lower() == 's':
                telefon = input("Introdueix el nou telèfon: ")
                agenda[nom] = telefon
                print(f"Telèfon de {nom} actualitzat amb èxit.")
        else:
            telefon = input("Introdueix el telèfon: ")
            agenda[nom] = telefon
            print(f"Contacte {nom} afegit amb èxit.")
    elif opcio == '2':
        cadena = input("Introdueix la cadena de cerca: ")
        print("Resultats de la cerca:")
        for nom, telefon in agenda.items():
            if nom.startswith(cadena):
                print(f"{nom}: {telefon}")
    elif opcio == '3':
        nom = input("Introdueix el nom a esborrar: ")
        if nom in agenda:
            confirmacio = input(f"Vols esborrar el contacte {nom}? (s/n): ")
            if confirmacio.lower() == 's':
                del agenda[nom]
                print(f"Contacte {nom} esborrat amb èxit.")
        else:
            print(f"No s'ha trobat cap contacte amb el nom {nom}.")
    elif opcio == '4':
        print("Llistat de contactes:")
        for nom, telefon in agenda.items():
            print(f"{nom}: {telefon}")
    elif opcio == '5':
        break
    else:
        print("Opció no vàlida. Si us plau, introdueix una opció vàlida (1-5).")
