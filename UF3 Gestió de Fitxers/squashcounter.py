def marcador_set(partit):
    marcador_a = 0
    marcador_b = 0
    resultat_sets = []

    for punt in partit:
        if punt == 'A':
            marcador_a += 1
        elif punt == 'B':
            marcador_b += 1

        if (marcador_a >= 9 or marcador_b >= 9) and abs(marcador_a - marcador_b) >= 2:
            resultat_sets.append(f"{marcador_a}-{marcador_b}")
            marcador_a = 0
            marcador_b = 0

    if marcador_a == 0 and marcador_b == 0:
        resultat_sets.append("0-0")
    else:
        resultat_sets.append(f"{marcador_a}-{marcador_b}")

    return resultat_sets

def main():
    num_partits = int(input("Introdueix el nombre de partits: "))
    resultats_finals = []

    for _ in range(num_partits):
        hist_partit = input("Introdueix la història del partit (finalitza amb 'F'): ")
        resultat_set = marcador_set(hist_partit)
        resultats_finals.append(resultat_set)

    for resultat_set in resultats_finals:
        print(" ".join(resultat_set))

if __name__ == "__main__":
    main()
