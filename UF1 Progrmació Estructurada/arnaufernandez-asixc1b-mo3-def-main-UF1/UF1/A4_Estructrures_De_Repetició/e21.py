import random
answer=int(input())
num=random.randint(1,101)
vidas=10
seguir=input()
try:
    while num != answer and vidas >0:
        print("És mes gran que",random.randint)
        if seguir.upper() =="SI":
            print("És mes gran que", random.randint)
        elif seguir.upper() =="NO":
            print("el numero es",answer,"han sobrado",vidas,"intentos")
except:
    print("error")