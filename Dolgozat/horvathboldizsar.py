from typing import *
from random import randint


def elso(a: int, b: int) -> List['int']:
    eredmeny: List['int'] = list()
    for i in range(b):
        valtozo1 = a * (i + 1)
        eredmeny.append(valtozo1)
    return eredmeny


print(elso(int(input("Kérlek add meg az első számot: ")), int(input("Kérlek add meg a második számot: "))))


def masodik():
    nevek: List['str'] = list()
    while True:
        bemenet = input("Írj be egy nevet: ")
        try:
            if bemenet != " " or bemenet != "":
                nevek.append(bemenet)
                pass
            if bemenet == " " or bemenet == "":
                if len(nevek) > 1:
                    print("Random név: " + nevek[randint(0, len(nevek))])
                return True
        finally:
            pass


masodik()


class Harmadik:
    def __init__(self):
        self.gombokszama: int = int(0)
        self.vizszintesgorgo: bool = False
        self.fuggolegesgorgo: bool = False
        self.gyarto: str = str("Gyártó: ")

    def __str__(self) -> str:
        return f"Gombokszáma: {self.gombokszama}, " \
               f"Vízszintes görgő: {self.vizszintesgorgo}," \
               f" Függőleges görgő: {self.fuggolegesgorgo}," \
               f" Gyártó: {self.gyarto}"


eger1 = Harmadik()
eger1.gombokszama = 3
eger1.vizszintesgorgo = True
eger1.fuggolegesgorgo = False
eger1.gyarto = "Genius"

eger2 = Harmadik()
eger2.gombokszama = 8
eger2.vizszintesgorgo = True
eger2.fuggolegesgorgo = False
eger2.gyarto = "Logitech"

eger3 = Harmadik()
eger3.gombokszama = 4
eger3.vizszintesgorgo = False
eger3.fuggolegesgorgo = True
eger3.gyarto = "Razer"

lista: List['Harmadik'] = list()
lista.append(eger1)
lista.append(eger2)
lista.append(eger3)

for x in range(len(lista)):
    print(lista[x])
