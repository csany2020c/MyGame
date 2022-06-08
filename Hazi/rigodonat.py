from typing import List
import random

#elsofeladat1
def legnagyobb(legnagyobbszam: list) -> int:
    b: int = legnagyobbszam[0]
    for i in legnagyobbszam:
        if b < i:
            b = i
    return b

lista: List['int'] = list()
a: int = 0
for i in range(3):
   a = int(input())
   lista.append(a)

print(legnagyobb(lista))

#masodikfeladat

list8num :List['int'] = [ 2,5,6,7,32,23,1,3]