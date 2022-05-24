from typing import TextIO, List

'''
class jatek:
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = str("A játék neve: ")
        self.kidatum: int = int(0)
        self.kategoria: str = str("Minősége: AAA")
        self.ar: int = int(0)


bement = jatek()
bement.nev = str(input("A játék neve: "))
bement.kidatum = int(input("Kiadás éve: "))
bement.kategoria = str(input("Minősége: "))
bement.ar = 35
print(bement.nev, bement.kidatum, bement.kategoria, bement.ar)

bement2 = jatek()
bement2.nev = "Valorant"
bement2.kidatum = 2019
bement2.kategoria = "AA"
bement2.ar = 0
print(bement2.nev, bement2.kidatum, bement2.kategoria, bement2.ar)

bement3 = jatek()
bement3.nev = "Rocket League"
bement3.kidatum = 2015
bement3.kategoria = "AA"
bement3.ar = 0
print(bement3.nev, bement3.kidatum, bement3.kategoria, bement3.ar)


jatek()'''


class jatek:
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = str("A játék neve: ")
        self.kidatum: int = int(0)
        self.kategoria: str = str("Minősége: AAA")
        self.ar: int = int(0)

valt : bool = True
fulloslist: List['str'] = list()

while valt == True:
    bement4 = jatek()
    bement4.nev = str(input("A játék neve: "))
    bement4.kidatum = int(input("Kiadás éve: "))
    bement4.kategoria = str(input("Minősége: "))
    bement4.ar = int(input("A játék ára: "))
    fulloslist.append(bement4.nev)
    fulloslist.append(bement4.kidatum)
    fulloslist.append(bement4.kategoria)
    fulloslist.append(bement4.ar)
    new: str = str(input("Szeretne mégegy játékot felvinni?"))
    if new == "Nem":
        valt = False
        break

bement = jatek()
bement.nev = str("Escape From Tarkov")
bement.kidatum = int(2017)
bement.kategoria = str("AAA")
bement.ar = 35
fulloslist.append(bement.nev)
fulloslist.append(bement.kidatum)
fulloslist.append(bement.kategoria)
fulloslist.append(bement.ar)

bement2 = jatek()
bement2.nev = "Valorant"
bement2.kidatum = 2019
bement2.kategoria = "AA"
bement2.ar = 0
fulloslist.append(bement2.nev)
fulloslist.append(bement2.kidatum)
fulloslist.append(bement2.kategoria)
fulloslist.append(bement2.ar)

bement3 = jatek()
bement3.nev = "Rocket League"
bement3.kidatum = 2015
bement3.kategoria = "AA"
bement3.ar = 0
fulloslist.append(bement3.nev)
fulloslist.append(bement3.kidatum)
fulloslist.append(bement3.kategoria)
fulloslist.append(bement3.ar)

print(fulloslist)




jatek()
