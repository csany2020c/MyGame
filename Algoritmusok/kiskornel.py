from typing import List
import math

def valami():
    while True:
        valami: int = int(input())

        if valami == 0:
            break





def valami2():
    szam: int = 1
    szam2: int = 0

    while (szam != 0):
        szam = int(input())

        if szam != 0:
            szam += szam2
    #print(szam2)





def listaz():
    lista: List['int'] = (4, 2, 3)
    szorzat: int = 1
    for i in lista:
        szorzat *= i
        #print("Eredmény: {dsa}".format(dsa=szorzat))






def osztoosszeg(sz: int) -> int:
    szamfele: int = sz // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if sz % x == 0:
            osszeg = osszeg + x
    return osszeg
#print(osztoosszeg(int(input())))
#print(osztoosszeg(16))
#print(osztoosszeg(21))

def baratsagosszamok(sz: int, sz2: int) -> bool:
    return sz != sz2 and osztoosszeg(sz) == sz2 and osztoosszeg(sz2) == sz

#print(baratsagosszamok(6, 6))
#print(baratsagosszamok(332,123))
#print(baratsagosszamok(220, 284))
#print(baratsagosszamok(319550, 430402))


def hatvany(alap: int, kitevo: int) -> List['int']:
    lista : list = []
    szorzat: int = 1
    for i in range(0, kitevo + 1):
        lista.append(szorzat)
        szorzat *= alap
    return  lista

#print(hatvany(2, 8))
#print(hatvany(3, 4))

def feladat1(lista: List['int'], szam: int) -> List['int']:
    lista2: list = []
    for x in lista:
        if x % szam == 0:
            lista2.append(x)
    return lista2

#print(feladat1((1,2,3,4,5,6,7,8), 2))

def feladat2(lista: List['int']) -> bool:
    if lista == 0:
        print("True")
    else:
        print("False")

#print(feladat2(0))

def feladat3min(sz1: int, sz2: int) -> int:
    if sz1 < sz2:
        return sz1
    if sz2 <sz1:
        return sz2
#print(feladat3(3, 2))

def feladat4minlist(lista: List['int']) -> int:
    x: int = lista[1]
    for i in lista:
        if i < x:
            x = i
    return x

#print(feladat4minlist((4,200,30,31,5,6,7,8,9)))

def feladat5(a1: int, q: int, n: int) -> List['int']:
    lista: list = []
    for i in range(n):
        x = a1 * q ** (i)
        lista.append(x)
    return lista

#print(feladat5(1, 2 ,4))

def feladat6(lista: List['int']) -> int:
    x: int = 0
    for i in lista:
        x += i
    return x

#print(feladat6((1,2,3)))

def feladat7(a: int, q: int, n: int) -> int:
    return feladat6(feladat5(a, q, n))
#print(feladat7(3, 5, 9))

def feladat8(a: float, b: float, c: float) -> List['float']:
    kilista: List['float'] = list()
    D: float = b*b - 4 * a * c
    if D >= 0:
        kilista.append((-b + math.sqrt(D)) / 2 * a)
    if D > 0:
        kilista.append((-b - math.sqrt(D)) / 2 * a)
    return kilista


#print(feladat8(3,7,4))

def tokeletesszamok(sz: int,) -> bool:
    oszt: int = sz // 2 + 1
    osszeg: int = 0
    for i in range(1, oszt):
        if sz % i == 0:
            osszeg = osszeg + i
    if osszeg == sz:
        return True
    else:
        return False

#print(tokeletesszamok(2))

def felbontas(sz: int) -> List['int']:
    lista: List['int'] = []
    if sz == 0:
        lista.append(0)
    while sz > 0:
        lista.append(sz % 10)
        sz = sz // 10
    lista.reverse()
    return lista

#print(felbontas(254))

def szamjegyekosszege(sz: int) -> int:
    osszeg: int = 0
    for i in felbontas(sz):
        osszeg += i
    return osszeg
#print(szamjegyekosszege(523))

def szamjegyekszorzata(sz: int) -> bool:
    szorzas: int = 1
    for i in felbontas(sz):
        szorzas*=i
    if szorzas == sz:
        return True
    else:
        return False

#print(szamjegyekszorzata())

def primek(sz: int):
    if sz == 1: return False
    gyokpluszegy = int(math.sqrt(sz)) + 1
    for i in range(2, gyokpluszegy):
        if sz % i == 0:
            return False
    return True
#print(primek(7))
def Mersenneszam(a: int):
    return 2 ** a -1

def Mersenneprim(n: int):
    return primek(n) and primek(Mersenneszam(n))

#print(Mersenneprim())

def tizenot(sz: int) -> int:
    szam = 0
    for i in range(100, 1000):
        if szamjegyekosszege(sz) == 15 and sz % 15 == 0:
            szam += 1
    return szam
print(tizenot())