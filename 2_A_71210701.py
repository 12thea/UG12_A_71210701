hm = str(input("Masuk nama : "))
kursi = []
dn = []
while hm != "STOP":
    o = "Masukkan nomor kursi "+hm+" : "
    a = input(o)
    if a not in kursi:
        kursi.append(a)
        dn.append(hm)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    hm = str(input("Masukkan nama: "))
print("List kursi yang telah terisi : ")

for ga in range (len(kursi)):
    print("Kursi nomor %s telah diisi oleh %s"%(kursi[ga],dn[ga]))