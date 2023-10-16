"""  
    Antonio Flores Lopez 
    Arnau Fernandez Pinar
    18/10/2022
    ASIXcb M03 UF1 PR2
    WorkingAge
"""
edad_min=16
edad_max=65
pregunta_edad=int(input("Cual es tu edad? "))
if(pregunta_edad>=edad_min and pregunta_edad<=65):
    print("Tienes edad para trabajar")
else:
    print("No tienes edad para trabajar")