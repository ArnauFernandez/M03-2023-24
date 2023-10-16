"""
Arnau Fernandez Pinar
ASIXc Mo3 UF1
Excercici 2
Crear un programa que sigui capaç de calcular la nota final de la UF1 del mòdul 03 del Cicle de Grau Superior d'Administració de Sistemes Informàtics en Xarxa (CFGS ASIX). El programa només haurà de fer el càlcul per a 3 estudiants, i mostra'ls per pantalla. Les notes de cadascun dels estudiants s'haurà de demanar per pantalla. La fórmula de la UF1 és: QUF1 = 0,30*RA1 + 0,70*RA2.  El pes de cada RA's està fitxat a l'inici de curs per a no ser modificat. La nota final de les UF's es calcula amb 2 decimals.
"""
nota_RA1_a1=int(input("introduce un numero"))
nota_RA2_a1=int(input("introduce un numero"))
nota_RA1_a2=int(input("introduce un numero"))
nota_RA2_a2=int(input("introduce un numero"))
nota_RA1_a3=int(input("introduce un numero"))
nota_RA2_a3=int(input("introduce un numero"))
Nota_uf_a1=((nota_RA1_a1*0.3)+(nota_RA2_a1*0.7))
Nota_uf_a2=((nota_RA1_a2*0.3)+(nota_RA2_a2*0.7))
Nota_uf_a3=((nota_RA1_a3*0.3)+(nota_RA2_a3*0.7))
print("la nota de la uf1 del alumno 1 es",Nota_uf_a1,"la nota del alumno 2 es",Nota_uf_a2,"la nota del alumno 3 es",Nota_uf_a3)
