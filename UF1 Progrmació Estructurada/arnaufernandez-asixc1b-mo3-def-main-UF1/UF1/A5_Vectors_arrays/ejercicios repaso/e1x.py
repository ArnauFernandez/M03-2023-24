cuadrado1=[0,1,2,3,4]    
cuadrado2=[0,1,2,3,4,5,6,7,8,9,10,12,13,14]

for x in cuadrado1:
    for y in cuadrado2:
        if y==0 or x==0  or y==len(cuadrado2) or x==len(cuadrado1)-1:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("")