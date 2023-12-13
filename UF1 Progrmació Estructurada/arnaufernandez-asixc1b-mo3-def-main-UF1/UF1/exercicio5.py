"""
"""

palabra = input("Digues una paraula: ")

for char in range(len(palabra)- 1, -1, -1):
    print(palabra[char], end="")
print("\n")