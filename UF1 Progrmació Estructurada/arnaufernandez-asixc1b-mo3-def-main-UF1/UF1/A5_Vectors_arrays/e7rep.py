# Declarar tres listas con cinco enteros cada una
llista1 = []
llista2 = []
llista3 = []

# Solicitar valores para llista1
print("Introdueix cinc valors per a llista1:")
for i in range(5):
    valor = int(input("Introdueix un enter: "))
    llista1.append(valor)

# Solicitar valores para llista2
print("Introdueix cinc valors per a llista2:")
for i in range(5):
    valor = int(input("Introdueix un enter: "))
    llista2.append(valor)

# Calcular la suma de llista1 y llista2 y llenar llista3
for i in range(5):
    suma = llista1[i] + llista2[i]
    llista3.append(suma)

# Mostrar en pantalla las tres listas
print("llista1:", llista1)
print("llista2:", llista2)
print("llista3 (suma de llista1 i llista2):", llista3)
