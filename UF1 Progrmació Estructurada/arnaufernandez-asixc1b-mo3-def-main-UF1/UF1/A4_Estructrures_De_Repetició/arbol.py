from time import sleep
ARBOL="🧱"
TRONCO="🪵"
mida = int(input())
for i in range(1, mida+1):
    print(" "*(mida- i),ARBOL*i)
    sleep(1)
for i in range(mida):
        print(" "*(mida-1),TRONCO)
        sleep(1)
print(" ")
