from typing import TextIO
from typing import List
from time import time
#def fakt(n: int) -> int:
 #   szorzat = 1
  #  for i in range(2, n + 1):
   #     szorzat *= i
    #return szorzat

#for i in range(0, 10000):
 #   print(fakt(4))

# def deez(nuts: int) -> List['int']:
#     l: List['int'] = list()
#     for i in range(1, nuts + 1):
#         if nuts % i == 0:
#             l.append(i)
#     return l
#
# #print(deez(54))
#
# def prim(be: int) -> bool:
#     return len(deez(be)) == 2
#
# for i in range(0,128):
#     print("{szam} {prim}".format(szam=i, prim=prim(i)))
#
# for i in range (0, 1024):
#     primszam = prim(i)
#     if primszam:
#         print()
# def oszti():
#
#     for i in  range(40, 42):
#         i = i%2
#         print(i)
#
#
# oszti()


# def deez(be:int) -> List['int']:
#     ki: List['int'] = list()
#
#     if be < 0:
#         for i in range(0, be - 1, -1):
#             ki.append(i)
#         return ki
#     else:
#         for i in range(0, be + 1):
#             ki.append(i)
#             return ki
#
#
#
#
#
# print(deez(-43))

def nuts(be:int) -> List['int']:
    ki: List['int'] = list()
    for i in range(0, be+1):
        ki.append(i)
        return ki
    if be % 2 ==0:
        ki.append(ki)
        return ki

#print(nuts(2))

def HF1(belist: List['int'], beszam:int) -> List['int']:
    kilist: List['int'] = list()
    for i in belist:
        if i % beszam == 0:
            kilist.append(i)
    return kilist

L7 = [3, 6, 8, 2, 3, 1, 4, 333, 4, 0, 44]

# print(HF1(L7, 11))

def HF2(belist: List['int']) -> bool:
    return 0 in belist


L7 = [3, 6, 8, 2, 10, 3, 1, 4, 333]
#print(HF2(L7))


def min(be: int, bebe: int) -> int:
        if be < bebe:
            print(be)
        else:
            print(bebe)
I= 8
#print(min(48,9))

# 2 feladat
L7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,]

L7.sort()

#print(L7[:1])


def helyiertek2(be:int) -> List['int']:
    ki: List['int'] = list()
    for c in str(abs(be)):
        ki.append(int(c))
    return ki

# A lista elemeinek a négyzetének az összege [2,3] 2*2+3*3
def negyzetosszeg(be: List['int']) -> int:
    szam: int = 0
    for i in be:
        szam+=i*i
    return szam
Lszomi = [4, 16, 37, 58, 89, 145, 42, 20, ]
def boldoge(szam: int) -> bool:
    aktualisnegyzetosszeg: int = szam
    szekvencia : List['int'] = list()
    while aktualisnegyzetosszeg != 1 and aktualisnegyzetosszeg not in Lszomi and aktualisnegyzetosszeg not in szekvencia:
        szekvencia.append(aktualisnegyzetosszeg)
        aktualisnegyzetosszeg = negyzetosszeg(helyiertek2(aktualisnegyzetosszeg))
        #print(szekvencia)
    return aktualisnegyzetosszeg == 1

ts1 = time()
#print(boldoge(2223))
l : List['int'] = list()
for i in range(1, 20000):
    if boldoge(i):
        l.append(i)
ts2 = time()
print("Az algoritmus {mp} másodpercig futott.".format(mp=(ts2 - ts1)))
print(l)


















