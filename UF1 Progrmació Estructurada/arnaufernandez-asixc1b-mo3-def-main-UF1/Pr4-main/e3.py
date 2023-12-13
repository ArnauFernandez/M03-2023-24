"""
Arnau Fernández Pinar
Matteo Vilchez
e3
Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells
inferiors a un número límit, que l’usuari introdueix per teclat.
(Ex: si el límit és 31 sumaParells 240 i sumaSenars 225)

28/11/2023
"""
par=0
impar=0
num=int(input())
for i in range(num):
    if i %2==0:
       par=par+i
    else:
        impar=impar+i
print("la suma total de pares es: ",par,"la suma total de impares es: ",impar)
