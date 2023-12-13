try:
    vocales='aeiou'
    consonants='bcdfghjklmnpqrstwxyz'
    texto='0'
    caracteresesp="\/$%€@|ª="
    while texto not in vocales or texto not in consonants or texto not in caracteresesp:
        texto = input("Ingrese: ")
        if texto in vocales:
            print("Vocal")
        elif texto in consonants:
            print("Consonant")
        elif texto ==' ':
            break
        elif texto in caracteresesp:
            print("caracter especial")
        elif len(texto)>1:
            print("no valido")
except:
    print("caracteres no permitidos")