import math
from typing import List
from time import time
from math import *

# Írassa ki a számokat 1-től 42-ig egyesével növekvően.
def egytolnegyvenkettoig():
    for i in range(1, 43):
        print(i)


# Olvasson be a billentyűzetről számokat addig, amíg 0-át nem írunk be.

def beolvasasvegjelig():
    # Fusson "örökkés" a ciklus.
    while (True):
        # Olvassunk be egy stringet a billentyűzetről, majd alakítsuk át egész számmá.
        # Az átalakított értéket tároljuk el a SZAM változóban.
        szam: int = int(input())

        if szam == 0:
            break


# Olvasson be a billentyűzetről számokat addig, amíg 0-át nem írunk be.

def beolvasasvegjelig2():
    # A SZAM vátozóban tároljuk a beolvasott értéket. Kezdetben egy olyan értéket kap
    # amivel a ciklusba beugrik. (Ha 0 lenne soha nem lépne be.)
    szam: int = 1
    while (szam != 0):
        # Beolvassa az értéket. Először stringként, majd int-re konvertálja.
        szam = int(input())
        # A ciklusmag végén visszadobja a feltételhez, amennyiben a beírt érték 0,
        # nem fut le újra a ciklus


# Olvasson be számokat 0 végjelig és a végjel után írja ki az összegüket.
def osszegzesvegjelig():
    # Létre kell hozni egy változót, amelynek az értéke kezdetben 0,
    # majd a későbbiekben ezt fogjuk növelni a beírt számokkal.
    osszeg: int = 0
    szam: int = 1
    while (szam != 0):
        szam = int(input())
        # Amennyiben a beírt szám nem 0, növeljük az összeg értékét a számmal.
        if szam != 0:
            osszeg += szam
            print("Az eddigi összeg: {sum}".format(sum=osszeg))
    print("Az összeg: {sum}".format(sum=osszeg))


# Készítsen egy listát, amelyben egész számokat tárol. Ennek a listának az
# elemeinek az összegét számolja ki, majd írja ki.

def osszegzeslistaban():
    lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
    osszeg: int = 0
    for i in lista: # Az i értékei: 6,5,9,3,1,2,3 (lista elemek)
        #print(i)
        osszeg += i
    print("Az összeg: {sum}".format(sum=osszeg))

# Készítsen egy listát, amelyben egész számokat tárol. Ennek a listának az
# elemeinek az összegét számolja ki, majd írja ki.

def osszegzeslistaban2():
    lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
    osszeg: int = 0
    for i in range(0, len(lista)): # Az i értékei: 0,1,2,3,4,5,6 (lista indexek)
        #print(i)
        osszeg += lista[i]
    print("Az összeg: {sum}".format(sum=osszeg))

# Készítsen függvényt, amelynek bemenete egy számokat tartalmazó lista,
# és a visszaadott értéke pedig a számok összege.
# Készítsen tesztet is.

# A függvény bemenetei a zárójelbe kerülnek. A kimenetének a típusát a -> után kell definiálni.
# A return után olyan típus jön, amit itt meghatároztunk.
def osszegzes(lista: List['int']) -> int:
    osszeg: int = 0
    for i in lista:  # Az i értékei: 6,5,9,3,1,2,3 (lista elemek)
        osszeg += i
    # A visszatérési értéket a függvény hívásának a helyén tudjuk majd felhasználni.
    return osszeg
# Teszt:
#lista: List['int'] = (6, 5, 9, 3, 1, 2, 3)
# A függvény paraméterként kapja meg a listát, majd a visszaadott értékét a print kapja meg.
#print(osszegzes(lista))
# Ugyan az, csak a lista a függvény paraméterében van létrehozva.
#print(osszegzes((4, 7, 8, 4)))

def fakt(n: int) -> int:
    print("Fakt {c} ".format(c=n))
    szorzat = 1
    for i in range(2, n + 1):
        szorzat *= i
    return szorzat

# for i in range(0, 1024):
#    print(fakt(i))

# x = fakt(2) + fakt(3) * 100
# print(x)

# https://www.w3schools.com/python/python_operators.asp

#print(8 % 3)
#print(100 % 33)
#if 100 % 33 == 0:


# Készítsen függvényt, amelynek bemenete egy szám és egy listában adja vissza
# a számnak az osztóit.

def osztok(n: int) -> List['int']:
    l: List['int'] = list()
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l


# print(osztok(26))
# for i in osztok(26):
#     print(i)

# https://hu.wikipedia.org/wiki/Pr%C3%ADmsz%C3%A1mok
# Készítsen függvényt, amelynek bemenete egy szám, és a kimenete logikai.
# A kimenete legyen igaz, amennyiben prímszám a bemenete.
# Prímszámnak pontosan két osztója van, 1 és önmaga. A 0 és 1 nem prímszám.

