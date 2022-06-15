from typing import List
import random

print("1.feladat")
print("")

szam1 = int(input())
szam2 = int(input())
for i in range(1, szam2 + 1):
    szorzat = i * szam1
    print(szorzat)

print("")
print("2.feladat")
print("")

nevlista: List['str'] = list()
while True:
    nev :str = str(input("Kérek egy nevet:"))
    if nev == "":
        break
    else:
        nevlista.append(nev)
randomnev = random.randint(0, len(nevlista) - 1)
print(nevlista[randomnev])

print("")
print("3.feladat")
print("")

class Eger:
    def __init__(self):
        super.__init__()


