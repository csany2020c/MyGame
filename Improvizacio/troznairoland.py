from typing import List
from typing import TextIO

class kezilabda:

    def __init__(self):
        super().__init__()
        self.szin: str = ""
        self.meret: int = 0
        self.ar: int = 0
        self.hasznalat: str = ""
        self.megerimegvenni: bool = False

lista: List['kezilabda'] = list()

kezilabda1 = kezilabda()
kezilabda1.szin = "kék-fehér"
kezilabda1.meret = 3
kezilabda1.ar = 10000
kezilabda1.hasznalat = "haladó"
kezilabda1.megerimegvenni = True
lista.append(kezilabda1)

kezilabda2 = kezilabda()
kezilabda2.szin = "fehér"
kezilabda2.meret = 3
kezilabda2.ar = 5000
kezilabda2.hasznalat = "kezdő"
kezilabda2.megerimegvenni = False
lista.append(kezilabda2)

kezilabda3 = kezilabda()
kezilabda3.szin = "zöld-kék"
kezilabda3.meret = 3
kezilabda3.ar = 8000
kezilabda3.hasznalat = "haladó"
kezilabda3.megerimegvenni = True
lista.append(kezilabda3)

kezilabda4 = kezilabda()
kezilabda4.szin = input("A labda színe:")
kezilabda4.meret = input("A labda mérete:")
kezilabda4.ar = input("A labda ára:")
kezilabda4.hasznalat = input("Megfelelő csoport:")
kezilabda4.megerimegvenni = input("Megéri-e megvenni?:")
lista.append(kezilabda4)
print(lista)


