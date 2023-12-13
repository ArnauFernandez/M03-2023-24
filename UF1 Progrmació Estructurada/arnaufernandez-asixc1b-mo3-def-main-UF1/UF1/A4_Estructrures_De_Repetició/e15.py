try:
    mensualidad = int(input(""))
    MESES = 20
    for i in range(1,MESES+1):
        if i<1:
            mensualidad=mensualidad
        if i>1:
            mensualidad =mensualidad*2
        print("El mes", i, "es un mensualidad de", mensualidad)
        total=mensualidad+mensualidad
    print("El total de los mensualidades es:",total)
except:
    print("No es un numero")