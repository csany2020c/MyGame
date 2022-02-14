from typing import List
from time import time
import math

#1. feladat: faktorialis szamolas
# def faktoralis(asd: int) -> int:
#     szorzat = 1
#     for i in range(2, asd + 1):
#         szorzat *= i
#     return szorzat


# print(faktoralis(6))

# 2. feladat
# print(8 % 3)

#3. feladat: primszam fuggveny, break
def osztok(n: int) -> list[int]:
    lista: List['int'] = list()
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista

# for i in osztok(26):
#     print(i)
#
# print(osztok(26))

# .feladat: primszam eldonto fuggveny, bemenet egy szam- kimenet igaz vagy hamis
# def primszam(a: int) -> bool:
#     if len(osztok(a)) == 2:
#         return True
#     else:
#         return False
#
# print(primszam(16))

#gyakorlas primszam fuggveny(lassu a szamolas 100000 felett)
# def primszam_sajat(a: int) -> bool:
#     erkezo = a
#     random = 0
#     onmaga = 1
#     if erkezo > 250:
#         return "Keress kisebb szamot!"
#     if erkezo > 0:
#         for i in range(erkezo):
#             if erkezo % onmaga == 0:
#                 random = random + 1
#             onmaga = onmaga + 1
#     else:
#         return "Nem lehet ilyet :)"
#
#     if random == 2:
#         return True
#     else:
#         return False

#print(primszam_sajat(250))

# 3.feladat, felesleges, mert mar feljebb van erre fuggveny
# def fuggveny1(n: int) -> bool:
#     return len(primszam(n)) == 2
#
# for i in range(0, 126):
#      print("{szam} {primszam}".format(szam=i, primszam=fuggveny1(i)))

#új számolás-gyakorlas
# ts1 = time()
# for i in range(100000, 1000000):
#     primszame = primszam_sajat(i)  # Prímszám eldöntő függvény helye
#     if primszame:
#         print(i)
# ts2 = time()
# print("Az algoritmus {mp} másodpercig futott.".format(mp=(ts2 - ts1)))

#9. feladat: binaris szamok
def binaris_ketto(a: int) -> int:
    w: str = ""
    erkezo = a
    while erkezo > 0:
        if erkezo % 2 == 0:
            w = w + "1"
        else:
            w = w + "0"
        erkezo = erkezo // 2
    return w

bejovo: int = int(input("Írj be egy számot: "))
print("Az eredmény:" + " " + binaris_ketto(bejovo))

#erdekesseg
# print(6 / 2)
# print(6 // 2)