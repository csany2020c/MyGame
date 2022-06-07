from random import randint
from typing import List

class eger:

    def __init__(self):
        super().__init__()
        self.gombok: int = 0
        self.viszintesgorgo: bool = False
        self.fuggolegesgorgo: bool = False
        self.gyarto: str = ""

    # def egyesfeladat():
    #     szamok: List['int'] = list()
    #     be1: int = int(input("Kérem adja meg az első számot: "))
    #     be2: int = int(input("Kérem adja meg a második számot: "))
    #     for i in range(1, be2 + 1):
    #         osszeg = be1
    #         osszeg *= i
    #         szamok.append(osszeg)
    #     print(szamok)
    #
    # egyesfeladat()

    def kettesfeladat():
        nevek: List['str'] = list()
        while True:
            be: str = str(input("Kérem adjon meg neveket: "))
            if be == "":
                print(nevek)
                print(nevek[randint(0, len(nevek) - 1)])
                break
            else:
                nevek.append(be)
    kettesfeladat()

eger1 = eger()
eger1.gombok = 3
eger1.viszintesgorgo = True
eger1.fuggolegesgorgo = False
eger1.gyarto = "Logitech"
print(eger1.gombok)
print(eger1.viszintesgorgo)
print(eger1.fuggolegesgorgo)
print(eger1.gyarto)

eger2 = eger()
eger2.gombok = 5
eger2.viszintesgorgo = True
eger2.fuggolegesgorgo = True
eger2.gyarto = "Hyper-X"
print(eger2.gombok)
print(eger2.viszintesgorgo)
print(eger2.fuggolegesgorgo)
print(eger2.gyarto)

eger3 = eger()
eger3.gombok = 4
eger3.viszintesgorgo = False
eger3.fuggolegesgorgo = False
eger3.gyarto = "Logitech"
print(eger3.gombok)
print(eger3.viszintesgorgo)
print(eger3.fuggolegesgorgo)
print(eger3.gyarto)
