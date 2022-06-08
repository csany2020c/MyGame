from typing import List
import random
#feladat1
#print(max(int(input()), (int(input())), (int(input()))))
#feladat2
def listazas(lista: list) -> list:
    lista2: List['int'] = list()
    atlag = sum(lista) // len(lista)
    for i in range(len(lista)):
        if lista[i] < atlag:
            lista2.append(lista[i])
    return lista2
print(listazas([1123452342, 546876976452, 43564745363, 345635354, 35635636, 35633656, 36535637, 7969678]))

#feladat3
def kilencven():
    lista1: List['int'] = list()
    for i in range(1 ,91):
        lista1.append((i))
    for x in range(200):
        random1: int = random.randint(0, len(lista1) - 1)
        random2: int = random.randint(0, len(lista1) - 1)
        lista1[random2] = int(lista1[random1])
        lista1[random1] = int(lista1[random2])
