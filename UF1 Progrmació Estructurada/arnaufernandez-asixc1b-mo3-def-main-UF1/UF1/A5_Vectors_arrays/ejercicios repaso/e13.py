"""
D'una empresa de transport es vol guardar el nom dels conductors que hi treballa, i els
quilòmetres que condueixen cada dia de la setmana.
Per desar aquesta informació es faran servir dues llistes:
● noms: Llista per desar els noms dels conductors.
● kms: Taula on a cada posició hi ha els kms que un conductor ha fet a cadascú dels
dies de la setmana.
Exemple de valors a les dues llistes:
noms = [Eva, Carles, Júlia]
kms = [
[100,230,90,150,80,115,75], # kms fets per Eva durant la setmana
[90,210,70,50,180,150,175] , # kms fets per Carles durant la setmana
[220,160,170,90,70,250,120] # kms fets per Julia durant la setmana
]
El programa procedirà de la manera següent. Primer demanarà per teclat:
● els noms de cada conductor
● per a cada conductor, els kms de cada dia de la setmana
A continuació, el programa generarà una nova llista (“total_kms”) amb els quilòmetres
totals que ha recorregut cada conductor durant la setmana.
Finalment, el programa mostrarà per pantalla la llista amb els noms de conductors i els
quilòmetres setmanals que ha fet.
"""
noms = []
kms = []
total_kms = []
for i in range(3):
    nom = input("Introdueix el nom del conductor: ")
    noms.append(nom)
    kms.append([])
    for j in range(7):
        km = float(input(f"Introdueix els quilòmetres del dia {j+1}: "))
        kms[i].append(km)
    total_kms.append(sum(kms[i]))
print("Noms\t\tKms")
for nom, km in zip(noms, total_kms):
    print(f"{nom}\t\t{km}")