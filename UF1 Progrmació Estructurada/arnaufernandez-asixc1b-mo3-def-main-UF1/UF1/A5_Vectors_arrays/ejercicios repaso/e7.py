"""
Escriu un programa que declari tres llistes “llista1”, “llista2” i “llista3”, amb cinc sencers
cadascuna, i que demani valors per a “llista1” i “llista2”. El programa ha d'emplenar
llavors llista3 de manera que contingui la suma dels elements de ‘llista1’ i ‘llista2’.
Per exemple, donades aquestes llistes:
llista1 = [23,54,-12,0,70]
llista2 = [543,-234,5,11,20]
‘llista3’ ha de tenir aquests elements:
llista3 = [566,-180,-7,11,90]
"""
llista1 = []
llista2 = []
llista3 = []
for i in range(5):
    llista1.append(int(input("Introduce un numero ")))
for i in range(5):
    llista2.append(int(input("Introduce un numero ")))
for i in range(5):
    llista3.append(llista1[i]+llista2[i])
for i in llista3:
    print(i)