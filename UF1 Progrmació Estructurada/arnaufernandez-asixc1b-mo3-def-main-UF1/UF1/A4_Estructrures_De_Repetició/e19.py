"""
e19.py “menuOpcions”
Escriu un programa que mostri el següent menú d’opcions:
Literatura
Cinema
Música
Videojocs
Sortir
Si l’usuari tria una opció de l’1 al 4,
el programa ha de mostrar uns quants suggeriments de títols relacionats amb el tema escollit.
Si l’usuari tria una opció no contemplada, el programa ha de mostrar un missatge d’error.
En tot cas, el programa tornarà a mostrar el menú d’opcions,
tret que l’usuari triï l’opció 5: en aquest cas,
el programa mostrarà un missatge de comiat i acabarà.
"""
choice=int(input())
while choice !=5:
    if choice ==1:
        print("Literatura")
    elif choice ==2:
        print("Cinema")
    elif choice ==3:
        print("Música")
    elif choice == 4:
        print("Videojocs")
print("no has escollit cap tema adeu")