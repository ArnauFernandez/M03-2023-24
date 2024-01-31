# Declarar el diccionario para almacenar nombres y notas
diccionario_alumnos = {}

# Pedir el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos: "))

# Bucle para introducir nombres y notas
for _ in range(num_alumnos):
    nombre_alumno = input("Introduce el nombre del alumno: ")

    # Validar si el nombre del alumno ya existe
    if nombre_alumno in diccionario_alumnos:
        print("Error: Este nombre ya existe. Introduce otro nombre.")
        continue

    # Inicializar la lista de notas para el alumno
    notas_alumno = []

    # Bucle para introducir notas hasta ingresar un número negativo
    while True:
        nota = float(input(f"Introduce la nota para {nombre_alumno} (introduce un número negativo para finalizar): "))

        if nota < 0:
            break

        notas_alumno.append(nota)

    # Almacenar el nombre y las notas en el diccionario
    diccionario_alumnos[nombre_alumno] = notas_alumno

# Mostrar la lista de alumnos y la nota media obtenida por cada uno
print("\nLista de alumnos y nota media:")
for nombre, notas in diccionario_alumnos.items():
    nota_media = sum(notas) / len(notas) if len(notas) > 0 else 0
    print(f"{nombre}: {notas}, Nota Media: {nota_media:.2f}")
