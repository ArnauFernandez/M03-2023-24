velocidadIn=int(input())
aceleracion=int(input())
tiempo=int(input())
velInst=velocidadIn+aceleracion*tiempo
velMed=(velocidadIn+velInst)/2
print(velInst)
print(velMed)
if velocidadIn <=0:
    print('error')