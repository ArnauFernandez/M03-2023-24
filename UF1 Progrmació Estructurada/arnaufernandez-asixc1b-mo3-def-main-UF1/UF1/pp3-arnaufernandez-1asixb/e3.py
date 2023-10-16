"""
Arnau Fernadez Pinar
ASIXc M03 UF1 PP3
24/01/2023
"""
CANT_PALABRAS=15 #declaramos la cantidad de palabras que queremos que tenga
listaPalabras=[] #generamos una lista para almacenar las palabras
LongPalabras=[] #generamos la lista para poder almacenar la longitud de las palabaras
for i in range(CANT_PALABRAS):
    PregPalabra=input("introduce una palabra: ") #pregunta al usuario una palabra
    listaPalabras.append(PregPalabra) #añade la plabara introducida por el usuario a la lista
    LongPalabras.append(len(PregPalabra)) #añade la longitud de la palabra para poder hacer la media de caracteres entre todos los carácteres

print("Las palabras introducidas son estas: ",listaPalabras) #muestra la lista de palabras introducidas
print("La palabra de mayor longitud es:",min(listaPalabras),"la palabra de menor longitud es :",max(listaPalabras))#muestra la palabra con mas caracteres y la que contiene menos
print("La Media de letras entre todas las palabras es de ",sum(LongPalabras)/len(LongPalabras)) #muestra la media de caracteres entre toda la suma de caracteres