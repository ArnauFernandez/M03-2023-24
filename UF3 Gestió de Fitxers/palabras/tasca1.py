import os
def escribir_palabras_en_archivo(palabras, longitud):
    """Escribe las palabras en un archivo."""
    try:
        nombre_archivo = f"paraules-{longitud}.txt"
        with open(nombre_archivo, "w") as salida:
            for palabra in palabras:
                salida.write(palabra + "\n")
        mensaje = f"Se ha creado el archivo {nombre_archivo} satisfactoriamente."
        print(mensaje)
        return mensaje
    except Exception as e:
        mensaje = f"Error al escribir en el archivo {nombre_archivo}: {e}"
        print(mensaje)
        return mensaje

def procesar_palabras(lineas, archivo_log):
    """Procesa las palabras y las escribe en archivos según su longitud."""
    palabras_por_longitud = {
        2: [],
        4: [],
        6: [],
        8: [],
        10: []
    }

    for linea in lineas:
        palabra = linea.strip()
        longitud = len(palabra)
        if longitud in palabras_por_longitud:
            palabras_por_longitud[longitud].append(palabra)

    registro = []
    for longitud, palabras in palabras_por_longitud.items():
        if palabras:
            mensaje = escribir_palabras_en_archivo(palabras, longitud)
            registro.append(mensaje)

    if registro:
        archivo_log.write("\n".join(registro) + "\n")
        print("Se ha actualizado el archivo de registro.")

def maint1():
    """Función principal."""
    with open("paraules.txt", "r") as entrada:
        lineas = entrada.readlines()

    with open("registro.log", "a") as archivo_log:
        archivo_log.write("Registro de eventos:\n")
        procesar_palabras(lineas, archivo_log)

if __name__ == "__main__":
    maint1()
