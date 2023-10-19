"""
Arnau Fernandez Pinar
ASIXc M03 UF1 PP1
Exercici 2: e2.py
Crear un programa que sigui capaç de calcular la nota final de la UF3 del mòdul 03
del Cicle de Grau Superior d'Administració de Sistemes Informàtics en Xarxa (CFGS ASIX).
El programa només haurà de fer el càlcul per a 1 estudiant, i mostra'ls per pantalla.
Les notes de cadascun dels estudiants s'haurà de demanar per pantalla.
La fórmula de la UF3 és: QUF3 =1*RA1 a on  RA1= 0,30*Pt1.3 + 0,70*Pp1.
El pes de cada IA està fitxat a l'inici de curs per a no ser modificat. La nota final de les UF's es calcula amb 2 decimals.
"""
ra1=float(input(""))
pp1=float(input(""))
quf3=ra1*0.30+pp1*0.70
print("La UF3 te els següents resultats, RA1 ",ra1,"prova pràctia ",pp1,"la nota total de la uf3 es ",round(quf3,2))