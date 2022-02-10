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






