from typing import List
import random

#elsofeladat
#def legnagyobb(legnagyobbszam: list) -> int:
#    b: int = legnagyobbszam[0]
#    for i in legnagyobbszam:
#        if b < i:
#            b = i
#    return b

#lista: List['int'] = list()
#a: int = 0
#for i in range(3):
#   a = int(input("Kérek egy számot:"))
#   lista.append(a)

#print(legnagyobb(lista))

#masodikfeladat

lista = list()
lista = [1, 3, 4, 7, 32, 10, 12, 9]


c: int = 0
d: int = 0
atlag: int = 0

for i in lista:
    c += 1

for y in lista:
    d = d + y

atlag = d / c

print(atlag)

for j in lista:
    if j < atlag:
        print(j)

