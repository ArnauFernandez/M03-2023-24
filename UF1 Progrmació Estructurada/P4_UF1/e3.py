"""
Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a un número límit, 
que l’usuari introdueix per teclat. ( Ex: si el límit és 31 sumaParells 240 i sumaSenars 225)
"""
par=0
impar=0
for i in range(31):
    if i %2==0:
       par=par+i
    else:
        impar=impar+i
print(par,impar)