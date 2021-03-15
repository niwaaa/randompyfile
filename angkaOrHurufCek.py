class const:
    HURUF = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ANGKA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1', '2',
             '3', '4', '5', '6', '7', '8', '9', '0', ]


def cekAngka(txt):
    angka = const.ANGKA
    for x in txt:
        counter = False
        for y in angka:
            if(x == y):
                counter = True
        if counter == True:
            print("ini angka")
        else:
            print("ini bukan angka")


def cekHuruf(txt):
    huruf = const.HURUF
    for x in txt:
        counter = False
        for y in huruf:
            if(x == y):
                counter = True
        if counter == True:
            print("ini huruf")
        else:
            print("ini bukan huruf")


cekAngka('123')
cekHuruf("as1")
