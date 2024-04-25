import pandas as pd

# Cargar el archivo CSV
bicing_data = pd.read_csv('2023_03_Marc_BicingNou_INFORMACIO.csv')

# Obtener la capacidad de la estación con más bicicletas
max_capacity_station = bicing_data.loc[bicing_data['capacity'].idxmax()]

# Obtener la capacidad de la estación con menos bicicletas
min_capacity_station = bicing_data.loc[bicing_data['capacity'].idxmin()]

# Obtener la capacidad total de la ciudad de Barcelona
total_capacity = bicing_data['capacity'].sum()

# Imprimir la información
print(f"Estación con más bicicletas: {max_capacity_station['station_id']} con {max_capacity_station['capacity']} bicicletas")
print(f"Estación con menos bicicletas: {min_capacity_station['station_id']} con {min_capacity_station['capacity']} bicicletas")
print(f"Capacidad total de la ciudad de Barcelona: {total_capacity}")
