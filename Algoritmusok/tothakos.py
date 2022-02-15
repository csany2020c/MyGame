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
    #print(osszeg)
    #print(szorzat)
    #print(darab)

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
    szamfele: int = szam // 2
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
        return osszeg
#print(osztoosszeg(int(input())))

def baratszamok(a: int, b: int) -> bool:
    a: int = 0
    b: int = 0
    for x in range():
        if a % x == 0:
            a = a+x
        if b % x == 0:
            b = b+x
        if a == b:
            return True
#print(baratszamok(int(input())))

def hatvany(c: int, d: int)-> List[int]:
    hatvanylista = list()
    for x in range():
        c *= c

def feladat00(lista1: List['int'], oszto: int) -> List['int']:
    lista: list = []
    for i in lista1:
        if i % oszto == 0:
            lista.append(i)

    return lista

#print(feladat00((1,2,3,4,5,6), 3))

def feladat01(lista: List['int']) -> bool:
    for i in lista:
        if i == 0:
            return True

#print(feladat01((0,1,2,3)))

def feladat1(szam1:int, szam2:int) -> int:
    if szam1 < szam2:
        return szam1
    else:
        szam2
#print(feladat1(3,9))

def feladat2(lista: List['int']) -> int:
    x: int = lista[1]
    for i in lista:
        if x > i:
            x = i
        return x
#print(feladat2((100,600,20,1000,10340,1024)))

#def fealadat3(a: int, q: int, n:int) -> List['int']:

def feladat4(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x
#print(feladat4((1,2,4,8,16,32,64,128,256)))

#def feladat5():

def feladat6(a: float, b:float, c:float) -> List['int']:
    lista: list = [1]

