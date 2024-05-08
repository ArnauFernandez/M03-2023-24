import os
logdir = os.path.join('log', 'paraules.log')
def leer_archivo(ruta_archivo, archivo_log):
    """Lee un archivo y devuelve una lista de líneas."""
    try:
        with open(ruta_archivo, "r") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        mensaje = f"El archivo {ruta_archivo} no se encontró."
        archivo_log.write(mensaje + "\n")
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

def escribir_archivo(ruta_archivo, lineas, archivo_log):
    """Escribe las líneas en un archivo."""
    try:
        with open(ruta_archivo, "w") as archivo:
            archivo.writelines(lineas)
        mensaje = f"Se ha creado el archivo {ruta_archivo} satisfactoriamente."
        archivo_log.write(mensaje + "\n")
    except Exception as e:
        mensaje = f"Error al escribir en el archivo {ruta_archivo}: {e}"
        print(mensaje)
        archivo_log.write(mensaje + "\n")

def maint2():
    """Función principal."""
    # Archivo de registro
    ruta_archivo_log = logdir
    with open(ruta_archivo_log, "a") as archivo_log:
        archivo_log.write("Registro de eventos:\n")

        # Leer el archivo original
        ruta_archivo_original = "paraules.txt"
        lineas = leer_archivo(ruta_archivo_original, archivo_log)
        if not lineas:
            mensaje = "No se puede continuar sin datos."
            archivo_log.write(mensaje + "\n")
            return

        # Agregar la cantidad de vocales a cada palabra
        lineas_con_vocales = agregar_cantidad_vocales(lineas)

        # Escribir las líneas en el nuevo archivo
        ruta_archivo_nuevo = "paraulesQuantitatVocals.txt"
        escribir_archivo(ruta_archivo_nuevo, lineas_con_vocales, archivo_log)

if __name__ == "__main__":
    maint2()
