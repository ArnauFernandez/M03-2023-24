import logging
def llegir_paraules(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as fitxer:
            paraules = fitxer.readlines()
            paraules = [paraula.strip().lower() for paraula in paraules]
        return paraules
    except FileNotFoundError:
        logging.error(f"No s'ha trobat el fitxer {ruta}.")
        return []
    except Exception as e:
        logging.error(f"Error en llegir el fitxer {ruta}: {str(e)}")
        return []

def escriure_paraules_per_vocal(paraules):
    vocals = ['a', 'e', 'i', 'o', 'u']
    fitxers = {}

    try:
        for vocal in vocals:
            fitxers[vocal] = open(f"paraules-{vocal}.txt", 'w', encoding='utf-8')

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
    logging.basicConfig(filename='paraules.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    paraules = llegir_paraules("paraules.txt")
    escriure_paraules_per_vocal(paraules)

if __name__ == "__main__":
    main()


