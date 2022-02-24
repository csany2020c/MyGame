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

def tökeletesszam_lista(szam: int, szam1: int) -> List['int']:
    lista: List['int'] = []
    for i in range(szam, szam1):
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

def szamjegyosszeg(x: int) -> int:
    osszeg = 0
    for x in range():
       if osszeg == x:
    return osszeg

print(szamjegyosszeg(55))

