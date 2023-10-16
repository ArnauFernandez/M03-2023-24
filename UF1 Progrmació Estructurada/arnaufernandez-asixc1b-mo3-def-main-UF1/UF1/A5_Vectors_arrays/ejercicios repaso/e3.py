MIDA_PARAULES = 15
paraula = input("Paraula? ")
llargadaMitjana = 0
frase = []
for i in range(MIDA_PARAULES):
    frase.append(paraula)

print(paraula)

paraulesResultat = []
paraulaLlarga = frase[0]
paraulaCurta = frase[0]
# Le pregunto a la primera palabra y sea cual sea es la mas larga porque si es la unica que tengo

for i in range(MIDA_PARAULES):
    llargadaMitjana = llargadaMitjana + len(frase[i])
    if len(frase[i]) > len(paraulaLlarga):
        paraulaLlarga = paraula[i]
    elif len(frase[i]) < len(paraulaCurta):
        paraulaCurta = frase[i]
paraulesResultat.append(paraulaLlarga)
paraulesResultat.append(paraulaCurta)
llargadaMitjana = llargadaMitjana / MIDA_PARAULES

#
print(f"MITJANA de la paraula és: {int(llargadaMitjana)}")