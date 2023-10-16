"""
Arnau Fernandez Pinar
ASIXc M03 UF1 PP3
24/01/2023
e1
"""
cuadrado1=int(input("Pide un tamaño: "))    
cuadrado2=int(input("Pide un Tamaño: ")) #generar variables para la creacion de la matriz

for x in range(cuadrado1):
    for y in range(cuadrado2):
        if y==0 or x==0  or y==cuadrado2-1 or x==cuadrado1-1: 
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("") #genera la matriz y controla donde debe poner 1 o 0



"""
cuadrado1=[0,1,2,3,4]    
cuadrado2=[0,1,2,3,4,5,6,7,8,9,10,12,13,14] #generar listas para la creacion de la matriz

for x in cuadrado1:
    for y in cuadrado2:
        if y==0 or x==0  or y==len(cuadrado2) or x==len(cuadrado1)-1: 
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("") #genera la matriz y controla donde debe poner 1 o 0
"""