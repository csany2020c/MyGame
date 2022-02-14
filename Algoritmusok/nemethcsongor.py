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


prim(szam)


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
