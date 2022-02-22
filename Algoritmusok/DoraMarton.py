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

print(termeszettokeletes(1, 30))