"""
            Luis Arteaga
            M03-Programació
            UF1
            24/1/2023
            Encriptar frases
            Descripció:
            Feu un programa per llegir una frase pel teclat i, en acabar, mostri la frase encriptada. Per encriptar
            la frase, ha de fer servir la posició alfabetica de cadascuna de les lletres, començant per la "a" amb un
            zero, la "b" amb el u, etc.
            Els espais en blanc no s'han de codificar i entre el codi numeric de cada lletra. Caldra escriure el
            caracter : per poder identificar a on comença i acaba cada lletra. No fer diferencies entre
            majuscules i minuscules. Exemple: Aaa 0:0:0 Bbb 0:0:0 Mmmab 12:12:12:0:1.
"""
frase = input("Introdueix la frase: ")
frase = frase.lower()
frase.replace(" ", "")
for x in frase:
    print(ord(x), end=".")
