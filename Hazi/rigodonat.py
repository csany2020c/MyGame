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

#print(legnagyobb(lista))

#masodikfeladat

list8num :List['int'] = [ 2,5,6,7,32,23,1,3]
osszeg = 0
db: int = 0
for i in list8num:
    osszeg += i
    db = i
    atlag = osszeg / db

    print("A számok átlagánál kisebb számok({a})".format(a=atlag))
    for a in list8num:
        if a < atlag:
            print (a)