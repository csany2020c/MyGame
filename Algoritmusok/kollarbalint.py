from typing import List

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

def hf2_7() -> List['int']:
    listaki: List['int'] = list()
    szam: int = 1

    for i in range(100, 999):
        for x in (hf2_3(szam)):
            if x ** 3 + x == szam:
                listaki.append(szam)
    return listaki

print(hf2_7())














