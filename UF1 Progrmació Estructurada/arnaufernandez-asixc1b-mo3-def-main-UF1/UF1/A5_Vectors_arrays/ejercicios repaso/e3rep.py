"""
Es vol fer un programa que llegeixi per teclat les 5 notes obtingudes per un alumne
(s’ha de validar que els notes estiguin compreses entre 0 i 10). A continuació heu de
mostrar totes les notes, la nota mitjana, la nota més alta que ha tret i la menor.
Pista: max , min, sum, len
"""
llista = []
for i in range(5):
    llista.append(int(input("Introduce una nota ")))
for i in llista:
    print(i)
print("La nota media es ", sum(llista)/len(llista))
print("La nota mas alta es ", max(llista))
print("La nota mas baja es ", min(llista))
