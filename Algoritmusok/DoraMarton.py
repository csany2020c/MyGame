import math
from typing import List


def szamolas():
    for i in range(1, 16):
        print(i)


def beolvasasvegjelig():
    while True:
        valami: int = int(input())
        if valami == 0:
            break


def szamok():
    szam: int = 1
    osszeg: int = 0
    szorzat: int = 1
    db: int = 0
    while szam != 0:
        szam = int(input())
        if szam != 0:
            osszeg += szam
            szorzat = szorzat * szam
            db += 1

    print(osszeg)
    print(szorzat)
    print(db)


def woohoo():
    list: List['int'] = (4, 2, 3)
    szorzat: int = 1
    for i in list:
        szorzat *= i
    print(szorzat)

def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg


def hazifeladat00(lista: List['int'], b: int) -> List['int']:
    listar: list = []
    for i in lista:
        if i % b == 0:
            listar.append(i)
    return listar

#print(hazifeladat00((1, 2, 3, 4), 2))

def hazifeladat01(lista1: List['int']) -> bool:
   for i in lista1:
       if i == 0:
           print('Igaz')
       else:
           print('Hamis')

#print(hazifeladat01((0, 1, 2, 3)))

def hazifeladat1(a: int, b: int) -> int:
    if a > b:
        print(b)
    else:
        print(a)

#print(hazifeladat1(200, 50))

def minlist(lista: List['int']) -> int:
    x: int = lista[1]
    for i in lista:
        if i < x:
            x = i
    return x

#print(minlist((35, 20, 5, 21)))

def feladat3(a1: int, q: int, n: int) -> List['int']:
    lista: list = []
    for i in range(n):
        x = a1 * q**(i)
        lista.append(x)
    return lista

# print(feladat3(3, 2, 4))

def feladat4(listabe: List['int']) -> int:
    x = 0
    for i in listabe:
        x += i
    return x

#print(feladat4((1, 4, 3, 4)))

def feladat5(szam1: int, szam2: int, szam3: int) -> int:
    x: int = feladat4(feladat3(szam1, szam2, szam3))
    return x

#print(feladat5(1, 2, 3))

def feladat6(a: float, b: float, c: float) -> List['int']:
    lista: List['float'] = list()
    D = b*b - 4*(a*c)
    if D > 0:
        lista.append(-b - math.sqrt(D) / (2 * a))
    if D == 0:
        lista.append(-b + math.sqrt(D) / (2 * a))
    return lista

#print(feladat6(2, 3, 4))

def tokeletes(a = int):
    if osztoosszeg(a) == a:
        return True
    else:
        return False

# print(tokeletes(6))

def termeszettokeletes(a = int, b = int) -> List['int']:
    lista: list = []
    for i in range(a, b):
        if tokeletes(i) == i:
            lista.append(i)
    return lista

#print(termeszettokeletes(1, 30))

def prim0(szam: int) -> bool:
    if szam == 1: return False
    gyokpluszegy = int(math.sqrt(szam)) + 1
    for i in range(2, gyokpluszegy):
        if szam % i == 0:
            return False
    return True


def prim1(szam: int):
    if szam == 1: return False
    return osztoosszeg(szam) == 1


def mersenneszam(n: int):
    return 2**n - 1


def mersenneprime(a: int):
    return prim0(a) and prim0(mersenneszam(a))

#print(mersenneprime(10))

def fibonacci(n: int) -> List['int']:
    if n == 0: return []
    if n == 1: return [0]
    lista: List = [0, 1]
    for i in range(2, n):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista

#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(2))
#print(fibonacci(3))
#print(fibonacci(200))

def lkkt(a: int, b: int) -> int:
    izecucc = 0
    if a % b == 0:
        izecucc = a
    if b % a == 0:
        izecucc = b
    if a % b and b % a != 0:
        izecucc = a * b
    return izecucc

#print(lkkt(20, 50))

def lnko(a: int, b: int) -> int:
    szam = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            if szam < i:
                szam = i
    return szam

#print(lnko(20, 10))

def szfenikus(a: int) -> bool:
    x = 1
    lista: List['int'] = []
    for i in range(2, a + 2):
        if prim0(i) and a % i == 0:
            lista.append(i)
    if len(lista) == 3:
        for y in lista:
            x *= y
    if x == a:
        return True
    else:
        return False

print(szfenikus(69))