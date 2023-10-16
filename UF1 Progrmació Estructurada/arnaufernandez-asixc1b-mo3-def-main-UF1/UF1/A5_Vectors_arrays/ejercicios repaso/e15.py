"""
Crear un programa per gestionar els resultats de la travessa de futbol. Per això
utilitzarem dues taules:
● Equips: Que és una taula de cadenes on guardem a cada columna el nom dels
equips de cada partit. A la travessa s'indiquen 15 partits.
● Resultats: És una taula d'enters on s'indica el resultat. També té dues columnes,
a la primera es guarda el nombre de gols de l'equip que està guardat a la primera
columna de la taula anterior, i a la segona els gols de l'altre equip.
El programa anirà demanant els noms dels equips de cada partit i el resultat del partit,
tot seguit s'imprimeix la travessa d'aquesta jornada.
Quina modificació caldria fer a les taules per guardar tots els resultats de totes les
jornades de la temporada?
"""
equips = []
resultats = []
for i in range(15):
    equips.append([])
    resultats.append([])
    for j in range(2):
        equips[i].append(input("Introdueix el nom de l'equip: "))
        resultats[i].append(int(input("Introdueix el resultat: ")))
for i in range(15):
    print("{} {} - {} {}".format(equips[i][0], resultats[i][0], resultats[i][1], equips[i][1]))