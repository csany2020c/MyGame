from typing import List
import math

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

#print(baratszame(220,284))
#print(baratszame(6,6))
#print(baratszame(1184,1210))

def hatvanyok(alap: int, kitevo: int) -> List['int']:
    hatvanyoklista: list = []
    szorzat: int = 1
    for i in range(0, kitevo + 1):
        hatvanyoklista.append(szorzat)
        szorzat *= alap
    return hatvanyoklista



def feladat0(lista1: List['int'], oszto: int) -> List['int']:
    lista2: list = []
    for i in lista1:
        if i % oszto == 0:
            lista2.append(i)

    return lista2


#print(feladat0((1,2,3,4,5,6), 3))


def feladat01(lista: List['int']) -> bool:
    for i in lista:
        if i == 0:
            return True

#print(feladat01((0,1,2,3)))

def feladat1(szam1:int, szam2:int) -> int:
    if szam1 < szam2:
        return szam1
    if szam2 < szam1:
        return szam2


#print(feladat1(2,5))

def feladat2(lista : List['int']) -> int:
    x = int = lista[1]
    for i in lista:
        if x > i:
            x = i
    return x

#print(feladat2((4444,2345,224,22345,111,5663,44)))

def feladat3(a1:int, q:int, n:int) -> List['int']:
    lista: List['int'] = list()
    for i in range(1, n+1):
        x = a1 * q**(i-1)
        lista.append(x)
    return lista


#print(feladat3(1,2,2))


def feladat4(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x

#print(feladat4((5,3,6,9,11)))

def feladat5(a:int, q:int, n:int) -> int:
    osszeg: int = feladat4(feladat3(a , q , n))
    return osszeg

#print(feladat5(1,2,2))


def feladat6(a: float, b: float, c: float) -> List['float']:
    kilista: List['list'] = list()
    D: float = b * b - 4 *a * c
    if D >= 0:
        kilista.append((-b + math.sqrt(D)) / (2 * a))
    if D > 0:
        kilista.append((-b - math.sqrt(D)) / (2 * a))
    return kilista

#print()

#HF2____________________________________________________________________________________________________________________

def tokeletesszam(szam: int) -> bool:
    összeg: int = 0
    oszto: int = szam // 2
    for x in range(1, oszto + 1):
        if szam % x == 0:
            összeg += x
    if összeg == szam:
        return True
    else:
        return False

#print(tökeletesszam(28))

def tokeletesszamlista(min: int, max: int) -> List['int']:
    lista : List['int'] = []
    for i in range(min, max):
        if tokeletesszam(i):
            lista.append(i)

    return lista

#print(tokeletesszamlista(1,555))

def tizesfelbontas(szam: int) -> List['int']:
    lista: List['int'] = []
    for i in str(szam):
        lista.append(int(i))
    return lista

#print(tizesfelbontas(1120))


def szamjegyekosszege(szam: int) -> int:
    osszeg = 0
    for i in (tizesfelbontas(szam)):
        osszeg +=i

    return  osszeg

#print(szamjegyekosszege(1102))

def szamjegyszorzas(szam: int) -> bool:
    szorzat = 1
    for i in (tizesfelbontas(szam)):
        szorzat *= int(i)
    if szorzat == szam:
        return True
    else:
        return False

#print(szamjegyszorzas(1))

def haromjegyutizenot() -> int:
    db = 0
    for i in range(100,1000):
        if i % 15 == 0 and szamjegyekosszege(i) == 15:
            db += 1
    return db

#print(haromjegyutizenot())

def armstrongszamharom() -> List['int']:
    lista: List = []
    for x in range(100, 1000):
        osszeg = 0
        for i in tizesfelbontas(x):
            osszeg += i ** 3
        if osszeg == x:
            lista.append(osszeg)
    return lista

#print(armstrongszamharom())

#^hibás!!!

#HF3____________________________________________________________________________________________________________________

def prim(szam: int) -> bool:
    if szam == 1: return False
    gyokmegegy = int(math.sqrt(szam)) + 1
    for i in range(2, gyokmegegy):
        if szam % i == 0:
            return False
    return True

#print(prim(4))

def mersenneszam(n: int):
    return 2**n -1

def mersenneprim(hatvany: int) -> bool:
    return prim(hatvany) and prim(mersenneszam(hatvany))

#print(mersenneprim(5))

def mersenneprimkeres(a: int) -> List['int']:
    lista: List['int'] = []
    for i in (a):
        if mersenneprim(i) == True:
            lista.append(i)
    return lista

#print(mersenneprimkeres())

def fibonacci(n: int) -> List['int']:
    if n == 0: return []
    if n == 1: return [0]
    lista: List = [0, 1]
    for i in range(2, n):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista

#print(fibonacci(20))

def legkisebbkozostobbszoros(a: int, b: int) -> int:
    szam: 0
    if a % b == 0:
        szam = a
    if b % a == 0:
        szam = b
    if b % a and a % b !=0:
        szam = a * b
    return  szam

#print(legkisebbkozostobbszoros(4,7))

def legnagyobbkozososzto(a: int, b: int) -> int:
    szam = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            if szam < i:
                szam = i
    return szam

#print(legnagyobbkozososzto(433,866))

def szfenikus()
