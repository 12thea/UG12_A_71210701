ya = int(input("input: "))
ga = 2

for b in range(1,ya+1):
    for k in range(1,(2*ya)):
        if b+k==ya+1 or k-b==ya-1:
            print("*",end="")
        elif b==ya and k!=ga:
            print("*",end="")
            ga=ga+2
        else:
            print(end=" ")
    print()