
llista = [["Mocós", "Capsigrany", "CALÇASSES", "CAP DE SURO", "BOTIFLER", "BENEIT"],
          ["Mocoso", "Alcaudon", "CALZAS", "CABEZA DE CORCHO", "BOTIFLER", "BOBALICÓN"],
          ["Brat", "Shrike", "FOOTWEAR", "CORK HEAD", "BOTIFLER", "STUPID"],
          ["Qev", "DEGHWA", "TLHA'", "NADEV GHITLH", "CHE'WI'", "CHELWI"]]
insult = input("Insult? ")
for i in range(len(llista[0])):
    if llista[0][i] == insult:
        print(llista[1][i], llista[2][i], llista[3][i])
    elif llista[1][i] == insult:
        print(llista[0][i], llista[2][i], llista[3][i])
    elif llista[2][i] == insult:
        print(llista[0][i], llista[1][i], llista[3][i])
    elif llista[3][i] == insult:
        print(llista[0][i], llista[1][i], llista[2][i])
else:
    print("Insult no trobat")
