"""
Arnau Fernandez Pinar
ASIXc M04 UF1 A4
Javier Amaya
MyPython.py
"""
CAP= "...\.../ ..."
ULLS= "...╚⊙ ⊙╝..."
COS = "═(███)═"
CUA =  " ═V═ "
pedir_cuerpo=int(input("introduce una medida: "))
print(CAP)
print (ULLS)
cont = 0
var=1
for cuerpo in range (pedir_cuerpo):
    if cont==0:
        print(COS)
    if cont==1:
        print(" ",COS)
    if cont==2:
        print("  ",COS)    
    cont=cont+var
    if cont==3:
        cont=1
        var=-1
    if cont==-1:
        cont=1
        var=1
print(CUA)