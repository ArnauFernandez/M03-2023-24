# Definir la configuració del joc
configuracio_joc = [
    ['x', 'x', '0', '0', '0', '0', 'x'],
    ['0', '0', 'x', '0', '0', '0', 'x'],
    ['0', '0', '0', '0', '0', '0', 'x'],
    ['0', 'x', 'x', 'x', '0', '0', 'x'],
    ['0', '0', '0', '0', 'x', '0', '0'],
    ['0', '0', '0', '0', 'x', '0', '0'],
    ['x', '0', '0', '0', '0', '0', '0']
]

# Llegir les coordenades (x, y) de l'usuari
x = int(input("Introdueix la coordenada x: "))
y = int(input("Introdueix la coordenada y: "))

# Comprovar si a la posició (x, y) hi ha aigua o un vaixell (tocat)
if configuracio_joc[y][x] == '0':
    print("Aigua")
else:
    print("Vaixell (tocat)")
