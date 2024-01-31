# Llegir els noms dels conductors
noms = []
num_conductors = int(input("Introdueix el nombre de conductors: "))
for i in range(num_conductors):
    nom_conductor = input(f"Introdueix el nom del conductor {i + 1}: ")
    noms.append(nom_conductor)

# Inicialitzar la taula de quilòmetres
kms = []
for i in range(num_conductors):
    kms_conductor = [int(x) for x in input(f"Introdueix els quilòmetres per al conductor {noms[i]} separats per espai: ").split()]
    kms.append(kms_conductor)

# Calcular els quilòmetres totals per cada conductor
total_kms = [sum(conductor) for conductor in kms]

# Mostrar la llista amb els noms i els quilòmetres totals
print("\nLlista de conductors i quilòmetres setmanals:")
for i in range(num_conductors):
    print(f"{noms[i]}: {total_kms[i]} kms")