def prim(be: int) -> bool:
    return len(osztok(be)) == 2


# for i in range(0, 128):
#     print("{szam} {prim}".format(szam=i, prim=prim(i)))

def primszam_Boldizsar(inputxd: int) -> bool:
    idk = 0
    osztodarab = 0
    for i in range(inputxd):
        idk = idk + 1
        eredmeny = inputxd % idk
        # print(eredmeny)
        if eredmeny == 0:
            osztodarab = osztodarab + 1
        if osztodarab > 2:
            return False
            #print("Ez nem prímszám")
            break
    if osztodarab == 2:
        return True
        # print("Prímszám")

#HF: A prim(i) függvényt cseréljék le saját prímszám függvényre, amely jobb hatásfokkal
# működik. A leggyorsabb algoritmus készítője 5-öst kap. Max RAM használat 24 GB.


def primszamgyors(szam: int) -> bool:
    gyok: int = int(math.sqrt(szam))
    for i in range(2, gyok):
        if szam % i == 0:
            return False
    return True


#
# ts1 = time()
# for i in range(1, 101000):
#     #primszame = prim(i) # Prímszám eldöntő függvény helye
#     #primszame = primszamgyors(i)
#     primszame = primszam_Boldizsar(i)
#     # if primszame:
#     #     print(i)
# ts2 = time()
# print("Az algoritmus {mp} másodpercig futott.".format(mp=(ts2 - ts1)))


# https://wiki.python.org/moin/BitwiseOperators
#
# 1 == igaz; 0 == hamis
#      10110111
#    & 11010001
#    ----------
#      10010001

#      10110111
#    >>       1
#---------------
#      01011011
#
#  x=0b 0101 1011
#  h=0x   5    B
# https://towardsdatascience.com/binary-hex-and-octal-in-python-20222488cee1
# https://slidetodoc.com/presentation_image/c38ff823e30ffb14271c6e0e604b1b10/image-21.jpg

def binaris_maszkolassal(szam: int) -> str:
    s: str = ""
    for i in range(0, 32):
        if (szam & 0x80000000) == 0:
            s += "0"
        else:
            s += "1"
        szam <<= 1
        print(szam)
    return s

def binary_osztassal(be: int) -> str:
    bemenet = abs(be)
    kimenet: str = ""
    while 0 < bemenet:
        if bemenet % 2 == 0:
            kimenet = "0" + kimenet
        else:
            kimenet = "1" + kimenet
        bemenet = bemenet // 2
    if kimenet == "":
        return "0"
    # return string[::-1]
    if be < 0:
        return "-" + kimenet
    return kimenet

# print(binaris_maszkolassal(255))

# Készítsen függvényt, melynek bemenete egy
# számokból álló lista,
# a kimenete szintén egy ugyan ilyen lista,
# de az csak a páros számokat tartlamazza
# azok közül, amik a bemeneten voltak.

# def függvénynév(bemeneteket kell írni) -> kimenet típusát, mert a kimenet neve a függvény neve
def parosak(belist: List['int']) -> List['int']:
    # Elő kell állítani a kimenetre kerülő adatokat tartalmazó listát
    kilist: List['int'] = list()
    # Végigjárja a bemeneti listát
    for i in belist:
        # Ha a listaelem (i) 2-vel való osztással képzett maradéka egyenlő 0-val, akkor...
        if i % 2 == 0:
            # ...hozzáfűzi a kimeneti listához.
            kilist.append(i)
    # A kimeneti listát vissza kell adni a hívás helyének.
    return kilist


# l3 = [3, 6, 8, 2, 3, 1, 4]
# l9 = [333, 4, 0, 44]
# l7 = [3]
# l4 = parosak(l3)
# l5 = parosak(l9)
# print(l4)
# print(l5)
# print(parosak(l7))
# print(parosak([]))
# print(parosak([2, 6, 8, 9]))

# Készítsen függvényt, amelynek bemenete egy szám, és
# a kimenete egy olyan lista, amely 0-tól a bemeneteként
# megadott számig 1-esével beleteszi az összes számot
# a kimeneti listába.
# Negatív értékre is működjön.
# Pl: be: 6 ki: [0,1,2,3,4,5,6]
# Pl: be: -6 ki: [0, -1, -2, -3, -4, -5, -6]

def szamolas(be: int) -> List['int']:
    kilist: List['int'] = list()
    if be < 0:
        for i in range(0, be - 1, -1):
            kilist.append(i)
    else:
        for i in range(0, be + 1):
            kilist.append(i)
    return kilist

# print(szamolas(6))
# print(szamolas(-6))
# print(szamolas(0))


# Az előző függvények felhasználásával készítsen egy
# függvényt, amelynek bemenete egy szám, és 0-tól
# kezdve a páros számokat addig a számíg kiírja.
# A megoldás 1-2 sor lehet csak!
