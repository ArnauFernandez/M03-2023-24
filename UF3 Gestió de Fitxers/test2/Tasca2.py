"""
Joel Joan
02/05/2023
Prova practica 1

Crear una còpia del fitxer paraules.txt tot afegint un número que indiqui la quantitat de caràcters de
cadascuna de les paraules del fitxer. El fitxer resultant s'ha de dir paraulesQuantitat.txt
"""
import datetime


def iniciar_log():
    with open('paraules.log', 'a') as log:
        log.write(f"{datetime.datetime.now()} - Iniciant el programa de recuento...\n")

def programa():
    with open('paraules.txt', 'r') as file:
        lineas = file.readlines()
    lineas = [linea.strip() for linea in lineas]
    lineas_procesadas = []
    for linea in lineas:
        nueva_linea = f"{len(linea)}\t{linea}"
        lineas_procesadas.append(nueva_linea)
    with open('paraulesQuantitat.txt', 'w') as file:
        # Escriure cada línia en el fitxer
        for linea in lineas_procesadas:
            file.write(linea + '\n')
def acabar_log():
    with open('paraules.log', 'a') as log:
        log.write(f"{datetime.datetime.now()} - Programa  de recuento finalizado.\n")


def main():
    iniciar_log()
    programa()
    acabar_log()