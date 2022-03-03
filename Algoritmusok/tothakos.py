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
#print(feladat2((600,20,1000,10340,1024, 1500)))

def fealadat3(a: int, q: int, n:int) -> List['int']:
    lista: list = []
    for i in range(1, n+1):
        x= a * q ** (i-1)
        lista.append(x)
    return lista
#print(fealadat3(1,2,10))

def feladat4(lista: List['int']) -> int:
    x = 0
    for i in lista:
        x += i
    return x
#print(feladat4((1,2,4,8,16,32,64,128,256)))

def feladat5(a: int, q: int, n: int) -> int:
    y: int = feladat4(fealadat3(a, q, n))
    return y
#print(feladat5(1, 2, 10))

def feladat6(a: float, b:float, c:float) -> List['int']:
    lista: list = []
    x = b * b - 4 * a * c
    if x >= 0:
        y: int = (-b + x) / (2 * a)
        lista.append(y)
        z: int = (-b - x) / (2 * a)
        lista.append(z)
    return lista
#print(feladat6(3, 7, 4))

def tokeletes(a: int)->bool:
    ossz: int = 0
    for i in range(1, ):
        if a % i == 0:
            ossz = ossz + i
    if ossz == a:
        return True
    else:
        return False
#print(tokeletes)

def tokeletes2(min: int, max: int) -> List['int']:
    lista: List['int'] = []
    for i in range(min, max):
        if tokeletes2(i):
            lista.append(i)
    return lista
#print(tokeletes2(1, 10))

def bonto(x: int)-> List['int']:
    lista: List['int'] = []
    if x <= 0:
        lista.append(0)
        return lista
    while x != 0:
        lista.append(x % 10)
        x = x // 10
    lista.reverse()
    return lista
#print(bonto(123))

def szamjegyosszeg(a: int)-> int:
    osszeg = 0
    for i in bonto(a):
        osszeg += i
    return osszeg
#print(szamjegyosszeg(123))

def szamjegyszorzat(y: int) -> int:
    szorzat = 1
    for i in bonto(y):
        szorzat *= i
    if szorzat == y:
        return True
    else:
        return False

#print(szamjegyszorzat(8))

def tizenot() -> int:
    db = 0
    for i in range(100, 1000):
        if i % 15 == 0 and szamjegyosszeg(i) == 15:
            db += 1
    return db
#print(tizenot())

def armstrong() -> List['int']:
    lista: List = []
    összeg = 0
    for x in range(100, 1000):
        for i in (bonto(x)):
            összeg += i ** 3
            if összeg != x:
                összeg = 0
            else:
                lista.append(összeg)
                összeg = 0
        return lista

#print(armstrong())

def prim(y: int) -> bool:
    if y == 1: return False
    gyokpluszmegegy = int(math.sqrt(y)) + 1
    for i in range(2, gyokpluszmegegy):
        if y % i == 0:
            return False
    return True
#print(prim(2))

def mersenne(x: int) -> bool:
    return 2 ** x -1

def mersenneprim(a: int) -> bool:
    return prim(a)
#print(mersenneprim(2))

def primkereso(x: int) -> List[int]:
    lista: List['int'] = [0]
    for i in [x]:
        if mersenneprim(i) == True:
            lista.append()
        return lista
#print(primkereso)

def legkisebbtobbszoros(a: int, b: int) -> int:
    szam = 0
    if a % b == 0:
        szam = a
    if b % a == 0:
        szam = b
    if b % a and a % b != 0:
        szam = a * b
    return szam
#print(legkisebbtobbszoros(3, 5))

def legnagyobboszto(a: int, b:int) -> int:
    szam = 0
    for i in range(1, a + 1):
        if a % 2 == 0 and b % i == 0:
            if szam < i:
                szam = i
    return szam
#print(legnagyobboszto(44, 88))

def fibonacci(y: int) -> List['int']:
    lista: List['int'] = [0, 1]
    for i in range(2, y):
        lista.append(lista[i-1] + lista[i-2])
    return lista
#print(fibonacci(100))

def szfenikus(a: int) -> bool:
    x = 0
    lista: List['int'] = []
    for i in range(2, a + 2):
        if prim(i) and a % i == 0:
            lista.append(i)
    if len(lista) == 3:
        for y in lista:
            x *= y
    if x == a:
        return True
    else:
        return False
#print(szfenikus(10))

#def boldogszam(x: int) -> bool:
    #lista: List[]
