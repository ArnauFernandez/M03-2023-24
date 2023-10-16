gener = [1, 12, 4, -5, 7, 3, 2,
         9, -6, 7, 8, 2, 14, -7,
         5, 13, 12, 4, 6, -7, 1,
         12, 4, -2, 3, 5, 2, 7,
         -2, 8, -15]
febrer = [1, 15, -5, 4, 6, 19,
          22, -1, 12, 16, 14, 17,
          18, 20, 21, 19, 14, 25,
          23, 12, 10, 17, 18, 6,
          8, 5, 12, 19]
marc = [20, 23, 21, 25, 26, 27,
        22, 24, 28, 25, 24, 19,
        14, 16, 14, 15, 20, 21,
        23, 25, 24, 25, 27, 25,
        25, 22, 21]
calendari = [gener, febrer, marc]
calendariMinima = [0, 0, 0]
calendariMaxima = [0, 0, 0]
calendariMitjana = [0, 0, 0]

for numMes in range(3):
    sortedMes = sorted(calendari[numMes], key=None, reverse=True)
    calendariMaxima[numMes] = sortedMes[0]
    calendariMinima[numMes] = sortedMes[-1]
    totalTemp = 0

    for temp in calendari[numMes]:
        totalTemp = totalTemp + temp

    tempMitjana = totalTemp / len(calendari[numMes])
    calendariMitjana[numMes] = tempMitjana

calendariMin = sorted(calendariMinima, key=None, reverse=True)
tempMinTrimestre = calendariMin[-1]
calendariMax = sorted(calendariMaxima, key=None, reverse=True)
tempMaxTrimestre = calendariMax[0]

tempMitjanaAcumulada = 0
for numMes in range(3):
    tempMitjanaAcumulada = tempMitjanaAcumulada + \
                           calendariMitjana[numMes]
tempMitjanaTrimestre = tempMitjanaAcumulada / len(calendariMitjana)


# TODO: Ja que sabem utilitzar definicions les utilitzarem :-)

def tempGener():
    print("Temp Gener")
    print(f"Min: {calendariMinima[0]}")
    print(f"Max: {calendariMaxima[0]}")
    print(f"Mitjana de Gener: {round(calendariMitjana[0], 2)}\n")


def tempFebrer():
    print("Temp Febrer")
    print(f"Min: {calendariMinima[1]}")
    print(f"Max: {calendariMaxima[1]}")
    print(f"Mitjana de Febrer: {round(calendariMitjana[1], 2)}\n")


def tempMarc():
    print("Temp Març")
    print(f"Min: {calendariMinima[2]}")
    print(f"Max: {calendariMaxima[2]}")
    print(f"Mitjana de Març: {round(calendariMitjana[2], 2)}\n")


def tempTrimestre():
    print("Temp Trimestre")
    print(f"Min: {tempMinTrimestre}")
    print(f"Max: {tempMaxTrimestre}")
    print(f"Mitjana de Gener, Febrer i Març: {round(tempMitjanaTrimestre, 2)}")


tempGener()
tempFebrer()
tempMarc()
tempTrimestre()
