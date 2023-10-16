numpos=0
numneg=0
zero=0
for i in range(2):
    numero=int(input())
    if numero>0:
        numpos=numpos+numero
    elif numero <0:
        numneg=numneg+1
    else:
        zero=zero+1
print("el total de valores mayores a 0 son",numpos)
print("el total de valores menores a 0 son",numneg)
print("el total de valores iguales a 0 son",zero)