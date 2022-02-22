from typing import List

def f0(lista: List['int'], szam: int) -> List['int']:
    lista0: list = []

    for i in lista:
        if i % szam == 0:
            lista0.append(i)

    return lista0

#print(f0((1,2,3,4,5,6,7,8,9,10,11,12), 5))

def f01(lista: List['int']) -> bool:

    for i in lista:
        if i == 0:
            return True
        else:
            return False

#print(f01((0,1,2)))

def f1(szam1: int,szam2: int) -> min:

    if szam1 > szam2:
        return szam2
    else:
        return szam1

#print(f1(10,25))

#def f2(lista: List['int']) -> minlist:
    #szam =


#print(f2((2,6,12))

#def f6(szam1: float, szam2: float, szam3: float) -> List['int']:1


def hf1(szambe: int) -> bool:
    osztok: int = szambe // 2 + 1
    osszeg: int = 0
    for x in range(1, osztok):
        if szambe % x == 0:
            osszeg = osszeg + x

    if szambe == osszeg:
        return True
    else:
        return False

#print(hf1(int(input())))
#Tökéletes szám pl:(6,28)

def hf2(szam1: int, szam2: int) -> List['int']:
    listaki: List['int'] = list()
    for i in range(szam1, szam2):
        if hf1(i):
            listaki.append(i)

    return listaki

#print(hf2(1, 500))

def hf3(szam: int) -> List['int']:

    listaki: List['int'] = list()
    for i in range(0, szam):
        listaki.append(szam % 10)



print(hf1(int(input())))












