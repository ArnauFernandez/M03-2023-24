# Vector de nombres
vector = (4, 8, 9, 40, 54, 84, 40, 6, 84, 1, 1, 68, 84, 68, 4, 840, 684, 25, 40, 98, 54, 687, 31, 4894, 468, 46, 84687, 894, 40, 846, 1681, 618, 161, 846, 84687, 6, 848)

# Comprovar si algun dels nombres és divisible entre 7
resultat = any(num % 7 == 0 for num in vector)

# Imprimir el resultat
print(resultat)
