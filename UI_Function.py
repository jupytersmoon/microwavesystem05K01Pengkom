def UI_Awal(x):
    Pembuka = "Microwave " + str(x) + "\n " + "\nTimer and Power"
    pola = "*"
    print(Pembuka)
    for i in range(5):
        for j in range(11):
            if j == 0 or i == 0 or j == 10 or i == 4:
                print(pola, end="  ")
            else:
                print(" ", end='  ')
        print(' ')

    tombol = [[0 for j in range(4)] for i in range(3)]; angka = 0
    for i in range(3):
        for j in range(3):
            angka += 1; tombol[i][j] = angka

    tombol[2][3] = "Cook"; tombol[1][3] = "Auto"

    for i in range(3):
        for j in range(4):
            print(" | " + str(tombol[i][j]) + " | " + " ", end='')
        print('')
    print('')
    return

def display_auto(x):
    auto = [["Daftar Automenu", "Time dan Power 1", "Time dan Power 2"],
            ["Autocook       ", "ikan/daging     ", "lasagna         "],
            ["Defrost        ", "450 gram        ", "900 gram        "],
            ["Popcorn        ", "1 porsi         ", "2 porsi         "],
            ["Melting Butter ", "125 gram        ", "250 gram        "],
            ["Quick Heating  ", "Sup             ", "Nasi            "]]

    display = [[0 for j in range(3)] for i in range(6)]
    for i in range(6):
        for j in range(3):
            display[i][j] = str(auto[i][j])
            print("| "+str(display[i][j]) + " | " + " ", end='')
        print('')
    print('')
