hm = input("input : ")
ish = len(hm)
print("Output :",end="")

for y in range(ish):
    print(hm[:y])

for ok in range(ish,0,-1):
    print(hm[:ok])