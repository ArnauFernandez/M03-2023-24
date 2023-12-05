import random
answer=random.randint(1,101)
vidas = 10
num=0
print(answer)
try:
    while num != answer and vidas != 0:
        print("tienes",vidas,"vidas")
        num=int(input(" "))
        if num==answer:
            print("acertaste con",vidas,"vidas")
        else:
            vidas = vidas - 1
    if vidas==0:
        print("sin vidas")
except:
    print("no me has dado un numero")