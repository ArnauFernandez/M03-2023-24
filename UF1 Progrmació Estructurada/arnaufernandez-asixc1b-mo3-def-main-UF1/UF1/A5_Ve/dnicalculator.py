dni=int(input("Dame digitos para el DNI: "))
LETRAS=("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")
print("la letra del dni es: ", LETRAS[dni%23])