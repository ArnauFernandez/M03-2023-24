# Llegir 10 enters de l'usuari
llista_valors = [int(input(f"Introdueix l'enter {i + 1}: ")) for i in range(10)]

# Trobar el valor més petit utilitzant la funció min()
valor_mes_petit = min(llista_valors)

# Imprimir el valor més petit
print(f"El valor més petit introduït és: {valor_mes_petit}")
