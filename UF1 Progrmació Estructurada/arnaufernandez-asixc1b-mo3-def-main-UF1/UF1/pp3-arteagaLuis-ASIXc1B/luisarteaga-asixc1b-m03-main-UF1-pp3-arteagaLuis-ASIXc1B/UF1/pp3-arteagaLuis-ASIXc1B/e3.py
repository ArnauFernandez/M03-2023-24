"""
            Luis Arteaga
            M03-Programació
            UF1
            24/1/2023
            Mida de les Paraules
            Descripció:
            Implementar un programa que faci les seguents operacions:
            Crear una llista per emmmagazemar 15 paraules.
            Mostra tot el seu contingut.
            Omplir-la, pel teclat, amb paraules. NO cal omplir-la del tot.
            Calcular la llargada mitjana de les paraules introduïdes i mostrar-la per pantalla.
            Copiar a una llista, totes les paraules, de llargada diferent de la llargada mitjana
            Mostra la llista amb les paraules, de llargada diferent de la llargada mitjana.
"""
listparaula = []
for x in range(15):
    paraula = input("Introdueix la paraula: ")
    listparaula.append(paraula)
suma_caracters = sum(len(paraula) for y in listparaula)
longitud_mitjana = suma_caracters / len(paraula)
paraula_mes_curta = max(paraula, key=len)
paraula_mes_llarga = min(paraula, key=len)

print("la longitud mitjana de la paraula es:", longitud_mitjana)
print("la paraules mes curta es:", paraula_mes_curta)
print("la paraula mes llarga es: ", paraula_mes_llarga)