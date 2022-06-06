from typing import TextIO, List
'''
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
    new: str = str(input("Szeretne még egy játékot felvinni?(Igen/Nem)"))
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

jatek()'''

class halak:

    def __init__(self) -> None:
        super().__init__()
        self.beirte: bool = False
        with open('ncshalak.txt', 'r') as befile:
            self.beolvasott = befile.read()
        if self.beolvasott == '':
            print("Nincs eltárolt adat.")
        else:
            print(self.beolvasott)
        self.save: bool
        self.haltipus:str = str(input("A hal típusa: "))
        self.haltomege: float = int(input("A hal tömege: "))
        self.horgaszneve:str = str(input("A horgász neve: "))
        self.csali:str = str(input("A csali típusa: "))
        self.to:str = str(input("A tó neve: "))
        self.osszefoglalo = f"{self.haltipus},{self.haltomege},{self.horgaszneve},{self.csali},{self.to},"
        self.save: str = str(input("Szeretnéd elmenteni az adatokat?(igen/nem)"))
        if self.save == "igen" or self.save == "Igen" or self.save == "IGEN":
            print(self.osszefoglalo)
            self.filebairas()
            self.save = True
        if self.save == "nem" or self.save == "Nem" or self.save == "NEM":
            self.save = False
            print("Az adatok nem lettek keltárolva!")
        self.kerdes: str = str(input("Szeretne még egy adatok bekérni?(igen/nem)"))
        if self.kerdes == "nem" or self.kerdes == "Nem" or self.kerdes == "NEM":
            self.filebairas()
            print("Nem szeretne több adatot bekérni.")
        if self.kerdes == "igen" or self.kerdes == "Igen" or self.kerdes == "IGEN":
            halak()

    def filebairas(self):
        with open('ncshalak.txt', 'w') as file:
            if self.save == True and self.beolvasott == '' and self.beirte == False:
                file.write(f"{self.osszefoglalo}")
                self.beirte = True
            if self.save == True and self.beirte != True:
                file.write(f"{self.beolvasott}\n{self.osszefoglalo}")
            if self.save == False:
                file.write(str(f"\n{self.beolvasott}"))

halak()