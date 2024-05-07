import os


def llegir_fitxer(ruta):
    dades_partit = []
    with open(ruta, 'r') as fitxer:
        linies = fitxer.readlines()
        equip1 = linies[0].strip()
        equip2 = linies[1].strip()
        dades_partit.append((equip1, equip2))
        for linia in linies[2:]:
            accio = linia.strip().split()
            dades_partit.append((int(accio[0]), int(accio[1])))
    return dades_partit


def analitzar_partit(dades_partit):
    punts_equip1 = 0
    punts_equip2 = 0
    resultat_accions = []
    for accio in dades_partit[1:]:
        if accio[0] == 1:
            resultat_accions.append("Cistella de " + dades_partit[0][0])
            punts_equip1 += 2
        elif accio[0] == 2:
            resultat_accions.append("Triple de " + dades_partit[0][0])
            punts_equip1 += 3
        elif accio[0] == 3:
            resultat_accions.append("Tir lliure de " + dades_partit[0][0])
            punts_equip1 += 1

        if accio[1] == 1:
            resultat_accions.append("Cistella de " + dades_partit[0][1])
            punts_equip2 += 2
        elif accio[1] == 2:
            resultat_accions.append("Triple de " + dades_partit[0][1])
            punts_equip2 += 3
        elif accio[1] == 3:
            resultat_accions.append("Tir lliure de " + dades_partit[0][1])
            punts_equip2 += 1

    if punts_equip1 > punts_equip2:
        resultat_accions.append("Guanya " + dades_partit[0][0])
    elif punts_equip1 < punts_equip2:
        resultat_accions.append("Guanya " + dades_partit[0][1])
    else:
        resultat_accions.append("Empat")

    return resultat_accions


def main():
    ruta_fitxer = input("Introdueix la ruta del fitxer: ")
    if not os.path.isfile(ruta_fitxer):
        print("El fitxer no existeix.")
        return

    dades_partit = llegir_fitxer(ruta_fitxer)
    resultat = analitzar_partit(dades_partit)
    for accio in resultat:
        print(accio)


if __name__ == "__main__":
    main()
