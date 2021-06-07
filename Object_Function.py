def objek(ob: bool):
    lampu = ob
    meja = ob
    return ob


def cook(co: bool):
    magnetron = co
    objek(co)
    return magnetron


def sensor_uap(su: int, am: int):
    if su < am:
        uap = cook(True)
    else:
        uap = cook(False)
    return uap


def sensor_switch(sw: bool):
    cook(sw)
    return sw


def sensor_daya(imp: int):
    if imp == 0:
        quit()


def suara(sr: int):
    tombol = "(ini file untuk suara tombol)"
    masak_mulai = "(ini file untuk suara masak mulai)"
    masak_selesai = "(ini file untuk suara masak selesai)"
    daya = "(ini file untuk suara daya)"
    noise = [tombol, masak_mulai, masak_selesai, daya]
    sound = noise[sr]
    return sound


def automenu(baris: int, kolom: int, sw, Z):
    auto = [["Daftar Automenu", "Time dan Power 1", "Time dan Power 2"],
            ["Autocook", "ikan/daging", "lasagna"],
            ["Defrost", "450 gram", "900 gram"],
            ["Popcorn", "1 porsi", "2 porsi"],
            ["Melting Butter", "125 gram", "250 gram"],
            ["Quick Heating", "Sup", "Nasi"]]
    print("")
    print(auto[baris][0] + " " + auto[baris][kolom])
    if baris == 1:
        if kolom == 1:
            po = 80
        else:
            po = 60
        su = 0
        am = 100
        power = 30 * po // 100
        cook_time = 0
        sensor_uap(su, am)
        while sensor_uap(su, am) is True:
            if sensor_switch(sw) is False:
                quit()
            sensor_daya(Z)
            if cook_time < power:
                cook(True)
                if cook_time % 3 == 2:
                    su += 3
                cook_time += 1
                sensor_uap(su, am)
            elif cook_time < 30:
                cook(False)
                cook_time += 1
                if cook_time == 30:
                    cook_time = 0
        auto_cooK_timer(0)
        print("Proses Auto Cook Selesai")
    elif baris == 2:
        po = 30
        power = 30 * po // 100
        if kolom == 1:
            time = 9 * 60
        else:
            time = 18 * 60
        cook_time = 0
        timer(time)
        for i in range(1, time+1):
            if sensor_switch(sw) is False:
                quit()
            sensor_daya(Z)
            if cook_time < power:
                cook(True)
                cook_time += 1
            elif cook_time < 30:
                cook(False)
                cook_time += 1
                if cook_time == 30:
                    cook_time = 0
        print("Proses Auto Defrost Selesai")
    elif baris == 3:
        po = 100
        if kolom == 1:
            time = 5 * 60
        else:
            time = 10 * 60
        cook_time = 0
        su = 0
        am = 100
        timer(time)
        for i in range(1, time+1):
            power = 30 * po // 100
            if sensor_switch(sw) is False:
                quit()
            sensor_daya(Z)
            if sensor_uap(su, am) is True:
                if cook_time < power:
                    cook(True)
                    cook_time += 1
                    if cook_time % 2 == 0:
                        su += 1
                elif cook_time < 30:
                    cook(False)
                    cook_time += 1
                    if cook_time == 30:
                        cook_time = 0
                if su >= 80:
                    po = 80
            else:
                break
        print("Proses Auto Popcorn Selesai")
    elif baris == 4:
        po = 20
        su = 0
        if kolom == 1:
            am = 50
        else:
            am = 100
        power = 30 * po // 100
        cook_time = 0
        sensor_uap(su, am)
        while sensor_uap(su, am) is True:
            if sensor_switch(sw) is False:
                quit()
            sensor_daya(Z)
            if cook_time < power:
                cook(True)
                if cook_time % 3 == 2:
                    su += 5
                cook_time += 1
                sensor_uap(su, am)
            elif cook_time < 30:
                cook(False)
                cook_time += 1
                if cook_time == 30:
                    cook_time = 0
        auto_cooK_timer(0)
        print("Proses Auto Melting Butter Selesai")
    elif baris == 5:
        po = 100
        su = 0
        am = 50
        if kolom == 2:
            po = 80
            am = 100
        power = 30 * po // 100
        cook_time = 0
        sensor_uap(su, am)
        while sensor_uap(su, am) is True:
            if sensor_switch(sw) is False:
                quit()
            sensor_daya(Z)
            if cook_time < power:
                cook(True)
                if cook_time % 3 == 2:
                    su += 5
                cook_time += 1
                sensor_uap(su, am)
            elif cook_time < 30:
                cook(False)
                cook_time += 1
                if cook_time == 30:
                    cook_time = 0
        auto_cooK_timer(0)
        print("Proses Auto Quick Heating Selesai")
    return


def timer(z):
    print("`````````````````````````````")
    print("Sedang Memasak ~")
    print(z, "detik", " ~ ")
    if z <= 300:
         while z > 10:
            z -= 10
            print(z, "detik", " ~ ")
    elif z > 300:
        while z > 100:
            z -= 100
            print(z, "detik", " ~ ")
    return ("Waktu Habis")


def manual_cook_sensor(daya, W_masak, waktu, sw, Z):
    for i in range(1, waktu+1):
        if sensor_switch(sw) is False:
            quit()
        sensor_daya(Z)
        if W_masak < daya:
            cook(True)
            objek(True)
            W_masak += 1
        elif W_masak < 30:
            cook(False)
            objek(False)
            W_masak += 1
            if W_masak == 30:
                W_masak = 0
    return ' '


def auto_cooK_timer(act):
    print("`````````````````````````````" + "\nMakanan Sedang disiapkan" + "\nAnda hanya diminta untuk menunggu ")
    print("")
    print("Tunggu ~~~~~~~~~~~~~~" + "\nTunggu ~~~~~~~~~~~~~~~~~~~" + "\nTunggu ~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("Uap Terdeteksi oleh Sensor " + "\n````````````````````````````")
    return
