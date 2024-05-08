import logging
import time

def setup_logging():
    logging.basicConfig(filename='paraules.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Temps d'execució: {execution_time:.2f} segons")

def llegir_paraules(ruta):
    try:
        logging.info("Inici de la lectura del fitxer")
        with open(ruta, 'r', encoding='utf-8') as fitxer:
            paraules = fitxer.readlines()
            paraules = [paraula.strip().lower() for paraula in paraules]
        logging.info("Fi de la lectura del fitxer")
        return paraules
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
    except Exception as e:
        logging.error(f"Error en escriure les paraules als fitxers: {str(e)}")
    finally:
        for fitxer in fitxers.values():
            fitxer.close()

def main():
    setup_logging()
    start_time = time.time()

    paraules = llegir_paraules("paraules.txt")
    escriure_paraules_per_consonant(paraules)

    log_execution_time(start_time)

if __name__ == "__main__":
    main()
