from typing import List
from time import time
import math


#1. feladat 42-ig szamok egyesevel kiiaratasa
# a: int = 0
# for c in range(42):
#     a = a + 1
#     print(a)

#2. feladat szamok beolvasasa ameddig a bemenet nem lesz 0
#3. feladat a 2. feladat alapján szamolja ossze a bemeneteket, ameddig nem 0 a bement
# asd = 0
# while(True):
#     a: int = int(input())
#     asd = asd + a
#     if a == 0:
#         # print(asd)
#         print("A beirt szamok osszege:" + " " + str(asd))
#         break

#4. feladat
# def osszeglistaban():
#     lista: List['int'] = (6, 1, 1, 1, 1, 1, 1)
#     ad: int = 0
#     for i in range(0, len(lista)):
#         ad += lista[i]
#     print("Az összeg: {sum}".format(sum=ad))
#
# osszeglistaban()
# lista: List['int'] = (6, 1, 1, 1, 1, 1, 1)
# def osszegzes(lista: List['int']) -> int:
#     szam: int = 0
#     for i in range(0, len(lista)):
#         szam += lista[i]
#     return szam
#
#
# print(osszegzes(lista))

#5. feladat: faktorialis szamolas
# def faktoralis(asd: int) -> int:
#     szorzat = 1
#     for i in range(2, asd + 1):
#         szorzat *= i
#     return szorzat


# print(faktoralis(6))

# 2. feladat
# print(8 % 3)

#6. feladat: primszam fuggveny, break
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

#7.feladat: primszam eldonto fuggveny, bemenet egy szam- kimenet igaz vagy hamis
# def primszam(a: int) -> bool:
#     if len(osztok(a)) == 2:
#         return True
#     else:
#         return False
#
# print(primszam(16))

#8. feladat: gyakorlas primszam fuggveny(lassu a szamolas 100000 felett)
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

# *.feladat, felesleges, mert mar feljebb van erre fuggveny
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
# def binaris_ketto(a: int) -> int:
#     w: str = ""
#     erkezo = a
#     while erkezo > 0:
#         if erkezo % 2 == 0:
#             w = w + "0"
#         else:
#             w = w + "1"
#         erkezo = erkezo // 2
#     return w
#
# bejovo: int = int(input("Írj be egy számot: "))
# print("Az eredmény:" + " " + binaris_ketto(bejovo))

#erdekesseg
# print(6 / 2)
# print(6 // 2)

#10.feladat: parosszamok, bemenet lista, kimenete lista a paros szamokkal
def parosfuggveny(a: List['int']) -> List['int']:
    lista: List['int'] = list()
    for i in a:
        if i % 2 == 0:
            lista.append(i)
    return lista

# bemenetelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -2, -3, -11]
# print(parosfuggveny(bemenetelist))

#11.feladat:szamolas 6-ig
def szamolas(a: int) -> List['int']:
    lista: List['int'] = list()
    # if a < 0:
    #     return "Sajnos ilyen számot jelenleg nem lehet számolni!"
    if a < 0:
        for i in range(0, a - 1, -1):
            lista.append(i)
    else:
        for i in range(0, a + 1):
            lista.append(i)
    return lista

# print(szamolas(66))
# print(szamolas(-66))

# . feladat: az elozo fuggvenyek hasznalta
# def osszeshasznalata(a: int) -> List['int']:
#     return parosfuggveny(szamolas(a))
#
# print(osszeshasznalata(7))

#házi feladat
#0.0 feladat
def maradeknelkuliosztok(a: List['int'], b: int) -> List['int']:
    uj: List['int'] = list()
    for i in a:
        if i % b == 0:
            uj.append(i)
    return uj

listacska = [1, 5 , 8, 9 , 150, 60, 44, 3, 0, 7]
# print(maradeknelkuliosztok(listacska, 6))

#
def logikaifuggveny(a: List['int']) -> bool:
    almagyar = 0
    for i in a:
        if i == 0:
            almagyar = almagyar + 1
    if almagyar >= 1:
        return True
    else:
        return False

alma = [20, 60, 70, 5, 6, 3, 7, 32]
alma1 = [12, 0, 6, 20, 7]
# print(logikaifuggveny(alma))
# print(logikaifuggveny(alma1))

#1. feladat
def min(a: int, b: int) -> int:
    if a > b:
        return b
    elif a == b:
        return a, b
    else:
        return a

# print(min(9, 8))

#2, feladat
def minilist(a: List['int']) -> int:
    szam = 0
    for i in a:
        if szam < i:
            szam = i
        break
    for i in a:
        if szam > i:
            szam = i
    return szam

minilistam = [5, 6, 8, 88, 2, 66, 30]
# print(minilist(minilistam))

#3.feladat
def harombemenet(a1: int, q: int, n: int) -> List['int']:
    uj: List['int'] = list()
    szam = ()
    szam = a1 * q
    while n > 0:
        szam = a1 * q
        n = n - 1
        break
    while n > 0:
        szam = szam * q
        n = n - 1
    if n == 0:
        uj.append(szam)
        return uj
# print(harombemenet(4, 4, 1))

#4. feladat
def osszeglista(a: List['int']) -> int:
    szam = 0
    for i in a:
        szam = szam + i
    return szam

osszeglistam = [1, 8, 16, 32, 88, 789]
# print(osszeglista(osszeglistam))

#5. feladat
def nemtom(a1: int, q: int, n: int) -> int:
    return osszeglista(harombemenet(a1, q, n))

# print(nemtom(5, 8, 2))

#6. feladat-nincs kész, majd egyszer...
def jerry(a: float, b: float, c: float) -> List['float']:
    listam: List['float'] = list()
    if a == 0:
        fruit = " "
        listam.append(fruit)
        return listam
    else:
        szam = math.pow(b, 2) # (b**2)
        szam1 = 4 * c
        szam2 = szam - szam1
        szam2 = 2 * a
        szam2 = pow(szam2, 2)

        if szam2 < 0:
            return listam

# print(jerry(8, 12, 3))