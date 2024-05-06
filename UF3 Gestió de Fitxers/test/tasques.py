
from eventsLog import data_hora_actual
from eventsLog import abrir_log
from eventsLog import events

def tasca1(texto):
    try:
        log = abrir_log()
        paraulesIng, paraulesItb, paraulesTic, paraulesTica, paraulesCio = [], [], [], [], []
        for palabra in texto:
            if palabra[-3:] == "ing":
                paraulesIng.append(palabra)
            elif palabra[-3:] == "itb":
                paraulesItb.append(palabra)
            elif palabra[-3:] == "tic":
                paraulesTic.append(palabra)
            elif palabra[-4:] == "tica":
                paraulesTica.append(palabra)
            elif palabra[-3:] == "ció":
                paraulesCio.append(palabra)
        log.write(data_hora_actual + ' ' + events["accions"]["tasca1"] + '\n')
        return paraulesIng, paraulesItb, paraulesTic, paraulesTica, paraulesCio
    except:
        log.write(data_hora_actual + ' ' + events["errors"]["Funcio"] + tasca1.__name__ + '\n')

def tasca2(texto):
    try:
        log = abrir_log()
        alfabet_catala = ['a', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n',
                          'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z']
        aparicionesLetras = []
        for palabra in texto:
            for letra in palabra:
                if letra in alfabet_catala:
                    encontrada = False
                    for recorrido in range(len(aparicionesLetras)):
                        if aparicionesLetras[recorrido][0] == letra:
                            aparicionesLetras[recorrido][1] += 1
                            encontrada = True
                    if encontrada is False:
                        aparicionesLetras.append([letra, 1])
        log.write(data_hora_actual + ' ' + events["accions"]["tasca2"] + '\n')
        aparicionesLetras = sorted(aparicionesLetras, key=lambda x: x[0])
        return aparicionesLetras
    except:
        log.write(data_hora_actual + ' ' + events["errors"]["Funcio"] + tasca2.__name__ + '\n')