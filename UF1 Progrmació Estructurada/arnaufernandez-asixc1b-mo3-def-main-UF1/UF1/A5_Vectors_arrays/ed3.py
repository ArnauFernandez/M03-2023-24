# Declarar el diccionario con los precios por kilo de las frutas
preus_fruites = {
    'poma': 2.5,
    'pera': 1.8,
    'banana': 3.0,
    'taronges': 2.2,
    'maduixa': 4.5
}

# Bucle principal
while True:
    # Leer la fruta y la cantidad del usuario
    fruita = input("Introdueix el nom de la fruita: ").lower()
    quantitat = float(input("Introdueix la quantitat en quilos: "))

    # Calcular el importe de la venta y mostrarlo si la fruta existe
    if fruita in preus_fruites:
        preu_quilo = preus_fruites[fruita]
        import_venda = preu_quilo * quantitat
        print(f"Import de la venda de {quantitat} quilos de {fruita.capitalize()}: {import_venda:.2f} euros")
    else:
        print("La fruita indicada no existeix.")

    # Preguntar si se quiere continuar calculando importes
    continuar = input("Vols continuar calculant imports? (s/n): ").lower()
    if continuar != 's':
        break
