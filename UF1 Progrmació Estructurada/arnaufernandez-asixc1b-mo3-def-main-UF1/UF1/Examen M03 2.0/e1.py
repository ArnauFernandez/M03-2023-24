"""
Arnau Fernandez Pinar
ASIXc M03 UF1 Ex2
Javier Amaya 
QuantsDigits.py
13/12/2022
"""
num=int(input("introdueix un nombre: "))
numdiv = num.split(" ") 
num1= int(numdiv[0])
num2 = int(numdiv[1])
num3 = int(numdiv[2])
contNum=0
if num<=0:
    print("has introducido un carácter no válido")
else:
    if num1>=0:
        contNum=contNum=contNum+1
    else:
        if num2>=0:
            contNum=contNum+1
        else:
            if num3>=0:
                contNum=contNum+1
print("El numero te ",contNum,"dígits")

    