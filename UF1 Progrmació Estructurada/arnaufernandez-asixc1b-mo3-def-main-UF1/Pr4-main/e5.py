"""
Arnau Fernández Pinar
Matteo Vilchez
e5
Programa que realitza la multiplicació, de dos nombres sencers,
mitjançant sumes
28/11/2023
"""
a = int(input())
b = int(input())
suma=0
for i in range(1,a+1):
        suma= suma + b
print(f"{a} x {b} = {suma}")