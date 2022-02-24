from typing import List


def tökeletesszam(szam: int) -> bool:
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

def tökeletesszam_lista(min: int, max: int) -> List['int']:
    lista: List['int'] = []
    for i in range(min, max):
        if tökeletesszam(i):
            lista.append(i)

    return lista

#print(tökeletesszam_lista(1, 10))


def szamfelbontas(szam: int) -> List['int']:
    lista: List['int'] = []
    while szam != 0:
        lista.append(szam % 10)
        szam = szam // 10
    return lista

#print(szamfelbontas(123))

def szamjegyosszeg(szam: int) -> int:
    osszeg = 0
    for i in (szamfelbontas(szam)):
        osszeg += i
    return osszeg
#print(szamjegyosszeg(122))

def szamjegyszorzas(szam: int) -> bool:
    szorzat = 1
    for i in str(szam):
        szorzat *= int(i)
    if szorzat == szam:
        return True
    else:
        return False

#print(szamjegyszorzas(16))



def legkisebbtöbbszörös(a: int, b: int) -> int:
    szam = 0
    if a % b == 0:
        szam = a
    if b % a == 0:
        szam = b
    if b % a and a % b != 0:
        szam = a * b
    return szam
#print(legkisebbtöbbszörös(3, 9))

