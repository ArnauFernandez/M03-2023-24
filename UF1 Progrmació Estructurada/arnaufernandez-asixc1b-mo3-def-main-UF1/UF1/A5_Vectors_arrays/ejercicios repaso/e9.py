"""
Volem guardar la temperatura mínima i màxima de 5 dies i tot seguit processar aquesta
informació. Per fer-ho, realitza un programa que faci el següent:
● Demanar la temperatura mínima i màxima de cadascun dels 5 dies
● Mostrar a continuació la temperatura mitjana de cada dia
● Després, mostri els dies amb menys temperatura
● Finalment, demani una temperatura per teclat i a continuació mostri els dies la
temperatura màxima dels quals coincideix amb ella. Si no hi ha cap dia que
coincideixi amb alguna de les temperatures màximes, cal mostrar un missatge
d'error.
Nota: per desar la temperatura màxima i mínima de cada dia, se suggereix utilitzar una
llista que contindrà la informació per als 5 dies on cada element de la llista serà una
llista de 2 elements: la temperatura mínima i la temperatura màxima.

"""
dades_temperatura = []

for i in range(5):
    min_temp = float(input(f"Introdueix la temperatura mínima del dia {i+1}: "))
    max_temp = float(input(f"Introdueix la temperatura màxima del dia {i+1}: "))
    dades_temperatura.append([min_temp, max_temp])

# Temperatura mitjana de cada dia
for i, (min_temp, max_temp) in enumerate(dades_temperatura):
    mitjana = (min_temp + max_temp) / 2
    print(f"La temperatura mitjana del dia {i+1} és {mitjana}")

# Dies amb menys temperatura
menys_temperatura = min(dades_temperatura, key=lambda x: x[1]-x[0])
print("Dies amb menys temperatura: ",menys_temperatura)

# Dies amb la temperatura màxima introduida
temp_buscada = float(input("Introdueix una temperatura per buscar: "))
dies_amb_temperatura = [i+1 for i, (min_temp, max_temp) in enumerate(dades_temperatura) if max_temp == temp_buscada]
if dies_amb_temperatura:
    print("Dies amb la temperatura màxima introduida:", dies_amb_temperatura)
else:
    print("No hi ha cap dia amb aquesta temperatura màxima.")

