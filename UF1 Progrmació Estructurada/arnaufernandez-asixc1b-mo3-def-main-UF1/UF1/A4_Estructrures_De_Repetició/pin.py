"""
Arnau Fernandez Pinar
ASIXc M04 UF1 A4
Javier Amaya
Pin.py
"""
pin ="4567"
for p in range(3):
    pw = int(input("Introduce el pin: "))
    if pw == pin:
        print("Bienvenido")
    else:
        pw = int(input("Introduzca la clave de nuevo: "))
print("Bloqueado")