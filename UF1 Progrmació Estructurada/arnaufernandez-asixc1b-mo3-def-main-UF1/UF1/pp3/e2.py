"""
Arnau Fernandez Pinar
pp3 e2 M03
1/02/2024
"""
try:
    frase = input("Introdueix la frase: ")
    frase = frase.lower()
    frase.replace(" ", "")
    for x in frase:
        print(ord(x) - 32 , end=".")
except:
    print("error")