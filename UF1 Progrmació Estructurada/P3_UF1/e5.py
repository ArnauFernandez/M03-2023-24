factura=int(input())
DESCUENTO=(factura*15)/100
total=factura-DESCUENTO
if factura >150:
    print(total)
