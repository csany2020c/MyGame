from typing import List

class egytoltizenotig:
    for i in range(1, 16):
        print(i)



class beolvasas:
    while(True):
        szam: int == int(input())

        if szam == 0:
            break

#def osztoparok(szam: int) -> int:
    #szamfele: int = szam // 2 + 1
    #osszeg: int = 0
    #for x in range(1, szamfele):
        #if szam % x == 0:
            #osszeg = osszeg + x
        #return osszeg
    #while(True):


#print(osztoparok(int(input())))

#def feladat00(lista: List) -> int:
 #   for i in range:






# 1. Készítsen függvényt, amely eldönti egy számról, hogy "tökéletes"-e.
def tokeletesszam(szam: int) -> int:
    szamfele: int = szam // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if szam % x == 0:
            osszeg = osszeg + x
        if szam == osszeg:
            return




