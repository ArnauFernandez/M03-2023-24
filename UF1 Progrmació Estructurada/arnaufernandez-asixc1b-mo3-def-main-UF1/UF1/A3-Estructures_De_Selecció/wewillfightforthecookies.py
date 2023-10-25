numeros=input()
numerosspl=numeros.split()
num1 = int(numerosspl[0])
num2 = int(numerosspl[1])
if num2%num1 == 0:
    print("let's eat")
else:
    print("let's fight")