def readfile2(path):
    file=open(path,mode='rt',encoding='utf-8')
    contenido = [int(nota) for nota in file.read().split() if nota.isdigit()]
    file.close()
    media=sum(contenido)/len(contenido)
    print("nota minima: ", min(contenido))
    print("nota máxima: ", max(contenido))
    print("la media es : ",round(media,3))
    return contenido