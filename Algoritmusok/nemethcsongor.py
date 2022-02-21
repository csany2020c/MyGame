import math
from typing import List


def binaris(bemenet: int) -> str:
    b: str = ''
    while bemenet > 0:
        if bemenet % 2 == 0:
            bemenet = bemenet // 2
            b = '0' + b
        else:
            bemenet = bemenet // 2
            b = '1' + b
    return b


szam = 135
if szam % 3 == 0:
    k: str = ", \n osztható hárommal, \n"
else:
    k: str = ", nem osztható hárommal,  \n"
if szam % 4 == 0:
    d: str = " osztható néggyel,  \n"
else:
    d: str = " nem osztható néggyel,  \n"
if szam % 5 == 0:
    c: str = " osztható öttel,  \n"
else:
    c: str = " nem osztható öttel,  \n"
if szam % 2 == 0:
    g: str = "  és páros"
else:
    g: str = " és páratlan"


def prim(input: int) -> bool:
    idk = 0
    osztodarab = 0
    for i in range(input):
        idk = idk + 1
        eredmeny = input % idk
        if eredmeny == 0:
            osztodarab = osztodarab + 1
        if osztodarab > 2:
            return False
    if osztodarab == 2:
        return True


if prim(szam) == True:
    a: str = " prímszám"
else:
    a: str = " nem - prímszám"
# print("A " + str(szam) + " bináris értéke " + str(binaris(szam) + str(k) + str(d) + str(c) + str(g) + str(a) + "."))


def parosito(lista: List['int']) -> List['int']:
    lista2: List['int'] = list()
    for i in lista:
        if i % 2 == 0:
            lista2.append(i)
    return lista2


lista: List['int'] = (6, 5, 10, 3, 0, 2, 3, 614, 982, 1537, -2)
# print(parosito(lista))


def szamolo(a: int) -> List['int']:
    lista3: list['int'] = list()
    if a == 0:
        lista3.append(0)
    if a > 0:
        for i in range(a):
            lista3.append(i + 1)
    if a < 0:
        for i in range(a * -1):
            lista3.append((i + 1) * -1)
    return lista3


# print(szamolo(5))


def parosszamolo(ncs: int) -> List['int']:
    return parosito(szamolo(ncs))


# print(parosszamolo(6))


def oszt(num: int, lajst: List['int']) -> List['int']:
    lajst2: List['int'] = list()
    for i in lajst:
        if i % num == 0:
            lajst2.append(i)
    return lajst2


berakando: List['int'] = (1, 2, 3, 4, 5, 6,)
# print(oszt(2, berakando))


def nulla(lista5: List['int']) -> bool:
    for i in lista5:
        if i == 0:
            return True
    return False


lista6: List['int'] = (1, 0, 2, 3, 4,)
# print(nulla(lista6))


def min(egy: int, ketto: int) -> int:
    if egy < ketto:
        return egy
    else:
        return ketto


# print(min(-6, 5))


def minlist(lajstrom: List['int']) -> int:
    kicsi: int = lajstrom[0]
    for i in lajstrom:
        if kicsi > i:
            kicsi = i
    return kicsi


lajstrom2: List['int'] = (15, 11, 6, 8, 37, 5)
# print(minlist(lajstrom2))


def haromszam(a1: int, q: int, n: int) -> List['int']:
    ki: List['int'] = list()
    ki.append(a1)
    for i in range(n - 1):
        ki.append(a1 * q)
        a1 *= q
    return ki


# print(haromszam(5, 6, 7))


def osszeadas(lista9: List['int']) -> int:
    a2 = 0
    for i in lista9:
        a2 += i
    return a2


lajstrom3: List['int'] = (1, 2, 3, 4)
# print(osszeadas(lajstrom3))


def mertan(elso: int, masodik: int, harmadik: int) -> int:
    return osszeadas(haromszam(4, 5, 8))


# print(mertan(4, 5, 54))


def masodfoku(a3: float, b3: float, c3: float) -> List['float']:
    diszkriminans: float = b3*b3 - 4*a3*c3
    megoldas: List['float'] = list()
    if diszkriminans < 0:
        return megoldas
    diszkriminans2 = math.sqrt(b3*b3 - 4*a3*c3)
    megoldas1 = (-b3 + diszkriminans2) / 2*a3
    megoldas2 = (-b3 - diszkriminans2) / 2*a3
    if megoldas1 == megoldas2:
        megoldas.append(megoldas1)
    else:
        megoldas.append(megoldas2)
        megoldas.append(megoldas1)
    return megoldas


# print(masodfoku(1, -7, 9))


def pitagorasz(bef1: float, bef2: float) -> float:
    a2: float = bef1 * bef1
    b2: float = bef2 * bef2
    atf: float = math.sqrt(a2 + b2)
    return atf


# print(pitagorasz(5, 6))


def relativ_prim(szam2: int, szam3: int) -> bool():
    idk = 1
    for i in range(szam2):
        idk = idk + 1
        er = szam3 % idk
        er2 = szam2 % idk
        if er == er2:
            return False
        return True


# print(relativ_prim(4, 35))
