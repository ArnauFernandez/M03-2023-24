from time import sleep
segundo = 00
minutos= 00
horas= 00
try:
    while segundo == 60:
        segundo = int(input())
        segundo=segundo-1
        sleep(1)
        print(str(00),":"+str(00),":"+str(segundo))

except:
    print("valor no valido")