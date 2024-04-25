import xml.etree.ElementTree as ET

# Parsear el archivo XML
tree = ET.parse('localidad_17202.xml')
root = tree.getroot()

# Encontrar el elemento <dia> más reciente para obtener la probabilidad de precipitación
ultimo_dia = root.find('.//dia[last()]')

# Encontrar el elemento <prob_precipitacion> dentro del último día
prob_precipitacion = ultimo_dia.find('prob_precipitacion')

# Obtener la probabilidad de precipitación del último día
probabilidad_precipitacion = float(prob_precipitacion.text) if prob_precipitacion is not None else None

# Encontrar el elemento <temperatura> dentro del último día
temperatura = ultimo_dia.find('temperatura')

# Obtener la temperatura media del último día
temperatura_maxima = float(temperatura.find('maxima').text)
temperatura_minima = float(temperatura.find('minima').text)
temperatura_media = (temperatura_maxima + temperatura_minima) / 2

# Mostrar los resultados por pantalla
print(f'Probabilidad de precipitación: {probabilidad_precipitacion}%')
print(f'Temperatura media: {temperatura_media}°C')
