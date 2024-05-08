import os
def calcular_quantitat_paraules(ruta_entrada, ruta_sortida):
    try:
        with open(ruta_entrada, 'r', encoding='utf-8') as fitxer_entrada:
            with open(ruta_sortida, 'w', encoding='utf-8') as fitxer_sortida:
                for linia in fitxer_entrada:
                    paraula = linia.strip()
                    quantitat_caracters = len(paraula)
                    fitxer_sortida.write(f"{paraula} {quantitat_caracters}\n")
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer {ruta_entrada}.")
    except Exception as e:
        print(f"S'ha produït un error: {str(e)}")

ruta_entrada = os.path.join('test3','paraules.txt')
ruta_sortida = os.path.join('test3','paraulesQuantitat.txt')
calcular_quantitat_paraules(ruta_entrada, ruta_sortida)
