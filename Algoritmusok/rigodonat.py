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


def listababeolvas() -> List['int']:
    visszaadottlista = list()
    szam: int = 1
    while (szam != 0):
        szam = int(input())
        if szam != 0:
            visszaadottlista.append(szam)
    return visszaadottlista



#l: List['int'] = (4, 2, 3)
#print(l)
#print(szorzat(l))

#l2 = listababeolvas()
#print(l2)
#print(szorzat(l2))

def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

#print(osztoosszeg(12))
#print(osztoosszeg(16))
#print(osztoosszeg(21))

def baratszame(a: int, b: int)-> bool:
    szamfelea:  int = a // 2 + 1
    szamfeleb:  int = b // 2 + 1
    osszega: int = 0
    osszegb: int = 0
    for y in range(1, szamfelea):
        if a % y ==0:
            osszega = osszega + y
    for y in range(1, szamfeleb):
        if b % y ==0:
            osszegb = osszegb + y
    if osszega !=b and osszegb !=a or a == b:
        return False
    else:
        return True

print(baratszame(220,284))
print(baratszame(6,6))
print(baratszame(1184,1210))

def feladat00(lista1: List['int'], oszto: int) -> List['int']:
    lista2: list = []
    for i in lista1:
        if i % oszto == 0:
            lista2.append(i)

    return lista2


#print(feladat00((1,2,3,4,5,6), 3))


def feladat01(lista: List['int']) -> bool:
    for i in lista:
        if i == 0:
            return True

#print(feladat01((0,1,2,3)))

def feladat1_min(szam1:int, szam2:int) -> int:
    if szam1 < szam2:
        return szam1
    else:
        return szam2

#print(feladat1_min(3,9))

def feladat2_minlist(lista: List['int']) -> int:
    x: int = 10000000000000000000000000000000000
    for i in lista:
        if x > i:
            x = i
    return x

#print(feladat2_minlist((100,600,200,1000)))


def feladat4_osszeg(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x

print(feladat4_osszeg((1,2,4,8,16)))









