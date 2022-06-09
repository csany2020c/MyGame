from typing import List

print("Első feladat:", '\n')

szam1 : int = int(input("Első szám: "))
szam2: int = int(input("Második szám: "))

if szam1 > 0 or szam2 > 0:
    for i in range(0, min(szam1, szam2) + 1):
        print(i)

if szam1 < 0 or szam2 < 0:
    for i in range(0, max(szam1, szam2), -1):
        print(i)

if  szam1 < 0 and szam2 > 0:
    for i in range(0, min(szam1, szam2), -1):
        print(i)

if  szam1 > 0 and szam2 < 0:
    for i in range(0, min(szam1, szam2), -1):
        print(i)
print('\n')
print("Második feladat: ")

listax: List['int'] = list()
listax = []

while True:
    szam3: int = int(input("Kérek egy nem negatív számot: "))
    try:
        if szam3 >= 0:
            listax.append(szam3)
            print(listax)

        if szam3 <= 0:
            break

    finally:
        pass

print('\n')
print("A lista első és utolsó eleme: ", listax[0], listax[len(listax) - 1], '\n')

print("Harmadik feladat: ", '\n')

class Bevasarlolista():

    def __init__(self) -> None:
        super().__init__()
        self.nev : str = ""
        self.ar : int = 0
        self.tomeg : int = 0

listy = list()
listy = []

termek1 = Bevasarlolista()
termek1.nev = "Akvárium"
termek1.ar = 15000
termek1.tomeg = 30
listy.append(termek1)

termek2 = Bevasarlolista()
termek2.nev = "Doboz"
termek2.ar = 5000
termek2.tomeg = 20
listy.append(termek2)

termek3 = Bevasarlolista()
termek3.nev = "Táska"
termek3.ar = 20000
termek3.tomeg = 15
listy.append(termek3)

teljesosszeg: int = 0

for i in listy:
    teljesosszeg = teljesosszeg + i.ar

print(teljesosszeg)























