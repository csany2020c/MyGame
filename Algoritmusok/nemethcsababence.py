from typing import List
# def fakt(n: int) -> int:
#     szorzat = 1
#     for i in range(2, n + 1):
#         szorzat *= i
#     return szorzat
#
# print(fakt(6))


# def modulo(bemenet:int) -> List['int']:
#     l: List['int'] = list()
#     for i in range(1, bemenet + 1):
#         if bemenet % i ==0:
#             l.append(i)
#     return l
#
# for i in modulo(26):
#     print(i)

'''def prim(bemenet:int) -> bool:
    for i in range(2, bemenet + 1):
        if bemenet / i == 1 or bemenet / i == bemenet:
            return True
        else:
            return False

print(prim(17))'''

'''def parosak(belist: List['int']) -> List['int']:
    kilist: List['int'] = list()
    for i in belist:
        if i % 2 == 0:
            kilist.append(i)
    return kilist


l3 = [3, 6, 8, 2, 3, 1, 4]

def szamfelfuzes(bemegy: int) -> List['int']:
    kilist : List['int'] = list()
    if bemegy < 0:
        for i in range(0, bemegy - 1, -1):
            kilist.append(i)
    else:
        for i in range(0, bemegy +1):
            kilist.append(i)
    return kilist

def szamolas(bemenet:int) -> List['int']:
    return parosak(szamfelfuzes(bemenet))
print(szamolas(4))'''

#0.0 feladat
'''def oszthatok(beszam :int, belist : List['int']) -> List['int']:
    kilist: List['int'] = list()
    for i in belist:
        if i % beszam == 0:
            kilist.append(i)
    return kilist

print(oszthatok(4, [2, 5, 7, 8]))'''

#0.1 feladat
'''def fugveny2(belist : List['int']) -> bool:
    for i in belist:
        if i == 0:
            print("igaz")
            return True
        else:
            print("hamis")
            return False
            break


fugveny2([0, 1, 3, 4])'''

#1. feladat
'''def min(egyikszam:int, masikszam:int) ->int:
    if egyikszam > masikszam:
        return masikszam
    else:
        return egyikszam

print(min(4, 2))'''
#2. feladat

'''def minlist(belist: List[int]) -> int:
        szamok = min(belist)
        return szamok
print(minlist([9, 4, 5, 8]))'''

#3. feladat


#4. feladat
'''def listelem(belist : List['int']) -> int:
    osszeg = belist[0]
    for i in range(1, len(belist)):
        osszeg += belist[i]
    return osszeg

print(listelem([10, 10, 3]))'''

#5. feladat

#6. feladat
# '''def masodfoku(egyikszam:float, masikszam:float, harmadikszam:float)-> List['int']:
#     kilist : List['int'] = list()
#     a = egyikszam
#     b = masikszam
#     c = harmadikszam'''