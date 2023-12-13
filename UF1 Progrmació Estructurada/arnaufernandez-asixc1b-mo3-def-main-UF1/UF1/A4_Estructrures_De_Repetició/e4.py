cantZeros=0
mayorZero=0
menorZero=0
cantidad=int(input(""))
for i in range(cantidad):
    numero=int(input(""))
    if numero>0:
        mayorZero=mayorZero+1
    elif numero<0:
        menorZero=menorZero+1
    else:
        cantZeros=cantZeros+1
print(mayorZero,menorZero,cantZeros)