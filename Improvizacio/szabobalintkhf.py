from typing import List
from random import random
from random import randint

print("Feladat1:")
print("")

szam1: int = int(input("Első szám:"))
szam2: int = int(input("Második szám:"))
szam3: int = int(input("Harmadik szám:"))
#
print("Feladat1: ", max(szam1, szam2, szam3))

print("")
print("Feladat2:")
print("")

listx = list()
listx = [1, 2, 3, 4, 5, 6, 7, 19]

n : int = 0
x : int = 0
atlag: int = 0

for i in listx:
    n += 1

for y in listx:
    x = x + y

atlag = x / n

print(atlag)

for j in listx:
    if j < atlag:
        print(j)

print("")
print("Feladat3:")
print("")

listy = list()
listy = []

for a in range(1, 91):
    listy.append(a)

for b in range(200):
    index1 = listy.index(randint(1, 90))
    index2 = listy.index(randint(1, 90))

    listy[index1], listy[index2] = listy[index2], listy[index1]

print(listy.index(1),listy.index(2),listy.index(3),listy.index(4),listy.index(5))

print("")
print("Feladat4:")
print("")

while True:
    szam21: int = int(input("Kérek egy 21-el osztható számot:"))
    if szam21 % 21:
        print("Nem osztható 21-el!")
        pass
    else:
        print("Köszönöm!")
        break

print("")
print("Feladat5:")
print("")

listc = list()
listc = []

kitalalt : int = 0

for c in range(1, 128):
    listc.append(c)

kitalalt = listc.index(randint(1, 127))

print("Kitaláltam egy számot, tippeljen hogy mi lehet az a szám, én pedig meg mondom hogy kisseb vagy nagyobb számra gondoltam!")

while True:
    tipp = int(input("Az ön tippje: "))

    if tipp > kitalalt:
        print("Kisebb!")
        pass

    if tipp < kitalalt:
        print("Nagyobb!")
        pass

    if tipp == kitalalt:
        print("Kitaláltad!")
        break



