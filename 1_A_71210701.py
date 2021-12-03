D1 = input("Masukkan deret angka : ")
D2 = 0
D3 = (D1.split(","))
print("Total :",end=" ")
for D4 in D3:
    D4=int(D4)
    if D4%2==1:
        D2 = D2-D4
        print(D4*-1, end=" ")
    else:
        D2 = D2+D4
        print("+",D4,end=" ")
print()
print("Hasil perhitungan diatas ialah", D2)