"""
Crear un programa que llegeixi els preus de 5 articles i les quantitats venudes per una
empresa a les seves 3 sucursals. El programa demanarà per teclat:
● Els preus de cada article
● La quantitat de cada article venut a cada sucursal
A partir de les dades anteriors el programa calcularà i mostrarà per pantalla:
● Per cada article, quantes unitats s'han venut en total
● La quantitat d'articles venuts a la sucursal 2
● La quantitat de l'article 3 venut a la sucursal 1
● La recaptació total de cada sucursal
● La recaptació total de l’empresa
● La sucursal de més recaptació
Pista: podeu fer servir les funcions sum i max de Python.
"""
preus = []
quantitats = []
for i in range(5):
    preus.append(float(input("Introdueix el preu de l'article {}: ".format(i+1))))
    quantitats.append([])
    for j in range(3):
        quantitats[i].append(int(input("Introdueix la quantitat de l'article {} a la sucursal {}: ".format(i+1, j+1))))
print("Quantitats totals de cada article:")
for i in range(5):
    print("Article {}: {}".format(i+1, sum(quantitats[i])))
print("Quantitat de l'article 3 venut a la sucursal 1: {}".format(quantitats[2][0]))
print("Quantitat d'articles venuts a la sucursal 2: {}".format(sum([quantitats[i][1] for i in range(5)])))
print("Recaptació total de cada sucursal:")
for i in range(3):
    print("Sucursal {}: {}".format(i+1, sum([preus[j]*quantitats[j][i] for j in range(5)])))
print("Recaptació total de l'empresa: {}".format(sum([preus[i]*sum(quantitats[i]) for i in range(5)])))
print("Sucursal de més recaptació: {}".format(max([sum([preus[j]*quantitats[j][i] for j in range(5)]) for i in range(3)])))