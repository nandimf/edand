import string
from random import choice
from colorama import Fore, Style, init


colorList = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.GREEN, Style.BRIGHT + Fore.YELLOW,
             Style.BRIGHT + Fore.BLUE, Fore.MAGENTA, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.WHITE, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.WHITE]


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


init()
print(choice(colorList) +
      f"""
      https://github.com/nandimf/edand
{choice(colorList)}
##    #       #	      ##    #  ####    #
# #   #	     # #      # #   #  #   #   #
#  #  #     #   #     #  #  #  #    #  #
#   # #    #######    #   # #  #    #  #
#    ##   #       #   #    ##  #   #   #
#     #  #         #  #     #  ####    #
{choice(colorList)}Created by: {choice(colorList)}Nandi Mirozul Fikri{choice(colorList)}
{choice(colorList)}Untuk Enkripsi dan Dekripsi Teks{choice(colorList)} Metode Caesar Cipher {choice(colorList)}
\n""")

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?', '"', '\'', ':', ';', '-', '_', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '{', '}', '[', ']', '<', '>', '/', '\\', '|', '`', '~', ' ']


def enkripsi(abjad):
    str = input(choice(colorList) + "Masukan Teks : " + choice(colorList))
    key = int(input(choice(colorList) +
                    "Masukan Key/Kunci (Number/nomor) : " + choice(colorList)))
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n - key) % 95
            convert = abjad[encrypt]
            result = result + convert
        else:
            result = result + 'null'

    print(f"Text TerEnkripsi : {result}" + choice(colorList))


def dekripsi(abjad):
    str = input(choice(colorList) + "Masukan Teks : " + choice(colorList))
    key = int(input(choice(colorList) +
                    "Masukan Key/kunci (Number/nomor) : " + choice(colorList)))

    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            decrypt = (n + key) % 95
            convert = abjad[decrypt]
            result = result + convert
        else:
            result = result + 'null'

    print(f"Text TerDekripsi : {result}" + choice(colorList))


pilihan = 'y'


while (pilihan == 'y'):
    print(choice(colorList) + "Menu Pilihan : ")
    print(choice(colorList) + "1. Enkripsi")
    print(choice(colorList) + "2. Dekripsi")
    print(choice(colorList) + "3. Keluar")

    menu = input(choice(colorList) +
                 "Menu Yang Di Pilih (number atau nomor) : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(abjad)
    elif menu == '3':
        print("Program anda Telah Keluar")
        break
    else:
        print("Menu Tidak Ditemukan")

    print("----------------------------------------")
    pilihan = input(choice(colorList) + "Apakah Ingin Melanjutkan ? (y/n) ")
    print("----------------------------------------")
