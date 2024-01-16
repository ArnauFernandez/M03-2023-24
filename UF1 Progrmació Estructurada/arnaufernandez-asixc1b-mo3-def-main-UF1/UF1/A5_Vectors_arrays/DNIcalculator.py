"""
Arnau Fernandez Pinar
M03 UF1 A5
DNIcalculator.py
"""
DNILETTER=("t","r","w","a","g","m","y","f","p","d","x","b","n","j","z","s","q","v","h","l","c","k","e")
try:
    dni=int(input(""))
    print(DNILETTER[dni%23])
except:
    print("error"