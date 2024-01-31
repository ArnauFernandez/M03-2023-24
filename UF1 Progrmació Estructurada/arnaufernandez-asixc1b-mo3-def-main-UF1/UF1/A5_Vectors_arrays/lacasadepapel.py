# Inicialitzar una llista per al recompte de caixes
recompte_caixes = [0] * 11

# Llegir les obertures de caixes fins que s'introdueixi -1
while True:
    obertura_caixa = int(input("Introdueix el número de la caixa oberta (o -1 per finalitzar): "))

    # Comprovar si s'ha introdueixi -1 per finalitzar
    if obertura_caixa == -1:
        break

    # Comprovar si el número de la caixa és vàlid (0-10)
    if 0 <= obertura_caixa <= 10:
        # Incrementar el recompte per a la caixa indicada
        recompte_caixes[obertura_caixa] += 1
    else:
        print("Número de caixa no vàlid. Si us plau, introdueix un número de caixa entre 0 i 10.")

# Mostrar el recompte de caixes
print(recompte_caixes)
