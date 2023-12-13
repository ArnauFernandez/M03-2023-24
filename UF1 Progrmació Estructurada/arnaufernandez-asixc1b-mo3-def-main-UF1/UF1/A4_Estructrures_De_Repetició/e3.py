num=2
acum=0
total=0
try:
    while num !=0:
        num=int(input(""))
        acum= acum + 1
        total=total+num
    print(total/acum)
except:
    print("No es")