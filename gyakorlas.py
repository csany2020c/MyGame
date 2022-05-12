from typing import List

def szamfelbont(x: int) -> List['int']:
    lista: List['int'] = []
    for i in str(x):
        lista.append(int(i))
    return lista

#print(szamfelbont(234))
def szamjegyosszeg(x: int) -> int:
    osszeg = 0
    for i in (szamfelbont(x)):
        osszeg += i
    return osszeg

#print(szamjegyosszeg(33))


def szamjegy(x: int) -> int:
    szorzat = 0
    for i in (szamfelbont(x)):
        szorzat *= int(i)
    #return szorzat
    if szorzat == x:
        return True
    else:
        return False
#print(szamjegy(541))


def osszeg(x: int, a: int) -> List['int']:
    lista: List['int'] = []
