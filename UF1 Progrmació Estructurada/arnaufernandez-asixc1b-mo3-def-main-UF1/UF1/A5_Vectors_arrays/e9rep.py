# Inicializar una lista para almacenar la información de temperatura de cada día
temperatures = []

# Solicitar la temperatura mínima y máxima de cada uno de los 5 días
for dia in range(1, 6):
    temp_min = float(input(f"Introdueix la temperatura mínima del dia {dia}: "))
    temp_max = float(input(f"Introdueix la temperatura màxima del dia {dia}: "))
    temperatures.append([temp_min, temp_max])

# Calcular la temperatura promedio de cada día y mostrarla
print("\nTemperatura mitjana de cada dia:")
for i, temp in enumerate(temperatures, start=1):
    temp_promedio = (temp[0] + temp[1]) / 2
    print(f"Dia {i}: {temp_promedio} graus Celsius")

# Encontrar los días con la menor temperatura
min_temperatura = min(min(temp) for temp in temperatures)
dies_menor_temperatura = [i+1 for i, temp in enumerate(temperatures) if min(temp) == min_temperatura]

print(f"\nDies amb menys temperatura: {dies_menor_temperatura}")

# Solicitar una temperatura al usuario
temperatura_buscar = float(input("\nIntrodueix una temperatura per trobar els dies amb la temperatura màxima coincident: "))

# Mostrar los días con la temperatura
