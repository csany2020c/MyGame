from typing import List
from typing import TextIO

class Sator:
    def __init__(self):
        super().__init__()
        self.szin : str = "transparent"
        self.merethossz : int = 300 #cm
        self.meretszeles: int = 300 #cm
        self.elferoszemelyek : int = 1
        self.ar : int = 0
        self.szallitas: int = 0
        self.ontarto: bool = False

class Peldak:
    def __init__(self):
        self.Partysator = Sator()

        self.Partysator.szin = "Fehér"
        self.Partysator.merethossz = 300
        self.Partysator.meretszeles = 300
        self.Partysator.elferoszemelyek = 6
        self.Partysator.ar = 27990
        self.Partysator.szallitas = 1090
        self.Partysator.ontarto = False

        print(self.Partysator.szin)
        print(self.Partysator.ar,"Ft")

Peldak()