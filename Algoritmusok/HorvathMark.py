from typing import List

def feladat(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
    return osszeg

#print(feladat(int(input())))

def feladat2(a: int , b: int) -> bool:
    szamoszto1: int = a // 2 + 1
    osszeg1: int = 0
    szamoszto2: int = b // 2 + 1
    osszeg2: int = 0
    for x in range(1, szamoszto1):
        if a % x == 0:
            osszeg1 += x
    for y in range(1, szamoszto2):
        if b % y == 0:
            osszeg2 += y
    if osszeg1 != b and osszeg2 != a or a == b:
        return False
    else:
        return True


#print(feladat2(1184, 1210))


def baratiszam_kereso(szam: int) -> int:
    szam2: int = feladat(szam)
    if szam == feladat(szam2) and szam != szam2:
        return szam2



#print(baratiszam_kereso(int(input())))

def baratiszam_kereso_tanar(eddigkeres: int):
    for x in range(1, eddigkeres + 1):
        y = feladat(x)
        z = feladat(y)
        if x != y and z ==x:
            print("{x}, {y}".format(x = x, y = y))

#baratiszam_kereso_tanar(2000)

def hatvany(alap: int, kitevo: int) -> List['int']:
    lista: list = []
    x: int = 1
    for i in range(kitevo + 1):
        lista.append(x)
        x *= alap

    return lista


print(hatvany(2, 32))