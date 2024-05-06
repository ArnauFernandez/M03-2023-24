
from eventsLog import data_hora_actual
from eventsLog import abrir_log
from eventsLog import events
def obrir_arxiu(rutaOrigen):
    try:
        texto = ""
        archivo = open(rutaOrigen, mode='r', encoding='utf-8')
        linia = archivo.readline()
        archivo.seek(0)
        while linia != "":
            linia = archivo.readline()
            texto += linia
        texto = texto.split('\n')
        archivo.close()
        return texto
    except:
        print("Error")

def escriure_arxiu(text, rutaDestino, tasca):
    try:
        log = abrir_log()
        if tasca == 'tasca1':
            terminacions = ["ing", "itb", "tic", "tica", "ció"]
            for term in range(len(terminacions)):
                archivo = open(rutaDestino + '-' + str(terminacions[term]) + '.txt', mode='w', encoding='utf-8')
                #log.write(data_hora_actual + ' ' + events['accions']['arxiuObert'] + f'("{archivo}")' + '\n')
                for palabra in text[term]:
                    archivo.write(palabra + '\n')
                archivo.close()
               #log.write(data_hora_actual + ' ' + events['accions']['arxiuTancat'] + f'("{archivo}")' + '\n')
        elif tasca == 'tasca2':
            archivo2 = open(rutaDestino + 'Quantitat.txt', mode='w', encoding='utf-8')
            for letras in range(len(text)):
                archivo2.write(text[letras][0] + '\t' + str(text[letras][1]) + '\n')
    except FileNotFoundError:
        log.write(data_hora_actual + ' ' + events["errors"]["FileNotFound"] + '\n')
        log.write(data_hora_actual + ' ' + events["accions"]["programaFinalitzat"] + '\n')
    except PermissionError:
        log.write(data_hora_actual + ' ' + events["errors"]["Permisos"])
        log.write(data_hora_actual + ' ' + events["accions"]["programaFinalitzat"] + '\n')
    except:
        log.write(data_hora_actual + ' ' + events["errors"]["Funcio"] + escriure_arxiu().__name__ + '\n')
        log.write(data_hora_actual + ' ' + events["accions"]["programaFinalitzat"] + '\n')

