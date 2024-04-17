
def readfile():
    path='studentsDS.py'
    file=open(path,mode='rt',encoding='utf-8')
    contenido = [int(nota) for nota in file.read().split()]
    file.close()
    print("nota minima: ", min(contenido))
    print("nota máxima: ", max(contenido))
    print("la media es : ", sum(contenido)/len(contenido))
    return contenido