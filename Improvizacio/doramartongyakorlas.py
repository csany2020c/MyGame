from typing import *
from random import randint

def elso():
    szam1 = int(input())
    szam2 = int(input())
    szam3 = int(input())
    print("legnagyobb szám: {a}".format(a=max(szam1, szam2, szam3)))

#elso()

def masodik():
    lista: list = [1, 2, 3, 4, 5, 6, 7, 8]
    osszeg: int = 0
    szamok: int = 0
    for i in lista:
        osszeg += i
        szamok = i
    atlag: int = osszeg / szamok
    for i in lista:
        if i < atlag:
            print(i)
#masodik()

#def harmadik():
    #???

def negyedik():
    while True:
        szam = int(input())
        if szam % 21:
            print("butavagy")
            pass
        else:
            print("jej")
            break

#negyedik()

def ototdik():
    szam1 = int(randint(0, 127))
    while True:
        szam2 = int(input())
        if szam1 > szam2:
            print("ez a szám túl kicsi")
            pass
        else:
            print("ez a szám túl nagy")
            pass
        if szam1 == szam2:
            print("eltaláltad!")
            break

ototdik()