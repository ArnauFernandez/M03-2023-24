try:
    # Solicita al usuario la cantidad de números primos que desea mostrar
    n = int(input("Introdueix la quantitat de nombres primers a mostrar: "))

    if n <= 0:
        print("Si us plau, introdueix un nombre enter positiu.")
    else:
        # Inicializa variables
        numeros_primers = []
        num = 2

        # Muestra los primeros N números primos
        while len(numeros_primers) < n:
            # Comprueba si el número es primo
            es_primer = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primer = False
                    break

            # Si es primo, lo imprime
            if es_primer:
                print(num, end=' ')
                numeros_primers.append(num)
            num += 1

except ValueError:
    print("Si us plau, introdueix un nombre enter.")
