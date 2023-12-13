"""
Arnau Fernandez Pinar
ASIXc PP1 UF1 Extraordinaria
30-05-2023
QuantesXifres
"""
try:
    pedirnum=0
    while pedirnum!=10000:
        pedirnum = int(input("introduce un numero: "))
        if pedirnum > 1 and pedirnum <10:
                print("el numero",pedirnum,"tiene 1 cifra")
        elif pedirnum >= 10 and pedirnum <100:
                print("el numero",pedirnum,"tiene 2 cifras")
        elif pedirnum >= 100 and pedirnum <1000:
            print("el numero", pedirnum, "tiene 3 cifras")
        elif pedirnum >= 1000 and pedirnum < 10000:
            print("el numero", pedirnum, "tiene 4 cifras")
        elif pedirnum >= 10000 and pedirnum < 10000:
            print("el numero", pedirnum, "tiene 5 cifras")
        elif pedirnum >10000:
            break
except:
    print("error")