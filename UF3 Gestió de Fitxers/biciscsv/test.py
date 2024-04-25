import pandas as pd

# Cargar el archivo CSV del Bicing de Barcelona
bicing_data = pd.read_csv('2023_03_Marc_BicingNou_INFORMACIO.csv')

# Obtener la capacidad de la estación con más bicicletas
max_capacity_station = bicing_data.loc[bicing_data['capacity'].idxmax()]

# Obtener la capacidad de la estación con menos bicicletas
min_capacity_station = bicing_data.loc[bicing_data['capacity'].idxmin()]

# Obtener la capacidad total de la ciudad de Barcelona
total_capacity = bicing_data['capacity'].sum()

# Imprimir los resultados
print("Estación con más bicicletas:")
print(f"Estación: {max_capacity_station['station_id']} con {max_capacity_station['capacity']} bicicletas")
print("\nEstación con menos bicicletas:")
print(f"Estación: {min_capacity_station['station_id']} con {min_capacity_station['capacity']} bicicletas")
print("\nCapacidad total de la ciudad de Barcelona:")
print(f"{total_capacity} bicicletas")
