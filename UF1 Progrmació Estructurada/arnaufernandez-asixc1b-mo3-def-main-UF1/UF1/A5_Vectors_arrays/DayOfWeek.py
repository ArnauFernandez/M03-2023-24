listDays=["","Dilluns","Dimarts","Dimecres","Dijous","Divendres"]
MIN=1
MAX=7
asknum=int(input("Introduzca usted un numero del 1 al 7: "))
try:
    if asknum >= MIN or asknum <= MAX:
        print(listDays[asknum])
except:
    print("error")
