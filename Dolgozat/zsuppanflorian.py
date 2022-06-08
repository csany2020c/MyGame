from random import randint
from typing import List

print("1.feladat")
def elso():
    e = int(input("adjon meg egy számot:"))
    b = int(input("adjon meg egy másik számot:"))
    for i in range(b + 1):
        osszeg = e * i
        if i != 0:
            print(osszeg)

elso()

print("2. feladat")
def masodik():
    nevek = []
    veg = 0
    while True:
        rand = randint(0, veg)
        nev = str(input("kérek egy nevet:"))
        if nev == "":
            break
        nevek.append(nev)
        veg = veg + 1
    print(nevek[rand])

masodik()

print("3.feladat")
class eger:
    def __init__(self) -> None:
        super().__init__()
        self.gomb : int = 0
        self.vgorgo: bool = True
        self.fgorgo: bool = False
        self.gyarto: str = " "

    def __str__(self) -> str:
        return "Gombok száma: {a}, Vizszintes görgő?: {b}, Függőleges görgő?: {c}, gyártó: {d}".format(a=self.gomb, b=self.vgorgo, c=self.fgorgo, d=self.gyarto)


egerek: List['eger'] = list()

eger1 = eger()
eger1.gomb = 4
eger1.vgorgo = False
eger1.fgorgo = True
eger1.gyarto = "Logitech"

eger2 = eger()
eger2.gomb = 10
eger2.vgorgo = False
eger2.fgorgo = True
eger2.gyarto = "Razer"

eger3 = eger()
eger3.gomb = 6
eger3.vgorgo = True
eger3.fgorgo = False
eger3.gyarto = "Trust"

egerek.append(eger1)
egerek.append(eger2)
egerek.append(eger3)

for i in egerek:
    print(i)

eger()
