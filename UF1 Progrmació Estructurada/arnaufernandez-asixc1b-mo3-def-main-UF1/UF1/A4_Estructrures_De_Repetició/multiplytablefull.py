"""
Arnau Fernandez Pinar
ASIXc M04 UF1 A4
Javier Amaya
MultiplyTable.py
"""
for vuelta in range(1,11):
    for multiplicar in range(1,11):
        if (vuelta*multiplicar) %2!=0:
            print("\t" )
        print("\t"+str(vuelta*multiplicar),end="")


