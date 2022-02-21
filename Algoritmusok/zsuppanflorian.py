import math
from typing import List


# szam = 69
# xd = False
# if szam > 1:
#     for i in range(2, szam):
#         if (szam % i) == 0:
#             xd = True
#             break
#
# if xd:
#     print(szam, "nem prímszám")
# else:
#     print(szam, "egy prínmszám")

# from sympy import *
# print(isprime(2))

# n = 234
# for i in range(2, n+1):
#     if n % i == 0:
#         ertek = 1
#         for k in range(2, (i//2)+1):
#             if(i % k == 0):
#                 ertek = 0
#                 break
#         if(ertek == 1):
#             print(i)

# be = int(256)
# if be % 2 == 0:
#    print("{0} páros".format(be))
# else:
#    print("{0} páratlan".format(be))
#


# list = [10, 21, 4, 43, 66, 100]
# for i in list:
#     if i % 2 == 0:
#         print(i)


# def parosak(bemenet: List['int']) -> List['int']:
#     kimenet: List['int'] = list()
#     for i in bemenet:
#         if i % 2 == 0:
#             kimenet.append(i)
#     return kimenet
#
# l3 = [3, 6, 8, 2, 3, 1, 4]
# l9 = [333, 4, 0, 44]
# l4 = parosak(l3)
# l5 = parosak(l9)
# print(l4)
# print(l5)
#
# def fugg(bemenet: int) -> List['int']:
#     kimenet: List['int'] = list()
#     szam : int = 0
#     if bemenet < 0:
#         for i in range(bemenet):
#             kimenet.append(szam)
#             szam = szam - 1
#     else:
#         for i in range(bemenet):
#             kimenet.append(szam)
#             szam = szam + 1
#     return kimenet
#
# bemenet =11
# print(fugg(bemenet))
#
# def paroslist(be :int) -> List['int']:
#     return parosak(fugg(be))
#
# print(paroslist(22))

# class Algorythm:
#     def __init__(self) -> None:
#         super().__init__()
#
#     def masikBinaris(self,szam:int) -> str:
#         outP:str = ""
#         for i in range(8):
#             outP += str(int(szam%2))
#             szam=int(szam/2)
#             print(szam)
#         return outP
#
#     def elso(self,lista:List['int'],szam:int) -> List['int']:
#         outLista:List['int'] = list()
#         for i in lista:
#             if(i%szam == 0):
#                 outLista.append(i)
#         return outLista
#
#     def masodik(self,lista:List['int']) -> bool:
#         count:int = 0
#         for i in lista:
#             if (i == 0):
#                 count+=1
#         if (count>0):
#             return True
#         else:
#             return False
#
#     def min(self,szam1:int,szam2:int) -> int:
#         return min(szam1,szam2)
#
#     def minList(self,lista:List['int']):
#         min:int = 999999
#         for i in lista:
#             if (i < min):
#                 min = i
#         return min
#
#     def mertanisorozat(self,a1:int,q:int,n:int) -> List['int']:
#         outList:List['int'] = list()
#         outList.append(a1)
#         for i in range(n):
#             if (i-1 >= 0):
#                 outList.append(outList[i-1] * q)
#         return outList
#
#     def negyedik(self,lista:List['int']) -> int:
#         count:int = 0
#         for i in lista:
#             count+=i
#         return count
#
#     def otodik(self,a1:int,q:int,n:int) -> int:
#         return self.negyedik(self.mertanisorozat(a1,q,n))
#
#
#
# Algorythm()
def prim(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def relative(x, y):
    return prim(x, y) == 1

print(relative(1, 2))



def relativ(a: int, b: int)-> bool:
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            a = i
    if a == 1:
        print("hamis")
    else:
        print("igaz")
relativ(21, 8)


# def donto(szam: int, szam2:int) ->bool:
#     a: int = 0
#     a2: int = 0
#     oszt = []
#     oszt2 = []
#
#     for i in range(0, szam):
#         a = a + 1
#         if szam % a == 0:
#             oszt.append(0)
#
#     for i in range(0, szam2):
#         a2 = a2 + 1
#         if szam2 % a2 == 0:
#             oszt2.append(1)
#
#     eldonto = len(oszt) / len(oszt2)
#     if eldonto == 1:
#         return True
#     else:
#         return False
#
# print(donto(21, 8))


#1
Num = int(input(" "))
ossz = 0
for i in range(1, Num):
    if(Num % i == 0):
        ossz = ossz + i
if (ossz == Num):
    print("igaz")
else:
    print("hamis")

#2
#def tokeletes(belist: List['int']) -> List['int']:
    #kilist: List['int'] = list()
    #for i in belist:
    #kilist.append(i)


#4
szam = 13455
osszeg = 0
for ossz in str(szam):
    osszeg += int(ossz)
print(osszeg)