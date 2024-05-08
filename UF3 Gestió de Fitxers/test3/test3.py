import logging

def llegir_paraules(ruta):
    try:
        logging.info("programa iniciat")
        with open(ruta, 'r', encoding='utf-8') as fitxer:
            paraules = fitxer.readlines()
            paraules = [paraula.strip().lower() for paraula in paraules]
        return paraules
        logging.info("programa acabat")
    except FileNotFoundError:
        logging.error(f"No s'ha trobat el fitxer {ruta}.")
        return []
    except Exception as e:
        logging.error(f"Error en llegir el fitxer {ruta}: {str(e)}")
        return []

def escriure_paraules_per_consonant(paraules):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    fitxers = {}

    try:
        for consonant in consonants:
            fitxers[consonant] = open(f"paraules-{consonant}.txt", 'w', encoding='utf-8')

        for paraula in paraules:
            primera_lletra = paraula[0]
            if primera_lletra in fitxers:
                fitxers[primera_lletra].write(paraula + '\n')
            else:
                logging.info(f"Paraula que comença per consonant: {paraula}")
    except Exception as e:
        logging.error(f"Error en escriure les paraules als fitxers: {str(e)}")
        # No es necesaria la cláusula finally
        for fitxer in fitxers.values():
            fitxer.close()

def main():
    logging.basicConfig(filename='paraules.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    paraules = llegir_paraules("paraules.txt")
    escriure_paraules_per_consonant(paraules)


