for x in range(ord("A"),ord("Z")+1):
    for y in range(ord("A"),x+1):
        print(chr(y),end="")
    print()