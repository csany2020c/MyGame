from typing import List
import math

#def fakt(n: int) -> int:
    #szorzat = 1
    #for i in range(2, n + 1):
        #szorzat *= i

    #return szorzat


#for i in range(1, 5000):
        #print(fakt(i))

#def oszt():
    #inp = int(input())
    #lista = []
    #oszto = 1
    #for i in range(inp):
        #if inp % oszto == 0:
            #lista.append(oszto)
        #oszto = oszto + 1

    #print(lista)

#def oszt2(n: int) -> int:
    #l: list['int'] = list()
    #for i in range(1, n + 1):
        #if n % i == 0:
            #l.append(i)

    #return l


# def prim():
#     inp = int(input())
#     lista =[]
#     mb = 1
#     mb2 = False
#     for i in range(inp):
#         if inp % mb == 0:
#             lista.append(mb)
#         mb = mb + 1
#
#     if len(lista) == 2:
#         mb2 = True
#     print(lista)


def hazi(belist: List['int']) -> List['int']:
    kilist: List['int'] = list()

    for i in belist:
        if i % 2 == 0:
            kilist.append(i)

    return kilist


l1 = [1, 55, 4877, 4625, 4, 2, 9, 7]
l2 = hazi(l1)
print(l1)
