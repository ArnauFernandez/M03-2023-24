"""
Escriu un programa que demani un número a l'usuari un número de mes (per exemple,
el 4, és a dir) El programa ha de validar que el nombre de mes sigui entre 1 i 12, si no és
així ha de mostrar un missatge d'error i preguntar novament fins que l'usuari
introdueixi un número de mes vàlid.
Un cop obtingueu un nombre de mes correcte, el programa mostrarà per pantalla
quants dies té el mes (al nostre exemple, 30) i el nom del mes (a l'exemple, abril). Has de
fer servir llistes. Per simplificar suposarem que el febrer sempre té 28 dies.

"""
import random
llista_mesos = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
llista_dies = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mes = int(input("Introdueix un número de mes: "))
while mes < 1 or mes > 12:
    print("Error, el número de mes ha de ser entre 1 i 12")
    mes = int(input("Introdueix un número de mes: "))
print("El mes", llista_mesos[mes-1], "té", llista_dies[mes-1], "dies")