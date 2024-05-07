class Llum:
    def __init__(self):
        self.encesa = False

    def encendre(self):
        self.encesa = True

    def apagar(self):
        self.encesa = False

    def alternar_estat(self):
        self.encesa = not self.encesa

    def estat_actual(self):
        return self.encesa

def llegir_fitxer(ruta):
    accions = []
    with open(ruta, 'r') as fitxer:
        for linia in fitxer:
            accions.append(linia.strip())
    return accions

def main():
    llum = Llum()
    ruta_fitxer = input("Introdueix la ruta del fitxer: ")
    ordres = llegir_fitxer(ruta_fitxer)
    finalitzat_correctament = False

    for ordre in ordres:
        if ordre == "TURN ON":
            llum.encendre()
        elif ordre == "TURN OFF":
            llum.apagar()
        elif ordre == "TOGGLE":
            llum.alternar_estat()
        elif ordre == "END":
            finalitzat_correctament = True
            break
        else:
            print("Acció no vàlida.")

        print(llum.estat_actual())

    if not finalitzat_correctament:
        print("El fitxer no acabava amb l'acció 'END'.")

if __name__ == "__main__":
    main()
