from typing import List
import random

class doga:

    def __init__(self) -> None:
        super().__init__()
        #self.elsofeladat()
        #self.masodikfeladat()

    def elsofeladat(self):
        print("Első feladat")
        listam: List[doga] = list()
        elsoszam: int = int(input("Kérem az első számot: "))
        masodikszam : int = int(input("Kérem a második számot: "))
        for i in range(1, masodikszam + 1):
            esloszam = elsoszam
            esloszam *= i
            listam.append(esloszam)
        print(listam)

    def masodikfeladat(self):
        print("Második feladat")
        listam: List [doga] = list()
        while True:
            nevek: str = str(input("Kérem adjon meg egy nevet: "))
            listam.append(nevek)
            if nevek == "":
                randomszam = random.randint(0, len(listam)- 1)
                print(listam[randomszam])
                return False

doga()

class egeres:

    def harmadikfeladat(self):
        def __init__(self) -> None:
            super().__init__()
            self.gombszam = 5
            self.vizszintesgorgo = "Van!"
            self.fuggolegesgorgo = "Nincs!"
            self.gyarto = "Yenkee"

        def __str__(self) -> str:
            return f"gombszam = {self.gombszam}, vizszintes = {self.vizszintesgorgo}, fuggoleges = {self.fuggolegesgorgo}, gyarto = {self.gyarto}"


elsoegerke = egeres()
elsoegerke.gombszam = 3
elsoegerke.vizszintes = "Van!"
elsoegerke.fuggoleges = "Nincs!"
elsoegerke.gyarto = "Yenkee"

elsoegerke2 = egeres()
elsoegerke2.gombszam = 5
elsoegerke2.vizszintes = "Van!"
elsoegerke2.fuggoleges = "Nincs!"
elsoegerke2.gyarto = "Logitech"

elsoegerke3 = egeres()
elsoegerke3.gombszam = 7
elsoegerke3.vizszintes = "Nincs!"
elsoegerke3.fuggoleges = "Van!"
elsoegerke3.gyarto = "Asus"


print(elsoegerke.gombszam, elsoegerke.vizszintes, elsoegerke.fuggoleges, elsoegerke.gyarto)
print(elsoegerke2.gombszam, elsoegerke2.vizszintes, elsoegerke2.fuggoleges, elsoegerke2.gyarto)
print(elsoegerke3.gombszam, elsoegerke3.vizszintes, elsoegerke3.fuggoleges, elsoegerke3.gyarto)

egeres()