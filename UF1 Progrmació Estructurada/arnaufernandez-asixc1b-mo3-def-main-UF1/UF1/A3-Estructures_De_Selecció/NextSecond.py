"""
Arnau Fernandez
ASIXc 1B UF1 M03 A3
2/11/2022
NextSecond.py
L'usuari introdueix una hora amb tres enters (hores, minuts i segons).
Imprimeix l'hora que serà al cap d'un segon
Input
10 50 59
Output
10:51:00
"""
horaEnt = input()
Horaspl = horaEnt.split(" ") 
hora = int(horaEnt[0])
minuto = int(horaEnt[1])
segundo = int(horaEnt[2])
segundo=segundo+1
HoraRev=(0<=hora<=23 and 0<=minuto<=59 and 0<=segundo<=59)
if HoraRev:
    segundo=segundo+1
    if segundo==0:
        segundo=0
        minuto=minuto+1
    if minuto== 0:
        minuto=0
        hora= hora+1
    if hora==24:
        hora=0
        minuto=0  
        segundo=0 
if (segundo<10):
    segundo="0"+str(segundo)
if (minuto<10):
    minuto="0"+str(minuto)
if (hora<10):
    hora="0"+str(hora)
print(str(hora)+":"+str(minuto)+":"+str(segundo))
 else:
        print("Hora no válida")