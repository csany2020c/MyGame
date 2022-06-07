from typing import List
from random import randint


def elsofeladat():
    elsoszam = input()
    masodikszam = input()
    for i in range(int(masodikszam)):
        print(elsoszam * i)


def masodikfeladat():
    while True:
        nevlista: List[''] = list()
        nev = input("Írj be egy nevet: ")
        nevlista.append(nev)
        if nev == "":
            cucc = (len(nevlista))
            cucc2 = randint(1, cucc)
            print(cucc2)
            break

class harmadikfeladat():
    def __init__(self):
        super().__init__()

        self.gombokszama: int = 1
        self.vizszintesgorgo: bool
        self.fuggolegesgorgo: bool
        self.gyarto: str = ""

    def __str__(self) -> str:
        return "Gombok száma = {a}; Vízszintesgörgő = {b}; Függölegesgörgő = {c}; Gyártó neve = {d}".format(a=self.gombokszama,b=self.vizszintesgorgo,c=self.fuggolegesgorgo,d=self.gyarto)

# def boolbeiras():
#     while True:
#         asd: str = input( + "")
#         if asd == "Igen":
#             return True
#         if asd == "Nem":
#             return False
#         else:
#             break

egerlista: List['harmadikfeladat'] = list()

eger = harmadikfeladat()
eger.gombokszama = input("Hány gomb van az egeren? ")
eger.vizszintesgorgo = input("Vízszintes görgő van az egeren [Igen/Nem]? ")
eger.fuggolegesgorgo = input("Függöleges görgő van az egeren [Igen/Nem]? ")
eger.gyarto = input("Egér gyártója: ")

if eger.vizszintesgorgo == "Igen" or eger.vizszintesgorgo == "I":
    eger.vizszintesgorgo = True

if eger.vizszintesgorgo == "Nem" or eger.vizszintesgorgo == "N":
    eger.vizszintesgorgo = False

if eger.fuggolegesgorgo == "Igen" or eger.vizszintesgorgo == "I":
    eger.fuggolegesgorgo = True

if eger.fuggolegesgorgo == "Nem" or eger.vizszintesgorgo == "N":
    eger.fuggolegesgorgo = False

eger1 = harmadikfeladat()
eger1.gombokszama = 3
eger1.vizszintesgorgo = False
eger1.fuggolegesgorgo = True
eger1.gyarto = "Logitech"

eger2 = harmadikfeladat()
eger2.gombokszama = 3
eger2.vizszintesgorgo = False
eger2.fuggolegesgorgo = True
eger2.gyarto = "Apple"

eger3 = harmadikfeladat()
eger3.gombokszama = 8
eger3.vizszintesgorgo = True
eger3.fuggolegesgorgo = False
eger3.gyarto = "Hama"

egerlista.append(eger)
egerlista.append(eger1)
egerlista.append(eger2)
egerlista.append(eger3)

for i in egerlista:
    print(i)

# # elsofeladat()
# masodikfeladat()


