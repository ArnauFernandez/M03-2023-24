"Exercici 2 Crea una llista i inicialitza-la amb 5 cadenes de caràcters llegides per teclat. Copia els elements de la llista a una altra llista però en ordre invers, i mostra els elements d'aquesta segona llista per pantalla."
lista=[]
listaReves=[]
for i in range(5):
    palabras=input("dame cinco palabras: ")
    lista.append(palabras)
    print(palabras)
for i in range(5):
    listaReves.append(lista[4-i])
print(listaReves)