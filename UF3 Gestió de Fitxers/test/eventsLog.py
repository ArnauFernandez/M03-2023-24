

import datetime

try:
    def abrir_log():
        log = open('./log/paraules.log', mode='a', encoding='utf-8')
        return log

    data_hora_actual = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    events = {
        "errors": {
            "FileNotFound": "ERROR: No s'ha trobat l'arxiu especificat.",
            "IsADirectory": "ERROR: L'arxiu especificat és un directori.",
            "Permissos": "ERROR: permissos requerits.",
            "Funcio": "ERROR: error desconegut a la funció ",
            "Arxiu": "ERROR: error desconegut a l'arxiu "
        },
        "accions": {
            "programaIniciat": "S'ha iniciat el programa ",
            "programaFinalitzat": "Ha finalitzat el programa ",
            "arxiuObert": "S'ha obert ",
            "arxiuTancat": "S'ha tancat ",
            "tasca1": "[TASCA 1] S'han extret les paraules amb terminacions correctament.",
            "tasca2": "[TASCA 2] S'han comptat les paraules correctament."
        }
    }

except:
    print('ERROR: Fatal')
