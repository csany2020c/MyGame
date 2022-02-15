from typing import List


def valami():
    while True:
        valami: int = int(input())

        if valami == 0:
            break





def valami2():
    szam: int = 1
    szam2: int = 0

    while (szam != 0):
        szam = int(input())

        if szam != 0:
            szam += szam2
    print(szam2)





def listaz():
    lista: List['int'] = (4, 2, 3)
    szorzat: int = 1
    for i in lista:
        szorzat *= i
        print("Eredmény: {dsa}".format(dsa=szorzat))






def osztoosszeg(sz: int) -> int:
    szamfele: int = sz // 2 + 1
    osszeg: int = 0
    for x in range(1, szamfele):
        if sz % x == 0:
            osszeg = osszeg + x
    return osszeg
#print(osztoosszeg(int(input())))
#print(osztoosszeg(16))
#print(osztoosszeg(21))

def baratsagosszamok(sz: int, sz2: int) -> bool:
    return sz != sz2 and osztoosszeg(sz) == sz2 and osztoosszeg(sz2) == sz

#print(baratsagosszamok(6, 6))
#print(baratsagosszamok(332,123))
#print(baratsagosszamok(220, 284))
#print(baratsagosszamok(319550, 430402))


def hatvany(alap: int, kitevo: int) -> List['int']:
    lista : list = []
    szorzat: int = 1
    for i in range(0, kitevo + 1):
        lista.append(szorzat)
        szorzat *= alap
    return  lista

print(hatvany(2, 8))
print(hatvany(3, 4))