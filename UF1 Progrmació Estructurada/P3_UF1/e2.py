pnum=int(input("Dime un numero: "))
snum=int(input("Dime un numero: "))
if pnum>=snum:
    pnum, snum = snum,pnum
print(pnum,snum)