# Ejemplos de palabras y frases palindrómicas
ejemplos_palindromos = [
    "cec", "cuc", "gag", "mínim", "nan", "nen", "pipiripip",
    "I Paco pagès sega poc api.",
    "Mig el llegim",
    "Set penis ineptes.",
    "Un aviador roda i va nu",
    "Acurruca", "Roma",
    "Amo la pacífica paloma",
    "Sobornos son robos",
    "Nada, yo soy Adán",
    "Amigo, no gima",
    "Amad a la dama."
]

# Verificar si cada ejemplo es un palíndromo
for ejemplo in ejemplos_palindromos:
    # Eliminar espacios y convertir a minúsculas
    cadena = ejemplo.replace(" ", "").lower()

    # Comprobar si la cadena es igual a su inversa
    resultado = cadena == cadena[::-1]

    # Mostrar el resultado
    print(f'"{ejemplo}" es palíndromo: {resultado}')
