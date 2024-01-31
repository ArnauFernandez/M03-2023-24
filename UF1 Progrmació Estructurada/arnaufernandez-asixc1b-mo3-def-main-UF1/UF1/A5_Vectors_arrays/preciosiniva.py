# Constant per l'IVA (21%)
IVA_PERCENTATGE = 21

# Llegir els preus dels 10 articles
preus_sense_iva = [float(input(f"Introdueix el preu sense IVA de l'article {i + 1}: ")) for i in range(10)]

# Calcular i imprimir els preus amb IVA
for i in range(10):
    preu_amb_iva = preus_sense_iva[i] + (preus_sense_iva[i] * IVA_PERCENTATGE / 100)
    print(f"{preus_sense_iva[i]} IVA = {preu_amb_iva:.2f}")
