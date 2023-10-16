fechaEnt = input("Introduce ")
fechaspl = fechaEnt.split("/") 
dia = int(fechaspl[0])
mes = int(fechaspl[1])
anyo = int(fechaspl[2])
FechaRev=(1<=mes<=12)
if FechaRev:
    if mes==1:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==2:
        if anyo % 4== 0 or (anyo % 100 == 0 and anyo %400==0):
            if dia<30:
                print("correcte")
        if not anyo % 4== 0 or (anyo % 100 == 0 and anyo %400==0):
            if dia<29:
                print("correcte")
            else:
                print("incorrecte")
    elif mes==3:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==4:
        if dia<31:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==5:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==6:
        if dia<31:
            print("correcte")
        else:
            print("incorrecte")

    elif mes==7:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==8:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==9:
        if dia<31:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==10:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==11:
        if dia<31:
            print("correcte")
        else:
            print("incorrecte")
    elif mes==12:
        if dia<32:
            print("correcte")
        else:
            print("incorrecte")
else:
    print("incorrecte")