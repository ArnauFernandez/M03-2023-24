import os

def readfile(path):
    file=open(path,mode='rt',encoding='utf-8')
    contenido = [int(nota) for nota in file.read().split()]
    file.close()
    media=sum(contenido)/len(contenido)
    print("nota minima: ", min(contenido))
    print("nota máxima: ", max(contenido))
    print("la media es : ",round(media,2))
    return contenido

