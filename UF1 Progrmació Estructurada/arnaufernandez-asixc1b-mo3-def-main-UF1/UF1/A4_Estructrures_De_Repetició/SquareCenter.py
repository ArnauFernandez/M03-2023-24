"""
Arnau Fernandez Pinar
ASIXc M03 A4 UF1
Javier Amaya
SquareCenter.py
Fes una funció que dibuixi dos quadrats concèntrics. l'usuari introdueix dos valors, el primer defineixen el costat del quadrat extern que pintarem amb o, el segon defineix el costat del segon quadrat. Aquest segon quadrat el pintarem amb *.
"""
medidas=input()
numspl= medidas.split()
cuadrPequeño=int(numspl[1])
cuadrGrande=int(numspl[0])
base=int ((cuadrGrande-cuadrPequeño)/2)
basex=int(cuadrPequeño)
#dibujar cuadrados
for x in range(cuadrGrande):
    basey=int(cuadrPequeño)
    for y in range(cuadrGrande):
        #cuadrado pequeño
        if (x>base-1 and y>base-1) and (basey>0 and basex>0):
            print("*  ",end="")
            basey=basey-1
        else:
            #cuadrado grande
              print("0  ",end="")
    #baja el contador cada vez que hace una línea nueva
    if(basex>0) and (x>base-1):
        basex=basex-1 
    print("")