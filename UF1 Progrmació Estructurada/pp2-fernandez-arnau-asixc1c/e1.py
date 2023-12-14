"""
Arnau Fernandez Pinar
14/12/2023
PP2 M03 UF1
e1 SumPositivevalues
"""
try:
    cant=int(input("Cantidad de dígitos a introducir: ")) #pedimos al usuario la cantidad de digitos que desea
    total=0 #creamos una variable acumuladora para obtener el resultado
    for i in range(cant):
        num=int(input("introduce un numero: "))
        if num<0: #aqui controlamos que el numero introducido no sea negativo para evitar resultados negativos
            total=total+0
        else:
            total=total+num #aqui controlamos que el numero sea positivo y podamos añadir digitos a la variable acumuladora
    print(total)
except:
    print("error")