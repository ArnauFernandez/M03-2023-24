INPUT = "Aquestx es una frase molt llarga i original"
OUTPUT = ''
#Primero defino las variables.
for c in INPUT:
    if c=='a' or c=='A':
        OUTPUT += 'x'
    #Le digo al programa que en la frase 'input' si encuentra un
    #caracter igual a 'a' o 'A' lo tenga en cuenta y lo cambie por X.
    #Se podria afinar mas.
    else:
        OUTPUT += c
    #En el caso que se cambiara el input, y no se cumpliera el if printaria nuevamente la frase.
print(OUTPUT)

frase = input("frase? ")
fraseResultat = ""
carReemplaçar = input("Caracter a reemplaçar? ")
carSubstitucio = input("Caraacter de substitutció? ")

for caracter in  frase:
    if caracter != carReemplaçar:
        fraseResultat = fraseResultat + caracter
    else:
        fraseResultat = fraseResultat + carSubstitucio

print(fraseResultat)