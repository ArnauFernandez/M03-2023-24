"""   
    Antonio Flores Lopez 
    Arnau Fernandez Pinar
    18/10/2022
    ASIXcb M03 UF1 PR2
    Encript12345
"""
txt = input("Codifica tu mensaje ")
x = txt.replace("a", "1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
x = x.replace("A", "1").replace("E","2").replace("I","3").replace("O","4").replace("U","5")
print(x)