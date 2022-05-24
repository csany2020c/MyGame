from typing import TextIO, List

class jatek:
    def __init__(self) -> None:
        super().__init__()
        self.nev: str = str("A játék neve: ")
        self.kidatum: int = int(0)
        self.kategoria: str = str("Minősége: AAA")
        self.ar: int = int(0)

valt : bool = True
fulloslist: List["jatek"] = list()

while valt == True:
    bement4 = jatek()
    bement4.nev = str(input("A játék neve: "))
    bement4.kidatum = int(input("Kiadás éve: "))
    bement4.kategoria = str(input("Minősége: "))
    bement4.ar = int(input("A játék ára: "))
    append4 = f"{bement4.nev} {bement4.kidatum} {bement4.kategoria} {bement4.ar}"
    fulloslist.append(append4)
    new: str = str(input("Szeretne mégegy játékot felvinni?(Igen/Nem)"))
    if new == "Nem":
        valt = False
        break

bement = jatek()
bement.nev = str("Escape From Tarkov")
bement.kidatum = int(2017)
bement.kategoria = str("AAA")
bement.ar = 35
append = f"{bement.nev} {bement.kidatum} {bement.kategoria} {bement.ar}"
fulloslist.append(append)

bement2 = jatek()
bement2.nev = "Valorant"
bement2.kidatum = 2019
bement2.kategoria = "AA"
bement2.ar = 0
append2 = f"{bement2.nev} {bement2.kidatum} {bement2.kategoria} {bement2.ar}"
fulloslist.append(append2)

bement3 = jatek()
bement3.nev = "Rocket League"
bement3.kidatum = 2015
bement3.kategoria = "AA"
bement3.ar = 0
append3 = f"{bement3.nev} {bement3.kidatum} {bement3.kategoria} {bement3.ar}"
fulloslist.append(append3)

print(fulloslist)

jatek()
