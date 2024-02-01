"""
Arnau Fernandez Pinar
pp3 e3 M03
1/02/2024
"""
try:
    listparaula = []
    for x in range(666):
        paraula = input("Introdueix la paraula: ")
        while paraula != "\q":
            listparaula.append(paraula)
        else:
            break
    suma_caracters = sum(len(paraula) for y in listparaula)
    longitud_mitjana = suma_caracters / len(paraula)
    paraula_mes_curta = max(paraula, key=len)
    paraula_mes_llarga = min(paraula, key=len)

    print("la longitud mitjana de la paraula es:", longitud_mitjana)
    print("la paraules mes curta es:", paraula_mes_curta)
    print("la paraula mes llarga es: ", paraula_mes_llarga)
except:
    print("error")