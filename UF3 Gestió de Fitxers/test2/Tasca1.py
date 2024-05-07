"""
Joel Joan
02/05/2023
Prova practica 1
Crea un programa en python per processar el fitxer de text anomenat
paraules.txt per dur a terme les tasques que es detallen més endevant:
L'aplicació no ha de tenir menú. Es a dir, quan s'executi el programa ha d'executar totes les tasques seqüencialment.
Els resultats ha d'estar als arxius de sortida. O a l'arxiu de log, anomenat paraules.log
S'han de fer servir més d'un fitxer, per a obtenir un disseny modular.
Cal declarar atributs, funcions (amb paràmetres i valors de retorn), per tal d'aconsegguir
un disseny descendent.
En tot moment, s'ha de comntemplar i tractar, el possibles errors que l 'usuari pugui cometre.
Cal respectar en tot moemnt, els caràcters amb accent, les majuscules i les minúscules.
La tasca es crear 5 fitxers amb lesparaules que comencin per cadascuna de les 5 vocals.
És a dir s'ha de crear el fitzer:
paraules-a.txt
paraules-e.txt
paraules-i.txt
paraules-o.txt
paraules-u.txt
L 'origen de dades és l'arxiu paraules.txt. Aquest arxiu inclou paraules que no comencen per vocal, i simplemente s'hauran d'obviar"""
import os

import datetime


def iniciar_log():
    with open('paraules.log', 'a') as log:
        log.write(f"{datetime.datetime.now()} - Iniciando el programa de vocales...\n")
def programa():
    with open('paraules.txt', 'r') as file:
        lineas = file.readlines()
        lineas = [linea.strip() for linea in lineas]

    vocales = ['a', 'e', 'i', 'o', 'u']
    palabras_filtradas = []
    for palabra in lineas:
        if palabra[0].lower() in vocales:
            palabras_filtradas.append(palabra)
    for vocal in vocales:
        with open(f'paraules-{vocal}.txt', 'w') as file:
            vocales_filtradas = [word for word in palabras_filtradas if word[0].lower() == vocal]
            file.write('\n'.join(vocales_filtradas))
def acabar_log():
    with open('paraules.log', 'a') as log:
        log.write(f"{datetime.datetime.now()} - Programa  de vocales finalizado.\n")

def main():
    iniciar_log()
    programa()
    acabar_log()

