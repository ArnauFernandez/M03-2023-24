class Robot:
    def __init__(self):
        self.posicio_x = 0.0
        self.posicio_y = 0.0
        self.velocitat = 1.0

    def dalt(self):
        self.posicio_y += self.velocitat

    def baix(self):
        self.posicio_y -= self.velocitat

    def dreta(self):
        self.posicio_x += self.velocitat

    def esquerra(self):
        self.posicio_x -= self.velocitat

    def accelerar(self):
        if self.velocitat < 10.0:
            self.velocitat += 0.5

    def disminuir(self):
        if self.velocitat > 0.5:
            self.velocitat -= 0.5

    def imprimir_posicio(self):
        print(f"La posició del robot és ({self.posicio_x}, {self.posicio_y})")

    def imprimir_velocitat(self):
        print(f"La velocitat del robot és {self.velocitat}")

def llegir_fitxer(ruta):
    accions = []
    with open(ruta, 'r') as fitxer:
        for linia in fitxer:
            accions.append(linia.strip())
    return accions

def main():
    robot = Robot()
    ruta_fitxer = input("Introdueix la ruta del fitxer: ")
    ordres = llegir_fitxer(ruta_fitxer)

    for ordre in ordres:
        if ordre == "DALT":
            robot.dalt()
        elif ordre == "BAIX":
            robot.baix()
        elif ordre == "DRETA":
            robot.dreta()
        elif ordre == "ESQUERRA":
            robot.esquerra()
        elif ordre == "ACCELERAR":
            robot.accelerar()
        elif ordre == "DISMINUIR":
            robot.disminuir()
        elif ordre == "POSICIO":
            robot.imprimir_posicio()
        elif ordre == "VELOCITAT":
            robot.imprimir_velocitat()
        elif ordre == "END":
            break
        else:
            print("Ordre invàlida.")

if __name__ == "__main__":
    main()
