import math
salari_base=int(input("introduzca un valor "))
venta1=int(input("introduzca un valor de venta "))
venta2=int(input("introduzca un valor de venta "))
venta3=int(input("introduzca un valor de venta "))
extra=(venta1+venta2+venta3)*0.1
total=(salari_base + extra)
print("el salario base es de",salari_base)
print("el total recibido por tres ventas es",total)