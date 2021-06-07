from UI_Function import *
from Object_Function import *

Z = 10
cook(False)
sensor_daya(Z)
suara(3)

while True:
    UI_Awal("K01")
    print("Gunakan input daya Negatif untuk akses Auto Menu")
    po = int(input("Masukkan tingkat Daya ( % ) : "))
    suara(0)
    while not po <= 100:
        po = int(input("Masukkan tingkat Daya ( % ) : "))
        suara(0)
    cook_time = 0

    if po >= 0:
        power = 30 * po // 100
        menit = int(input("Masukkan menit : "))
        suara(0)
        detik = int(input("Masukkan detik : "))
        suara(0)
        while not ((0 <= menit < 60 and 0 <= detik <= 59) or (menit == 60 and detik == 0)):
            menit = int(input("Masukkan menit : "))
            suara(0)
            detik = int(input("Masukkan detik : "))
            suara(0)
        time = menit * 60 + detik
        print(menit, "menit ", detik,  " detik dengan Daya ", po, "%", " ?", end=' ')
        pilihan_1 = str(input("Y/N "))

        while pilihan_1 != "Y" and pilihan_1 != "y" or pilihan_1 == "N" or pilihan_1 == "n":
            print("Ulangi input, tolong sesuaikan")
            print('')
            menit = int(input("Masukkan menit : "))
            suara(0)
            detik = int(input("Masukkan detik : "))
            suara(0)
            while not ((0 <= menit < 60 and 0 <= detik <= 59) or (menit == 60 and detik == 0)):
                menit = int(input("Masukkan menit : "))
                suara(0)
                detik = int(input("Masukkan detik : "))
                suara(0)
            time = menit * 60 + detik
            print(menit, "menit dan ", detik, "detik ?", end=' ')
            pilihan_1 = str(input("Y/N "))
        suara(1)
        sw = True
        manual_cook_sensor(power, cook_time, time, sw, Z)
        print(timer(time))
        suara(2)
        print("`````````````````````````````")
        print("Proses Memasak Sudah Selesai")

    else:
        print("\n" + "Anda Memasuki Zona Auto menu " + "\n")
        display_auto(0)
        pil_1 = int(input(" Masukkan Menu yang diinginkan : Baris ke - "))
        suara(0)
        pil_2 = int(input("                             : Kolom ke - "))
        suara(0)
        while not (0 < pil_1 < 6 and 0 < pil_2 < 3):
            pil_1 = int(input(" Masukkan Menu yang diingkan : Baris ke - "))
            suara(0)
            pil_2 = int(input("                             : Kolom ke - "))
            suara(0)
        suara(1)
        sw = True
        automenu(pil_1, pil_2, sw, Z)
        suara(2)
    microwave = str(input("Apakah ingin memasak lagi? Y/N" + "\n"))
    suara(0)
    if microwave != "Y" and microwave != "y" or microwave == "N" or microwave == "n":
        quit()
