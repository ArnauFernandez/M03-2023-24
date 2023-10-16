notas=[]
for i in range(5):
    PedirNota=int(input("Dame una nota: "))
    if PedirNota>10 or PedirNota<0:
    
        print("nota no válida")
    else:
        notas.append(PedirNota)
mitjana=sum(notas)/len(notas)
print(mitjana,max(notas),min(notas))
print(notas)