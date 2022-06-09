import random
from typing import TextIO
from typing import List


class Egerek:
    def __init__(self):
        super().__init__()
        self.gombok: int = 3
        self.vizszintesgorgo: bool = True
        self.fuggolegesgorgo: bool = True
        self.gyarto: str = "Genius"


class Dolgozat:
    def __init__(self) -> None:
        super().__init__()
        number: int = int(input("Kérek egy számot!"))
        length: int = int(input("Kérek még egy számot!"))
        for i in range(length):
            print(number * (i + 1))

        neveklista: List = list()
        whiletrue = True
        while whiletrue:
            bemenet = input("Kérek egy nevet!")
            if bemenet != "":
                neveklista.append(bemenet)
            if bemenet == "":
                whiletrue = False
        print("random nev: " + neveklista[random.randint(0, len(neveklista) - 1)])

        egereklista: List = list()

        eger1 = Egerek()
        eger1.gombok = 5
        eger1.fuggolegesgorgo = True
        eger1.vizszintesgorgo = True
        eger1.gyarto = "Logitech"
        eger2 = Egerek()
        eger2.gombok = 3
        eger2.fuggolegesgorgo = True
        eger2.vizszintesgorgo = False
        eger2.gyarto = "Asus"
        eger3 = Egerek()
        eger3.gombok = 2
        eger3.fuggolegesgorgo = False
        eger3.vizszintesgorgo = False
        eger3.gyarto = "Tesco"

        egereklista.append(eger1)
        egereklista.append(eger2)
        egereklista.append(eger3)

        for i in range(len(egereklista)):
            print(egereklista[i].gombok)
            print(egereklista[i].fuggolegesgorgo)
            print(egereklista[i].vizszintesgorgo)
            print(egereklista[i].gyarto)


Dolgozat()
