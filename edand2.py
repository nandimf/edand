import string

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?', '"', '\'', ':', ';', '-', '_', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '{', '}', '[', ']', '<', '>', '/', '\\', '|', '`', '~', ' ']


def enkrip(pesan):
    global abjad

    key = input('Masukkan key   : ')
    cipher = ' '
    for i in pesan:
        k = abjad.find(i)
        k = (k + key) % 100
        cipher = cipher+abjad[k]
    else:
        cipher = cipher + i

    return cipher


def dekrip(cipher):
    global abjad
    key = input('Masukkan key  : ')

    pesan = ' '
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key) % 100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i

    return pesan


print()
print("========================================")
print("|   https://github.com/nandimf/edand   |")
print("========================================")
print()
print("========================================")
print()
print("##    #       #	      ##    #  ####    #")
print("# #   #	     # #      # #   #  #   #   #")
print("#  #  #     #   #     #  #  #  #    #  #")
print("#   # #    #######    #   # #  #    #  #")
print("#    ##   #       #   #    ##  #   #   #")
print("#     #  #         #  #     #  ####    #")
print()
print("Created By : Nandi Mirozul Fikri")
print("Untuk Enkripsi dan Dekripsi Teks dengan Metode Caesar Cipher")
print("========================================")

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?', '"', '\'', ':', ';', '-', '_', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '{', '}', '[', ']', '<', '>', '/', '\\', '|', '`', '~', ' ']


def enkripsi(abjad):
    str = input("Masukan Teks : ")
    key = int(input("Masukan Key/Kunci (Number/nomor) : "))

    str = str.lower()
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n - key) % 95
            convert = abjad[encrypt]
            result = result + convert
        else:
            result = result + ''

    print(f"Text TerEnkripsi : {result}")


def dekripsi(abjad):
    str = input("Masukan Teks : ")
    key = int(input("Masukan Key/Kunci (Number/nomor) : "))

    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            decrypt = (n + key) % 95
            convert = abjad[decrypt]
            result = result + convert
        else:
            result = result + 'null'

    print(f"Text TerDekripsi : {result}")


pilihan = 'y'

while (pilihan == 'y'):
    print("Menu Pilihan : ")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    menu = input("Menu Yang Di Pilih (number atau nomor) : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(abjad)
    elif menu == '3':
        print("Program Anda Telah Keluar")
        break
    else:
        print("Menu Tidak Ditemukan")

    print("----------------------------------------")
    pilihan = input("Apakah Ingin Melanjutkan ? (y/n) ")
    print("----------------------------------------")
