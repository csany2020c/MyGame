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

    def __str__(self) -> str:
        return "Szín = {a}, Szélesség = {b}, Hosszúság = {c}, Elférő személyek = {d}, Ár = {e}, Szállítási díj = {f}, Öntartó = {g}".format(a = self.szin, b = self.meretszeles, c = self.merethossz, d = self.elferoszemelyek, e = self. ar, f = self.szallitas, g = self.ontarto)

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

        print("Sátrak:    ",self.Partysator)

class Focista:
    def __init__(self):
        super().__init__()
        self.nev : str = "transparent"
        self.magassag : int = 0
        self.suly: int = 0
        self.ballabas: bool = False

    def __str__(self) -> str:
        return "{a}, Magassag = {b}, Suly = {c}, Ballabas = {d}".format(a = self.nev, b = self.magassag, c = self.suly, d = self.ballabas)

class Peldak2:
    def __init__(self):
        self.peldafoci = Focista()

        self.peldafoci.nev = "Ronaldo Siuuu"
        self.peldafoci.magassag = 180
        self.peldafoci.suly = 70
        self.peldafoci.ballabas = True

        print("Focisták:  ",self.peldafoci)

class Majom:
    def __init__(self):
        super().__init__()
        self.eletkor: int = 0
        self.faj : str = "transparent"
        self.farokhossz: int = 10 #cm
        self.emberszabasu: bool = False

    def __str__(self) -> str:
        return "{b}, Életkor = {a}, Farokhossz = {c}, Emberszabásu = {d}".format(a = self.eletkor, b = self.faj, c = self.farokhossz, d = self.emberszabasu)



class Peldak3:
    def __init__(self):
        #majmoca = str(input("Ide a majmot ---> "))


        self.maki1 = Majom()
        self.maki2 = Majom()
        self.maki3 = Majom()
        self.maki4 = Majom()

        self.maki1.faj = "Orángután"
        self.maki1.eletkor = 12
        self.maki1.farokhossz = 0
        self.maki1.emberszabasu = True

        self.maki2.faj = "Gyurusfarku"
        self.maki2.eletkor = 7
        self.maki2.farokhossz = 30
        self.maki2.emberszabasu = False

        self.maki3.faj = "Selyemmajom"
        self.maki3.eletkor = 2
        self.maki3.farokhossz = 15
        self.maki3.emberszabasu = False

        #self.maki4.faj = "Gorilla"
        #self.maki4.eletkor = 40
        #self.maki4.farokhossz = 2
        #self.maki4.emberszabasu = True

        self.maki4.faj = str(input("Az új majom fajtája: "))
        self.maki4.eletkor = int(input("Az új majom életkora: "))
        self.maki4.farokhossz = int(input("Az új majom farkának a hossza (cm): "))
        emberszabasu = input("Az új majom emberszabású -e (I/N)?: ")

        if emberszabasu == "I":
            self.maki4.emberszabasu = True
        return

        #print(self.maki4)

        print("Majmok:    ", self.maki1,"|", self.maki2, "|", self.maki3, "|", self.maki4)
        #if majmoca == "Orángután":
            #print(self.maki1)
        #if majmoca == "Gyűrűsfarkú":
            #print(self.maki2)
        #if majmoca == "Selyemmajom":
            #print(self.maki3)
        #if majmoca == "Gorilla":
            #print(self.maki4)


Peldak()
print("|-----------------------------------------------------|")
Peldak2()
print("|-----------------------------------------------------|")
Peldak3()