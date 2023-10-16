listaNum=[]
AskNum=int(input("Dame un número: "))
while AskNum >0:
        AskNum=int(input("Dame un número: "))
        listaNum.append(AskNum)
        if AskNum<0:
            print("Error")
print(listaNum)