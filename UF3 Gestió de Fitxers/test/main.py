import os
import tasques
import text_InputOutput
from eventsLog import data_hora_actual
from eventsLog import abrir_log
from eventsLog import events
def main():
    try:
        log = abrir_log()
        log.write(data_hora_actual + ' ' + events["accions"]["programaIniciat"] + '\n')
        RUTAORIGEN =os.path.join('entrada','paraules.txt')
        RUTADESTI = os.path.join('sortida','paraules.txt')
        text = text_InputOutput.obrir_arxiu(RUTAORIGEN)
        ##TASCA1
        llistaAmbTerminacions = tasques.tasca1(text)
        text_InputOutput.escriure_arxiu(llistaAmbTerminacions, RUTADESTI, 'tasca1')
        ##TASCA2
        llistaAmbQuantitatLletres = tasques.tasca2(text)
        text_InputOutput.escriure_arxiu(llistaAmbQuantitatLletres, RUTADESTI, 'tasca2')
    except:
        log.write(data_hora_actual + ' ' + events["errors"]["Funcio"] + main.__name__ + '\n')

log = abrir_log()
main()
log.write(data_hora_actual + ' ' + events["accions"]["programaFinalitzat"] + '\n')