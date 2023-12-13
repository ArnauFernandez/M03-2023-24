"""
Arnau Fernandez Pinar
ASIXc PP1 UF1 Extraordinaria
30-05-2023
EsMenor
"""
dataNaixement=input("Dime una fecha de nacimiento")
dataActual=input("Dime la fecha de hoy")

if dataActual>dataNaixement:
    print("eres mayor de edad")
elif dataNaixement<dataActual:
    print("Eres menor de edad")
else:
    print("error")