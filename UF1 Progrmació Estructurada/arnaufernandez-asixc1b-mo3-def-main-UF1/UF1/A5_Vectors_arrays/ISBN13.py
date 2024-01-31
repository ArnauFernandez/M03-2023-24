# Input
isbn_13 = input("Introdueix els 13 dígits del codi ISBN-13: ")

# Verificació del dígit de control del ISBN-13
if len(isbn_13) == 13 and isbn_13.isdigit():
    suma = 0
    for i in range(12):
        digit = int(isbn_13[i])
        factor = 3 if i % 2 == 1 else 1
        suma += digit * factor

    control = (10 - (suma % 10)) % 10
    dígit_de_control = int(isbn_13[-1])

    resultat = control == dígit_de_control

    # Output
    print(resultat)
else:
    print("L'ISBN-13 ha de tenir 13 dígits i ser una seqüència de dígits.")
