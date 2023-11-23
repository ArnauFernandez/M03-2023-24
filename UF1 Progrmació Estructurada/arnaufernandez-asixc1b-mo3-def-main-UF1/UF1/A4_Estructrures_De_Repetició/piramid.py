CONT=0
SIMBOLO="🧱"
cantidad=int(input())
for base in range(cantidad):
    CONT = CONT + 1
    if CONT >= 1:
        print(SIMBOLO * CONT)