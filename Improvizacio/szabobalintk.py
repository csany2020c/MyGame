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

#Peldak()

class Focista:
    def __init__(self):
        super().__init__()
        self.nev : str = "transparent"
        self.magassag : int = 0
        self.suly: int = 0
        self.ballabas: bool = False

class Peldak2:
    def __init__(self):
        self.peldafoci = Focista()

        self.peldafoci.nev = "Ronaldo Siuuu"
        self.peldafoci.magassag = 180
        self.peldafoci.suly = 70
        self.peldafoci.ballabas = True

        print(self.peldafoci.nev)
        print(self.peldafoci.ballabas)

#Peldak2()

class Majom:
    def __init__(self):
        super().__init__()
        self.eletkor: int = 0
        self.faj : str = "transparent"
        self.farokhossz: int = 10 #cm
        self.emberszabasu: bool = False



class Peldak3:
    def __init__(self):
        self.maki1 = Majom()

        self.maki1.faj = "Orángután"
        self.maki1.eletkor = 12
        self.maki1.farokhossz = 0
        self.maki1.emberszabasu = True

        print(self.maki1.faj)
        print(self.maki1.eletkor)
        print(self.maki1.emberszabasu)

        if self.maki1.farokhossz <= 10 or self.maki1.emberszabasu == True:
            print("Nincsen farka")


Peldak3()

