"""
Arnau Fernandez
pp3 e1 M03
1/02/2024
"""
try:
    MESURA = 5
    MATRIU = MESURA
    for x in range(MATRIU):
        for y in range(MATRIU):
            if x == 0 or x == MATRIU - 1 or y == 0 or y == MATRIU - 1 :
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
except:
    print("error")