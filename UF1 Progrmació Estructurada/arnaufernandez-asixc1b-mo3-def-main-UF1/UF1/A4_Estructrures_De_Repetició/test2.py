letras="abcdefghijqlmnñopqrstuwxyz"
frase=input()
totalletras=0
for letras in frase.lower():
    totalletras+=1
print("la palabra introducida",frase," tiene ",totalletras,"caracteres")