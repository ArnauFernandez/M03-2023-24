# Santoral del mes de gener
santoral_gener = {
    1: ["Santa Maria", "Solemnitat de l'Any Nou"],
    2: ["Sant Basili Magne", "Santa Genoveva", "Santa Adelaida"],
    3: ["Sant Gèmin", "Sant Genis", "Sant José"],
    4: ["Sant Enric de Settle", "Sant Teodoric de Canterbury", "Sant Rigobert"],
    5: ["Sant Josemaría Escrivá", "Sant Apol·lònia", "Santa Simeona"],
    6: ["Sant Gaspar del Bufalo", "Santa Melani", "Sant Wilbrod"],
    7: ["Sant Ramon de Peñafort", "Santa Luciana", "Sant Aldric"],
    8: ["Santa Isabel d'Hongria", "Santa Julia de Mèrida", "Santa Maria"],
    9: ["Sant Marc d'Efes", "Sant Felano", "Santa Marciana", "San Honorato"],
    # ... Pots continuar afegint sants per cada dia
}

# Demanar el nom de l'usuari
nom_usuari = input("Introdueix el teu nom: ")

# Comprovar si el sant de l'usuari està al santoral de gener
for dia, sants in santoral_gener.items():
    if nom_usuari in sants:
        print(f"{nom_usuari}, el teu sant és el dia {dia} de gener.")
        break
else:
    print(f"{nom_usuari}, el teu sant no està al santoral de gener.")
