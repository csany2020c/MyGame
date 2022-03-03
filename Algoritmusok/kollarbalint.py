from typing import List
from time import time
import math

def hf1_0(lista: List['int'], szam: int) -> List['int']:
    lista0: list = []

    for i in lista:
        if i % szam == 0:
            lista0.append(i)

    return lista0

#print(hf1_0((1,2,3,4,5,6,7,8,9,10,11,12), 5))

def hf1_01(lista: List['int']) -> bool:

    for i in lista:
        if i == 0:
            return True
        else:
            return False

#print(hf1_01((0,1,2)))

def hf1_1(szam1: int,szam2: int) -> min:

    if szam1 > szam2:
        return szam2
    else:
        return szam1

#print(hf1_1(10,25))

#def hf1_2(lista: List['int']) -> minlist:
    #szam =


#print(hf1_2((2,6,12))


def hf2_1(szambe: int) -> bool:
    osztok: int = szambe // 2 + 1
    osszeg: int = 0
    for x in range(1, osztok):
        if szambe % x == 0:
            osszeg = osszeg + x

    if szambe == osszeg:
        return True
    else:
        return False

#print(hf2_1(int(input())))
#Tökéletes szám pl:(6,28)

def hf2_2(szam1: int, szam2: int) -> List['int']:
    listaki: List['int'] = list()
    for i in range(szam1, szam2):
        if hf2_1(i):
            listaki.append(i)

    return listaki

#print(hf2_2(1, 500))

def hf2_3(szam1: int) -> List['int']:
    listaki: List['int'] = list()
    while szam1 > 0:
        listaki.append(szam1 % 10)
        szam1 = szam1 // 10
    return listaki

#print(hf2_3(375))

def hf2_4(szam: int) -> int:
    eredmeny: int = 0
    for i in (hf2_3(szam)):
        eredmeny += i
    return eredmeny

#print(hf2_4(850))

def hf2_5(szam: int) -> int:
    szam2: int = 1
    for i in (hf2_3(szam)):
        szam2 *= i
    if szam2 == szam:
        return True
    else:
        return False

#print(hf2_5(1))

def hf2_6() -> int:
    szam: int = 0

    for i in range(1, 999):
        if hf2_4(i) == 15 and i % 15 == 0:
            szam += 1
    return szam

#print(hf2_6())

def hf2_7() ->  List['int']:
    listaki: List['int'] = list()
    szam: int = 1

    for i in range(100, 999):
        for x in (hf2_3(szam)):
            if x ** 3 + x == szam:
                listaki.append(szam)
    return listaki
#Nincs kész
print(hf2_7())

def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

def hf3_1prim(szam: int):
    if szam == 1: return False
    return osztoosszeg(szam) == 1

def hf3_1a(hatvany: int):
    return 2**hatvany - 1

def hf3_1b(szam: int):
    return hf3_1prim(szam) and hf3_1prim(hf3_1a(szam))

#print(hf3_1b(1))

def hf3_2(n: int) -> List['int']:
    if n == 0: return []
    if n == 1: return [0]
    listaki: List = [0, 1]
    for i in range(2, n):
        listaki.append(listaki[i - 1]+listaki[i - 2])
    return listaki

#print(hf3_2(0))
#print(hf3_2(1))
#print(hf3_2(15))

def hf3_3(a: int, b: int) -> int:
    return a * b
#print(hf3_3(47311, 60401))

def hf4_0(a: int) -> int:
    osszeg: int = 0
    for i in (hf2_3(a)):
        osszeg += i ** 2
    return osszeg

#print(hf4_0(52))

def hf4_1(szambe: int) -> bool:
    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0
    e: int = 0
    f: int = 0
    g: int = 0
    if szambe == 1:
        return True
    else:
        for i in (hf2_3(szambe)):
            a += i ** 2
    if a == 1:
        return True
    else:
        for i in (hf2_3(a)):
            b += i ** 2
    if b == 1:
        return True
    else:
        for i in (hf2_3(b)):
            c += i ** 2
    if c == 1:
        return True
    else:
        for i in (hf2_3(c)):
            d += i ** 2
    if d == 1:
        return True
    else:
        for i in (hf2_3(d)):
            e += i ** 2
    if e == 1:
        return True
    else:
        for i in (hf2_3(e)):
            f += i ** 2
    if f == 1:
        return True
    else:
        for i in (hf2_3(f)):
            g += i ** 2
    if g == 1:
        return True
    else:
        return False

print(hf4_1(881))

def hf4_2() -> List['int']:
    listaki: List = []

    for i in range(0, 200000):
        if hf4_1(i) == 1:
            listaki.append(i)
    return listaki

#print(hf4_2())