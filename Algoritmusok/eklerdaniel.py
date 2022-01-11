from typing import TextIO
from typing import List

#def fakt(n: int) -> int:
 #   szorzat = 1
  #  for i in range(2, n + 1):
   #     szorzat *= i
    #return szorzat

#for i in range(0, 10000):
 #   print(fakt(4))

def deez(nuts: int) -> List['int']:
    l: List['int'] = list()
    for i in range(1, nuts + 1):
        if nuts % i == 0:
            l.append(i)
    return l

#print(deez(54))

def prim(be: int) -> bool:
    return len(deez(be)) == 2

for i in range(0,128):
    print("{szam} {prim}".format(szam=i, prim=prim(i)))

for i in range (0, 1024):
    primszam = prim(i)
    if primszam:
        print()



