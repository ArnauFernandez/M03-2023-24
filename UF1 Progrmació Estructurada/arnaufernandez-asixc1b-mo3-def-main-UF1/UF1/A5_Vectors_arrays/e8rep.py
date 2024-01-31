# Inicializar listas para almacenar nombres y edades
nombres = []
edades = []

# Proceso de lectura de datos
while True:
    nombre = input("Introdueix el nom de l'alumne (o '*' per acabar): ")

    # Comprobar si se ha introducido un asterisco para salir del bucle
    if nombre == '*':
        break

    edad = int(input(f"Introdueix l'edat de {nombre}: "))

    # Añadir nombres y edades a las respectivas listas
    nombres.append(nombre)
    edades.append(edad)

# Mostrar los alumnos mayores de edad
print("\nAlumnes majors d'edat:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"{nombres[i]} - {edades[i]} anys")

# Obtener la edad máxima
edad_maxima = max(edades)

# Mostrar los alumnos más viejos
print("\nAlumnes més vells:")
for i in range(len(nombres)):
    if edades[i] == edad_maxima:
        print(f"{nombres[i]} - {edades[i]} anys")
