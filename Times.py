def timer(x, z):
    if x == "Y" or x == "y":
        print("Sedang Memasak ~")
        print(z, "detik", " ~ ")
        if z <= 300:
            while z > 10:
                z -= 10
                print(z , "detik", " ~ ")
        elif z > 300:
            while z > 100:
                z -= 100
                print(z, "detik", " ~ ")
    return ("Waktu Habis")


def manualcook(x, y, z):
    for i in range(1, z+1):
        if y < x :
            cook(True)
            y += 1
        elif y < 30 :
            cook(False)
            y += 1
            if y == 30:
                y = 0
    return ' '


menit = int(input("Masukkan menit : "))
detik = int(input("Masukkan detik : "))
po = int(input("Masukkan tingkat Daya ( % ) :"))

cook_time = 0
power = 30*po//100
total_waktu = menit*60 + detik
print( menit, "menit dan ", detik, "detik ?", end = ' ')
a = str(input("Y/N " ))

while a != "Y" and a != "y" or a == "N" or a == "n":
    print("Ulangi input, tolong sesuaikan") ; print('')
    menit = int(input("Masukkan menit : "))
    detik = int(input("Masukkan detik : "))
    total_waktu = menit*60 + detik
    print( menit, "menit dan ", detik, "detik ?", end = ' ')
    a = str(input("Y/N " ))

print(cooking(a, total_waktu))

