CANT_PALABRAS=15
listaPalabras=[]
LongPalabras=[]
for i in range(CANT_PALABRAS):
    PregPalabra=input("introduce una palabra: ")
    listaPalabras.append(PregPalabra)
    LongPalabras.append(len(PregPalabra))

print("Las palabras introducidas son estas: ",listaPalabras)
print("La palabra de mayor longitud es:",min(listaPalabras),"la palabra de menor longitud es :",max(listaPalabras))
print("La Media de letras entre todas las palabras es de ",sum(LongPalabras)/len(LongPalabras))