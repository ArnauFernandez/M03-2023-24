def leer_archivo(ruta_archivo):
    """Lee un archivo y devuelve una lista de líneas."""
    try:
        with open(ruta_archivo, "r") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return []

def contar_vocales(palabra):
    """Cuenta la cantidad de vocales en una palabra."""
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

def agregar_cantidad_vocales(lineas):
    """Agrega la cantidad de vocales al inicio de cada línea."""
    lineas_con_vocales = []
    for linea in lineas:
        # Eliminar los espacios en blanco al principio y al final de la línea
        palabra = linea.strip()
        # Contar la cantidad de vocales en la palabra
        cantidad_vocales = contar_vocales(palabra)
        # Crear la nueva línea con el formato especificado
        nueva_linea = f"{cantidad_vocales}\t{palabra}\n"
        lineas_con_vocales.append(nueva_linea)
    return lineas_con_vocales

def escribir_archivo(ruta_archivo, lineas):
    """Escribe las líneas en un archivo."""
    try:
        with open(ruta_archivo, "w") as archivo:
            archivo.writelines(lineas)
        print(f"Se ha creado el archivo {ruta_archivo} satisfactoriamente.")
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_archivo}: {e}")

def maint2():
    """Función principal."""
    # Leer el archivo original
    ruta_archivo_original = "paraules.txt"
    lineas = leer_archivo(ruta_archivo_original)
    if not lineas:
        print("No se puede continuar sin datos.")
        return

    # Agregar la cantidad de vocales a cada palabra
    lineas_con_vocales = agregar_cantidad_vocales(lineas)

    # Escribir las líneas en el nuevo archivo
    ruta_archivo_nuevo = "paraulesQuantitatVocals.txt"
    escribir_archivo(ruta_archivo_nuevo, lineas_con_vocales)

if __name__ == "__main__":
    maint2()
