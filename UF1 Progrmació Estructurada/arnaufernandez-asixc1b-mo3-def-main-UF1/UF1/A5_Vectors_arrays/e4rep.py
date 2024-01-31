lnum=[]
try:
    num=int(input("Ingrese"))
    while num!=0:
        asknum = int(input("Ingrese: "))
        if asknum>0:
            lnum.append(asknum)
        else:
            print("No es posible")
            break
    print(lnum)
except:
    print("error")