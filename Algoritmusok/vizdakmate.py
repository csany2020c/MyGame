from typing import List

def Szamok1tol15ig():
    for i in range(1, 16):
        print(i)


def beolvasasvegjelig():
    while True:
        valami: int = int(input())
        if valami == 0:
            break



def beolvasasvegjelig2():

    szam: int = 1
    while (szam != 0):

        szam = int(input())


def szamok():
    beolvasas: int = 1
    osszeg: int = 0
    szorzat: int = 1
    darab: int = 0
    while (beolvasas != 0):
        beolvasas = int(input())
        if beolvasas != 0:
            osszeg += beolvasas
            szorzat *= beolvasas
            darab += 1

    print(osszeg)
    print(szorzat)
    print(darab)

def szorzat(lista: List['int']) -> int:
    sz: int = 1
    for i in lista:
        sz *= i

    return sz






l: List['int'] = (4, 2, 3)
print(l)
print(szorzat(l))