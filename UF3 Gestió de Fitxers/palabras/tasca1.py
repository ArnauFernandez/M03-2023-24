import os
import time

ruta_entrada = 'paraules.txt'
logdir = os.path.join('log', 'paraules.log')

def escribir_palabras_en_archivo(palabras, longitud):
    """Escribe las palabras en un archivo."""
    try:
        nombre_archivo = f"paraules-{longitud}.txt"
        with open(nombre_archivo, "w") as salida:
            for palabra in palabras:
                salida.write(palabra + "\n")
        mensaje = f"Se ha creado el archivo {nombre_archivo} satisfactoriamente."
        return mensaje
    except Exception as e:
        mensaje = f"Error al escribir en el archivo {nombre_archivo}: {e}"
        return mensaje

def procesar_palabras(lineas):
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

    for longitud, palabras in palabras_por_longitud.items():
        if palabras:
            escribir_palabras_en_archivo(palabras, longitud)

def main():
    """Función principal."""
    start_time = time.time()
    with open(logdir, "a") as archivo_log:
        archivo_log.write(f"--- Inicio del programa ---\n")
        with open(ruta_entrada, "r") as entrada:
            lineas = entrada.readlines()

        procesar_palabras(lineas)

        end_time = time.time()
        elapsed_time = end_time - start_time
        archivo_log.write(f"--- Fin del programa ---\n")
        archivo_log.write(f"Tiempo transcurrido: {elapsed_time:.2f} segundos\n")

if __name__ == "__main__":
    main()
