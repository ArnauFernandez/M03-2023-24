# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:15:59 2021

@author: Paulina
"""

palabra = input("Digues una paraula: ")

for char in range(len(palabra)- 1, -1, -1):
    print(palabra[char], end="")
print("\n")