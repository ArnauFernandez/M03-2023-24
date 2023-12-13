try:
    # Solicita al usuario un número para comprobar si es primo
    numero = int(input("Introdueix un nombre per comprovar si és primer: "))

    # Comprueba si el número es menor o igual a 1
    if numero <= 1:
        print(f"{numero} no és un nombre primer.")
    else:
        # Itera desde 2 hasta la parte entera de la raíz cuadrada del número
        es_primer = True
        limite = int(numero**0.5) + 1
        for i in range(2, limite):
            # Si el número es divisible por algún número en ese rango, no es primo
            if numero % i == 0:
                es_primer = False
                break

        # Muestra el resultado
        if es_primer:
            print(f"{numero} és un nombre primer.")
        else:
            print(f"{numero} no és un nombre primer.")

except ValueError:
    print("Si us plau, introdueix un nombre enter.")
