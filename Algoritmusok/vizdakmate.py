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






#l: List['int'] = (4, 2, 3)
#print(l)
#print(szorzat(l))


def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg


def baratiszamok(a: int, b: int)-> bool:
    szama: int = 0
    szamb: int = 0
    for x in range():
        if szama % x == szama + x:
            osszeg = szama + x
        if szamb % x == szamb + x:
            osszeg = szamb + x
  #  return

#def hatvany(a: int, b:int) -> List['int']:
 #   visszadottlista = list()
  #  szam: int = 1
   # while (szam != 1):
    #    szam = int(input())
 #       if szam != 0:
  #          visszaadottlista.append(szam)
    #return visszaadottlista

   # print()


def tokeletes(szam: int) -> int:
    szam1: int = szam
    osszeg: int = 0
    for x in range(1, szam1):
        if szam % x == 0:
            osszeg = osszeg + x
       # return osszeg
    if osszeg == szam:
        return True
    else:
        return False

#print(tokeletes(42))

def parameter(szam: int) -> bool:
    osszeg: int = 0
        for i in range(1, szam):
            if osszeg == szam:

print(parameter(22))