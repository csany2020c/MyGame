from typing import List
import random

#elsofeladat
def legnagyobb(legnagyobbszam: list) -> int:
    b: int = legnagyobbszam[0]
    for i in legnagyobbszam:
        if b < i:
            b = i
    return b

lista: List['int'] = list()
a: int = 0
for i in range(3):
   a = int(input("Kérek egy számot:"))
   lista.append(a)

print(legnagyobb(lista))

#masodikfeladat

list8num :List['int'] = [1,3,4,7,32,10,12,9]