from typing import List

# class Program:
#     def __init__(self):
#         szam:int = 0
#         for i in range(42):
#             szam = szam + 1
#             print(szam)
#
# Program()



    # szam = int(input())
    # ossz : int = 0
    # ossz = szam
    # while (szam != 0):
    #     szam = int(input())
    #     if szam != 0:
    #         ossz += szam
    #     #ossz = ossz + szam
    # print(ossz)


    #
    # list = [3,2,1,5,4]
    # x = sum(list)
    # print(x)


def listaossz():
    lista: List['int'] = (2,3,4,5)
    osszeg: int = 0
    for i in lista:
        osszeg += i
    print("az osszeg {a}".format(a=osszeg))

def listaossz2():
    lista: List['int'] = (2,3,4,5)
    osszeg: int = 0
    for i in range(0, len(lista)):
        osszeg += lista[i]
        print("az osszeg {a}".format(a=osszeg))

def osszegzes(lista: List['int']) -> int:
    szam: int = 0
    szam = int(input())
    osszeg: int = 0
    for i in range(0, len(lista)):
        osszeg += lista[i]
        return osszeg


lista: List['int'] = (2,3,4,5)
print(osszegzes())

osszegzes()
