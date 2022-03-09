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

def oszthato()-> int:
    osszeg = 0
    for i in range(100,1000):
        if i % 15 == 0 and szamfelbontas(i) == 15:
            osszeg += 1
            return i

#print(oszthato())
#def armstrong(x: int)-> int:
    #szam: int = 0
    #for x in szamfelbontas(x):
   #     szam %


#HF3 1B FELADAT
def primek(szam: int) -> bool:
    if szam == 1: return False
    gyok = int(math.sqrt(szam)) + 1
    for i in range(1, gyok):
        if szam % i == 0:
            return False
    return True

#print(primek(1))

def mersenszamok(n:int):
    return 2*n-1

def fibonacci(n: int)->List['int']:
    n = int
    list: List['int'] = []
    for i in range(2, n):
        list.append()
    return list
print(fibonacci(100))




