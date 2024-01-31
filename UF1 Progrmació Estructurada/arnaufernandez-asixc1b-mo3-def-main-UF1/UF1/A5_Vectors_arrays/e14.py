# Inicialitzar les llistes per emmagatzemar els preus i les quantitats venudes
preus_articles = []
quantitats_sucursals = [[] for _ in range(3)]

# Llegir els preus de cada article
for i in range(5):
    preu = float(input(f"Introdueix el preu de l'article {i + 1}: "))
    preus_articles.append(preu)

# Llegir les quantitats venudes per cada sucursal i article
for sucursal in range(3):
    for article in range(5):
        quantitat = int(input(f"Introdueix la quantitat de l'article {article + 1} venut a la sucursal {sucursal + 1}: "))
        quantitats_sucursals[sucursal].append(quantitat)

# Calcular i mostrar les dades sol·licitades
print("\nResultats:")
for article in range(5):
    total_articles = sum(quantitats_sucursals[s][article] for s in range(3))
    print(f"Quantitat total venuda de l'article {article + 1}: {total_articles} unitats")

quantitat_sucursal_2 = sum(quantitats_sucursals[1])
print(f"\nQuantitat total venuda a la sucursal 2: {quantitat_sucursal_2} unitats")

quantitat_article_3_sucursal_1 = quantitats_sucursals[0][2]
print(f"Quantitat de l'article 3 venut a la sucursal 1: {quantitat_article_3_sucursal_1} unitats")

recaptacio_sucursals = [sum(preus_articles[article] * quantitats_sucursals[s][article] for article in range(5)) for s in range(3)]
for sucursal in range(3):
    print(f"Recaptació total de la sucursal {sucursal + 1}: {recaptacio_sucursals[s]} euros")

recaptacio_empresa = sum(recaptacio_sucursals)
print(f"\nRecaptació total de l'empresa: {recaptacio_empresa} euros")

sucursal_mes_recaptacio = recaptacio_sucursals.index(max(recaptacio_sucursals)) + 1
print(f"La sucursal amb més recaptació és la sucursal {sucursal_mes_recaptacio}")
