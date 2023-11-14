PIN=0
tries=3
while tries>0 and PIN !="1234" and PIN !="0007":
    PIN=input()
    tries=tries-1
if tries>0:
    print("pin correcto bienvenido te han sobrado",tries,"intentos")
else:
    print("sin intentos")