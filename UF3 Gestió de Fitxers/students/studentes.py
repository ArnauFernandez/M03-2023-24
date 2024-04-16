import os
import statistics
file=open('student.stats',mode='rt',encoding='utf-8')
lecturaNotas=file.read()
lnum=[]
lnum.append(lecturaNotas)
media=statistics.mean(lnum)
file.close()

nums=lecturaNotas.split()

print("nota minima: ",min(nums))
print("nota máxima: ",max(nums))
print("la media es : ",media)