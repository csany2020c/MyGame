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

def hazifeladat2(lista: List['int']) -> int:
