from typing import List

class versenyzo():
    def __init__(self):
        self.gyozelmek: int = 11
        self.veresegek: int = 0
        self.dontetlen: int = 0
        self.sulycsoport: str = "welterweight"
        self.cim: str = ""
        self.ko: bool

    def __str__(self) -> str:
        return  "gyozelmek = {a}; veresegek = {b}; dontetlen = {c}; sulycsoport = {d}; cim = {e}; ko = {f}".format(a = self.gyozelmek, b = self.veresegek, c = self.dontetlen, d = self.sulycsoport, e = self.cim, f = self.ko)

khamzat = versenyzo()
khamzat.gyozelmek = 11
khamzat.veresegek = 0
khamzat.dontetlen = 0
khamzat.sulycsoport = "welterweight"
khamzat.ko = False

islam = versenyzo()
islam.gyozelmek = 22
islam.veresegek = 1
islam.dontetlen = 0
islam.sulycsoport = "lightweight"
islam.ko = False

glover = versenyzo()
glover.gyozelmek = 33
glover.veresegek = 7
glover.dontetlen = 0
glover.sulycsoport = "light heavyweight"
glover.cim = "címvédő"
glover.ko = False

francis = versenyzo()
francis.gyozelmek = 17
francis.veresegek = 3
francis.dontetlen = 0
francis.sulycsoport = "heavyweight"
francis.cim = "címvédő"
francis.ko = False

khamzat.gyozelmek = input("Hány győzelme van:")
khamzat.veresegek = input("Hány veresége van:")
khamzat.dontetlen = input("Hány döntetlenje van:")
khamzat.sulycsoport = input("Milyen súlycsoport:")
khamzat.cim = input("Mi a címe:")

lista:List['versenyzo'] = list()
lista.append(islam)
lista.append(glover)
lista.append(francis)

for i in lista:
    print(i)






