"""
Arnau Fernandez
ASIXc A2 M3
4/10/2022
IsValidNote
L'usuari escriu un enter i s'imprimeix true si existeix un bitllet d'euros amb la quantitat entrada, false en qualsevol altre cas.
"""
billete=int(input("Introduzca un valor"))
billetes=(5,10,20,50,100,200,500)
print(billete in billetes)