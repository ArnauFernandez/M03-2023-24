import random
import statistics as stats

llista = []
par = 0
imp = 0

n = 100

for i in range(n):
    num = random.randint(1, 50)
    llista.append(num)

    if i % 2 == 0:
        par += num  # llista[::2] son les posicions pars 0,2,4...
    else:
        imp += num

print(llista)
print('Mitjana de nums pars:', par / (n / 2))
print("Mitjana de nums impart:", imp / (n / 2))
