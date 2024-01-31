import random
from random import randint
lnum=[]
for i in range(5):
    aleatorio=random.randint(1,10)
    lnum.append(aleatorio)
print(lnum)
print("la nota mas alta es: ",max(lnum),"la nota mas baja es: ",min(lnum),"la nota media es: ",sum(lnum)/len(lnum))