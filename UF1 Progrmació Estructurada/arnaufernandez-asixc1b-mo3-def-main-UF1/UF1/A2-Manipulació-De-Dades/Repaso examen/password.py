#ex2
frase=input("Introduce una frase: ")
letraReemplazar=input("Letra a reemplazar: ").lower()
nuevaLetra=input("nueva letra: ")
for i in frase:
    if i==letraReemplazar:
        i = nuevaLetra
    print(i,end=" ")
print("")