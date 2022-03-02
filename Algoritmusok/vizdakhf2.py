from typing import List

def osztoosszeg(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg


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
    for x in range(szam, szam1):
        if tökeletesszam(x):
            lista.append(x)

    return lista

#print(tökeletesszam_lista(1, 10))


def szamfelbontas(szam: int) -> List['int']:
    lista: List['int'] = []
    if szam == 0:
        lista.append(0)
    while szam != 0:
        lista.append(szam % 10)
        szam = szam // 10
        lista.reverse()
    return lista


#print(szamfelbontas(343))

def szamjegyosszeg(x: int) -> int:
    osszeg = 0
    for x in szamfelbontas(x):
        osszeg += x
    return osszeg

#print(szamjegyosszeg(553))

def szorzat(x: int) -> bool:
    szorzat = 0
    for x in szamfelbontas(x):
        szorzat *= x
    if szorzat == x:
        return True
    else:
        return False
    pass
#print(szorzat(54))

def oszthato(a: int)-> int:
    osszeg : 0
    for a in szamjegyosszeg(a):
        if osszeg == 15:
            return True
        if szam % 15:
            return True
        pass
#print(oszthato(555))
#def armstrong(x: int)-> int:
    #szam: int = 0
    #for x in szamfelbontas(x):
   #     szam %


#HF3 1B FELADAT
def primek(szam: int)-> bool:
    pass

def mersenszamok(n:int):
    return 2*n-1





